# Team Evaluation Starter Kit

## Who This Is For

Engineering, security, SRE, data, or content teams deciding whether agent skills
are safe and useful enough for a pilot.

## First 15 Minutes

1. Open the [Adoption Matrix](../adoption-matrix.md).
2. Pick one low- or medium-risk workflow.
3. Copy the [skill evaluation worksheet](../templates/skill-evaluation-worksheet.md).
4. Decide the sandbox boundary, owner, success criteria, and review date.

## First Useful Workflow

Run a pilot that produces evidence:

1. Choose one skill and one representative task.
2. Run in a sandbox, fixture repo, staging environment, or read-only context.
3. Capture input, commands, outputs, failed checks, and reviewer decisions.
4. Decide: reject, revisit, or limited pilot.

## After The First Workflow

Use the first decision to choose the next artifact:

- If the evidence is weak, keep the workflow in review and update the
  [skill evaluation worksheet](../templates/skill-evaluation-worksheet.md).
- If the evidence supports a limited pilot, complete the
  [team pilot readiness checklist](../checklists/team-pilot-readiness.md) and
  open the [pilot plan](../templates/pilot-plan.md) before adding users.
- If the pilot is already complete, move the owner, rollback, monitoring, and
  evidence notes into [rollout readiness](../templates/rollout-readiness.md).

## Representative ASE Examples

- [`route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer`](https://agentskillexchange.com/skills/route-risky-coding-agent-work-through-human-approval-checkpoints-with-humanlayer/)
- [`run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox`](https://agentskillexchange.com/skills/run-agent-generated-code-in-local-microvm-sandboxes-with-microsandbox/)
- [`investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt`](https://agentskillexchange.com/skills/investigate-production-incidents-across-kubernetes-and-cloud-signals-with-holmesgpt/)
- [`translate-and-validate-sql-across-dialects-with-sqlglot`](https://agentskillexchange.com/skills/translate-and-validate-sql-across-dialects-with-sqlglot/)

## Safety Reminders

- Start one risk level lower than your target production workflow.
- Require a named owner for each skill pilot.
- Record evidence, not only impressions.
- Do not move from sandbox to production without rollback and monitoring.
