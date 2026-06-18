# Local AI on Linux

This page is a public-safe companion guide for a KeepItTechie video about running local AI services on Linux in a homelab.

## Episode Goal

This episode introduces local AI as another self-hosted service layer in the homelab. It shows how local AI can support learning, experimentation, privacy, and Linux workflows without depending entirely on cloud tools.

The goal is practical: understand the moving parts, protect the endpoint, and use fake or demo data when explaining the stack publicly.

## What Viewers Will Learn

- What local AI means.
- Why Linux is a strong platform for local AI.
- Where tools like Open WebUI and llama.cpp fit.
- Why OpenAI-compatible local endpoints are useful.
- How local AI can connect to apps and workflows.
- Why private prompts, documents, and model data should not be published.
- Why local AI endpoints should not be exposed publicly without strong protection.

## Why Local AI Matters

Local AI gives the lab more control over where prompts and data go. It is also a good learning path for Linux, GPUs, APIs, automation, and self-hosted workflows.

Running AI locally can help viewers experiment without depending on one cloud service for every request. That does not mean local AI is automatically secure. The surrounding apps, logs, uploaded files, and integrations still need careful handling.

Hardware limits matter too. GPU memory, CPU speed, RAM, disk space, and model size all affect the experience.

## Where Local AI Fits in the Homelab

Local AI can sit alongside other app services:

- Documentation workflows.
- Automation tools.
- Development tools.
- Private assistants.
- Content workflows.
- Local-first personal apps.

In this repo, local AI is documented as an internal service. It can support other tools, but it should not become a public endpoint by default.

## Core Components

A practical local AI stack usually includes:

- A GPU or CPU host.
- Model files.
- An inference engine such as llama.cpp.
- An OpenAI-compatible API endpoint.
- A web frontend such as Open WebUI.
- Apps or tools that call the endpoint.

The exact model choices and runtime details can change over time, but the architecture pattern stays useful: local model runtime, private endpoint, controlled access, and careful data handling.

## Local AI vs Cloud AI

| Area | Local AI | Cloud AI |
|---|---|---|
| Control | More control over runtime and data flow | Provider manages infrastructure |
| Performance | Depends on local hardware | Usually stronger models available |
| Privacy | Can keep more data local if configured correctly | Data leaves the lab |
| Maintenance | User manages models and services | Provider handles operations |
| Cost | Hardware/electricity cost | Subscription/API cost |

This is not an argument that one is always better. The useful lesson is knowing which tradeoffs matter for a specific workflow.

## API Endpoints and App Integrations

An OpenAI-compatible local endpoint lets apps use a familiar API pattern while routing requests to a local service.

Public examples should use placeholders such as:

```text
https://ai.home.example.com/v1
```

Local endpoints should be private, authenticated, or tightly controlled. Never publish keys, private endpoint URLs, real app configs, or private prompts.

## Model Storage and Hardware

Models can take a lot of disk space. Some models require more GPU memory than others, and quantized models can make smaller systems more useful.

Viewers do not need the biggest GPU to learn the architecture. Start with a simple model or web UI, then expand when the use case is clear.

Document model choices safely:

- Use generic model categories where possible.
- Avoid private model paths.
- Avoid sensitive datasets.
- Do not commit model files.
- Review any generated outputs before sharing.

## Privacy and Security Notes

Local AI is not automatically private if connected apps send data elsewhere.

Watch these areas closely:

- Logs can contain prompts.
- Uploaded documents can contain sensitive data.
- Vector databases and embeddings can contain private information.
- Web UIs and APIs should stay protected.
- Public docs should use fake prompts and demo data only.

Treat local AI like any other powerful internal service: private by default, monitored, backed up where needed, and documented without exposing private data.

## Public-Safe Demo Ideas

- Show the [local AI flow diagram](../../diagrams/local-ai-flow.md).
- Use a fake prompt with no personal or operational data.
- Show a sanitized endpoint example such as `https://ai.home.example.com/v1`.
- Explain Open WebUI conceptually without private chat history.
- Show how an app might call a local OpenAI-compatible endpoint.
- Show what should not be published.

Do not show live chat logs, private prompts, uploaded documents, private model directories, or private workflow data.

## Example Local AI Flow

| Step | Component | What Happens |
|---|---|---|
| 1 | User/App | Sends a request to a local AI endpoint |
| 2 | Open WebUI or App | Provides the interface or workflow |
| 3 | Local API Endpoint | Receives OpenAI-compatible request |
| 4 | Inference Engine | Runs the model locally |
| 5 | Model Storage | Provides the selected model file |
| 6 | Response | Returns output to the user or app |

## Example Component Table

| Component | Role | Access Recommendation | Public-Safe Notes |
|---|---|---|---|
| GPU/AI Host | Runs local inference workloads | Private LAN / VPN | Do not publish exact host details |
| Open WebUI | Browser interface for local AI | Private LAN / VPN | Do not share private chat history |
| Local API Endpoint | App integration point | Private / authenticated | Do not expose publicly without protection |
| Model Storage | Stores model files | Private | Avoid publishing private paths |
| App Integrations | Tools that call the endpoint | Depends on app | Use fake/demo prompts in docs |

## Common Mistakes

- Exposing a local AI API publicly.
- Sharing chat logs or uploaded documents.
- Assuming local always means private.
- Ignoring logs.
- Running models without monitoring resource usage.
- Storing sensitive prompts in public repos.
- Committing `.env` files with API keys.
- Using real personal data in demos.
- Overbuying hardware before understanding requirements.

## What Is Intentionally Not Shown

- Private prompts.
- Chat history.
- Uploaded documents.
- Vector databases.
- Private model paths.
- API keys.
- Live endpoints.
- Raw app configs.
- Private workflow data.
- Sensitive personal, job, or financial data.

## Commands and Examples

These commands are safe examples that viewers can adapt in their own lab. Review command output before sharing it publicly because it can include hostnames, usernames, paths, GPU details, and running processes.

```bash
# Example: check a sanitized local AI endpoint
curl -I https://ai.home.example.com

# Example: inspect GPU usage in a viewer's own lab
nvidia-smi

# Example: run the repo safety scan before sharing docs
python3 scripts/public_safety_scan.py
```

## After Watching

- Read the [Local AI Stack](../../services/local-ai/README.md) service doc.
- Study the [local AI flow diagram](../../diagrams/local-ai-flow.md).
- Review the [Apps and AI](../apps-and-ai.md) index.
- Start with a small model or simple web UI.
- Protect local endpoints.
- Use fake/demo prompts in public docs.
- Monitor resource usage.

## Related Docs

- [Apps and AI](../apps-and-ai.md)
- [Current Setup](../current-setup.md)
- [Build Your Own Homelab](../build-your-own.md)
- [Local AI Stack](../../services/local-ai/README.md)
- [Local AI Flow Diagram](../../diagrams/local-ai-flow.md)
- [Screenshot Policy](../screenshots-policy.md)
- [Pre-Publish Review](../pre-publish-review.md)
- [Glossary](../glossary.md)
