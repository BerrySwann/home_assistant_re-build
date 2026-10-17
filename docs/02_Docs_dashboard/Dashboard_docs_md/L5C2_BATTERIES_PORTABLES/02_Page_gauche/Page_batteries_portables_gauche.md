<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20gauche-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/phone` (navigation de la vignette L5C2) |
| 🔗 **Accès depuis** | Vignette L5C2 (tap) |
| 🏗️ **Layout** | `type: grid` - 8 cartes de niveau 1 (4 appareils : 1 heading + 1 conditional chacun) |
| 📄 **Fichier YAML** | `L5C2_14_Batteries_Portables/02_page_gauche/page_L5C2_batteries_portables_gauche.yaml` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 📅 **Modifié le** | 2026-10-11 (MD réécrit à partir du YAML) |

---

# 📱 L5C2 - Page Batteries Portables - GAUCHE (appareils Eric)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Appareils affichés](#appareils-affichés)
3. [Comportement conditionnel](#comportement-conditionnel)
4. [Entités utilisées](#entités-utilisées)
5. [Code YAML](#code-yaml)
6. [Dépannage](#dépannage)
7. [Points à vérifier](#points-à-vérifier)

---

## 🎯 VUE D'ENSEMBLE

Colonne de gauche de la page `/dashboard-tablette/phone`. Elle regroupe les 4 appareils d'**Eric** (POCO X7 Pro, OnePlus 10 Pro NE2213, Samsung A8 SM-A530F, Tablette). Pour chaque appareil : un titre (`heading`, icône `mdi:cellphone-nfc`, tap = retour `/dashboard-tablette/0`), puis un bloc **conditionnel** qui contient :

- une jauge `custom:streamline-card` (template `portable`) alimentée par `sensor.<appareil>_battery_level` ;
- une carte `entities` : niveau, état de batterie, type de chargeur, santé, température, type de réseau, connexion Wi-Fi.

La colonne de droite (appareils de Mamour) est documentée dans [`PAGE_BATTERIES_PORTABLES_DROITE.md`](../03_page_droite/PAGE_BATTERIES_PORTABLES_DROITE.md).

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:streamline-card` | Jauge visuelle batterie (template `portable`, défini ailleurs) |
| `card_mod` | Suppression du fond, de l'ombre et de la bordure de la carte `entities` |

---

## Appareils affichés

| Titre dans le YAML | Préfixe des entités | Entité de condition |
|:--|:--|:--|
| Xiaomi POCO X7 Pro | `sensor.eric_` | `sensor.eric_battery_level` |
| Oneplus 10Pro NE2213 (E) | `sensor.ne2213_eric_` | `sensor.ne2213_eric_battery_level` |
| Samsung A8 SM-A530F | `sensor.sm_a530f_` | `sensor.sm_a530f_battery_level` |
| Tablette | `sensor.tablette_` | `sensor.tablette_battery_level` |

Les 4 appareils ont les mêmes 7 lignes : `battery_level`, `battery_state`, `charger_type`, `battery_health`, `battery_temperature`, `network_type`, `wi_fi_connection`.

Variantes dans le YAML : pour le OnePlus NE2213 (E), les lignes `battery_health` ont un nom explicite (`Battery health`) et `secondary_info: none` ; les lignes `battery_state` et `charger_type` portent les noms `Battery state` et `Charger type` sur tous les appareils.

---

## Comportement conditionnel

Chaque bloc est enveloppé dans un `type: conditional` avec deux conditions sur `battery_level` : `state_not: unavailable` **et** `state_not: unknown`. Si l'appareil est hors ligne, son titre reste affiché mais le bloc batterie disparaît.

> Asymétrie voulue ou non avec la page droite : le côté Mamour n'a **pas** de `conditional` (voir [`PAGE_BATTERIES_PORTABLES_DROITE.md`](../03_page_droite/PAGE_BATTERIES_PORTABLES_DROITE.md)).

---

## Entités utilisées

Intégration **Home Assistant Companion App (Android)**, aucune entité à créer dans un fichier YAML. Les 28 entités ci-dessous existent toutes dans HA (vérification en direct le 2026-10-11).

| Appareil | Entités |
|:--|:--|
| POCO X7 Pro | `sensor.eric_battery_level/state/health/temperature`, `sensor.eric_charger_type`, `sensor.eric_network_type`, `sensor.eric_wi_fi_connection` |
| OnePlus 10 Pro NE2213 (E) | `sensor.ne2213_eric_battery_level/state/health/temperature`, `sensor.ne2213_eric_charger_type`, `sensor.ne2213_eric_network_type`, `sensor.ne2213_eric_wi_fi_connection` |
| Samsung A8 SM-A530F | `sensor.sm_a530f_battery_level/state/health/temperature`, `sensor.sm_a530f_charger_type`, `sensor.sm_a530f_network_type`, `sensor.sm_a530f_wi_fi_connection` |
| Tablette | `sensor.tablette_battery_level/state/health/temperature`, `sensor.tablette_charger_type`, `sensor.tablette_network_type`, `sensor.tablette_wi_fi_connection` |

---

## Code YAML

