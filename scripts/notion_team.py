"""Optional Notion team setup and immutable closeout publishing. Python 3.10+."""
import argparse
import getpass
import json
import os
from pathlib import Path
import subprocess
import sys
import uuid
import urllib.request
import urllib.error

VERSION = "2025-09-03"

def rich(text):
    if not isinstance(text, str) or len(text) > 1900:
        raise ValueError("Each text field must be a string of at most 1900 characters.")
    return [{"type": "text", "text": {"content": text}}]

def schema():
    text = {"rich_text": {}}
    select = lambda names: {"select": {"options": [{"name": n} for n in names]}}
    common = {"Nombre": {"title": {}}, "ID externo": text, "Responsable": text}
    return {
        "Proyectos": {**common, "Resultado esperado": text,
            "Estado": select(["Pendiente", "En curso", "Bloqueado", "Completado"]),
            "Indicador": text, "Valor actual": {"number": {}}, "Meta": {"number": {}},
            "Fecha objetivo": {"date": {}}},
        "Tareas": {**common, "Estado": select(["Pendiente", "En curso", "Bloqueado", "Completado"]),
            "Prioridad": select(["Urgente", "Esta semana", "Después"]),
            "Siguiente paso": text, "Bloqueo": text, "Quién desbloquea": text,
            "Próximo seguimiento": {"date": {}}, "Fecha límite": {"date": {}}},
        "Actualizaciones": {**common, "Fecha": {"date": {}}, "Hecho": text,
            "Siguiente paso": text, "Bloqueo": text, "Entregable": {"url": {}}},
    }

class API:
    def __init__(self, token):
        self.token = token

    def call(self, method, path, body=None):
        request = urllib.request.Request(
            "https://api.notion.com/v1/" + path,
            data=json.dumps(body).encode("utf-8") if body is not None else None,
            headers={"Authorization": "Bearer " + self.token,
                     "Notion-Version": VERSION, "Content-Type": "application/json"},
            method=method)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            # Do not print server payloads, headers or tokens. Never blindly retry writes.
            raise RuntimeError("Notion HTTP %s. Keep the pending file; retry after checking access/rate limits." % exc.code) from None
        except (urllib.error.URLError, TimeoutError):
            raise RuntimeError("Notion connection interrupted. Remote result may exist; retry using the same IDs.") from None

def tracked_by_git(path):
    """True when Git tracks this file, so a token inside it could be committed."""
    try:
        result = subprocess.run(
            ["git", "ls-files", "--error-unmatch", path.name],
            cwd=str(path.parent), capture_output=True, text=True, timeout=10)
        return result.returncode == 0
    except (OSError, subprocess.SubprocessError):
        # No Git, or not a repository. Nothing can be committed from here.
        return False

def resolve_token(config, config_path):
    """NOTION_TOKEN first, then the token stored in .notion/config.json.

    Storing the token in the config file lets one file carry everything a
    participant needs, instead of each person editing their shell profile on a
    different operating system. The file lives under .notion/, which the kit
    gitignores, so the exposure matches a token in ~/.zshrc rather than adding
    a new one. The guard below refuses a stored token if that assumption ever
    breaks and the file becomes tracked.
    """
    token = os.environ.get("NOTION_TOKEN")
    if token:
        return token
    stored = (config or {}).get("token")
    if stored:
        if tracked_by_git(config_path):
            raise ValueError(
                "%s is tracked by Git and holds a token. Remove it from version control "
                "before relying on a stored token." % config_path)
        return stored
    if sys.stdin.isatty():
        return getpass.getpass("Notion token (hidden): ")
    raise ValueError(
        'No token available. Add "token" to .notion/config.json, set NOTION_TOKEN, '
        "or run interactively.")

def save(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)

def children(api, parent):
    result, cursor = [], None
    while True:
        path = "blocks/" + parent + "/children?page_size=100"
        if cursor:
            path += "&start_cursor=" + cursor
        page = api.call("GET", path)
        result.extend(page["results"])
        if not page.get("has_more"):
            return result
        cursor = page["next_cursor"]

def find_child(api, parent, kind, name):
    matches = [b["id"] for b in children(api, parent)
               if b["type"] == kind and b[kind].get("title") == name]
    if len(matches) > 1:
        raise ValueError("Multiple matching Notion children. Resolve duplicates before continuing: " + name)
    return matches[0] if matches else None

