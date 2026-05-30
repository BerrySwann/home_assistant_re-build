<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--05--29-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard` (vignette principale) |
| 🔗 **Accès depuis** | L4C1 - Matrice dashboard principal (ligne 4, colonne 1) |
| 🏗️ **Layout** | `stack-in-card` vertical — 4 sections (PVE, HA, Z2M, MariaDB) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-05-29 |
| 🏠 **Version HA** | 2025.2+ |

---

# 🖥️ L4C1 PROXMOX VE

---

## 🎯 VUE D'ENSEMBLE

Vignette de supervision complète de l'infrastructure Proxmox VE. Affiche les métriques CPU/RAM/Disk + statut + boutons de contrôle pour 4 services : Proxmox PVE, Home Assistant, Zigbee2MQTT, MariaDB.

> ⚠️ Snapshots supprimés (entités non fonctionnelles) — 2026-05-29

### Intégrations requises
- ✅ `proxmox_ve` — Intégration Proxmox VE (UI)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `button-card` | Statuts, uptime, vCPU, boutons contrôle |
| `bar-card` | Jauges CPU %, RAM %, Disk GiB |
| `stack-in-card` | Groupement vertical sans bordures |
| `text-divider-row` | Séparateurs de sections |
| `mod-card` | Style CSS des séparateurs |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────┐
│  ── Proxmox VE ──                               │
│  [PROXMOX VE]  statut: online/offline           │
│  CPU % │ RAM % │ Disk GiB                       │
│  Uptime │ Backup │ vCPU                         │
│  [Tout ON] [Tout OFF] [Reboot] [Shutdown]       │
├─────────────────────────────────────────────────┤
│  ── Home Assistant ──                           │
│  [HOME ASSISTANT]  statut: running/stopped      │
│  CPU % │ RAM % │ Disk GiB                       │
│  Uptime │ vCPU                                  │
│  [Démarrer] [Stopper] [LXC] [HA] [Reload]      │
├─────────────────────────────────────────────────┤
│  ── ZigBee2MQTT ──                              │
│  [ZIGBEE2MQTT]  statut: running/stopped         │
│  CPU % │ RAM % │ Disk GiB                       │
│  Uptime │ vCPU                                  │
│  [Démarrer] [Stopper] [Relancer]                │
├─────────────────────────────────────────────────┤
│  ── MariaDB ──                                  │
│  [MARIADB]  statut: running/stopped             │
│  CPU % │ RAM % │ Disk GiB                       │
│  Uptime │ vCPU                                  │
│  [Démarrer] [Stopper] [Relancer]                │
└─────────────────────────────────────────────────┘
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🟢 PROXMOX VE (nœud)

| Entité | Rôle |
|--------|------|
| `sensor.pve_statut` | Statut online/offline |
| `sensor.pve_utilisation_du_processeur` | CPU % |
| `sensor.pve_memory_usage_percentage` | RAM % |
| `sensor.pve_utilisation_du_disque` | Disk GiB (max 94) |
| `sensor.pve_uptime` | Uptime en heures |
| `binary_sensor.pve_backup_status` | Statut backup (off=OK) |
| `sensor.pve_max_cpu` | Nombre vCPU |
| `button.pve_tout_demarrer` | Démarrer tous les LXC |
| `button.pve_tout_stopper` | Stopper tous les LXC |
| `button.pve_redemarrer` | Reboot nœud PVE |
| `button.pve_shut_down` | Shutdown nœud PVE |

### 🔵 HOME ASSISTANT (LXC 100)

| Entité | Rôle |
|--------|------|
| `sensor.homeassistant_statut` | Statut running/stopped |
| `sensor.homeassistant_utilisation_du_processeur` | CPU % (max 100, target 82) |
| `sensor.homeassistant_memory_usage_percentage` | RAM % (max 100, target 72) |
| `sensor.homeassistant_utilisation_du_disque` | Disk GiB (max 32, target 22) |
| `sensor.homeassistant_uptime` | Uptime en heures |
| `sensor.homeassistant_max_cpu` | Nombre vCPU |
| `button.homeassistant_demarrer` | Démarrer LXC |
| `button.homeassistant_stopper` | Stopper LXC |
| `button.homeassistant_redemarrer` | Redémarrer LXC |
| `button.homeassistant_restart` | Restart HA (service) |
| `button.homeassistant_reload` | Reload HA |

### 🟠 ZIGBEE2MQTT (LXC 200)

| Entité | Rôle |
|--------|------|
| `sensor.z2m_statut` | Statut running/stopped |
| `sensor.z2m_utilisation_du_processeur` | CPU % |
| `sensor.z2m_memory_usage_percentage` | RAM % |
| `sensor.z2m_utilisation_du_disque` | Disk GiB (max 3.86) |
| `sensor.z2m_uptime` | Uptime en heures |
| `sensor.z2m_max_cpu` | Nombre vCPU |
| `button.z2m_demarrer` | Démarrer LXC |
| `button.z2m_stopper` | Stopper LXC |
| `button.z2m_redemarrer` | Relancer LXC |

### 🔴 MARIADB (LXC 201)

| Entité | Rôle |
|--------|------|
| `sensor.mariadb_statut` | Statut running/stopped |
| `sensor.mariadb_utilisation_du_processeur` | CPU % |
| `sensor.mariadb_memory_usage_percentage` | RAM % |
| `sensor.mariadb_utilisation_du_disque` | Disk GiB (max 7.78) |
| `sensor.mariadb_uptime` | Uptime en heures |
| `sensor.mariadb_max_cpu` | Nombre vCPU |
| `button.mariadb_demarrer` | Démarrer LXC |
| `button.mariadb_stopper` | Stopper LXC |
| `button.mariadb_redemarrer` | Relancer LXC |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `proxmox_ve` | Intégration HA | ✅ Essentiel |
| `button-card` | HACS | ✅ Essentiel |
| `bar-card` | HACS | ✅ Essentiel |
| `stack-in-card` | HACS | ✅ Essentiel |
| `text-divider-row` | HACS | ✅ Essentiel |
| `mod-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- `Dashboard/L4C1_PROXMOX/vignette_L4C1_proxmox_2026-05-29.yaml`
- `docs/L4C1_PROXMOX/PAGE_PROXMOX.md`
- `docs/DEPENDANCES_GLOBALES.md`

---

← Retour : `L1C3_CLIM` | → Suivant : `L4C2_MINI_PC`
