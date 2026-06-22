# Resource Index

Generated from `data/resources.json`. Edit the JSON source, then rerun
`python3 scripts/generate-resource-index.py`.

## By Source Type

### ASE

| Resource | Framework | Why it matters |
|---|---|---|
| [Agent Skill Exchange](https://agentskillexchange.com/) | Multi-Framework | Provides the human-facing discovery layer for the canonical ASE skills catalog. |
| [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills) | Multi-Framework | This companion repo should point readers to the canonical skill source of truth. |
| [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification) | Multi-Framework | Shows how ASE separates listed skills from security-reviewed skills. |

### Community

| Resource | Framework | Why it matters |
|---|---|---|
| [AgentBench GitHub](https://github.com/THUDM/AgentBench) | AgentBench | AgentBench helps readers understand broad benchmark design for agent environments. |
| [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code | Useful for non-official ecosystem discovery when labeled separately from Anthropic-owned sources. |
| [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP | Useful for seeing the breadth of MCP servers, while clearly marked as community-maintained. |
| [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | GAIA | GAIA gives broad context for assistant tasks that require reasoning and tool use. |
| [OWASP Top 10 For LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Security | Provides a practical security checklist for skills that use tools, prompts, data, or code execution. |
| [τ-bench GitHub](https://github.com/sierra-research/tau-bench) | τ-bench | Tool-agent benchmarks help teams think about state, tool calls, and task success before building local evals. |

### Lab

| Resource | Framework | Why it matters |
|---|---|---|
| [HELM GitHub](https://github.com/stanford-crfm/helm) | HELM | The repo helps readers inspect benchmark methodology and implementation details. |
| [HELM Latest](https://crfm.stanford.edu/helm/latest/) | HELM | HELM is useful context for model-level scenario and metric design. |
| [OpenAI Codex Docs](https://developers.openai.com/codex) | Codex | Provides lab-owned guidance for Codex workflows and setup. |

### Official

| Resource | Framework | Why it matters |
|---|---|---|
| [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | GitHub Copilot | Shows how skills are installed and selected for Copilot cloud agent and related GitHub surfaces. |
| [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | GitHub Copilot | Connects terminal-native Copilot workflows to the broader skill ecosystem. |
| [Agno Docs](https://docs.agno.com/) | Agno | Adds coverage for a lightweight agent framework used to compare fast agent app patterns. |
| [Agno GitHub](https://github.com/agno-agi/agno) | Agno | Provides source context for Agno agent app examples and framework structure. |
| [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) | MCP | Gives provider-owned context for MCP as an agent-tool bridge. |
| [Arize Phoenix Docs](https://arize.com/docs/phoenix) | Arize Phoenix | Supports evidence-based review for RAG, agent, and LLM application workflows. |
| [Arize Phoenix GitHub](https://github.com/Arize-ai/phoenix) | Arize Phoenix | Provides source context for Phoenix observability and evaluation workflows. |
| [AWS Bedrock Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) | AWS Bedrock Agents | Managed agents, action groups, IAM, and knowledge bases are important deployment surfaces for enterprise skill-like workflows. |
| [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) | Azure AI Foundry | Agent Service concepts help teams map skill-backed workflows into managed Azure agent deployments. |
| [Azure AI Foundry Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/) | Azure AI Foundry | Azure AI Foundry provides enterprise AI project, agent, evaluation, deployment, and governance surfaces. |
| [Braintrust Docs](https://www.braintrust.dev/docs) | Braintrust | Braintrust helps teams manage repeated eval cycles and evidence across agent workflow pilots. |
| [Braintrust SDK GitHub](https://github.com/braintrustdata/braintrust-sdk-javascript) | Braintrust | The SDK repo gives implementation context for recording evals and experiments from applications. |
| [Claude Code Docs](https://code.claude.com/docs) | Claude Code | Primary source for Claude Code workflow and usage guidance. |
| [Claude Code Headless](https://code.claude.com/docs/en/headless) | Claude Code | Important for automation-oriented skills and CI workflows. |
| [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks) | Claude Code | Hooks are a useful reference point for approval, validation, and automation boundaries. |
| [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp) | Claude Code | Shows how Claude Code connects to tools and context through MCP. |
| [Claude Code Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory) | Claude Code | Memory affects how skills, instructions, and project preferences persist across agent work. |
| [Claude Code Settings Docs](https://docs.anthropic.com/en/docs/claude-code/settings) | Claude Code | Settings are part of the runtime boundary that skill authors need to understand. |
| [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) | Claude Code | Subagents are a useful comparison point for skill routing and workflow specialization. |
| [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/) | Cloudflare Workers | Workers can host lightweight tool adapters, routing layers, and policy checks around skill-backed workflows. |
| [Composio Docs](https://docs.composio.dev/) | Composio | Shows how connector-heavy agent workflows can expose external actions safely. |
| [Composio GitHub](https://github.com/ComposioHQ/composio) | Composio | Provides source context for agent connector and tool integration patterns. |
| [CrewAI Docs](https://docs.crewai.com/) | CrewAI | Shows how role-based and flow-based agent workflows can be captured as reusable skill recipes. |
| [CrewAI GitHub](https://github.com/crewAIInc/crewAI) | CrewAI | Provides source context for CrewAI framework usage and project structure. |
| [Cursor Agent Skills](https://cursor.com/docs/context/skills) | Cursor | Primary source for Cursor's skill model. |
| [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools) | Cursor | Helps distinguish skills from callable editor tools. |
| [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent) | Cursor | Background agents show how skill guidance can support asynchronous coding work. |
| [Cursor Rules Docs](https://docs.cursor.com/en/context/rules) | Cursor | Rules are an important adjacent concept for skill-like guidance in IDE agents. |
| [DeepEval Docs](https://deepeval.com/docs/getting-started) | DeepEval | DeepEval is relevant for teams that want CI-style eval tests around agent or skill outputs. |
| [DeepEval GitHub](https://github.com/confident-ai/deepeval) | DeepEval | The repo provides source-backed implementation context for LLM app testing. |
| [Fly.io Docs](https://fly.io/docs/) | Fly.io | Containerized agent services often need hosting, secrets, logs, and rollback practices beyond local skill execution. |
| [garak GitHub](https://github.com/NVIDIA/garak) | garak | Adds source-backed coverage for adversarial LLM testing and vulnerability discovery. |
| [Gemini API Docs](https://ai.google.dev/gemini-api/docs) | Gemini | Provider-level setup reference for Gemini-backed agent workflows. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Gemini | Represents Gemini-powered terminal-agent workflows. |
| [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs) | Gemini | Useful for terminal-agent setup, configuration, and workflow guidance. |
| [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | GitHub Copilot | Defines Copilot's skill model and helps compare it with other agent-skill runtimes. |
| [GitHub Copilot Docs](https://docs.github.com/en/copilot) | GitHub Copilot | Provides the official source for Copilot's coding-agent and customization surfaces. |
| [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp) | GitHub Copilot | Explains how MCP extends Copilot across IDE, CLI, app, cloud agent, and code review surfaces. |
| [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | GitHub Copilot | Helps readers distinguish persistent repository guidance from portable agent skills. |
| [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills) | GitHub Copilot | Shows how programmatic Copilot sessions can compose skills with MCP servers and hooks. |
| [Google ADK Agents Docs](https://google.github.io/adk-docs/agents/) | Google ADK | Helps compare how Google structures agents and agent workflow components. |
| [Google ADK Python](https://github.com/google/adk-python) | Google ADK | Source-backed reference for Google's agent development patterns. |
| [Google ADK Tools Docs](https://google.github.io/adk-docs/tools/) | Google ADK | Tool concepts help readers distinguish skill instructions from callable capabilities. |
| [Google Agent Development Kit Docs](https://google.github.io/adk-docs/) | Google ADK | Provides official Google guidance for building agents, tools, and workflows. |
| [Google Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) | Google Vertex AI Agent Builder | Google Cloud managed agent and enterprise search surfaces are relevant for deploying skill-adjacent workflows with cloud governance. |
| [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs) | Guardrails AI | Shows runtime validation patterns that can protect skill-backed workflows. |
| [Guardrails AI GitHub](https://github.com/guardrails-ai/guardrails) | Guardrails AI | Provides source context for guardrail implementation and validator patterns. |
| [Haystack Docs](https://docs.haystack.deepset.ai/docs/intro) | Haystack | Shows how production retrieval and pipeline workflows can be reviewed before skill adoption. |
| [Haystack GitHub](https://github.com/deepset-ai/haystack) | Haystack | Provides source context for production RAG and agent pipeline patterns. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Hermes | Shows a skills-oriented self-improving agent architecture. |
| [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md) | Hermes | Memory boundaries are closely related to reusable skill behavior. |
| [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md) | Hermes | Shows how Hermes documents built-in skills and their roles. |
| [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | Hermes | Defines how Hermes exposes and manages skills. |
| [HumanLayer GitHub](https://github.com/humanlayer/humanlayer) | HumanLayer | Provides source context for approval gates and human review patterns around tool calls. |
| [Inspect AI Docs](https://inspect.aisi.org.uk/) | Inspect AI | Inspect AI is useful for teams that need custom tasks, solvers, scorers, and reproducible eval logs. |
| [Lakera Docs](https://docs.lakera.ai/) | Lakera | Adds source-backed coverage for runtime protection and prompt injection defense. |
| [LangChain Agents](https://www.langchain.com/agents) | LangChain/LangGraph | Explains LangGraph's role in agent orchestration. |
| [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | LangChain/LangGraph | Shows how MCP tooling can plug into LangChain and LangGraph workflows. |
| [Langfuse Docs](https://langfuse.com/docs) | Langfuse | Helps teams review prompt and tool-call behavior before expanding an agent workflow. |
| [Langfuse GitHub](https://github.com/langfuse/langfuse) | Langfuse | Provides source context for Langfuse deployment and LLM observability implementation. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | LangChain/LangGraph | Source-backed reference for graph-based agent orchestration. |
| [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview) | LangChain/LangGraph | Explains stateful agent graphs and durable workflow concepts. |
| [LangGraph Human-in-the-loop Docs](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop) | LangChain / LangGraph | Provides a framework reference for approval gates and human-supervised agent workflows. |
| [LangGraph Persistence Docs](https://docs.langchain.com/oss/python/langgraph/persistence) | LangChain / LangGraph | State and persistence are central concepts for durable agent workflows and skill handoffs. |
| [LangSmith Docs](https://docs.langchain.com/langsmith/observability) | LangSmith | Gives teams a source-backed way to collect trace and eval evidence for skill-backed workflows. |
| [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) | LlamaFirewall | Adds runtime protection coverage for LLM application safety review. |
| [LlamaIndex Docs](https://developers.llamaindex.ai/python/framework/) | LlamaIndex | Covers the data and retrieval layer that many agent skills need to reference safely. |
| [LlamaIndex GitHub](https://github.com/run-llama/llama_index) | LlamaIndex | Provides source context for RAG agent and data workflow examples. |
| [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/stable/) | Microsoft AutoGen | Documents a major multi-agent ecosystem whose workflows can be translated into reusable skill guidance. |
| [Microsoft AutoGen GitHub](https://github.com/microsoft/autogen) | Microsoft AutoGen | Provides source code and examples for AutoGen agent applications and multi-agent workflows. |
| [MLCommons AILuminate](https://mlcommons.org/ailuminate/) | MLCommons AILuminate | AILuminate adds source-backed safety benchmark context for risk and governance discussions. |
| [Modal Docs](https://modal.com/docs) | Modal | Modal is useful for Python-heavy skill-backed data, model, and evaluation workflows with bounded execution. |
| [Model Context Protocol Docs](https://modelcontextprotocol.io/) | MCP | Primary source for tool/context protocol concepts. |
| [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) | MCP | Gives readers a starting point for understanding MCP as a tool and context layer for agents. |
| [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP | Source-backed reference for MCP specification and docs. |
| [n8n Docs](https://docs.n8n.io/) | n8n | Helps teams compare deterministic AI workflow automation with agent orchestration. |
| [n8n GitHub](https://github.com/n8n-io/n8n) | n8n | Provides source context for self-hosted workflow automation and connector patterns. |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Governance | Useful background for teams creating approval, governance, and rollout processes for agent skills. |
| [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents) | OpenAI Agents SDK | Useful for learning how a major provider frames agent design, tool use, and orchestration. |
| [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/) | OpenAI Agents | Shows source-backed patterns for tools, handoffs, guardrails, tracing, and agent execution. |
| [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python) | OpenAI Agents | Provides source code and examples for OpenAI agent workflows. |
| [OpenAI Apps SDK Docs](https://developers.openai.com/apps-sdk/) | OpenAI Apps SDK | Helps readers understand app and tool surfaces adjacent to agent skill workflows. |
| [OpenAI Codex](https://github.com/openai/codex) | Codex | Codex is a core coding-agent workflow surface for skill-driven repo work. |
| [OpenAI Evals GitHub](https://github.com/openai/evals) | OpenAI Evals | The repository gives readers a source-backed implementation reference for eval workflows. |
| [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals) | OpenAI Evals | OpenAI Evals guidance helps teams build repeatable checks for OpenAI-backed agent and skill workflows. |
| [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools) | OpenAI Agents | Helps distinguish model tools from higher-level skills and workflows. |
| [OpenClaw Docs](https://docs.openclaw.ai/) | OpenClaw | Explains OpenClaw providers, skills, tools, crons, and runtime setup. |
| [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation) | OpenClaw | Example of tool-specific runtime documentation that skills can wrap into workflows. |
| [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai) | OpenClaw | Provider setup affects how skills run across agent runtimes. |
| [OpenClaw Repository](https://github.com/openclaw/openclaw) | OpenClaw | Source-backed reference for OpenClaw runtime and contribution details. |
| [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | Observability | Gives teams vocabulary for traces, metrics, and evidence around agent workflows. |
| [OWASP LLM Top 10 GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) | OWASP LLM Top 10 | Provides source context for LLM application risk categories used in skill safety review. |
| [promptfoo Docs](https://www.promptfoo.dev/docs/intro/) | promptfoo | Helps teams test prompt and agent workflow behavior before rollout. |
| [promptfoo GitHub](https://github.com/promptfoo/promptfoo) | promptfoo | Provides source context for prompt and LLM application evaluation workflows. |
| [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama) | PurpleLlama | Provides source context for Meta LLM safety and runtime protection tooling. |
| [Pydantic AI Docs](https://pydantic.dev/docs/ai/overview/) | Pydantic AI | Gives Python teams a typed approach to agent workflows that can be reviewed as code. |
| [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai) | Pydantic AI | Provides source context for typed Python agent and evaluation patterns. |
| [PyRIT Docs](https://azure.github.io/PyRIT/) | PyRIT | Supports repeatable risk identification and evidence gathering for agent workflows. |
| [PyRIT GitHub](https://github.com/Azure/PyRIT) | PyRIT | Provides source context for Microsoft red-team tooling around generative AI systems. |
| [Ragas Docs](https://docs.ragas.io/) | Ragas | Ragas is relevant for skills that retrieve, ground, summarize, or answer from documents. |
| [Ragas GitHub](https://github.com/vibrantlabsai/ragas) | Ragas | The repo helps readers inspect RAG evaluation implementation details and examples. |
| [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/) | Semantic Kernel | Shows how enterprise agent workflows use plugins, functions, planners, memory, and application integration. |
| [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel) | Semantic Kernel | Provides source context for Semantic Kernel app and agent orchestration patterns. |
| [Strands Agents Docs](https://strandsagents.com/) | Strands Agents | Adds SDK-level agent workflow coverage for teams comparing tool, hook, and observability patterns. |
| [Strands Agents GitHub](https://github.com/strands-agents/harness-sdk) | Strands Agents | Provides source context for Strands agent SDK workflow patterns. |
| [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench) | SWE-bench | The repo helps readers inspect benchmark setup instead of relying on leaderboard claims alone. |
| [SWE-bench Site](https://www.swebench.com/) | SWE-bench | SWE-bench is useful context for evaluating coding-agent and repository patch workflows. |
| [Vercel AI Gateway Docs](https://vercel.com/docs/ai-gateway) | Vercel AI Gateway | Adds model gateway and policy-layer coverage for teams operating skill-backed AI applications. |
| [Vercel AI GitHub](https://github.com/vercel/ai) | Vercel AI SDK | Provides source context for Vercel AI SDK patterns used in AI apps and agent workflows. |
| [Vercel AI SDK Docs](https://ai-sdk.dev/docs) | Vercel AI SDK | Shows how skill-backed workflows can become application features with tool calling and deployment. |
| [Vercel Deployments Docs](https://vercel.com/docs/deployments) | Vercel Platform | Preview deployments are useful evidence points before rolling out skill-backed AI app workflows. |
| [Vercel Functions Docs](https://vercel.com/docs/functions) | Vercel Platform | Function limits, runtime behavior, and environment handling shape how agent workflows should be hosted. |
| [Vercel Platform Docs](https://vercel.com/docs) | Vercel Platform | Helps teams understand how hosted AI apps and skill-backed workflows are deployed, configured, and operated on Vercel. |
| [Vertex AI Agent Engine Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) | Google Vertex AI Agent Builder | Agent Engine documentation helps teams understand managed deployment, operation, and integration choices for agent workflows. |
| [Weights & Biases Weave Docs](https://docs.wandb.ai/weave) | Weights & Biases Weave | Helps teams connect agent workflow evidence to experiment and eval review. |
| [Weights & Biases Weave GitHub](https://github.com/wandb/weave) | Weights & Biases Weave | Provides source context for Weave tracing and evaluation implementation. |
| [Zapier Docs](https://docs.zapier.com/) | Zapier | Gives teams a source-backed reference for SaaS workflow automation around agent output. |

## By Framework

### AWS Bedrock Agents

| Resource | Framework | Why it matters |
|---|---|---|
| [AWS Bedrock Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) | AWS Bedrock Agents | Managed agents, action groups, IAM, and knowledge bases are important deployment surfaces for enterprise skill-like workflows. |

### AgentBench

| Resource | Framework | Why it matters |
|---|---|---|
| [AgentBench GitHub](https://github.com/THUDM/AgentBench) | AgentBench | AgentBench helps readers understand broad benchmark design for agent environments. |

### Agno

| Resource | Framework | Why it matters |
|---|---|---|
| [Agno Docs](https://docs.agno.com/) | Agno | Adds coverage for a lightweight agent framework used to compare fast agent app patterns. |
| [Agno GitHub](https://github.com/agno-agi/agno) | Agno | Provides source context for Agno agent app examples and framework structure. |

### Arize Phoenix

| Resource | Framework | Why it matters |
|---|---|---|
| [Arize Phoenix Docs](https://arize.com/docs/phoenix) | Arize Phoenix | Supports evidence-based review for RAG, agent, and LLM application workflows. |
| [Arize Phoenix GitHub](https://github.com/Arize-ai/phoenix) | Arize Phoenix | Provides source context for Phoenix observability and evaluation workflows. |

### Azure AI Foundry

| Resource | Framework | Why it matters |
|---|---|---|
| [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview) | Azure AI Foundry | Agent Service concepts help teams map skill-backed workflows into managed Azure agent deployments. |
| [Azure AI Foundry Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/) | Azure AI Foundry | Azure AI Foundry provides enterprise AI project, agent, evaluation, deployment, and governance surfaces. |

### Braintrust

| Resource | Framework | Why it matters |
|---|---|---|
| [Braintrust Docs](https://www.braintrust.dev/docs) | Braintrust | Braintrust helps teams manage repeated eval cycles and evidence across agent workflow pilots. |
| [Braintrust SDK GitHub](https://github.com/braintrustdata/braintrust-sdk-javascript) | Braintrust | The SDK repo gives implementation context for recording evals and experiments from applications. |

### Claude Code

| Resource | Framework | Why it matters |
|---|---|---|
| [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code | Useful for non-official ecosystem discovery when labeled separately from Anthropic-owned sources. |
| [Claude Code Docs](https://code.claude.com/docs) | Claude Code | Primary source for Claude Code workflow and usage guidance. |
| [Claude Code Headless](https://code.claude.com/docs/en/headless) | Claude Code | Important for automation-oriented skills and CI workflows. |
| [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks) | Claude Code | Hooks are a useful reference point for approval, validation, and automation boundaries. |
| [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp) | Claude Code | Shows how Claude Code connects to tools and context through MCP. |
| [Claude Code Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory) | Claude Code | Memory affects how skills, instructions, and project preferences persist across agent work. |
| [Claude Code Settings Docs](https://docs.anthropic.com/en/docs/claude-code/settings) | Claude Code | Settings are part of the runtime boundary that skill authors need to understand. |
| [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) | Claude Code | Subagents are a useful comparison point for skill routing and workflow specialization. |

### Cloudflare Workers

| Resource | Framework | Why it matters |
|---|---|---|
| [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/) | Cloudflare Workers | Workers can host lightweight tool adapters, routing layers, and policy checks around skill-backed workflows. |

### Codex

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Codex](https://github.com/openai/codex) | Codex | Codex is a core coding-agent workflow surface for skill-driven repo work. |
| [OpenAI Codex Docs](https://developers.openai.com/codex) | Codex | Provides lab-owned guidance for Codex workflows and setup. |

### Composio

| Resource | Framework | Why it matters |
|---|---|---|
| [Composio Docs](https://docs.composio.dev/) | Composio | Shows how connector-heavy agent workflows can expose external actions safely. |
| [Composio GitHub](https://github.com/ComposioHQ/composio) | Composio | Provides source context for agent connector and tool integration patterns. |

### CrewAI

| Resource | Framework | Why it matters |
|---|---|---|
| [CrewAI Docs](https://docs.crewai.com/) | CrewAI | Shows how role-based and flow-based agent workflows can be captured as reusable skill recipes. |
| [CrewAI GitHub](https://github.com/crewAIInc/crewAI) | CrewAI | Provides source context for CrewAI framework usage and project structure. |

### Cursor

| Resource | Framework | Why it matters |
|---|---|---|
| [Cursor Agent Skills](https://cursor.com/docs/context/skills) | Cursor | Primary source for Cursor's skill model. |
| [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools) | Cursor | Helps distinguish skills from callable editor tools. |
| [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent) | Cursor | Background agents show how skill guidance can support asynchronous coding work. |
| [Cursor Rules Docs](https://docs.cursor.com/en/context/rules) | Cursor | Rules are an important adjacent concept for skill-like guidance in IDE agents. |

### DeepEval

| Resource | Framework | Why it matters |
|---|---|---|
| [DeepEval Docs](https://deepeval.com/docs/getting-started) | DeepEval | DeepEval is relevant for teams that want CI-style eval tests around agent or skill outputs. |
| [DeepEval GitHub](https://github.com/confident-ai/deepeval) | DeepEval | The repo provides source-backed implementation context for LLM app testing. |

### Fly.io

| Resource | Framework | Why it matters |
|---|---|---|
| [Fly.io Docs](https://fly.io/docs/) | Fly.io | Containerized agent services often need hosting, secrets, logs, and rollback practices beyond local skill execution. |

### GAIA

| Resource | Framework | Why it matters |
|---|---|---|
| [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | GAIA | GAIA gives broad context for assistant tasks that require reasoning and tool use. |

### Gemini

| Resource | Framework | Why it matters |
|---|---|---|
| [Gemini API Docs](https://ai.google.dev/gemini-api/docs) | Gemini | Provider-level setup reference for Gemini-backed agent workflows. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Gemini | Represents Gemini-powered terminal-agent workflows. |
| [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs) | Gemini | Useful for terminal-agent setup, configuration, and workflow guidance. |

### GitHub Copilot

| Resource | Framework | Why it matters |
|---|---|---|
| [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | GitHub Copilot | Shows how skills are installed and selected for Copilot cloud agent and related GitHub surfaces. |
| [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | GitHub Copilot | Connects terminal-native Copilot workflows to the broader skill ecosystem. |
| [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | GitHub Copilot | Defines Copilot's skill model and helps compare it with other agent-skill runtimes. |
| [GitHub Copilot Docs](https://docs.github.com/en/copilot) | GitHub Copilot | Provides the official source for Copilot's coding-agent and customization surfaces. |
| [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp) | GitHub Copilot | Explains how MCP extends Copilot across IDE, CLI, app, cloud agent, and code review surfaces. |
| [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | GitHub Copilot | Helps readers distinguish persistent repository guidance from portable agent skills. |
| [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills) | GitHub Copilot | Shows how programmatic Copilot sessions can compose skills with MCP servers and hooks. |

### Google ADK

| Resource | Framework | Why it matters |
|---|---|---|
| [Google ADK Agents Docs](https://google.github.io/adk-docs/agents/) | Google ADK | Helps compare how Google structures agents and agent workflow components. |
| [Google ADK Python](https://github.com/google/adk-python) | Google ADK | Source-backed reference for Google's agent development patterns. |
| [Google ADK Tools Docs](https://google.github.io/adk-docs/tools/) | Google ADK | Tool concepts help readers distinguish skill instructions from callable capabilities. |
| [Google Agent Development Kit Docs](https://google.github.io/adk-docs/) | Google ADK | Provides official Google guidance for building agents, tools, and workflows. |

### Google Vertex AI Agent Builder

| Resource | Framework | Why it matters |
|---|---|---|
| [Google Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform) | Google Vertex AI Agent Builder | Google Cloud managed agent and enterprise search surfaces are relevant for deploying skill-adjacent workflows with cloud governance. |
| [Vertex AI Agent Engine Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview) | Google Vertex AI Agent Builder | Agent Engine documentation helps teams understand managed deployment, operation, and integration choices for agent workflows. |

### Governance

| Resource | Framework | Why it matters |
|---|---|---|
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Governance | Useful background for teams creating approval, governance, and rollout processes for agent skills. |

### Guardrails AI

| Resource | Framework | Why it matters |
|---|---|---|
| [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs) | Guardrails AI | Shows runtime validation patterns that can protect skill-backed workflows. |
| [Guardrails AI GitHub](https://github.com/guardrails-ai/guardrails) | Guardrails AI | Provides source context for guardrail implementation and validator patterns. |

### HELM

| Resource | Framework | Why it matters |
|---|---|---|
| [HELM GitHub](https://github.com/stanford-crfm/helm) | HELM | The repo helps readers inspect benchmark methodology and implementation details. |
| [HELM Latest](https://crfm.stanford.edu/helm/latest/) | HELM | HELM is useful context for model-level scenario and metric design. |

### Haystack

| Resource | Framework | Why it matters |
|---|---|---|
| [Haystack Docs](https://docs.haystack.deepset.ai/docs/intro) | Haystack | Shows how production retrieval and pipeline workflows can be reviewed before skill adoption. |
| [Haystack GitHub](https://github.com/deepset-ai/haystack) | Haystack | Provides source context for production RAG and agent pipeline patterns. |

### Hermes

| Resource | Framework | Why it matters |
|---|---|---|
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Hermes | Shows a skills-oriented self-improving agent architecture. |
| [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md) | Hermes | Memory boundaries are closely related to reusable skill behavior. |
| [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md) | Hermes | Shows how Hermes documents built-in skills and their roles. |
| [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | Hermes | Defines how Hermes exposes and manages skills. |

### HumanLayer

| Resource | Framework | Why it matters |
|---|---|---|
| [HumanLayer GitHub](https://github.com/humanlayer/humanlayer) | HumanLayer | Provides source context for approval gates and human review patterns around tool calls. |

### Inspect AI

| Resource | Framework | Why it matters |
|---|---|---|
| [Inspect AI Docs](https://inspect.aisi.org.uk/) | Inspect AI | Inspect AI is useful for teams that need custom tasks, solvers, scorers, and reproducible eval logs. |

### Lakera

| Resource | Framework | Why it matters |
|---|---|---|
| [Lakera Docs](https://docs.lakera.ai/) | Lakera | Adds source-backed coverage for runtime protection and prompt injection defense. |

### LangChain / LangGraph

| Resource | Framework | Why it matters |
|---|---|---|
| [LangGraph Human-in-the-loop Docs](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop) | LangChain / LangGraph | Provides a framework reference for approval gates and human-supervised agent workflows. |
| [LangGraph Persistence Docs](https://docs.langchain.com/oss/python/langgraph/persistence) | LangChain / LangGraph | State and persistence are central concepts for durable agent workflows and skill handoffs. |

### LangChain/LangGraph

| Resource | Framework | Why it matters |
|---|---|---|
| [LangChain Agents](https://www.langchain.com/agents) | LangChain/LangGraph | Explains LangGraph's role in agent orchestration. |
| [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | LangChain/LangGraph | Shows how MCP tooling can plug into LangChain and LangGraph workflows. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | LangChain/LangGraph | Source-backed reference for graph-based agent orchestration. |
| [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview) | LangChain/LangGraph | Explains stateful agent graphs and durable workflow concepts. |

### LangSmith

| Resource | Framework | Why it matters |
|---|---|---|
| [LangSmith Docs](https://docs.langchain.com/langsmith/observability) | LangSmith | Gives teams a source-backed way to collect trace and eval evidence for skill-backed workflows. |

### Langfuse

| Resource | Framework | Why it matters |
|---|---|---|
| [Langfuse Docs](https://langfuse.com/docs) | Langfuse | Helps teams review prompt and tool-call behavior before expanding an agent workflow. |
| [Langfuse GitHub](https://github.com/langfuse/langfuse) | Langfuse | Provides source context for Langfuse deployment and LLM observability implementation. |

### LlamaFirewall

| Resource | Framework | Why it matters |
|---|---|---|
| [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall) | LlamaFirewall | Adds runtime protection coverage for LLM application safety review. |

### LlamaIndex

| Resource | Framework | Why it matters |
|---|---|---|
| [LlamaIndex Docs](https://developers.llamaindex.ai/python/framework/) | LlamaIndex | Covers the data and retrieval layer that many agent skills need to reference safely. |
| [LlamaIndex GitHub](https://github.com/run-llama/llama_index) | LlamaIndex | Provides source context for RAG agent and data workflow examples. |

### MCP

| Resource | Framework | Why it matters |
|---|---|---|
| [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) | MCP | Gives provider-owned context for MCP as an agent-tool bridge. |
| [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP | Useful for seeing the breadth of MCP servers, while clearly marked as community-maintained. |
| [Model Context Protocol Docs](https://modelcontextprotocol.io/) | MCP | Primary source for tool/context protocol concepts. |
| [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro) | MCP | Gives readers a starting point for understanding MCP as a tool and context layer for agents. |
| [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP | Source-backed reference for MCP specification and docs. |

### MLCommons AILuminate

| Resource | Framework | Why it matters |
|---|---|---|
| [MLCommons AILuminate](https://mlcommons.org/ailuminate/) | MLCommons AILuminate | AILuminate adds source-backed safety benchmark context for risk and governance discussions. |

### Microsoft AutoGen

| Resource | Framework | Why it matters |
|---|---|---|
| [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/stable/) | Microsoft AutoGen | Documents a major multi-agent ecosystem whose workflows can be translated into reusable skill guidance. |
| [Microsoft AutoGen GitHub](https://github.com/microsoft/autogen) | Microsoft AutoGen | Provides source code and examples for AutoGen agent applications and multi-agent workflows. |

### Modal

| Resource | Framework | Why it matters |
|---|---|---|
| [Modal Docs](https://modal.com/docs) | Modal | Modal is useful for Python-heavy skill-backed data, model, and evaluation workflows with bounded execution. |

### Multi-Framework

| Resource | Framework | Why it matters |
|---|---|---|
| [Agent Skill Exchange](https://agentskillexchange.com/) | Multi-Framework | Provides the human-facing discovery layer for the canonical ASE skills catalog. |
| [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills) | Multi-Framework | This companion repo should point readers to the canonical skill source of truth. |
| [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification) | Multi-Framework | Shows how ASE separates listed skills from security-reviewed skills. |

### OWASP LLM Top 10

| Resource | Framework | Why it matters |
|---|---|---|
| [OWASP LLM Top 10 GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) | OWASP LLM Top 10 | Provides source context for LLM application risk categories used in skill safety review. |

### Observability

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) | Observability | Gives teams vocabulary for traces, metrics, and evidence around agent workflows. |

### OpenAI Agents

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/) | OpenAI Agents | Shows source-backed patterns for tools, handoffs, guardrails, tracing, and agent execution. |
| [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python) | OpenAI Agents | Provides source code and examples for OpenAI agent workflows. |
| [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools) | OpenAI Agents | Helps distinguish model tools from higher-level skills and workflows. |

### OpenAI Agents SDK

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents) | OpenAI Agents SDK | Useful for learning how a major provider frames agent design, tool use, and orchestration. |

### OpenAI Apps SDK

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Apps SDK Docs](https://developers.openai.com/apps-sdk/) | OpenAI Apps SDK | Helps readers understand app and tool surfaces adjacent to agent skill workflows. |

### OpenAI Evals

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Evals GitHub](https://github.com/openai/evals) | OpenAI Evals | The repository gives readers a source-backed implementation reference for eval workflows. |
| [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals) | OpenAI Evals | OpenAI Evals guidance helps teams build repeatable checks for OpenAI-backed agent and skill workflows. |

### OpenClaw

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenClaw Docs](https://docs.openclaw.ai/) | OpenClaw | Explains OpenClaw providers, skills, tools, crons, and runtime setup. |
| [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation) | OpenClaw | Example of tool-specific runtime documentation that skills can wrap into workflows. |
| [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai) | OpenClaw | Provider setup affects how skills run across agent runtimes. |
| [OpenClaw Repository](https://github.com/openclaw/openclaw) | OpenClaw | Source-backed reference for OpenClaw runtime and contribution details. |

### PurpleLlama

| Resource | Framework | Why it matters |
|---|---|---|
| [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama) | PurpleLlama | Provides source context for Meta LLM safety and runtime protection tooling. |

### PyRIT

| Resource | Framework | Why it matters |
|---|---|---|
| [PyRIT Docs](https://azure.github.io/PyRIT/) | PyRIT | Supports repeatable risk identification and evidence gathering for agent workflows. |
| [PyRIT GitHub](https://github.com/Azure/PyRIT) | PyRIT | Provides source context for Microsoft red-team tooling around generative AI systems. |

### Pydantic AI

| Resource | Framework | Why it matters |
|---|---|---|
| [Pydantic AI Docs](https://pydantic.dev/docs/ai/overview/) | Pydantic AI | Gives Python teams a typed approach to agent workflows that can be reviewed as code. |
| [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai) | Pydantic AI | Provides source context for typed Python agent and evaluation patterns. |

### Ragas

| Resource | Framework | Why it matters |
|---|---|---|
| [Ragas Docs](https://docs.ragas.io/) | Ragas | Ragas is relevant for skills that retrieve, ground, summarize, or answer from documents. |
| [Ragas GitHub](https://github.com/vibrantlabsai/ragas) | Ragas | The repo helps readers inspect RAG evaluation implementation details and examples. |

### SWE-bench

| Resource | Framework | Why it matters |
|---|---|---|
| [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench) | SWE-bench | The repo helps readers inspect benchmark setup instead of relying on leaderboard claims alone. |
| [SWE-bench Site](https://www.swebench.com/) | SWE-bench | SWE-bench is useful context for evaluating coding-agent and repository patch workflows. |

### Security

| Resource | Framework | Why it matters |
|---|---|---|
| [OWASP Top 10 For LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) | Security | Provides a practical security checklist for skills that use tools, prompts, data, or code execution. |

### Semantic Kernel

| Resource | Framework | Why it matters |
|---|---|---|
| [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/) | Semantic Kernel | Shows how enterprise agent workflows use plugins, functions, planners, memory, and application integration. |
| [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel) | Semantic Kernel | Provides source context for Semantic Kernel app and agent orchestration patterns. |

### Strands Agents

| Resource | Framework | Why it matters |
|---|---|---|
| [Strands Agents Docs](https://strandsagents.com/) | Strands Agents | Adds SDK-level agent workflow coverage for teams comparing tool, hook, and observability patterns. |
| [Strands Agents GitHub](https://github.com/strands-agents/harness-sdk) | Strands Agents | Provides source context for Strands agent SDK workflow patterns. |

### Vercel AI Gateway

| Resource | Framework | Why it matters |
|---|---|---|
| [Vercel AI Gateway Docs](https://vercel.com/docs/ai-gateway) | Vercel AI Gateway | Adds model gateway and policy-layer coverage for teams operating skill-backed AI applications. |

### Vercel AI SDK

| Resource | Framework | Why it matters |
|---|---|---|
| [Vercel AI GitHub](https://github.com/vercel/ai) | Vercel AI SDK | Provides source context for Vercel AI SDK patterns used in AI apps and agent workflows. |
| [Vercel AI SDK Docs](https://ai-sdk.dev/docs) | Vercel AI SDK | Shows how skill-backed workflows can become application features with tool calling and deployment. |

### Vercel Platform

| Resource | Framework | Why it matters |
|---|---|---|
| [Vercel Deployments Docs](https://vercel.com/docs/deployments) | Vercel Platform | Preview deployments are useful evidence points before rolling out skill-backed AI app workflows. |
| [Vercel Functions Docs](https://vercel.com/docs/functions) | Vercel Platform | Function limits, runtime behavior, and environment handling shape how agent workflows should be hosted. |
| [Vercel Platform Docs](https://vercel.com/docs) | Vercel Platform | Helps teams understand how hosted AI apps and skill-backed workflows are deployed, configured, and operated on Vercel. |

### Weights & Biases Weave

| Resource | Framework | Why it matters |
|---|---|---|
| [Weights & Biases Weave Docs](https://docs.wandb.ai/weave) | Weights & Biases Weave | Helps teams connect agent workflow evidence to experiment and eval review. |
| [Weights & Biases Weave GitHub](https://github.com/wandb/weave) | Weights & Biases Weave | Provides source context for Weave tracing and evaluation implementation. |

### Zapier

| Resource | Framework | Why it matters |
|---|---|---|
| [Zapier Docs](https://docs.zapier.com/) | Zapier | Gives teams a source-backed reference for SaaS workflow automation around agent output. |

### garak

| Resource | Framework | Why it matters |
|---|---|---|
| [garak GitHub](https://github.com/NVIDIA/garak) | garak | Adds source-backed coverage for adversarial LLM testing and vulnerability discovery. |

### n8n

| Resource | Framework | Why it matters |
|---|---|---|
| [n8n Docs](https://docs.n8n.io/) | n8n | Helps teams compare deterministic AI workflow automation with agent orchestration. |
| [n8n GitHub](https://github.com/n8n-io/n8n) | n8n | Provides source context for self-hosted workflow automation and connector patterns. |

### promptfoo

| Resource | Framework | Why it matters |
|---|---|---|
| [promptfoo Docs](https://www.promptfoo.dev/docs/intro/) | promptfoo | Helps teams test prompt and agent workflow behavior before rollout. |
| [promptfoo GitHub](https://github.com/promptfoo/promptfoo) | promptfoo | Provides source context for prompt and LLM application evaluation workflows. |

### τ-bench

| Resource | Framework | Why it matters |
|---|---|---|
| [τ-bench GitHub](https://github.com/sierra-research/tau-bench) | τ-bench | Tool-agent benchmarks help teams think about state, tool calls, and task success before building local evals. |

## By Tag

- **actions**: [Zapier Docs](https://docs.zapier.com/)
- **adapters**: [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- **adk**: [Google ADK Python](https://github.com/google/adk-python), [Google Agent Development Kit Docs](https://google.github.io/adk-docs/)
- **agent**: [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools), [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- **agent-engine**: [Vertex AI Agent Engine Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- **agents**: [AgentBench GitHub](https://github.com/THUDM/AgentBench), [Agno Docs](https://docs.agno.com/), [Agno GitHub](https://github.com/agno-agi/agno), [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview), [Azure AI Foundry Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/), [CrewAI Docs](https://docs.crewai.com/), [CrewAI GitHub](https://github.com/crewAIInc/crewAI), [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [Google ADK Agents Docs](https://google.github.io/adk-docs/agents/), [Google ADK Tools Docs](https://google.github.io/adk-docs/tools/), [Google Agent Development Kit Docs](https://google.github.io/adk-docs/), [Haystack Docs](https://docs.haystack.deepset.ai/docs/intro), [LangChain Agents](https://www.langchain.com/agents), [LangGraph](https://github.com/langchain-ai/langgraph), [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview), [LlamaIndex Docs](https://developers.llamaindex.ai/python/framework/), [LlamaIndex GitHub](https://github.com/run-llama/llama_index), [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/stable/), [Microsoft AutoGen GitHub](https://github.com/microsoft/autogen), [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents), [Pydantic AI Docs](https://pydantic.dev/docs/ai/overview/), [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai), [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/), [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel), [Strands Agents Docs](https://strandsagents.com/), [Strands Agents GitHub](https://github.com/strands-agents/harness-sdk), [Vercel AI GitHub](https://github.com/vercel/ai), [Vercel AI SDK Docs](https://ai-sdk.dev/docs), [τ-bench GitHub](https://github.com/sierra-research/tau-bench)
- **agents-sdk**: [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/), [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python)
- **ai-sdk**: [Vercel AI GitHub](https://github.com/vercel/ai), [Vercel AI SDK Docs](https://ai-sdk.dev/docs)
- **anthropic**: [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), [Claude Code Docs](https://code.claude.com/docs), [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp), [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- **api**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- **approval**: [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks), [HumanLayer GitHub](https://github.com/humanlayer/humanlayer), [LangGraph Human-in-the-loop Docs](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop)
- **apps**: [OpenAI Apps SDK Docs](https://developers.openai.com/apps-sdk/)
- **assistant-tasks**: [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard)
- **auth**: [Composio Docs](https://docs.composio.dev/)
- **automation**: [Claude Code Headless](https://code.claude.com/docs/en/headless), [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks), [Composio Docs](https://docs.composio.dev/)
- **aws**: [AWS Bedrock Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- **azure**: [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview), [Azure AI Foundry Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- **background-agent**: [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent)
- **benchmark**: [AgentBench GitHub](https://github.com/THUDM/AgentBench), [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard), [HELM GitHub](https://github.com/stanford-crfm/helm), [HELM Latest](https://crfm.stanford.edu/helm/latest/), [MLCommons AILuminate](https://mlcommons.org/ailuminate/), [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench), [SWE-bench Site](https://www.swebench.com/), [τ-bench GitHub](https://github.com/sierra-research/tau-bench)
- **catalog**: [Agent Skill Exchange](https://agentskillexchange.com/), [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills), [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md)
- **chatgpt**: [OpenAI Apps SDK Docs](https://developers.openai.com/apps-sdk/)
- **claude-code**: [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code), [Claude Code Docs](https://code.claude.com/docs), [Claude Code Headless](https://code.claude.com/docs/en/headless), [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks), [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp), [Claude Code Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory), [Claude Code Settings Docs](https://docs.anthropic.com/en/docs/claude-code/settings), [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- **cli**: [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs), [OpenAI Codex](https://github.com/openai/codex)
- **cloud-agent**: [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- **codex**: [OpenAI Codex](https://github.com/openai/codex), [OpenAI Codex Docs](https://developers.openai.com/codex)
- **coding-agent**: [GitHub Copilot Docs](https://docs.github.com/en/copilot), [OpenAI Codex](https://github.com/openai/codex)
- **coding-agents**: [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench), [SWE-bench Site](https://www.swebench.com/)
- **community**: [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code), [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- **configuration**: [Claude Code Settings Docs](https://docs.anthropic.com/en/docs/claude-code/settings)
- **connectors**: [Composio Docs](https://docs.composio.dev/), [Composio GitHub](https://github.com/ComposioHQ/composio), [n8n Docs](https://docs.n8n.io/), [n8n GitHub](https://github.com/n8n-io/n8n), [Zapier Docs](https://docs.zapier.com/)
- **containers**: [Fly.io Docs](https://fly.io/docs/)
- **context**: [Claude Code Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory), [Cursor Rules Docs](https://docs.cursor.com/en/context/rules), [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp), [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
- **credentials**: [n8n Docs](https://docs.n8n.io/)
- **cursor**: [Cursor Agent Skills](https://cursor.com/docs/context/skills), [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools), [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent), [Cursor Rules Docs](https://docs.cursor.com/en/context/rules)
- **data**: [LlamaIndex Docs](https://developers.llamaindex.ai/python/framework/)
- **datasets**: [Braintrust Docs](https://www.braintrust.dev/docs)
- **deployment**: [AWS Bedrock Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview), [Azure AI Foundry Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/), [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/), [Fly.io Docs](https://fly.io/docs/), [Google Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform), [Modal Docs](https://modal.com/docs), [Vercel AI SDK Docs](https://ai-sdk.dev/docs), [Vercel Deployments Docs](https://vercel.com/docs/deployments), [Vercel Functions Docs](https://vercel.com/docs/functions), [Vercel Platform Docs](https://vercel.com/docs), [Vertex AI Agent Engine Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- **docs**: [Claude Code Docs](https://code.claude.com/docs), [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs), [GitHub Copilot Docs](https://docs.github.com/en/copilot), [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md), [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol), [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools), [OpenClaw Docs](https://docs.openclaw.ai/)
- **edge**: [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- **enterprise**: [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- **enterprise-search**: [Google Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- **environment-variables**: [Vercel Platform Docs](https://vercel.com/docs)
- **eval-framework**: [Inspect AI Docs](https://inspect.aisi.org.uk/)
- **evals**: [Arize Phoenix Docs](https://arize.com/docs/phoenix), [Arize Phoenix GitHub](https://github.com/Arize-ai/phoenix), [Langfuse Docs](https://langfuse.com/docs), [LangSmith Docs](https://docs.langchain.com/langsmith/observability), [OpenAI Evals GitHub](https://github.com/openai/evals), [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals), [promptfoo Docs](https://www.promptfoo.dev/docs/intro/), [promptfoo GitHub](https://github.com/promptfoo/promptfoo), [Pydantic AI Docs](https://pydantic.dev/docs/ai/overview/), [PyRIT Docs](https://azure.github.io/PyRIT/), [Weights & Biases Weave Docs](https://docs.wandb.ai/weave), [Weights & Biases Weave GitHub](https://github.com/wandb/weave)
- **evaluation**: [AgentBench GitHub](https://github.com/THUDM/AgentBench), [Azure AI Foundry Docs](https://learn.microsoft.com/en-us/azure/ai-foundry/), [Braintrust Docs](https://www.braintrust.dev/docs), [Braintrust SDK GitHub](https://github.com/braintrustdata/braintrust-sdk-javascript), [DeepEval Docs](https://deepeval.com/docs/getting-started), [DeepEval GitHub](https://github.com/confident-ai/deepeval), [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard), [Haystack Docs](https://docs.haystack.deepset.ai/docs/intro), [HELM GitHub](https://github.com/stanford-crfm/helm), [HELM Latest](https://crfm.stanford.edu/helm/latest/), [Inspect AI Docs](https://inspect.aisi.org.uk/), [MLCommons AILuminate](https://mlcommons.org/ailuminate/), [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), [OpenAI Evals GitHub](https://github.com/openai/evals), [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals), [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/), [Ragas Docs](https://docs.ragas.io/), [Ragas GitHub](https://github.com/vibrantlabsai/ragas), [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench), [SWE-bench Site](https://www.swebench.com/), [τ-bench GitHub](https://github.com/sierra-research/tau-bench)
- **evidence**: [Vercel Deployments Docs](https://vercel.com/docs/deployments)
- **experiments**: [Braintrust Docs](https://www.braintrust.dev/docs), [Braintrust SDK GitHub](https://github.com/braintrustdata/braintrust-sdk-javascript), [Weights & Biases Weave Docs](https://docs.wandb.ai/weave)
- **framework**: [Google ADK Agents Docs](https://google.github.io/adk-docs/agents/)
- **functions**: [Vercel Functions Docs](https://vercel.com/docs/functions), [Vercel Platform Docs](https://vercel.com/docs)
- **gateway**: [Vercel AI Gateway Docs](https://vercel.com/docs/ai-gateway)
- **gemini**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs)
- **genai**: [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- **github**: [Braintrust SDK GitHub](https://github.com/braintrustdata/braintrust-sdk-javascript), [DeepEval GitHub](https://github.com/confident-ai/deepeval), [HELM GitHub](https://github.com/stanford-crfm/helm), [OpenAI Evals GitHub](https://github.com/openai/evals), [Ragas GitHub](https://github.com/vibrantlabsai/ragas), [SWE-bench GitHub](https://github.com/SWE-bench/SWE-bench)
- **github-copilot**: [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [GitHub Copilot Docs](https://docs.github.com/en/copilot), [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp), [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions), [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills)
- **google**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs), [Google ADK Python](https://github.com/google/adk-python), [Google Agent Development Kit Docs](https://google.github.io/adk-docs/)
- **google-adk**: [Google ADK Agents Docs](https://google.github.io/adk-docs/agents/), [Google ADK Tools Docs](https://google.github.io/adk-docs/tools/)
- **google-cloud**: [Google Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform), [Vertex AI Agent Engine Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- **governance**: [MLCommons AILuminate](https://mlcommons.org/ailuminate/), [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP LLM Top 10 GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications)
- **grounding**: [Ragas Docs](https://docs.ragas.io/)
- **guardrails**: [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs), [Guardrails AI GitHub](https://github.com/guardrails-ai/guardrails), [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall), [OWASP Top 10 For LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **handoffs**: [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents)
- **headless**: [Claude Code Headless](https://code.claude.com/docs/en/headless)
- **hermes**: [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md), [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md), [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
- **hooks**: [Claude Code Hooks Docs](https://docs.anthropic.com/en/docs/claude-code/hooks)
- **hosting**: [Fly.io Docs](https://fly.io/docs/), [Vercel Platform Docs](https://vercel.com/docs)
- **human-in-the-loop**: [HumanLayer GitHub](https://github.com/humanlayer/humanlayer), [LangGraph Human-in-the-loop Docs](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop)
- **iam**: [AWS Bedrock Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- **ide**: [Cursor Agent Skills](https://cursor.com/docs/context/skills), [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent)
- **image-generation**: [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation)
- **instructions**: [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- **jobs**: [Modal Docs](https://modal.com/docs)
- **knowledge**: [Agno Docs](https://docs.agno.com/)
- **lab**: [OpenAI Codex Docs](https://developers.openai.com/codex)
- **langchain**: [LangChain Agents](https://www.langchain.com/agents), [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters), [LangGraph](https://github.com/langchain-ai/langgraph)
- **langgraph**: [LangChain Agents](https://www.langchain.com/agents), [LangGraph](https://github.com/langchain-ai/langgraph), [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview), [LangGraph Human-in-the-loop Docs](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop), [LangGraph Persistence Docs](https://docs.langchain.com/oss/python/langgraph/persistence)
- **llm**: [OWASP Top 10 For LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama)
- **llm-risk**: [OWASP LLM Top 10 GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications)
- **llm-tests**: [DeepEval Docs](https://deepeval.com/docs/getting-started), [DeepEval GitHub](https://github.com/confident-ai/deepeval)
- **managed-agents**: [AWS Bedrock Agents Docs](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), [Azure AI Foundry Agents Overview](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/overview), [Google Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- **marketplace**: [Agent Skill Exchange](https://agentskillexchange.com/)
- **mcp**: [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers), [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp), [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp), [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters), [Model Context Protocol Docs](https://modelcontextprotocol.io/), [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro), [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol), [OpenAI Apps SDK Docs](https://developers.openai.com/apps-sdk/)
- **memory**: [Agno Docs](https://docs.agno.com/), [Claude Code Memory Docs](https://docs.anthropic.com/en/docs/claude-code/memory), [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md)
- **metrics**: [DeepEval Docs](https://deepeval.com/docs/getting-started), [DeepEval GitHub](https://github.com/confident-ai/deepeval), [HELM Latest](https://crfm.stanford.edu/helm/latest/)
- **model-evaluation**: [HELM GitHub](https://github.com/stanford-crfm/helm), [HELM Latest](https://crfm.stanford.edu/helm/latest/)
- **model-routing**: [Vercel AI Gateway Docs](https://vercel.com/docs/ai-gateway)
- **monitoring**: [LangSmith Docs](https://docs.langchain.com/langsmith/observability)
- **multi-agent**: [CrewAI Docs](https://docs.crewai.com/), [CrewAI GitHub](https://github.com/crewAIInc/crewAI), [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/stable/), [Microsoft AutoGen GitHub](https://github.com/microsoft/autogen)
- **multi-environment**: [AgentBench GitHub](https://github.com/THUDM/AgentBench)
- **observability**: [Arize Phoenix Docs](https://arize.com/docs/phoenix), [Arize Phoenix GitHub](https://github.com/Arize-ai/phoenix), [Braintrust Docs](https://www.braintrust.dev/docs), [Langfuse Docs](https://langfuse.com/docs), [Langfuse GitHub](https://github.com/langfuse/langfuse), [LangSmith Docs](https://docs.langchain.com/langsmith/observability), [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/), [Strands Agents Docs](https://strandsagents.com/), [Weights & Biases Weave Docs](https://docs.wandb.ai/weave), [Weights & Biases Weave GitHub](https://github.com/wandb/weave)
- **openai**: [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents), [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/), [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python), [OpenAI Codex Docs](https://developers.openai.com/codex), [OpenAI Evals GitHub](https://github.com/openai/evals), [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals), [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools), [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai)
- **openclaw**: [OpenClaw Docs](https://docs.openclaw.ai/), [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation), [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai), [OpenClaw Repository](https://github.com/openclaw/openclaw)
- **orchestration**: [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/)
- **persistence**: [LangGraph Persistence Docs](https://docs.langchain.com/oss/python/langgraph/persistence)
- **pipelines**: [Haystack Docs](https://docs.haystack.deepset.ai/docs/intro), [Haystack GitHub](https://github.com/deepset-ai/haystack)
- **plugins**: [Semantic Kernel Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/), [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- **policy**: [Lakera Docs](https://docs.lakera.ai/), [Vercel AI Gateway Docs](https://vercel.com/docs/ai-gateway)
- **preview**: [Vercel Deployments Docs](https://vercel.com/docs/deployments)
- **prompt-injection**: [Lakera Docs](https://docs.lakera.ai/), [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall), [promptfoo Docs](https://www.promptfoo.dev/docs/intro/)
- **prompts**: [Langfuse Docs](https://langfuse.com/docs)
- **protocol**: [Model Context Protocol Docs](https://modelcontextprotocol.io/), [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
- **provider**: [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai)
- **providers**: [Vercel AI Gateway Docs](https://vercel.com/docs/ai-gateway)
- **python**: [Google ADK Python](https://github.com/google/adk-python), [Modal Docs](https://modal.com/docs), [Pydantic AI Docs](https://pydantic.dev/docs/ai/overview/), [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai)
- **quality**: [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
- **rag**: [Arize Phoenix Docs](https://arize.com/docs/phoenix), [Haystack Docs](https://docs.haystack.deepset.ai/docs/intro), [Haystack GitHub](https://github.com/deepset-ai/haystack), [LlamaIndex Docs](https://developers.llamaindex.ai/python/framework/), [LlamaIndex GitHub](https://github.com/run-llama/llama_index), [Ragas Docs](https://docs.ragas.io/), [Ragas GitHub](https://github.com/vibrantlabsai/ragas)
- **red-team**: [garak GitHub](https://github.com/NVIDIA/garak), [promptfoo Docs](https://www.promptfoo.dev/docs/intro/), [promptfoo GitHub](https://github.com/promptfoo/promptfoo), [PyRIT Docs](https://azure.github.io/PyRIT/), [PyRIT GitHub](https://github.com/Azure/PyRIT)
- **regression**: [DeepEval Docs](https://deepeval.com/docs/getting-started), [Inspect AI Docs](https://inspect.aisi.org.uk/), [OpenAI Evals Guide](https://platform.openai.com/docs/guides/evals)
- **repo**: [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills), [Agno GitHub](https://github.com/agno-agi/agno), [Arize Phoenix GitHub](https://github.com/Arize-ai/phoenix), [Composio GitHub](https://github.com/ComposioHQ/composio), [CrewAI GitHub](https://github.com/crewAIInc/crewAI), [garak GitHub](https://github.com/NVIDIA/garak), [Guardrails AI GitHub](https://github.com/guardrails-ai/guardrails), [Haystack GitHub](https://github.com/deepset-ai/haystack), [HumanLayer GitHub](https://github.com/humanlayer/humanlayer), [Langfuse GitHub](https://github.com/langfuse/langfuse), [LlamaIndex GitHub](https://github.com/run-llama/llama_index), [Microsoft AutoGen GitHub](https://github.com/microsoft/autogen), [n8n GitHub](https://github.com/n8n-io/n8n), [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python), [OpenClaw Repository](https://github.com/openclaw/openclaw), [OWASP LLM Top 10 GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications), [promptfoo GitHub](https://github.com/promptfoo/promptfoo), [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama), [Pydantic AI GitHub](https://github.com/pydantic/pydantic-ai), [PyRIT GitHub](https://github.com/Azure/PyRIT), [Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel), [Strands Agents GitHub](https://github.com/strands-agents/harness-sdk), [Vercel AI GitHub](https://github.com/vercel/ai), [Weights & Biases Weave GitHub](https://github.com/wandb/weave)
- **repository**: [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- **resources**: [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
- **retrieval**: [Ragas Docs](https://docs.ragas.io/), [Ragas GitHub](https://github.com/vibrantlabsai/ragas)
- **risk**: [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), [OWASP Top 10 For LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- **rollout**: [Vercel Deployments Docs](https://vercel.com/docs/deployments)
- **rules**: [Cursor Rules Docs](https://docs.cursor.com/en/context/rules)
- **runtime**: [Claude Code Settings Docs](https://docs.anthropic.com/en/docs/claude-code/settings), [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/), [Fly.io Docs](https://fly.io/docs/), [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs), [Lakera Docs](https://docs.lakera.ai/), [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall), [OpenClaw Docs](https://docs.openclaw.ai/), [OpenClaw Repository](https://github.com/openclaw/openclaw), [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama), [Vercel Functions Docs](https://vercel.com/docs/functions), [Vertex AI Agent Engine Overview](https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview)
- **safety**: [MLCommons AILuminate](https://mlcommons.org/ailuminate/), [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- **scorers**: [Inspect AI Docs](https://inspect.aisi.org.uk/)
- **sdk**: [Braintrust SDK GitHub](https://github.com/braintrustdata/braintrust-sdk-javascript), [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills), [Strands Agents Docs](https://strandsagents.com/), [Strands Agents GitHub](https://github.com/strands-agents/harness-sdk)
- **security**: [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification), [garak GitHub](https://github.com/NVIDIA/garak), [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs), [Lakera Docs](https://docs.lakera.ai/), [LlamaFirewall](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall), [OWASP LLM Top 10 GitHub](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications), [OWASP Top 10 For LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), [PurpleLlama GitHub](https://github.com/meta-llama/PurpleLlama), [PyRIT Docs](https://azure.github.io/PyRIT/), [PyRIT GitHub](https://github.com/Azure/PyRIT)
- **serverless**: [Modal Docs](https://modal.com/docs), [Vercel Functions Docs](https://vercel.com/docs/functions)
- **servers**: [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- **settings**: [Claude Code Settings Docs](https://docs.anthropic.com/en/docs/claude-code/settings)
- **skills**: [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [Agent Skill Exchange](https://agentskillexchange.com/), [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills), [Cursor Agent Skills](https://cursor.com/docs/context/skills), [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md), [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md), [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
- **software-engineering**: [SWE-bench Site](https://www.swebench.com/)
- **spec**: [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
- **state**: [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview), [LangGraph Persistence Docs](https://docs.langchain.com/oss/python/langgraph/persistence)
- **subagents**: [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- **terminal-agent**: [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- **testing**: [garak GitHub](https://github.com/NVIDIA/garak), [promptfoo Docs](https://www.promptfoo.dev/docs/intro/), [PyRIT Docs](https://azure.github.io/PyRIT/)
- **tool-use**: [GAIA Leaderboard](https://huggingface.co/spaces/gaia-benchmark/leaderboard), [τ-bench GitHub](https://github.com/sierra-research/tau-bench)
- **tools**: [Agno Docs](https://docs.agno.com/), [Agno GitHub](https://github.com/agno-agi/agno), [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), [Composio Docs](https://docs.composio.dev/), [Composio GitHub](https://github.com/ComposioHQ/composio), [CrewAI Docs](https://docs.crewai.com/), [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools), [Google ADK Tools Docs](https://google.github.io/adk-docs/tools/), [HumanLayer GitHub](https://github.com/humanlayer/humanlayer), [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/stable/), [Model Context Protocol Docs](https://modelcontextprotocol.io/), [Model Context Protocol Introduction](https://modelcontextprotocol.io/docs/getting-started/intro), [OpenAI Agents Guide](https://platform.openai.com/docs/guides/agents), [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/), [OpenAI Apps SDK Docs](https://developers.openai.com/apps-sdk/), [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools), [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation), [Pydantic AI Docs](https://pydantic.dev/docs/ai/overview/), [Strands Agents Docs](https://strandsagents.com/), [Vercel AI SDK Docs](https://ai-sdk.dev/docs)
- **traces**: [Arize Phoenix Docs](https://arize.com/docs/phoenix), [Langfuse Docs](https://langfuse.com/docs), [Langfuse GitHub](https://github.com/langfuse/langfuse), [LangSmith Docs](https://docs.langchain.com/langsmith/observability), [Weights & Biases Weave Docs](https://docs.wandb.ai/weave)
- **tracing**: [OpenTelemetry GenAI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- **triggers**: [n8n Docs](https://docs.n8n.io/)
- **validation**: [Guardrails AI Docs](https://guardrailsai.com/guardrails/docs), [Guardrails AI GitHub](https://github.com/guardrails-ai/guardrails)
- **verification**: [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
- **workers**: [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/)
- **workflow-automation**: [n8n Docs](https://docs.n8n.io/), [n8n GitHub](https://github.com/n8n-io/n8n), [Zapier Docs](https://docs.zapier.com/)
- **workflows**: [CrewAI Docs](https://docs.crewai.com/), [LangGraph Human-in-the-loop Docs](https://docs.langchain.com/oss/python/langgraph/human-in-the-loop), [LangGraph Persistence Docs](https://docs.langchain.com/oss/python/langgraph/persistence), [LlamaIndex Docs](https://developers.llamaindex.ai/python/framework/), [Microsoft AutoGen Docs](https://microsoft.github.io/autogen/stable/)
