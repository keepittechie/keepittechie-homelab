# Proxmox

## Purpose

Proxmox is the virtualization platform for the homelab. It runs the VMs and containers that power DNS, reverse proxying, monitoring, media, local AI tooling, personal apps, and automation.

## Where It Fits

```text
Physical server
  |
Proxmox
  |
VMs and containers
  |
DNS, proxy, apps, monitoring, media, AI, automation
```

Proxmox gives the lab flexibility: services can be moved, backed up, restored, cloned, and isolated more easily than if every workload ran directly on bare metal.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Proxmox VE on server hardware |
| Example DNS | `proxmox.home.example.com` |
| Public access | No |
| Backup target | Proxmox Backup Server |

## Key Dependencies

- Reliable storage for VM disks
- Proxmox Backup Server
- Pi-hole DNS
- pfSense network access
- NAS or ZFS storage mounts where needed

## Network / DNS

Proxmox management should stay on trusted networks only. Guest VMs can have hostnames and service aliases:

```text
pontus.home.example.com      # primary DNS VM
priapus.home.example.com     # secondary DNS VM
zelus.home.example.com       # proxy / automation VM
heimdall.home.example.com    # app VM
hephaestus.home.example.com  # GPU / AI VM
```

Public docs should avoid publishing full VM inventories when they reveal sensitive services or access paths.

## Backup Notes

- Back up important VMs to Proxmox Backup Server.
- Keep restore notes per service, not only per VM.
- Test restores into an isolated network when possible.
- Document which services need app-aware database dumps in addition to VM backups.

## Security Notes

- Keep the Proxmox web UI private.
- Use strong admin authentication.
- Avoid broad guest-to-guest network access.
- Do not publish cluster credentials, API credentials, or full host exports.

## What Viewers Can Learn

- Why virtualization is useful in a homelab.
- How to separate services by VM role.
- How VM backups and app backups solve different problems.
- How to grow a lab without rebuilding every service from scratch.

## Future Improvements

- Add a sanitized VM role table.
- Add a basic restore test example.
- Document guest naming conventions.
