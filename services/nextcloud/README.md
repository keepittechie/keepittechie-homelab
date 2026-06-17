# Nextcloud

## Purpose

Nextcloud provides self-hosted file sync and private cloud workflows. It is a user-facing app that depends on storage, a database, app data, DNS, and reverse proxy routing.

## Why This Matters

Nextcloud is a useful teaching service because it looks simple from the browser but has serious operational requirements behind it. Files, app data, databases, user accounts, background jobs, reverse proxy settings, and backups all need to work together.

## Where It Fits in the Homelab

```text
Client devices
  |
nextcloud.home.example.com
  |
Reverse proxy
  |
Nextcloud app, database, and storage
```

Nextcloud can be limited-public if intentionally hardened, but admin access and private data should stay protected.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `nextcloud.home.example.com` |
| Public access | Limited and reviewed |
| Primary data | User files, app data, database, config |
| Admin access | Private or strongly authenticated |

## Storage / Data Layout

Example data responsibility table:

| Data Type | Example Path | Backup Priority | Notes |
|---|---|---|---|
| User files | `/mnt/storage/appdata/nextcloud/data` | Critical | Do not publish real file names |
| Database | `/mnt/storage/appdata/nextcloud/db` | Critical | Needs app-aware backup |
| App config | `/opt/apps/example/nextcloud` | High | Keep private values out of Git |
| Backups | `/mnt/storage/backups/nextcloud` | Critical | Store privately |
| Logs | `/mnt/storage/appdata/nextcloud/logs` | Medium | Logs may contain sensitive context |

## Network / DNS

Example:

```text
nextcloud.home.example.com -> proxy.home.example.com
```

The reverse proxy and trusted hostname configuration matter. Incorrect proxy settings can make a working app look broken or unsafe.

## Key Responsibilities

- Provide self-hosted file sync.
- Store and protect user data.
- Maintain database and app data consistency.
- Integrate with reverse proxy and TLS configuration.
- Support safe backup and restore workflows.
- Keep admin access private.

## Example Public-Safe Configuration

Example operational checklist:

| Area | Public-Safe Note | Private Detail |
|---|---|---|
| DNS | Use `nextcloud.home.example.com` examples | Live domains and routes |
| Storage | Use generic paths | Real user file paths |
| Database | Document backup need | Real database dumps |
| Reverse proxy | Explain trusted proxy concept | Live config values |
| Users | Use fake demo users | Real user list |

## Backup and Restore Notes

- Back up the database and user data together.
- Back up configuration privately.
- Document whether external storage is included.
- Test restores before relying on the service for critical files.
- Record restore evidence with sanitized notes.

## Security Notes

- Use strong authentication.
- Keep admin access private.
- Do not publish user lists, sync logs, file names, or shares.
- Keep trusted proxy and hostname settings in private docs if they reveal live routes.
- Review public screenshots carefully.

## Common Mistakes to Avoid

- Backing up files without the database.
- Assuming reverse proxy config is only cosmetic.
- Publishing screenshots with real file names.
- Exposing the admin interface without strong controls.
- Forgetting background jobs and maintenance settings.

## What Viewers Can Learn

- Why user-facing cloud apps need careful backups.
- How file data, app data, and databases differ.
- Why reverse proxy settings matter.
- How to document a private cloud without leaking private files.

## Future Improvements

- Add a public-safe restore checklist.
- Add a sanitized reverse proxy troubleshooting section.
- Add fake demo data for screenshots.
