# HumanLayer

HumanLayer provides human-in-the-loop approval patterns for agents and tool
calls.

## Where It Fits In Agent Operations

HumanLayer fits the approval and escalation layer. It is relevant when agents
need human review before sensitive actions.

## Skill-Adjacent Concepts

- approval gates
- human review
- tool call authorization
- escalation
- audit evidence
- workflow interruption and resume

## Best Fit

- workflows that can write, deploy, message, or mutate state
- agent tools with high-impact permissions
- pilots that need explicit human approval evidence

## When Not To Use It

- read-only learning workflows
- deterministic scripts with existing approval paths
- workflows where all actions are low risk

## Safety And Rollout

- Define which actions require approval.
- Save approval decisions with context.
- Make reject/revise paths explicit.
- Keep approvals close to trace or diff evidence.

## Source Links

- [HumanLayer GitHub](https://github.com/humanlayer/humanlayer)

## Relation To Skills

A skill can require human approval before invoking risky tools or completing an
external side effect.
