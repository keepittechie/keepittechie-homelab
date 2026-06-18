# Docker Compose Examples

These examples demonstrate safe patterns for documenting self-hosted app layouts without publishing production compose files.

## Included Examples

| File | Demonstrates |
|---|---|
| [dashboard-compose.yml](dashboard-compose.yml) | A simple dashboard-style service with a named volume and internal network |
| [app-template.yml](app-template.yml) | A generic app plus database pattern using `.env` placeholders |

## What Must Be Changed Before Use

- Replace example images with real images in private config.
- Replace service names, volumes, ports, and environment values privately.
- Create a real `.env` file outside the public repo.
- Review app documentation before exposing any ports.

## What Should Never Be Committed

- Real `.env` files.
- App secrets, database credentials, API keys, or tokens.
- Private app URLs.
- Raw app exports or database dumps.

## What Readers Can Learn

Readers can learn the difference between public-safe templates and real runtime config. This connects to the [Glance / Homepage Dashboard service doc](../../services/glance/README.md), the [Apps and AI guide](../../docs/apps-and-ai.md), and the [environment example](../env/README.md).

These are sanitized examples, not production-ready drop-in configs.
