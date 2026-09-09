---
name: wfk-git-safe
description: >-
  Handle requested commits, synchronization or Git publication without losing work. Use for "commit", "sube mis cambios", "sincroniza con GitHub", or a Git conflict.
---

# WFK git-safe

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/git-safe/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Read canonical Git guidance, preserving its invariants about user data and
sequential operations. Replace machine-specific helpers and automatic checkpoint/
push/session-cleanup instructions with this workflow:
1. Inspect repository root, status, current branch, remotes and relevant diff.
2. Determine the user-authorized operation and exact files; preserve unrelated
   staged and unstaged work. Do not assume every changed file is yours.
3. Use the configured Git identity and hooks. If no identity is configured, ask
   for it or use an identity the user has already authorized; never invent one.
4. For a commit, stage only selected paths, inspect the staged diff and run
   configured checks. Do not bypass a failed hook or scanner.
5. Push only when requested/authorized and to the verified user destination.
   Read remote state as needed; handle divergence deliberately, never force.
6. Verify the resulting local/remote state and report what was actually saved.
No fixed username, account, Windows path, scanner version or repository is
required. Do not copy Luca's personal local_commit.py. A missing Git install
does not block local notes; it blocks the requested Git operation only.