def setup(api, parent, path, token=None):
    parent = str(uuid.UUID(parent))
    config = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"parent": parent, "sources": {}}
    if config["parent"] != parent:
        raise ValueError("Existing configuration belongs to a different parent.")
    home = config.get("home") or find_child(api, parent, "child_page", "Tamarindos — Equipo")
    if not home:
        home = api.call("POST", "pages", {
            "parent": {"type": "page_id", "page_id": parent},
            "properties": {"title": {"title": rich("Tamarindos — Equipo")}},
            "children": [{"object": "block", "type": "paragraph", "paragraph": {
                "rich_text": rich("Revisar prioridades, responsables y bloqueos. Cada tarea tiene un responsable y un siguiente paso. Las actualizaciones conservan el trabajo realizado.")}}]
        })["id"]
    config["home"] = home
    save(path, config)
    for name, properties in schema().items():
        if name in config["sources"]:
            continue
        if name != "Proyectos":
            properties["Proyecto"] = {"relation": {
                "data_source_id": config["sources"]["Proyectos"],
                "single_property": {}}}
        database = find_child(api, home, "child_database", name)
        if database:
            result = api.call("GET", "databases/" + database)
        else:
            result = api.call("POST", "databases", {
                "parent": {"type": "page_id", "page_id": home}, "is_inline": True,
                "title": rich(name), "initial_data_source": {"properties": properties}})
        sources = result["data_sources"]
        if len(sources) != 1:
            raise ValueError("Expected exactly one data source in " + name)
        source = sources[0]["id"]
        actual = api.call("GET", "data_sources/" + source)["properties"]
        if any(key not in actual or actual[key]["type"] != next(iter(value))
               for key, value in properties.items()):
            raise ValueError("Existing database schema differs: " + name)
        config["sources"][name] = source
        save(path, config)
    # Automatic publishing begins only after successful explicit setup.
    config["auto_publish"] = True
    # Store the token so this one file is everything a participant needs. The
    # directory is gitignored; tracked_by_git() refuses to use it if that changes.
    if token and not tracked_by_git(path):
        config["token"] = token
    save(path, config)
    return config

def validate_event(event):
    uuid.UUID(event["id"])
    for key in ("title", "owner", "date", "done", "next", "blocker"):
        rich(event[key])
    if not event["owner"].strip() or not event["title"].strip():
        raise ValueError("A real owner and title are required.")
    from datetime import date
    date.fromisoformat(event["date"])
    if event.get("project_page"):
        uuid.UUID(event["project_page"])
    if event.get("deliverable") and not event["deliverable"].startswith("https://"):
        raise ValueError("Deliverable must be a shared HTTPS link.")

def publish(api, config, event):
    validate_event(event)
    source = config["sources"]["Actualizaciones"]
    found = api.call("POST", "data_sources/" + source + "/query", {
        "filter": {"property": "ID externo", "rich_text": {"equals": event["id"]}}})["results"]
    if len(found) > 1:
        raise ValueError("Duplicate external ID in Notion; resolve before retrying.")
    if found:
        return found[0]["id"]
    properties = {
        "Nombre": {"title": rich(event["title"])},
        "ID externo": {"rich_text": rich(event["id"])},
        "Responsable": {"rich_text": rich(event["owner"])},
        "Fecha": {"date": {"start": event["date"]}},
        "Hecho": {"rich_text": rich(event["done"])},
        "Siguiente paso": {"rich_text": rich(event["next"])},
        "Bloqueo": {"rich_text": rich(event["blocker"])},
    }
    if event.get("project_page"):
        properties["Proyecto"] = {"relation": [{"id": event["project_page"]}]}
    if event.get("deliverable"):
        properties["Entregable"] = {"url": event["deliverable"]}
    return api.call("POST", "pages", {
        "parent": {"type": "data_source_id", "data_source_id": source},
        "properties": properties})["id"]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("plan")
    create = commands.add_parser("setup")
    create.add_argument("--parent", required=True, help="Parent page UUID (not URL)")
    send = commands.add_parser("publish")
    send.add_argument("event", type=Path)
    args = parser.parse_args()
    if args.command == "plan":
        print(json.dumps(schema(), ensure_ascii=False, indent=2))
        return
    config_path = args.root / ".notion" / "config.json"
    config = None
    if args.command == "publish":
        config = json.loads(config_path.read_text(encoding="utf-8"))
        event = json.loads(args.event.read_text(encoding="utf-8"))
        validate_event(event)
    token = resolve_token(config, config_path)
    api = API(token)
    if args.command == "setup":
        config = setup(api, args.parent, config_path, token)
        print("https://www.notion.so/" + config["home"].replace("-", ""))
    else:
        page = publish(api, config, event)
        save(args.event.with_suffix(".receipt.json"), {"event": event["id"], "notion_page": page})
        print("Published: https://www.notion.so/" + page.replace("-", ""))

if __name__ == "__main__":
    try:
        main()
    except (ValueError, KeyError, OSError, RuntimeError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
