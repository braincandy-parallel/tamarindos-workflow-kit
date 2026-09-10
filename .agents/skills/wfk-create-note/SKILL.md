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
- For SPC, follow wfk-create-spec and the lifecycle interview. Do not bypass missing scope questions.
- For PL/PLN, follow wfk-plan-spec. Require a real spec and review; return to missing stages rather than making an unlinked plan.
- For PIC, search existing open work first and merge matching context. Its
  completed-work/PJL gate applies only when completed work exists; an initial
  onboarding or future-task PIC can say no work has been completed.
- For EB, link the actual underlying report; if no source exists, ask for it.
- A note-only request ends at the requested note. Within an authorized project lifecycle, continue the next stage per the shared contract. External actions still need task authorization.
Retain canonical section structure and technical headings; write prose in Spanish.
Read the output back and verify references and any requested follow-up links.

Read `<root>/05_System/Workflows/REF - Project Lifecycle.md` and apply its relevant stage rules.
