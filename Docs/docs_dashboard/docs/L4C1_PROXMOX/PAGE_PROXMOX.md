<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--06--13-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Fichier YAML** | `Dashboard/L4C1_10_Proxmox/page_L4C1_proxmox_2026-06-18.yaml` |
| 🔗 **Accès depuis** | Tap sur vignette L4C1 → `/dashboard-tablette/systeme-proxmox` |
| 🏗️ **Layout** | `grid` → `stack-in-card` vertical — 5 sections |
| 📅 **Modifié le** | 2026-06-10 |
| 🏠 **Version HA** | 2025.2+ |

---

# 🖥️ PAGE PROXMOX — SUPERVISION COMPLÈTE

> **2026-06-10** : Refonte complète — style PVE web UI. 5 sections (ajout MyElectricalData). Boutons contrôle supprimés. bar-card remplacée par progress bars inline. apexcharts CPU 1h par section.

---

## 🎯 VUE D'ENSEMBLE

Page de supervision de l'infrastructure Proxmox VE. 5 sections indépendantes : nœud PVE, VM HA (QEMU 100), LXC Z2M (200), LXC MariaDB (201), LXC MyElectricalData (202). Chaque section : badge statut coloré + CPU/RAM/Disk barres inline + Uptime + graphe CPU 1h.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `button-card` | Badge statut + barres CPU/RAM/Disk + Uptime |
| `stack-in-card` | Groupement vertical sans bordure |
| `text-divider-row` | Séparateurs de sections (blanc) |
| `mod-card` | CSS séparateurs (`--text-divider-color: white`) |
| `apexcharts-card` | Graphe CPU sparkline 1h par section |

> ⚠️ **bar-card supprimée** — remplacée par barres HTML inline dans `button-card label`
> ⚠️ **Boutons de contrôle supprimés** — page lecture seule

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────────┐
│  🏷️ PROXMOX  (heading card)                         │
├─────────────────────────────────────────────────────┤
│  stack-in-card (background: none)                   │
│  ├── ── Proxmox VE ──                              │
│  │   [PROXMOX VE ●online]                          │
│  │   CPU (X vCPU)          XX.X %  ████░░░         │
│  │   RAM                   XX.X%  (X.XX / X GiB)  │
│  │   Disque                XX / XX GiB  (XX%)      │
│  │   [Uptime: Xj Xh]  [Backup: ✓ OK]              │
│  │   ▁▂▃ apexcharts CPU 1h ▃▂▁                    │
│  ├── ── Home Assistant ──                          │
│  │   [HOME ASSISTANT ●running]                     │
│  │   CPU · RAM · Disque · Uptime · apexcharts      │
│  ├── ── ZigBee2MQTT ──                             │
│  │   [ZIGBEE2MQTT ●running]                        │
│  │   CPU · RAM · Disque · Uptime · apexcharts      │
│  ├── ── MariaDB ──                                 │
│  │   [MARIADB ●running]                            │
│  │   CPU · RAM · Disque · Uptime · apexcharts      │
│  └── ── MyElectricalData ──                        │
│      [MYELECTRICALDATA ●running]                   │
│      CPU · RAM · Disque · Uptime · apexcharts      │
└─────────────────────────────────────────────────────┘
```

### Couleurs accent par section

| Section | Couleur |
|---------|---------|
| Proxmox VE | `#0f9d58` (vert) |
| Home Assistant | `#03a9f4` (bleu) |
| ZigBee2MQTT | `#ff9800` (orange) |
| MariaDB | `#f44336` (rouge) |
| MyElectricalData | `#00bcd4` (cyan) |

**Couleur statut badge (universelle) :** `running`/`online` → `rgb(15,157,88)` vert · `stopped`/`offline` → `rgb(244,67,54)` rouge

**Barres inline CPU :**
- PVE/HA : <75% bleu · 75-90% orange · >90% rouge
- Z2M/MariaDB/MED : <40% bleu · 40-60% orange · >60% rouge

**Uptime :** `parseFloat(sensor_heures) / 24` → jours · `% 24` → heures restantes

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🟢 SECTION PROXMOX VE (nœud)

| Entité | Rôle | Seuils |
|--------|------|--------|
| `sensor.pve_statut` | Badge statut | online/offline |
| `sensor.pve_utilisation_du_processeur` | CPU % | <75 bleu · 75-90 orange · >90 rouge |
| `sensor.pve_max_cpu` | Nb vCPU affiché dans label CPU | — |
| `sensor.pve_utilisation_de_la_memoire` | RAM utilisée GiB | <70% bleu · 70-85 orange · >85 rouge |
| `sensor.pve_utilisation_maximale_de_la_memoire` | RAM max GiB | — |
| `sensor.pve_utilisation_du_disque` | Disque utilisé GiB | <70% bleu · 70-85 orange · >85 rouge |
| `sensor.pve_utilisation_maximale_du_disque` | Disque max GiB | — |
| `sensor.pve_uptime` | Uptime (heures flottantes) | — |
| `binary_sensor.pve_backup_status` | Statut backup | off=✓ OK · on=⚠ ERREUR |

