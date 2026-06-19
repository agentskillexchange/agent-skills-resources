# Multi-Framework Skills

A multi-framework skill should describe a workflow that can travel across
runtimes without pretending every runtime has the same features.

## Good Multi-Framework Claims

- The workflow is portable.
- The tool is available through a CLI, API, or MCP server.
- The safety checks apply across runtimes.
- Framework-specific setup is separated into adapters or notes.

## Weak Multi-Framework Claims

- "Works everywhere" with no tested surfaces.
- Runtime-specific commands mixed into generic instructions.
- Claims about vendor features without official sources.
- No fallback when a runtime lacks a tool or permission model.

## Structure

| Section | Purpose |
|---|---|
| Framework-neutral workflow | The stable process |
| Surface-specific notes | Codex, Claude Code, Copilot, OpenClaw, Cursor, Gemini CLI, etc. |
| Tool adapters | CLI, API, MCP, browser, filesystem |
| Verification | Evidence that does not depend on one runtime |
| Limitations | Unsupported runtimes or untested claims |

## Practical Test

If removing the runtime name breaks the skill, it is probably not
multi-framework. If the workflow still makes sense and only setup changes, the
skill is a better candidate.
