# Framework Guides

These pages explain where major agent frameworks, runtimes, and protocols fit in
the skills ecosystem.

## Choose A Framework Guide By Job

| Job to do | Start with | Why |
|---|---|---|
| Inspect a repo, edit code, and verify changes from the terminal | [Codex](codex.md), [Claude Code](claude-code.md), or [Gemini](gemini.md) | Terminal agents fit bounded implementation loops with command evidence. |
| Keep skill-backed work inside an IDE or GitHub review flow | [Cursor](cursor.md) or [GitHub Copilot](github-copilot.md) | Editor and PR surfaces keep context, rules, review, and approval close to code. |
| Run scheduled, channel-based, or persistent agent workflows | [OpenClaw](openclaw.md) or [Hermes](hermes.md) | Runtime-owned workflows need explicit permissions, logs, health checks, and rollback. |
| Build an agent app, graph, or integration layer | [LangChain and LangGraph](langchain-langgraph.md) or [Model Context Protocol](mcp.md) | Frameworks and protocols make state, tools, handoffs, and integration boundaries explicit. |

## Compare Against A Finished Evidence Shape

After you pick a framework guide, compare the workflow with a completed
evaluation example before filling out a worksheet. Use the example for evidence
shape only; do not treat it as a framework endorsement or catalog ranking.

| Framework choice | Compare with | Evidence shape to copy |
|---|---|---|
| Terminal coding agent or repo-review workflow | [Staff Engineer Mode](../examples/completed-evaluations/staff-engineer-mode-evaluation.md) | Requested checks, changed files, unresolved risks, and reviewer notes. |
| Approval-gated, sensitive-action, or team policy workflow | [HumanLayer Approval Workflow](../examples/completed-evaluations/humanlayer-approval-workflow-evaluation.md) | Approval request, approver identity, denied-action behavior, and security-review notes. |
| MCP, data, or read-only integration workflow | [MCP Database Inspection](../examples/completed-evaluations/mcp-database-inspection-evaluation.md) | Credential scope, query log, validation checks, and sample result review. |
| Scheduled runtime or day-2 operations workflow | [OpenClaw Runtime Ops](../examples/completed-evaluations/openclaw-runtime-ops-evaluation.md) | Commands inspected, config paths reviewed, operator notes, and missing runbook evidence. |

- [Codex](codex.md)
- [Claude Code](claude-code.md)
- [GitHub Copilot](github-copilot.md)
- [OpenClaw](openclaw.md)
- [Hermes](hermes.md)
- [Cursor](cursor.md)
- [Gemini](gemini.md)
- [LangChain and LangGraph](langchain-langgraph.md)
- [Model Context Protocol](mcp.md)
