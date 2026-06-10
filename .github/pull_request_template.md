# Summary

Describe the companion-resource change and why it belongs here.

## Type of change

- [ ] Source-backed resource addition
- [ ] Source label correction
- [ ] Framework/resource page improvement
- [ ] Completed evaluation example
- [ ] Typo or link correction
- [ ] Other documentation improvement

## Checklist

- [ ] I did not modify `agentskillexchange/skills`.
- [ ] I did not duplicate the full skills catalog.
- [ ] Source labels are evidence-backed.
- [ ] Third-party resources are marked `Community` unless ownership proves otherwise.
- [ ] I did not invent official claims, compatibility claims, or stale popularity claims.
- [ ] Generated indexes were updated if needed.
- [ ] Validation commands were run.

## Validation

```bash
python3 scripts/generate-resource-index.py
python3 scripts/generate-skill-mapping-index.py
python3 scripts/generate-template-index.py
python3 scripts/generate-nav-index.py
python3 scripts/generate-repo-stats.py
python3 scripts/validate-resources.py
python3 scripts/validate-links.py --timeout 15
python3 scripts/audit-freshness.py --timeout 15
```
