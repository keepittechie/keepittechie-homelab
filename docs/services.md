# Service Map

## Core Services

| Service | Category | Purpose | Public? |
|---|---|---|---|
| pfSense | Network | Firewall/router | No |
| Pi-hole Primary | DNS | DNS filtering | No |
| Pi-hole Secondary | DNS | DNS redundancy | No |
| Proxmox | Virtualization | VM host | No |
| Proxmox Backup Server | Backup | Incremental VM backups | No |
| Synology | Storage | NAS | No |
| NGINX Reverse Proxy | Proxy | Internal HTTPS routing | Limited |
| Cloudflare Tunnel | Edge Access | Public access for selected services | Limited |

## App Services

| Service | Category | Purpose | Public? |
|---|---|---|---|
| Wiki.js | Docs | Public/private documentation | Partial |
| Nextcloud | Cloud | File sync and personal cloud | Limited |
| Glance | Dashboard | Homelab homepage | No |
| Grafana | Monitoring | Metrics dashboards | No |
| Prometheus | Monitoring | Metrics collection | No |
| Loki | Logs | Log aggregation | No |
| Plex | Media | Media streaming | Limited |
| Servarr Stack | Media Automation | Media management | No |
| Open WebUI | AI | Local AI interface | No |
| FinanceHQ | Personal App | Local financial command center | No |
| CareerFill | Personal App | Job application workflow | No |
| AWX | Automation | Ansible automation | No |

## Documentation Rule

Each service gets its own folder under `services/` with:

- What it does
- Where it runs
- Dependencies
- Ports
- Backup notes
- Restore notes
- Security notes
- Video ideas
