# Network Design

The network is built around pfSense, internal DNS, readable service names, and conservative exposure. The public examples in this repo use `10.10.0.0/24` and `home.example.com`.

For visual references, see the [DNS flow diagram](../diagrams/dns-flow.md), [reverse proxy flow diagram](../diagrams/reverse-proxy-flow.md), and [Homelab DNS and Pi-hole guide](guides/dns-pihole.md). For terms such as LAN, VLAN, DNS, DHCP, service identity, and machine identity, use the [Glossary](glossary.md).

## Core Flow

```text
Client device
  |
Pi-hole DNS
  |
pfSense firewall
  |
Internal service or internet
```

For internal web apps, DNS points users at the reverse proxy:

```text
grafana.home.example.com
  |
NGINX reverse proxy
  |
Grafana container or VM backend
```

## DNS Strategy

| Record Type | Example | Purpose |
|---|---|---|
| Machine identity | `pontus.home.example.com` | Names the VM or physical host |
| Service identity | `pihole1.home.example.com` | Names the service role |
| Reverse proxy identity | `grafana.home.example.com` | Gives users a clean service URL |
| Storage identity | `nas.home.example.com` | Keeps storage access readable |

Pi-hole handles DNS filtering and local records. pfSense remains the network policy point and can hand out DNS settings through DHCP.

## Example Internal Records

```text
10.10.0.x    firewall.home.example.com
10.10.0.x    pihole1.home.example.com pontus.home.example.com
10.10.0.x    pihole2.home.example.com priapus.home.example.com
10.10.0.x    proxy.home.example.com zelus.home.example.com
10.10.0.x    proxmox.home.example.com
10.10.0.x    plex.home.example.com apollo.home.example.com
10.10.0.x    grafana.home.example.com wiki.home.example.com apps.home.example.com
10.10.0.x    ai.home.example.com hephaestus.home.example.com
```

These are sanitized examples, not a live zone file.

## Segmentation Model

| Network | Purpose | Default Trust |
|---|---|---|
| LAN / Admin | Admin workstations and trusted servers | Highest |
| Server / Lab | Proxmox VMs and services | High, but controlled |
| Media | Media services and storage clients | Limited to required paths |
| IoT | Smart devices and low-trust hardware | Restricted |
| Guest | Visitor devices | Internet-only |
| VPN | Remote admin access | Treated like admin, with strong auth |

The lab can run with a simple LAN, but documenting the segmentation model helps viewers understand how to grow safely.

## Firewall Principles

- Start with least privilege between network segments.
- Keep admin interfaces off the public internet.
- Allow DNS to Pi-hole and internet egress only where needed.
- Allow reverse proxy traffic to approved backend services.
- Use VPN or trusted LAN access for pfSense, Proxmox, PBS, NAS, AWX, and monitoring.
- Review public services separately from private services.

## Public Access Pattern

Cloudflare Tunnel is used for selected public services only. The important teaching point is that public access is a deliberate exception, not the default.

| Service Type | Public Access Guidance |
|---|---|
| Admin tools | Do not publish |
| Monitoring | Keep private |
| Automation | Keep private |
| Personal finance / career apps | Keep private |
| Public docs or portfolio content | Publish only intentionally |
| Media services | Limit exposure and use strong authentication |

## Troubleshooting Checklist

1. Confirm the client is using Pi-hole for DNS.
2. Confirm the local DNS record resolves to the expected private address.
3. Confirm pfSense allows the path between client and service.
4. Confirm the reverse proxy can reach the backend.
5. Confirm the service itself is listening.
6. Check logs in the app, proxy, and monitoring stack.

## Public Repo Boundary

Do not commit raw firewall exports, switch backups, full DNS zone files, VPN configs, public IPs, or screenshots that reveal sensitive records.
