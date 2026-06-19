# Glossary

Concise definitions for common agent skill terms.

| Term | Meaning |
|---|---|
| Agent skill | Reusable instructions, setup notes, safety constraints, and verification steps for a repeatable agent workflow. |
| Tool | A callable capability such as a CLI, API, browser action, database query, or file operation. |
| MCP server | A server that exposes tools, resources, or prompts through the Model Context Protocol. |
| Agent runtime | The environment that coordinates the model, tools, memory, approvals, filesystem, and execution. |
| Coding agent | An agent focused on code tasks such as editing files, running tests, reviewing changes, and using repositories. |
| Workflow | A sequence of actions that produces a reviewable outcome. |
| Handoff | A structured transfer of context, decisions, evidence, and next steps between agents or people. |
| Guardrail | A rule, check, approval gate, or technical boundary that reduces unsafe behavior. |
| Verification | Evidence that the work succeeded, such as tests, logs, screenshots, citations, or dry-run output. |
| Provenance | The source and ownership trail for a skill, tool, claim, or resource. |
| Sandbox | A constrained environment where actions can be tested with limited blast radius. |
| Approval gate | A point where the agent must stop and wait for human approval before continuing. |
| Memory | Stored context that can help future agent runs, such as preferences, project state, or prior decisions. |
| Observability | Logs, traces, metrics, and reports that make agent behavior inspectable. |
| Evaluation | A structured review of quality, safety, usefulness, and reliability. |

Use these terms consistently when writing new learning pages, playbooks, or
resource notes.
