# Security Approval Workflow

## Practical Scenario

A team wants coding agents to keep moving on routine work while routing risky
actions through approval gates and checking dependency, sandbox, and prompt-flow
risk before changes reach production.

## Relevant ASE Skill Examples

| Skill | Role in the workflow |
|---|---|
| `route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer` | Adds human approval checkpoints for higher-risk agent actions |
| `scan-project-dependencies-for-supply-chain-vulnerabilities-with-murphysec` | Checks dependency and supply-chain risk before release |
| `red-team-agent-workflows-for-jailbreaks-prompt-injection-and-policy-failures-with-deepteam` | Exercises agent workflows against policy and prompt-injection failures |
| `run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox` | Provides a safer execution boundary for generated code |

## How They Fit Together

1. Define which agent actions require approval.
2. Run dependency and security scans before promoting code.
3. Red-team the prompt/tool workflow where user input, tools, or policies are
   involved.
4. Execute generated or untrusted code in a sandboxed environment where
   possible.

## Setup Considerations

- Approval tools need clear identity, channel, and escalation rules.
- Dependency scanners need access to lockfiles and manifests.
- Sandbox workflows need limits on file, network, and credential access.
- Red-team checks should use representative prompts, not only happy-path tests.

## Security And Trust Considerations

- Never treat an approval gate as a substitute for code review.
- Keep secrets out of prompts, logs, generated reports, and test fixtures.
- Separate temporary link failures from hard security findings.
- Record evidence for approvals, scans, and sandbox runs.

## What To Evaluate Before Adopting

- Which actions are blocked until human approval?
- Are scan results actionable and reproducible?
- Does the sandbox match the runtime risk?
- Can the workflow distinguish temporary failures from real blockers?

## Related Pages

- [Security And Guardrails Workflow](../workflows/security-and-guardrails.md)
- [MCP](../frameworks/mcp.md)
- [Best Practices](../best-practices.md)
- [Source Labeling](../maintenance/source-labeling.md)
