<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20droite-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/phone` (navigation de la vignette L5C2) |
| 🔗 **Accès depuis** | Vignette L5C2 (tap) |
| 🏗️ **Layout** | `type: grid` - 9 cartes de niveau 1 (3 appareils : heading + vertical-stack + entities chacun) |
| 📄 **Fichier YAML** | `L5C2_BATTERIES_PORTABLES/03_page_droite/page_L5C2_batteries_portables_droite.yaml` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 📅 **Modifié le** | 2026-10-11 (MD réécrit à partir du YAML) |

---

# 📱 L5C2 - Page Batteries Portables - DROITE (appareils Mamour)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Appareils affichés](#appareils-affichés)
3. [Différence avec la page gauche](#différence-avec-la-page-gauche)
4. [Entités utilisées](#entités-utilisées)
5. [Code YAML](#code-yaml)
6. [Dépannage](#dépannage)
7. [Points à vérifier](#points-à-vérifier)

---

## 🎯 VUE D'ENSEMBLE

Colonne de droite de la page `/dashboard-tablette/phone`. Elle regroupe les 3 appareils de **Mamour**. Pour chaque appareil : un titre (`heading`, icône `mdi:cellphone-nfc`, tap = retour `/dashboard-tablette/0`), une jauge `custom:streamline-card` (template `portable`) dans un `vertical-stack`, puis une carte `entities` (niveau, état de batterie, type de chargeur, santé, température, type de réseau, connexion Wi-Fi).

La colonne de gauche (appareils d'Eric) est documentée dans [`PAGE_BATTERIES_PORTABLES_GAUCHE.md`](../02_page_gauche/PAGE_BATTERIES_PORTABLES_GAUCHE.md).

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:streamline-card` | Jauge visuelle batterie (template `portable`, défini ailleurs) |
| `card_mod` | Suppression du fond, de l'ombre et de la bordure de la carte `entities` |

---

## Appareils affichés

| Titre dans le YAML | Préfixe des entités | Jauge (variable `entity`) |
|:--|:--|:--|
| Xiaomi POCO X7 Pro Mamour | `sensor.mamour_` | `sensor.mamour_battery_level` |
| Oneplus 10Pro NE2213 (M) | `sensor.ne2213_mamour_` | `sensor.ne2213_mamour_battery_level` |
| Oneplus 7 GM1901 | `sensor.gm1901_` | `sensor.gm1901_battery_level` |

Chaque appareil a les mêmes 7 lignes : `battery_level`, `battery_state`, `charger_type`, `battery_health`, `battery_temperature`, `network_type`, `wi_fi_connection`. Pour le OnePlus NE2213 (M), la ligne `battery_health` porte le nom `Battery health` et `secondary_info: none`.

---

## Différence avec la page gauche

Cette page n'utilise **aucun** `type: conditional` : les cartes de Mamour restent affichées même si l'appareil est hors ligne (valeurs `unavailable` ou `unknown`). C'est la seule différence de structure avec la page gauche.

---

## Entités utilisées

Intégration **Home Assistant Companion App (Android)**, aucune entité à créer dans un fichier YAML. Les 21 entités ci-dessous existent toutes dans HA (vérification en direct le 2026-10-11).

| Appareil | Entités |
|:--|:--|
| POCO X7 Pro (Mamour) | `sensor.mamour_battery_level/state/health/temperature`, `sensor.mamour_charger_type`, `sensor.mamour_network_type`, `sensor.mamour_wi_fi_connection` |
| OnePlus 10 Pro NE2213 (M) | `sensor.ne2213_mamour_battery_level/state/health/temperature`, `sensor.ne2213_mamour_charger_type`, `sensor.ne2213_mamour_network_type`, `sensor.ne2213_mamour_wi_fi_connection` |
| OnePlus 7 GM1901 | `sensor.gm1901_battery_level/state/health/temperature`, `sensor.gm1901_charger_type`, `sensor.gm1901_network_type`, `sensor.gm1901_wi_fi_connection` |

---

## Code YAML

> Copie du fichier `page_L5C2_batteries_portables_droite.yaml` (le fichier YAML fait foi).

