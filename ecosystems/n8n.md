# n8n

n8n is a workflow automation platform for connecting triggers, actions, APIs,
and services.

## Where It Fits In Agent Operations

n8n fits the workflow automation and connector layer. It can automate many
AI-adjacent workflows without requiring a full agent framework.

## Skill-Adjacent Concepts

- triggers
- workflow steps
- connectors
- credentials
- retries
- external side effects
- human review steps

## Best Fit

- deterministic AI workflow automation
- connector-heavy operations
- workflows that need scheduling and SaaS integration
- cases where approval can be inserted into the flow

## When Not To Use It

- open-ended planning tasks
- workflows that need complex agent reasoning
- high-risk automation without audit and rollback

## Safety And Rollout

- Scope credentials per workflow.
- Watch hidden retries and duplicate side effects.
- Log inputs, outputs, and external writes.
- Add human approval before sensitive actions.

## Source Links

- [n8n docs](https://docs.n8n.io/)
- [n8n GitHub](https://github.com/n8n-io/n8n)

## Relation To Skills

A skill can describe how an n8n workflow should be invoked, reviewed, and
verified as part of a larger agent workflow.
