# Rollout Evidence

Use this table before expanding a skill-backed workflow beyond a sandbox or
small pilot.

| Field | Evidence |
|---|---|
| Pilot owner |  |
| Skill or workflow |  |
| Systems touched |  |
| Trace/log link |  |
| Eval result |  |
| Approval evidence |  |
| Security review note |  |
| Rollback plan |  |
| Monitoring owner |  |
| Production readiness decision | reject / revisit / limited rollout / production |

## Minimum Review

- [ ] Trace or run log reviewed.
- [ ] Tool calls and permissions reviewed.
- [ ] Eval or expected-output check passed.
- [ ] Human approval evidence captured for risky actions.
- [ ] Rollback path tested or documented.
- [ ] Owner and review date assigned.

## Post-Go Audit Trail

After a `production` or `limited rollout` decision, keep the review record easy
to audit without reopening the full pilot packet:

| Keep current | Why it matters |
|---|---|
| Latest trace, eval, or expected-output check | Shows the workflow still behaves like the approved pilot |
| Permission, tool, or data-scope change | Makes the next review compare the expanded rollout to the approved boundary |
| Approval, incident, rollback, or mitigation note | Preserves why access widened, paused, or changed |
| Next owner and review date | Gives the visitor a concrete operating loop after the first `Go` |

## Decision Notes

```text

```
