# Cloudflare Tunnel

## Purpose

Cloudflare Tunnel provides selected public access to approved services without opening broad inbound ports on the firewall. In this homelab, it is used as a controlled publishing path, not as a shortcut to expose admin tools.

## Why This Matters

Most homelab services should remain private. A tunnel can make a service reachable from the internet, but that does not automatically make the service safe to publish.

This is a useful place to teach the difference between:

- Internal access.
- VPN access.
- Public access.
- Public access with additional authentication and policy.

## Where It Fits in the Homelab

```text
Public user
  |
Cloudflare edge
  |
Tunnel connector
  |
Reverse proxy or approved backend
```

The tunnel should point to selected services only. The default for admin tools should be private access.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Tunnel connector on a Linux host or app VM |
| Typical pairing | Reverse proxy |
| Example internal DNS | `proxy.home.example.com` |
| Public access | Selected services only |
| Credentials | Stored privately outside Git |

## Network / DNS

Public hostnames belong in private tunnel configuration, not in this public repo unless they are intentionally shared branding. Internal docs should use examples like:

```text
public.example.com -> tunnel -> proxy.home.example.com -> approved service
```

Private services should continue using `home.example.com` examples.

## Key Responsibilities

- Provide outbound tunnel connectivity for selected public services.
- Avoid broad inbound firewall exposure.
- Keep public service decisions documented.
- Support access policy and authentication where appropriate.
- Keep tunnel credentials private.

## Example Public-Safe Configuration

Sanitized service exposure table:

| Service | Public? | Access Control | Notes |
|---|---|---|---|
| Public docs site | Yes, if intended | App auth or public read-only content | Review pages before publishing |
| Wiki.js public namespace | Limited | Namespace permissions | Private admin pages stay private |
| Nextcloud | Limited | Strong user auth and hardening | Review carefully before publishing |
| Grafana | No by default | VPN or trusted LAN | Dashboards can leak infrastructure |
| Proxmox | No | VPN only | Hypervisor admin interface |
| pfSense | No | VPN only | Firewall admin interface |
| FinanceHQ | No | Private LAN | Sensitive personal data |
| CareerFill | No | Private LAN | Sensitive career data |

## Backup and Restore Notes

- Keep tunnel configuration in a private backup location.
- Document public service intent in sanitized form.
- Keep recovery notes for recreating routes in private runbooks.
- Do not commit connector credentials or generated config files.

## Security Notes

- Never commit tunnel credentials.
- Do not publish admin tools through the tunnel.
- Require strong authentication for user-specific apps.
- Review public routes after app upgrades.
- Treat the tunnel as internet exposure, not just convenience.

## Common Mistakes to Avoid

- Publishing dashboards because they are useful internally.
- Assuming a tunnel replaces app authentication.
- Forgetting to remove stale public routes.
- Copying tunnel config into a public repo.
- Exposing services that were designed only for trusted LAN access.

## What Viewers Can Learn

- How selected public access can work without broad inbound port forwards.
- Why exposure decisions should be documented.
- Why public access needs both routing and authentication thinking.
- How to explain tunnel architecture without leaking credentials.

## Related Sanitized Examples

- [Cloudflare Tunnel config shape](../../examples/cloudflare-tunnel/config.example.yml)
- [Cloudflare Tunnel example notes](../../examples/cloudflare-tunnel/README.md)
- [Reverse proxy flow diagram](../../diagrams/reverse-proxy-flow.md)

## Future Improvements

- Add a public-service review checklist.
- Add a sanitized tunnel traffic diagram.
- Add example private-only and public-approved route categories.
