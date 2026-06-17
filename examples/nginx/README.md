# NGINX Reverse Proxy Example

This example demonstrates a sanitized NGINX server block for internal HTTPS routing.

It includes:

- HTTP to HTTPS redirect.
- TLS certificate placeholders.
- Reverse proxying to an internal app.
- Common proxy headers.
- WebSocket upgrade headers.

## What Must Be Changed Before Use

- Replace `app.home.example.com` with a private service name in private config.
- Replace `/etc/local-ca/example/...` with private certificate paths.
- Replace `http://app.internal.example:8080` with the real upstream in private config.
- Review TLS settings before using this pattern for real services.

## What Should Never Be Committed

- Real certificate keys.
- Private CA material.
- Real upstream hostnames if they expose private infrastructure.
- Production NGINX exports with secrets or account-specific values.

## What Viewers Can Learn

This shows how DNS aliases, TLS, and upstream routing work together. It connects to the [Reverse Proxy service doc](../../services/reverse-proxy/README.md) and the [reverse proxy flow diagram](../../diagrams/reverse-proxy-flow.md).

This is a sanitized example, not a production-ready drop-in config.
