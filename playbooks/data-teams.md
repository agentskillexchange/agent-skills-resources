# Data Teams

## Who This Is For

Analytics engineers, data platform teams, data scientists, and research teams
evaluating skills for database inspection, SQL validation, and source-backed
analysis.

## When Agent Skills Are Useful

- Inspecting databases through controlled MCP paths.
- Validating SQL before moving across dialects or warehouses.
- Comparing dbt models and warehouse relations before migration.
- Drafting research with source links and internal-data caveats.

## When Not To Use Them Yet

- The agent requires write access to production data.
- Sensitive rows would be copied into public drafts or logs.
- The team cannot review generated SQL before execution.

## First 30-Minute Evaluation

1. Review `query-and-inspect-postgres-databases-through-mcp-with-pgedge-postgres-mcp`.
2. Compare it with `translate-and-validate-sql-across-dialects-with-sqlglot`.
3. Confirm credentials can be read-only.
4. Check whether the skill records database, dialect, and query assumptions.

## First Pilot Workflow

Use a sample schema or read-only staging database. Inspect tables through MCP,
validate a SQL transformation with SQLGlot, then compare migration parity with
`compare-dbt-models-and-warehouse-relations-before-trusting-migration-parity-with-dbt-audit-helper`.

## Trust And Safety Checklist

- Credentials are read-only and scoped.
- Query output is sampled or redacted when sensitive.
- SQL dialect and table grain are explicit.
- Claims in research drafts are tied to citations or query evidence.

## Rollout Path

- Sandbox: sample CSVs, fixtures, or non-sensitive schemas.
- Limited team: read-only access for one analytics workflow.
- Production: require query review, data-handling policy, and audit logs.

## Metrics To Track

- SQL validation failures caught before execution.
- Data-quality issues found before migration.
- Query evidence included in final reports.
- Sensitive-data handling exceptions.

## Common Failure Modes

- Running generated SQL directly on production data.
- Treating sampled rows as full-population evidence.
- Mixing public research claims with internal data without labeling.

## Related Links

- [Data Research Workflow](../case-studies/data-research-workflow.md)
- [Data Platform](../workflows/data-platform.md)
- [Content And Research](../workflows/content-and-research.md)
- [Generated skill mapping index](../generated/ase-skill-mapping-index.md)
