# Hardware

This page documents hardware roles at a public-safe level. Exact serial numbers, WAN details, full storage labels, and private management information should stay out of this repo.

## Compute

| Name / Role | Platform | Main Use | Public Notes |
|---|---|---|---|
| Proxmox host | Dell PowerEdge T140 class server | Primary virtualization | Runs core VMs and lab workloads |
| GPU / AI server | Linux server with NVIDIA RTX A2000 12GB | Local AI and GPU-assisted workloads | Supports local inference, Open WebUI, and media processing experiments |
| Docker app VM host group | Proxmox VMs | App and container workloads | Used for services such as Wiki.js, monitoring, dashboards, and personal apps |
| Media VM | Proxmox VM | Plex and related media services | Keeps media workloads separate from core infrastructure |
| Automation VM | Linux VM | AWX / Ansible control | Runs repeatable admin workflows |

## Network

| Device | Purpose | Notes |
|---|---|---|
| pfSense firewall | Routing, firewalling, DHCP, DNS forwarding, VPN, segmentation | Main control point for network policy |
| Managed switch | Wired network aggregation | VLAN-capable switching where needed |
| Wireless access point / router | Wi-Fi access | Kept separate from core routing decisions |
| Pi-hole primary VM | DNS filtering and local DNS | Example alias: `pihole1.home.example.com` |
| Pi-hole secondary VM | DNS redundancy | Example alias: `pihole2.home.example.com` |

## Storage

| Storage System | Role | What It Teaches |
|---|---|---|
| Synology NAS | Shared files, media storage, backup targets | NAS administration, shares, snapshots, and appliance workflows |
| Rocky Linux ZFS storage server | Linux storage and ZFS datasets | ZFS pools, datasets, scrubs, snapshots, and Linux-first storage practice |
| Proxmox Backup Server | VM and container backups | Deduplication, retention, restore tests, and backup verification |
| Local VM disks | OS and application runtime storage | Sizing, separation of app data, and restore planning |

## Example Hardware Inventory

| Sanitized Host | Role | Example DNS |
|---|---|---|
| `pfsense` | Firewall | `firewall.home.example.com` |
| `pontus` | Primary DNS | `pihole1.home.example.com` |
| `priapus` | Secondary DNS | `pihole2.home.example.com` |
| `zelus` | Reverse proxy / automation VM | `proxy.home.example.com` |
| `heimdall` | Docker app VM | `apps.home.example.com` |
| `apollo` | Media VM | `plex.home.example.com` |
| `chronos` | Proxmox Backup Server | `pbs.home.example.com` |
| `bison` | Rocky Linux ZFS storage | `zfs.home.example.com` |
| `hephaestus` | GPU and local AI workloads | `ai.home.example.com` |

## Sizing Notes

- DNS, reverse proxy, and small dashboards do not need large VMs.
- Monitoring and logging need enough disk for retention, not just CPU.
- Media and AI workloads benefit from deliberate storage paths and GPU planning.
- Backup storage should be sized for retention and restore testing, not just the first backup.

## Public Repo Boundary

Keep these details private:

- Serial numbers
- Full disk IDs
- Exact WAN information
- Real public IPs
- Full switch, firewall, or NAS exports
- Photos showing labels, keys, QR codes, or management screens
