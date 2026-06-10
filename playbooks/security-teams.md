# Security Teams

## Who This Is For

Security engineers, AppSec teams, and platform owners reviewing agent workflows
that touch dependencies, approval gates, generated code, or prompt/tool risk.

## When Agent Skills Are Useful

- Adding human approval checkpoints for risky actions.
- Scanning dependency and supply-chain risk before release.
- Testing agent workflows for jailbreak, prompt-injection, and policy failures.
- Running generated code inside a constrained sandbox.

## When Not To Use Them Yet

- The workflow requires secrets in prompts or logs.
- No one owns final approval for risky actions.
- The team cannot reproduce scan findings or sandbox runs.

## First 30-Minute Evaluation

1. Review `route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`.
2. Compare it with `scan-project-dependencies-for-supply-chain-vulnerabilities-with-murphysec`.
3. Identify which actions must be blocked until a human approves.
4. Confirm output includes evidence, not only a pass/fail summary.

## First Pilot Workflow

Start with a non-production repo. Route high-risk actions through HumanLayer,
scan dependencies with MurphySec, and run generated code with
`run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox` before
allowing any merge recommendation.

## Trust And Safety Checklist

- Secrets are not sent to prompts, logs, or generated reports.
- Human approvals include identity, reason, and timestamp.
- Temporary link or scan failures are not collapsed into success.
- Sandbox limits cover files, network, and credentials.

## Rollout Path

- Sandbox: run against intentionally vulnerable fixtures.
- Limited team: pilot on internal tools or low-risk services.
- Production: require approval evidence, scan logs, and escalation paths.

## Metrics To Track

- Risky actions blocked before approval.
- Scan findings triaged correctly.
- False positives and false negatives from guardrail tests.
- Time to reproduce security evidence.

## Common Failure Modes

- Treating an approval tool as a replacement for code review.
- Allowing generated code to run with ambient credentials.
- Marking temporary scanner failures as clean results.

## Related Links

- [Security Approval Workflow](../case-studies/security-approval-workflow.md)
- [Security And Guardrails](../workflows/security-and-guardrails.md)
- [MCP](../frameworks/mcp.md)
- [Quality Checklist](../examples/quality-checklist.md)
