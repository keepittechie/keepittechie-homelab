# Glance / Homepage Dashboard

## Purpose

The dashboard is the homelab start page. It groups service links, status widgets, documentation shortcuts, and daily operational views into one place.

## Why This Matters

A dashboard makes the lab easier to use, but it can also reveal a lot about private infrastructure. The learning goal is to show how to organize services without publishing sensitive admin links or live internal details.

## Where It Fits in the Homelab

```text
Admin browser
  |
dashboard.home.example.com
  |
Dashboard app
  |
Links to services, docs, monitoring, and workflows
```

The dashboard is a navigation layer. It is not the source of truth for infrastructure.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `dashboard.home.example.com` |
| Public access | No |
| Primary audience | Homelab admin |
| Data type | Links, groups, widgets, health checks |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| Dashboard config | `/opt/apps/example/dashboard` | High | Remove private URLs before sharing |
| Icons/assets | `/mnt/storage/appdata/dashboard/assets` | Medium | Safe if they contain no private data |
| Widget settings | `/mnt/storage/appdata/dashboard/widgets` | High | May reference private services |
| Backups | `/mnt/storage/backups/dashboard` | Medium | Keep private configs private |

## Network / DNS

Example:

```text
dashboard.home.example.com -> proxy.home.example.com
```

Dashboard links should use service identities, not raw backend addresses. Public examples should use `home.example.com` names only.

## Key Responsibilities

- Group common service links.
- Surface health checks where useful.
- Link documentation and dashboards.
- Keep admin workflows easy to find.
- Avoid exposing sensitive services publicly.
- Provide a safe pattern readers can adapt.

## Example Public-Safe Configuration

Sanitized dashboard grouping:

| Group | Example Services | Purpose | Public Notes |
|---|---|---|---|
| Core Infrastructure | pfSense, Pi-hole, Proxmox, PBS | Admin entry points | Keep private |
| Monitoring | Grafana, Prometheus, Loki | Visibility and troubleshooting | Do not publish live dashboards |
| Media | Plex, Tautulli, Tdarr | Media workflows | Keep user data private |
| Documentation | Wiki.js, GitHub repo | Notes and public docs | Separate public/private links |
| Apps | FinanceHQ, CareerFill | Personal workflows | Private only |

## Backup and Restore Notes

- Back up dashboard configuration.
- Keep widget credentials and private URLs out of public examples.
- Store public-safe examples separately from live config.
- Test that important links still work after restore.
- Rebuild is usually easy if the service list is documented.

## Security Notes

- Do not publish a dashboard full of admin links.
- Do not include private URLs, credentials, or personal bookmarks in screenshots.
- Keep health check endpoints private if they reveal service status.
- Avoid public widgets that expose infrastructure state.
- Treat dashboard config as sensitive if it references private services.

## Common Mistakes to Avoid

- Treating the dashboard as harmless because it is "just links."
- Publishing screenshots without redaction.
- Mixing public bookmarks with private admin shortcuts.
- Storing widget credentials in public examples.
- Letting stale links hide real service changes.

## What Readers Can Learn

- How a dashboard improves daily homelab use.
- How to group services by workflow.
- Why dashboard config should be sanitized before publishing.
- How health checks and documentation links help operations.

## Related Sanitized Examples

- [Dashboard Docker Compose example](../../examples/docker-compose/dashboard-compose.yml)
- [Docker Compose example notes](../../examples/docker-compose/README.md)
- [Environment file placeholders](../../examples/env/README.md)

## Future Improvements

- Add a sanitized dashboard example file.
- Add a dashboard-to-service matrix.
- Add screenshot guidance for public docs.
