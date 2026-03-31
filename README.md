# Gemini

A small Python CLI scaffold for interpreting slash-style commands.

## Available commands

- `/init` : initialize project state (stub implementation)
- `/gemini` : show basic status
- `/gemini summary` : print repository summary
- `/gemini help` : print help text

## Run

```bash
python gemini.py /gemini help
```

## GitHub Action

You can reuse this repository's Gemini CLI as a GitHub Action.

Example usage from another repository:

```yaml
uses: m2106337/Gemini/.github/actions/gemini@main
with:
	command: '/gemini summary'
```

Or reference the action from within this repo:

```yaml
uses: ./.github/actions/gemini
with:
	command: '/gemini help'
```

## Publishing to GitHub Marketplace

This repository includes a top-level `action.yml` and `LICENSE` to support publishing the action to the GitHub Marketplace.

Quick publish steps:

1. Create a release tag (e.g. `v1.0.0`) and push it.
2. Create a GitHub Release from that tag.
3. Use the Marketplace publish flow in the repository settings to list the action.

See [RELEASE.md](RELEASE.md) for detailed steps.
