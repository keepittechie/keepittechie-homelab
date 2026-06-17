# YouTube Companion Series

This plan turns the public homelab repo into a companion resource for KeepItTechie videos. Each episode should connect a real lab pattern to a practical lesson viewers can reuse.

| Episode | Goal | What Viewers Learn | Repo Files To Reference | Safe Demo Ideas |
|---|---|---|---|---|
| 1. Full Homelab Tour | Explain the full lab at a high level | How firewall, DNS, virtualization, storage, monitoring, media, AI, and apps fit together | `README.md`, `docs/overview.md`, `diagrams/homelab-overview.md` | Walk through the Mermaid diagram and sanitized service matrix |
| 2. How My pfSense Network Is Structured | Teach the network control plane | Routing, DHCP, firewall policy, and why admin tools stay private | `docs/network.md`, `services/pfsense/README.md` | Use fake VLANs and `10.10.0.0/24` examples |
| 3. Pi-hole and Internal DNS | Show why local DNS matters | Primary/secondary DNS, service aliases, and troubleshooting name resolution | `services/pihole/README.md`, `inventory/sanitized/hosts.example.yml` | Add a fake `grafana.home.example.com` record |
| 4. Proxmox VM Layout | Explain VM role separation | Why virtualization helps with isolation, testing, and rebuilds | `services/proxmox/README.md`, `docs/hardware.md` | Show a sanitized VM role table |
| 5. Proxmox Backup Server | Show backup thinking | Retention, verification, and restore testing | `services/proxmox-backup-server/README.md`, `docs/storage-and-backups.md` | Restore a disposable demo VM or walk through a sanitized checklist |
| 6. Synology NAS vs Linux ZFS Storage | Compare storage approaches | Appliance NAS workflows versus Linux storage learning | `services/synology/README.md`, `services/zfs-storage/README.md` | Compare sanitized share and dataset examples |
| 7. Reverse Proxy and Internal HTTPS | Make services easier to reach | DNS aliases, TLS, proxy routing, and private admin boundaries | `services/reverse-proxy/README.md`, `docs/network.md` | Build a fake `app.home.example.com` route |
| 8. Cloudflare Tunnel Done Safely | Explain selective public access | Why public access should be intentional and documented | `services/cloudflare-tunnel/README.md`, `docs/security-notes.md` | Review a public-access decision table without showing credentials |
| 9. Monitoring the Homelab with Grafana | Build useful visibility | Metrics, logs, exporters, and uptime checks | `services/monitoring/README.md`, `docs/service-matrix.md` | Show a recreated dashboard with fake hostnames |
| 10. Local AI on Linux | Explain local inference | GPU limits, model serving, Open WebUI, and local-first AI tooling | `services/local-ai/README.md` | Send a demo request to a fake local endpoint |
| 11. Self-Hosted Dashboard | Show daily lab navigation | Service grouping, dashboard links, and safe shortcuts | `services/glance/README.md`, `diagrams/homelab-overview.md` | Build a sanitized dashboard section |
| 12. AWX and Ansible Automation | Turn admin tasks into repeatable jobs | Inventories, playbooks, credentials, and guardrails | `services/automation-awx/README.md`, `inventory/sanitized/hosts.example.yml` | Run a read-only fake inventory report |
| 13. Building Local-First Personal Apps | Connect infrastructure to real workflows | Private app hosting, data boundaries, backups, and local AI support | `services/financehq/README.md`, `services/careerfill/README.md` | Use fake financial and job-search sample data |

## Episode Format

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

- Add video links back into this file after episodes are published.
- Keep raw admin screens, real domains, public IPs, and credentials out of recordings.
- Use sanitized diagrams and fake data for repeatable demos.
