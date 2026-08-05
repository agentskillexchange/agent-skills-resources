# Security, Policy, And Governance

Use this section when a skill-backed workflow touches sensitive data, tools,
repositories, users, deployments, or external systems.

| Topic | Use it for |
|---|---|
| [Agent Safety Review Guide](agent-safety-review-guide.md) | Review risk before piloting a skill-backed workflow |
| [Prompt Injection And Tool Abuse](prompt-injection-and-tool-abuse.md) | Identify prompt injection, tool misuse, and indirect instruction risk |
| [Data And Secrets Handling](data-and-secrets-handling.md) | Decide what data, secrets, logs, and artifacts may be exposed |
| [Policy And Governance](policy-and-governance.md) | Connect skill review to policy, ownership, and risk frameworks |
| [Runtime Guardrails](runtime-guardrails.md) | Add validation, filters, policy checks, and refusal paths |
| [Red Teaming And Evals](red-teaming-and-evals.md) | Test agent workflows before wider rollout |
| [Security Rollout Checklist](security-rollout-checklist.md) | Capture minimum go/no-go evidence |

## Start With A Reviewable Example

If the workflow needs human approval, privileged tool use, or denied-action
evidence, compare it with the
[HumanLayer Approval Workflow](../examples/completed-evaluations/humanlayer-approval-workflow-evaluation.md)
example before filling out the
[Security Rollout Checklist](security-rollout-checklist.md). Use the example
for evidence shape only; the decision still belongs to your own workflow,
owners, logs, and approvals.

Security review should stay evidence-based. Do not approve a skill only because
the framework is familiar or popular.
