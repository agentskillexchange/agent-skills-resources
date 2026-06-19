# Agent Skill Ecosystem

This framework-neutral map shows where skills sit relative to models, runtimes,
tools, MCP, memory, evaluation, and operations.

```mermaid
flowchart TD
  Model["Model or provider"] --> Runtime["Agent runtime"]
  Runtime --> Skill["Skill layer"]
  Runtime --> Memory["Memory and context"]
  Runtime --> Approval["Human approval"]
  Skill --> Tools["Tools: CLI, API, browser, files"]
  Skill --> MCP["MCP servers"]
  Skill --> Workflow["Repeatable workflow"]
  MCP --> External["External systems"]
  Tools --> External
  Workflow --> Evaluation["Evaluation and verification"]
  Approval --> Evaluation
  Memory --> Workflow
  Evaluation --> Ops["Rollout, monitoring, maintenance"]
```

Skills are the policy and workflow layer. Tools and MCP provide capability;
skills explain when and how those capabilities should be used.
