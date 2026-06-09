# LangChain And LangGraph

LangChain and LangGraph are framework-level tools for building agentic systems.
They are especially relevant when a skill describes orchestration, state,
retrieval, tools, evaluation, or human-in-the-loop control.

## Role In The Skills Ecosystem

- Agent orchestration and stateful workflow framework.
- Strong fit for graph-based agents, tool nodes, RAG, memory, evaluation, and
  long-running workflows.
- Skills should be explicit about state, tools, interrupts, and observability.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Public LangGraph repository. |
| Official | [LangChain agents page](https://www.langchain.com/agents) | LangChain's agent and LangGraph product context. |
| Official | [LangGraph agents reference](https://reference.langchain.com/python/langgraph/agents/) | API reference for agent workflow primitives. |
| ASE | [LangChain skills on ASE](https://agentskillexchange.com/browse-skills/?q=LangChain) | Live ASE search for LangChain-related skills. |

## Skill Guidance

LangGraph-oriented skills should include:

- state schema
- tool node behavior
- interrupt and approval points
- testable graph outputs
- traces or evaluation checks

## Skill Patterns That Fit LangChain And LangGraph

- graph-based orchestration
- tool and MCP adapters
- durable state machines
- human-in-the-loop approvals
- retrieval, memory, and evaluation loops

## Representative ASE Examples

- `assemble-production-agent-harnesses-with-deepagents`
- `langgraph-js-agent-orchestration-framework`
- `langchain-mcp-server`

## Common Mistakes

- Describing an agent graph without naming state or interrupts.
- Skipping evaluation and trace expectations.
- Hiding tool permissions behind generic "agent can call tools" language.
