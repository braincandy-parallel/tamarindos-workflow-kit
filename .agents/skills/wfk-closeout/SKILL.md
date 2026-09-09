---
name: wfk-closeout
description: >-
  Save session progress and a resumable next step. Use for "cerremos", "terminamos por hoy", "guarda mi avance para mañana", or end-of-session closeout.
---

# WFK closeout

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/closeout/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Use canonical closeout content and PIC templates with this portable sequence.
1. Read current conversation, relevant PJL/DN and open PICs. Skip full Claude
   transcript retrieval, local/remote worker sweeps and automatic Git actions.
2. Log real completed work through wfk-log-work; create missing logs as needed.
   If nothing was completed, say so rather than inventing a progress entry.
3. Update an existing matching PIC, or create one via wfk-create-note PIC, for
   each genuinely unfinished workstream. Include context, evidence, precise next
   steps, known issues, verified key files and blockers. Completed physical
   actions remain user-reported unless independently verified.
4. Preserve a supplied return date. Otherwise use tomorrow; restaurant operations
   may run on weekends, so do not skip them unless the user has that schedule.
5. Close only PICs whose completion is evidenced; leave unresolved work open.
6. Verify the saved logs/PICs and report paths and the next action.
If the session failed, preserve failures and recovery instructions explicitly;
do not transform a failed attempt into a success summary. Repeating closeout
merges the same workstream rather than creating another PIC.
