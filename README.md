# Agent Skills Resources

An independent public learning hub for agent skills, AI agents, agent workflows,
MCP, coding agents, skill design, skill evaluation, agent safety, and rollout
playbooks.

Use this repo to understand the concepts, compare skill surfaces, review
source-backed resources, and design safer team pilots. The separate
[agentskillexchange/skills](https://github.com/agentskillexchange/skills) repo
is the canonical skills catalog, and [Agent Skill Exchange](https://agentskillexchange.com/)
is the public site.

[![Source labels](https://img.shields.io/badge/sources-Official%20%7C%20Lab%20%7C%20Community%20%7C%20ASE-0f766e?style=for-the-badge)](data/resources.json)
[![Companion repo](https://img.shields.io/badge/companion-resource%20hub-2563eb?style=for-the-badge)](https://github.com/agentskillexchange/skills)

Start with [Learning Paths](learning/), the [Glossary](glossary.md), or the
[Best-Practices Cookbook](cookbook/).

## Start Here In 60 Seconds

1. Read [Agent Skills 101](learning/agent-skills-101.md).
2. Compare [skills vs tools vs MCP](learning/skills-vs-tools-vs-mcp.md).
3. Use the [Glossary](glossary.md) to normalize vocabulary.
4. Review the [Best-Practices Cookbook](cookbook/).
5. Pick a team path from [Starter Kits](starter-kits/) or [Playbooks](playbooks/).

## What You Can Learn Here

- What agent skills are and where they fit in the agent ecosystem.
- How skills differ from tools, MCP servers, runtimes, and workflows.
- How to design source-backed skills with clear setup, permissions, and evidence.
- How to evaluate skill quality without relying on popularity claims.
- How teams can pilot agent workflows with sandboxing, approval gates, and rollout checks.
- Where to find official framework, MCP, safety, observability, and adoption resources.

## About This Repo

This is a source-backed educational guide for agent skills and AI agent
workflows. It provides learning paths, visual maps, examples, rollout playbooks,
evaluation templates, source-labeling guidance, and a curated resource index.
It is not a catalog mirror and does not try to track every published skill.

## What You'll Find Here

| Need | Start here |
|---|---|
| Learn the agent skills ecosystem | [Learning Paths](learning/) |
| Understand terminology | [Glossary](glossary.md) |
| Design better skills | [Best-Practices Cookbook](cookbook/) |
| Compare Codex, Claude Code, GitHub Copilot, OpenClaw, Hermes, Cursor, Gemini CLI, LangChain, LangGraph, MCP, and OpenAI Agents SDK | [Framework pages](frameworks/) |
| Review source-backed resources | [Resource Index](generated/resource-index.md) |
| Evaluate skill quality and agent safety | [Quality Checklist](examples/quality-checklist.md) |
| Run a bounded rollout | [Playbooks](playbooks/) and [Templates](templates/) |

## I Want To

| Goal | Go here |
|---|---|
| Understand agent skills | [Agent Skills 101](learning/agent-skills-101.md) |
| Learn the vocabulary | [Glossary](glossary.md) |
| Build a first skill | [Skill Design Patterns](learning/skill-design-patterns.md) |
| Compare frameworks | [Framework Comparison](framework-comparison.md) |
| See workflow stacks | [Showcase Workflow Stacks](showcase/) |
| Find official resources | [Resource Index](generated/resource-index.md) |
| Review skill quality | [Skill Evaluation Basics](learning/skill-evaluation-basics.md) |
| Build a skill | [Skill Author Starter Kit](starter-kits/skill-author.md) and [Cookbook](cookbook/) |
| Run a team pilot | [Team Evaluation Starter Kit](starter-kits/team-evaluation.md) |
| Browse the canonical catalog | [Agent Skill Exchange](https://agentskillexchange.com/browse-skills/) |

## Use This Repo When

- You want to understand where agent skills fit across AI agents, coding agents,
  MCP, Model Context Protocol, Codex, Claude Code, GitHub Copilot, OpenClaw,
  Hermes Agent, Cursor, Gemini CLI, LangChain, LangGraph, and OpenAI Agents SDK.
- You need source-backed framework resources, visual maps, examples, skill
  evaluation templates, agent safety checks, verification guidance, or rollout
  playbooks.
- You want representative examples without copying the full catalog.

## Do Not Use This Repo For

- The full skill catalog.
- The installable skill source of truth.
- Official vendor claims unless the claim is source-backed.
- Catalog-wide generated skill dumps.

## What This Is

Agent skills are reusable instructions, workflows, and tool-usage patterns that
help agents perform repeatable work. A good skill explains when to use a tool,
how to set it up, what safety checks matter, and how to verify the result.

This repo helps developers answer four questions:

- Where do skills fit in the agent stack?
- Which labs, frameworks, and runtimes support skill-like workflows?
- How should teams evaluate, write, and verify skills?
- Where can I find source-backed examples without confusing them for the main
  ASE catalog?

It covers MCP and the Model Context Protocol, verification, skill evaluation,
rollout playbooks, and practical adoption evidence for teams working with
agentic development and operations.

## How This Differs From `agentskillexchange/skills`

| Repo | Purpose | Use it for |
|---|---|---|
| [agent-skills-resources](https://github.com/agentskillexchange/agent-skills-resources) | Companion guide | Learning, diagrams, framework links, best practices, and curated examples |
| [agentskillexchange/skills](https://github.com/agentskillexchange/skills) | Canonical catalog | Actual skill files, generated indexes, categories, verification, and installable entries |
| [agentskillexchange.com](https://agentskillexchange.com/) | Live marketplace | Browsing, search, skill pages, industry collections, and creation workflows |

## Skill Ecosystem Layers

| Layer | Examples | What skills add |
|---|---|---|
| Model/provider | OpenAI, Anthropic, Google | Model-specific setup and constraints |
| Runtime | Codex, Claude Code, GitHub Copilot, OpenClaw, Hermes, Cursor, Gemini CLI | Repeatable agent workflows |
| Framework | LangGraph, OpenAI Agents SDK, ADK | Orchestration patterns and state |
| Protocol/tooling | MCP, CLIs, APIs, browser tools | Tool setup, permissions, and usage recipes |
| Verification | tests, scans, traces, approvals | Evidence that the workflow worked |

## Ecosystem Map

```mermaid
flowchart LR
  User["User or team"] --> Runtime["Agent runtime"]
  Runtime --> Framework["Agent framework or coding agent"]
  Framework --> Skills["Skills layer"]
  Skills --> Tools["Tools, APIs, CLIs, MCP servers"]
  Skills --> Context["Memory and context"]
  Skills --> Safety["Verification and guardrails"]
  Skills --> Ops["Schedules, crons, deployments"]
  Safety --> Evidence["Tests, scans, logs, citations"]
  Tools --> Outcome["Repeatable workflow outcome"]
  Evidence --> Outcome
```

## Quick Paths

| Path | Start here | What to read next |
|---|---|---|
| New to skills | [Agent Skills 101](learning/agent-skills-101.md) | [Skills vs Tools vs MCP](learning/skills-vs-tools-vs-mcp.md) |
| Learning terms | [Glossary](glossary.md) | [Ecosystem Map](ecosystem-map.md) |
| Skimming the ecosystem | [Awesome Agent Skills](awesome-agent-skills.md) | [Framework Comparison](framework-comparison.md) |
| Seeing workflow stacks | [Showcase Workflow Stacks](showcase/) | [Case Studies](case-studies/) |
| Building a skill | [Skill Design Patterns](learning/skill-design-patterns.md) | [Best-Practices Cookbook](cookbook/) |
| Comparing frameworks | [Framework pages](frameworks/) | [resources.json](data/resources.json) |
| Choosing a starter path | [Starter Kits](starter-kits/) | [Adoption Matrix](adoption-matrix.md) |
| Exploring workflows | [Workflow pages](workflows/) | [ASE skill mapping](data/ase-skill-mapping.json) |
| Applying skills to scenarios | [Case Studies](case-studies/) | [Generated skill mapping index](generated/ase-skill-mapping-index.md) |
| Planning adoption | [Playbooks](playbooks/) | [Adoption Matrix](adoption-matrix.md) |
| Running a pilot | [Evaluation Templates](templates/) | [Template Index](generated/template-index.md) |
| Reviewing quality | [Annotated Examples](examples/annotated-skill-examples.md) | [Quality Checklist](examples/quality-checklist.md) |
| Maintaining resources | [Freshness Audit](maintenance/freshness-audit.md) | [Source Labeling](maintenance/source-labeling.md) |
| Evaluating trust | [Security And Permissions](cookbook/security-and-permissions.md) | [Skill Evaluation Basics](learning/skill-evaluation-basics.md) |
| Contributing | [CONTRIBUTING](CONTRIBUTING.md) | [ASE Create Skill](https://agentskillexchange.com/create-skill/) |

## Framework And Resource Guide

| Area | Role in the ecosystem | Guide |
|---|---|---|
| Codex | Coding agent and terminal workflow runtime | [Codex](frameworks/codex.md) |
| Claude Code | Coding agent with project workflows, tools, and automation | [Claude Code](frameworks/claude-code.md) |
| GitHub Copilot | GitHub-native coding assistant, cloud agent, CLI, SDK, MCP, and skills surface | [GitHub Copilot](frameworks/github-copilot.md) |
| OpenClaw | Agent runtime for providers, crons, skills, tools, and channels | [OpenClaw](frameworks/openclaw.md) |
| Hermes | Self-improving agent with skills, memory, and agent-managed workflows | [Hermes](frameworks/hermes.md) |
| Cursor | IDE agent environment with context, skills, and background agents | [Cursor](frameworks/cursor.md) |
| Gemini CLI | Open-source terminal agent from Google | [Gemini](frameworks/gemini.md) |
| LangChain / LangGraph | Agent orchestration and stateful workflow framework | [LangChain / LangGraph](frameworks/langchain-langgraph.md) |
| MCP | Protocol for connecting agents to tools and context providers | [MCP](frameworks/mcp.md) |

## Source Labels

Every resource in [data/resources.json](data/resources.json) uses one of four
labels:

- `Official`: vendor or project-owned documentation or repository.
- `Lab`: research lab, model provider, or frontier-lab material.
- `Community`: useful third-party material that is not official.
- `ASE`: Agent Skill Exchange site, repo, data, or documentation.

When a claim is not source-backed, leave it out.

## Data Files

- [data/resources.json](data/resources.json): structured source list.
- [data/ase-skill-mapping.json](data/ase-skill-mapping.json): representative
  ASE skill examples by framework and workflow area.
- [learning/](learning/): framework-neutral learning paths for agent skills.
- [glossary.md](glossary.md): concise vocabulary for skill design and adoption.
- [cookbook/](cookbook/): practical best-practice recipes and anti-patterns.
- [diagrams/](diagrams/): framework-neutral Mermaid diagrams.
- [awesome-agent-skills.md](awesome-agent-skills.md): Awesome-style curated
  front door for agent skill resources.
- [framework-comparison.md](framework-comparison.md): practical comparison of
  major skill and agent workflow surfaces.
- [showcase/](showcase/): real-world workflow stacks that combine frameworks,
  skills, pilot notes, and verification evidence.
- [generated/resource-index.md](generated/resource-index.md): generated resource
  index grouped by source type, framework, and tag.
- [generated/ase-skill-mapping-index.md](generated/ase-skill-mapping-index.md):
  generated representative ASE skill index grouped by workflow and framework.
- [generated/nav-index.md](generated/nav-index.md): generated navigation index
  for learning, cookbook, framework, workflow, example, case-study, playbook,
  template, diagram, contributing, and maintenance pages.
- [generated/template-index.md](generated/template-index.md): generated index of
  fillable pilot and review templates.
- [generated/repo-stats.md](generated/repo-stats.md): generated repository data
  snapshot.
- [workflows/](workflows/): visual workflow guides that show how skills fit into
  practical SRE, security, data, content, and research work.
- [case-studies/](case-studies/): practical scenarios that connect 2-4 existing
  ASE skills into reviewable workflows.
- [playbooks/](playbooks/): adoption guides for teams evaluating skill-based
  workflows.
- [starter-kits/](starter-kits/): short paths for coding-agent users, MCP users,
  team evaluators, and skill authors.
- [templates/](templates/): fillable worksheets for evaluation, risk review,
  security review, rollout readiness, and post-pilot review.
- [adoption-matrix.md](adoption-matrix.md): lightweight comparison of starting
  workflows, risk levels, rollout paths, and expected evidence.

## Quality Loop

Use the repo as a small maintenance loop:

1. Add or revise source-backed resources.
2. Map only existing ASE skill slugs.
3. Review examples against the [quality checklist](examples/quality-checklist.md).
4. Run validation and freshness checks.
5. Keep source labels honest when ownership changes.

## Validation

```bash
python3 scripts/validate-resources.py
python3 scripts/validate-links.py
python3 scripts/audit-freshness.py
python3 scripts/generate-resource-index.py
python3 scripts/generate-skill-mapping-index.py
python3 scripts/generate-nav-index.py
python3 scripts/generate-template-index.py
python3 scripts/generate-repo-stats.py
```

## Loop Roadmap

Future loops should expand one area at a time:

1. Deepen Codex, Claude Code, GitHub Copilot, OpenClaw, Hermes, Cursor, Gemini, LangGraph, and MCP pages.
2. Add more ASE skill mappings from the public catalog.
3. Add visual workflow stacks for security, data, SRE, legal, GTM, and support.
4. Add a freshness audit that flags moved docs, stale links, or unsupported claims.
5. Add deeper case studies for teams evaluating adoption paths.
6. Add adoption playbooks for team-specific rollout decisions.
7. Add fillable pilot templates for recording evidence and go/no-go decisions.
8. Add completed evaluation examples and repo stats for stronger first-read clarity.
