---
name: wfk-pickup
description: >-
  Find and resume saved work. Use for "retomar", "qué pendientes tengo", "continuar mañana" when asking to resume, or an existing PIC; not session closeout.
---

# WFK pickup

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/pickup/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Use canonical triage criteria with local PIC discovery instead of Claude session
claims, PM integrations or worktree claiming.
1. Search 01_Notes and 02_Projects recursively for PIC - *.md. Read frontmatter
   and include open or picked-up items; exclude closed/done and templates.
2. Present a short prioritized list grounded in the files. If the user named a
   workstream, read its PIC, linked files, project instructions and relevant PJL.
3. Explain next steps and blockers. Listing/resuming context alone is read-only.
4. If the user also requests execution, carry out that authorized task and
   update only its progress. Never claim ownership through a hidden lock.
No PICs is a valid empty state. Offer a real first task; do not invent backlog.

Read `<root>/05_System/Workflows/REF - Project Lifecycle.md` and apply its relevant stage rules.
Within an authorized continue/resume request, load the linked SPC, review, plan, PJL and PIC and route to the next dependency-ready stage via wfk-project. A request only to list/triage remains read-only; do not claim or execute work from an informational request.
