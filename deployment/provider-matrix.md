# Provider Matrix

This matrix is a practical orientation guide for hosted agent and skill-backed
workflows. It is not a vendor ranking.

| Provider / surface | Best fit | Skill-adjacent role | Watch for |
|---|---|---|---|
| [Vercel Platform](../ecosystems/vercel-platform.md) | AI web apps, APIs, serverless functions | hosted app surface for tool-calling workflows | request duration, env scope, web security |
| [Cloudflare Workers](../ecosystems/cloudflare-workers.md) | edge workers and lightweight APIs | low-latency runtime for stateless workflows | runtime limits and dependency constraints |
| [Fly.io](../ecosystems/fly-io.md) | containers and global app services | container hosting for custom agent services | image patching and regional state |
| [Modal](../ecosystems/modal.md) | Python jobs, serverless compute, GPU tasks | hosted functions for data/model workflows | dependency pinning and job boundaries |
| [AWS Bedrock Agents](../ecosystems/aws-bedrock-agents.md) | AWS-native managed agents | managed agents, action groups, knowledge bases | IAM scope and enterprise policy |
| [Azure AI Foundry](../ecosystems/azure-ai-foundry.md) | Microsoft/Azure AI app lifecycle | agents, evaluation, deployment, governance | tenant policy and data handling |
| [Google Vertex AI Agent Builder](../ecosystems/google-vertex-ai-agent-builder.md) | Google Cloud agent apps and enterprise search | managed agent building and deployment | project/IAM setup and audit evidence |

## How To Use This Matrix

1. Pick the workflow shape first.
2. Pick the runtime that matches that shape.
3. Review secrets, approvals, and observability.
4. Run a bounded pilot before production use.
