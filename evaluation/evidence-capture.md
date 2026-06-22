# Evidence Capture

Good evaluation evidence is compact, inspectable, and tied to a decision. It
does not need to be elaborate, but it should be enough for another reviewer to
understand why the workflow passed or failed.

## Evidence Types

| Evidence | Best for |
|---|---|
| Trace | model calls, tool calls, timing, retries |
| Command log | coding-agent and repo workflows |
| Diff or artifact | code, docs, generated files |
| Citation list | research and content workflows |
| Approval record | risky writes, external messages, deployments |
| Eval score | repeated task sets and regression runs |
| Reviewer note | qualitative judgment and next action |

## Minimum Evidence Bundle

- input or task ID
- skill or workflow name
- model/runtime if relevant
- output artifact or result
- trace/log/artifact link
- pass/fail/revisit decision
- reason for decision

## Keep Evidence Safe

- redact secrets and customer data
- avoid storing raw private prompts unless required
- separate public examples from internal pilot evidence
- document who can access logs and traces
- keep retention aligned with team policy
