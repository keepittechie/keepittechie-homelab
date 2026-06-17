# Pi-hole

## Purpose

Pi-hole provides DNS filtering, local DNS records, and visibility into what devices are resolving on the network. The lab uses a primary and secondary Pi-hole so DNS remains available during maintenance or failure of one resolver.

## Why This Matters

DNS is one of the first services viewers should understand in a homelab. Clean DNS lets users reach `grafana.home.example.com` instead of memorizing IP addresses, and DNS filtering gives useful visibility into client behavior.

Pi-hole also makes it easier to teach the difference between:

- A machine hostname.
- A service alias.
- A DNS resolver.
- An upstream DNS provider.

## Where It Fits in the Homelab

```text
Client devices
  |
pfSense DHCP hands out DNS
  |
Pi-hole primary and secondary
  |
Upstream DNS or firewall-forwarded DNS
```

Pi-hole is not the firewall. It answers DNS questions and filters domains. pfSense still controls routing and firewall policy.

## Host / Runtime

| Field | Value |
|---|---|
| Primary example host | `pontus` |
| Secondary example host | `priapus` |
| Runtime | Proxmox VMs |
| Example DNS | `pihole1.home.example.com`, `pihole2.home.example.com` |
| Public access | No |

## Network / DNS

Clients should receive both Pi-hole resolvers through DHCP:

```text
DNS server 1: pihole1.home.example.com
DNS server 2: pihole2.home.example.com
```

This prevents devices from bypassing the local DNS path. If a device is allowed to use random public DNS, local service names may fail and filtering visibility becomes incomplete.

## Key Responsibilities

- Resolve internal service names.
- Filter unwanted or known-bad domains.
- Provide query visibility.
- Support primary and secondary DNS availability.
- Help keep service access readable through local aliases.
- Document local DNS intent in sanitized form.

## Example Public-Safe Configuration

Sanitized local DNS examples:

| DNS Name | Points To | Purpose | Public Notes |
|---|---|---|---|
| `pihole1.home.example.com` | Primary DNS VM | Main resolver | Safe example only |
| `pihole2.home.example.com` | Secondary DNS VM | Backup resolver | Safe example only |
| `proxy.home.example.com` | Reverse proxy | Internal HTTPS routing | Do not publish live records |
| `grafana.home.example.com` | Reverse proxy | Monitoring dashboard | Keep dashboard private |
| `proxmox.home.example.com` | Proxmox host | Hypervisor UI | VPN or trusted LAN only |
| `pbs.home.example.com` | Backup server | VM backup target | Private infrastructure |

Example DHCP DNS handoff:

```text
pfSense DHCP options
  -> primary DNS: pihole1.home.example.com
  -> secondary DNS: pihole2.home.example.com
```

## Backup and Restore Notes

- Export Pi-hole settings after changing blocklists, allowlists, or local records.
- Keep real exports private.
- Document important local DNS names in sanitized form.
- Restore both resolvers from the intended baseline.
- Verify that DHCP still hands out both resolvers after restore.

## Security Notes

- Do not expose Pi-hole admin pages publicly.
- Keep admin authentication enabled.
- Do not publish the full live local DNS zone.
- Keep dashboard API keys and widget credentials out of Git.
- Review screenshots for private domains and client names.

## Common Mistakes to Avoid

- Giving clients only one DNS resolver.
- Letting clients bypass Pi-hole with public DNS.
- Putting every service directly on an IP instead of using aliases.
- Publishing a raw local DNS export.
- Forgetting that DNS failure can make working services look broken.

## What Viewers Can Learn

- Why local DNS is a quality-of-life upgrade.
- Why primary and secondary DNS matter.
- How DNS aliases make reverse proxying easier.
- How to document DNS publicly without leaking the real zone.

## Related Sanitized Examples

- [Pi-hole local DNS CSV](../../examples/pihole/local-dns-records.example.csv)
- [Pi-hole example notes](../../examples/pihole/README.md)
- [DNS flow diagram](../../diagrams/dns-flow.md)

## Future Improvements

- Add a sanitized Pi-hole restore walkthrough.
- Add a primary/secondary sync note if a sync tool is used.
- Add a DNS troubleshooting checklist.
