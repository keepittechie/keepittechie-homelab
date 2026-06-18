# Screenshot Policy

Screenshots can make the repo easier to understand, but they also carry a high risk of leaking private infrastructure details. Do not add real screenshots until they have been reviewed carefully.

This page focuses on screenshot safety rules. For broader planning, file organization, and future visual ideas, see the [Visual Assets Guide](visual-assets-guide.md).

## Screenshot Safety Checklist

- [ ] Hide browser bookmarks.
- [ ] Hide logged-in usernames.
- [ ] Hide emails.
- [ ] Hide public IP addresses.
- [ ] Hide exact private host IP addresses.
- [ ] Hide live internal domains.
- [ ] Hide API keys or service credentials.
- [ ] Hide tunnel identifiers.
- [ ] Hide financial or job-related data.
- [ ] Hide database names if they reveal private context.
- [ ] Blur or crop sensitive panels.
- [ ] Prefer sanitized demo dashboards when possible.

## Safer Screenshot Types

| Screenshot Type | Why It Is Safer |
|---|---|
| Sanitized diagrams | Explain architecture without exposing live systems |
| Demo dashboards | Show layout using fake data |
| Fake-data app views | Teach the workflow without exposing personal records |
| Cropped UI panels | Focus on one setting or concept |
| Local lab examples without sensitive values | Useful when all visible data is reviewed |

## Unsafe Screenshot Types

| Screenshot Type | Risk |
|---|---|
| Router or firewall pages with live rules | Can expose network policy and private paths |
| DNS pages with real hostnames | Can reveal the live naming scheme |
| Cloudflare tunnel pages | Can reveal public routes, account details, or tunnel identifiers |
| Grafana dashboards with internal URLs | Can expose service names and topology |
| Nextcloud pages with user files | Can expose personal files or account names |
| FinanceHQ or CareerFill real data | Can expose private financial or career records |

## Public Repo Rule

If a screenshot is needed, create a sanitized demo view, crop aggressively, and review it with the [Pre-Publish Review Checklist](pre-publish-review.md) before merging.

Related docs:

- [Visual Assets Guide](visual-assets-guide.md)
- [Assets Index](../assets/README.md)
