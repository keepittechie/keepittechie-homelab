# Local AI Stack

## Purpose

The local AI stack provides private, Linux-first AI experimentation using a GPU server, local model storage, an OpenAI-compatible inference endpoint, and Open WebUI.

## Why This Matters

Local AI is useful for privacy, control, learning, and content creation. It lets viewers understand how models run, why GPU memory matters, how local APIs can mimic hosted AI APIs, and where self-hosted AI fits into a practical homelab.

For KeepItTechie, this stack also supports Linux GPU setup notes, local-first tools, automation, and practical AI workflows without treating every prompt as cloud-bound.

## Where It Fits in the Homelab

```text
Local tools and browser UI
  |
openwebui.home.example.com
  |
ai.home.example.com
  |
GPU server and local model storage
```

The AI stack is an internal service. It can support other tools, but it should not be exposed publicly without strong authentication, rate limiting, and resource controls.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | Linux GPU server or GPU-capable VM |
| GPU role | Local inference and AI experiments |
| Example DNS | `ai.home.example.com`, `openwebui.home.example.com` |
| Public access | No |
| Primary users | Admin tools, local workflows, content experiments |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| Model files | `/mnt/storage/appdata/models` | Low to medium | Large files may be easier to redownload |
| Open WebUI data | `/mnt/storage/appdata/openwebui` | High | Contains app state and settings |
| API service config | `/opt/apps/example/local-ai` | High | Keep credentials private |
| Experiment outputs | `/mnt/storage/appdata/ai-output` | Case by case | Sanitize before sharing |

## Network / DNS

Example internal names:

```text
openwebui.home.example.com -> proxy.home.example.com
ai.home.example.com        -> proxy.home.example.com
```

Example sanitized API base URL:

```text
https://ai.home.example.com/v1
```

Do not publish a real unauthenticated endpoint.

## Key Responsibilities

- Run local models for private experimentation.
- Provide an OpenAI-compatible API shape through a local endpoint.
- Provide a browser UI through Open WebUI.
- Keep model and prompt workflows internal.
- Support KeepItTechie demos around Linux, GPUs, and local-first AI.
- Track GPU, CPU, memory, and disk usage.

## Example Public-Safe Configuration

Sanitized component map:

| Component | Role | Access Level | Public Notes |
|---|---|---|---|
| GPU server | Runs inference workloads | Private LAN | Do not expose management access |
| llama.cpp-compatible endpoint | Local API for model calls | Internal Only | Use placeholder URLs in docs |
| Open WebUI | Web UI for local AI | Private LAN | Do not publish real chats |
| Model storage | Stores local model files | Internal Only | Do not commit model files |
| Monitoring | Tracks GPU and service health | Private LAN | Sanitize dashboards before screenshots |

Example request shape for teaching:

```text
POST https://ai.home.example.com/v1/chat/completions
Authorization: Bearer REPLACE_WITH_PRIVATE_VALUE
```

The example shows the API pattern only. Do not commit real credentials.

## Backup and Restore Notes

- Back up Open WebUI state if users, settings, or conversations matter.
- Document model names and sources without storing large models in Git.
- Back up service configuration privately.
- Rebuild notes may be more useful than full binary backups for model runners.
- Treat prompts and outputs as sensitive if they include personal or operational context.

## Security Notes

- Do not expose local AI endpoints publicly without strong controls.
- Keep API credentials private.
- Do not publish real prompts, chats, or generated private data.
- Monitor resource usage so AI workloads do not starve other services.
- Keep model download sources and licenses documented where appropriate.

## Common Mistakes to Avoid

- Publishing an unauthenticated AI endpoint.
- Assuming local prompts are safe to share publicly.
- Filling storage with models without documenting what is actually used.
- Ignoring GPU and memory monitoring.
- Treating local AI as a magic service instead of a normal app with backups and logs.

## What Viewers Can Learn

- How local inference differs from hosted AI.
- Why GPU memory and model size matter.
- How OpenAI-compatible APIs make local tools easier to integrate.
- How local AI fits into Linux and self-hosting workflows.
- How to keep AI experiments private and controlled.

## Related Docs

- [Local AI on Linux Guide](../../docs/guides/local-ai.md)
- [Local AI flow diagram](../../diagrams/local-ai-flow.md)
- [Apps and AI](../../docs/apps-and-ai.md)

## Future Improvements

- Add a sanitized model inventory template.
- Add GPU monitoring dashboard ideas.
- Add a local AI lab checklist with public-safe example prompts.
