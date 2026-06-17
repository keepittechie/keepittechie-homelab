# Diagrams

Store public-safe diagrams here. Diagrams should teach the architecture without exposing live DNS zones, public IPs, raw firewall rules, or private credentials.

## Recommended Files

| File | Purpose |
|---|---|
| `network-overview.drawio` | Internet, pfSense, LAN, Proxmox, storage, and clients |
| `dns-flow.drawio` | Client to Pi-hole to upstream resolver flow |
| `reverse-proxy-flow.drawio` | Service alias to reverse proxy to backend |
| `backup-flow.drawio` | Proxmox to PBS plus app-aware backup notes |
| `monitoring-flow.drawio` | Exporters to Prometheus/Loki to Grafana |
| `local-ai-stack.drawio` | Open WebUI to local AI endpoint to GPU server |

Export PNG or SVG versions only after reviewing them for private information.

## Simple Network Placeholder

```text
Internet
  |
Cloudflare Tunnel for selected public services
  |
pfSense firewall
  |
10.10.0.0/24 lab LAN
  |
  +-- Proxmox host
  |   +-- pihole1.home.example.com
  |   +-- pihole2.home.example.com
  |   +-- proxy.home.example.com
  |   +-- grafana.home.example.com
  |   +-- wiki.home.example.com
  |   +-- ai.home.example.com
  |
  +-- nas.home.example.com
  +-- zfs.home.example.com
  +-- pbs.home.example.com
```

## Reverse Proxy Placeholder

```text
grafana.home.example.com
wiki.home.example.com
nextcloud.home.example.com
        |
        v
proxy.home.example.com
        |
        +-- monitoring app backend
        +-- documentation app backend
        +-- file sync app backend
```

## Backup Placeholder

```text
Proxmox guests
  |
  +-- scheduled VM backups -> pbs.home.example.com
  |
  +-- app database dumps -> private backup target
  |
  +-- config in Git where public-safe
```

## Diagram Safety Checklist

- Use `home.example.com`, not the live private domain.
- Use `10.10.0.0/24` examples, not full private exports.
- Remove public IPs, account IDs, tokens, and QR codes.
- Crop screenshots so they do not show private bookmarks or admin details.
- Prefer role labels when exact host details do not help the viewer.
