# Local Quality Scripts

These scripts provide lightweight checks for the public KeepItTechie homelab repo. They are useful guardrails, not a replacement for manual review.

## Scripts

| Script | Purpose |
|---|---|
| `check_markdown_links.py` | Checks relative Markdown links and reports missing local files |
| `check_diagrams.py` | Confirms diagram pages have Mermaid fences and expected public-safe sections |
| `public_safety_scan.py` | Scans for obvious secrets, private domains, exact private host IPs, personal paths, and private-facing wording |

## Run Locally

```bash
python3 scripts/check_markdown_links.py
python3 scripts/check_diagrams.py
python3 scripts/public_safety_scan.py
git diff --check
```

## Limits

- The link checker verifies that local linked files exist, but it does not validate heading anchors.
- The diagram checker skips `diagrams/README.md` because it is an index, not a diagram page.
- The public-safety scan is conservative and pattern-based. It can catch obvious mistakes, but it cannot prove that a repo is safe.
- Manual review is still required before publishing screenshots, config snippets, or new sanitized examples.
