# Media Stack

## Purpose

The media stack handles streaming, library management, request workflows, monitoring, and media processing. It is a real-world example of multiple self-hosted services working together.

## Where It Fits

```text
Media storage
  |
Plex, Servarr apps, Tautulli, Tdarr
  |
Users and admin dashboards
```

The stack is split by role so streaming, automation, analytics, and transcoding are easier to reason about.

## Host / Runtime

| Component | Example Runtime | Example DNS |
|---|---|---|
| Plex | Media VM, example `apollo` | `plex.home.example.com` |
| Radarr / Sonarr / Prowlarr | Media automation VM, example `dionysus` | `radarr.home.example.com` |
| Transmission | Media automation VM | `transmission.home.example.com` |
| Jellyseerr | Request workflow | `requests.home.example.com` |
| Tautulli | Plex analytics | `tautulli.home.example.com` |
| Tdarr | GPU or worker-capable VM, example `hephaestus` | `tdarr.home.example.com` |

## Key Dependencies

- NAS or storage server paths
- Reverse proxy for internal URLs
- DNS records
- Media app databases and config directories
- GPU support where transcoding or processing needs it

## Network / DNS

Most automation dashboards should stay private. Plex may have limited external access depending on the desired user model, but the admin and automation interfaces should not be broadly exposed.

Example internal aliases:

```text
plex.home.example.com
radarr.home.example.com
sonarr.home.example.com
prowlarr.home.example.com
transmission.home.example.com
requests.home.example.com
tautulli.home.example.com
tdarr.home.example.com
```

## Backup Notes

- Back up application configuration and databases.
- Keep media files separate from app config backups.
- Back up Plex metadata if watch history and library state matter.
- Document storage mount assumptions for restore.

## Security Notes

- Do not expose automation dashboards publicly.
- Keep download clients private.
- Use strong authentication for any media service with remote access.
- Do not publish real library paths, usernames, or API credentials.

## What Viewers Can Learn

- How a multi-service app stack is organized.
- Why storage paths and permissions matter.
- Why each app has a distinct role.
- How to document app dependencies before something breaks.

## Future Improvements

- Add a sanitized media data-flow diagram.
- Add restore notes for Plex metadata.
- Add a table separating app config from media files.
