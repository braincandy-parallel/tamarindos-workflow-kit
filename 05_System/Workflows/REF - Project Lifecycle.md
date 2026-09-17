---
date created: 2026-09-09
tags: [reference, workflow-kit, lifecycle]
category: Reference
---
# Project lifecycle contract

Shared by Claude Code and Codex. This is the required workflow for structured project work, including business processes, operations, research deliverables and software. Apply it over conflicting lifecycle/automatic-continuation instructions in older canonical skills. Host restrictions and the user's current instructions remain authoritative. Host-specific execution policy adapts tools, not this lifecycle.

## Enter through the project, not through implementation

On a new project request ("I want to build...", "set up a system...", "quiero crear...", "organicemos...", "nuevo proyecto"), inspect the relevant saved context before acting. For an existing project, read its agents.md, lessons.md, active SPC, review, PL and recent PJL; load only relevant domain references/inventories/decisions. A root AGENTS.md/CLAUDE.md is session priming, not a replacement for domain context. Do not act on guessed infrastructure.

Find the narrowest existing workstream. A subproject stays inside its parent:
02_Projects/<parent>/<subproject>/. Ask which business only if the distinction cannot be inferred. Never create a new root project for work already belonging to a parent.

Create only the missing project structure needed for the authorized work: specs/YYYY-MM-DD/, plans/YYYY-MM-DD/, reports/YYYY-MM-DD/, reviews/YYYY-MM-DD/, agents.md, lessons.md and PJL - <Project>.md. Add pickups/YYYY-MM-DD/ for PICs and work-logs/ for substantial WLs when needed. Link the subproject from the parent's agents.md and log. Never move existing data just to standardize it.

This is not required for a conversational answer, translation of supplied text, typo correction, or a standalone meeting/log entry. For a small structured project use a brief SPC and short PL, not no pipeline. If the user explicitly requests a one-off exception, record it in the PJL; never infer an exception from "don't ask permission."

## 1. Spec: interview and persist

Use create-spec (Codex wfk-create-spec; canonical create-note SPC). Before implementation, determine:
- What outcome should change, and for whom?
- What is in scope and explicitly out?
- What constraints, dependencies and real domain context apply?
- What observable evidence will mean done?

Read the conversation and existing records first. Ask focused missing questions, normally one at a time, in the user's language. An underspecified project MUST receive an interview question before any implementation or external creation. The prohibition on repetitive permission requests never suppresses these scope questions. Do not infer answers from elapsed time. State known answers so the user need not repeat them.

Scale to brief/standard/full using canonical templates. Save SPC - <Title>.md under specs/<date> with purpose, scope, requirements, constraints and measurable acceptance. Unanswered material decisions mean status: Draft and dependent work waits. When the supplied requirements are sufficient, summarize the scope, record its source and set status: Ready; do not invent a formal approval. "Draft a spec only" ends after drafting/review as requested, not implementation.

Maintain one current source of truth. Update the active spec with a dated change note, preserving decision history; use a new dated artifact only for a deliberate revision and mark which supersedes which. Do not pick a file solely because it has the newest date if the project context points to another active version.

## Review before planning

Read the relevant canonical review criteria. Review outcome/scope, feasibility/domain context, and acceptance/risks. Save an RE or ARE under reviews/<date> with source link and outcome: ready or changes-required. Resolve blocking findings in the spec before advancing. A local sequential review is valid when no independent review is requested/available; label it honestly, never claim three independent agents.

Apply factual corrections within known scope; ask when a finding requires a real user decision. Re-review changed sections. Missing optional oracle/connector infrastructure is not a substitute for review and not itself a reason to skip it. Mark unverifiable claims and block only work that depends on them.

## 2. Plan: persistent execution source

Use create-plan/plan-spec (Codex wfk-plan-spec; canonical plan-spec). Require a real current SPC and review; if absent, go back to the missing stage. A generic request to plan is not permission to bypass the spec.

Save PL - <Title>.md under plans/<date>. Include source and review wikilinks, status, completed, total, task IDs, status, dependencies, deliverables/paths, acceptance checks, and Work Log. Task states: todo, in-progress, blocked, done. Counters must match the task table. Brief work may use a flat table; complex work uses phases with useful checkpoints.

Before implementation, use scripts/pipeline_gate.py with --spec, --review and --plan and --stage implement, when available. It is a read-only structural check; also inspect requirement/acceptance meaning. If the helper is unavailable, perform the same checks manually and disclose that. A failed gate means repair the missing stage, not bypass the helper. Do not make empty placeholder docs just to pass.

