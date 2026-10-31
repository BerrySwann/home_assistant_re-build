# PROXMOX — ETAT INFRASTRUCTURE
*Dernière mise à jour : 2026-10-31*

---

## VMs ET CONTAINERS

| VMID | Nom | Type | IP | Status | Notes |
|:-----|:----|:-----|:---|:-------|:------|
| VM 100 | HomeAssistant | VM (KVM) | `10.32.154.243` | running | HAOS - VM principale |
| CT 200 | Z2M | CT (LXC) | `10.32.154.244` | running | Zigbee2MQTT + Mosquitto, nesting=1 |
| CT 201 | mariadb | CT (LXC) | `10.32.154.242` | running | MariaDB, nesting=1 |
| CT 202 | myelectricaldata | CT (LXC) | `10.32.154.245` | running | MyElectricalData, nesting=1 |
| CT 501 | searxng | CT (LXC) | `10.32.154.246` | running | SearXNG, Debian 12, nesting=1 (requis systemd 252) |

---

## STOCKAGE

| Volume | Type | Utilise | Total | % |
|:-------|:-----|:--------|:------|:--|
| `local` | dir | 57.0 GB | 94.0 GB | 60.7% |
| `local-lvm` | lvmthin | 57.7 GB | 349.0 GB | 16.5% |

> `local` : backups, ISO, templates (format dir).
> `local-lvm` : disques VMs/CTs (format LVM thin - ne peut PAS stocker des backups).
> Seuil d'alerte : local > 85%. Apres backup nuit (VM 100 ~8-10 GB) surveiller.

---

## JOBS BACKUP

| Job ID | VMID | Heure | Retention | Stockage |
|:-------|:-----|:------|:----------|:---------|
| backup-f493ec85 | VM 100 (HA) | 02:00 | keep-last=3 | local |
| backup-lxc-200 | CT 200 (Z2M) | 03:00 | keep-last=5 | local |
| backup-lxc-201 | CT 201 (MariaDB) | 04:00 | keep-last=5 | local |
| backup-120a853f | CT 202 (MyElectricalData) | 05:00 | keep-last=5 | local |
| e54794f1 | CT 501 (SearXNG) | 06:00 | keep-last=1 | local |

> Tous les backups : compression zstd, mode snapshot.
> CT 501 : keep-last=1 (service leger, 1 seule sauvegarde suffit).
> Planification etalee sur la nuit pour eviter les acces disque simultanees.

---

## HISTORIQUE INTERVENTIONS

| Date | Action |
|:-----|:-------|
| 2026-08-08 | Correction `maxfiles` deprecie dans `/etc/pve/jobs.cfg` (PVE 7+) |
| 2026-08-08 | Creation MCP Proxmox (`ReBuild/proxmox-mcp/`) - API REST Python |
| 2026-08-20 | Reduction retention VM 100 + CT 202 : 7 -> 5 jours (espace local 89% -> 68%) |
| 2026-08-20 | Reduction retention CT 200 + CT 201 : 7 -> 5 jours |
| 2026-08-20 | Installation CT 501 SearXNG (Debian 12, IP 10.32.154.251) |
| 2026-08-20 | Activation nesting=1 sur CT 501 (fix systemd 252 warning) |
| 2026-08-20 | Creation job backup CT 501 : 06:00, keep-last=1 |
| 2026-08-30 | Suppression snapshots LVM orphelins (snap VM 100/201/202 de mai-aout) |
| 2026-08-30 | Reduction retention VM 100 : keep-last=5 -> 3 (local a 59%) |
| 2026-09-24 | CT 501 : IP réelle constatée `10.32.154.246` (net0 PVE vérifié ; .251 obsolète, plus active) |
| 2026-10-09 | local : 55→63.9 GB (59%→68%) — local-lvm : 71→57.3 GB (21%→16%, -13.7 GB constaté) |
| 2026-10-09 | Mise à jour 132 paquets (44 Proxmox + 88 Debian) — PVE reste 9.2.10, pas de reboot, tous VMs/CTs running |
| 2026-10-09 | Redémarrage VM 100 (HA) : RAM saturée 93% (8.1/8GB) → retombée à 33% (2.6/8GB) après reboot |
| 2026-10-31 | Mise à jour Proxmox par Eric puis redémarrage du host : PVE 9.2.24 (noyau 7.0.14-26-pve), VM 100 + CT 200/201/202/501 running après redémarrage. Sauvegarde HA `Avant_maj_Proxmox_2026-10-31` faite avant. Relevé fait avec `pveversion`, `qm list`, `pct list`, `pvesm status` ; jobs de sauvegarde et IP des CT non relus ce jour-là |

---

## ACCESS

| Service | Acces | URL / Commande |
|:--------|:------|:---------------|
| Proxmox UI | Local | `https://10.32.154.240:8006` |
| Proxmox UI | Distant | Tailscale |
| Home Assistant | Distant | `https://erodi-ha.com` (Cloudflare Tunnel) |
| SSH Proxmox | Local | `ssh root@10.32.154.240` |

---

*Genere avec Cowork - HA ReBuild*
