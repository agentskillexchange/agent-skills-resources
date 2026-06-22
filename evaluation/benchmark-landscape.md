# Benchmark Landscape

Public benchmarks can help readers understand what different agent systems are
being tested for. They should be paired with workflow-specific evidence before a
team adopts a skill.

## Benchmark Families

| Benchmark / surface | What it emphasizes | Use carefully because |
|---|---|---|
| [SWE-bench](../ecosystems/swe-bench.md) | software engineering issues and patch generation | repo-specific skill workflows may need different tests |
| [GAIA](../ecosystems/gaia.md) | general assistant tasks requiring reasoning and tool use | tasks are broader than most production skills |
| [τ-bench](../ecosystems/tau-bench.md) | tool-agent behavior in simulated domains | simulation results do not replace real integration tests |
| [AgentBench](../ecosystems/agentbench.md) | multi-environment agent evaluation | broad benchmark scope may not match one workflow |
| [HELM](../ecosystems/helm.md) | holistic model evaluation scenarios | model-level evals are not enough for tool workflows |
| [MLCommons AILuminate](../ecosystems/mlcommons-ailuminate.md) | AI safety and risk evaluation | safety taxonomy still needs workflow-specific controls |

## Eval Tooling Surfaces

| Tool / platform | What it helps with |
|---|---|
| [Inspect AI](../ecosystems/inspect-ai.md) | programmable eval tasks and scorers |
| [OpenAI Evals](../ecosystems/openai-evals.md) | eval datasets and API-based evaluation workflows |
| [Ragas](../ecosystems/ragas.md) | RAG and retrieval quality evaluation |
| [DeepEval](../ecosystems/deepeval.md) | LLM app test cases and metrics |
| [Braintrust](../ecosystems/braintrust.md) | eval tracking, experiments, prompts, and datasets |

## Selection Rules

- Use coding benchmarks for coding workflows.
- Use RAG evals for retrieval and grounded-answer workflows.
- Use safety benchmarks for risk review, not product approval by themselves.
- Always add at least one workflow-specific test before rollout.
- Capture traces or logs, not only pass/fail numbers.
