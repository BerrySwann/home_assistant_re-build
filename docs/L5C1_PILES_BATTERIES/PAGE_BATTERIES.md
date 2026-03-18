<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--07-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/L5C1_page_batteries.yaml` |
| 🔗 **Accès depuis** | Tap vignette L5C1 → `/dashboard-tablette/battery-bp` |
| 🔗 **Retour vers** | Tap header → `/dashboard-tablette/0` |
| 🏗️ **Layout** | `type: grid` — 5 sections `battery-state-card` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-07 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# 🔋 PAGE BATTERIES — DÉTAIL PAR TYPE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Structure commune](#structure-commune)
4. [Section 1 — Boutons HUE](#section-1--boutons-hue)
5. [Section 2 — Boutons & détecteurs IKEA](#section-2--boutons--détecteurs-ikea)
6. [Section 3 — Contacts fenêtres IKEA](#section-3--contacts-fenêtres-ikea)
7. [Section 4 — Contacts fenêtres SONOFF](#section-4--contacts-fenêtres-sonoff)
8. [Section 5 — Thermostats SONOFF](#section-5--thermostats-sonoff)
9. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page complète listant tous les équipements à batterie, découpée en 5 sections par type/marque. Chaque section affiche un collapse avec le niveau minimum et la plage, triée par niveau croissant. Dégradé rouge → jaune → vert.

### Cartes HACS

| Carte | Usage |
|-------|-------|
| `custom:battery-state-card` | 5 sections indépendantes |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────────┐
│  HEADER — "BATTERIES (Boutons / Thermostats…)"      │
│  tap → /dashboard-tablette/0                        │
├─────────────────────────────────────────────────────┤
│  [1] Boutons HUE              11 entités            │
│      collapse · mdi:light-switch                    │
├─────────────────────────────────────────────────────┤
│  [2] Boutons & détect. IKEA    8 entités            │
│      collapse · mdi:hammer-screwdriver              │
├─────────────────────────────────────────────────────┤
│  [3] Contacts fenêtres IKEA    4 entités            │
│      collapse · mdi:window-closed-variant           │
├─────────────────────────────────────────────────────┤
│  [4] Contacts fenêtres SONOFF  4 entités            │
│      collapse · mdi:window-closed-variant           │
├─────────────────────────────────────────────────────┤
│  [5] Thermostats SONOFF        7 entités            │
│      collapse · mdi:thermometer                     │
└─────────────────────────────────────────────────────┘
```

---

## 📍 STRUCTURE COMMUNE

Chaque section suit le même schéma — seuls le `heading`, l'icône du collapse et la liste d'entités varient.

### Blocs identiques dans les 5 sections

```yaml
secondary_info: "{last_changed}"
colors:
  steps:
    - "#ff0000"
    - "#ffff00"
    - "#00ff00"
  gradient: true
filter:
  exclude:
    - name: entity_id
      value: sensor.ne2213_*
    - name: entity_id
      value: sensor.gm1901_battery_level
    - name: entity_id
      value: sensor.sm_a530f_battery_level
    - name: entity_id
      value: sensor.tablette_battery_level
sort:
  by: state
bulk_rename:
  - from: " Batterie"
  - from: " Battery"
  - from: " level"
  - from: " (HUE)"
  - from: Hue Smart
  - from: button
    to: Bouton
  - from: Th
    to: Thermostat
card_mod:
  style: |
    ha-card {
      background: none !important;
      box-shadow: none !important;
      border: none !important;
    }
```

---

## 📍 SECTION 1 — Boutons HUE

### Collapse
`"Boutons HUE (Total : {count} / Mini. : {min} %)"` · `mdi:light-switch`

### Entités (11) · Philips Hue [bridge natif]

| Entité | Pièce |
|--------|-------|
| `sensor.hue_smart_button_entee_1_batterie` | Entrée 1 |
| `sensor.hue_smart_button_entee_2_batterie` | Entrée 2 |
| `sensor.hue_smart_button_eco_batterie` | Eco |
| `sensor.hue_smart_button_table_batterie` | Table salon |
| `sensor.hue_smart_button_cuisine_batterie` | Cuisine |
| `sensor.hue_smart_button_couloir_batterie` | Couloir |
| `sensor.hue_smart_button_bureau_batterie` | Bureau |
| `sensor.boutton_salle_de_bain_hue_battery` | SDB |
| `sensor.hue_smart_button_chambre_batterie` | Chambre |
| `sensor.hue_smart_button_chambre_gege_batterie` | Chambre Gege |
| `sensor.hue_smart_button_chambre_eric_batterie` | Chambre Eric |

