# Nextcloud

## Purpose

Nextcloud provides self-hosted file sync, personal cloud workflows, and a practical example of running a user-facing app behind a reverse proxy.

## Where It Fits

```text
Client devices
  |
nextcloud.home.example.com
  |
Reverse proxy
  |
Nextcloud app, database, and storage
```

Nextcloud is more sensitive than a simple demo app because it can contain personal files, calendar data, contacts, and private documents.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | VM or app host |
| Example host | `atlas` or app VM |
| Example DNS | `nextcloud.home.example.com` |
| Public access | Limited and hardened if enabled |
| Storage | App data path plus optional NAS-backed storage |

## Key Dependencies

- Reverse proxy
- TLS configuration
- Database
- App data storage
- Background job configuration
- Backup and restore process

## Network / DNS

Example:

```text
nextcloud.home.example.com -> proxy.home.example.com
```

If a public hostname is used, keep it separate from the private examples in this repo and document the security decision in a private runbook.

## Backup Notes

- Back up the database and app data together.
- Back up configuration files privately.
- Test restores before relying on the service for critical files.
- Document whether external storage mounts are included in backups.

## Security Notes

- Use strong authentication.
- Keep trusted proxy and hostname settings accurate.
- Do not publish real user lists, file paths, sync logs, or shares.
- Keep admin recovery steps in private docs if they expose account details.

## What Viewers Can Learn

- What makes a self-hosted cloud app different from a static service.
- Why reverse proxy and trusted hostname configuration matters.
- Why app-aware backups matter for file sync tools.
- How to decide whether a service should be public or private.

## Future Improvements

- Add a sanitized install model.
- Add a backup and restore checklist.
- Add a public-safe troubleshooting section for proxy issues.
