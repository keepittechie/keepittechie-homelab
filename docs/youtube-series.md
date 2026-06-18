# YouTube Companion Series

This page maps the homelab documentation to potential KeepItTechie video topics. It is a public companion plan, not a private production schedule.

Each topic includes:

- Goal
- What viewers learn
- Repo references
- Safe demo ideas

| Episode | Goal | What Viewers Learn | Repo References | Safe Demo Ideas |
|---|---|---|---|---|
| 1. Full Homelab Tour | Explain the full lab at a high level | How firewall, DNS, virtualization, storage, monitoring, media, AI, and apps fit together | `README.md`, `docs/episodes/full-homelab-tour.md`, `docs/overview.md`, `diagrams/homelab-overview.md` | Walk through the Mermaid diagram and sanitized service matrix |
| 2. Building a Homelab in Stages | Give beginners a safe build path | How to start small, add layers, and avoid copying a private setup blindly | `docs/build-your-own.md`, `docs/viewer-guide.md`, `docs/glossary.md` | Walk through stages with sanitized names such as `home.example.com` |
| 3. How the pfSense Network Is Structured | Teach the network control plane | Routing, DHCP, firewall policy, and why admin tools stay private | `docs/network.md`, `services/pfsense/README.md` | Use fake VLANs and `10.10.0.0/24` examples |
| 4. Pi-hole and Internal DNS | Show why local DNS matters | Primary/secondary DNS, service identities, and troubleshooting name resolution | `docs/episodes/dns-pihole.md`, `services/pihole/README.md`, `inventory/sanitized/hosts.example.yml` | Add a fake `grafana.home.example.com` record |
| 5. Proxmox VM Layout | Explain VM role separation | Why virtualization helps with isolation, testing, and rebuilds | `docs/episodes/proxmox-vm-layout.md`, `services/proxmox/README.md`, `docs/hardware.md` | Show a sanitized VM role table |
| 6. Proxmox Backup Server | Show backup thinking | Retention, verification, and restore testing | `services/proxmox-backup-server/README.md`, `docs/storage-and-backups.md` | Restore a disposable demo VM or walk through a sanitized checklist |
| 7. Synology NAS vs Linux ZFS Storage | Compare storage approaches | Appliance NAS workflows versus Linux storage learning | `services/synology/README.md`, `services/zfs-storage/README.md` | Compare sanitized share and dataset examples |
| 8. Reverse Proxy and Internal HTTPS | Make services easier to reach | DNS aliases, TLS, proxy routing, and private admin boundaries | `services/reverse-proxy/README.md`, `docs/network.md` | Build a fake `app.home.example.com` route |
| 9. Cloudflare Tunnel Done Safely | Explain selective public access | Why public access should be intentional and documented | `services/cloudflare-tunnel/README.md`, `docs/security-notes.md` | Review a public-access decision table without showing credentials |
| 10. Monitoring the Homelab with Grafana | Build useful visibility | Metrics, logs, exporters, and uptime checks | `services/monitoring/README.md`, `docs/service-matrix.md` | Show a recreated dashboard with fake hostnames |
| 11. Local AI on Linux | Explain local inference | GPU role, model storage, Open WebUI, and local-first AI tooling | `docs/apps-and-ai.md`, `services/local-ai/README.md` | Send a placeholder request to `https://ai.home.example.com/v1` |
| 12. Self-Hosted Dashboard | Show daily lab navigation | Service grouping, dashboard links, health checks, and public-safe dashboard design | `docs/apps-and-ai.md`, `services/glance/README.md`, `diagrams/homelab-overview.md` | Build a sanitized dashboard section with fake links |
| 13. Building a Personal Wiki | Show documentation habits | Public/private namespaces, runbooks, content planning, and safe publishing boundaries | `docs/apps-and-ai.md`, `services/wiki/README.md` | Create fake public/private namespace examples |
| 14. Nextcloud Private Cloud | Explain self-hosted file sync | User files, app data, database backups, reverse proxy dependency, and restore planning | `docs/apps-and-ai.md`, `services/nextcloud/README.md` | Use fake files and a sanitized backup checklist |
| 15. Media Stack Overview | Explain a multi-app media workflow | Plex, Servarr-style automation, Tautulli, Tdarr, storage dependencies, and private dashboards | `docs/apps-and-ai.md`, `services/media-stack/README.md` | Map fake media paths and service roles |
| 16. AWX and Ansible Automation | Turn admin tasks into repeatable jobs | Inventories, playbooks, credentials, job templates, and guardrails | `docs/apps-and-ai.md`, `services/automation-awx/README.md`, `inventory/sanitized/hosts.example.yml` | Run a read-only fake inventory report |
| 17. Building Local-First Personal Apps | Connect infrastructure to real workflows | Private app hosting, data boundaries, backups, and local AI support | `docs/apps-and-ai.md`, `services/financehq/README.md`, `services/careerfill/README.md` | Use fake financial and job-search sample data |

## Episode Format

Each topic can follow a simple walkthrough format:

```text
Problem:
What pain point does this solve?

Architecture:
Where does it sit in the lab?

Build or walkthrough:
What are the key pieces?

Security:
What should viewers avoid exposing?

Demo:
What does success look like?

Viewer exercise:
What can viewers try in their own lab?
```

## Publishing Notes

- Episode companion pages live in [docs/episodes](episodes/README.md).
- Add video links back into this file after episodes are published.
- Keep raw admin screens, real domains, public IPs, and credentials out of recordings.
- Use sanitized diagrams and fake data in repeatable demos.
- Use `home.example.com` service names and generic paths such as `/mnt/storage/appdata`.
