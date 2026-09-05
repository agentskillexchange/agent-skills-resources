# MCP Database Inspection Evaluation

This is an illustrative completed worksheet, not a certification claim.

## Skill

- Skill slug: `postgresql-mcp-server`
- Workflow: read-only database inspection through MCP
- Source of example: representative mapping in `data/ase-skill-mapping.json`
- Decision: pilot in staging with data-owner review

## Workflow Fit

The skill fits data, platform, and analytics teams that want agents to inspect
schemas, explain table relationships, and draft bounded SQL questions without
granting write access or live production privileges.

## Permissions Reviewed

- Repo access: not required for a read-only inspection pilot.
- Data access: staging or sample database only, with table allowlist and row
  limits.
- Network access: limited to the reviewed MCP server and approved database host.
- Production access: not approved for the first pilot.
- Human approval: required from a data owner before sharing query findings.

## Verification Evidence Example

```text
Pilot database: staging analytics replica
Allowed actions: schema inspection, EXPLAIN, SELECT queries with row limits
Expected evidence: MCP config, credential scope, query log, SQL validation,
sample result checks, data-owner decision
```

## Risk Review Summary

- Main risk: read credentials or MCP tools expose more tables than the workflow
  needs.
- Mitigation: start with a staging database, table allowlist, row limits, and
  saved query logs before any broader access.
- Open question: which tables should be excluded because sample rows may reveal
  sensitive customer, employee, or transaction data.

## Why A Team Might Pilot It

- The workflow is useful before write or migration work is considered.
- The permission boundary can be reviewed from config and query logs.
- A data owner can compare generated SQL against expected table semantics.

## Why A Team Might Reject It

- The MCP server configuration cannot prove read-only access.
- Query logs, row limits, or validation output are missing.
- The data owner cannot review the schema, sample output, or sharing decision.