## 3. Implement: execute, verify, update

Advance automatically through authorized stages when scope is established. Do not ask "may I continue?" at each ordinary stage. Do not implement if a material answer is pending, review outcome is changes-required, or no linked plan exists.

Run the next dependency-ready task. After a meaningful task or milestone, verify its acceptance, record evidence and update the PL and PJL/DN before context is lost. Mark physical work user-reported until verified; drafting a checklist is not doing the physical work.

Use human checkpoints for complex phases that need an actual choice, operational confirmation or acceptance. Do not manufacture approval gates for ordinary reversible work. Parallel work is optional only where explicitly authorized and tools support it; sequential execution preserves the same deliverables and evidence. No fabricated team APIs.

A material scope change returns to the spec, review and affected plan tasks. Do not silently accumulate new features in implementation.

## Two logging layers and rollups

PJL is the detailed persistent record: paths, commands, versions/commits when evidenced, decisions and rationale, failures and recovery, remote verification and next actions. Write it first. DN is the human summary under Worked on, grouped by project/subproject with up to three concise outcome bullets, one bold key outcome and a PJL link. Avoid technical build-log detail. Create missing DN/PJL files when required by authorized work; preserve unrelated content.

For heavy work (10+ tasks or a multi-phase sprint), use WL for granular evidence and link DN -> PJL -> WL. Never write secrets into logs, notes, plans, specs or any tracked file, and never claim a transcript is complete if unavailable. One sanctioned exception exists: the `token` field of `.notion/config.json`, which the Notion publisher reads. That directory is gitignored by the kit and the script refuses a stored token if the file ever becomes tracked, so writing it there is the designed setup path, not a leak. Write it without objecting when asked. Still never print a token value into tool output, chat or a vault document. Re-read before edits and verify afterward. Merge duplicate work instead of appending it again. A partial write is reported accurately and resumed from the saved record.

On a request for a weekly/monthly rollup, or an applicable end-of-period workflow, aggregate real dated files: weekly from DN/PJL/WL, monthly from weekly reports plus relevant gaps. Save RE under 01_Notes/Reports/Weekly/<date>/ or Monthly/<date>/ with explicit period, source links, outcomes, blockers and trends. Reuse an existing corresponding rollup rather than duplicate it; never invent missing days or treat trends as measured business performance without supporting data. No scheduler is implied.

## Pickup and closeout are part of the pipeline

At startup, orient and inspect existing resumable work. Pickup loads the active spec, review, plan, PJL and relevant PIC; it does not rebuild work merely because a new chat started. An explicit "continue" resumes the next authorized task. A request only to list or explain pending work remains read-only.

At closeout:
1. Reconcile task status and evidence in the PL; distinguish saved, published and actually deployed.
2. Log real work to PJL and DN, with WL when needed. Do not push/commit/deploy merely because a session is closing.
3. Search existing PICs before creating one. Update the matching PIC, or create one under the subproject's pickups/<date> when unfinished work has context not captured by its plan. Include done/next, known issues, verified files, blockers and links to active SPC/PL. If the plan contains all continuation context, link it explicitly instead.
4. Close a PIC only when its stated work is resolved. A session ending never marks an incomplete project complete.
5. Before project completion, run the gate with --stage complete, and verify all acceptance evidence, remaining tasks, dependencies and required participant/physical checks. Set plan frontmatter acceptance: verified and acceptance_evidence to the actual report path relative to the plan, within this project, only after reviewing that evidence. Passing the structural gate alone is insufficient.
6. State separately: session saved; project complete or still in progress; exact next step and artifact.

Configured Notion publishing follows scripts/NOTION-WORKFLOW.md if present. Failure leaves a local pending event; it must not hide a saved local closeout. Do not infer remote sync from writing a note.

## Onboarding and persistence

Teach the user that they can speak naturally in their language; show one short project example that starts with an interview. Preserve identity/role/language, local documents and decisions during setup/update. Root instructions and project context survive new sessions; conversation history is not shared automatically.

Hook scripts remain host-specific helpers. Existing Claude hooks are soft warnings unless documented otherwise; do not claim they enforce the pipeline or run in Codex. Do not install global hooks as part of onboarding without an explicit installation request. The lifecycle is an instruction contract plus checks, not a guarantee that a model can never deviate.
