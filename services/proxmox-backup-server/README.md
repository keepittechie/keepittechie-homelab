# Proxmox Backup Server

## Purpose

Proxmox Backup Server stores deduplicated backups for Proxmox VMs and containers. It is the main VM recovery layer for the lab.

## Where It Fits

```text
Proxmox guests
  |
scheduled backups
  |
Proxmox Backup Server
  |
restore test or production recovery
```

PBS is not just storage. It provides backup catalogs, retention, verification, pruning, and a restore workflow that fits Proxmox.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `chronos` |
| Runtime | Dedicated PBS install or VM |
| Example DNS | `pbs.home.example.com` |
| Public access | No |
| Primary clients | Proxmox hosts |

## Key Dependencies

- Proxmox host access
- Backup datastore storage
- Time synchronization
- Private backup credentials
- Restore network or isolated test target

## Network / DNS

PBS should be reachable from Proxmox over the private network. It should not be published through the public reverse proxy.

Example:

```text
proxmox.home.example.com -> pbs.home.example.com
```

## Backup Notes

- Configure backup schedules for important guests.
- Use retention rules that match the storage available.
- Run verification jobs.
- Keep datastore encryption material private.
- Document the last successful restore test.

## Security Notes

- Keep the PBS UI private.
- Restrict backup credentials to the required datastore and permissions.
- Do not publish datastore paths, encryption material, or raw backup exports.
- Treat PBS like critical infrastructure, not a normal app dashboard.

## What Viewers Can Learn

- Why backups need restore tests.
- How PBS differs from copying VM disk files.
- How retention and pruning prevent backup storage from growing forever.
- Why backup systems need their own security boundary.

## Future Improvements

- Add a sanitized retention policy example.
- Add a restore-test checklist.
- Document which VMs are critical and which are easy to rebuild.
