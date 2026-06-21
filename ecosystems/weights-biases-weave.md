# Weights & Biases Weave

Weights & Biases Weave is an LLM application tracing and evaluation tool.

## Where It Fits In Agent Operations

Weave fits the observability, eval, and experiment tracking layer for LLM apps
and agent workflows.

## Skill-Adjacent Concepts

- traces
- model and tool call review
- evaluations
- datasets
- experiment tracking
- production feedback

## Best Fit

- teams already using Weights & Biases
- LLM app and agent experimentation
- workflows where evals and traces need to live near ML experimentation

## When Not To Use It

- connector-only automation
- teams without a review path for captured traces
- workflows where telemetry cannot be stored

## Safety And Rollout

- Decide what run data can be captured.
- Keep sensitive inputs out of broad-access projects.
- Use evals before expanding pilots.
- Preserve links to traces and reports in rollout docs.

## Source Links

- [Weave docs](https://docs.wandb.ai/weave)
- [Weave GitHub](https://github.com/wandb/weave)

## Relation To Skills

A skill can reference Weave traces and evals as operational evidence for team
adoption.
