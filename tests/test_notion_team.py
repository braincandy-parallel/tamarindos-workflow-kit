import importlib.util
from pathlib import Path
import tempfile
import unittest
import uuid

spec = importlib.util.spec_from_file_location("notion_team", Path(__file__).resolve().parents[1] / "scripts" / "notion_team.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class FakeAPI:
    def __init__(self):
        self.pages = []
        self.calls = []
    def call(self, method, path, body=None):
        self.calls.append((method, path, body))
        if path.endswith("/query"):
            identifier = body["filter"]["rich_text"]["equals"]
            return {"results": [p for p in self.pages if p["properties"]["ID externo"]["rich_text"][0]["text"]["content"] == identifier]}
        if path == "pages":
            page = {"id": str(uuid.uuid4()), **body}
            self.pages.append(page)
            return page
        raise AssertionError(path)

class NotionTests(unittest.TestCase):
    def event(self):
        return dict(id=str(uuid.uuid4()), title="Avance de prueba", owner="Persona de prueba",
                    date="2026-09-09", done="Trabajo de prueba", next="Revisar", blocker="")
    def test_retry_reuses_remote_record(self):
        api = FakeAPI()
        config = {"sources": {"Actualizaciones": "source"}}
        event = self.event()
        first = module.publish(api, config, event)
        self.assertEqual(first, module.publish(api, config, event))
        self.assertEqual(len(api.pages), 1)
    def test_invalid_event_never_contacts_notion(self):
        api = FakeAPI()
        for field, value in [("id", "../oops"), ("owner", ""), ("date", "yesterday"),
                             ("done", "x" * 2000), ("deliverable", "file:///private")]:
            event = self.event()
            event[field] = value
            with self.assertRaises(ValueError):
                module.publish(api, {"sources": {"Actualizaciones": "source"}}, event)
        self.assertEqual(api.calls, [])
    def test_does_not_mutate_task_status(self):
        api = FakeAPI()
        module.publish(api, {"sources": {"Actualizaciones": "source"}}, self.event())
        self.assertNotIn("Estado", api.pages[0]["properties"])
        self.assertTrue(all(call[0] == "POST" for call in api.calls))
    def test_duplicate_id_stops(self):
        api = FakeAPI()
        event = self.event()
        config = {"sources": {"Actualizaciones": "source"}}
        module.publish(api, config, event)
        api.pages.append(api.pages[0].copy())
        with self.assertRaises(ValueError):
            module.publish(api, config, event)
    def test_receipt_atomic_save(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "nested" / "receipt.json"
            module.save(path, {"id": "test"})
            self.assertTrue(path.exists())
            self.assertFalse(path.with_suffix(".tmp").exists())
    def test_schema_tracks_bottlenecks(self):
        schema = module.schema()
        self.assertEqual(set(schema), {"Proyectos", "Tareas", "Actualizaciones"})
        self.assertTrue({"Responsable", "Bloqueo", "Quién desbloquea", "Próximo seguimiento"} <= set(schema["Tareas"]))


    def test_setup_reuses_home_and_databases_after_lost_config(self):
        class SetupAPI:
            def __init__(self):
                self.blocks = {}
                self.databases = {}
                self.sources = {}
                self.writes = 0
            def call(self, method, path, body=None):
                if path.startswith("blocks/"):
                    parent = path.split("/")[1]
                    return {"results": self.blocks.get(parent, []), "has_more": False}
                if method == "POST":
                    self.writes += 1
                    identifier = str(uuid.uuid4())
                    parent = body["parent"]["page_id"]
                    if path == "pages":
                        self.blocks.setdefault(parent, []).append({
                            "id": identifier, "type": "child_page",
                            "child_page": {"title": body["properties"]["title"]["title"][0]["text"]["content"]}})
                        return {"id": identifier}
                    if path == "databases":
                        source = str(uuid.uuid4())
                        self.blocks.setdefault(parent, []).append({
                            "id": identifier, "type": "child_database",
                            "child_database": {"title": body["title"][0]["text"]["content"]}})
                        self.databases[identifier] = {"id": identifier, "data_sources": [{"id": source}]}
                        self.sources[source] = {"properties": {
                            key: {"type": next(iter(value))}
                            for key, value in body["initial_data_source"]["properties"].items()}}
                        return self.databases[identifier]
                if path.startswith("databases/"):
                    return self.databases[path.split("/")[1]]
                if path.startswith("data_sources/"):
                    return self.sources[path.split("/")[1]]
                raise AssertionError(path)
        with tempfile.TemporaryDirectory() as tmp:
            api = SetupAPI()
            parent = str(uuid.uuid4())
            first = module.setup(api, parent, Path(tmp) / "first.json")
            second = module.setup(api, parent, Path(tmp) / "recovered.json")
            self.assertEqual(first, second)
            self.assertEqual(api.writes, 4)

if __name__ == "__main__":
    unittest.main()
