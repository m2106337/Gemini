# Release & Marketplace Publishing

Steps to publish the `Gemini` GitHub Action to the Marketplace:

1. Ensure the repository is public and contains a top-level `action.yml` (this repo includes one).
2. Create a lightweight tag for the release, e.g. `v1.0.0`:

```bash
git tag -a v1.0.0 -m "Release Gemini CLI Action v1.0.0"
git push origin v1.0.0
```

3. Create a GitHub Release from the tag (via the web UI or `gh`):

```bash
gh release create v1.0.0 --title "v1.0.0" --notes "Initial Gemini CLI Action release"
```

4. Open the repository on GitHub, go to the Actions tab and verify the action metadata renders.
5. Use the Marketplace publish flow in the repository settings / Actions to list the action. Follow the UI prompts to add marketplace metadata and publish.

Notes:
- The action is implemented as a composite action and requires Python on the runner.
- A `LICENSE` file is required for Marketplace; this repo includes an MIT license.
