# LangSmith

LangSmith is an observability and evaluation platform for LLM and agent
applications from LangChain.

## Where It Fits In Agent Operations

LangSmith fits the trace, eval, dataset, and monitoring layer. It helps teams
review what an agent did and compare behavior across runs.

## Skill-Adjacent Concepts

- LLM traces
- tool call inspection
- datasets and evals
- prompt and run comparisons
- production monitoring
- feedback and regression review

## Best Fit

- LangChain/LangGraph-heavy teams
- agent eval workflows
- debugging multi-step tool use
- tracking pilot evidence before rollout

## When Not To Use It

- workflows with no model or tool trace to review
- teams that only need static documentation
- approval workflows without runtime evidence

## Safety And Rollout

- Decide what prompt/output data may be logged.
- Keep sensitive data handling explicit.
- Attach trace links to pilot and rollout reviews.
- Pair traces with eval outcomes before expanding usage.

## Source Links

- [LangSmith docs](https://docs.langchain.com/langsmith/observability)

## Relation To Skills

A skill can require LangSmith trace evidence before a workflow is considered
ready for broader team use.
