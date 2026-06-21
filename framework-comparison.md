# Framework Comparison

This matrix compares where major agent skill surfaces fit. It is a practical
orientation guide, not a vendor ranking.

| Framework or surface | Primary surface | Best fit | Skill support / skill-like support | MCP/tool support | Team rollout considerations | Source links |
|---|---|---|---|---|---|---|
| Codex | Terminal coding agent and repo workflow | Codebase inspection, edits, tests, patches, and implementation loops | Skills and repo instructions work best when commands and verification are explicit | Strong fit for CLIs, local tools, APIs, and MCP clients when configured | Use bounded worktrees, test evidence, review diffs, and avoid broad refactors | [Guide](frameworks/codex.md), [openai/codex](https://github.com/openai/codex) |
| Claude Code | Coding agent for project workflows and automation | Project-local development, headless runs, MCP, and coding workflows | Project workflows, subagents, instructions, and skill-like reusable guidance | Anthropic docs cover MCP usage with Claude Code | Review permissions, headless automation scope, generated diffs, and CI evidence | [Guide](frameworks/claude-code.md), [Claude Code docs](https://code.claude.com/docs) |
| GitHub Copilot | GitHub, IDE, CLI, cloud agent, and SDK surfaces | GitHub-native issues, PRs, code review, release notes, and Copilot CLI | Official GitHub docs describe agent skills and skill directories for Copilot surfaces | GitHub documents MCP across IDE, CLI, app, cloud agent, and code review | Review organization policies, repository permissions, MCP policy, and PR approval flow | [Guide](frameworks/github-copilot.md), [Copilot docs](https://docs.github.com/en/copilot) |
| OpenClaw | Agent runtime for providers, tools, channels, crons, and skills | Scheduled operations, multi-provider routing, Telegram/runtime workflows, and automation | Native runtime skills and cron-driven workflows | Tool integrations, providers, browser/search/image tools, and runtime-managed capabilities | Treat crons as production automation; require health checks, logs, rollback, and owner allowlists | [Guide](frameworks/openclaw.md), [OpenClaw docs](https://docs.openclaw.ai/) |
| Hermes | Self-improving personal agent runtime | Persistent personal agent workflows, memory, and skill evolution | Hermes documents skills and bundled skill catalog concepts | Tooling depends on runtime setup and configured integrations | Define memory boundaries, persistence rules, and review points before trusting autonomous updates | [Guide](frameworks/hermes.md), [Hermes Agent](https://github.com/NousResearch/hermes-agent) |
| Cursor | IDE agent environment | Editor-first coding, context rules, project changes, and background agents | Cursor documents agent skills and rules/context features | Agent tools and MCP-style integrations depend on project/editor setup | Keep project rules precise; validate edits with local tests and PR review | [Guide](frameworks/cursor.md), [Cursor skills docs](https://cursor.com/docs/context/skills) |
| Gemini CLI | Terminal agent from Google | Terminal-native repo analysis, command loops, and Google-backed agent workflows | Skill-like usage depends on repo instructions and reusable command guidance | CLI, APIs, and tool calls depend on local setup | Keep credentials scoped, record commands, and verify generated changes | [Guide](frameworks/gemini.md), [Gemini CLI](https://github.com/google-gemini/gemini-cli) |
| LangChain / LangGraph | Agent orchestration framework | Stateful workflows, graph-based agents, durable orchestration, and evaluation loops | Skills are usually workflow modules or reusable agent/tool instructions rather than runtime-native skill folders | Strong tool and MCP adapter ecosystem | Design state, retries, observability, and approval boundaries before production use | [Guide](frameworks/langchain-langgraph.md), [LangGraph](https://github.com/langchain-ai/langgraph) |
| MCP | Tool and context protocol | Connecting agents to tools, APIs, data, and context providers | MCP is not itself a skill system; skills often wrap MCP setup and usage patterns | Native purpose is tool/context integration | Review server trust, auth scopes, tool allowlists, and data access before rollout | [Guide](frameworks/mcp.md), [MCP docs](https://modelcontextprotocol.io/) |
| OpenAI Agents SDK | Agent framework and SDK | Tools, handoffs, guardrails, tracing, and programmatic agent execution | Skill-like patterns appear as reusable tools, prompts, runbooks, and evaluation harnesses | Tool calling and integrations are first-class SDK concerns | Validate traces, guardrails, tool permissions, and human approval paths | [Agents SDK docs](https://openai.github.io/openai-agents-python/), [Repo](https://github.com/openai/openai-agents-python) |
| Google ADK | Agent development kit | Google ecosystem agent apps, tools, and multi-agent workflows | Skill-like behavior is usually encoded through reusable agent instructions, tools, and workflow modules | Tool support depends on ADK setup and Google integrations | Review credentials, deployment target, and provider-specific policies | [ADK docs](https://google.github.io/adk-docs/), [ADK Python](https://github.com/google/adk-python) |

## Adjacent Agent Ecosystems

These ecosystems are not always skill-native, but they shape how reusable agent
workflows are designed, reviewed, and adopted.

| Ecosystem | Primary surface | Best fit | Skill-like support | Source links |
|---|---|---|---|---|
| CrewAI | Crews, flows, tasks, and role-based agents | Business workflows and multi-agent process automation | Roles, tasks, tools, memory, knowledge, guardrails, and flows can be wrapped as reusable skill recipes | [Guide](ecosystems/crewai.md), [Docs](https://docs.crewai.com/) |
| Microsoft AutoGen | Multi-agent framework, AgentChat, Core, Studio, and extensions | Research prototypes and multi-agent applications | Agent teams, tools, code execution, Studio workflows, and MCP workbench patterns | [Guide](ecosystems/autogen.md), [Docs](https://microsoft.github.io/autogen/stable/) |
| Semantic Kernel | Application SDK for agents, plugins, functions, planners, and processes | Enterprise app integration and Microsoft-oriented stacks | Plugins, functions, prompt templates, memory, and processes map well to reusable instructions | [Guide](ecosystems/semantic-kernel.md), [Docs](https://learn.microsoft.com/en-us/semantic-kernel/overview/) |
| LlamaIndex | Data, retrieval, tools, agents, workflows, and evaluation | RAG agents, data workflows, and structured extraction | Data sources, indexes, retrievers, agents, tools, evals, and workflows become reusable skill patterns | [Guide](ecosystems/llamaindex.md), [Docs](https://developers.llamaindex.ai/python/framework/) |
| Pydantic AI | Typed Python agents, tools, outputs, evals, and graph workflows | Python agent apps with testable structured outputs | Typed tools, schemas, evals, durable execution, and approval patterns support skill-like reuse | [Guide](ecosystems/pydantic-ai.md), [Docs](https://pydantic.dev/docs/ai/overview/) |
| Haystack | RAG, pipelines, components, tools, agents, and evaluators | Production retrieval and document workflows | Pipelines, tools, document stores, evaluators, and MCP serving can be documented as repeatable workflows | [Guide](ecosystems/haystack.md), [Docs](https://docs.haystack.deepset.ai/docs/intro) |
| Strands Agents | Agent SDK with tools, hooks, observability, and coding-agent setup | SDK-based agent apps and observable tool use | Tools, hooks, traces, and app-owned runtime policy can be captured as skills | [Guide](ecosystems/strands-agents.md), [Docs](https://strandsagents.com/) |
| Agno | Agent apps with tools, memory, knowledge, models, and multi-agent patterns | Lightweight agent apps and fast framework comparison | Tools, knowledge, memory, and multi-agent setup can be described as reusable workflow guidance | [Guide](ecosystems/agno.md), [Docs](https://docs.agno.com/) |

## How To Use This Matrix

- If you are learning, start with the surface you already use.
- If you are adopting as a team, start with the risk model and rollout path, not
  the newest feature.
- If you are writing skills, make the workflow portable where possible but avoid
  claiming multi-framework support without evidence.
- If you are operating skill-backed workflows, use [Agent Ops](ops/) for traces,
  evals, approvals, workflow automation, model gateways, and rollout evidence.
- If you are deploying skill-backed workflows, use [Deployment](deployment/) for
  runtime hosting, sandboxing, secrets, provider comparison, and readiness checks.
