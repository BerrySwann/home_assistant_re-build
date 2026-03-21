<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/phone` |
| 🔗 **Accès depuis** | Vignette L5C2 (tap) |
| 🏗️ **Layout** | `type: grid` — 2 grilles distinctes (Eric / Mamour) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 📱 L5C2 — Page Batteries Portables

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Grille 1 — Appareils Eric](#grille-1--appareils-eric-conditional)
4. [Grille 2 — Appareils Mamour](#grille-2--appareils-mamour)
5. [Entités utilisées](#entités-utilisées--provenance-complète)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page détaillée par appareil mobile : niveau de batterie, état de charge, type de chargeur, santé, température, réseau et Wi-Fi. Organisée en **2 grilles** : une pour les appareils Eric (avec cartes conditionnelles — masquées si hors ligne), une pour les appareils Mamour (toujours affichées).

### Intégrations requises
- ✅ Home Assistant Companion App (Android) — 7 appareils

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:streamline-card` | Jauge visuelle batterie (template: `portable`) |
| `card_mod` | Suppression bordures sur les entités |

---

## 🏗️ ARCHITECTURE

```
GRILLE 1 — ERIC (conditional: masqué si unavailable/unknown)
┌─────────────────────────────────────────────┐
│  POCO X7 Pro (Eric)                         │
│  ├── streamline-card template: portable     │
│  └── entities: level / state / charger /    │
│      health / temperature / network / wifi  │
├─────────────────────────────────────────────┤
│  OnePlus 10 Pro NE2213 (Eric)              │
│  └── (idem)                                 │
├─────────────────────────────────────────────┤
│  Samsung A8 SM-A530F                        │
│  └── entities: level / state / charger /    │
│      health / temperature                   │
│      (pas network_type / wi_fi_connection)  │
├─────────────────────────────────────────────┤
│  Tablette                                   │
│  └── (idem Samsung)                         │
└─────────────────────────────────────────────┘

GRILLE 2 — MAMOUR (pas de conditional — toujours affichée)
┌─────────────────────────────────────────────┐
│  POCO X7 Pro (Mamour)                       │
│  └── streamline-card + entities complètes   │
├─────────────────────────────────────────────┤
│  OnePlus 10 Pro NE2213 (Mamour)            │
│  └── (idem)                                 │
├─────────────────────────────────────────────┤
│  OnePlus 7 GM1901                           │
│  └── (idem)                                 │
└─────────────────────────────────────────────┘
```

