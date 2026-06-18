# Homelab DNS and Pi-hole

This guide explains how DNS, Pi-hole, and local service names fit into a homelab.

## Guide Goal

This guide shows why DNS makes a homelab easier to use. Instead of memorizing raw addresses, readers can use readable service names such as `grafana.home.example.com`, `proxy.home.example.com`, and `nas.home.example.com`.

For beginners, the key idea is simple: DNS is the phone book for the lab. Pi-hole can answer local names, filter unwanted domains, and forward everything else upstream.

## What Readers Will Learn

- What DNS does.
- Why local DNS matters in a homelab.
- What Pi-hole does besides ad blocking.
- Why a primary and secondary DNS setup is useful.
- How DHCP can hand DNS servers to client devices.
- Why internal service names are easier than raw IP addresses.
- What DNS details should stay out of public repos.

## Why DNS Matters in a Homelab

DNS becomes important as soon as the lab has more than a few services. A name such as `grafana.home.example.com` is easier to remember, document, and move than a raw address.

Local DNS helps with:

- Readable service names.
- Easier troubleshooting.
- Cleaner reverse proxy routing.
- Better documentation.
- Fewer hardcoded addresses in notes and bookmarks.
- Clear separation between service identity and machine identity.

DNS also makes the lab easier to explain. Readers can understand what a service does by its name before learning which VM, container, or host runs it.

## Where Pi-hole Fits

Pi-hole sits in the DNS layer. In this lab pattern, clients ask Pi-hole for DNS answers. Pi-hole answers local records when it knows them, blocks known ad or tracker domains when configured to do so, and forwards other requests to an upstream resolver.

Pi-hole can provide:

- DNS filtering.
- Local DNS records.
- Query visibility.
- Upstream DNS forwarding.
- A useful place to document internal service names privately.

The Pi-hole admin UI should stay private. It can reveal clients, query history, local records, blocklists, and other details that do not belong in public screenshots.

## Primary and Secondary DNS

A primary and secondary DNS setup keeps name resolution available when one resolver is down for maintenance or troubleshooting.

Example service names:

```text
pihole1.home.example.com
pihole2.home.example.com
```

If the primary resolver is down, clients can still ask the secondary resolver. This does not replace backups or monitoring, but it does reduce the chance that a single DNS VM breaks access to the whole lab.

Both resolvers should be documented, backed up, and kept private.

## Local DNS Records

Local DNS records map names to internal services. This is where service identity and machine identity become useful.

- **Service identity:** The name readers or users type, such as `grafana.home.example.com`.
- **Machine identity:** The VM, container host, or physical machine that runs the workload.

Keeping those separate makes services easier to move later. Public docs use sanitized examples so the pattern is visible without publishing the real DNS zone.

## DHCP and DNS Handoff

At a high level, pfSense or another router can hand DNS settings to client devices through DHCP:

```text
Client joins network
  -> DHCP provides network settings
  -> DHCP includes Pi-hole DNS servers
  -> Client asks Pi-hole for names
  -> Pi-hole answers local records or forwards upstream
```

This keeps clients pointed at the intended DNS path. If clients are pointed at random public DNS servers, local names may fail and DNS filtering visibility becomes incomplete.

## Public-Safe Examples

- Open the [DNS flow diagram](../../diagrams/dns-flow.md).
- Open the [sanitized Pi-hole CSV example](../../examples/pihole/local-dns-records.example.csv).
- Explain service names such as `proxy.home.example.com`, `grafana.home.example.com`, and `nas.home.example.com`.
- Explain how DNS reduces raw address memorization.
- Review what not to publish: live records, admin screenshots, raw exports, and private domains.

Do not include a real Pi-hole admin page unless it is sanitized or uses demo data.

## Example Local DNS Records

| Hostname | Points To | Purpose |
|---|---|---|
| `proxy.home.example.com` | Reverse proxy | Routes internal web services |
| `grafana.home.example.com` | Monitoring service | Opens the monitoring dashboard |
| `nas.home.example.com` | Storage service | Points to the NAS service identity |
| `ai.home.example.com` | Local AI service | Points to the local AI entry point |

This table avoids exact addresses. For a CSV-style teaching template, see the [sanitized Pi-hole local DNS example](../../examples/pihole/local-dns-records.example.csv).

## Common Mistakes

- Pointing clients at random DNS servers.
- Configuring only one DNS server.
- Exposing DNS admin interfaces publicly.
- Documenting real internal DNS records in public repos.
- Relying only on raw addresses.
- Forgetting to update DNS when services move.
- Confusing service identity and machine identity.
- Treating DNS filtering as a replacement for firewall policy.

## What Is Intentionally Not Shown

- Real DNS records.
- Exact IPs.
- Private domains.
- Pi-hole API tokens.
- Admin screenshots.
- Raw exports.
- Upstream provider choices if private.
- Private DHCP scopes.

## Commands and Examples

These commands use sanitized example names:

```bash
dig grafana.home.example.com
nslookup proxy.home.example.com
ping pihole1.home.example.com
```

Related safe examples:

- [DNS flow diagram](../../diagrams/dns-flow.md)
- [Pi-hole example notes](../../examples/pihole/README.md)
- [Sanitized local DNS CSV](../../examples/pihole/local-dns-records.example.csv)

## Next Steps

- Read the [Pi-hole service doc](../../services/pihole/README.md).
- Study the [DNS flow diagram](../../diagrams/dns-flow.md).
- Review the [sanitized local DNS CSV](../../examples/pihole/local-dns-records.example.csv).
- Document real local DNS records privately.
- Avoid putting live DNS records, admin screenshots, or raw exports in public repos.

## Related Docs

- [Core Infrastructure](../core-infrastructure.md)
- [Network Design](../network.md)
- [DNS Flow](../../diagrams/dns-flow.md)
- [Pi-hole Example](../../examples/pihole/README.md)
- [Pi-hole](../../services/pihole/README.md)
- [pfSense](../../services/pfsense/README.md)
- [Glossary](../glossary.md)
- [Pre-Publish Review](../pre-publish-review.md)
