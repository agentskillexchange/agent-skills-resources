# SRE Incident Response

## Practical Scenario

An operations team wants agents to help during incidents without giving them
unbounded production authority. The goal is faster triage, clearer remediation
drafts, and better pre-production alert checks.

## Relevant ASE Skill Examples

| Skill | Role in the workflow |
|---|---|
| `investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt` | Correlates Kubernetes and cloud signals during incident triage |
| `investigate-production-incidents-across-observability-signals-and-draft-next-remediation-steps-with-opensre` | Turns observability evidence into proposed remediation steps |
| `tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern` | Focuses log collection across related pods |
| `lint-and-validate-prometheus-alerting-rules-before-noisy-or-broken-alerts-reach-production-with-pint` | Checks alert rules before they create production noise |

## How They Fit Together

1. Use log and signal-gathering skills to collect evidence.
2. Use incident-analysis skills to draft likely causes and next steps.
3. Keep remediation proposals human-reviewed before production action.
4. Feed lessons back into alert validation and runbook updates.

## Setup Considerations

- Kubernetes access should use least-privilege contexts.
- Cloud and observability access should be read-only for triage unless a
  specific remediation action is approved.
- Incident output should include timestamps, namespaces, services, and commands
  used.

## Security And Trust Considerations

- Avoid giving agents direct production write permissions during diagnosis.
- Treat remediation steps as drafts until reviewed by the on-call owner.
- Redact customer data and secrets from logs before sharing summaries.
- Keep alert-rule changes separate from incident narration.

## What To Evaluate Before Adopting

- Does the workflow cite the signals it used?
- Are commands bounded to the intended namespace or service?
- Can the agent distinguish symptoms from confirmed root cause?
- Is there a clean handoff from triage to human-approved action?

## Related Pages

- [SRE Incident Ops Workflow](../workflows/sre-incident-ops.md)
- [OpenClaw](../frameworks/openclaw.md)
- [MCP](../frameworks/mcp.md)
- [Freshness Audit](../maintenance/freshness-audit.md)
