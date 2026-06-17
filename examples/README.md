# Sanitized Configuration Examples

These examples are public-safe teaching templates for common homelab patterns. They are not production-ready drop-in configs, and they should be adapted carefully before use.

The examples use sanitized domains, generic paths, placeholder credentials, and role-based hostnames so viewers can learn the pattern without exposing private infrastructure.

## Example Index

| Example | Purpose | Related Docs | Safety Notes |
|---|---|---|---|
| [NGINX reverse proxy](nginx/README.md) | Shows an internal HTTPS reverse proxy server block | [Reverse Proxy](../services/reverse-proxy/README.md) | Replace domains, certificate paths, and upstreams privately |
| [Docker Compose](docker-compose/README.md) | Shows reusable app and dashboard compose patterns | [Glance / Homepage Dashboard](../services/glance/README.md) | Do not commit real `.env` files or live service secrets |
| [Prometheus](prometheus/README.md) | Shows sanitized scrape targets for common exporters | [Monitoring](../services/monitoring/README.md) | Keep live targets, API details, and alert destinations private |
| [Pi-hole local DNS](pihole/README.md) | Shows a safe CSV format for documenting internal records | [Pi-hole](../services/pihole/README.md) | Review real DNS records before publishing |
| [Cloudflare Tunnel](cloudflare-tunnel/README.md) | Shows tunnel config shape without credentials | [Cloudflare Tunnel](../services/cloudflare-tunnel/README.md) | Never commit tunnel IDs, credentials, or real public hostnames |
| [Environment file](env/README.md) | Shows how to publish placeholders safely | [Pre-Publish Review](../docs/pre-publish-review.md) | Commit `.env.example`, never real `.env` files |

## Before Using These Examples

- Replace `home.example.com` with the private domain only in private config.
- Replace placeholder credentials such as `CHANGE_ME` outside the public repo.
- Keep real secrets, keys, certs, tunnel credentials, and private exports out of Git.
- Run the [pre-publish review checklist](../docs/pre-publish-review.md) before sharing changes.
