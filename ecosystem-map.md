# Agent Skills Ecosystem Map

Skills sit between a general-purpose agent and the concrete tools, commands, and
workflows the agent needs to operate reliably.

## Stack View

```mermaid
flowchart TB
  L1["Models and providers"]
  L2["Agent runtimes"]
  L3["Agent frameworks"]
  L4["Skills and reusable workflows"]
  L5["Tools, APIs, CLIs, MCP servers"]
  L6["Verification, logs, scans, and evidence"]
  L7["Business or developer outcome"]

  L1 --> L2
  L2 --> L3
  L3 --> L4
  L4 --> L5
  L4 --> L6
  L5 --> L7
  L6 --> L7
```

## Skills Vs Adjacent Concepts

| Concept | What it is | How skills relate |
|---|---|---|
| Agent | The system that plans and acts. | Skills teach the agent repeatable procedures. |
| Tool | A callable function, API, CLI, or MCP server. | Skills explain when and how to use tools safely. |
| MCP | A protocol for connecting tools and context to agents. | Skills can wrap MCP workflows and usage patterns. |
| Workflow | A sequence of steps with checks and outcomes. | Skills turn workflows into reusable instructions. |
| Memory | Stored context, preferences, and history. | Skills can define what to remember and when to retrieve it. |
| Guardrail | A rule, approval, test, or safety check. | Strong skills include verification and escalation points. |

## Practical Roles

```mermaid
flowchart LR
  Skill["Skill"] --> Setup["Install and setup"]
  Skill --> Context["Context to inspect"]
  Skill --> Steps["Workflow steps"]
  Skill --> Checks["Validation checks"]
  Skill --> Escalation["When to ask for help"]
  Checks --> Output["Reliable result"]
  Escalation --> Output
```

## Agent Skill Adoption Loop

```mermaid
flowchart LR
  Discover["Discover source-backed resources"] --> Select["Select one workflow"]
  Select --> Evaluate["Evaluate skill quality and risk"]
  Evaluate --> Pilot["Run bounded pilot"]
  Pilot --> Evidence["Capture evidence"]
  Evidence --> Decide["Reject, revisit, or roll out"]
  Decide --> Maintain["Audit freshness and update sources"]
  Maintain --> Discover
```

## What Makes A Skill Useful

A useful skill is specific enough to execute and broad enough to reuse. It should
name the upstream source, explain installation, show real usage, and state how
to verify the result.

Weak skills usually fail in predictable ways:

- They only say "copy this folder" instead of explaining the upstream tool.
- They claim popularity or official status without a source.
- They skip prerequisites, credentials, or security checks.
- They describe a category instead of a concrete workflow.
