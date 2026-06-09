# OpenClaw

OpenClaw is an agent runtime for providers, skills, tools, crons, channels, and
long-running operations. It is especially relevant to skill-based workflows
because skills can be part of scheduled or channel-driven automation.

## Role In The Skills Ecosystem

- Agent runtime and operations layer.
- Strong fit for crons, Telegram/other channels, provider routing, skills,
  tools, and durable workspace operations.
- Skills should include operational guardrails, output contracts, and recovery
  checks.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [OpenClaw docs](https://docs.openclaw.ai/) | Documentation hub for OpenClaw setup and tools. |
| Official | [openclaw/openclaw](https://github.com/openclaw/openclaw) | Public OpenClaw repository. |
| ASE | [OpenClaw skills catalog](https://agentskillexchange.com/browse-skills/?framework=OpenClaw) | Live ASE view of OpenClaw skills. |

## Skill Guidance

OpenClaw skills should state:

- provider/runtime assumptions
- whether the task is interactive or scheduled
- command and file boundaries
- health checks
- when to notify a channel

