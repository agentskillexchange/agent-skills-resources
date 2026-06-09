# Model Context Protocol

Model Context Protocol (MCP) standardizes how agents connect to tools and
context providers. Skills and MCP are complementary: MCP exposes capabilities;
skills explain how to use them in a repeatable workflow.

## Role In The Skills Ecosystem

- Tool and context connection protocol.
- Strong fit for database access, SaaS tools, browser tools, filesystems,
  memory providers, and custom APIs.
- Skills should name the MCP server, permissions, setup, and usage workflow.

## Source-Backed Resources

| Label | Resource | Why it matters |
|---|---|---|
| Official | [Model Context Protocol docs](https://modelcontextprotocol.io/) | Official MCP documentation site. |
| Official | [modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | Official MCP specification and docs repository. |
| Official | [Model Context Protocol GitHub org](https://github.com/modelcontextprotocol) | Official SDK and implementation organization. |
| ASE | [MCP skills catalog](https://agentskillexchange.com/browse-skills/?framework=MCP) | Live ASE view of MCP-related skills. |

## Skill Guidance

MCP skills should include:

- server install/setup
- permission boundaries
- client compatibility
- tool call examples
- verification and cleanup steps

