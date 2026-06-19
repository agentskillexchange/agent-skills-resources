# Install And Setup Clarity

Setup instructions should help a user reach the first safe validation quickly.
They should not merely explain how to copy a markdown file.

## A Useful Setup Section

| Part | What to include |
|---|---|
| Prerequisites | Runtime, account, token, local dependency, OS caveat |
| Install path | One primary install command or documented setup path |
| Configuration | Required env vars, files, permissions, and scopes |
| First safe test | A read-only or local validation command |
| Failure signs | Common setup errors and what they usually mean |

## Good / Weak

| Weak | Better |
|---|---|
| "Clone the repo and run it." | "Install the CLI, authenticate, then run a read-only status command." |
| "Set your API key." | "Set a token with read-only repo scope for the pilot." |
| "Run the workflow." | "Run against a sandbox project before touching production." |

## First Safe Command

Prefer commands that inspect state instead of changing it:

- `--version`
- `status`
- `list`
- `dry-run`
- read-only API query
- test connection command

If the first command writes, deletes, deploys, or contacts users, add an
approval gate before it.
