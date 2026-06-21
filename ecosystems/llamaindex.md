# LlamaIndex

LlamaIndex is a data and agent framework for connecting LLM workflows to
documents, indexes, tools, retrieval, and structured data.

## Where It Fits

LlamaIndex fits strongly in the RAG and data-agent layer. It helps when skills
depend on private or structured knowledge rather than only prompt instructions.

## Skill-Like Concepts

- agents and tools
- workflows
- indexes and retrievers
- structured extraction
- evaluation and observability
- human-in-the-loop and MCP-related patterns

## Best Fit

- RAG agents
- document and knowledge workflows
- data extraction and research workflows
- workflows that need retrieval, citations, or structured outputs

## When Not To Use It

- pure coding-agent workflows
- simple CLI automation
- tasks where no retrieval or data layer is needed

## Safety And Rollout

- Review source documents and data access.
- Check retrieval quality, citations, and hallucination risk.
- Keep evaluation examples for important workflows.
- Separate read-only research from write actions.

## Source Links

- [LlamaIndex docs](https://developers.llamaindex.ai/python/framework/)
- [LlamaIndex GitHub](https://github.com/run-llama/llama_index)

## Relation To Skills

A skill can wrap a LlamaIndex workflow by explaining the data sources, retrieval
setup, expected output, and evaluation evidence needed before reuse.
