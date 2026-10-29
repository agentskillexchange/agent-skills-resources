# Cursor

Cursor is an IDE-centered agent environment. Its skills and context features help
developers steer agent work inside editor and repository workflows.

## Role In The Skills Ecosystem

- IDE agent environment.
- Strong fit for project context, editor workflows, background agents, and
  coding assistance.
- Skills should be written as practical editor/repo workflows, not generic
  productivity advice.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [Cursor Agent Skills docs](https://cursor.com/docs/context/skills) | Cursor documentation for skills. |
| Official | [Cursor tools docs](https://docs.cursor.com/en/agent/tools) | Tool usage inside Cursor Agent. |
| Official | [Cursor Background Agents](https://docs.cursor.com/background-agent) | Background-agent workflow context. |
| ASE | [Cursor skills catalog](https://agentskillexchange.com/browse-skills/?framework=Cursor) | Live ASE view of Cursor-related skills. |

## Skill Guidance

Cursor skills should state:

- repo context to include
- editor or background-agent mode
- file patterns to inspect
- validation commands
- expected review output

## Skill Patterns That Fit Cursor

- project rules and context files
- IDE-centered implementation workflows
- background-agent task routing
- MCP setup across editor clients
- reusable review checklists

## Representative ASE Examples

- `sync-agent-rules-and-skill-files-across-coding-assistants-with-ai-rules-sync`
- `install-one-mcp-server-across-claude-code-cursor-codex-and-vs-code-without-manual-config-edits`
- `capture-search-and-optionally-sync-local-coding-agent-session-history-across-claude-code-codex-cursor-cli-and-gemini-with-specstory`

## Next Artifact To Open

If you are evaluating a Cursor skill for an IDE-centered repository workflow,
compare it with the
[Staff Engineer Mode completed evaluation](../examples/completed-evaluations/staff-engineer-mode-evaluation.md)
first, then copy the evidence shape into the
[Skill Evaluation Worksheet](../templates/skill-evaluation-worksheet.md).

Carry forward the repository and editor context, agent mode, file patterns and
allowed tools, validation commands, requested review output, unresolved risks,
and the bounded expected output. The example is an evidence pattern for a
Cursor workflow, not an endorsement of Cursor or a specific skill.

## Common Mistakes

- Writing skills that assume a terminal-only workflow.
- Forgetting editor context and project rules.
- Claiming cross-client compatibility without setup checks.
