# Overview

This companion repo explains where agent skills fit in AI agent workflows and
how teams can move from learning to evaluation and rollout. The canonical skill
catalog remains [agentskillexchange/skills](https://github.com/agentskillexchange/skills).

## Ecosystem Map

```mermaid
flowchart LR
  Catalog["ASE skills catalog"] --> Skills["Agent skills"]
  Skills --> Runtimes["Codex, Claude Code, GitHub Copilot, OpenClaw, Hermes, Cursor, Gemini CLI"]
  Skills --> Protocols["MCP and tool protocols"]
  Skills --> Frameworks["LangChain, LangGraph, OpenAI Agents SDK"]
  Skills --> Evidence["Verification, safety, approvals"]
  Skills --> Deployment["Deployment and runtime hosting"]
  Skills --> Evaluation["Evaluation and benchmarks"]
  Runtimes --> Workflows["Coding agents and agent workflows"]
  Protocols --> Workflows
  Frameworks --> Workflows
  Deployment --> Rollout["Skill evaluation and rollout playbooks"]
  Evaluation --> Rollout
  Evidence --> Rollout["Skill evaluation and rollout playbooks"]
```

## Adoption Flow

```mermaid
flowchart LR
  Learn["Learn"] --> Compare["Compare frameworks"]
  Compare --> Evaluate["Evaluate skills"]
  Evaluate --> Pilot["Run a bounded pilot"]
  Pilot --> Rollout["Roll out with evidence"]
  Rollout --> Maintain["Audit freshness and sources"]
```

## Data Snapshot

| Metric | Count |
|---|---:|
| Source-backed resources | 129 |
| Official resources | 117 |
| Lab resources | 3 |
| Community resources | 6 |
| ASE resources | 3 |
| Representative mapped ASE skills | 46 |
| Playbooks | 6 |
| Templates | 8 |
| Generated indexes | 5 |

## Generated Indexes

- [Resource Index](generated/resource-index.md)
- [ASE Skill Mapping Index](generated/ase-skill-mapping-index.md)
- [Navigation Index](generated/nav-index.md)
- [Template Index](generated/template-index.md)
- [Repo Stats](generated/repo-stats.md)

## Public Front Door

- [Awesome Agent Skills](awesome-agent-skills.md): curated source-backed entry
  point for readers who want a fast overview.
- [Framework Comparison](framework-comparison.md): practical matrix for
  choosing the right framework or runtime surface.
- [Deployment](deployment/): runtime hosting, sandboxing, secrets, and rollout
  readiness for skill-backed workflows.
- [Evaluation](evaluation/): benchmark landscape, eval design, regression
  testing, and evidence capture for agent workflows.
- [Showcase Workflow Stacks](showcase/): polished stack examples that combine
  framework resources, representative skills, pilot plans, and verification
  evidence.
- [Starter Kits](starter-kits/): short paths for coding-agent users, MCP users,
  team evaluators, and skill authors.

## Use This Repo For

- Learning how agent skills relate to AI agents, coding agents, tools, MCP, and
  framework runtimes.
- Comparing Codex, Claude Code, GitHub Copilot, OpenClaw, Hermes, Cursor, Gemini CLI,
  LangChain, LangGraph, and OpenAI Agents SDK resources.
- Evaluating skill quality, agent safety, verification evidence, and rollout
  readiness.
- Choosing benchmark and eval evidence without treating leaderboards as workflow
  approval.
- Planning deployment with runtime boundaries, sandboxing, secrets, approvals,
  and rollback evidence.
- Running small pilot workflows with playbooks and templates before production
  adoption.
