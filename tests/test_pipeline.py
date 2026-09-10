"""Regression tests for project stage gates, including failed/premature transitions."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("pipeline_gate", ROOT / "scripts/pipeline_gate.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)

class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.spec = self.root / "specs/2026-09-09/SPC - Example.md"
        self.review = self.root / "reviews/2026-09-09/ARE - Example.md"
        self.plan = self.root / "plans/2026-09-09/PL - Example.md"
        for path in (self.spec, self.review, self.plan):
            path.parent.mkdir(parents=True)
        self.spec.write_text("---\nstatus: Ready\n---\nOutcome and scope.\n", encoding="utf-8")
        self.review.write_text('---\noutcome: ready\nsource: "[[SPC - Example]]"\n---\nReviewed.\n', encoding="utf-8")
        self.plan.write_text('---\nstatus: In Progress\nsource: "[[SPC - Example]]"\nreview: "[[ARE - Example]]"\ncompleted: 0\ntotal: 1\n---\n| ID | Task | Status |\n| --- | --- | --- |\n| T1 | Verify participant | todo |\n', encoding="utf-8")

    def run_gate(self, stage="implement"):
        return gate.check(self.spec, self.review, self.plan, stage)

    def replace(self, path, old, new):
        path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")

    def test_ready_project_can_implement(self):
        self.assertEqual(self.run_gate()["result"], "structural-pass")

    def test_unanswered_interview_stops_build(self):
        self.replace(self.spec, "Ready", "Draft")
        with self.assertRaisesRegex(ValueError, "interview"):
            self.run_gate()

    def test_missing_spec_cannot_be_replaced_by_plan(self):
        self.spec.unlink()
        with self.assertRaises(OSError):
            self.run_gate()

    def test_blocking_review_stops_build(self):
        self.replace(self.review, "outcome: ready", "outcome: changes-required")
        with self.assertRaisesRegex(ValueError, "Review"):
            self.run_gate()

    def test_wrong_source_is_rejected(self):
        self.replace(self.plan, "SPC - Example", "SPC - Another")
        with self.assertRaisesRegex(ValueError, "link"):
            self.run_gate()

    def test_counters_must_match_tasks(self):
        self.replace(self.plan, "completed: 0", "completed: 1")
        with self.assertRaisesRegex(ValueError, "counters"):
            self.run_gate()

    def test_closeout_does_not_complete_pending_onboarding(self):
        with self.assertRaisesRegex(ValueError, "unfinished"):
            self.run_gate("complete")

    def test_claimed_complete_plan_is_checked_even_at_implement(self):
        self.replace(self.plan, "In Progress", "Complete")
        with self.assertRaisesRegex(ValueError, "unfinished"):
            self.run_gate()

    def test_all_tasks_done_still_needs_acceptance(self):
        self.replace(self.plan, "| todo |", "| done |")
        self.replace(self.plan, "completed: 0", "completed: 1")
        with self.assertRaisesRegex(ValueError, "acceptance"):
            self.run_gate("complete")

    def test_completion_requires_real_evidence_file(self):
        self.replace(self.plan, "| todo |", "| done |")
        self.replace(self.plan, "completed: 0", "completed: 1\nacceptance: verified\nacceptance_evidence: ../../reports/RE - Acceptance.md")
        with self.assertRaisesRegex(ValueError, "evidence"):
            self.run_gate("complete")
        report = self.root / "reports/RE - Acceptance.md"
        report.parent.mkdir()
        report.write_text("Observed acceptance evidence.", encoding="utf-8")
        self.assertEqual(self.run_gate("complete")["done"], 1)

    def test_duplicate_task_ids_fail(self):
        self.replace(self.plan, "| T1 | Verify participant | todo |", "| T1 | First | todo |\n| T1 | Duplicate | todo |")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            self.run_gate()

    def test_nested_subproject_works(self):
        self.assertEqual(self.run_gate()["tasks"], 1)
        # Gate derives project boundary from dated plans, not a hardcoded top-level project.
        self.assertEqual(self.plan.parent.parent.parent, self.root)

    def test_entrypoints_and_stage_adapters_load_contract(self):
        for name in ("AGENTS.md", "CLAUDE.md"):
            self.assertIn("REF - Project Lifecycle.md", (ROOT / name).read_text(encoding="utf-8"))
        for name in ("project", "create-spec", "plan-spec", "implement", "closeout", "pickup", "log-work", "rollup"):
            text = (ROOT / ".agents/skills" / ("wfk-" + name) / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn("REF - Project Lifecycle.md", text)
        for name in ("create-spec", "create-plan", "plan-spec", "wfk-project", "wfk-rollup"):
            self.assertTrue((ROOT / ".claude/skills" / name / "SKILL.md").is_file())

if __name__ == "__main__":
    unittest.main()
