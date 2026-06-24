# Awesome Agent Skills

A concise, source-backed guide to agent skills, MCP tools, coding agents, agent
frameworks, evaluation, safety, deployment, and rollout playbooks.

This is the shareable front door for the independent
[agent-skills-resources](README.md) guide. It is not the full catalog. Browse
the canonical skill catalog in [agentskillexchange/skills](https://github.com/agentskillexchange/skills)
or on [Agent Skill Exchange](https://agentskillexchange.com/).

## Start Here

| Need | Link |
|---|---|
| Learn the concept | [Agent Skills 101](learning/agent-skills-101.md) |
| Compare skills, tools, MCP, agents, and workflows | [Skills vs Tools vs MCP](learning/skills-vs-tools-vs-mcp.md) |
| Compare framework surfaces | [Framework Comparison](framework-comparison.md) |
| Review official/source-backed resources | [Resource Index](generated/resource-index.md) |
| Evaluate skill quality and safety | [Quality Checklist](examples/quality-checklist.md) |
| Plan a team pilot | [Playbooks](playbooks/) |

## What Are Agent Skills?

Agent skills are reusable instructions, scripts, examples, and workflow notes
that help an agent do repeatable work. A useful skill explains the source
project, setup steps, safe usage, verification evidence, and when to stop for
human review.

Skills sit between broad prompts and raw tools:

- prompts tell an agent what you want
- tools give an agent callable capabilities
- MCP connects tools and context
- skills describe when and how to use those capabilities for a repeatable
  workflow

## Official Skill And Runtime Docs

| Resource | Why it matters |
|---|---|
| [GitHub Copilot agent skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) | GitHub's skill model for Copilot surfaces. |
| [Adding agent skills for GitHub Copilot](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | Creating, adding, managing, and reviewing Copilot skills. |
| [GitHub Copilot CLI skills](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills) | Skill usage in terminal-native Copilot CLI workflows. |
| [Cursor Agent Skills](https://cursor.com/docs/context/skills) | Cursor's skill model for IDE agent workflows. |
| [Hermes Skills Feature Docs](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md) | Hermes Agent skill behavior and boundaries. |
| [OpenClaw Docs](https://docs.openclaw.ai/) | Runtime, provider, tool, and cron concepts for OpenClaw workflows. |

## Coding-Agent Skill Surfaces

| Surface | Start here | Good fit |
|---|---|---|
| Codex | [Codex guide](frameworks/codex.md) | Terminal-first repo work, tests, patch review, and implementation loops. |
| Claude Code | [Claude Code guide](frameworks/claude-code.md) | Project workflows, headless automation, MCP, and coding-agent operations. |
| GitHub Copilot | [GitHub Copilot guide](frameworks/github-copilot.md) | GitHub-native issues, PRs, code review, Copilot CLI, and SDK sessions. |
| OpenClaw | [OpenClaw guide](frameworks/openclaw.md) | Runtime ops, crons, channels, provider routing, and scheduled automation. |
| Hermes | [Hermes guide](frameworks/hermes.md) | Self-improving agent workflows, memory, and persistent skill usage. |
| Cursor | [Cursor guide](frameworks/cursor.md) | IDE context, rules, background agents, and project-local coding workflows. |
| Gemini CLI | [Gemini guide](frameworks/gemini.md) | Google-backed terminal-agent workflows. |

## MCP And Tool-Context Resources

| Resource | Why it matters |
|---|---|
| [Model Context Protocol Docs](https://modelcontextprotocol.io/) | Core protocol for connecting tools and context to agents. |
| [Model Context Protocol Repository](https://github.com/modelcontextprotocol/modelcontextprotocol) | Source-backed MCP specification and documentation repository. |
| [GitHub Copilot MCP Docs](https://docs.github.com/en/copilot/concepts/context/mcp) | MCP support across Copilot IDE, CLI, app, cloud agent, and code review surfaces. |
| [Claude Code MCP Docs](https://docs.anthropic.com/en/docs/claude-code/mcp) | Anthropic-owned Claude Code MCP guidance. |
| [LangChain MCP Adapters](https://github.com/langchain-ai/langchain-mcp-adapters) | LangChain ecosystem adapter reference for MCP. |

## Skill Quality And Verification

- Start with a real upstream source, not a category idea.
- Include install/setup steps that help users install the upstream tool, not
  only copy a Markdown folder.
- Explain permissions, secrets, local files, network access, and write actions.
- Include verification steps with observable output.
- Avoid stale stars, download counts, or "official" claims unless they are
  source-backed.
- Use [ASE Verification](https://github.com/agentskillexchange/skills/tree/main/verification)
  and the [quality checklist](examples/quality-checklist.md) for review.

## Team Rollout And Adoption

| Need | Start here |
|---|---|
| Pick a first workflow | [Adoption Matrix](adoption-matrix.md) |
| Run a bounded pilot | [Playbooks](playbooks/) |
| Record evidence | [Evaluation Templates](templates/) |
| Review risks | [Security Review Template](templates/security-review.md) |
| Compare surfaces | [Framework Comparison](framework-comparison.md) |

## Representative ASE Examples

These are examples, not a catalog dump:

- [`staff-engineer-mode`](https://agentskillexchange.com/skills/staff-engineer-mode/)
- [`run-terminal-native-coding-agent-workflows-with-github-copilot-cli`](https://agentskillexchange.com/skills/run-terminal-native-coding-agent-workflows-with-github-copilot-cli/)
- [`postgresql-mcp-server`](https://agentskillexchange.com/skills/postgresql-mcp-server/)
- [`route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`](https://agentskillexchange.com/skills/route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer/)
- [`investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`](https://agentskillexchange.com/skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt/)
- [`run-a-self-improving-personal-agent-with-hermes-agent`](https://agentskillexchange.com/skills/run-a-self-improving-personal-agent-with-hermes-agent/)

## Browse The Full Catalog

- [Agent Skill Exchange](https://agentskillexchange.com/)
- [Browse skills](https://agentskillexchange.com/browse-skills/)
- [Canonical skills repo](https://github.com/agentskillexchange/skills)
- [Representative mapping index](generated/ase-skill-mapping-index.md)
