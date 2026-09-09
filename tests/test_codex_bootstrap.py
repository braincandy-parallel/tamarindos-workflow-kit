"""Portable onboarding behavior tests; synthetic workspaces only."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "bootstrap", ROOT / ".agents/skills/wfk-setup/scripts/bootstrap.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="tamarindos-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "Espacio con acentos y espacios"
        skill = self.root / ".agents/skills/wfk-setup/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("fixture", encoding="utf-8")

    def run_setup(self, **overrides):
        args = dict(root=self.root, name="María", role="Servicio",
                    priority="Organizar acuerdos", today="2026-09-09")
        args.update(overrides)
        return MODULE.bootstrap(**args)

    def snapshot(self):
        return {p.relative_to(self.root).as_posix(): p.read_bytes()
                for p in self.root.rglob("*") if p.is_file()}

    def test_fresh_workspace_has_resumable_context(self):
        result = self.run_setup()
        self.assertEqual(len(result["created"]), 8)
        config = json.loads((self.root / "workflow-kit.config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["user_name"], "María")
        self.assertEqual(config["language"], "es")
        self.assertNotIn(str(self.root), json.dumps(config))
        pic = next(self.root.rglob("PIC - *.md")).read_text(encoding="utf-8")
        self.assertIn("Organizar acuerdos", pic)
        self.assertIn("status: open", pic)
        self.assertIn("[[PJL - Tamarindos]]", pic)
        self.assertTrue((self.root / "02_Projects/tamarindos/PJL - Tamarindos.md").is_file())

    def test_repeat_preserves_user_edits_and_profile(self):
        self.run_setup()
        dn = self.root / "01_Notes/Daily/DN - 2026-09-09.md"
        dn.write_text(dn.read_text(encoding="utf-8") + "\nDato del usuario.\n", encoding="utf-8")
        before = self.snapshot()
        result = self.run_setup(name="Otro", role="Otra", priority="No sustituir", project="otro")
        self.assertEqual(result["created"], [])
        self.assertEqual(self.snapshot(), before)

    def test_repair_creates_only_missing_files(self):
        self.run_setup()
        lessons = self.root / "02_Projects/tamarindos/lessons.md"
        lessons.unlink()
        before = self.snapshot()
        result = self.run_setup()
        self.assertEqual(result["created"], ["02_Projects/tamarindos/lessons.md"])
        for path, data in before.items():
            self.assertEqual((self.root / path).read_bytes(), data)

    def test_invalid_project_does_not_write(self):
        before = self.snapshot()
        for project in ("../outside", "con", "a/b", "a\\b", "a" * 65):
            with self.assertRaises(ValueError):
                self.run_setup(project=project)
            self.assertEqual(before, self.snapshot())

    def test_conflicting_parent_is_detected_before_config_write(self):
        (self.root / "02_Projects").write_text("existing file", encoding="utf-8")
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertEqual(before, self.snapshot())

    def test_malformed_existing_config_is_preserved(self):
        config = self.root / "workflow-kit.config.json"
        config.write_text("{invalid", encoding="utf-8")
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.run_setup()
        self.assertEqual(before, self.snapshot())

    def test_moved_workspace_uses_new_location(self):
        self.run_setup()
        destination = self.root.parent / "Moved copy"
        self.root.rename(destination)
        self.root = destination
        result = self.run_setup(today="2026-09-10")
        self.assertIn("01_Notes/Daily/DN - 2026-09-10.md", result["created"])
        self.assertFalse(any("PIC -" in p for p in result["created"]))
        self.assertTrue((destination / "01_Notes/Daily/DN - 2026-09-10.md").is_file())


if __name__ == "__main__":
    unittest.main()
