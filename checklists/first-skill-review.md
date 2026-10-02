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

## Choose The First Review Decision

Use the evidence block above to choose one next action before opening a deeper
worksheet:

| Evidence pattern | Decision | Next action |
|---|---|---|
| No repeated workflow, unreachable source, or missing safety boundary. | Reject | Record the blocker in `Next Action`; do not evaluate further. |
| Useful workflow, but setup, permissions, or verification evidence is incomplete. | Revisit with fixes | Ask for the missing proof before scoring the skill. |
| Clear workflow, reachable source, named permissions, and reviewable checks. | Move to deeper evaluation | Copy the evidence into the skill evaluation worksheet. |

## Revisit With Fixes Handoff

When the decision is `Revisit with fixes`, send the author back to
[Repair Before First Review](../examples/quality-checklist.md#repair-before-first-review)
with the weak evidence area named in `Next Action`.

Use this quick map so the author knows what to repair before returning:

| Missing review evidence | Repair path |
|---|---|
| Source URL, ownership, or reachability | Add source provenance and a reachable upstream link. |
| Setup proof | Add an install, account, auth, or hosted-runtime step a reviewer can try. |
| Permission or safety boundary | Name minimum access, write actions, production risk, and approval checkpoints. |
| Repeated workflow | Add the first object to inspect, bounded steps, expected output, and handoff. |
| Observable check | Add the pass signal, failure signal, open risk, and saved artifact or log. |

After the repair, rerun this first review and replace `Next Action` with the
new evidence outcome.

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
