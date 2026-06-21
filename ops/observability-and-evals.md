# Observability And Evals

Agent observability helps teams understand what happened during a run. Evals
help teams decide whether a workflow is improving, stable, or regressing.

## What To Capture

| Evidence | Why it matters |
|---|---|
| Trace | Shows model calls, tool calls, timing, and intermediate steps |
| Prompt/tool logs | Helps debug why the agent took an action |
| Inputs and outputs | Makes review reproducible |
| Eval result | Gives a repeatable quality signal |
| Regression check | Protects against silent behavior changes |
| Human approval record | Shows who allowed risky action and why |

## Before Expanding A Pilot

Save enough evidence to answer:

- What did the agent see?
- Which tools did it call?
- What changed?
- Who reviewed the output?
- Which evals or checks passed?
- What would trigger rollback?

## Common Failure Modes

- only saving final output
- missing tool call details
- no baseline examples for comparison
- treating one successful run as production readiness
- collecting traces without reviewing them

## Related Ecosystems

- [LangSmith](../ecosystems/langsmith.md)
- [Langfuse](../ecosystems/langfuse.md)
- [Arize Phoenix](../ecosystems/arize-phoenix.md)
- [Weights & Biases Weave](../ecosystems/weights-biases-weave.md)
- [OpenTelemetry GenAI](../ecosystems/opentelemetry-genai.md)
