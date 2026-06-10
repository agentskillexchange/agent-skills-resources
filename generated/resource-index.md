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
| [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code | Useful for non-official ecosystem discovery when labeled separately from Anthropic-owned sources. |
| [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP | Useful for seeing the breadth of MCP servers, while clearly marked as community-maintained. |

### Lab

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Codex Docs](https://developers.openai.com/codex) | Codex | Provides lab-owned guidance for Codex workflows and setup. |

### Official

| Resource | Framework | Why it matters |
|---|---|---|
| [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | GitHub Copilot | Shows how skills are installed and selected for Copilot cloud agent and related GitHub surfaces. |
| [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | GitHub Copilot | Connects terminal-native Copilot workflows to the broader skill ecosystem. |
| [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) | MCP | Gives provider-owned context for MCP as an agent-tool bridge. |
| [Claude Code Docs](https://code.claude.com/docs) | Claude Code | Primary source for Claude Code workflow and usage guidance. |
| [Claude Code Headless](https://code.claude.com/docs/en/headless) | Claude Code | Important for automation-oriented skills and CI workflows. |
| [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp) | Claude Code | Shows how Claude Code connects to tools and context through MCP. |
| [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) | Claude Code | Subagents are a useful comparison point for skill routing and workflow specialization. |
| [Cursor Agent Skills](https://cursor.com/docs/context/skills) | Cursor | Primary source for Cursor's skill model. |
| [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools) | Cursor | Helps distinguish skills from callable editor tools. |
| [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent) | Cursor | Background agents show how skill guidance can support asynchronous coding work. |
| [Cursor Rules Docs](https://docs.cursor.com/en/context/rules) | Cursor | Rules are an important adjacent concept for skill-like guidance in IDE agents. |
| [Gemini API Docs](https://ai.google.dev/gemini-api/docs) | Gemini | Provider-level setup reference for Gemini-backed agent workflows. |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Gemini | Represents Gemini-powered terminal-agent workflows. |
| [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs) | Gemini | Useful for terminal-agent setup, configuration, and workflow guidance. |
| [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | GitHub Copilot | Defines Copilot's skill model and helps compare it with other agent-skill runtimes. |
| [GitHub Copilot Docs](https://docs.github.com/en/copilot) | GitHub Copilot | Provides the official source for Copilot's coding-agent and customization surfaces. |
| [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp) | GitHub Copilot | Explains how MCP extends Copilot across IDE, CLI, app, cloud agent, and code review surfaces. |
| [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions) | GitHub Copilot | Helps readers distinguish persistent repository guidance from portable agent skills. |
| [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills) | GitHub Copilot | Shows how programmatic Copilot sessions can compose skills with MCP servers and hooks. |
| [Google ADK Python](https://github.com/google/adk-python) | Google ADK | Source-backed reference for Google's agent development patterns. |
| [Google Agent Development Kit Docs](https://google.github.io/adk-docs/) | Google ADK | Provides official Google guidance for building agents, tools, and workflows. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Hermes | Shows a skills-oriented self-improving agent architecture. |
| [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md) | Hermes | Memory boundaries are closely related to reusable skill behavior. |
| [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md) | Hermes | Shows how Hermes documents built-in skills and their roles. |
| [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | Hermes | Defines how Hermes exposes and manages skills. |
| [LangChain Agents](https://www.langchain.com/agents) | LangChain/LangGraph | Explains LangGraph's role in agent orchestration. |
| [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | LangChain/LangGraph | Shows how MCP tooling can plug into LangChain and LangGraph workflows. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | LangChain/LangGraph | Source-backed reference for graph-based agent orchestration. |
| [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview) | LangChain/LangGraph | Explains stateful agent graphs and durable workflow concepts. |
| [Model Context Protocol Docs](https://modelcontextprotocol.io/) | MCP | Primary source for tool/context protocol concepts. |
| [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP | Source-backed reference for MCP specification and docs. |
| [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/) | OpenAI Agents | Shows source-backed patterns for tools, handoffs, guardrails, tracing, and agent execution. |
| [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python) | OpenAI Agents | Provides source code and examples for OpenAI agent workflows. |
| [OpenAI Codex](https://github.com/openai/codex) | Codex | Codex is a core coding-agent workflow surface for skill-driven repo work. |
| [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools) | OpenAI Agents | Helps distinguish model tools from higher-level skills and workflows. |
| [OpenClaw Docs](https://docs.openclaw.ai/) | OpenClaw | Explains OpenClaw providers, skills, tools, crons, and runtime setup. |
| [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation) | OpenClaw | Example of tool-specific runtime documentation that skills can wrap into workflows. |
| [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai) | OpenClaw | Provider setup affects how skills run across agent runtimes. |
| [OpenClaw Repository](https://github.com/openclaw/openclaw) | OpenClaw | Source-backed reference for OpenClaw runtime and contribution details. |

## By Framework

### Claude Code

| Resource | Framework | Why it matters |
|---|---|---|
| [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code) | Claude Code | Useful for non-official ecosystem discovery when labeled separately from Anthropic-owned sources. |
| [Claude Code Docs](https://code.claude.com/docs) | Claude Code | Primary source for Claude Code workflow and usage guidance. |
| [Claude Code Headless](https://code.claude.com/docs/en/headless) | Claude Code | Important for automation-oriented skills and CI workflows. |
| [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp) | Claude Code | Shows how Claude Code connects to tools and context through MCP. |
| [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) | Claude Code | Subagents are a useful comparison point for skill routing and workflow specialization. |

### Codex

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Codex](https://github.com/openai/codex) | Codex | Codex is a core coding-agent workflow surface for skill-driven repo work. |
| [OpenAI Codex Docs](https://developers.openai.com/codex) | Codex | Provides lab-owned guidance for Codex workflows and setup. |

### Cursor

| Resource | Framework | Why it matters |
|---|---|---|
| [Cursor Agent Skills](https://cursor.com/docs/context/skills) | Cursor | Primary source for Cursor's skill model. |
| [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools) | Cursor | Helps distinguish skills from callable editor tools. |
| [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent) | Cursor | Background agents show how skill guidance can support asynchronous coding work. |
| [Cursor Rules Docs](https://docs.cursor.com/en/context/rules) | Cursor | Rules are an important adjacent concept for skill-like guidance in IDE agents. |

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
| [Google ADK Python](https://github.com/google/adk-python) | Google ADK | Source-backed reference for Google's agent development patterns. |
| [Google Agent Development Kit Docs](https://google.github.io/adk-docs/) | Google ADK | Provides official Google guidance for building agents, tools, and workflows. |

### Hermes

| Resource | Framework | Why it matters |
|---|---|---|
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Hermes | Shows a skills-oriented self-improving agent architecture. |
| [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md) | Hermes | Memory boundaries are closely related to reusable skill behavior. |
| [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md) | Hermes | Shows how Hermes documents built-in skills and their roles. |
| [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | Hermes | Defines how Hermes exposes and manages skills. |

### LangChain/LangGraph

| Resource | Framework | Why it matters |
|---|---|---|
| [LangChain Agents](https://www.langchain.com/agents) | LangChain/LangGraph | Explains LangGraph's role in agent orchestration. |
| [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | LangChain/LangGraph | Shows how MCP tooling can plug into LangChain and LangGraph workflows. |
| [LangGraph](https://github.com/langchain-ai/langgraph) | LangChain/LangGraph | Source-backed reference for graph-based agent orchestration. |
| [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview) | LangChain/LangGraph | Explains stateful agent graphs and durable workflow concepts. |

### MCP

| Resource | Framework | Why it matters |
|---|---|---|
| [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp) | MCP | Gives provider-owned context for MCP as an agent-tool bridge. |
| [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) | MCP | Useful for seeing the breadth of MCP servers, while clearly marked as community-maintained. |
| [Model Context Protocol Docs](https://modelcontextprotocol.io/) | MCP | Primary source for tool/context protocol concepts. |
| [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol) | MCP | Source-backed reference for MCP specification and docs. |

### Multi-Framework

| Resource | Framework | Why it matters |
|---|---|---|
| [Agent Skill Exchange](https://agentskillexchange.com/) | Multi-Framework | Provides the human-facing discovery layer for the canonical ASE skills catalog. |
| [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills) | Multi-Framework | This companion repo should point readers to the canonical skill source of truth. |
| [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification) | Multi-Framework | Shows how ASE separates listed skills from security-reviewed skills. |

### OpenAI Agents

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/) | OpenAI Agents | Shows source-backed patterns for tools, handoffs, guardrails, tracing, and agent execution. |
| [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python) | OpenAI Agents | Provides source code and examples for OpenAI agent workflows. |
| [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools) | OpenAI Agents | Helps distinguish model tools from higher-level skills and workflows. |

### OpenClaw

| Resource | Framework | Why it matters |
|---|---|---|
| [OpenClaw Docs](https://docs.openclaw.ai/) | OpenClaw | Explains OpenClaw providers, skills, tools, crons, and runtime setup. |
| [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation) | OpenClaw | Example of tool-specific runtime documentation that skills can wrap into workflows. |
| [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai) | OpenClaw | Provider setup affects how skills run across agent runtimes. |
| [OpenClaw Repository](https://github.com/openclaw/openclaw) | OpenClaw | Source-backed reference for OpenClaw runtime and contribution details. |

## By Tag

- **adapters**: [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters)
- **adk**: [Google ADK Python](https://github.com/google/adk-python), [Google Agent Development Kit Docs](https://google.github.io/adk-docs/)
- **agent**: [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools), [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- **agents**: [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [Google Agent Development Kit Docs](https://google.github.io/adk-docs/), [LangChain Agents](https://www.langchain.com/agents), [LangGraph](https://github.com/langchain-ai/langgraph), [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview)
- **agents-sdk**: [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/), [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python)
- **anthropic**: [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), [Claude Code Docs](https://code.claude.com/docs), [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp), [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- **api**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs)
- **automation**: [Claude Code Headless](https://code.claude.com/docs/en/headless)
- **background-agent**: [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent)
- **catalog**: [Agent Skill Exchange](https://agentskillexchange.com/), [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills), [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md)
- **claude-code**: [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code), [Claude Code Docs](https://code.claude.com/docs), [Claude Code Headless](https://code.claude.com/docs/en/headless), [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp), [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- **cli**: [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs), [OpenAI Codex](https://github.com/openai/codex)
- **cloud-agent**: [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- **codex**: [OpenAI Codex](https://github.com/openai/codex), [OpenAI Codex Docs](https://developers.openai.com/codex)
- **coding-agent**: [GitHub Copilot Docs](https://docs.github.com/en/copilot), [OpenAI Codex](https://github.com/openai/codex)
- **community**: [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code), [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- **context**: [Cursor Rules Docs](https://docs.cursor.com/en/context/rules), [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp)
- **cursor**: [Cursor Agent Skills](https://cursor.com/docs/context/skills), [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools), [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent), [Cursor Rules Docs](https://docs.cursor.com/en/context/rules)
- **docs**: [Claude Code Docs](https://code.claude.com/docs), [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs), [GitHub Copilot Docs](https://docs.github.com/en/copilot), [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md), [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol), [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools), [OpenClaw Docs](https://docs.openclaw.ai/)
- **gemini**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs), [Gemini CLI](https://github.com/google-gemini/gemini-cli), [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli/tree/main/docs)
- **github-copilot**: [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [GitHub Copilot Docs](https://docs.github.com/en/copilot), [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp), [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions), [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills)
- **google**: [Gemini API Docs](https://ai.google.dev/gemini-api/docs), [Google ADK Python](https://github.com/google/adk-python), [Google Agent Development Kit Docs](https://google.github.io/adk-docs/)
- **headless**: [Claude Code Headless](https://code.claude.com/docs/en/headless)
- **hermes**: [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md), [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md), [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
- **ide**: [Cursor Agent Skills](https://cursor.com/docs/context/skills), [Cursor Background Agent Docs](https://docs.cursor.com/en/background-agent)
- **image-generation**: [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation)
- **instructions**: [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- **lab**: [OpenAI Codex Docs](https://developers.openai.com/codex)
- **langchain**: [LangChain Agents](https://www.langchain.com/agents), [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters), [LangGraph](https://github.com/langchain-ai/langgraph)
- **langgraph**: [LangChain Agents](https://www.langchain.com/agents), [LangGraph](https://github.com/langchain-ai/langgraph), [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview)
- **marketplace**: [Agent Skill Exchange](https://agentskillexchange.com/)
- **mcp**: [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers), [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp), [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp), [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters), [Model Context Protocol Docs](https://modelcontextprotocol.io/), [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
- **memory**: [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md)
- **openai**: [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/), [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python), [OpenAI Codex Docs](https://developers.openai.com/codex), [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools), [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai)
- **openclaw**: [OpenClaw Docs](https://docs.openclaw.ai/), [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation), [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai), [OpenClaw Repository](https://github.com/openclaw/openclaw)
- **protocol**: [Model Context Protocol Docs](https://modelcontextprotocol.io/)
- **provider**: [OpenClaw OpenAI Provider](https://docs.openclaw.ai/providers/openai)
- **python**: [Google ADK Python](https://github.com/google/adk-python)
- **quality**: [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
- **repo**: [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills), [OpenAI Agents SDK Repository](https://github.com/openai/openai-agents-python), [OpenClaw Repository](https://github.com/openclaw/openclaw)
- **repository**: [GitHub Copilot Repository Instructions](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions)
- **resources**: [Awesome Claude Code](https://github.com/hesreallyhim/awesome-claude-code)
- **rules**: [Cursor Rules Docs](https://docs.cursor.com/en/context/rules)
- **runtime**: [OpenClaw Docs](https://docs.openclaw.ai/), [OpenClaw Repository](https://github.com/openclaw/openclaw)
- **sdk**: [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills)
- **security**: [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
- **servers**: [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers)
- **skills**: [Adding Agent Skills For GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills), [Adding Agent Skills For GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills), [Agent Skill Exchange](https://agentskillexchange.com/), [AgentSkillExchange Skills](https://github.com/agentskillexchange/skills), [Cursor Agent Skills](https://cursor.com/docs/context/skills), [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills), [GitHub Copilot SDK Custom Skills](https://docs.github.com/en/copilot/how-tos/copilot-sdk/features/skills), [Hermes Agent](https://github.com/NousResearch/hermes-agent), [Hermes Memory Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/memory.md), [Hermes Skills Catalog](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/skills-catalog.md), [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md)
- **spec**: [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol)
- **state**: [LangGraph Docs](https://docs.langchain.com/oss/python/langgraph/overview)
- **subagents**: [Claude Code Subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents)
- **terminal-agent**: [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- **tools**: [Anthropic MCP Docs](https://docs.anthropic.com/en/docs/agents-and-tools/mcp), [Cursor Agent Tools](https://docs.cursor.com/en/agent/tools), [Model Context Protocol Docs](https://modelcontextprotocol.io/), [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/), [OpenAI Tools Guide](https://platform.openai.com/docs/guides/tools), [OpenClaw Image Generation](https://docs.openclaw.ai/tools/image-generation)
- **verification**: [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
