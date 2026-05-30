<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--05--29-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard` (vignette L4C1) |
| 🔗 **Accès depuis** | Matrice dashboard principal — Ligne 4, Colonne 1 |
| 🏗️ **Layout** | `stack-in-card` vertical — 4 sections |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-05-29 |
| 🏠 **Version HA** | 2025.2+ |

---

# 🖥️ PAGE PROXMOX PVE — SUPERVISION COMPLÈTE

> ⚠️ **2026-05-29** : Boutons Snapshot supprimés (entités non fonctionnelles). Section Mosquitto supprimée.

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Section PROXMOX VE](#section-proxmox-ve)
4. [Section HOME ASSISTANT](#section-home-assistant)
5. [Section ZIGBEE2MQTT](#section-zigbee2mqtt)
6. [Section MARIADB](#section-mariadb)
7. [Entités utilisées](#entités-utilisées)
8. [Dépendances critiques](#dépendances-critiques)

---

## 🎯 VUE D'ENSEMBLE

Page de supervision complète de l'infrastructure Proxmox VE. 4 sections : nœud PVE, VM HA, LXC Z2M, LXC MariaDB. Chaque section affiche statut, CPU/RAM/Disk, uptime, vCPU et boutons de contrôle.

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
│  Statut • CPU % • RAM % • Disk GiB             │
│  Uptime • Backup • vCPU                         │
│  [Tout ON] [Tout OFF] [Reboot] [Shutdown]       │
├─────────────────────────────────────────────────┤
│  ── Home Assistant ──                           │
│  Statut • CPU % • RAM % • Disk GiB             │
│  Uptime • vCPU                                  │
│  [Démarrer] [Stopper] [LXC] [HA] [Reload]      │
├─────────────────────────────────────────────────┤
│  ── ZigBee2MQTT ──                              │
│  Statut • CPU % • RAM % • Disk GiB             │
│  Uptime • vCPU                                  │
│  [Démarrer] [Stopper] [Relancer]                │
├─────────────────────────────────────────────────┤
│  ── MariaDB ──                                  │
│  Statut • CPU % • RAM % • Disk GiB             │
│  Uptime • vCPU                                  │
│  [Démarrer] [Stopper] [Relancer]                │
└─────────────────────────────────────────────────┘
```

---

## 📍 SECTION PROXMOX VE

### Entités
| Entité | Rôle | Seuils |
|--------|------|--------|
| `sensor.pve_statut` | online / offline | — |
| `sensor.pve_utilisation_du_processeur` | CPU % | ✅ <75 ⚠️ 75-90 ❌ >90 |
| `sensor.pve_memory_usage_percentage` | RAM % | ✅ <75 ⚠️ 75-90 ❌ >90 |
| `sensor.pve_utilisation_du_disque` | Disk GiB (max 94) | ✅ <60 ⚠️ 60-80 ❌ >80 |
| `sensor.pve_uptime` | Uptime heures | — |
| `binary_sensor.pve_backup_status` | Backup OK/ERREUR | off=OK on=ERREUR |
| `sensor.pve_max_cpu` | vCPU count | — |

### Boutons de contrôle
| Bouton | Action |
|--------|--------|
| `button.pve_tout_demarrer` | Démarrer tous LXC |
| `button.pve_tout_stopper` | Stopper tous LXC |
| `button.pve_redemarrer` | Reboot nœud PVE |
| `button.pve_shut_down` | Shutdown nœud PVE |

---

## 📍 SECTION HOME ASSISTANT (LXC 100 — QEMU)

### Entités
| Entité | Rôle | Seuils |
|--------|------|--------|
| `sensor.homeassistant_statut` | running / stopped | — |
| `sensor.homeassistant_utilisation_du_processeur` | CPU % (target 82) | ✅ <75 ⚠️ 75-90 ❌ >90 |
| `sensor.homeassistant_memory_usage_percentage` | RAM % (target 72) | ✅ <75 ⚠️ 75-90 ❌ >90 |
| `sensor.homeassistant_utilisation_du_disque` | Disk GiB (max 32, target 22) | ✅ <20 ⚠️ 20-28 ❌ >28 |
| `sensor.homeassistant_uptime` | Uptime heures | — |
| `sensor.homeassistant_max_cpu` | vCPU count | — |

### Boutons de contrôle
| Bouton | Action |
|--------|--------|
| `button.homeassistant_demarrer` | Démarrer LXC |
| `button.homeassistant_stopper` | Stopper LXC |
| `button.homeassistant_redemarrer` | Redémarrer LXC |
| `button.homeassistant_restart` | Restart service HA |
| `button.homeassistant_reload` | Reload HA |

---

## 📍 SECTION ZIGBEE2MQTT (LXC 200)

### Entités
| Entité | Rôle | Seuils |
|--------|------|--------|
| `sensor.z2m_statut` | running / stopped | — |
| `sensor.z2m_utilisation_du_processeur` | CPU % | ✅ <40 ⚠️ 40-60 ❌ >60 |
| `sensor.z2m_memory_usage_percentage` | RAM % | ✅ <50 ⚠️ 50-70 ❌ >70 |
| `sensor.z2m_utilisation_du_disque` | Disk GiB (max 3.86) | ✅ <2.5 ⚠️ 2.5-3.4 ❌ >3.4 |
| `sensor.z2m_uptime` | Uptime heures | — |
| `sensor.z2m_max_cpu` | vCPU count | — |

### Boutons de contrôle
| Bouton | Action |
|--------|--------|
| `button.z2m_demarrer` | Démarrer LXC |
| `button.z2m_stopper` | Stopper LXC |
| `button.z2m_redemarrer` | Relancer LXC |

---

## 📍 SECTION MARIADB (LXC 201)

### Entités
| Entité | Rôle | Seuils |
|--------|------|--------|
| `sensor.mariadb_statut` | running / stopped | — |
| `sensor.mariadb_utilisation_du_processeur` | CPU % | ✅ <50 ⚠️ 50-75 ❌ >75 |
| `sensor.mariadb_memory_usage_percentage` | RAM % | ✅ <60 ⚠️ 60-80 ❌ >80 |
| `sensor.mariadb_utilisation_du_disque` | Disk GiB (max 7.78) | ✅ <5 ⚠️ 5-7 ❌ >7 |
| `sensor.mariadb_uptime` | Uptime heures | — |
| `sensor.mariadb_max_cpu` | vCPU count | — |

### Boutons de contrôle
| Bouton | Action |
|--------|--------|
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

- `docs/L4C1_PROXMOX/L4C1_VIGNETTE_PROXMOX.md`
- `Dashboard/L4C1_PROXMOX/vignette_L4C1_proxmox_2026-05-29.yaml`
- `docs/DEPENDANCES_GLOBALES.md`

---

← Retour : `L4C1_VIGNETTE_PROXMOX.md` | → Suivant : `docs/L4C2_MINI_PC/`
