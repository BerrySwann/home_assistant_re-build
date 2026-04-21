<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-03a9f4?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord_2026-03-*.yaml → Vue: air-quality → section[0]` |
| 🔗 **Accès depuis** | Vignette L6C1 tap → `/dashboard-tablette/air-quality` |
| 🏗️ **Type carte** | `type: grid` (section unique) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3.x |

---

# 🫧 L6C1 — Page : Qualité de l'Air (Appartement)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Structure par pièce](#structure-par-pièce)
4. [Pop-ups graphiques (bubble-card)](#pop-ups-graphiques-bubble-card)
5. [Streamline templates requis](#streamline-templates-requis)
6. [Entités utilisées](#entités-utilisées)
7. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page détaillée de qualité de l'air pour 3 pièces : Salon, Bureau, Chambre. Chaque pièce dispose de deux `ring-tile` (PM2.5 et tCOV) avec marqueur de moyenne 24h, et d'accès à des **pop-ups graphiques** via `bubble-card`.

**Principe :**
- **ring-tile** : valeur instantanée + marqueur moy 24h → vue compacte
- **bubble-card button** → ouvre un pop-up avec graphique historique (streamline template `pm25` / `cov`)
- **3 sections identiques** : Salon → Bureau → Chambre

### Intégrations requises

- ✅ **IKEA Vindstyrka** (Zigbee/Matter) — PM2.5 + VOC index natifs
- ✅ **Templates** — `sensor.tcov_*_ppb` (device_class ppb)
- ✅ **Sensors statistics** — `sensor.pm2_5_*_moy_24h`, `sensor.tcov_*_moy_24h`

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:bubble-card` | Séparateurs sections + pop-ups graphiques + boutons lien pop-up |
| `custom:streamline-card` | Ring-tiles (pm25_ring-tile, cov_ring-tile) + graphiques dans pop-ups (pm25, cov) |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌──────────────────────────────────────────────────────────┐
│  AIR QUALITY (heading)                     tap → /0      │
├──────────────────────────────────────────────────────────┤
│  ══ SALON ══════════════════════════════════════════     │  ← bubble-card separator
│  [ PM2.5 ring-tile   col:6 ]  [ tCOV ring-tile  col:6 ] │  ← 2 × streamline ring-tile
│  [ Graph. PM2.5 Salon ↗  ]   [ Graph. tCOV Salon ↗  ]  │  ← 2 × bubble-card button
│  [pop-up #spm25 — streamline pm25   (hidden)]            │
│  [pop-up #scov  — streamline cov    (hidden)]            │
├──────────────────────────────────────────────────────────┤
│  ══ BUREAU ═════════════════════════════════════════     │
│  [ PM2.5 ring-tile   col:6 ]  [ tCOV ring-tile  col:6 ] │
│  [ Graph. PM2.5 Bureau ↗ ]   [ Graph. tCOV Bureau ↗ ]  │
│  [pop-up #bpm25 — streamline pm25   (hidden)]            │
│  [pop-up #bcov  — streamline cov    (hidden)]            │
├──────────────────────────────────────────────────────────┤
│  ══ CHAMBRE ════════════════════════════════════════     │
│  [ PM2.5 ring-tile   col:6 ]  [ tCOV ring-tile  col:6 ] │
│  [ Graph. PM2.5 Chambre ↗]   [ Graph. tCOV Chambre ↗]  │
│  [pop-up #cpm25 — streamline pm25   (hidden)]            │
│  [pop-up #ccov  — streamline cov    (hidden)]            │
└──────────────────────────────────────────────────────────┘
```

### Hashes pop-up utilisés

| Hash | Contenu | Déclencheur |
|:-----|:--------|:------------|
| `#spm25` | Graphique PM2.5 Salon | bouton "Graph. PM2.5 Salon" |
| `#scov` | Graphique tCOV Salon | bouton "Graph. tCOV Salon" |
| `#bpm25` | Graphique PM2.5 Bureau | bouton "Graph. PM2.5 Bureau" |
| `#bcov` | Graphique tCOV Bureau | bouton "Graph. tCOV Bureau" |
| `#cpm25` | Graphique PM2.5 Chambre | bouton "Graph. PM2.5 Chambre" |
| `#ccov` | Graphique tCOV Chambre | bouton "Graph. tCOV Chambre" |

---

## 📐 STRUCTURE PAR PIÈCE

Chaque section (Salon / Bureau / Chambre) est identique dans sa structure. Exemple pour **Salon** :

### 1. Séparateur de section

```yaml
type: custom:bubble-card
card_type: separator
name: SALON
icon: mdi:sofa        # mdi:desktop-tower-monitor (Bureau) / mdi:bed (Chambre)
rows: 2
styles: |-
  .bubble-line {
    background: var(--primary-text-color);
    opacity: 1;
  }
```

### 2. Ring-tile PM2.5

```yaml
type: custom:streamline-card
template: pm25_ring-tile
variables:
  card_name: PM2.5 du Salon
  entity: sensor.qualite_air_salon_ikea_pm25
  marker2: sensor.pm2_5_salon_moy_24h
grid_options:
  columns: 6
  rows: auto
```

- `entity` : valeur instantanée (µg/m³)
- `marker2` : marqueur moy 24h — positionné sur le ring pour visualiser la tendance

### 3. Ring-tile tCOV

```yaml
type: custom:streamline-card
template: cov_ring-tile
variables:
  card_name: tCOV du Salon
  entity: sensor.tcov_salon_ppb
  marker2: sensor.tcov_salon_moy_24h
grid_options:
  columns: 6
  rows: auto
```

- `entity` : `sensor.tcov_salon_ppb` — template ppb (device_class correct pour ring-tile)
- `marker2` : moy 24h du tCOV brut

### 4. Bouton lien pop-up PM2.5

```yaml
type: custom:bubble-card
card_type: button
button_type: state
entity: sensor.qualite_air_salon_ikea_pm25
name: Graph. PM2.5 Salon
icon: mdi:open-in-new
show_state: true
tap_action:
  action: navigate
  navigation_path: "#spm25"
grid_options:
  columns: 6
  rows: auto
card_mod:
  style: |
    ha-card { margin-top:-30px; }
```

Affiche la valeur instantanée du PM2.5 + icône lien → ouvre le pop-up.

### 5. Bouton lien pop-up tCOV

Identique avec `entity: sensor.tcov_salon_ppb`, `unit: ppb`, `navigation_path: "#scov"`.

### 6. Pop-up PM2.5 (vertical-stack)

```yaml
type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    hash: "#spm25"
    name: Air Quality SALON
    icon: mdi:air-filter
    bg_opacity: "0"
    close_on_click: false
  - type: custom:streamline-card
    template: pm25
    variables:
      entity_sensor: sensor.qualite_air_salon_ikea_pm25
      mean_24h_entity: sensor.pm2_5_salon_moy_24h
```

### 7. Pop-up tCOV (vertical-stack)

```yaml
type: vertical-stack
cards:
  - type: custom:bubble-card
    card_type: pop-up
    hash: "#scov"
    name: Air Quality SALON
    icon: mdi:air-filter
    bg_opacity: "0"
    close_on_click: false
  - type: custom:streamline-card
    template: cov
    variables:
      entity_sensor: sensor.qualite_air_salon_ikea_voc_index
      mean_24h_entity: sensor.tcov_salon_moy_24h
```

> **Note :** Le pop-up tCOV lit `sensor.qualite_air_salon_ikea_voc_index` (VOC index brut) comme `entity_sensor`, tandis que le ring-tile lit `sensor.tcov_salon_ppb`. Les deux templates graphiques (`pm25`, `cov`) utilisent les entités natives pour l'historique.

---

## 🪟 POP-UPS GRAPHIQUES (BUBBLE-CARD)

Les pop-ups sont déclarés dans des `vertical-stack` afin que la `bubble-card pop-up` et la `streamline-card` graphique soient liés. Le pop-up s'ouvre via navigation vers son `hash`.

**Paramètres communs des pop-ups :**

| Paramètre | Valeur | Effet |
|:----------|:-------|:------|
| `bg_opacity: "0"` | Fond transparent | Pop-up flottant sans fond opaque |
| `close_on_click: false` | Non | Ne se ferme pas au clic à l'extérieur |
| `hide_backdrop: false` | Non | Backdrop visible derrière le pop-up |

---

## 📋 STREAMLINE TEMPLATES REQUIS

Cette page nécessite **4 templates Streamline** à déclarer dans la configuration Streamline :

| Template | Variables | Usage |
|:---------|:----------|:------|
| `pm25_ring-tile` | `card_name`, `entity`, `marker2` | Ring-tile PM2.5 avec marqueur 24h |
| `cov_ring-tile` | `card_name`, `entity`, `marker2` | Ring-tile tCOV avec marqueur 24h |
| `pm25` | `entity_sensor`, `mean_24h_entity` | Graphique historique PM2.5 (dans pop-up) |
| `cov` | `entity_sensor`, `mean_24h_entity` | Graphique historique tCOV (dans pop-up) |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Entités natives IKEA Vindstyrka (source primaire)

| Entité | Pièce | Mesure | Intégration |
|:-------|:------|:-------|:------------|
| `sensor.qualite_air_salon_ikea_pm25` | Salon | PM2.5 µg/m³ | IKEA / Zigbee [NAT] |
| `sensor.qualite_air_salon_ikea_voc_index` | Salon | VOC index | IKEA / Zigbee [NAT] |
| `sensor.qualite_air_bureau_ikea_pm25` | Bureau | PM2.5 µg/m³ | IKEA / Zigbee [NAT] |
| `sensor.qualite_air_bureau_ikea_voc_index` | Bureau | VOC index | IKEA / Zigbee [NAT] |
| `sensor.qualite_air_chambre_ikea_pm25` | Chambre | PM2.5 µg/m³ | IKEA / Zigbee [NAT] |
| `sensor.qualite_air_chambre_ikea_voc_index` | Chambre | VOC index | IKEA / Zigbee [NAT] |

### Sensors statistics 24h

Source : `sensors/air_qualite/pm25_tcov_moy_24h.yaml` — `platform: statistics`, `state_characteristic: mean`, `max_age: 24h`

| Entité | unique_id | Source → |
|:-------|:----------|:---------|
| `sensor.pm2_5_salon_moy_24h` | `pm25_salon_mean_24h` | `*_salon_ikea_pm25` |
| `sensor.tcov_salon_moy_24h` | `tcov_salon_mean_24h` | `*_salon_ikea_voc_index` |
| `sensor.pm2_5_bureau_moy_24h` | `pm25_bureau_mean_24h` | `*_bureau_ikea_pm25` |
| `sensor.tcov_bureau_moy_24h` | `tcov_bureau_mean_24h` | `*_bureau_ikea_voc_index` |
| `sensor.pm2_5_chambre_moy_24h` | `pm25_chambre_mean_24h` | `*_chambre_ikea_pm25` |
| `sensor.tcov_chambre_moy_24h` | `tcov_chambre_mean_24h` | `*_chambre_ikea_voc_index` |

### Templates ppb

Source : `templates/air_qualite/tcov_ppb.yaml` — `device_class: volatile_organic_compounds_parts`, `unit: ppb`

| Entité | unique_id | Source → |
|:-------|:----------|:---------|
| `sensor.tcov_salon_ppb` | `tcov_salon_ppb` | `*_salon_ikea_voc_index` |
| `sensor.tcov_bureau_ppb` | `tcov_bureau_ppb` | `*_bureau_ikea_voc_index` |
| `sensor.tcov_chambre_ppb` | `tcov_chambre_ppb` | `*_chambre_ikea_voc_index` |

---

## 🐛 DÉPANNAGE

### Les ring-tiles affichent "unavailable"
→ Vérifier que les capteurs IKEA sont disponibles. Si `sensor.tcov_*_ppb` = unavailable, vérifier que le template `templates/air_qualite/tcov_ppb.yaml` est chargé.

### Le marqueur moy 24h n'apparaît pas sur le ring-tile
→ Les sensors `platform: statistics` ont besoin de 24h de données pour calculer la moyenne. Attendre si les capteurs viennent d'être ajoutés.

### Le pop-up ne s'ouvre pas au clic sur le bouton
→ Vérifier que le `hash` du pop-up (`#spm25`, etc.) correspond exactement à la `navigation_path` du bouton. Un espace ou caractère différent empêche l'ouverture.

### Le pop-up s'ouvre mais le graphique est vide
→ Les templates Streamline `pm25` et `cov` doivent être configurés dans la config Streamline globale. Vérifier leur déclaration.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:bubble-card` | HACS | ✅ Essentiel |
| `custom:streamline-card` | HACS | ✅ Essentiel |
| Templates Streamline : `pm25_ring-tile`, `cov_ring-tile`, `pm25`, `cov` | Streamline config | ✅ Requis × 4 |
| IKEA Vindstyrka × 3 | Zigbee/Matter [NAT] | ✅ Essentiel |
| `sensor.pm2_5_*_moy_24h` × 3 | `platform: statistics` | ✅ Requis |
| `sensor.tcov_*_ppb` × 3 | Template ppb | ✅ Requis |
| `sensor.tcov_*_moy_24h` × 3 | `platform: statistics` | ✅ Requis |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Vignette L6C1 | `docs/L6C1_AIR_QUALITE/L6C1_VIGNETTE_AIR_QUALITE.md` |
| Page YAML | `dashbord/page_air_qualite.yaml` |
| Sensors statistics | `sensors/air_qualite/pm25_tcov_moy_24h.yaml` |
| Templates ppb | `templates/air_qualite/tcov_ppb.yaml` |

---

← Retour : `docs/L6C1_AIR_QUALITE/L6C1_VIGNETTE_AIR_QUALITE.md` | → Suivant : `docs/L6C2_*/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L6C1_VIGNETTE_AIR_QUALITE]]*
