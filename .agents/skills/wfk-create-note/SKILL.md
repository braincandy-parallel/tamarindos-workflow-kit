---
name: wfk-create-note
description: >-
  Create or update meeting notes, reports, specs, plans and pickups. Use for "minuta", "reporte", "especificación", "plan", "crear nota", or MN/RE/EB/SPC/PL/PLN/PIC/PD/SD/DD/SO.
---

# WFK create-note

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/create-note/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Read the canonical lookup and the selected templates/<TYPE>.md plus references
it requires for the actual document. Supported types: MN, RE, EB, SPC, PL (alias
PLN), PIC, PD, SD, DD and SO. FD/CAM lack packaged templates; do not claim support.
Use the portable policy for tools, paths, optional services and writes.
- Work from supplied meeting notes without a redundant interview. Retain exact
  facts, decisions and owners. Link the MN in today's DN under Meetings/Calls,
  creating the DN when needed with date created, tags, category and Worked on.
- For specs, choose brief for a small task; user-specified scope wins. State the
  tier and ask only if essential scope information is missing.
- For PL/PLN, require a real source spec or an explicit request to plan directly
  from supplied scope. If no spec exists, record source as the user's request,
  never a broken wikilink. Missing optional oracle/review service does not block.
- For PIC, search existing open work first and merge matching context. Its
  completed-work/PJL gate applies only when completed work exists; an initial
  onboarding or future-task PIC can say no work has been completed.
- For EB, link the actual underlying report; if no source exists, ask for it.
- Do not auto-start reviews, implementation, external tickets or skill retirement
  after note creation. Link/log only the documented task-related outcome.
Retain canonical section structure and technical headings; write prose in Spanish.
Read the output back and verify references and any requested follow-up links.
