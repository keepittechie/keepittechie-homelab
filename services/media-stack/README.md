# Media Stack

## Purpose

The media stack handles media streaming, library management, request workflows, analytics, and media processing. It is a practical example of several self-hosted services working together around shared storage.

## Why This Matters

Media stacks are popular homelab projects because they combine storage, networking, permissions, automation, metadata, and user-facing apps. They also teach a key lesson: the media files, app databases, and automation dashboards all have different security and backup needs.

## Where It Fits in the Homelab

```text
Media storage
  |
Plex, Servarr-style apps, Tautulli, Tdarr
  |
media.home.example.com and private admin dashboards
```

Plex may be limited-public depending on the design, but automation dashboards and download clients should stay private.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Media VM, app VM, or containers |
| Example DNS | `media.home.example.com` |
| Storage dependency | NAS or ZFS-backed media paths |
| Public access | Limited for user-facing media only |
| Admin access | Private LAN or VPN |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| Media files | `/mnt/storage/media` | Medium | Large files may use a separate backup strategy |
| App config | `/mnt/storage/appdata/media` | High | Small but important |
| Metadata | `/mnt/storage/appdata/plex` | High | Rebuilding metadata can take time |
| Transcode/cache | `/mnt/storage/appdata/transcode` | Low | Often disposable |
| Backup exports | `/mnt/storage/backups/media` | High | Keep private |

## Network / DNS

Example internal aliases:

```text
media.home.example.com
plex.home.example.com
tautulli.home.example.com
tdarr.home.example.com
```

Automation dashboards should remain private even if the user-facing media app has limited public access.

## Key Responsibilities

- Stream media through Plex or a similar front end.
- Organize media through Servarr-style automation.
- Track usage and health with Tautulli.
- Process or transcode media with Tdarr.
- Depend on well-documented storage paths.
- Keep automation and admin dashboards private.

## Example Public-Safe Configuration

Sanitized service map:

| Service | Purpose | Access Level | Data Dependency | Public Notes |
|---|---|---|---|---|
| Plex | Media streaming | Limited Public | `/mnt/storage/media` and app metadata | Keep users and libraries private |
| Servarr-style apps | Library automation | Private LAN | Media paths and app config | Do not expose dashboards |
| Tautulli | Media analytics | Private LAN | Plex history and metadata | Screenshots can reveal users |
| Tdarr | Media processing | Private LAN | Media files and transcode cache | GPU acceleration can be generic |
| Download client | Retrieval workflow | Private LAN | Temporary and completed media paths | Keep private |

## Backup and Restore Notes

- Back up app configuration and databases.
- Back up Plex metadata if history and library state matter.
- Keep media files separate from app config backups.
- Document storage mount assumptions.
- Test restoring a single app config before relying on the full stack.

## Security Notes

- Do not expose automation dashboards publicly.
- Keep download clients private.
- Do not publish real media library paths, user names, or watch history.
- Use strong authentication for any limited-public media access.
- Keep storage permissions narrow and understandable.

## Common Mistakes to Avoid

- Mixing media files and app config without a clear backup plan.
- Giving every container broad access to all storage.
- Publishing dashboards that reveal users or library contents.
- Ignoring storage path consistency across apps.
- Treating GPU acceleration as required before the basic stack is stable.

## What Viewers Can Learn

- How multi-app stacks depend on storage design.
- Why each media service has a distinct role.
- How app data and media files need different backup strategies.
- Why private dashboards should stay private.
- How to explain GPU acceleration without exposing hardware details.

## Future Improvements

- Add a sanitized media data-flow diagram.
- Add restore notes for Plex metadata.
- Add a public-safe storage permission example.
