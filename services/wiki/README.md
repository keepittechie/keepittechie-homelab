# Wiki.js

## Purpose

Wiki.js is the documentation hub for the homelab. It can hold public learning pages, private runbooks, troubleshooting notes, and operational references.

## Why This Matters

A homelab becomes easier to maintain when the decisions are written down. Wiki.js helps separate quick operational notes from polished public GitHub documentation.

The important public lesson is that documentation needs boundaries: public pages can teach patterns, while private namespaces can hold details that should not appear in GitHub.

## Where It Fits in the Homelab

```text
Browser
  |
wiki.home.example.com
  |
Reverse proxy
  |
Wiki.js app, database, and uploads
```

Wiki.js complements this repository. This repo is public-safe and reader-facing. Wiki.js can contain deeper private operational notes.

## Host / Runtime

| Field | Value |
|---|---|
| Runtime | App VM or container |
| Example DNS | `wiki.home.example.com` |
| Public access | Namespace-dependent |
| Primary data | Pages, uploads, metadata, auth settings |
| Admin access | Private or authenticated |

## Storage / Data Layout

Example layout:

| Data | Example Path | Backup Need | Notes |
|---|---|---|---|
| Database | `/mnt/storage/appdata/wiki/db` | High | Contains page metadata and content |
| Uploads | `/mnt/storage/appdata/wiki/uploads` | High | May contain screenshots or files |
| Config | `/opt/apps/example/wiki` | High | Keep private settings out of Git |
| Public exports | `/mnt/storage/backups/wiki-public` | Medium | Review before publishing |

## Network / DNS

Example:

```text
wiki.home.example.com -> proxy.home.example.com
```

Private admin pages should require authentication. Public pages should be reviewed before publishing or linking from public docs.

## Key Responsibilities

- Host homelab documentation.
- Separate public and private content.
- Preserve runbooks and troubleshooting notes.
- Support organized homelab documentation for KeepItTechie.
- Keep private operational details out of public repos.
- Provide a searchable knowledge base for the lab.

## Example Public-Safe Configuration

Sanitized namespace model:

| Namespace | Audience | Access Level | Notes |
|---|---|---|---|
| `/public` | Public readers | Limited Public | Review before publishing |
| `/homelab` | Internal learning notes | Private LAN | Sanitize before copying to GitHub |
| `/admin` | Operator runbooks | Private LAN or VPN | Never publish raw admin notes |
| `/drafts` | Private documentation drafts | Private | Review and sanitize before publishing |

## Backup and Restore Notes

- Back up the database and uploads together.
- Back up configuration privately.
- Test restoring pages and uploaded assets.
- Keep private namespace exports out of public Git.
- Review public exports for sensitive screenshots and links.

## Security Notes

- Do not allow anonymous access to private namespaces.
- Do not copy raw private runbooks into public docs.
- Review screenshots for hostnames, paths, and account data.
- Keep auth settings and credentials private.
- Treat docs as operational data, not just text.

## Common Mistakes to Avoid

- Mixing private admin notes with public tutorials.
- Forgetting to back up uploads.
- Publishing screenshots that reveal private data.
- Treating the wiki as a replacement for Git when versioned docs are needed.
- Letting stale runbooks stay unmarked.

## What Readers Can Learn

- Why documentation is part of operations.
- How public docs and private runbooks can coexist.
- How to turn internal notes into safe teaching material.
- Why backups matter for documentation platforms.

## Future Improvements

- Add a sanitized content tree.
- Add public/private review checklist examples.
- Add a Wiki.js restore checklist.
