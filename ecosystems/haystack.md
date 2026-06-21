# Haystack

Haystack is a framework for building production AI pipelines, RAG systems, and
agent workflows.

## Where It Fits

Haystack fits the pipeline, retrieval, and production RAG layer. It is useful
when workflows need components, document stores, tools, evaluators, and
deployment-minded pipeline structure.

## Skill-Like Concepts

- pipelines
- components and tools
- agents
- RAG and document stores
- evaluators
- tracing and monitoring integrations
- MCP serving patterns

## Best Fit

- production RAG workflows
- document search and question answering
- extraction and summarization pipelines
- teams that need reusable components rather than one-off prompts

## When Not To Use It

- simple coding-agent instructions
- workflows with no retrieval or pipeline need
- production workflows without evaluation data

## Safety And Rollout

- Review document sources and access controls.
- Keep evaluation sets for retrieval quality.
- Monitor pipeline failures and low-confidence outputs.
- Require human review for external or customer-facing output.

## Source Links

- [Haystack docs](https://docs.haystack.deepset.ai/docs/intro)
- [Haystack GitHub](https://github.com/deepset-ai/haystack)

## Relation To Skills

A skill can wrap a Haystack workflow by explaining pipeline setup, data access,
evaluation evidence, and the operational checks needed before adoption.
