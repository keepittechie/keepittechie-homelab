# Glance Dashboard

## Purpose

Glance is the homelab dashboard: a quick place to see important links, service groups, status widgets, and daily operational shortcuts.

## Where It Fits

```text
Admin browser
  |
dashboard.home.example.com
  |
Dashboard app
  |
Links to services, docs, monitoring, and media tools
```

The dashboard is not the source of truth for infrastructure, but it is a useful daily entry point.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Container or app VM |
| Example DNS | `dashboard.home.example.com` |
| Public access | No |
| Similar current grouping source | Homepage/Glance-style dashboard config |
| Primary audience | Lab admin |

## Key Dependencies

- Pi-hole DNS records
- Reverse proxy route
- Service URLs
- Optional widgets or health checks
- Icons or small static assets

## Network / DNS

Dashboard links should use service aliases instead of raw IPs:

```text
grafana.home.example.com
pihole1.home.example.com
proxmox.home.example.com
wiki.home.example.com
plex.home.example.com
```

Internal admin links should not be exposed publicly just because they appear on a dashboard.

## Backup Notes

- Back up dashboard configuration.
- Keep widget credentials in private runtime files.
- Keep icons and non-secret assets versioned if useful.
- Sanitize any dashboard config before publishing examples.

## Security Notes

- Do not publish a dashboard full of private admin links.
- Keep widget credentials out of Git.
- Avoid screenshots showing real internal domains, personal bookmarks, or account data.
- Treat the dashboard as private operational visibility.

## What Viewers Can Learn

- How a dashboard improves homelab usability.
- How to group services by workflow.
- Why links, monitoring, and documentation belong near each other.
- How to share dashboard ideas without publishing private URLs.

## Future Improvements

- Add a sanitized dashboard group example.
- Add a dashboard-to-service inventory mapping.
- Decide whether the public docs should use "Glance" as the canonical dashboard name if the implementation changes.
