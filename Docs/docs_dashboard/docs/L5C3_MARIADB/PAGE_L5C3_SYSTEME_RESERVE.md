<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--05--18-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/reserve` |
| 🔗 **Accès depuis** | Vignette L5C3 (MariaDB) → tap → `/dashboard-tablette/reserve` |
| 🏗️ **Layout** | `type: vertical`, max_columns: 3 |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Créé le** | 2026-05-18 |
| 🏠 **Version HA** | 2025.2.x |

---

# 🖥️ PAGE RÉSERVE SYSTÈME — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section Home Assistant](#section-home-assistant)
4. [Section Zigbee2MQTT](#section-zigbee2mqtt)
5. [Section MariaDB](#section-mariadb)
6. [Entités utilisées](#entités-utilisées--provenance-complète)
7. [Couleurs et seuils](#couleurs-et-seuils)
8. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page de surveillance des trois services critiques fonctionnant en conteneurs Proxmox VE :
- **Home Assistant** : CPU, Uptime, Mémoire (%)  + Mémoire (GiB utilisée)
- **Zigbee2MQTT (Z2M)** : CPU, Uptime, Mémoire (%) + Mémoire (MiB utilisée)
- **MariaDB** : CPU, Uptime, Mémoire (%) + Mémoire (MiB utilisée)

### Intégrations requises

- ✅ **proxmox_ve** — 12 sensors (CPU, Uptime, Memory % / Used pour HA, Z2M, MariaDB)
- ✅ **sql.yaml** — `sensor.taille_db_home_assistant` (taille DB en MiB)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:button-card` | Titre "Réserve Système" + Headers de section (HOME ASSISTANT, Z2M, MARIADB) |
| `custom:stack-in-card` | Groupement vertical sans bordure (3 sections) |
| `custom:bar-card` | Jauges CPU, Uptime, Memory %, Memory Used |
| `card-mod` | Personnalisation CSS (icons, fonts, pas de bordures) |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌──────────────────────────────────────────────────────────┐
│  TITRE PRINCIPAL : "Réserve Système"                     │
│  (button-card, fond noir transparent, icône database)    │
├──────────────────────────────────────────────────────────┤
│
│  SECTION 1 : HOME ASSISTANT
│  ┌────────────────────────────────────────────────────┐
│  │ Header: "HOME ASSISTANT" (bleu/info)               │
│  │ ├── Row 1: CPU | Uptime                           │
│  │ │     └── bar-cards avec seuils (74%→75%→90%)     │
│  │ └── Row 2: Memory % | Memory Used                 │
│  │     └── bar-cards avec seuils (74%→75%→80%)       │
│  └────────────────────────────────────────────────────┘
│
│  SECTION 2 : ZIGBEE2MQTT (Z2M)
│  ┌────────────────────────────────────────────────────┐
│  │ Header: "ZIGBEE2MQTT" (orange)                     │
│  │ ├── Row 1: CPU | Uptime                           │
│  │ │     └── bar-cards avec seuils (74%→75%→90%)     │
│  │ └── Row 2: Memory % | Memory Used                 │
│  │     └── bar-cards avec seuils (74%→75%→80%)       │
│  └────────────────────────────────────────────────────┘
│
│  SECTION 3 : MARIADB
│  ┌────────────────────────────────────────────────────┐
│  │ Header: "MARIADB" (rouge)                          │
│  │ ├── Row 1: CPU | Uptime                           │
│  │ │     └── bar-cards avec seuils (74%→75%→90%)     │
│  │ └── Row 2: Memory % | Memory Used                 │
│  │     └── bar-cards avec seuils (74%→75%→80%)       │
│  └────────────────────────────────────────────────────┘
│
└──────────────────────────────────────────────────────────┘
```

---

## 🖥️ SECTION HOME ASSISTANT

### Header

| Propriété | Valeur |
|-----------|--------|
| Type | `custom:button-card` |
| Icône | `mdi:home-assistant` |
| Couleur icône | RGB(33, 150, 243) — **Primary** |
| Fond | RGBA(33, 150, 243, 0.15) — bleu transparent |
| Bordure gauche | 3px solid RGB(33, 150, 243) |

### Entités

| Métrique | Entité | Type | Unit | Min/Max | Target | Couleurs |
|----------|--------|------|------|---------|--------|----------|
| **CPU Used** | `sensor.homeassistant_utilisation_du_processeur` | NAT | % | 0–100 | 82% | Green(0-74%) → Yellow(75-79%) → Red(90-100%) |
| **Uptime** | `sensor.homeassistant_uptime` | NAT | h | 0–168 | 150h | Orange(0-120h) → Green(120-168h) |
| **Mémoire %** | `sensor.homeassistant_memory_usage_percentage` | NAT | % | 0–100 | 65% | Green(0-74%) → Orange(75-79%) → Red(80-100%) |
| **Mémoire Utilisée** | `sensor.homeassistant_utilisation_de_la_memoire` | NAT | GiB | 0–8.0 | 6 GiB | Red (fixed) |

---

## 🖥️ SECTION ZIGBEE2MQTT

### Header

| Propriété | Valeur |
|-----------|--------|
| Type | `custom:button-card` |
| Icône | `mdi:zigbee` |
| Couleur icône | RGB(255, 152, 0) — **Warning** |
| Fond | RGBA(255, 152, 0, 0.15) — orange transparent |
| Bordure gauche | 3px solid RGB(255, 152, 0) |

### Entités

| Métrique | Entité | Type | Unit | Min/Max | Target | Couleurs |
|----------|--------|------|------|---------|--------|----------|
| **CPU Used** | `sensor.z2m_utilisation_du_processeur` | NAT | % | 0–100 | 82% | Green(0-74%) → Yellow(75-79%) → Red(90-100%) |
| **Uptime** | `sensor.z2m_uptime` | NAT | h | 0–168 | 150h | Orange(0-120h) → Green(120-168h) |
| **Mémoire %** | `sensor.z2m_memory_usage_percentage` | NAT | % | 0–100 | 65% | Green(0-74%) → Orange(75-79%) → Red(80-100%) |
| **Mémoire Utilisée** | `sensor.z2m_utilisation_de_la_memoire` | NAT | MiB | 0–0.5 | 0.35 MiB | Red (fixed) |

---

## 🖥️ SECTION MARIADB

### Header

| Propriété | Valeur |
|-----------|--------|
| Type | `custom:button-card` |
| Icône | `mdi:database` |
| Couleur icône | RGB(244, 67, 54) — **Error** |
| Fond | RGBA(244, 67, 54, 0.15) — rouge transparent |
| Bordure gauche | 3px solid RGB(244, 67, 54) |

### Entités

| Métrique | Entité | Type | Unit | Min/Max | Target | Couleurs |
|----------|--------|------|------|---------|--------|----------|
| **CPU Used** | `sensor.mariadb_utilisation_du_processeur` | NAT | % | 0–100 | 82% | Green(0-74%) → Yellow(75-79%) → Red(90-100%) |
| **Uptime** | `sensor.mariadb_uptime` | NAT | h | 0–168 | 150h | Orange(0-120h) → Green(120-168h) |
| **Mémoire %** | `sensor.mariadb_memory_usage_percentage` | NAT | % | 0–100 | 65% | Green(0-74%) → Orange(75-79%) → Red(80-100%) |
| **Mémoire Utilisée** | `sensor.mariadb_utilisation_de_la_memoire` | NAT | MiB | 0–1.0 | 0.7 MiB | Red (fixed) |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Home Assistant Container

| Entité | Source | Type | Décription |
|--------|--------|------|-----------|
| `sensor.homeassistant_utilisation_du_processeur` | Proxmox VE | NAT | CPU utilisation % du conteneur HA |
| `sensor.homeassistant_uptime` | Proxmox VE | NAT | Uptime du conteneur en heures |
| `sensor.homeassistant_memory_usage_percentage` | Proxmox VE | NAT | Mémoire utilisée en % du total |
| `sensor.homeassistant_utilisation_de_la_memoire` | Proxmox VE | NAT | Mémoire utilisée en GiB (absolu) |

### Zigbee2MQTT Container

| Entité | Source | Type | Décription |
|--------|--------|------|-----------|
| `sensor.z2m_utilisation_du_processeur` | Proxmox VE | NAT | CPU utilisation % du conteneur Z2M |
| `sensor.z2m_uptime` | Proxmox VE | NAT | Uptime du conteneur en heures |
| `sensor.z2m_memory_usage_percentage` | Proxmox VE | NAT | Mémoire utilisée en % du total |
| `sensor.z2m_utilisation_de_la_memoire` | Proxmox VE | NAT | Mémoire utilisée en MiB (absolu) |

### MariaDB Container

| Entité | Source | Type | Décription |
|--------|--------|------|-----------|
| `sensor.mariadb_utilisation_du_processeur` | Proxmox VE | NAT | CPU utilisation % du conteneur MariaDB |
| `sensor.mariadb_uptime` | Proxmox VE | NAT | Uptime du conteneur en heures |
| `sensor.mariadb_memory_usage_percentage` | Proxmox VE | NAT | Mémoire utilisée en % du total |
| `sensor.mariadb_utilisation_de_la_memoire` | Proxmox VE | NAT | Mémoire utilisée en MiB (absolu) |
| `sensor.taille_db_home_assistant` | sql.yaml | NAT | Taille de la base MariaDB en MiB |

---

## 🎨 COULEURS ET SEUILS

### Seuils CPU

- 🟢 **Green** : 0–74% (Normal)
- 🟡 **Yellow** : 75–79% (Attention)
- 🔴 **Red** : 90–100% (Critique)

### Seuils Uptime

- 🟡 **Orange** : 0–120 heures (< 5 jours)
- 🟢 **Green** : 120–168 heures (5–7 jours)

### Seuils Mémoire (%)

- 🟢 **Green** : 0–74% (Normal)
- 🟠 **Orange** : 75–79% (Attention)
- 🔴 **Red** : 80–100% (Critique)

### Mémoire Utilisée (GiB/MiB)

- 🔴 **Red** : Fixed — pas d'animation

---

## 🔧 DÉPANNAGE

### Les bar-cards ne s'affichent pas

- Vérifier que l'intégration **proxmox_ve** est active : Paramètres → Appareils et services → Proxmox VE
- Vérifier que les 6 appareils Proxmox (HA, Z2M, MariaDB containers) sont activés
- Vérifier le nom exact des sensors dans HA : Outils de développement → États

### Les valeurs sont "unavailable"

- Vérifier la connexion Proxmox VE
- Vérifier que les conteneurs sont en cours d'exécution dans Proxmox
- Vérifier les logs du service **proxmox_ve** : Paramètres → Journaux

### Les couleurs ne changent pas

- Vérifier que `card_mod` est installé (HACS → Frontend)
- Vérifier que `bar-card` est à jour (HACS → Frontend)
- Relancer l'interface Home Assistant (F5 ou Ctrl+Shift+R)

---

## 📌 NOTES

- Cette page affiche les métriques **en temps réel** des 3 services principaux
- Les seuils de couleur sont calibrés pour détecter les anomalies (CPU en montée, RAM basse pour chaque service)
- L'Uptime en heures aide à identifier les redémarrages involontaires
- La mémoire utilisée en GiB/MiB est utile pour tracker les fuites mémoire graduelles
