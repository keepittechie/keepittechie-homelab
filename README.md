# KeepItTechie Homelab

This repo is the public, viewer-friendly breakdown of the KeepItTechie homelab. It documents the architecture, service roles, and learning path behind the lab without turning the repo into a private config dump.

KeepItTechie focuses on Linux, open source, self-hosting, server administration, automation, local AI, and practical homelab learning. This repo supports that same teaching style: explain what each piece does, where it fits, why it exists, and what viewers can learn from it.

## Start Here

| Area | Link | What It Covers |
|---|---|---|
| Overview | [docs/overview.md](docs/overview.md) | Big-picture layout and design goals |
| Hardware | [docs/hardware.md](docs/hardware.md) | Compute, network, storage, and backup hardware |
| Network | [docs/network.md](docs/network.md) | pfSense, DNS, segmentation, and access patterns |
| Services | [docs/services.md](docs/services.md) | Service map and public/private boundaries |
| Storage and Backups | [docs/storage-and-backups.md](docs/storage-and-backups.md) | Synology, ZFS, PBS, and restore thinking |
| Security | [docs/security-notes.md](docs/security-notes.md) | Public repo safety and exposure rules |
| Content Map | [docs/content-map.md](docs/content-map.md) | YouTube episode ideas tied to the lab |

## Lab At A Glance

| Layer | Stack |
|---|---|
| Firewall / Router | pfSense |
| DNS | Two Pi-hole VMs |
| Virtualization | Proxmox |
| Storage | Synology NAS and Rocky Linux ZFS storage server |
| VM Backups | Proxmox Backup Server |
| Reverse Proxy | NGINX reverse proxy |
| Selected Public Access | Cloudflare Tunnel |
| Monitoring | Grafana, Prometheus, exporters, Loki, Promtail |
| Media | Plex, Servarr stack, Tautulli, Tdarr |
| Local AI | NVIDIA RTX A2000 12GB server, llama.cpp-compatible API, Open WebUI |
| Docs / Dashboard | Wiki.js and Glance |
| Personal Apps | FinanceHQ and CareerFill |
| Automation | AWX and Ansible control node |

## Example Sanitized Topology

```text
Internet
  |
Cloudflare Tunnel for selected public apps
  |
pfSense firewall
  |
10.10.0.0/24 lab LAN
  |
  +-- proxmox.home.example.com
  |   +-- pihole1.home.example.com
  |   +-- pihole2.home.example.com
  |   +-- proxy.home.example.com
  |   +-- grafana.home.example.com
  |   +-- ai.home.example.com
  |
  +-- nas.home.example.com
  +-- zfs.home.example.com
  +-- pbs.home.example.com
```

The names above are examples. They show the shape of the lab without publishing the live private records.

## Documentation Philosophy

- Document the architecture and reasoning, not raw private exports.
- Show enough detail for viewers to learn and rebuild similar patterns.
- Prefer sanitized examples over copied production configuration.
- Keep admin surfaces private unless there is a clear reason to publish a service.
- Treat restore notes as seriously as install notes.
- Keep the repo useful even when the real lab changes.

## Public Safety Rules

This repo should never contain:

- Real passwords or recovery codes
- API keys, service account credentials, or tunnel credentials
- SSH private keys, VPN keys, or backup encryption keys
- Private certificates or certificate authority keys
- Full pfSense, switch, NAS, or app exports with secrets
- Real public IP addresses
- Raw `.env` files
- Financial data, job application data, private messages, or personal records

Use `.env.example`, sanitized YAML, Markdown explanations, and placeholders such as `REPLACE_ME`.

## Repo Layout

| Path | Purpose |
|---|---|
| `docs/` | Main viewer-facing documentation |
| `services/` | Per-service breakdowns |
| `inventory/sanitized/` | Safe example inventory |
| `inventory/private.example/` | Pattern for private inventory that should stay untracked |
| `diagrams/` | Sanitized diagrams and diagram notes |
| `templates/` | Reusable documentation templates |

## Suggested Workflow

Before committing, review `git status` and run a sensitive-string scan for keys, credential assignments, tunnel credentials, and private key headers. If the scan finds anything sensitive, sanitize it before committing.

## Status

This is a living public reference for the KeepItTechie homelab. It is intentionally documentation-first: enough structure to teach from, without exposing the private operational details that belong in a private notes repo, password manager, or internal Wiki.js admin space.

## License

This homelab documentation is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE).

You are free to share and adapt the material as long as you give appropriate credit to Joshua Lacy / KeepItTechie.
