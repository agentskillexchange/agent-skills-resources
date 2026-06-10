# MCP Tooling User Starter Kit

## Who This Is For

Developers connecting agents to tools, APIs, databases, browser automation, or
context providers through MCP or MCP-like integrations.

## First 15 Minutes

1. Read [frameworks/mcp.md](../frameworks/mcp.md).
2. Skim [ecosystem-map.md](../ecosystem-map.md) to separate skills, tools, MCP,
   workflows, and guardrails.
3. Pick one read-only MCP workflow first.
4. Review server auth, tool allowlists, data access, and logs before connecting
   production systems.

## First Useful Workflow

Start with a read-only tool:

1. Install or configure the MCP server in a sandbox.
2. Confirm the agent can list tools and inspect context.
3. Run a bounded query or browser action.
4. Verify the result outside the agent.
5. Write down the permission and rollback boundaries before expanding access.

## Representative ASE Examples

- [`postgresql-mcp-server`](https://agentskillexchange.com/skills/postgresql-mcp-server/)
- [`playwright-mcp-browser-automation`](https://agentskillexchange.com/skills/playwright-mcp-browser-automation/)
- [`give-mcp-clients-language-server-code-intelligence`](https://agentskillexchange.com/skills/give-mcp-clients-language-server-code-intelligence/)
- [`use-mcp-context-forge-as-an-mcp-gateway-and-registry`](https://agentskillexchange.com/skills/use-mcp-context-forge-as-an-mcp-gateway-and-registry/)

## Safety Reminders

- Prefer read-only credentials for the first pilot.
- Review MCP server source and install path.
- Treat browser, shell, database, and cloud tools as high-risk until proven
  otherwise.
- Require explicit human approval for write actions.
