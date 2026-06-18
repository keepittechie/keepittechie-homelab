# Apps and AI

This page is the beginner-friendly entry point for the application, media, dashboard, documentation, local AI, and automation services in the KeepItTechie homelab.

These services sit on top of the core infrastructure, storage, backups, monitoring, and reverse proxy layers. They are the part readers are most likely to recognize from daily use, but they also carry the most private data.

For a visual reference, see the [local AI flow diagram](../diagrams/local-ai-flow.md). For the guide, see [Local AI on Linux](guides/local-ai.md). For unfamiliar app, endpoint, and public-safe documentation terms, use the [Glossary](glossary.md).

## Recommended Reading Order

| Step | Topic | Link | Why Start Here |
|---|---|---|---|
| 1 | Local AI | [Local AI Stack](../services/local-ai/README.md), [Local AI Guide](guides/local-ai.md) | Learn the GPU, endpoint, model, and Open WebUI pattern |
| 2 | Dashboard | [Glance / Homepage Dashboard](../services/glance/README.md) | See how services are grouped for daily use |
| 3 | Documentation | [Wiki.js](../services/wiki/README.md) | Learn public/private documentation boundaries |
| 4 | Media | [Media Stack](../services/media-stack/README.md) | Understand storage-heavy multi-app workflows |
| 5 | Private cloud | [Nextcloud](../services/nextcloud/README.md) | Learn file sync, app data, and restore planning |
| 6 | Personal apps | [FinanceHQ](../services/financehq/README.md), [CareerFill](../services/careerfill/README.md) | See local-first private app patterns |
| 7 | Automation | [AWX / Ansible](../services/automation-awx/README.md) | Learn how repeatable admin workflows are organized |

## Stack Summary

| Area | Service | Public-Safe Example | Main Lesson |
|---|---|---|---|
| Local AI | llama.cpp-compatible endpoint and Open WebUI | `ai.home.example.com` | Local AI should stay private and observable |
| Media | Plex, Servarr-style apps, Tautulli, Tdarr | `media.home.example.com` | App config and media files need different backup plans |
| Documentation | Wiki.js | `wiki.home.example.com` | Public docs and private runbooks need boundaries |
| Private cloud | Nextcloud | `nextcloud.home.example.com` | File sync apps need app-aware backups |
| Dashboard | Glance or Homepage | `dashboard.home.example.com` | Dashboards help operations but can leak links |
| Personal apps | FinanceHQ and CareerFill | Private app aliases only | Architecture can be public; data must stay private |
| Automation | AWX / Ansible | `awx.home.example.com` | Automation needs safe inventory and credential boundaries |

## Good Learning Projects

| Project | Why It Helps Readers | Public-Safe Demo |
|---|---|---|
| Build a dashboard group | Teaches service organization | Use fake `home.example.com` links |
| Add a Wiki.js public/private namespace model | Teaches documentation hygiene | Use sample namespaces |
| Run a local AI request | Teaches local endpoint patterns | Use placeholder API URL |
| Map media app dependencies | Teaches storage and app data separation | Use generic paths |
| Create a read-only AWX job idea | Teaches safe automation | Use fake inventory groups |
| Document a private app backup plan | Teaches data boundaries | Use fake FinanceHQ or CareerFill data |

## Public-Safe Documentation Boundary

Document:

- Architecture and service roles.
- Generic paths such as `/opt/apps/example` and `/mnt/storage/appdata`.
- Fake demo data.
- Public-safe screenshots or recreated examples.
- Backup and restore categories.

Do not document:

- Real app config exports.
- Financial data.
- Job applications, recruiter messages, or resume details.
- Real API credentials.
- Private database paths.
- Live internal-only URLs.
- Real local AI prompts that include private context.

## Related Docs

- [Core Infrastructure](core-infrastructure.md)
- [Storage and Monitoring](storage-monitoring.md)
- [Local AI on Linux Guide](guides/local-ai.md)
- [Glossary](glossary.md)
- [How To Read Service Pages](how-to-read-service-pages.md)
- [Public-Safe Diagrams](../diagrams/README.md)
- [Service Matrix](service-matrix.md)
- [Pre-Publish Review Checklist](pre-publish-review.md)
