# ZFS Storage Server

## Purpose

The ZFS storage server is a Rocky Linux storage system used for Linux-first storage learning, resilient datasets, snapshots, scrubs, and storage experiments.

## Why This Matters

ZFS is different from a normal filesystem because it combines storage pooling, checksumming, snapshots, datasets, and data integrity features into one storage platform. It is useful for learning how Linux storage works beneath higher-level applications.

This server complements the Synology NAS. The NAS provides appliance storage; the ZFS server provides hands-on Linux storage practice.

## Where It Fits in the Homelab

```text
Linux services and lab clients
  |
NFS / SMB / direct mount
  |
zfs.home.example.com
  |
ZFS pools, datasets, snapshots, and scrubs
```

The ZFS server is not documented here as a live pool export. It is documented as a safe learning pattern.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `bison` |
| Runtime | Rocky Linux with ZFS |
| Example DNS | `zfs.home.example.com` |
| Public access | No |
| Main use | Datasets, snapshots, Linux storage learning |

## Storage / Data Layout

Sanitized dataset examples:

| Dataset | Purpose | Snapshot Policy | Notes |
|---|---|---|---|
| `tank/media` | Media storage experiments | Daily or weekly | Keep real library paths private |
| `tank/backups` | Backup landing area | Daily | Do not publish backup contents |
| `tank/appdata` | App support data | Daily and before major changes | May need app-aware backups too |
| `tank/lab` | Scratch space for learning | Optional | Safe place for experiments |

Document dataset purpose and retention. Do not publish exact disk serials, full pool status, or private mount maps.

## Network / DNS

Example:

```text
zfs.home.example.com -> 10.10.0.x
```

Expose only the storage protocols needed by trusted clients. Management access should stay private.

## Key Responsibilities

- Provide Linux-based storage for learning and selected workloads.
- Organize data into datasets.
- Support snapshots for rollback.
- Run scrubs to verify stored data.
- Teach storage concepts beyond appliance administration.
- Document storage intent without exposing hardware details.

## Example Public-Safe Configuration

Useful commands to document the workflow:

```bash
zpool status
zfs list
zpool scrub tank
zfs snapshot tank/appdata@example-snapshot
```

Do not include real command output in the public repo if it exposes disk serials, pool topology, mount paths, or private dataset names.

## Backup and Restore Notes

- ZFS snapshots are local rollback points, not full off-host backups.
- Replicate or back up critical datasets when possible.
- Test file rollback using a safe demo dataset.
- Keep pool topology and disk identity in private docs.
- Pair ZFS snapshots with app-aware backups for databases and stateful services.

## Security Notes

- Keep management access private.
- Restrict NFS/SMB access by client and role.
- Do not publish disk serial numbers.
- Do not publish full `zpool status` output from the live server.
- Avoid exposing dataset names that reveal private projects or people.

## Common Mistakes to Avoid

- Treating snapshots as off-site backups.
- Running scrubs but never reviewing results.
- Sharing every dataset broadly over the network.
- Publishing exact pool layout or disk identifiers.
- Forgetting that app-consistent backups may still be needed.

## What Viewers Can Learn

- How pools, datasets, snapshots, and scrubs fit together.
- Why ZFS is useful for storage learning.
- How ZFS differs from a normal filesystem.
- How to document storage architecture safely.
- How Linux storage complements a NAS appliance.

## Future Improvements

- Add a sanitized snapshot schedule.
- Add a fake dataset restore walkthrough.
- Add a public-safe ZFS health checklist.
