---
name: wfk-orient
description: >-
  Read saved workspace context and priorities. Use for "ponme al día", "orient", "comenzar sesión", or returning after compaction; does not create a new profile.
---

# WFK orient

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/orient/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Execute the canonical context-loading purpose using this sequence instead of
its machine registry, orphan/process sweep and Claude path validation.
1. Read config/profile, current project instructions and lessons.
2. Read today's SOD if present, current WRM/MRM if present, today's DN and
   relevant PJL. Distinguish stale reports from current ones.
3. Summarize documented priorities, progress, blockers and next actions.
4. If no configuration exists, explain the fresh state and route an actual
   onboarding request to wfk-setup. Do not demand nonexistent reports.
Read-only: do not rewrite timestamps, status, profiles or notes.
