# Claude Code

Claude Code is Anthropic's coding-agent environment. It is commonly used for
repo-aware development, tool use, subagents, MCP workflows, and project-specific
instructions.

## Role In The Skills Ecosystem

- Coding-agent workflow surface.
- Strong fit for repeatable development, refactoring, debugging, and repository
  automation skills.
- Skills should avoid vague "be better at coding" prompts and instead name the
  files, tools, checks, and escalation rules.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [Claude Code docs](https://code.claude.com/docs) | Anthropic's documentation entry point. |
| Official | [Claude Code headless docs](https://code.claude.com/docs/en/headless) | Programmatic and automation-oriented Claude Code usage. |
| Lab | [Anthropic Claude Code advanced patterns](https://resources.anthropic.com/) | Anthropic resources for subagents, MCP, and scaling patterns. |
| ASE | [Claude Code skills catalog](https://agentskillexchange.com/browse-skills/?framework=Claude%20Code) | Live ASE view of Claude Code skills. |

## Skill Guidance

Claude Code skills should be clear about:

- project context to load
- tools or MCP servers to use
- command safety
- expected artifacts
- review and verification steps

## Skill Patterns That Fit Claude Code

- project workflow installation
- subagent and MCP routing
- security review passes
- browser and CLI verification
- documentation or content workflows inside a repo

## Representative ASE Examples

- `run-claude-code-security-operations-with-secopsagentkit`
- `install-claude-code-project-workflows-with-claude-workflow-v2`
- `install-focused-claude-code-workflow-plugins-from-claude-night-market`
- `drive-token-efficient-browser-testing-from-coding-agents-with-playwright-cli`

## Common Mistakes

- Treating a skill as a vague persona instead of an executable workflow.
- Forgetting to name tools, files, and verification commands.
- Letting generated content drift away from source-backed evidence.
