# Local AI Stack

## Purpose

The local AI stack supports private AI experimentation, Linux-first AI workflows, local inference, and tool integrations without sending every request to a hosted provider.

## Where It Fits

```text
Local tools and web UI
  |
OpenAI-compatible local endpoint
  |
GPU server
  |
local models
```

The stack is useful for learning how models run, how GPU memory affects choices, and how local AI can connect to real admin workflows.

## Host / Runtime

| Field | Value |
|---|---|
| Example host | `hephaestus` |
| GPU | NVIDIA RTX A2000 12GB |
| Runtime | Linux GPU server / VM workloads |
| Example DNS | `ai.home.example.com`, `openwebui.home.example.com` |
| Public access | No |

## Key Dependencies

- NVIDIA driver stack
- CUDA-capable runtime where needed
- Local model storage
- llama.cpp-style OpenAI-compatible endpoint
- Open WebUI
- Reverse proxy for internal-only access

## Network / DNS

Local AI endpoints should stay private unless strong authentication, rate limiting, and resource controls are in place.

Example:

```text
openwebui.home.example.com -> proxy.home.example.com
ai.home.example.com        -> proxy.home.example.com
```

## Backup Notes

- Back up Open WebUI configuration if conversations, users, or settings matter.
- Document model locations, but do not commit large model files.
- Keep generated personal data out of public examples.
- Rebuild notes may be more useful than full binary backups for model runners.

## Security Notes

- Do not publish unauthenticated model endpoints.
- Treat local AI prompts and outputs as potentially sensitive.
- Keep API-style credentials out of Git.
- Monitor GPU and disk usage so model workloads do not break unrelated services.

## What Viewers Can Learn

- How local inference differs from hosted AI APIs.
- Why VRAM matters.
- How OpenAI-compatible endpoints make local tools easier to integrate.
- How to keep AI workflows local-first and privacy-aware.

## Future Improvements

- Add a sanitized model inventory format.
- Add GPU monitoring examples.
- Add a private-versus-public AI endpoint decision checklist.
