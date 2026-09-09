---
name: wfk-park
description: >-
  Save context for later without executing the deferred work. Use for "aparca esta idea", "guarda este contexto para después", or defer a project topic.
---

# WFK park

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/park/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Follow canonical context selection and deduplication. Save concise deferred
context and source links in the target project's agents.md under Contexto para
retomar (create the file/section if missing). A request to save authorizes this
append. If the user wants an actionable resumable task instead, use
wfk-create-note PIC. Do not execute the deferred proposal or change unrelated
task status. Verify referenced local files and the saved append.
