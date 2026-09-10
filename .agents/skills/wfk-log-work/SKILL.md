---
name: wfk-log-work
description: >-
  Record completed work in the project log and daily note. Use for "registra el avance", "anota lo que hicimos", "log work"; not future plans alone.
---

# WFK log-work

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/log-work/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Follow canonical two-layer logging using local path resolution.
Use the current conversation and supplied facts, not Claude JSONL or remote
systems. Distinguish user-reported physical work from tool-verified digital work.
Find/create one PJL for the project, or 01_Notes/Project Logs for cross-project
work, with category Project Log. Find/create today's DN with category Daily Note
and headings Meetings/Calls and Worked on. Both use local date and frontmatter.
Read existing entries and merge by project/topic; repeating the same request
must not duplicate the same event. Write the detailed PJL entry first, then
a brief DN summary linked to it. Verify both. Never imply deployment or Git
backup merely because files were saved. Do not create a WL unless warranted.

Read `<root>/05_System/Workflows/REF - Project Lifecycle.md` and apply its relevant stage rules.
Use the narrowest subproject PJL and qualified links where necessary. For 10+ tasks or a multi-phase sprint, write a WL and link DN -> PJL -> WL. Keep the DN at three outcome bullets per project, one bold key outcome; detailed technical evidence stays in PJL/WL.
