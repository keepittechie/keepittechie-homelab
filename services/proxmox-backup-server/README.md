# Proxmox Backup Server

## Purpose

Proxmox Backup Server, or PBS, is the main VM and container backup target for the homelab. It stores deduplicated backups from Proxmox and provides a restore workflow that fits the virtualization layer.

## Why This Matters

Backups are only useful if they can be restored. PBS matters because it moves the lab from hope-based recovery to a recovery path that can be tested.

It also teaches viewers that a backup system needs its own documentation, retention policy, and security boundary.

## Where It Fits in the Homelab

```text
Proxmox guests
  |
scheduled backups
  |
pbs.home.example.com
  |
restore test or production recovery
```

PBS is separate from the VM host so a failure of the hypervisor does not automatically erase the backup history.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `chronos` |
| Runtime | Dedicated PBS install or VM |
| Example DNS | `pbs.home.example.com` |
| Public access | No |
| Primary clients | Proxmox hosts |

## Network / DNS

PBS should be reachable from Proxmox over trusted internal networks only:

```text
proxmox.home.example.com -> pbs.home.example.com
```

It should not be exposed through public routes or general dashboards.

## Key Responsibilities

- Receive Proxmox VM and container backups.
- Store backups in datastores.
- Deduplicate backup data.
- Apply retention and pruning policies.
- Verify backups where possible.
- Support file-level or full guest restores.
- Provide evidence that critical services can be recovered.

## Example Public-Safe Configuration

Example retention policy:

| Backup Group | Example Schedule | Example Retention | Notes |
|---|---|---|---|
| Core infrastructure VMs | Nightly | Keep recent daily and weekly points | DNS, proxy, monitoring, automation |
| Personal app VMs | Nightly | Keep enough history for rollback | Requires app-aware database backups too |
| Media automation VMs | Weekly | Keep fewer points | Easier to rebuild than core services |
| Test VMs | On demand | Short retention | Avoid filling backup storage |

Example backup/restore checklist:

- [ ] Confirm the VM or container is included in the backup schedule.
- [ ] Confirm the latest backup completed successfully.
- [ ] Confirm retention policy is documented.
- [ ] Restore into an isolated test target when possible.
- [ ] Validate DNS, login, app health, and storage mounts.
- [ ] Record restore test evidence in public-safe notes.

## Backup and Restore Notes

- Datastores are backup storage locations managed by PBS.
- Retention should match service importance and available storage.
- Verification jobs help catch backup problems earlier.
- Restore evidence should include date, service, restore target, and result.
- Keep backup credentials, encryption material, and datastore internals private.

## Security Notes

- Keep the PBS UI private.
- Use scoped backup credentials.
- Do not publish datastore paths, keys, or raw backup exports.
- Treat PBS as critical infrastructure.
- Keep restore notes public-safe and free of real private paths.

## Common Mistakes to Avoid

- Never testing a restore.
- Keeping backups on the same failed storage as the original workload.
- Backing up databases only through crash-consistent VM backups.
- Forgetting to prune old backups.
- Publishing backup screenshots that reveal private paths or names.

## What Viewers Can Learn

- Why restore testing matters.
- How PBS differs from a plain file copy.
- How retention, pruning, and verification fit together.
- How to document recovery without leaking infrastructure details.

## Future Improvements

- Add one documented restore test.
- Add a service criticality table.
- Add app-aware backup notes for database-backed services.
