# Langfuse

Langfuse is an LLM engineering platform for tracing, prompt management, evals,
and observability.

## Where It Fits In Agent Operations

Langfuse fits the agent observability and evaluation layer. It helps teams
review traces, prompt/tool behavior, feedback, and quality signals.

## Skill-Adjacent Concepts

- traces and spans
- prompt management
- evals and scores
- datasets
- production monitoring
- feedback loops

## Best Fit

- teams needing open-source-friendly LLM observability
- agent pilots that need trace evidence
- workflows with prompt and tool-call review

## When Not To Use It

- purely deterministic automations
- workflows where traces cannot be stored
- teams without a review process for collected telemetry

## Safety And Rollout

- Define what data may be captured.
- Review retention and access controls.
- Use evals for regression checks, not only dashboards.
- Attach run evidence to rollout decisions.

## Source Links

- [Langfuse docs](https://langfuse.com/docs)
- [Langfuse GitHub](https://github.com/langfuse/langfuse)

## Relation To Skills

A skill can point to required Langfuse traces or eval scores as acceptance
evidence for a pilot.