> Copie du fichier `page_L5C2_batteries_portables_gauche.yaml` (le fichier YAML fait foi).

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
    heading: Xiaomi POCO X7 Pro
  - type: conditional
    conditions:
      - entity: sensor.eric_battery_level
        state_not: unavailable
      - entity: sensor.eric_battery_level
        state_not: unknown
    card:
      type: vertical-stack
      cards:
        - type: custom:streamline-card
          template: portable
          variables:
            entity: sensor.eric_battery_level
        - type: entities
          entities:
            - entity: sensor.eric_battery_level
            - entity: sensor.eric_battery_state
              name: Battery state
            - entity: sensor.eric_charger_type
              name: Charger type
              secondary_info: none
            - entity: sensor.eric_battery_health
            - entity: sensor.eric_battery_temperature
            - entity: sensor.eric_network_type
            - entity: sensor.eric_wi_fi_connection
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
    heading: Oneplus 10Pro NE2213 (E)
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: conditional
    conditions:
      - entity: sensor.ne2213_eric_battery_level
        state_not: unavailable
      - entity: sensor.ne2213_eric_battery_level
        state_not: unknown
    card:
      type: vertical-stack
      cards:
        - type: custom:streamline-card
          template: portable
          variables:
            entity: sensor.ne2213_eric_battery_level
        - type: entities
          entities:
            - entity: sensor.ne2213_eric_battery_level
            - entity: sensor.ne2213_eric_battery_state
              name: Battery state
            - entity: sensor.ne2213_eric_charger_type
              name: Charger type
              secondary_info: none
            - entity: sensor.ne2213_eric_battery_health
              name: Battery health
              secondary_info: none
            - entity: sensor.ne2213_eric_battery_temperature
            - entity: sensor.ne2213_eric_network_type
            - entity: sensor.ne2213_eric_wi_fi_connection
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
    heading: Samsung A8 SM-A530F
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: conditional
    conditions:
      - entity: sensor.sm_a530f_battery_level
        state_not: unavailable
      - entity: sensor.sm_a530f_battery_level
        state_not: unknown
    card:
      type: vertical-stack
      cards:
        - type: custom:streamline-card
          template: portable
          variables:
            entity: sensor.sm_a530f_battery_level
        - type: entities
          entities:
            - entity: sensor.sm_a530f_battery_level
            - entity: sensor.sm_a530f_battery_state
              name: Battery state
            - entity: sensor.sm_a530f_charger_type
              name: Charger type
              secondary_info: none
            - entity: sensor.sm_a530f_battery_health
            - entity: sensor.sm_a530f_battery_temperature
            - entity: sensor.sm_a530f_network_type
            - entity: sensor.sm_a530f_wi_fi_connection
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
    heading: Tablette
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: conditional
    conditions:
      - entity: sensor.tablette_battery_level
        state_not: unavailable
      - entity: sensor.tablette_battery_level
        state_not: unknown
    card:
      type: vertical-stack
      cards:
        - type: custom:streamline-card
          template: portable
          variables:
            entity: sensor.tablette_battery_level
        - type: entities
          entities:
            - entity: sensor.tablette_battery_level
            - entity: sensor.tablette_battery_state
              name: Battery state
            - entity: sensor.tablette_charger_type
              name: Charger type
              secondary_info: none
            - entity: sensor.tablette_battery_health
            - entity: sensor.tablette_battery_temperature
            - entity: sensor.tablette_network_type
            - entity: sensor.tablette_wi_fi_connection
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

### Un appareil d'Eric a son bloc batterie masqué en permanence
1. Vérifier que l'app Companion HA est active sur l'appareil et connectée au serveur HA.
2. L'appareil doit être sur le même réseau ou joignable à distance pour que les entités repassent en `available`.
3. Forcer la synchronisation depuis l'app Companion (Paramètres > Serveur Home Assistant).

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

- L'ancien MD (`PAGE_BATTERIES_PORTABLES.md`, 2026-04-17) citait des entités `sensor.poco_x7_pro_*` et disait que le Samsung et la Tablette n'avaient ni `network_type` ni `wi_fi_connection`. Le YAML actuel utilise `sensor.eric_*` pour le POCO et affiche `network_type` et `wi_fi_connection` pour tous les appareils : le MD a été aligné sur le YAML.
- Le template `portable` de streamline-card n'a pas été retrouvé dans ce dossier : son emplacement n'est pas vérifié.

---

## 🔗 FICHIERS LIÉS

- [`PAGE_BATTERIES_PORTABLES_DROITE.md`](../03_page_droite/PAGE_BATTERIES_PORTABLES_DROITE.md) - page droite (appareils Mamour)
- [`L5C2_VIGNETTE_BATTERIES_PORTABLES.md`](../01_vignette/L5C2_VIGNETTE_BATTERIES_PORTABLES.md) - vignette résumé

---

← Retour : `L5C1_PILES_BATTERIES/` | → Suivant : `L5C3_MARIADB/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L5C2_VIGNETTE_BATTERIES_PORTABLES]]  [[PAGE_BATTERIES_PORTABLES_DROITE]]*
