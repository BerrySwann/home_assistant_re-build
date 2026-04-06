<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--21-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/prises` |
| 🔗 **Accès depuis** | Vignette L3C2 (tap) · Heading "PRISES éCO." (retour → `/dashboard-tablette/0`) |
| 🏗️ **Layout** | `type: grid` — 5 sections par pièce |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-21 |
| 🏠 **Version HA** | 2026.3 |

---

# 🔌 L3C2 — Page Prises éCO. (Commandes Éco Prises)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Structure de la page](#structure-de-la-page)
3. [Template card_mod (pattern commun)](#template-cardmod--pattern-commun)
4. [Configuration par carte](#configuration-par-carte)
5. [Bugs identifiés](#bugs-identifiés)
6. [Entités utilisées](#entités-utilisées--provenance-complète)

---

## 🎯 VUE D'ENSEMBLE

Page de commande des **prises éco** par pièce. Chaque prise est représentée par une `custom:mushroom-entity-card` avec un `card_mod` CSS avancé affichant en temps réel la **puissance (W)**, les **ampères (A/mA)** et la **tension (V)** via des badges colorés, une **barre de progression** proportionnelle à la charge max, et une **animation** icône vibrante si la prise consomme.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:mushroom-entity-card` | Commande toggle + badges W/A/V |
| `card_mod` | CSS avancé — badges, progress bar, animation plug |
| `custom:streamline-card` | `template: nav_bar` — barre navigation bas de page |

---

## 🏗️ STRUCTURE DE LA PAGE

```
type: grid
├── Heading "PRISES éCO." → navigate /dashboard-tablette/0
├── [1. ENTRÉE]
│     ├── Heading "Entrée"   (icon: phu:rooms-hallway)
│     └── Prise Eco. Horloge (switch.prise_horloge_ikea)
├── [4. SALON]
│     ├── Heading "Salon"    (icon: mdi:sofa)
│     └── Prise Eco. Salon   (light.hue_smart_eco_salon)
├── [4. SALON — TV]
│     ├── Heading "TV Salon" (icon: cil:tv)              ⚠️ CoreUI icon (dépendance)
│     └── Prise Eco. TV Salon (switch.prise_tv_salon_ikea)
├── [7. BUREAU]
│     ├── Heading "Bureau"   (icon: mdi:desktop-tower-monitor)
│     └── Prise PC Bureau    (switch.hue_smart_eco_pc_bureau)
├── [9. CHAMBRE — TV]
│     ├── Heading "Chambre"  (icon: mdi:bed)
│     └── Prise Eco. TV Chambre (light.hue_smart_eco_tv_chambre)
├── [9. CHAMBRE — Lit]
│     ├── Heading "Tête de Lit" (icon: mdi:bed)
│     └── Prise Eco. Têtes de Lit (switch.prise_tete_de_lit_chambre)
└── custom:streamline-card template: nav_bar
```

---

## 🎨 TEMPLATE CARD_MOD — PATTERN COMMUN

Chaque carte `mushroom-entity-card` utilise le même bloc `card_mod` paramétrable. Les variables à configurer par carte sont en tête de bloc :

```jinja2
/* --- MAIN SETTINGS --- */
{% set max_watts = 2500 %}           {# Puissance max de l'appareil #}
{% set show_ma = false %}            {# true → mA, false → A #}
{% set custom_msg = "MAX: 2500W" %}  {# Texte affiché en bas à droite #}
{% set theme_mode = 'dark' %}        {# 'dark' ou 'light' #}
{% set card_height = '90px' %}       {# Hauteur de la carte #}

/* --- SENSORS --- */
{% set sensor_power =   'sensor.*_power' %}
{% set sensor_voltage = 'sensor.*_voltage' %}
{% set sensor_current = 'sensor.*_current' %}
```

### Logique d'animation (commune)
La vitesse d'animation de l'icône est inversement proportionnelle à la charge : plus la prise tire de watts, plus l'icône vibre vite. Seuil min : `0.4s`, seuil max calculé : `dur = 2.0 - (watts / max_watts * 1.5)`.

### Badges CSS
| Badge | Position | Couleur | Valeur |
|-------|----------|---------|--------|
| Watts (W) | `::after` sur `ha-card` | Orange `rgb(255,152,0)` | `sensor.*_power` |
| Ampères (A/mA) | `::before` sur `ha-card` | Bleu `rgb(33,150,243)` | `sensor.*_current` |
| Volts (V) | `::after` sur `.container` | Vert `rgb(76,175,80)` | `sensor.*_voltage` |

### Barre de progression
`::before` sur `.container` — largeur = `(watts / max_watts * 100)%` — couleur verte, hauteur 4px en bas de carte.

---

## 📋 CONFIGURATION PAR CARTE

