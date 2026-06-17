# Service Map

This page maps the homelab services by role and exposure level. Each service also has a dedicated README under `services/`.

## Core Infrastructure

| Service | Category | Example DNS | Default Exposure | Service Docs |
|---|---|---|---|---|
| pfSense | Firewall / router | `firewall.home.example.com` | Private | [pfSense](../services/pfsense/README.md) |
| Pi-hole primary | DNS | `pihole1.home.example.com` | Private | [Pi-hole](../services/pihole/README.md) |
| Pi-hole secondary | DNS | `pihole2.home.example.com` | Private | [Pi-hole](../services/pihole/README.md) |
| Proxmox | Virtualization | `proxmox.home.example.com` | Private | [Proxmox](../services/proxmox/README.md) |
| Proxmox Backup Server | Backup | `pbs.home.example.com` | Private | [PBS](../services/proxmox-backup-server/README.md) |
| Synology NAS | Storage | `nas.home.example.com` | Private | [Synology](../services/synology/README.md) |
| Rocky Linux ZFS storage | Storage | `zfs.home.example.com` | Private | [ZFS storage](../services/zfs-storage/README.md) |
| NGINX reverse proxy | Reverse proxy | `proxy.home.example.com` | Private / limited | [Reverse proxy](../services/reverse-proxy/README.md) |
| Cloudflare Tunnel | Public edge | Public hostnames only | Limited | [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md) |

## Observability

| Service | Purpose | Default Exposure |
|---|---|---|
| Grafana | Dashboards for metrics and logs | Private |
| Prometheus | Metrics collection | Private |
| Node Exporter | Host metrics | Private |
| cAdvisor | Container metrics | Private |
| Blackbox Exporter | Endpoint checks | Private |
| Speedtest exporter | Network performance visibility | Private |
| Uptime Kuma | Service uptime checks | Private |
| Loki | Log aggregation | Private |
| Promtail | Log shipping | Private |
| Proxmox exporter | Proxmox metrics | Private |

See [services/monitoring/README.md](../services/monitoring/README.md).

## App And Learning Services

| Service | Purpose | Default Exposure | Service Docs |
|---|---|---|---|
| Wiki.js | Documentation and runbooks | Partial | [Wiki.js](../services/wiki/README.md) |
| Glance | Homelab dashboard | Private | [Glance](../services/glance/README.md) |
| Nextcloud | File sync and personal cloud | Limited | [Nextcloud](../services/nextcloud/README.md) |
| Plex | Media streaming | Limited | [Media stack](../services/media-stack/README.md) |
| Servarr stack | Media automation | Private | [Media stack](../services/media-stack/README.md) |
| Transmission | Download client | Private | [Media stack](../services/media-stack/README.md) |
| Jellyseerr | Media request workflow | Private | [Media stack](../services/media-stack/README.md) |
| Tautulli | Plex analytics | Private | [Media stack](../services/media-stack/README.md) |
| Tdarr | Media transcode automation | Private | [Media stack](../services/media-stack/README.md) |
| Local AI endpoint | Local model serving | Private | [Local AI](../services/local-ai/README.md) |
| Open WebUI | Local AI web interface | Private | [Local AI](../services/local-ai/README.md) |
| FinanceHQ | Local-first finance command center | Private | [FinanceHQ](../services/financehq/README.md) |
| CareerFill | Job application workflow tool | Private | [CareerFill](../services/careerfill/README.md) |
| AWX | Ansible automation UI | Private | [AWX](../services/automation-awx/README.md) |

## Public-Safe Service Documentation Pattern

Each service README should answer:

- What problem does this service solve?
- Where does it sit in the lab?
- What host or runtime owns it?
- What does it depend on?
- How does DNS and network access work?
- What needs to be backed up?
- What should never be exposed?
- What can viewers learn from it?

## Exposure Rule Of Thumb

| Exposure | Use For | Avoid For |
|---|---|---|
| Private LAN | Admin panels, dashboards, storage, automation | Public users |
| VPN | Remote admin access | Anonymous access |
| Reverse proxy only | Clean internal HTTPS names | Bypassing auth |
| Cloudflare Tunnel | Selected public services | Broad admin access |

When in doubt, keep the service private and document what would need to be hardened before publishing it.
