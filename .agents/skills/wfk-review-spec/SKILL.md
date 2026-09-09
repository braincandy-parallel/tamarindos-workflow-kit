---
name: wfk-review-spec
description: >-
  Review a specification for scope, feasibility and acceptance gaps. Use for "revisa esta especificación", "evalúa los riesgos", or readiness before planning.
---

# WFK review-spec

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/review-spec/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Read the source spec and project context. Apply canonical review criteria, but
perform three sequential perspectives: scope/user outcome, feasibility/context,
and verification/risks. Do not claim three independent agents ran.
Verify technical claims against available local sources. If an external system
is needed but unavailable, mark the claim unverified and explain the implication;
do not launch placeholder SSH/database commands.
Save one RE - Revision de <title>.md under project/reviews/YYYY-MM-DD with
category Report, source link, findings ranked by severity, evidence and unresolved
decisions. A request for conversational feedback alone need not create a file.
Do not edit the spec or produce a plan automatically.
