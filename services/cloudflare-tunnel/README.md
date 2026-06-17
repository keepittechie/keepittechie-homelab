# Cloudflare Tunnel

## Purpose

Cloudflare Tunnel provides controlled public access for selected services without opening broad inbound firewall rules. In this lab, it is treated as an exception path for approved public services, not a default path for admin tools.

## Where It Fits

```text
Public user
  |
Cloudflare
  |
Tunnel connector in the homelab
  |
Reverse proxy or approved backend
```

The tunnel should point only to services that have been intentionally reviewed for public access.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Tunnel connector on a Linux host or app VM |
| Typical pairing | Reverse proxy |
| Example internal DNS | `proxy.home.example.com` |
| Public access | Selected services only |
| Admin access | Private dashboard and private credentials |

## Key Dependencies

- Cloudflare account and DNS zone
- Reverse proxy routes
- Service authentication
- pfSense egress access
- Private tunnel credentials stored outside Git

## Network / DNS

Public hostnames should map to intentionally published services. Internal-only services should continue to use `home.example.com` and stay private.

Example public-safe policy:

| Service Type | Tunnel? |
|---|---|
| Public docs | Maybe |
| Portfolio or channel site | Maybe |
| pfSense | No |
| Proxmox | No |
| Pi-hole admin | No |
| Grafana | Usually no |
| FinanceHQ / CareerFill | No |

## Backup Notes

- Store tunnel configuration and credentials privately.
- Keep a sanitized list of published service categories in this repo.
- Document why each public service is exposed.
- Keep recovery notes for recreating the tunnel in a private runbook.

## Security Notes

- Never commit tunnel credentials.
- Do not publish admin interfaces through the tunnel.
- Put strong authentication in front of anything user-specific.
- Review public services after major app upgrades.

## What Viewers Can Learn

- How to publish a service without opening a general inbound port.
- Why public access should be deliberate and documented.
- How tunnels, DNS, reverse proxies, and authentication fit together.
- Why "reachable from the internet" is a security decision, not a convenience setting.

## Future Improvements

- Add a sanitized public-service decision checklist.
- Add a diagram showing tunnel traffic flow.
- Document an example private-only service that should not be tunneled.
