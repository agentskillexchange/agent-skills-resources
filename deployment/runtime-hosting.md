# Runtime Hosting

Runtime hosting is about matching the workflow shape to the execution surface.
Most skill-backed workflows do not need the same runtime.

## Common Hosting Shapes

| Shape | Good fit | Watch for |
|---|---|---|
| Web app or API | User-facing AI features, chat, tool calls | request timeouts, auth, user data boundaries |
| Background worker | scheduled enrichment, queue processing | retries, idempotency, duplicate writes |
| Edge worker | low-latency routing, lightweight transformations | runtime limits, dependency limits |
| Container service | custom tooling, CLIs, long-running processes | image provenance, patching, resource limits |
| Sandbox | untrusted code, generated commands, risky tools | network egress, filesystem isolation, cleanup |
| Managed agent platform | enterprise agents and connectors | vendor lock-in, audit exports, policy controls |

## Provider Surfaces Covered

- [Vercel Platform](../ecosystems/vercel-platform.md)
- [Cloudflare Workers](../ecosystems/cloudflare-workers.md)
- [Fly.io](../ecosystems/fly-io.md)
- [Modal](../ecosystems/modal.md)
- [AWS Bedrock Agents](../ecosystems/aws-bedrock-agents.md)
- [Azure AI Foundry](../ecosystems/azure-ai-foundry.md)
- [Google Vertex AI Agent Builder](../ecosystems/google-vertex-ai-agent-builder.md)

## Selection Questions

- Does the workflow need user interaction or a scheduled/background loop?
- Does it call external tools with write permissions?
- Does it need long-running execution or short stateless requests?
- Are inputs trusted, partially trusted, or untrusted?
- Does the provider expose logs, traces, approvals, and audit records?

## When Not To Deploy Yet

- install/setup is unclear
- permissions are broader than the pilot needs
- the workflow cannot be replayed in a sandbox
- there is no owner or rollback path
- failures would affect customers, production data, or external messages
