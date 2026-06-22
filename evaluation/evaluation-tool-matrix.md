# Evaluation Tool Matrix

This matrix helps readers pick an evaluation surface for the kind of workflow
they are reviewing. It is not a ranking.

| Surface | Best fit | Skill-adjacent use |
|---|---|---|
| [SWE-bench](../ecosystems/swe-bench.md) | coding-agent patch workflows | compare coding issue resolution patterns |
| [GAIA](../ecosystems/gaia.md) | broad assistant/tool-use tasks | understand general tool-using assistant evaluation |
| [τ-bench](../ecosystems/tau-bench.md) | tool-agent reliability | test tool-call behavior in simulated domains |
| [AgentBench](../ecosystems/agentbench.md) | broad agent environments | compare multi-environment agent behavior |
| [HELM](../ecosystems/helm.md) | model evaluation scenarios | understand model-level evaluation dimensions |
| [MLCommons AILuminate](../ecosystems/mlcommons-ailuminate.md) | safety and risk evaluation | align safety review with benchmarked risk categories |
| [Inspect AI](../ecosystems/inspect-ai.md) | programmable eval tasks | write custom evals with task/scorer structure |
| [OpenAI Evals](../ecosystems/openai-evals.md) | API-backed eval workflows | run model and task evals for OpenAI workflows |
| [Ragas](../ecosystems/ragas.md) | RAG quality | evaluate retrieval, grounding, and answer quality |
| [DeepEval](../ecosystems/deepeval.md) | LLM app tests | run test cases and metrics for app workflows |
| [Braintrust](../ecosystems/braintrust.md) | eval tracking | manage datasets, experiments, prompts, and results |

## Practical Rule

Choose the tool that matches the workflow evidence you need. If the workflow is
about repository edits, start with coding-agent examples. If it is about
retrieval, start with RAG evals. If it is about external actions, include tool
call traces and approval checks even if the benchmark score looks good.
