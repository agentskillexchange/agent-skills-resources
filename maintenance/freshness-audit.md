# Freshness Audit

Run the freshness audit whenever resources are added, and at least monthly for
routine maintenance.

```bash
python3 scripts/audit-freshness.py --timeout 15
```

## What It Checks

- required fields in `data/resources.json`
- duplicate resource URLs
- source labels
- HTTP status for resource URLs
- optional `last_checked_at` freshness
- mapped ASE skill slugs against the public skills catalog

## Interpreting Results

- `ok: true` means the resource hub is structurally healthy.
- HTTP `403` or `429` should be reviewed manually before removal; many docs
  sites block scripted checks or rate-limit temporarily.
- Missing fields or duplicate URLs should be fixed directly.
- Unknown ASE slugs should be removed or corrected.
- Stale `last_checked_at` entries should be rechecked and updated if the field
  is used.

## Remove Vs Relabel

Remove a resource when:

- the URL is gone and no replacement exists
- the resource is no longer about agent skills, tools, frameworks, or workflows
- the source cannot be verified

Relabel a resource when:

- an "Official" entry is actually third-party
- a lab page moves into product docs
- a community repo becomes project-owned or vice versa

