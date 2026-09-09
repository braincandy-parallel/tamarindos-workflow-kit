---
name: wfk-implement
description: >-
  Execute a supplied plan and verify outcomes. Use for "implementa el plan", "ejecuta esta fase", or continuing authorized implementation; not drafting a plan.
---

# WFK implement

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/implement/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Read the actual plan, source spec and project context. Apply canonical task
tracking and acceptance criteria with sequential local execution. Do not run
Claude team APIs, automatic deployments, mandatory session commits or cleanup.
Choose the next task whose dependencies are satisfied. Carry out authorized
work, verify its acceptance criteria, then update task status and completed/total
tracking in the plan. Log relevant outcomes via wfk-log-work.
For physical restaurant tasks, prepare instructions/checklists and record the
human's reported completion; do not mark physical work done because a document
was written. Stop at a genuine blocker and preserve next steps. External actions
and Git publication require task authorization, not merely a plan mentioning them.
