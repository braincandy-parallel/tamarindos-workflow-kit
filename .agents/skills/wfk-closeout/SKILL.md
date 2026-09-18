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
3. Verify shared publication when `<root>/.notion/config.json` has `auto_publish`
   true. wfk-log-work owns the publish step and already ran it in step 2, one
   event per project per `<root>/scripts/NOTION-WORKFLOW.md`. Named projects
   without verified pages remain separate events with `project_page` omitted;
   report the missing relation, but treat a returned Notion URL as published.
   Genuinely projectless work is one additional event, including in a mixed
   session. Confirm a real Notion URL exists for every event, and that each event
   either landed under its project or had a missing relation reported as pending;
   silently unrelated work ends up under "Sin proyecto" in the digest. Do not publish a
   project twice: a second run builds a new event ID and duplicates the record.
   Retry only the events still pending in `.notion/outbox/`, and report per
   project. Skip this silently when publishing is not configured.
4. Update an existing matching PIC, or create one via wfk-create-note PIC, for
   each genuinely unfinished workstream. Include context, evidence, precise next
   steps, known issues, verified key files and blockers. Completed physical
   actions remain user-reported unless independently verified.
5. Preserve a supplied return date. Otherwise use tomorrow; restaurant operations
   may run on weekends, so do not skip them unless the user has that schedule.
6. Close only PICs whose completion is evidenced; leave unresolved work open.
7. Verify the saved logs/PICs and report paths and the next action. State local
   saves and shared publication as separate claims.
If the session failed, preserve failures and recovery instructions explicitly;
do not transform a failed attempt into a success summary. Repeating closeout
merges the same workstream rather than creating another PIC.

Read `<root>/05_System/Workflows/REF - Project Lifecycle.md` and apply its relevant stage rules.
Follow the shared lifecycle closeout checklist. Reconcile the active plan first; then log and update/create the matching PIC if the plan lacks continuation context. Distinguish session saved from project complete. Project completion requires all tasks and acceptance evidence; do not close the project merely because setup succeeded.
