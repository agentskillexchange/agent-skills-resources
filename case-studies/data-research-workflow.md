# Data Research Workflow

## Practical Scenario

A data or research team wants agents to draft source-backed analysis while
keeping database access, SQL translation, and evidence quality reviewable.

## Relevant ASE Skill Examples

| Skill | Role in the workflow |
|---|---|
| `draft-cited-research-reports-with-storm` | Produces cited research drafts from source collection |
| `run-autonomous-deep-research-workflows-with-gpt-researcher` | Runs broader research workflows with explicit source gathering |
| `query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp` | Connects database inspection to MCP-mediated workflows |
| `translate-and-validate-sql-across-dialects-with-sqlglot` | Checks SQL portability and dialect changes before reuse |

## How They Fit Together

1. Gather external sources and draft the research narrative.
2. Query internal or structured data through a controlled database path.
3. Validate SQL before moving across warehouses or dialects.
4. Review citations, query assumptions, and data limitations before publishing.

## Setup Considerations

- Database credentials should be read-only for exploration.
- Research output should separate cited claims from agent interpretation.
- SQL examples should include dialect and table-grain assumptions.
- Source collection should record URLs and retrieval dates where possible.

## Security And Trust Considerations

- Do not expose sensitive database rows in public research drafts.
- Treat unsupported research claims as drafts, not facts.
- Keep source labels honest when a resource is community-maintained.
- Validate generated SQL before execution against production data.

## What To Evaluate Before Adopting

- Are citations specific enough to audit?
- Does the workflow distinguish public sources from internal data?
- Are SQL transformations deterministic and reviewed?
- Is there a final human review before external publication?

## Related Pages

- [Data Platform Workflow](../workflows/data-platform.md)
- [Content And Research Workflow](../workflows/content-and-research.md)
- [LangChain / LangGraph](../frameworks/langchain-langgraph.md)
- [Quality Checklist](../examples/quality-checklist.md)
