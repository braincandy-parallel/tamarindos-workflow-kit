---
name: wfk-setup
description: >-
  Configure a fresh Tamarindos workspace and user profile. Use for "setup", "configura mi espacio", "primera vez", or onboarding; not routine session startup.
---

# WFK setup

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/setup/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

Follow the portable setup procedure instead of the canonical machine scanner,
global skill installer, automatic migration and three-PIC onboarding.
1. Read existing workflow-kit.config.json if present. Reuse its name, role,
   project and language. Ask only for missing name, role and first priority.
2. For a fresh copy, propose project slug tamarindos (unless the user supplied
   another). The first priority is context, not an invented task completion.
3. Read scripts/bootstrap.py before running. Use Python 3.10+ from the current
   environment: python (Windows) or python3 (macOS/Linux). Run it with --root,
   --name, --role, --priority and --project arguments taken from supplied facts.
   Quote arguments correctly for the shell. No credentials or remote writes.
4. If Python is unavailable, perform the same create-missing-only scaffold
   described in the script with native file tools. Do not install Python or
   other programs without a user request. Preserve existing config/profile data.
5. Verify config, today's DN, project PJL, agents.md, lessons.md, preferences
   and one onboarding PIC. Report their paths and suggest wfk-pickup.
   No global installation is needed: Codex reads .agents/skills from this repo.
A repeated setup fills missing scaffolding without resetting the user's profile.
To change an existing profile, make only the explicitly requested edits after
reading the current file; do not silently replace it with setup arguments.

Read `<root>/05_System/Workflows/REF - Project Lifecycle.md` and apply its relevant stage rules.
After setup, explain the persistent lifecycle and demonstrate one brief Spanish project request starting with a scope interview. Do not start the person's first project without a project request. Preserve this contract and the native adapters on subsequent updates.
