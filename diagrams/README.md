# Diagrams

This folder contains public-safe Mermaid diagrams for the KeepItTechie homelab. The diagrams explain architecture patterns without exposing live DNS zones, exact host addresses, public IP addresses, private credentials, screenshots, or raw config exports.

If this is the first stop, start with the homelab overview, then open the diagram for the topic you are studying: DNS, backups, reverse proxying, local AI, or monitoring.

## Diagram Index

| Diagram | Purpose | Best Starting Point For | File |
|---|---|---|---|
| Homelab Overview | Shows the full high-level lab flow from internet access to apps, storage, monitoring, and local AI | Viewers who want the big picture first | [homelab-overview.md](homelab-overview.md) |
| DNS Flow | Shows how clients use pfSense DHCP, Pi-hole, local records, blocking, and upstream DNS | Viewers learning internal DNS and service names | [dns-flow.md](dns-flow.md) |
| Backup Flow | Shows VM backups, app data, NAS targets, ZFS snapshots, and restore verification | Viewers learning backup design and restore proof | [backup-flow.md](backup-flow.md) |
| Reverse Proxy Flow | Shows internal HTTPS routing and selected public access through a tunnel | Viewers learning service identities, TLS, and public/private boundaries | [reverse-proxy-flow.md](reverse-proxy-flow.md) |
| Local AI Flow | Shows Open WebUI, a local OpenAI-compatible endpoint, llama.cpp, model storage, and GPU runtime | Viewers learning local-first AI on Linux | [local-ai-flow.md](local-ai-flow.md) |
| Monitoring Flow | Shows exporters, Prometheus, Loki, Grafana, generic alerts, and the review loop | Viewers learning observability basics | [monitoring-flow.md](monitoring-flow.md) |

## Public-Safe Diagram Rules

- Use `home.example.com`, not a live private domain.
- Use `10.10.0.0/24` for network examples, not exact host addresses.
- Use role labels when exact host details do not help viewers learn the design.
- Do not add screenshots, raw exports, private certificate paths, tunnel identifiers, usernames, email addresses, or credential material.
- Review diagrams before publishing to confirm they show architecture, not private infrastructure details.
