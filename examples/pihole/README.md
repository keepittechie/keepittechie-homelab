# Pi-hole Local DNS Example

This example demonstrates a simple CSV format for documenting local DNS records in a public-safe way.

The included CSV uses intentionally fake host addresses and sanitized names:

- `home.example.com`
- `proxy.home.example.com`
- `grafana.home.example.com`
- `nas.home.example.com`

## What Must Be Changed Before Use

- Replace records with real values only in private documentation or private config.
- Confirm each record has a clear purpose.
- Keep service aliases separate from machine identity where useful.

## What Should Never Be Committed

- Full live DNS exports.
- Client names that identify people or devices.
- Private domains.
- Exact production host addresses.
- Pi-hole API keys or admin credentials.

## What Viewers Can Learn

Viewers can learn how internal DNS records make homelab services easier to remember and troubleshoot. This connects to the [Pi-hole service doc](../../services/pihole/README.md), the [network guide](../../docs/network.md), and the [DNS flow diagram](../../diagrams/dns-flow.md).

This is a sanitized example, not a production-ready drop-in config.
