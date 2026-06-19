# Educational Content Guide

Use this guide when adding learning pages, cookbook entries, diagrams, or
resource notes.

## Add A Resource

1. Prefer official documentation or a maintained source.
2. Add the resource to `data/resources.json`.
3. Use a stable `id`.
4. Label the source accurately.
5. Explain why the resource matters for learning or adoption.
6. Run validation and link checks.

## Source Labels

| Label | Use when |
|---|---|
| Official | The resource is owned by the project or vendor |
| Lab | The resource is from a model provider or research lab |
| Community | The resource is useful but third-party |
| ASE | The resource is from Agent Skill Exchange |

Do not call a resource official because it is popular. Ownership matters.

## Write Framework-Neutral Guidance

Good educational guidance explains the concept first, then names examples. Keep
the main advice useful for Codex, Claude Code, GitHub Copilot, OpenClaw, Cursor,
Gemini CLI, LangGraph, MCP hosts, and custom runtimes.

## Avoid Vendor Claims

If a page says a product supports a feature, link to an official source. If the
source is community-maintained, say so.

## Keep Examples Source-Backed

Examples should teach patterns. Avoid turning learning pages into catalog
listings. Link to the canonical catalog only when a reader needs real skill
files to inspect.

## Avoid Duplicating The Skills Catalog

This repo is an educational hub. It should not contain generated latest-skill
lists, category dumps, or broad catalog mirrors. Keep representative examples
small, stable, and explanatory.

## Review Before Commit

- Does the page teach a concept?
- Are claims sourced or removed?
- Are framework names accurate?
- Are safety and approval points visible?
- Did generated indexes update?
- Did validation pass?
