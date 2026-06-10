# SRE And Platform Teams

## Who This Is For

SRE, platform, infrastructure, and on-call teams evaluating skills for incident
triage, runtime operations, and agent-assisted remediation drafts.

## When Agent Skills Are Useful

- Collecting Kubernetes, cloud, and observability signals during incidents.
- Drafting next remediation steps from evidence.
- Validating alerting rules before they create production noise.
- Reusing runtime operations runbooks for agent platforms.

## When Not To Use Them Yet

- Agents need unrestricted production write access.
- Incident evidence cannot be logged or reviewed safely.
- The team lacks a human on-call owner for final action.

## First 30-Minute Evaluation

1. Review `investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`.
2. Compare it with `tail-multi-pod-kubernetes-logs-by-label-during-incidents-with-stern`.
3. Confirm the skill bounds namespace, service, and command scope.
4. Check whether output separates symptoms from confirmed causes.

## First Pilot Workflow

Use a staging incident or historical incident packet. Collect logs with Stern,
draft remediation with HolmesGPT or OpenSRE, then validate alert rules with
`lint-and-validate-prometheus-alerting-rules-before-noisy-or-broken-alerts-reach-production-with-pint`.

## Trust And Safety Checklist

- Production access is read-only during diagnosis.
- Remediation commands require human approval.
- Summaries redact secrets and customer data.
- Alert changes are reviewed separately from incident narration.

## Rollout Path

- Sandbox: replay historical incidents or staging alerts.
- Limited team: allow read-only triage during one service's on-call rotation.
- Production: require evidence logs, owner approval, and rollback notes.

## Metrics To Track

- Time to collect relevant signals.
- Correctly identified services or namespaces.
- Human-accepted remediation drafts.
- Alert-rule issues caught before deployment.

## Common Failure Modes

- Confusing correlation with root cause.
- Running broad commands across unintended namespaces.
- Letting incident urgency bypass approval boundaries.

## Related Links

- [SRE Incident Response](../case-studies/sre-incident-response.md)
- [SRE Incident Ops](../workflows/sre-incident-ops.md)
- [Runtime Ops: OpenClaw](../case-studies/runtime-ops-openclaw.md)
- [OpenClaw](../frameworks/openclaw.md)