### 🔵 SECTION HOME ASSISTANT (QEMU 100)

| Entité | Rôle | Note |
|--------|------|------|
| `sensor.homeassistant_statut` | Badge statut | running/stopped |
| `sensor.homeassistant_utilisation_du_processeur` | CPU % | — |
| `sensor.homeassistant_max_cpu` | Nb vCPU | — |
| `sensor.homeassistant_utilisation_de_la_memoire` | RAM utilisée GiB | — |
| `sensor.homeassistant_utilisation_maximale_de_la_memoire` | RAM max GiB | — |
| `sensor.system_monitor_utilisation_du_disque` | Disque utilisé GiB | ⚠️ Utilise system_monitor (homeassistant_* renvoie 0.0) |
| `sensor.homeassistant_utilisation_maximale_du_disque` | Disque max GiB | — |
| `sensor.homeassistant_uptime` | Uptime (heures) | — |

### 🟠 SECTION ZIGBEE2MQTT (LXC 200)

| Entité | Rôle |
|--------|------|
| `sensor.z2m_statut` | Badge statut |
| `sensor.z2m_utilisation_du_processeur` | CPU % |
| `sensor.z2m_max_cpu` | Nb vCPU |
| `sensor.z2m_utilisation_de_la_memoire` | RAM utilisée GiB |
| `sensor.z2m_utilisation_maximale_de_la_memoire` | RAM max GiB |
| `sensor.z2m_utilisation_du_disque` | Disque utilisé GiB |
| `sensor.z2m_utilisation_maximale_du_disque` | Disque max GiB |
| `sensor.z2m_uptime` | Uptime (heures) |

### 🔴 SECTION MARIADB (LXC 201)

| Entité | Rôle |
|--------|------|
| `sensor.mariadb_statut` | Badge statut |
| `sensor.mariadb_utilisation_du_processeur` | CPU % |
| `sensor.mariadb_max_cpu` | Nb vCPU |
| `sensor.mariadb_utilisation_de_la_memoire` | RAM utilisée GiB |
| `sensor.mariadb_utilisation_maximale_de_la_memoire` | RAM max GiB |
| `sensor.mariadb_utilisation_du_disque` | Disque utilisé GiB |
| `sensor.mariadb_utilisation_maximale_du_disque` | Disque max GiB |
| `sensor.mariadb_uptime` | Uptime (heures) |

### 🩵 SECTION MYELECTRICALDATA (LXC 202)

| Entité | Rôle |
|--------|------|
| `sensor.myelectricaldata_statut` | Badge statut |
| `sensor.myelectricaldata_utilisation_du_processeur` | CPU % |
| `sensor.myelectricaldata_max_cpu` | Nb vCPU |
| `sensor.myelectricaldata_utilisation_de_la_memoire` | RAM utilisée GiB |
| `sensor.myelectricaldata_utilisation_maximale_de_la_memoire` | RAM max GiB |
| `sensor.myelectricaldata_utilisation_du_disque` | Disque utilisé GiB |
| `sensor.myelectricaldata_utilisation_maximale_du_disque` | Disque max GiB |
| `sensor.myelectricaldata_uptime` | Uptime (heures) |

---

## ⚠️ POINTS D'ATTENTION

| Sujet | Détail |
|-------|--------|
| Disque HA | `sensor.homeassistant_utilisation_du_disque` retourne 0.0 GiB → remplacé par `sensor.system_monitor_utilisation_du_disque` |
| Uptime | Les sensors PVE retournent des **heures flottantes** (pas des secondes). Formule : `parseFloat / 24` pour jours |
| stack-in-card fond | Nécessite `card_mod: style: ha-card { background: none !important }` sinon fond gris |
| MyElectricalData badge | Couleur statut = vert `rgb(15,157,88)` universel — PAS le cyan `#00bcd4` de la section |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `proxmox_ve` | Intégration HA | ✅ Essentiel |
| `button-card` | HACS | ✅ Essentiel |
| `stack-in-card` | HACS | ✅ Essentiel |
| `apexcharts-card` | HACS | ✅ Essentiel |
| `text-divider-row` | HACS | ✅ Essentiel |
| `mod-card` | HACS | ✅ Essentiel |
| `card-mod` | HACS | ✅ Essentiel |
| `phu:proxmox` | Icon pack | ✅ Vignette uniquement |

---

## 🔗 FICHIERS LIÉS

- `Dashboard/L4C1_10_Proxmox/page_L4C1_proxmox_2026-06-18.yaml`
- `docs/L4C1_PROXMOX/L4C1_VIGNETTE_PROXMOX.md`
- `docs/DEPENDANCES_GLOBALES.md`

---

← Retour : `L4C1_VIGNETTE_PROXMOX.md` | → Suivant : `docs/L4C2_MINI_PC/`
