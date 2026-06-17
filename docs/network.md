# Network Design

## DNS Strategy

Internal DNS is built around readable service names.

Example:

```text
pihole1.home.example.com
pihole2.home.example.com
proxy.home.example.com
wiki.home.example.com
monitoring.home.example.com
```

## DNS Roles

| Name | Purpose |
|---|---|
| Pi-hole Primary | Main DNS resolver and blocker |
| Pi-hole Secondary | Backup DNS resolver |
| pfSense | Firewall, DHCP, VLAN routing |
| Reverse Proxy | Internal HTTPS routing |

## VLAN / Network Segmentation Ideas

| Network | Purpose |
|---|---|
| LAN | Trusted servers and admin workstations |
| Wi-Fi | Personal devices |
| IoT | Smart devices / less trusted devices |
| Guest | Internet-only devices |
| Lab | Test systems |

## Firewall Principles

- Default deny between VLANs.
- Allow only required ports.
- Keep DNS pinned to Pi-hole.
- Use VPN for private admin access.
- Avoid exposing admin panels directly to the internet.

## Public Repo Note

Do not publish complete firewall exports unless they are reviewed and sanitized.
