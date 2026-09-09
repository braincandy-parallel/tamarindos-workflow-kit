"""Check packaged references needed by a fresh Codex download."""
from pathlib import Path
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]


class BundleTests(unittest.TestCase):
    def test_native_entrypoint_case_and_canonical_targets(self):
        names = {p.name for p in ROOT.iterdir()}
        self.assertIn("AGENTS.md", names)
        self.assertNotIn("agents.md", names)
        wrappers = list((ROOT / ".agents/skills").glob("*/SKILL.md"))
        self.assertEqual(len(wrappers), 13)
        for wrapper in wrappers:
            content = wrapper.read_text(encoding="utf-8")
            expected = wrapper.parent.name
            self.assertIn("\nname: " + expected + "\n", content)
            self.assertIn("\ndescription: >-\n", content)
            canonical = ROOT / "skills" / expected.removeprefix("wfk-") / "SKILL.md"
            self.assertTrue(canonical.is_file(), str(canonical))
            self.assertEqual(wrapper.parent.resolve().parents[2], ROOT)
        self.assertTrue((ROOT / "05_System/Workflows/REF - Codex Execution Policy.md").is_file())

    def test_supported_note_templates_ship(self):
        for kind in ("MN", "RE", "EB", "SPC", "PL", "PIC", "PD", "SD", "DD", "SO"):
            template = ROOT / "skills/create-note/templates" / (kind + ".md")
            self.assertTrue(template.is_file(), str(template))

    def test_local_document_links_resolve(self):
        for name in ("README.md", "CODEX.md", "SETUP.md", "WORKFLOW.md"):
            path = ROOT / name
            content = path.read_text(encoding="utf-8")
            headings = {re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")
                        for text in re.findall(r"^#{1,6} (.+)$", content, re.M)}
            for link in re.findall(r"\]\(([^)]+)\)", content):
                if link.startswith("#"):
                    self.assertIn(unquote(link[1:]), headings, (name, link))
                elif not link.startswith(("https://", "http://")):
                    self.assertTrue((path.parent / unquote(link.split("#")[0])).exists(),
                                    (name, link))

    def test_adapter_package_has_no_personal_machine_paths(self):
        paths = list((ROOT / ".agents").rglob("*.md"))
        paths += list((ROOT / ".agents").rglob("*.py"))
        for path in paths:
            content = path.read_text(encoding="utf-8")
            self.assertNotRegex(content, r"(?i)[a-z]:[/\\]Users[/\\]")
            self.assertNotIn("braincandy-parallel/workflow-kit.git", content)
            self.assertNotIn("C:/Program Files/Git", content)


if __name__ == "__main__":
    unittest.main()
