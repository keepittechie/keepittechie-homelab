# KeepItTechie Content Map

This repo can support a full KeepItTechie homelab series. Each topic should connect a real lab service to a practical lesson viewers can reuse.

For the more detailed episode-by-episode plan, see [YouTube Companion Series](youtube-series.md).

## Series Structure

| Episode | Topic | Viewer Takeaway |
|---|---|---|
| 1 | Full homelab overview | How the pieces fit together without getting lost in tools |
| 2 | pfSense firewall design | Basic routing, DHCP, firewall rules, and safe exposure |
| 3 | Pi-hole DNS pair | Local DNS, redundancy, ad blocking, and service names |
| 4 | Proxmox virtualization | Why VMs make a homelab easier to test and rebuild |
| 5 | Proxmox Backup Server | Backups, retention, and restore tests that actually matter |
| 6 | Synology plus ZFS storage | Appliance NAS vs Linux storage server tradeoffs |
| 7 | NGINX reverse proxy | Clean internal URLs and service routing |
| 8 | Cloudflare Tunnel | Publishing selected services without opening everything |
| 9 | Monitoring stack | Grafana, Prometheus, logs, exporters, and uptime checks |
| 10 | Media stack | Plex, Servarr, Tautulli, and Tdarr as a real app ecosystem |
| 11 | Local AI | Running AI locally with a GPU server and Open WebUI |
| 12 | Wiki.js | Building a documentation habit for the lab |
| 13 | Glance dashboard | Creating a simple control surface for daily use |
| 14 | FinanceHQ | Local-first personal apps and privacy-minded design |
| 15 | CareerFill | Automation for job search workflows |
| 16 | AWX / Ansible | Turning repeatable admin work into automation |

## Episode Template

```text
Problem:
What pain point does this solve?

Where it fits:
What depends on it, and what does it depend on?

Build:
What are the main install or configuration steps?

Security:
What should stay private?

Demo:
What does success look like?

Failure mode:
What breaks when this service is down?

Takeaway:
What can viewers reuse in their own lab?
```

## Good Demo Angles

| Service | Demo Idea |
|---|---|
| pfSense | Show rule thinking with sanitized networks |
| Pi-hole | Add a local DNS record and resolve a service name |
| Proxmox | Clone or restore a test VM |
| PBS | Restore a VM into an isolated test network |
| Reverse proxy | Add a new internal service identity |
| Monitoring | Build a simple dashboard from node metrics |
| Loki / Promtail | Trace a service issue through logs |
| Media stack | Explain how each app has a different role |
| Local AI | Send a request to a local OpenAI-compatible endpoint |
| Wiki.js | Convert a private runbook idea into a public-safe doc |
| Glance | Build a dashboard section for core services |
| AWX | Run a safe read-only homelab check playbook |

## Public Safety For Videos

- Blur real public domains, real public IPs, tokens, and account identifiers.
- Prefer recreated examples over live admin screens.
- Avoid showing full firewall exports or full DNS record lists.
- Use `home.example.com` and `10.10.0.0/24` in slides and diagrams.
- Keep private Wiki.js admin pages out of public screen recordings.

## Repo Tie-In

Each video can point viewers to:

- The service README for the architecture.
- The sanitized inventory for naming patterns.
- The diagram notes for topology.
- The security notes for what not to publish.
- The [service matrix](service-matrix.md) for access and backup priority.
