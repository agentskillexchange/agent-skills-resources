# Agent Ops

Agent skills need more than good instructions. Teams also need operational
evidence: traces, logs, evals, approvals, rollback plans, ownership, and
monitoring.

| Topic | Use it for |
|---|---|
| [Agent Ops Overview](agent-ops-overview.md) | Understand the operating layer around skill-backed workflows |
| [Observability And Evals](observability-and-evals.md) | Decide what traces, logs, evals, and regressions to keep |
| [Human Approval Workflows](human-approval-workflows.md) | Add review gates before risky actions |
| [Workflow Automation](workflow-automation.md) | Compare connector automation with agent orchestration |
| [Model Gateways And Policy](model-gateways-and-policy.md) | Review model routing, provider failover, cost, and policy controls |
| [Rollout Evidence](rollout-evidence.md) | Capture the minimum evidence before production expansion |

Use these pages with the [checklists](../checklists/) and
[templates](../templates/) when a workflow moves from learning to team use.

## Choose The First Ops Artifact

| Stage | Open first | Capture before moving on |
|---|---|---|
| Designing a pilot | [Agent Ops Overview](agent-ops-overview.md) | Owner, workflow boundary, evidence sources, and operating risks |
| Preparing review gates | [Human Approval Workflows](human-approval-workflows.md) | Actions that need approval, reviewer role, and escalation path |
| Checking behavior | [Observability And Evals](observability-and-evals.md) | Trace/log location, expected-output check, and regression signal |
| Expanding after a `Go` decision | [Rollout Evidence](rollout-evidence.md) | Monitoring owner, review cadence, rollback trigger, and next review date |
