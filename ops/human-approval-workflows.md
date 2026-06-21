# Human Approval Workflows

Human approval gates keep agent workflows from silently crossing risk
boundaries.

## When Approval Is Needed

Require approval before:

- writing to production systems
- sending external messages
- merging or deploying code
- changing security, billing, or access settings
- deleting data
- calling tools with broad permissions
- acting on uncertain or sensitive model output

## Approval Surfaces

Approvals can happen in:

- pull requests
- issue comments
- chat approvals
- dashboard review queues
- workflow automation steps
- incident review docs
- ticketing systems

## Evidence To Capture

| Field | Example |
|---|---|
| Request | What the agent wants to do |
| Risk | Why approval is needed |
| Approver | Who approved or rejected |
| Decision | approve, reject, revise |
| Artifact | trace, diff, report, screenshot, log |
| Follow-up | rollback, monitor, or expand |

## Related Ecosystems

- [HumanLayer](../ecosystems/humanlayer.md)
- [Composio](../ecosystems/composio.md)
- [n8n](../ecosystems/n8n.md)
- [Zapier](../ecosystems/zapier.md)
