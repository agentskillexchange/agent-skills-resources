# Arize Phoenix

Arize Phoenix is an observability and evaluation tool for LLM applications.

## Where It Fits In Agent Operations

Phoenix fits the tracing, evaluation, troubleshooting, and experiment review
layer for LLM and agent workflows.

## Skill-Adjacent Concepts

- traces
- spans
- evals
- datasets
- troubleshooting
- experiment review
- retrieval and tool-call analysis

## Best Fit

- teams diagnosing LLM application behavior
- RAG and agent quality review
- eval-driven pilot decisions

## When Not To Use It

- workflows with no saved run data
- teams that cannot review or retain telemetry
- static skill authoring without runtime use

## Safety And Rollout

- Review data capture and retention.
- Save eval results alongside trace links.
- Use issue examples to improve skills and prompts.
- Keep human review for production side effects.

## Source Links

- [Phoenix docs](https://arize.com/docs/phoenix)
- [Phoenix GitHub](https://github.com/Arize-ai/phoenix)

## Relation To Skills

A skill can require Phoenix traces or eval output as proof that an agent
workflow behaves as expected.