| Pièce | Entité (toggle) | Capteurs W/V/A | max_watts | show_ma | Couleur OFF |
|-------|-----------------|----------------|-----------|---------|-------------|
| Entrée — Horloge | `switch.prise_horloge_ikea` | `sensor.prise_horloge_ikea_*` | 2500 | false | *(vert toujours)* |
| Salon | `light.hue_smart_eco_salon` | `sensor.prise_salon_chargeur_nous_*` | 2500 | false | *(vert toujours)* |
| TV Salon | `switch.prise_tv_salon_ikea` | ~~`sensor.light.hue_smart_tv_salon_*`~~ 🐛 | 250 | `ture` ✅ *(voulu — affiche mA)* | *(vert toujours)* |
| Bureau | `switch.hue_smart_eco_pc_bureau` | `sensor.prise_bureau_pc_ikea_*` | 500 | false | **Gris si OFF** ✅ |
| TV Chambre | `light.hue_smart_eco_tv_chambre` | `sensor.prise_tv_chambre_nous_*` | 500 | false | *(vert toujours)* |
| Tête de Lit | `switch.prise_tete_de_lit_chambre` | `sensor.prise_tete_de_lit_chambre_*` | 50 | false | *(vert toujours)* |

> ℹ️ **Bureau uniquement** : implémente la logique `color_plug` conditionnelle (vert si ON / gris si OFF). Les autres cartes sont toujours vertes.

---

## 🐛 BUGS IDENTIFIÉS

### [L1] TV Salon — `show_ma = ture` ✅ Voulu

`ture` est une string non-vide → truthy en Jinja2 → les ampères s'affichent en **mA** pour la TV Salon. C'est intentionnel — la TV Salon tire peu de courant et mA est plus lisible à cette échelle.

---

### [L2] TV Salon — `sensor.light.hue_smart_tv_salon_*` (entity_id invalide)

```jinja2
# AVANT (bug)
{% set sensor_power =   'sensor.light.hue_smart_tv_salon_power' %}
{% set sensor_voltage = 'sensor.light.hue_smart_tv_salon_voltage' %}
{% set sensor_current = 'sensor.light.hue_smart_tv_salon_current' %}

# APRÈS (fix probable)
{% set sensor_power =   'sensor.prise_tv_salon_ikea_power' %}
{% set sensor_voltage = 'sensor.prise_tv_salon_ikea_voltage' %}
{% set sensor_current = 'sensor.prise_tv_salon_ikea_current' %}
```

`sensor.light.hue_smart_tv_salon_*` n'est pas un entity_id HA valide (le domaine `light` ne peut pas être préfixe de `sensor`). Les badges W/A/V afficheront `0 W / 0 A / 0 V` (valeur float(0) de states() = 0).

---

### [L3] Salon — mismatch entité/capteurs (à vérifier)

L'entité togglee est `light.hue_smart_eco_salon` mais les capteurs pointent vers `sensor.prise_salon_chargeur_nous_*`. Si l'éco-prise salon et le chargeur salon sont deux appareils distincts, les valeurs W/A/V affichées ne correspondent pas à l'entité toggleée.

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### Switches / Lights (toggle)

| Entité | Type | Pièce |
|--------|------|-------|
| `switch.prise_horloge_ikea` | IKEA Dirigera | 1. ENTRÉE |
| `light.hue_smart_eco_salon` | Philips Hue | 4. SALON |
| `switch.prise_tv_salon_ikea` | IKEA Dirigera | 4. SALON |
| `switch.hue_smart_eco_pc_bureau` | Philips Hue | 7. BUREAU |
| `light.hue_smart_eco_tv_chambre` | Philips Hue | 9. CHAMBRE |
| `switch.prise_tete_de_lit_chambre` | Intégration native | 9. CHAMBRE |

### Capteurs de mesure (W / V / A)

| Capteur | Source |
|---------|--------|
| `sensor.prise_horloge_ikea_power/voltage/current` | IKEA Dirigera |
| `sensor.prise_salon_chargeur_nous_power/voltage/current` | NOUS (Zigbee) |
| ~~`sensor.light.hue_smart_tv_salon_*`~~ → à corriger | — |
| `sensor.prise_bureau_pc_ikea_power/voltage/current` | IKEA Dirigera |
| `sensor.prise_tv_chambre_nous_power/voltage/current` | NOUS (Zigbee) |
| `sensor.prise_tete_de_lit_chambre_power/voltage/current` | Intégration native |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:mushroom-entity-card` | HACS | ✅ |
| `card_mod` | HACS | ✅ |
| `custom:streamline-card` | HACS | ✅ (template: nav_bar requis) |
| CoreUI Icons (`cil:tv`) | HACS / custom | ⚠️ Dépendance icône TV Salon |

---

## 🔗 FICHIERS LIÉS

- [`L3C2_VIGNETTE_PRISES.md`](./L3C2_VIGNETTE_PRISES.md) — vignette dashboard

---

# annotations_log:
# [L1] show_ma = ture → voulu (mA pour TV Salon — confirmé s14)
# [L2] sensor.light.hue_smart_tv_salon_* → entity_id invalide — corrigé : sensor.prise_tv_salon_ikea_* (confirmé s14)
# [L3] light.hue_smart_eco_salon togglee mais capteurs = prise_salon_chargeur_nous — mismatch à vérifier

← Retour : `L3C1_ECLAIRAGE/` | → Suite : `L3C3_STORES/`
