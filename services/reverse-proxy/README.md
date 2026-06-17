# Reverse Proxy

## Purpose

The reverse proxy provides clean HTTPS names for internal services and routes browser traffic to the correct backend. It keeps users from memorizing ports and lets service URLs stay consistent even if the backend moves.

## Where It Fits

```text
Client
  |
service.home.example.com
  |
NGINX reverse proxy
  |
backend VM or container
```

The proxy is the front door for many internal web apps. It is not a reason to publish every service to the internet.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `zelus` |
| Runtime | NGINX on Linux |
| Example DNS | `proxy.home.example.com` |
| Public access | Limited, only for approved services |
| Primary inputs | Pi-hole DNS records and backend service definitions |

## Key Dependencies

- Pi-hole local DNS
- pfSense firewall policy
- TLS certificate workflow
- Backend services
- Cloudflare Tunnel for selected public routes

## Network / DNS

Example service aliases:

```text
wiki.home.example.com     -> proxy.home.example.com
grafana.home.example.com  -> proxy.home.example.com
plex.home.example.com     -> proxy.home.example.com
ai.home.example.com       -> proxy.home.example.com
```

The proxy then routes each hostname to the correct private backend.

## Backup Notes

- Keep NGINX site configs backed up privately.
- Document sanitized routing patterns in this repo.
- Back up TLS automation metadata privately.
- Keep rollback notes for config changes.

## Security Notes

- Do not proxy admin tools publicly by default.
- Test config before reloading.
- Keep private upstream addresses out of public examples unless sanitized.
- Add authentication or network restrictions where appropriate.

## What Viewers Can Learn

- Why reverse proxies are useful in homelabs.
- How DNS names map to backend services.
- How internal HTTPS can make services easier to use.
- Why clean URLs do not replace access control.

## Future Improvements

- Add a sanitized NGINX server block example.
- Add an internal-only versus public route table.
- Add a proxy troubleshooting checklist.
