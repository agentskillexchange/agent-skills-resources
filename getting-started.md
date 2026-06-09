# Getting Started

This guide is for people who want to understand or create agent skills without
confusing this companion repo with the main ASE catalog.

## Beginner Path

1. Read [ecosystem-map.md](ecosystem-map.md).
2. Browse the canonical catalog at [Agent Skill Exchange](https://agentskillexchange.com/browse-skills/).
3. Inspect a few source-backed examples in [agentskillexchange/skills](https://github.com/agentskillexchange/skills).
4. Pick one workflow you repeat often.
5. Write a small skill that explains setup, steps, verification, and failure modes.

## Framework-Specific Path

| If you use | Start with |
|---|---|
| Codex | [frameworks/codex.md](frameworks/codex.md) |
| Claude Code | [frameworks/claude-code.md](frameworks/claude-code.md) |
| OpenClaw | [frameworks/openclaw.md](frameworks/openclaw.md) |
| Hermes | [frameworks/hermes.md](frameworks/hermes.md) |
| Cursor | [frameworks/cursor.md](frameworks/cursor.md) |
| Gemini CLI | [frameworks/gemini.md](frameworks/gemini.md) |
| LangGraph | [frameworks/langchain-langgraph.md](frameworks/langchain-langgraph.md) |
| MCP clients | [frameworks/mcp.md](frameworks/mcp.md) |

## ASE Contributor Path

1. Check the live skill already does not exist.
2. Prefer a real upstream repo, package, or API.
3. Use clear `name`, `slug`, `description`, `category`, `framework`, `verification`, and `source` metadata.
4. Include concrete install/setup guidance.
5. Include at least one practical usage flow.
6. Include verification steps.
7. Submit through the ASE workflow or GitHub contribution path.

## Trust And Safety Checklist

- Source URL exists and points to the real upstream project.
- Install steps do not use unsafe pipe-to-shell commands without warning.
- Secrets, tokens, and credentials are handled explicitly.
- The skill avoids fake "official" claims.
- The body includes usage and verification, not only metadata.
- The skill explains when not to use the workflow.

