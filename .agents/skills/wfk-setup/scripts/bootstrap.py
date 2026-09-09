"""Create a portable Tamarindos workspace using only the Python standard library.

No network, package installation, global settings, or Git mutations. Existing
files are preserved. A partial run can be repeated to create remaining files.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

PATHS = {
    "daily_notes": "01_Notes/Daily",
    "meetings": "01_Notes/Meetings",
    "pickups": "01_Notes/Pickups",
    "reports": "01_Notes/Reports",
    "projects": "02_Projects",
    "operations": "03_Operations",
    "reference": "04_Reference",
    "templates": "05_System/Templates",
}
RESERVED = {"con", "prn", "aux", "nul"} | {
    prefix + str(n) for prefix in ("com", "lpt") for n in range(1, 10)
}


def slug(value):
    if not isinstance(value, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
        raise ValueError("Project must be a lowercase slug, such as tamarindos.")
    if len(value) > 64 or value in RESERVED:
        raise ValueError("Project name is too long or reserved.")
    return value


def text(value, label):
    if not isinstance(value, str) or not value.strip() or any(ord(c) < 32 for c in value):
        raise ValueError(label + " must contain nonempty single-line text.")
    return value.strip()


def fm(category, tags, today, extra=""):
    return ("---\ndate created: " + today + "\ntags: " + json.dumps(tags, ensure_ascii=False)
            + "\ncategory: " + category + "\n" + extra + "---\n\n")


def checked_target(root, relative):
    target = root / relative
    # Reject symlinks/junctions escaping or redirecting the intended tree.
    current = target
    while current != root:
        if current.is_symlink() or (hasattr(current, "is_junction") and current.is_junction()):
            raise ValueError("Linked target is not supported: " + relative)
        current = current.parent
    if not target.resolve().is_relative_to(root):
        raise ValueError("Target escapes workspace: " + relative)
    return target


def bootstrap(root, name, role, priority, project="tamarindos", today=None):
    root = Path(root).resolve(strict=True)
    if not root.is_dir() or not (root / ".agents/skills/wfk-setup/SKILL.md").is_file():
        raise ValueError("Run against a downloaded Tamarindos kit.")
    name, role, priority = (text(v, k) for v, k in
                            ((name, "Name"), (role, "Role"), (priority, "Priority")))
    project = slug(project)
    today = dt.date.fromisoformat(today).isoformat() if today else dt.date.today().isoformat()
    config_path = checked_target(root, "workflow-kit.config.json")
    existing = {}
    if config_path.exists():
        existing = json.loads(config_path.read_text(encoding="utf-8-sig"))
        if not isinstance(existing, dict):
            raise ValueError("Existing configuration must be an object.")
        name = text(existing.get("user_name", name), "Existing name")
        role = text(existing.get("role", role), "Existing role")
        priority = text(existing.get("first_priority", priority), "Existing priority")
        projects = existing.get("projects", [])
        if projects:
            if not isinstance(projects, list):
                raise ValueError("Existing projects must be a list.")
            project = slug(projects[0])
    project_dir = "02_Projects/" + project
    project_title = project.replace("-", " ").title()
    config = {
        "schema_version": 1,
        "user_name": name,
        "role": role,
        "language": "es",
        "first_priority": priority,
        "projects": [project],
        "paths": PATHS,
        "setup_date": today,
        "distribution_repo": "https://github.com/braincandy-parallel/tamarindos-workflow-kit",
    }
    preference = (fm("Reference", ["reference", "onboarding", "preferences"], today)
                  + "# Preferencias de bienvenida\n\n"
                  + "- Nombre: " + name + "\n- Función: " + role
                  + "\n- Idioma: español\n- Primera prioridad: " + priority + "\n")
    pic = (fm("Pickup", ["pickup", "onboarding", project], today,
              "status: open\nproject: " + json.dumps(project) + "\ngoal: Unaligned\n"
              + "pickup_date: " + today + "\n")
           + "# Primer pendiente\n\n## Context\n\n"
           + name + " trabaja en " + role + ". Su primera prioridad es: " + priority
           + "\n\n## What Was Done\n\n"
           + "Se preparó la estructura inicial del espacio. La tarea todavía no se ha ejecutado."
           + "\n\n## What Needs to Happen Next\n\n"
           + "1. Aclarar el resultado esperado de la primera prioridad.\n"
           + "2. Revisar la información disponible y elegir el primer paso concreto.\n"
           + "\n## Known Issues\n\nNo se han identificado problemas todavía.\n"
           + "\n## Key Files\n\n"
           + "- [[PJL - " + project_title + "]]\n"
           + "\n## Blockers or Dependencies\n\nPor determinar al revisar la tarea.\n")
    files = {
        "workflow-kit.config.json": json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        "04_Reference/REF - Onboarding Preferences.md": preference,
        "04_Reference/REF - Agent Lessons.md":
            fm("Reference", ["reference", "lessons"], today) + "# Lecciones compartidas\n",
        project_dir + "/agents.md":
            "# Contexto de " + project_title + "\n\n"
            + "- Persona: " + name + "\n- Función: " + role
            + "\n- Primera prioridad: " + priority
            + "\n- Idioma: español\n\n## Contexto para retomar\n",
        project_dir + "/lessons.md": "# Lecciones de " + project_title + "\n",
        project_dir + "/PJL - " + project_title + ".md":
            fm("Project Log", ["project-log", project], today)
            + "# Registro de " + project_title + "\n",
        "01_Notes/Daily/DN - " + today + ".md":
            fm("Daily Note", ["daily"], today) + "# " + today
            + "\n\n## TODO\n\n## Meetings/Calls\n\n## Worked on\n\n## Notes\n",
        project_dir + "/pickups/" + today + "/PIC - Primer pendiente.md": pic,
    }
    # Onboarding is a one-time workstream, even when setup runs on a later day.
    pickups = checked_target(root, project_dir + "/pickups")
    if pickups.is_dir() and any(pickups.rglob("PIC - Primer pendiente.md")):
        files.pop(project_dir + "/pickups/" + today + "/PIC - Primer pendiente.md")
    # Preflight all paths before creating anything.
    targets = {relative: checked_target(root, relative) for relative in files}
    for relative, target in targets.items():
        if target.exists() and not target.is_file():
            raise ValueError("Expected a regular file: " + relative)
        for parent in target.parents:
            if parent == root:
                break
            if parent.exists() and not parent.is_dir():
                raise ValueError("Parent is not a directory: " + relative)
    directories = list(PATHS.values()) + [
        project_dir + "/" + d for d in ("specs", "plans", "reports", "reviews", "pickups")
    ]
    for relative in directories:
        target = checked_target(root, relative)
        if target.exists() and not target.is_dir():
            raise ValueError("Expected a directory: " + relative)
    created, preserved = [], []
    for relative in directories:
        checked_target(root, relative).mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        target = targets[relative]
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            with target.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(content)
        except FileExistsError:
            preserved.append(relative)
        else:
            if target.read_text(encoding="utf-8") != content:
                raise OSError("Write verification failed: " + relative)
            created.append(relative)
    return {"created": created, "preserved": preserved, "project": project}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--name", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--priority", required=True)
    parser.add_argument("--project", default="tamarindos")
    parser.add_argument("--date", help="Override local date, YYYY-MM-DD.")
    args = parser.parse_args()
    try:
        result = bootstrap(args.root, args.name, args.role, args.priority, args.project, args.date)
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
