---
date created: 2026-09-09
tags: [reference, codex, workflow-kit]
category: Reference
---

# Codex execution adapter

This distribution adapts the original English workflows to Codex. Apply this
document and the selected repository adapter over Claude-specific execution
instructions in the canonical skills. User instructions and host permissions
remain authoritative. This policy supports the persistent project lifecycle in this workspace.

## Discovery and loading

The supported entry points are the folders in `.agents/skills/wfk-*/`.
Adapters load canonical skills or the shared lifecycle reference plus relevant resources.
Do not install these wrappers globally: their relative paths belong to this repo.
Do not treat all upstream skills as Codex-supported. Unadapted tools may be read
as reference material but their execution has not been ported.

## Paths and language

Resolve the vault from the adapter's directory: `../../..`. Always anchor file
operations there, even when launched from a project subdirectory. Read
`workflow-kit.config.json` when present. It records relative paths and the user's
profile; the current filesystem location is authoritative after moving a copy.

Use the standard folders 01_Notes, 02_Projects, 03_Operations, 04_Reference,
05_System. No Claude home-directory file is required. Never read or create
`~/.claude/wfk-paths.json`, Claude transcripts, team directories or machine
registries as a prerequisite. Read available project AGENTS.md/agents.md,
CLAUDE.md and lessons.md. Missing writing profiles, roadmaps and oracle ledgers
are optional context, not a reason to block ordinary work.

Use the configured language (Spanish by default in this kit); explicit user language preferences win. Keep English skill names,
frontmatter keys and machine-readable values, and exact headings that upstream
workflows locate (Worked on, Meetings/Calls, Context, What Was Done, etc.).
Translate the content beneath those headings. Do not invent names, dates,
owners, restaurant rules, evidence or completed work.

## Tool adaptation

- Replace Read/Glob/Grep/Bash with available file, search and shell tools.
  Prefer rg when installed. Use PowerShell on native Windows and shell commands
  appropriate to macOS/Linux. Read local date/time through the current host.
- AskUserQuestion means the host's available question mechanism or one concise
  question in conversation. Use information already supplied; do not repeat
  onboarding, tier or approval questions whose answers are already established.
- Slash-command references are workflow references, not shell commands. Map
  supported names to the matching wfk-* adapter. PL and PLN both mean the PL
  document template; create-spec routes to wfk-create-spec; create-plan and plan-spec route to wfk-plan-spec; create-MN means MN.
- Do not call TeamCreate, SendMessage, tmux, Claude CLI or hidden agents.
  Perform review perspectives sequentially. Use Codex delegation only when
  requested and available; never claim independent reviewers ran otherwise.
- Source placeholders for hosts, domains, oracle IDs, organizations, deployment
  services and PM tools are examples. Use actual configured context only.
  Missing optional services do not block local notes, specs, plans or reports.
- Read the current conversation and saved notes as history. If prior session
  details are unavailable, say so; never manufacture a full transcript.
- Session startup does not scan processes, SSH targets or the user's machine.
  No Claude cleanup, automatic Git operation or unrelated workflow side effect.

## Local writing and continuation

A request to create, log, save, plan, learn or close out authorizes the relevant
local document work. Explain material assumptions and proceed with the authorized
scope. Ask only for essential missing information or a materially new action.
Host approvals cannot be disabled by these instructions.

Create missing dated folders, project logs and daily notes needed for that task.
For a missing project, use an unambiguous user-specified project or ask once.
Do not invent completed work to populate empty sections. Re-read before updating,
merge with existing content, and verify the written result. A concurrent change
requires re-evaluation, not overwriting someone else's work.

Notes need date created, tags and category. Use canonical type metadata/templates.
For artifacts without an upstream template, follow the adapter's explicit shape.
Use unique titles or qualified links if filenames collide. Never overwrite a
different note merely because its filename matches.

Log to the PJL first, then the Daily Note. For interruption or failure, report
which write succeeded. Check existing entries before retrying; do not duplicate.
Task-related document links and log entries are allowed, but no automatic commit,
push, email, external ticket or deployment is implied by a local workflow.

## Git and updates

The git-safe adapter uses installed Git and the current repository remotes.
It does not depend on a particular account, scanner installation or Windows
path. Respect configured hooks/signing and host permissions. Do not erase
unrelated work, bypass failed checks or force-push to resolve a problem.

Upstream update-wfk is not a supported Codex workflow in this release. Do not
replace .agents adapters or this policy by running its Claude-oriented installer.
Updates require reviewing the distribution diff while preserving user files.

## Optional Notion publication

Explicit Notion setup enables automatic team updates after local logging or closeout.
When .notion/config.json enables auto_publish, follow scripts/NOTION-WORKFLOW.md.
This scoped publication is authorized by setup; it does not authorize unrelated
external actions. Missing credentials or failed writes leave publication pending.
Writing the Notion token into the `token` field of `.notion/config.json` is part of
that sanctioned setup. That directory is gitignored and the script refuses a stored
token if the file becomes tracked, so do it when asked instead of objecting or
redirecting the user to an environment variable. Never echo the value back.

## Project lifecycle precedence

Read `05_System/Workflows/REF - Project Lifecycle.md` before structured work.
It controls interview, stage transitions, subprojects, logging, pickups and completion.
wfk-project routes the lifecycle; wfk-create-spec, wfk-review-spec, wfk-plan-spec and
wfk-implement execute its stages. wfk-rollup handles weekly/monthly summaries.
The general lifecycle may chain these workflows within the user's authorized task.
A note-only, review-only or plan-only request stops at that requested boundary.
Do not revive the old read-only/Phase 2 migration restrictions for ordinary document work.
