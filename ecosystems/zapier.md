# Zapier

Zapier is a workflow automation and integration platform for connecting apps,
actions, triggers, and AI-assisted workflows.

## Where It Fits In Agent Operations

Zapier fits the connector and automation layer. It is useful when a workflow
mostly moves data between apps or triggers known actions.

## Skill-Adjacent Concepts

- triggers
- actions
- app connectors
- workflow automation
- AI-assisted automation
- external messages and writes
- approval or review steps by workflow design

## Best Fit

- SaaS automation
- low-code operational workflows
- routing data between business systems
- deterministic workflows around AI output

## When Not To Use It

- workflows needing deep agent planning
- custom code-heavy orchestration
- sensitive writes without clear approval evidence

## Safety And Rollout

- Review app permissions and connected accounts.
- Separate draft/review from send/write actions.
- Log task history and external side effects.
- Add approval before customer-facing or production changes.

## Source Links

- [Zapier docs](https://docs.zapier.com/)

## Relation To Skills

A skill can document when a Zapier workflow should run, what it changes, and
what evidence reviewers need before enabling it for a team.
