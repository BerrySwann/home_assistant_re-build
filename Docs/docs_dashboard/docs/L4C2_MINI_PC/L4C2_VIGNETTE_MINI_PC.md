<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--05--10-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📍 **Position** | Dashboard HOME — Ligne 4, Colonne 2 |
| 🔗 **Navigation** | `/dashboard-tablette/systeme-mini-pc` |
| 🃏 **Type de carte** | `custom:button-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-05-10 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# 🖥️ VIGNETTE L4C2 : MINI PC

---

## 📋 VUE D'ENSEMBLE

Vignette carrée affichant 5 métriques système du Mini PC Intel NUC en temps réel. L'entité principale est `sensor.temperature_cpu_package` (lecture via `sensors` Linux / command_line). La couleur de l'icône NUC et du champ température change dynamiquement selon les seuils thermiques.

### Design visuel

```
╔══════════════════════════════╗
║  [NUC]🟢      🌡️ 48°C 🟢    ║
║     _____ Mini - P.C. _____  ║
║  🖥️ CPU:  23%                ║
║  ⚡ Power: 11W               ║
║  💾 RAM:  58%                ║
║  💿 SD:   42%                ║
╚══════════════════════════════╝
   ↑ Bordure: 3px double white
   Background: transparent
```

### Grille CSS (`grid-template-areas`)

| Zone | Contenu |
|:-----|:--------|
| `i` | Icône `phu:intel-nuc` — couleur selon T° CPU |
| `temp` | T° CPU + icône thermomètre — couleur seuils |
| `n` | Nom `_____ Mini - P.C. _____` (bold, 13px) |
| `cpu` | CPU % — icône `mdi:server` |
| `conso` | Power W (prise IKEA) — icône `mdi:lightning-bolt-outline` |
| `ram` | RAM % — icône `mdi:memory` |
| `sd` | Disk % — icône `mdi:harddisk` |

---

## 🔧 CODE SOURCE COMPLET

Fichier : `Dashboard/L4C2_Mini_PC/vignette_L4C2_mini_pc_2026-05-10.yaml`

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

| Entité | Type | Fichier source | Rôle dans la vignette |
|:-------|:----:|:--------------|:----------------------|
| `sensor.temperature_cpu_package` | TPL | `templates/Mini-PC/MP_02_sonde_température_mini-pc.yaml` ← MQTT (`sensor.proxmox_cpu_package`) | Entité principale — icône + champ `temp` |
| `sensor.system_monitor_utilisation_du_processeur` | NAT | Intégration `system_monitor` | Champ `cpu` — CPU % |
| `sensor.system_monitor_utilisation_de_la_memoire` | NAT | Intégration `system_monitor` | Champ `ram` — RAM % |
| `sensor.system_monitor_utilisation_du_disque` | NAT | Intégration `system_monitor` | Champ `sd` — Disk % |
| `sensor.prise_mini_pc_ikea_power` | NAT | Zigbee2MQTT (prise IKEA Inspelning) | Champ `conso` — Watts |

---

## 🎨 LOGIQUE JAVASCRIPT — SEUILS COULEUR

### Icône NUC + champ `temp` (T° CPU)

| Plage | Couleur |
|:------|:--------|
| < 65°C | `rgb(70, 175, 75)` — vert |
| 65–74°C | `orange` |
| ≥ 75°C | `rgb(244,67,54)` — rouge |

### Champs `cpu` et `ram` (%)

| Plage | Couleur texte |
|:------|:--------------|
| < 75% | `white` |
| 75–89% | `orange` |
| ≥ 90% | `rgb(244,67,54)` — rouge |

### Champ `conso` (W)

| Plage | Couleur texte |
|:------|:--------------|
| < 15W | `white` |
| 15–18W | `orange` |
| ≥ 19W | `rgb(244,67,54)` — rouge |

> Toutes les icônes dans les `custom_fields` restent en `rgb(70,175,75)` fixe (vert). Seul le texte de la valeur prend la couleur dynamique via `--text-color-sensor`.

---

## 🔄 LOGIQUE DE NAVIGATION

```
USER CLICK
    ↓
tap_action: navigate
    ↓
navigation_path: /dashboard-tablette/systeme-mini-pc
    ↓
OUVERTURE PAGE MINI PC
    ├─ Image + IP locale/externe + Uptime
    ├─ Bar-cards : CPU USED / CPU Temp.
    ├─ Bar-cards : RAM % / USED / FREE
    ├─ Bar-card  : SSD SATA 512Go
    ├─ Bar-cards : Download / Upload (enp6s18)
    ├─ Ring-tile + mini-graph : CPU Utilisation 24h
    ├─ Bar-card  : CPU SPEED (GHz)
    ├─ Bar-cards : Charges système 1m / 5m / 15m
    ├─ Ring-tile + mini-graph : Température CPU 24h
    ├─ Bar-cards : Core 0 / 1 / 2 / 3
    ├─ Bar-card  : Température CPU (résumé)
    ├─ Bar-card  : Température Carte Mère
    ├─ Ring-tile + mini-graph : Conso. W 24h
    ├─ Bar-card  : POWER (résumé)
    ├─ Ring-tile + mini-graph : Mémoire utilisée
    ├─ Bar-card  : MEMORY (résumé)
    └─ Pop-ups : #speed / #temp / #conso / #disk / #memory
```

---

## 🐛 DÉPANNAGE

### L'icône reste grise (`#aaaaaa`)
→ `sensor.temperature_cpu_package` est `unavailable` ou `unknown`. Vérifier le `command_line` dans HA.

### Le champ `temp` affiche N/A
→ Même cause. Vérifier que le sensor est actif : `Outils de dev > États > temperature_cpu_package`.

### Les valeurs CPU/RAM/Disk ne s'actualisent pas
→ Vérifier que `triggers_update` liste bien les 5 entités. Sans `triggers_update`, la vignette ne se rafraîchit que sur changement de l'entité principale.

---

## 📚 FICHIERS LIÉS

- Page : `Dashboard/L4C2_Mini_PC/page_L4C2_mini_pc_2026-05-10.yaml`
- Doc page : `PAGE_MINI_PC.md`
- Sensor T° : `templates/Mini-PC/MP_01_sonde_température_mini-pc.yaml`
- UM prise : `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml`
- AVG prise : `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml`

---

## 📝 HISTORIQUE

| Date | Changement |
|:-----|:-----------|
| 2026-03-25 | Création initiale (migration RPi4 → Mini PC Intel NUC) |
| 2026-05-03 | Documentation mise à jour |
| 2026-05-10 | Refonte complète doc + YAML sauvegardé — entités confirmées sur prod |

---

<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_MINI_PC]]  [[L4C3_VIGNETTE_MAJ]]*
