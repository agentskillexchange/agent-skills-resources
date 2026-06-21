# CrewAI

CrewAI is an agent framework for building crews, flows, tasks, and role-based
agent workflows.

## Where It Fits

CrewAI sits in the orchestration layer. It is useful when a workflow is easier
to express as roles, tasks, and coordinated steps instead of one long prompt.

## Skill-Like Concepts

- agents with roles and goals
- tasks and crews
- flows for controlled workflow execution
- tools and integrations
- memory and knowledge
- guardrails and observability integrations

## Best Fit

- repeated business workflows
- multi-step research or operations tasks
- agent teams with clear roles
- workflows that benefit from explicit task structure

## When Not To Use It

- one-off coding edits
- workflows where a single deterministic script is enough
- high-risk production writes without human approval and logs

## Safety And Rollout

- Start with read-only tools.
- Name which agent can call which tool.
- Log task outputs and final decisions.
- Add human approval before writes, external messages, or production actions.

## Source Links

- [CrewAI docs](https://docs.crewai.com/)
- [CrewAI GitHub](https://github.com/crewAIInc/crewAI)

## Relation To Skills

A skill can wrap a CrewAI workflow by describing when to use it, how to install
dependencies, which tools are required, and what evidence proves the crew ran
correctly.
