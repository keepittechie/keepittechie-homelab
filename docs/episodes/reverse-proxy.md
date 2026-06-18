# Homelab Reverse Proxy and Internal HTTPS

This page is a public-safe companion guide for a KeepItTechie video about reverse proxies, internal HTTPS, and carefully selected public access.

## Episode Goal

This episode teaches how a reverse proxy gives clean service URLs, how internal HTTPS improves the homelab experience, and why public access should be limited to selected services.

The goal is to make the web side of the lab easier to use without turning every internal dashboard into an internet-facing service.

## What Viewers Will Learn

- What a reverse proxy does.
- Why friendly service names help.
- How DNS and reverse proxy routing work together.
- What internal HTTPS means.
- Why Cloudflare Tunnel should be used selectively.
- Why admin dashboards should usually stay private.
- What not to publish in a public repo.

## Why a Reverse Proxy Matters

A reverse proxy gives one clean entry point for multiple web services. Instead of remembering ports and backend hosts, viewers can use names such as `wiki.home.example.com`, `grafana.home.example.com`, or `app.home.example.com`.

This helps with:

- Cleaner URLs.
- Easier TLS management.
- Fewer ports to remember.
- More stable service identities.
- Simpler documentation.
- A cleaner day-to-day homelab experience.

The important boundary is this: a reverse proxy makes services easier to reach, but it does not automatically make them safe to publish.

## Internal HTTPS

HTTPS can be useful inside the lab too. It gives browsers a cleaner experience, helps apps behave more like they would in production-style environments, and teaches TLS concepts safely.

Internal HTTPS often involves local certificates or an internal certificate authority. The high-level idea is:

- The browser requests `https://wiki.home.example.com`.
- The reverse proxy presents a certificate.
- The browser decides whether that certificate is trusted.
- The proxy forwards traffic to the backend app.

Private certificate files, certificate authority keys, and exact certificate paths should never be committed to this repo.

## Service Names and DNS

DNS and the reverse proxy work together.

Internal DNS points a service name at the reverse proxy. The proxy then decides which backend app should receive the request.

Example:

```text
wiki.home.example.com
  -> internal DNS points to reverse proxy
  -> reverse proxy receives HTTPS request
  -> proxy forwards traffic to the wiki backend
```

This separates service identity from backend host identity. The service name is what viewers or users type. The backend host is where the app happens to run.

## Private Access vs Public Access

Reverse proxying is not the same thing as public exposure.

Useful access categories:

- Internal-only services stay on the trusted LAN.
- VPN-only or admin services require private access.
- Selected public services are intentionally exposed.
- Public tunnel access should have a clear reason and protection plan.

Admin interfaces such as firewall, hypervisor, backup, monitoring, and automation dashboards should usually stay private.

## Where Cloudflare Tunnel Fits

Cloudflare Tunnel can publish selected services without opening broad inbound firewall ports. That is useful, but it still creates internet exposure.

A tunnel should answer a few questions before anything is published:

- Is this service meant for public visitors?
- Is authentication strong enough?
- Does the app leak private information?
- Is the public route documented?
- Can the service be disabled quickly if needed?

Tunnel credentials, connector config from the live lab, and access policy details that reveal private infrastructure should stay out of public docs.

## Public-Safe Demo Ideas

- Show the [reverse proxy flow diagram](../../diagrams/reverse-proxy-flow.md).
- Walk through the [sanitized NGINX example](../../examples/nginx/reverse-proxy-site.conf).
- Walk through the [sanitized Cloudflare Tunnel example](../../examples/cloudflare-tunnel/config.example.yml).
- Explain a service exposure decision table.
- Show what should not be published.
- Avoid live dashboards unless they are sanitized or recreated with demo data.

## Example Reverse Proxy Flow

| Step | Component | What Happens |
|---|---|---|
| 1 | Client | Opens `https://wiki.home.example.com` |
| 2 | Internal DNS | Resolves the service name to the reverse proxy |
| 3 | Reverse Proxy | Receives the HTTPS request |
| 4 | TLS Layer | Presents an internal certificate |
| 5 | Backend App | Proxy forwards traffic to the wiki service |

## Example Exposure Decision Table

| Service Type | Example | Access Recommendation | Why |
|---|---|---|---|
| Firewall UI | pfSense | Private / VPN only | Edge admin panels should not be public |
| Proxmox UI | Proxmox | Private / VPN only | VM control plane should stay protected |
| Dashboard | Homelab dashboard | Private or VPN only | Often exposes internal links |
| Public website | Blog or docs site | Public via tunnel/proxy if hardened | Designed for public visitors |
| Personal finance app | FinanceHQ-style app | Private only | Sensitive personal data |

## Common Mistakes

- Exposing every service publicly.
- Publishing real NGINX configs with hostnames.
- Committing certificate files.
- Committing Cloudflare tunnel credentials.
- Skipping authentication.
- Pointing DNS at the wrong place.
- Forgetting WebSocket headers for apps that need them.
- Assuming HTTPS means the app is safe to expose.
- Exposing admin dashboards.

## What Is Intentionally Not Shown

- Live NGINX configs.
- Real internal domains.
- Exact backend IPs.
- Private certificate paths.
- Private certificates.
- Cloudflare tunnel IDs.
- Tunnel credentials.
- Access policy details if sensitive.
- Firewall rules.
- Live dashboard screenshots.

## Commands and Examples

These commands use sanitized example names. Review command output before sharing it publicly because it can include redirects, headers, service names, backend hints, or certificate details.

```bash
# Test an internal HTTPS route with a sanitized name
curl -I https://wiki.home.example.com

# Check DNS resolution for a service name
dig wiki.home.example.com

# Review the repo's public-safe NGINX example
cat examples/nginx/reverse-proxy-site.conf
```

## After Watching

- Read the [Reverse Proxy](../../services/reverse-proxy/README.md) service doc.
- Study the [reverse proxy flow diagram](../../diagrams/reverse-proxy-flow.md).
- Review the [sanitized NGINX example](../../examples/nginx/README.md).
- Review the [sanitized Cloudflare Tunnel example](../../examples/cloudflare-tunnel/README.md).
- Decide which services should stay private.
- Avoid exposing admin interfaces.

## Related Docs

- [Core Infrastructure](../core-infrastructure.md)
- [Network Design](../network.md)
- [Current Setup](../current-setup.md)
- [Reverse Proxy](../../services/reverse-proxy/README.md)
- [Cloudflare Tunnel](../../services/cloudflare-tunnel/README.md)
- [Reverse Proxy Flow Diagram](../../diagrams/reverse-proxy-flow.md)
- [NGINX Example](../../examples/nginx/README.md)
- [Cloudflare Tunnel Example](../../examples/cloudflare-tunnel/README.md)
- [Screenshot Policy](../screenshots-policy.md)
- [Pre-Publish Review](../pre-publish-review.md)
- [Glossary](../glossary.md)
