---
name: wfk-discover
description: >-
  Show the Codex workflows installed in this repository. Use for "qué habilidades tienes", "ayuda con los comandos", "discover", or available workflows.
---

# WFK discover

Resolve the repository root as `../../..` from this skill's directory.
Read `<root>/05_System/Workflows/REF - Codex Execution Policy.md`, then
`<root>/skills/discover/SKILL.md`. Resolve canonical references relative
to that canonical directory. This adapter and the portable policy override
Claude-specific tool, installation, path and workflow-side-effect instructions.

List the real .agents/skills/wfk-*/SKILL.md files and read their metadata.
Explain the supported workflows in Spanish with explicit $wfk-* invocation
examples and Spanish natural-language examples. Distinguish those adapters
from the larger upstream skills/ catalog, which is not fully ported.
Do not install, update or activate every skill just to list them.
