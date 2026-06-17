# Documentation Roadmap

This roadmap tracks how the public KeepItTechie homelab repo can grow without becoming a private config dump.

Completed foundation work now covers the public-safe base docs, navigation, architecture diagram, service matrix, and the first three service deep-dive groups: core infrastructure, storage/monitoring, and apps/media/AI.

## Phase 1: Public-Safe Foundation

- [x] Expand the main README.
- [x] Add top-level docs for overview, hardware, network, services, storage, security, and content planning.
- [x] Add service READMEs with consistent sections.
- [x] Add sanitized inventory and environment examples.
- [x] Add a basic secret scan.

## Phase 2: Diagrams and Navigation

- [x] Add a Mermaid architecture diagram.
- [x] Add a service matrix.
- [x] Link new docs from the README.
- [x] Link diagram docs from the diagrams index.
- [x] Add cross-links between deep-dive index pages.
- [ ] Add sanitized exported images for key diagrams.

## Phase 3: Service Deep Dives

- [x] Add a core infrastructure index page.
- [x] Add a storage and monitoring index page.
- [x] Add an apps and AI index page.
- [x] Add deeper pfSense network walkthrough notes with sanitized examples.
- [x] Add Pi-hole DNS record examples.
- [x] Add Proxmox VM role examples.
- [x] Add PBS backup and restore checklist notes.
- [x] Add reverse proxy sanitized NGINX example.
- [x] Add Cloudflare Tunnel service exposure table.
- [x] Add Synology NAS share map examples.
- [x] Add ZFS dataset and command examples.
- [x] Add monitoring target and dashboard examples.
- [x] Add local AI stack notes with safe component examples.
- [x] Add media stack dependency examples.
- [x] Add Wiki.js namespace examples.
- [x] Add Nextcloud data responsibility examples.
- [x] Add dashboard grouping examples.
- [x] Add personal app public/private boundary examples.
- [x] Add AWX automation boundary examples.
- [ ] Add deeper screenshots or generated visuals with fake data.
- [ ] Add final public-safe diagrams for app and storage flows.

## Phase 4: Backup and Restore Proof

- [ ] Document one successful Proxmox Backup Server restore test.
- [x] Add a public-safe restore test evidence template.
- [ ] Add app-aware backup notes for Wiki.js, Nextcloud, FinanceHQ, and CareerFill.
- [ ] Add a sanitized restore checklist for the media stack.
- [ ] Add storage rollback examples for NAS snapshots and ZFS snapshots.

## Phase 5: Video Companion Expansion

- [ ] Add links to published KeepItTechie videos.
- [ ] Add per-episode repo references.
- [ ] Add safe demo scripts or checklists where useful.
- [ ] Add viewer exercises for DNS, backups, monitoring, and reverse proxying.
- [ ] Add viewer exercises for local AI, dashboards, documentation, media, and private apps.

## Phase 6: Sanitized Config Examples

- [ ] Add sanitized NGINX reverse proxy examples.
- [ ] Add sanitized Pi-hole local DNS examples.
- [ ] Add sanitized Ansible inventory examples.
- [ ] Add sanitized Grafana dashboard notes.
- [ ] Add example `.env` patterns without real values.
- [ ] Add sanitized app config snippets where useful.

## Maintenance Rule

Every new phase should keep the repo documentation-first. Public examples should teach structure and decision-making without exposing live infrastructure.