---

## 📍 SECTION 2 — Boutons & détecteurs IKEA

### Collapse
`"Capteurs IKEA (Total : {count} / Mini. : {min} %)"` · `mdi:hammer-screwdriver`

### Entités (8) · Zigbee2MQTT [Z2M]

| Entité | Type |
|--------|------|
| `sensor.inter_tv_chambre_ikea_rodret_battery` | Inter RODRET chambre TV |
| `sensor.inter_bureau_rodret_battery` | Inter RODRET bureau |
| `sensor.inter_somrig_battery` | Inter SOMRIG |
| `sensor.inter_salon_4_ikea_battery` | Inter salon |
| `sensor.detecteur_de_fuite_ikea_battery` | Détecteur de fuite |
| `sensor.detecteur_vallhorn_battery` | Détecteur VALLHORN |
| `sensor.poussoir_ikea_tradfri_battery` | Poussoir TRADFRI |
| `sensor.inter_radiateur_salle_de_bain_ikea_rodret_battery` | Inter radiateur SDB |

---

## 📍 SECTION 3 — Contacts fenêtres IKEA

### Collapse
`"Contacts de fenêtres IKEA (Total : {count} / Mini. : {min} %)"` · `mdi:window-closed-variant`

### Entités (4) · Zigbee2MQTT [Z2M]

| Entité | Pièce |
|--------|-------|
| `sensor.contact_fenetre_salon_ikea_battery` | Salon |
| `sensor.contact_fenetre_cuisine_ikea_battery` | Cuisine |
| `sensor.contact_fenetre_bureau_ikea_battery` | Bureau |
| `sensor.contact_fenetre_chambre_ikea_battery` | Chambre |

---

## 📍 SECTION 4 — Contacts fenêtres SONOFF

### Collapse
`"Contacts de fenêtres SONOFF (Total : {count} / Mini. : {min} %)"` · `mdi:window-closed-variant`

### Entités (4) · Zigbee2MQTT [Z2M]

| Entité | Pièce |
|--------|-------|
| `sensor.contact_fenetre_salon_sonoff_battery` | Salon |
| `sensor.contact_fenetre_cuisine_sonoff_battery` | Cuisine |
| `sensor.contact_fenetre_bureau_sonoff_battery` | Bureau |
| `sensor.contact_fenetre_chambre_sonoff_battery` | Chambre |

---

## 📍 SECTION 5 — Thermostats SONOFF

### Collapse
`"Thermostats SONOFF (Total : {count} / Mini. : {min} %)"` · `mdi:thermometer`

### Entités (7) · Zigbee2MQTT [Z2M]

| Entité | Pièce |
|--------|-------|
| `sensor.th_balcon_nord_battery` | Balcon Nord (T° ext) |
| `sensor.th_salon_battery` | Salon |
| `sensor.th_cellier_battery` | Cellier |
| `sensor.th_cuisine_battery` | Cuisine |
| `sensor.th_bureau_battery` | Bureau |
| `sensor.th_salle_de_bain_battery` | SDB |
| `sensor.th_chambre_battery` | Chambre |

---

## 🐛 DÉPANNAGE

### "Custom element doesn't exist: battery-state-card"
Nom HACS exact : `battery-state-card` (pas `batterie-state-card`). Vider le cache navigateur après installation.

### Une section affiche des appareils d'une autre section
Les `filter/exclude` ne filtrent que les entités exclues — les entités d'une section peuvent apparaître dans une autre si elles ne sont pas dans le collapse. Vérifier que chaque entité est bien listée dans **une seule** section.

---

## 📝 DÉPENDANCES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:battery-state-card` | HACS | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

- `dashbord/L5C1_page_batteries.yaml`
- `docs/L5C1_PILES_BATTERIES/L5C1_VIGNETTE_BATTERIES.md`

---

← Retour : `L5C1_VIGNETTE_BATTERIES.md` | → Suivant : —