> ⚠️ **Asymétrie** : La grille Eric utilise `type: conditional` (carte masquée si l'appareil est `unavailable` ou `unknown`). La grille Mamour n'utilise **pas** de conditional — les cartes s'affichent même si l'appareil est hors ligne.

---

## 📍 GRILLE 1 — APPAREILS ERIC (conditional)

### Structure conditionnelle (pattern commun)

```yaml
type: conditional
conditions:
  - entity: sensor.<device>_battery_level
    state_not: unavailable
  - entity: sensor.<device>_battery_level
    state_not: unknown
card:
  type: vertical-stack
  cards:
    - type: custom:streamline-card
      template: portable
      variables:
        entity: sensor.<device>_battery_level
    - type: entities
      entities:
        - entity: sensor.<device>_battery_level
        - entity: sensor.<device>_battery_state
          name: Battery state
        - entity: sensor.<device>_charger_type
          name: Charger type
          secondary_info: none
        - entity: sensor.<device>_battery_health
        - entity: sensor.<device>_battery_temperature
        - entity: sensor.<device>_network_type       # POCO / OnePlus uniquement
        - entity: sensor.<device>_wi_fi_connection   # POCO / OnePlus uniquement
      state_color: true
      card_mod:
        style: |
          ha-card { background: none !important; box-shadow: none !important; border: none !important; }
```

### Appareils de la grille 1

| Appareil | Préfixe entité | network/wifi |
|----------|---------------|-------------|
| POCO X7 Pro (Eric) | `sensor.poco_x7_pro_` | ✅ Oui |
| OnePlus 10 Pro NE2213 (Eric) | `sensor.ne2213_eric_` | ✅ Oui |
| Samsung A8 SM-A530F | `sensor.sm_a530f_` | ❌ Non |
| Tablette | `sensor.tablette_` | ❌ Non |

---

## 📍 GRILLE 2 — APPAREILS MAMOUR

### Structure (pas de conditional)

```yaml
type: grid
cards:
  - type: heading
    icon: mdi:cellphone-nfc
    heading: <nom appareil>
    heading_style: title
  - type: vertical-stack
    cards:
      - type: custom:streamline-card
        template: portable
        variables:
          entity: sensor.<device>_battery_level
  - type: entities
    entities:
      - entity: sensor.<device>_battery_level
      - entity: sensor.<device>_battery_state
        name: Battery state
      - entity: sensor.<device>_charger_type
        name: Charger type
        secondary_info: none
      - entity: sensor.<device>_battery_health
      - entity: sensor.<device>_battery_temperature
      - entity: sensor.<device>_network_type
      - entity: sensor.<device>_wi_fi_connection
    state_color: true
    card_mod:
      style: |
        ha-card { background: none !important; box-shadow: none !important; border: none !important; }
```

### Appareils de la grille 2

| Appareil | Préfixe entité |
|----------|---------------|
| POCO X7 Pro (Mamour) | `sensor.poco_x7_pro_mamour_` |
| OnePlus 10 Pro NE2213 (Mamour) | `sensor.ne2213_mamour_` |
| OnePlus 7 GM1901 | `sensor.gm1901_` |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives HA (Android Companion App — aucun fichier YAML)

| Appareil | Entités |
|----------|---------|
| **POCO X7 Pro (Eric)** | `sensor.poco_x7_pro_battery_level/state/charger_type/battery_health/battery_temperature/network_type/wi_fi_connection` |
| **POCO X7 Pro (Mamour)** | `sensor.poco_x7_pro_mamour_battery_level/state/charger_type/battery_health/battery_temperature/network_type/wi_fi_connection` |
| **OnePlus 10 Pro (Eric)** | `sensor.ne2213_eric_battery_level/state/charger_type/battery_health/battery_temperature/network_type/wi_fi_connection` |
| **OnePlus 10 Pro (Mamour)** | `sensor.ne2213_mamour_battery_level/state/charger_type/battery_health/battery_temperature/network_type/wi_fi_connection` |
| **OnePlus 7 GM1901** | `sensor.gm1901_battery_level/state/charger_type/battery_health/battery_temperature/network_type/wi_fi_connection` |
| **Samsung A8 SM-A530F** | `sensor.sm_a530f_battery_level/state/charger_type/battery_health/battery_temperature` |
| **Tablette** | `sensor.tablette_battery_level/state/charger_type/battery_health/battery_temperature` |

---

## 🐛 DÉPANNAGE

### Carte d'un appareil Eric masquée en permanence
1. Vérifier que l'app Companion HA est active sur l'appareil et connectée au serveur HA.
2. L'appareil doit être **sur le même réseau** ou accessible via Nabu Casa pour que les entités passent en `available`.
3. Forcer la synchronisation depuis l'app Companion → Paramètres → Serveur home Assistant → Vérifier la connexion.

### `custom:streamline-card` template `portable` non trouvé
1. Le template `portable` doit être défini dans la configuration streamline-card (probablement dans `configuration.yaml` ou un fichier dédié).
2. Vérifier que streamline-card est installé et que le template `portable` existe bien.

### Carte Mamour affichée même hors ligne
- Comportement normal (pas de conditional sur la grille 2). Pour aligner avec la grille Eric, ajouter un `type: conditional` autour de chaque bloc.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| HA Companion App (Android) — 7 appareils | Intégration native | ✅ Essentiel |
| `custom:streamline-card` + template `portable` | HACS | ✅ Essentiel |
| `card_mod` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Documentation
- [`L5C2_VIGNETTE_BATTERIES_PORTABLES.md`](./L5C2_VIGNETTE_BATTERIES_PORTABLES.md) — vignette résumé

---

← Retour : `L5C1_PILES_BATTERIES/` | → Suivant : `L5C3_MARIADB/`
