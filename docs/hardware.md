# Hardware

## Compute

| Host | Type | Role | Notes |
|---|---|---|---|
| Proxmox Host | Dell PowerEdge T140 | Main virtualization host | Runs core VMs |
| GPU Server | Linux server with NVIDIA RTX A2000 12GB | Local AI / media processing | Used for LLM and GPU workloads |
| ZFS Storage Server | Rocky Linux + ZFS | Dedicated storage | ZFS pool for storage experiments |
| Synology NAS | 4x 8TB RAID5 | Shared storage | Media, files, backup target |

## Networking

| Device | Role |
|---|---|
| pfSense Firewall | Routing, firewall policy, VPN, VLANs |
| Managed Switch | LAN switching |
| Wireless Router / AP | Wi-Fi access |
| Pi-hole Primary | DNS filtering |
| Pi-hole Secondary | DNS redundancy |

## Storage

| Storage | Purpose |
|---|---|
| Synology NAS | Main shared storage |
| ZFS Server | Linux/ZFS learning and storage |
| Proxmox Backup Server datastore | VM backups |
| Local VM disks | Application runtime storage |

## Notes

Keep serial numbers, exact WAN details, and sensitive topology information out of the public repo.