```yaml
type: grid
cards:
  - type: heading
    icon: mdi:cellphone-nfc
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
    heading: Xiaomi POCO X7 Pro Mamour
  - type: vertical-stack
    cards:
      - type: custom:streamline-card
        template: portable
        variables:
          entity: sensor.mamour_battery_level
  - type: entities
    entities:
      - entity: sensor.mamour_battery_level
      - entity: sensor.mamour_battery_state
        name: Battery state
      - entity: sensor.mamour_charger_type
        name: Charger type
        secondary_info: none
      - entity: sensor.mamour_battery_health
      - entity: sensor.mamour_battery_temperature
      - entity: sensor.mamour_network_type
      - entity: sensor.mamour_wi_fi_connection
    state_color: true
    show_header_toggle: true
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:cellphone-nfc
    heading: Oneplus 10Pro NE2213 (M)
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: vertical-stack
    cards:
      - type: custom:streamline-card
        template: portable
        variables:
          entity: sensor.ne2213_mamour_battery_level
  - type: entities
    entities:
      - entity: sensor.ne2213_mamour_battery_level
      - entity: sensor.ne2213_mamour_battery_state
        name: Battery state
      - entity: sensor.ne2213_mamour_charger_type
        name: Charger type
        secondary_info: none
      - entity: sensor.ne2213_mamour_battery_health
        name: Battery health
        secondary_info: none
      - entity: sensor.ne2213_mamour_battery_temperature
      - entity: sensor.ne2213_mamour_network_type
      - entity: sensor.ne2213_mamour_wi_fi_connection
    state_color: true
    show_header_toggle: true
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:cellphone-nfc
    heading: Oneplus 7 GM1901
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: vertical-stack
    cards:
      - type: custom:streamline-card
        template: portable
        variables:
          entity: sensor.gm1901_battery_level
  - type: entities
    entities:
      - entity: sensor.gm1901_battery_level
      - entity: sensor.gm1901_battery_state
        name: Battery state
      - entity: sensor.gm1901_charger_type
        name: Charger type
        secondary_info: none
      - entity: sensor.gm1901_battery_health
      - entity: sensor.gm1901_battery_temperature
      - entity: sensor.gm1901_network_type
      - entity: sensor.gm1901_wi_fi_connection
    state_color: true
    show_header_toggle: true
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
```

---

## 🐛 DÉPANNAGE

### Carte Mamour affichée même hors ligne
Comportement normal (pas de `conditional`). Pour aligner sur la page gauche, envelopper chaque bloc (jauge + entities) dans un `type: conditional` avec les conditions `state_not: unavailable` et `state_not: unknown` sur `battery_level`.

### `custom:streamline-card` : template `portable` non trouvé
1. Le template `portable` doit être défini dans la configuration de streamline-card.
2. Vérifier que streamline-card est installé et que le template existe.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| HA Companion App (Android) | Intégration native | ✅ Essentiel |
| `custom:streamline-card` + template `portable` | HACS | ✅ Essentiel |
| `card_mod` | HACS | ✅ Essentiel |

---

## Points à vérifier

- Le 2026-10-11, `sensor.ne2213_mamour_battery_health` et `sensor.ne2213_mamour_battery_temperature` valaient `unknown` (les autres capteurs de cet appareil avaient une valeur). Cause non vérifiée.
- L'ancien MD (`PAGE_BATTERIES_PORTABLES.md`, 2026-04-17) citait `sensor.poco_x7_pro_mamour_*` pour le premier appareil ; le YAML actuel utilise `sensor.mamour_*`. Le MD a été aligné sur le YAML.
- Le template `portable` de streamline-card n'a pas été retrouvé dans ce dossier : son emplacement n'est pas vérifié.

---

## 🔗 FICHIERS LIÉS

- [`PAGE_BATTERIES_PORTABLES_GAUCHE.md`](../02_page_gauche/PAGE_BATTERIES_PORTABLES_GAUCHE.md) - page gauche (appareils Eric)
- [`L5C2_Vignette_BATTERIES_PORTABLES.md`](../01_vignette/L5C2_Vignette_BATTERIES_PORTABLES.md) - vignette résumé

---

← Retour : `L5C1_PILES_BATTERIES/` | → Suivant : `L5C3_MARIADB/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L5C2_Vignette_BATTERIES_PORTABLES]]  [[PAGE_BATTERIES_PORTABLES_GAUCHE]]*
