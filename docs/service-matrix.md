# Service Matrix

This matrix gives viewers a quick way to understand what each service does, where it runs, how it should be accessed, and how carefully it should be backed up. It is intentionally sanitized for public GitHub.

For the first deep-dive reading path, start with [Core Infrastructure](core-infrastructure.md). For a friendlier grouped list, use the [Service Catalog](service-catalog.md). For a sanitized role view, use [Public-Safe Inventory](inventory-public.md). For storage, backups, and visibility, read [Storage and Monitoring](storage-monitoring.md). For application, media, local AI, dashboard, documentation, and automation services, read [Apps and AI](apps-and-ai.md).

| Service | Category | Runs On | Access Level | Backup Priority | Public Repo Notes |
|---|---|---|---|---|---|
| pfSense | Network | Firewall appliance or VM | VPN Only | Critical | Document rule philosophy, not raw exports |
| Pi-hole Primary | DNS | Proxmox VM, example `pontus` | Private LAN | High | Use sanitized records such as `pihole1.home.example.com` |
| Pi-hole Secondary | DNS | Proxmox VM, example `priapus` | Private LAN | High | Keep paired with the primary resolver |
| Proxmox | Virtualization | Hypervisor host | VPN Only | Critical | Keep management private and document VM roles |
| Proxmox Backup Server | Backup | Dedicated host or VM, example `chronos` | VPN Only | Critical | Track retention and restore tests, not datastore secrets |
| Synology NAS | Storage | Synology DSM appliance | Private LAN | Critical | Document share purpose without private paths |
| ZFS Storage Server | Storage | Rocky Linux server, example `bison` | Private LAN | High | Keep pool layout and disk IDs private |
| NGINX Reverse Proxy | Proxy | Linux VM, example `zelus` | Private LAN | High | Show sanitized routing patterns only |
| Cloudflare Tunnel | Edge access | Linux host or app VM | Public via Tunnel | High | Document exposure decisions, not credentials |
| Grafana | Monitoring | Docker app host | Private LAN | Medium | Sanitize dashboards before screenshots |
| Prometheus | Monitoring | Docker app host | Internal Only | Medium | Keep scrape targets private |
| Loki | Logging | Docker app host | Internal Only | Medium | Avoid publishing logs or private labels |
| Plex | Media | Media VM or container | Limited Public | Medium | Keep library paths, users, and watch history private |
| Servarr Stack | Media automation | Media automation VM or containers | Private LAN | Medium | Keep automation dashboards private |
| Tautulli | Media analytics | Media VM or container | Private LAN | Medium | Can expose user activity in screenshots |
| Tdarr | Media processing | GPU-capable host or container | Private LAN | Medium | Keep queues and media paths private |
| Open WebUI | Local AI | GPU/app host | Private LAN | Medium | Do not expose local AI chats publicly |
| llama.cpp endpoint | Local AI | GPU host or service container | Internal Only | Medium | Keep endpoint private unless heavily protected |
| Wiki.js | Documentation | Docker app host or VM | Limited Public | High | Separate public pages from private runbooks |
| Nextcloud | File sync | App VM or app host | Limited Public | Critical | Back up database and data together |
| Glance or Homepage dashboard | Dashboard | App host | Private LAN | Low | Publish layout ideas, not live links |
| FinanceHQ | Personal app | App VM or container | Private LAN | Critical | Use fake finance data only |
| CareerFill | Personal app | App VM or container | Private LAN | High | Keep applications, messages, and resumes private |
| AWX | Automation | Automation VM or app host | VPN Only | High | Keep credentials, inventories, and vault data private |

## Access Level Definitions

| Access Level | Meaning |
|---|---|
| Private LAN | Reachable only from trusted internal networks |
| VPN Only | Admin surface that should require trusted remote access |
| Public via Tunnel | Intentionally published through a tunnel and reviewed for exposure |
| Internal Only | Backend service that should not be directly browsed by users |
| Limited Public | May be public in a controlled way, but should be reviewed carefully |

## How To Use This Matrix

- Start here when deciding whether a service belongs in a video, diagram, or public example.
- Update it whenever a service moves hosts or changes exposure level.
- Treat backup priority as a documentation priority too: critical services need clear restore notes.
- Use the core infrastructure deep dives for the network, DNS, virtualization, backup, proxy, and tunnel layers.
- Use the storage and monitoring guide for NAS, ZFS, PBS restore test evidence, and Grafana/Prometheus/Loki visibility.
- Use the apps and AI guide for local AI, media, documentation, dashboards, personal apps, and automation.
- Use the service catalog when a less dense service overview is easier to read.
