# Source Labeling

Every entry in `data/resources.json` must use one source label.

## Labels

| Label | Use for | Example |
|---|---|---|
| `Official` | Vendor or project-owned docs/repos | `github.com/openai/codex` |
| `Lab` | Frontier lab or research-lab material | OpenAI product/lab pages |
| `Community` | Third-party lists, guides, or repos | community awesome lists |
| `ASE` | Agent Skill Exchange site, repo, or verification material | `agentskillexchange/skills` |

## Rules

- Do not call a resource official unless ownership proves it.
- GitHub org ownership matters, but docs pages can move; verify before labeling.
- Community lists can be useful, but keep them separate from official sources.
- ASE links should point to the companion's source of truth: the site, the main
  skills repo, or verification material.
- Avoid popularity claims unless fetched live and clearly sourced.

## Common Cases

- Vendor documentation: `Official`
- Vendor GitHub repository: `Official`
- Model provider blog/product page: `Lab`
- Third-party "awesome" list: `Community`
- ASE catalog, verification, mappings, or marketplace links: `ASE`

