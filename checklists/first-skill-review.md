# First Skill Review Checklist

Use this for a fast first pass before a deeper evaluation.

## Skill

- Skill name or slug:
- Source URL:
- Reviewer:
- Date:

## Checklist

- [ ] The skill maps to a repeated workflow.
- [ ] The source is clear and reachable.
- [ ] Setup steps are specific enough to try.
- [ ] Required permissions are named.
- [ ] Verification or expected output is described.
- [ ] Safety-sensitive actions are visible.
- [ ] The skill is not only a generic prompt or category label.

## Evidence

```text

```

## Evidence Example

Use a short block like this when the first pass has enough proof to move
forward:

```text
Source: official upstream repo and docs are reachable.
Setup: package install, required account, and auth command are named.
Permissions: default workflow is read-only; write actions require approval.
Workflow: agent inspects the target issue, gathers context, proposes a patch,
then runs the named verification command.
Observable check: `npm test` passes and the saved log includes the changed
module.
Open risk: production deployment is out of scope for this review.
```

## Decision

- [ ] Reject
- [ ] Revisit with fixes
- [ ] Move to deeper evaluation

## Deeper Evaluation Handoff

If this review moves forward, copy the evidence above into the
[Skill Evaluation Worksheet](../templates/skill-evaluation-worksheet.md) and
fill these fields first:

- Target workflow and expected output
- Required tools, accounts, permissions, and approval points
- Verification checks, pass signal, and artifacts to save
- Main risk, mitigation, and pilot decision reason

## Next Action

```text

```
