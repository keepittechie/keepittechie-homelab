# Cloudflare Tunnel Example

This example demonstrates the shape of a Cloudflare Tunnel config without including real tunnel credentials or real public hostnames.

## What Must Be Changed Before Use

- Replace `EXAMPLE_TUNNEL_NAME` in private config.
- Replace the credentials file path privately.
- Replace demo hostnames with approved public routes in private config.
- Add access policies and app authentication where appropriate.

## What Should Never Be Committed

- Tunnel IDs.
- Credentials files.
- Real public hostnames unless they are intentionally public branding.
- Generated Cloudflare config with account-specific values.
- Any token or connector secret.

## What Readers Can Learn

Readers can learn how tunnel ingress rules map public hostnames to private services while keeping broad inbound firewall ports closed. This connects to the [Cloudflare Tunnel service doc](../../services/cloudflare-tunnel/README.md) and the [reverse proxy flow diagram](../../diagrams/reverse-proxy-flow.md).

This is a sanitized example, not a production-ready drop-in config.
