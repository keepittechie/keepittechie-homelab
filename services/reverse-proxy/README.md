# Reverse Proxy

## Purpose

The reverse proxy provides clean internal HTTPS routing for homelab services. Instead of accessing services by ports or backend hosts, users can open names like `grafana.home.example.com` or `proxy.home.example.com`.

## Why This Matters

A reverse proxy makes a self-hosted lab easier to use and easier to explain. It separates the service name viewers type from the backend machine or container that runs the app.

It also creates an important teaching boundary: internal HTTPS routing is not the same as public exposure.

## Where It Fits in the Homelab

```text
Browser
  |
service.home.example.com
  |
NGINX reverse proxy
  |
private backend app
```

Pi-hole points service aliases at the proxy. The proxy then routes traffic to the correct backend.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `zelus` |
| Runtime | NGINX on Linux |
| Example DNS | `proxy.home.example.com` |
| Public access | Limited, only for approved services |
| Primary inputs | DNS records, TLS certificates, upstream definitions |

## Network / DNS

Example internal aliases:

```text
grafana.home.example.com  -> proxy.home.example.com
pihole1.home.example.com  -> private DNS host
proxmox.home.example.com  -> private hypervisor host
pbs.home.example.com      -> private backup server
```

The reverse proxy usually handles web apps, not every protocol in the lab.

## Key Responsibilities

- Route service hostnames to private backend apps.
- Provide internal HTTPS.
- Keep user-facing service names stable.
- Separate private-only routes from public routes.
- Support controlled tunnel publishing for selected services.
- Make internal app URLs easier to teach and remember.

## Example Public-Safe Configuration

Sanitized NGINX server block example:

```nginx
server {
    listen 443 ssl;
    server_name app.home.example.com;

    ssl_certificate /path/to/internal/fullchain.pem;
    ssl_certificate_key /path/to/internal/privkey.pem;

    location / {
        proxy_pass http://app-backend.home.example.com:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto https;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

This is a placeholder. Do not copy live certificate paths, real backend names, or production routes into public docs.

## Backup and Restore Notes

- Back up NGINX site configs privately.
- Document public-safe route intent in this repo.
- Keep certificate material private.
- Test config before reloads.
- Keep rollback notes for proxy changes.

## Security Notes

- Do not expose every dashboard just because it has a proxy entry.
- Keep Proxmox, PBS, pfSense, Pi-hole admin, and monitoring private unless there is a specific hardened access plan.
- Do not publish certificate files or private CA material.
- Be careful with proxy screenshots because they can reveal internal hostnames.

## Common Mistakes to Avoid

- Treating reverse proxy access as authentication.
- Publishing admin dashboards through a tunnel by default.
- Mixing internal-only and public routes without clear labels.
- Reloading NGINX without testing configuration.
- Committing real certificate paths or app hostnames.

## What Viewers Can Learn

- How internal HTTPS improves homelab usability.
- How DNS aliases and upstream routing work together.
- Why private reverse proxy access is different from public access.
- How to document routes safely.

## Related Sanitized Examples

- [NGINX reverse proxy server block](../../examples/nginx/reverse-proxy-site.conf)
- [NGINX example notes](../../examples/nginx/README.md)
- [Reverse proxy flow diagram](../../diagrams/reverse-proxy-flow.md)

## Future Improvements

- Add a sanitized route inventory.
- Add a proxy troubleshooting checklist.
- Add a local CA overview without certificate material.
