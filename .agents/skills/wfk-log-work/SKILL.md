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

Publish to the shared Notion workspace in the same turn, as part of logging, not
as a separate request. Read `<root>/.notion/config.json`: if it is missing or
`auto_publish` is not true, skip silently and do not mention Notion. If it is
configured, follow `<root>/scripts/NOTION-WORKFLOW.md` exactly. Build one event
per project logged, not one per session. Set `project_path` to each project's
vault-relative folder and `project_name` to its readable name; the script finds or
creates the matching Notion project page from that path, so work lands under a real
project rather than "Sin proyecto", and identity is the path so a rename never
duplicates. A project whose folder you genuinely cannot determine is still its own
event with `project_path` omitted and the relation reported pending; never invent a
path or a UUID. Work with no identifiable project is a single event with no relation.
Write each event to `.notion/outbox/<UUID>.json`
before any network call, then run `python scripts/notion_team.py publish` once per
event. Report each project's real Notion URL. If any event fails, name which
projects published and which stay pending, and call the run partial. Never present
a local save as a publication, and never print a token.

Read `<root>/05_System/Workflows/REF - Project Lifecycle.md` and apply its relevant stage rules.
Use the narrowest subproject PJL and qualified links where necessary. For 10+ tasks or a multi-phase sprint, write a WL and link DN -> PJL -> WL. Keep the DN at three outcome bullets per project, one bold key outcome; detailed technical evidence stays in PJL/WL.
