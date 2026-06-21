# Strands Agents

Strands Agents is an agent SDK ecosystem with agent, tool, hook, observability,
and coding-agent-oriented setup patterns.

## Where It Fits

Strands fits the SDK and application layer. It is useful when developers want to
compose agent behavior in code while preserving hooks and operational review
points.

## Skill-Like Concepts

- agents
- tools
- SDK workflows
- hooks
- observability
- coding-agent setup guidance
- runtime policy by application design

## Best Fit

- SDK-based agent apps
- teams that want hooks and observable execution
- workflows where tool calls need application-level control

## When Not To Use It

- static documentation tasks
- simple local coding-agent edits
- workflows without a developer-owned app surface

## Safety And Rollout

- Review hooks and tool permissions.
- Keep logs and traces for agent steps.
- Start with read-only tools.
- Require human approval for production side effects.

## Source Links

- [Strands Agents docs](https://strandsagents.com/)
- [Strands Agents GitHub](https://github.com/strands-agents/harness-sdk)

## Relation To Skills

A skill can describe how to run or review a Strands agent workflow, including
the tool surface, hooks, required setup, and verification evidence.
