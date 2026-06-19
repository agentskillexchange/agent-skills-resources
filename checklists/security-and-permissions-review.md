# Security And Permissions Review Checklist

Use this before approving a skill, tool, or workflow with sensitive access.

## Review

- Skill/tool/workflow:
- Systems touched:
- Reviewer:
- Date:

## Checklist

- [ ] Secrets handling is documented.
- [ ] Repository access is scoped.
- [ ] Data access is scoped.
- [ ] Network access is expected and explainable.
- [ ] Command execution is bounded.
- [ ] Production writes require human approval.
- [ ] Generated code or artifacts are reviewed before use.
- [ ] Logs do not expose secrets or private data.
- [ ] Dependency or supply-chain risk is understood.

## Evidence

```text

```

## Decision

- [ ] Block
- [ ] Revisit with mitigations
- [ ] Approve for sandbox
- [ ] Approve for limited rollout

## Next Action

```text

```
