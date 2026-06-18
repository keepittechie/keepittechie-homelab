# Contributing

This is a public documentation repo for the KeepItTechie homelab. Contributions are welcome when they make the material clearer, safer, or easier for viewers to learn from.

## Good Contributions

- Typo fixes
- Broken link fixes
- Diagram improvements
- Sanitized example improvements
- Beginner-friendly explanations
- Better structure in service docs
- Notes that make security boundaries clearer

## Do Not Submit

- Real credentials
- Private keys or certificates
- API keys or tunnel credentials
- Real public IP addresses
- Raw pfSense, switch, router, NAS, or app exports
- Private DNS zones
- Personal financial data
- Job application data or private messages
- Advice that exposes admin tools publicly without strong warnings

## Public-Safe Examples

Use examples like:

```text
home.example.com
10.10.0.0/24
pihole1.home.example.com
proxy.home.example.com
grafana.home.example.com
```

## Pull Request Checklist

- [ ] The change is documentation-first and viewer-friendly.
- [ ] Examples are sanitized.
- [ ] No real credentials or private exports are included.
- [ ] Links were checked where practical.
- [ ] Local docs checks were run when practical.
- [ ] The service matrix or roadmap was updated if the change affects them.
- [ ] Screenshots follow the screenshot policy or are not included.

Use the [pull request template](.github/pull_request_template.md) when opening changes. For safety-sensitive updates, review the [Pre-Publish Review Checklist](docs/pre-publish-review.md) and [Screenshot Policy](docs/screenshots-policy.md).

## Local Checks

Run the lightweight checks before opening a pull request when practical:

```bash
python3 scripts/check_markdown_links.py
python3 scripts/check_diagrams.py
python3 scripts/public_safety_scan.py
git diff --check
```

These checks are guardrails. They do not replace manual review for screenshots, examples, or security-sensitive docs.

## Issues

Use the issue templates for documentation improvements, safety reviews, and sanitized config example requests. Keep issue content public-safe and avoid posting private config, screenshots, or operational details.

## Tone

Keep the writing practical and approachable. This repo should feel like a useful KeepItTechie homelab guide: clear, grounded in real learning, and careful about private operational details.
