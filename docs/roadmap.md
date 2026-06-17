# Documentation Roadmap

This roadmap tracks how the public KeepItTechie homelab repo can grow without becoming a private config dump.

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
- [ ] Add sanitized exported images for key diagrams.

## Phase 3: Service Deep Dives

- [ ] Add deeper pfSense network walkthrough notes with sanitized examples.
- [ ] Add Pi-hole DNS record examples.
- [ ] Add Proxmox VM role examples.
- [ ] Add monitoring dashboard examples.
- [ ] Add local AI stack notes with safe model inventory examples.

## Phase 4: Backup and Restore Proof

- [ ] Document one successful Proxmox Backup Server restore test.
- [ ] Add app-aware backup notes for Wiki.js, Nextcloud, FinanceHQ, and CareerFill.
- [ ] Add a sanitized restore checklist for the media stack.
- [ ] Add storage rollback examples for NAS snapshots and ZFS snapshots.

## Phase 5: Video Companion Expansion

- [ ] Add links to published KeepItTechie videos.
- [ ] Add per-episode repo references.
- [ ] Add safe demo scripts or checklists where useful.
- [ ] Add viewer exercises for DNS, backups, monitoring, and reverse proxying.

## Phase 6: Sanitized Config Examples

- [ ] Add sanitized NGINX reverse proxy examples.
- [ ] Add sanitized Pi-hole local DNS examples.
- [ ] Add sanitized Ansible inventory examples.
- [ ] Add sanitized Grafana dashboard notes.
- [ ] Add example `.env` patterns without real values.

## Maintenance Rule

Every new phase should keep the repo documentation-first. Public examples should teach structure and decision-making without exposing live infrastructure.
