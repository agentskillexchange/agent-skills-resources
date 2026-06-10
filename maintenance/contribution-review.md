# Contribution Review

Use this guide when reviewing issues or pull requests for this companion repo.
The canonical skill catalog remains
[agentskillexchange/skills](https://github.com/agentskillexchange/skills).

## Review Source Labels

- `Official`: vendor or project-owned docs or repositories.
- `Lab`: research-lab or model-provider material where lab ownership is clear.
- `Community`: third-party guides, awesome lists, examples, and tools.
- `ASE`: Agent Skill Exchange site, repo, data, or documentation.

Ask for evidence when ownership is unclear. If ownership cannot be proven, use
`Community`.

## Review Completed Evaluation Examples

- Confirm the ASE skill slug exists publicly.
- Keep the example illustrative, not a certification claim.
- Require workflow fit, permissions reviewed, verification evidence, risk
  summary, and decision.
- Do not duplicate full `SKILL.md` bodies.

## Avoid Duplicate Catalog Behavior

Reject changes that copy large parts of the canonical skills catalog into this
repo. Link to the catalog instead, and keep examples representative.

## When To Reject

- Fake or unverifiable skills.
- Unsupported official/vendor claims.
- Full catalog dumps.
- Stale popularity claims.
- Resources with no clear workflow or framework relevance.
- Examples that imply safety certification without evidence.

## When To Redirect To `agentskillexchange/skills`

Ask contributors to submit to the canonical catalog when they are adding or
editing an actual skill, changing skill metadata, or proposing catalog-wide
skill generation.
