# KeepItTechie Homelab

A public, viewer-friendly breakdown of the KeepItTechie homelab: networking, virtualization, storage, monitoring, media services, local AI, backups, and self-hosted apps.

This repo is designed to be both documentation and a learning resource. It shows the *architecture and reasoning* behind the lab without publishing secrets, API keys, public tunnel tokens, passwords, private certificates, or sensitive internal details.

## Table of Contents

- [Homelab Overview](docs/overview.md)
- [Hardware](docs/hardware.md)
- [Network Design](docs/network.md)
- [Service Map](docs/services.md)
- [Storage and Backups](docs/storage-and-backups.md)
- [Monitoring](services/monitoring/README.md)
- [Local AI Stack](services/local-ai/README.md)
- [Security Notes](docs/security-notes.md)
- [Content Map for YouTube](docs/content-map.md)

## Core Design Goals

- Teach Linux, networking, and self-hosting through real infrastructure.
- Keep important services local-first.
- Separate public-facing services from private admin services.
- Use DNS names instead of memorizing IP addresses.
- Document every service well enough to rebuild it later.
- Avoid exposing secrets or sensitive configuration.

## Lab Summary

| Area | Stack |
|---|---|
| Firewall / Routing | pfSense |
| DNS | Pi-hole primary and secondary |
| Virtualization | Proxmox |
| Storage | Synology NAS, ZFS storage server, Proxmox Backup Server |
| Reverse Proxy | NGINX reverse proxy, Cloudflare Tunnel for selected public services |
| Monitoring | Grafana, Prometheus, exporters, Loki/Promtail |
| Media | Plex, Servarr stack, Tautulli, Tdarr |
| Local AI | GPU server, llama.cpp / OpenAI-compatible local endpoint, Open WebUI |
| Apps | Wiki.js, Nextcloud, FinanceHQ, CareerFill, Glance dashboard |
| Automation | AWX / Ansible control node |

## Public Safety Rules

This repo should never contain:

- Real passwords
- API keys
- Cloudflare tunnel tokens
- VPN keys
- Private SSL certificates
- Full firewall exports with secrets
- `.env` files
- Public IP addresses unless intentionally shared
- Backup encryption keys

Use `.env.example`, sanitized YAML, and documentation instead.

## Suggested Repo Workflow

```bash
git clone git@github.com:keepittechie/homelab.git
cd homelab

# Add documentation and sanitized configs only
git status
git add .
git commit -m "Initial KeepItTechie homelab documentation"
git push
```

## Status

This repo is a living document. The goal is not perfection on day one - the goal is to make the lab easier to explain, rebuild, and teach from.
