# Ecosystem Coverage Matrix

This matrix shows which skill-adjacent concepts each ecosystem emphasizes.
It is a starting point for orientation, not a capability guarantee.

| Ecosystem | Agents | Tools | Workflows | MCP | Memory / knowledge | Evals / observability | Guardrails / approvals |
|---|---|---|---|---|---|---|---|
| CrewAI | Yes | Yes | Crews and flows | Tooling-dependent | Memory and knowledge | Observability integrations | Guardrails and process design |
| AutoGen | Yes | Yes | AgentChat, Core, Studio | MCP workbench and extensions | Application-dependent | Debugging and Studio workflows | Human review by app design |
| Semantic Kernel | Yes | Plugins/functions | Planners and processes | Connector-dependent | Memory support | Enterprise app telemetry by design | Policy and app-layer controls |
| LlamaIndex | Yes | Yes | Workflows | MCP examples and tools | Core RAG/data strength | Evals and observability | Human-in-the-loop patterns |
| Pydantic AI | Yes | Toolsets | Graphs and durable execution | MCP support | App-specific | Evals and instrumentation | Human-in-the-loop approval |
| Haystack | Yes | Tools/components | Pipelines | MCP serving | RAG and document stores | Evaluators and tracing | Pipeline-level controls |
| Strands Agents | Yes | Tools | SDK workflows | Integration-dependent | App-specific | Hooks and observability | Hooks and runtime policy |
| Agno | Yes | Tools | Multi-agent apps | Integration-dependent | Memory and knowledge | Monitoring by app setup | Team policy by app setup |

## Use This Matrix For

- deciding which ecosystem page to read first
- checking whether a workflow is mostly RAG, orchestration, coding, or runtime ops
- identifying where a skill needs extra setup or review notes

## Do Not Use It For

- vendor ranking
- security approval
- assuming feature parity across languages or deployment targets

## Ops Layer

| Area | Start here | Use it for |
|---|---|---|
| Observability and evals | [Agent Ops](../ops/) | traces, evals, prompt/tool logs, regression checks |
| Human approval | [Human Approval Workflows](../ops/human-approval-workflows.md) | approval before writes, deployments, external messages, sensitive actions |
| Workflow automation | [Workflow Automation](../ops/workflow-automation.md) | n8n, Zapier, Composio, connector-heavy flows |
| Gateways and policy | [Model Gateways And Policy](../ops/model-gateways-and-policy.md) | model routing, failover, cost controls, audit logs |

## Deployment Layer

| Area | Start here | Use it for |
|---|---|---|
| Deployment overview | [Deployment](../deployment/) | choosing runtime boundaries and rollout evidence |
| Runtime hosting | [Runtime Hosting](../deployment/runtime-hosting.md) | web apps, workers, containers, jobs, managed agents |
| Sandbox/container execution | [Sandbox And Container Execution](../deployment/sandbox-and-container-execution.md) | generated code, shell commands, repository automation |
| Provider comparison | [Provider Matrix](../deployment/provider-matrix.md) | Vercel, Cloudflare Workers, Fly.io, Modal, AWS, Azure, Google Cloud |

## Evaluation Layer

| Area | Start here | Use it for |
|---|---|---|
| Evaluation overview | [Evaluation](../evaluation/) | turning skill claims into evidence |
| Benchmark landscape | [Benchmark Landscape](../evaluation/benchmark-landscape.md) | SWE-bench, GAIA, τ-bench, AgentBench, HELM, AILuminate |
| Eval design | [Eval Design](../evaluation/eval-design.md) | task rubrics, datasets, tool checks, safety checks |
| Regression testing | [Regression Testing](../evaluation/regression-testing.md) | catching drift after prompt/model/tool changes |
| Tool matrix | [Evaluation Tool Matrix](../evaluation/evaluation-tool-matrix.md) | Inspect AI, OpenAI Evals, Ragas, DeepEval, Braintrust |

## Security Layer

| Area | Start here | Use it for |
|---|---|---|
| Safety review | [Security](../security/) | permissions, data, secrets, tools, approval, evidence |
| Prompt injection | [Prompt Injection And Tool Abuse](../security/prompt-injection-and-tool-abuse.md) | untrusted input, tool misuse, indirect instructions |
| Runtime guardrails | [Runtime Guardrails](../security/runtime-guardrails.md) | validators, filters, policy checks, refusal paths |
| Red teaming | [Red Teaming And Evals](../security/red-teaming-and-evals.md) | adversarial prompts, regression tests, risk probes |
