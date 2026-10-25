<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20gauche-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path dashboard** | `/dashboard-tablette/lumieres` (navigation de la vignette L3C1) |
| 🔗 **Accès depuis** | Vignette L3C1 (tap) |
| 🏗️ **Layout** | `type: grid` - 10 cartes de niveau 1 (1 titre de page + 4 pièces : headings et cartes mushroom) |
| 📄 **Fichier YAML** | `L3C1_ECLAIRAGE/02_page_gauche/page_L3C1_eclairage_gauche.yaml` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 📅 **Modifié le** | 2026-10-11 (MD réécrit à partir du YAML) |

---

# 💡 L3C1 - Page Commandes Lumières - GAUCHE (Entrée, Salon, Cuisine, Couloir)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Pièces](#pièces)
4. [Entités utilisées](#entités-utilisées)
5. [Dépendances critiques](#dépendances-critiques)
6. [Code YAML](#code-yaml)
7. [Points à vérifier](#points-à-vérifier)

---

## 🎯 VUE D'ENSEMBLE

Colonne de gauche de la page `/dashboard-tablette/lumieres` : les pièces **sans popup ni condition** (Entrée, Salon, Cuisine, Couloir). Chaque pièce a un titre (`heading`) avec des badges d'état, et une ou deux cartes `custom:mushroom-entity-card` qui affichent l'état texte de la pièce (`sensor.lumiere_<pièce>_etat`) et allument ou éteignent la lumière au tap (`light.toggle`). Chaque carte contient un bloc `card_mod` "USER CONFIG" (animation flame CSS sur l'icône).

Les pièces à plusieurs circuits (Bureau, Écran, Salle de Bain, Chambre, Têtes de Lit) et les popups sont dans [`PAGE_ECLAIRAGE_DROITE.md`](../03_page_droite/PAGE_ECLAIRAGE_DROITE.md).

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:mushroom-entity-card` | Bouton principal par pièce (état texte + toggle) |
| `card_mod` | Animation flame de l'icône (variables `use_number` et `number_entity` du bloc USER CONFIG) |

---

## 🏗️ ARCHITECTURE

```
type: grid
│
├── [HEADING] LUMIERES - retour (tap → /dashboard-tablette/0), pleine largeur
│
├── [HEADING] Entrée        badge : light.entree
├── [mushroom-entity-card]  sensor.lumiere_entree_etat   → toggle light.entree   (cols 12, rows 2)
│
├── [HEADING] Salon         badges : sensor.th_salon_temperature, cover.store_salon,
│                                    light.salon, light.table
├── [mushroom-entity-card]  sensor.lumiere_salon_etat    → toggle light.salon    (cols 6, rows 2)
├── [mushroom-entity-card]  sensor.lumiere_table_etat    → toggle light.table    (cols 6, rows 2)
│
├── [HEADING] Cuisine       badges : sensor.th_cuisine_temperature, light.cuisine
├── [mushroom-entity-card]  sensor.lumiere_cuisine_etat  → toggle light.cuisine  (cols 12, rows 2)
│
├── [HEADING] Couloir       badge : light.couloir
└── [mushroom-entity-card]  sensor.lumiere_couloir_etat  → toggle light.couloir  (cols 12, rows 2)
```

---

## Pièces

| Pièce | Badges du titre | Carte(s) | Entité d'état | Cible du tap (`light.toggle`) | Largeur |
|:--|:--|:--|:--|:--|:--|
| Entrée | `light.entree` | 1 | `sensor.lumiere_entree_etat` | `light.entree` | 12 colonnes |
| Salon | `sensor.th_salon_temperature` (vert), `cover.store_salon` (tap = more-info), `light.salon`, `light.table` | 2 | `sensor.lumiere_salon_etat`, `sensor.lumiere_table_etat` | `light.salon`, `light.table` | 6 + 6 colonnes |
| Cuisine | `sensor.th_cuisine_temperature` (vert), `light.cuisine` | 1 | `sensor.lumiere_cuisine_etat` | `light.cuisine` | 12 colonnes |
| Couloir | `light.couloir` | 1 | `sensor.lumiere_couloir_etat` | `light.couloir` | 12 colonnes |

Toutes les cartes : `layout: horizontal`, `secondary_info: state`, `icon_color: deep-orange`.

---

## Entités utilisées

Toutes les entités ci-dessous existent dans HA (vérification en direct le 2026-10-11). Au moment du relevé, les 5 lumières sont `off` et les 5 capteurs d'état valent `Éteint`.

| Entité | Source | Rôle |
|:--|:--|:--|
| `light.entree`, `light.couloir`, `light.cuisine`, `light.salon`, `light.table` | Philips Hue (intégration native) | lumières commandées |
| `sensor.lumiere_entree_etat`, `sensor.lumiere_salon_etat`, `sensor.lumiere_table_etat`, `sensor.lumiere_cuisine_etat`, `sensor.lumiere_couloir_etat` | template `templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml` | état texte affiché sur les cartes |
| `sensor.th_salon_temperature`, `sensor.th_cuisine_temperature` | capteurs de température (SONOFF TH selon l'ancien MD, non revérifié) | badges des titres |
| `cover.store_salon` | intégration native | badge état du store salon (valeur `open` le 2026-10-11) |
| `sensor.plug_power` | non vérifié | variable `number_entity` des blocs USER CONFIG (valeur `unknown` le 2026-10-11) ; non utilisée en mode état (`use_number: false`) |

`light.toggle` apparaît dans le YAML comme **service** (action de tap), ce n'est pas une entité.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `sensor.lumiere_*_etat` (5 capteurs de cette page) | template `P3_etats_status.yaml` | ✅ Essentiel |
| `light.*` (5 lumières Hue) | Philips Hue | ✅ Essentiel |
| `custom:mushroom-entity-card` | HACS | ✅ Essentiel |
| `card_mod` | HACS | ✅ Essentiel (animation flame) |

---

## Code YAML

> Copie du fichier `page_L3C1_eclairage_gauche.yaml` (le fichier YAML fait foi).

```yaml
type: grid
cards:
  - type: heading
    icon: hue:bulb-group-classic-3-alt
    heading: LUMIERES
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/0
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: heading
    icon: phu:rooms-hallway
    heading: Entrée
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.entree
        color: state
        name: Entrée
        state_content:
          - name
          - state
        icon: mdi:ceiling-light
  - type: custom:mushroom-entity-card
    entity: sensor.lumiere_entree_etat
    secondary_info: state
    icon_color: deep-orange
    name: Entrée
    tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id:
          - light.entree
    layout: horizontal
    card_mod:
      style:
        mushroom-shape-icon$: |
          .shape {
            {# ========== USER CONFIG ========== #}
            {# true = number mode, false = state mode #}
            {% set use_number      = false %}
            {# STATE MODE SETTINGS #}
            {% set state_entity    = 'light.entree' %}
            {% set active_value    = 'on' %}
            {# OPTIONAL: NUMBER MODE SETTINGS #}
            {% set number_entity   = 'sensor.plug_power' %}
            
            {# '>' '<' '=' '>=' '<=' #}
            {% set number_operator = '>' %}
            
            {% set threshold       = 0.0 %}
            {# ========== END USER CONFIG ====== #}
            {# ----------- TRIGGER LOGIC ----------- #}
            {% if use_number %}
              {% set num = states(number_entity) | float(0) %}
              {% if number_operator == '>' %}
                {% set trigger_active = (num > threshold) %}
              {% elif number_operator == '<' %}
                {% set trigger_active = (num < threshold) %}
              {% elif number_operator == '=' %}
                {% set trigger_active = (num == threshold) %}
              {% elif number_operator == '>=' %}
                {% set trigger_active = (num >= threshold) %}
              {% elif number_operator == '<=' %}
                {% set trigger_active = (num <= threshold) %}
              {% else %}
                {% set trigger_active = false %}
              {% endif %}
            {% else %}
              {% set trigger_active = (states(state_entity) == active_value) %}
            {% endif %}
            {# --------- END TRIGGER LOGIC --------- #}
            {% if trigger_active %}
              --shape-animation: flame-core 1.4s infinite;
              --flame-layer1: flame-layers 1.8s infinite;
              --flame-layer2: ember-pulse 2.4s infinite;
              opacity: 1;
            {% else %}
              --shape-animation: none;
              --flame-layer1: none;
              --flame-layer2: none;
              opacity: 0.6;
            {% endif %}
            position: relative;
            transform-origin: 50% 75%;
          }
          /* Flame layers */
          .shape::before,
          .shape::after {
            content: "";
            position: absolute;
            inset: -8px;
            border-radius: inherit;
            pointer-events: none;
            filter: blur(3px);
          }
          .shape::before {
            animation: var(--flame-layer1);
          }
          .shape::after {
            animation: var(--flame-layer2);
          }
          /* Core flame motion: chaotic vertical flicker + heat ripple */
          @keyframes flame-core {
            0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
            25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
            40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
            55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
            70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
            85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
            100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          }
          /* Outer flame shape: shifting blurred glow */
          @keyframes flame-layers {
            0% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
            33% {
              box-shadow:
                0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                0 -16px 30px -8px rgba(255, 160, 0, 0.5);
            }
            66% {
              box-shadow:
                0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                0 -8px 20px -6px rgba(255, 220, 0, 0.35);
            }
            100% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
          }
          /* Ember pulse: slow breathing glow */
          @keyframes ember-pulse {
            0% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
            50% {
              box-shadow:
                0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                0 0 90px 35px rgba(255, 150, 0, 0.25);
            }
            100% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
          }
        .: |
          mushroom-shape-icon {
            /* On définit les variables directment sur le composant */
            {% if is_state('light.entree', 'on') %}
              --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
              --icon-color: rgb(var(--rgb-deep-orange)) !important;
            {% else %}
              --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
              --icon-color: rgb(var(--rgb-disabled)) !important;
            {% endif %}
            
            --icon-size: 65px;
            display: flex;
            margin: -18px 30px -20px !important;
            padding-right: 20px;
          }
          ha-card {
            clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
            border: 1px solid {% if is_state('light.entree', 'on') %} transparent {% else %} grey {% endif %};
            background-color: {% if is_state('light.entree', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
            height: 120px !important;
            width: auto !important;
          }
    grid_options:
      columns: 12
      rows: 2
  - type: heading
    icon: mdi:sofa
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.th_salon_temperature
        color: green
      - type: entity
        show_state: true
        show_icon: true
        entity: cover.store_salon
        color: state
        tap_action:
          action: more-info
      - type: entity
        show_state: true
        show_icon: true
        entity: light.salon
        icon: hue:flourish-alt
        color: state
        state_content: state
      - type: entity
        show_state: true
        show_icon: true
        entity: light.table
        icon: mdi:ceiling-light
        color: state
        state_content: state
    heading: Salon
  - type: custom:mushroom-entity-card
    entity: sensor.lumiere_salon_etat
    secondary_info: state
    icon_color: deep-orange
    name: Salon
    tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id:
          - light.salon
    layout: horizontal
    card_mod:
      style:
        mushroom-shape-icon$: |
          .shape {
            {# ========== USER CONFIG ========== #}
            {# true = number mode, false = state mode #}
            {% set use_number      = false %}
            {# STATE MODE SETTINGS #}
            {% set state_entity    = 'light.salon' %}
            {% set active_value    = 'on' %}
            {# OPTIONAL: NUMBER MODE SETTINGS #}
            {% set number_entity   = 'sensor.plug_power' %}
            
            {# '>' '<' '=' '>=' '<=' #}
            {% set number_operator = '>' %}
            
            {% set threshold       = 0.0 %}
            {# ========== END USER CONFIG ====== #}
            {# ----------- TRIGGER LOGIC ----------- #}
            {% if use_number %}
              {% set num = states(number_entity) | float(0) %}
              {% if number_operator == '>' %}
                {% set trigger_active = (num > threshold) %}
              {% elif number_operator == '<' %}
                {% set trigger_active = (num < threshold) %}
              {% elif number_operator == '=' %}
                {% set trigger_active = (num == threshold) %}
              {% elif number_operator == '>=' %}
                {% set trigger_active = (num >= threshold) %}
              {% elif number_operator == '<=' %}
                {% set trigger_active = (num <= threshold) %}
              {% else %}
                {% set trigger_active = false %}
              {% endif %}
            {% else %}
              {% set trigger_active = (states(state_entity) == active_value) %}
            {% endif %}
            {# --------- END TRIGGER LOGIC --------- #}
            {% if trigger_active %}
              --shape-animation: flame-core 1.4s infinite;
              --flame-layer1: flame-layers 1.8s infinite;
              --flame-layer2: ember-pulse 2.4s infinite;
              opacity: 1;
            {% else %}
              --shape-animation: none;
              --flame-layer1: none;
              --flame-layer2: none;
              opacity: 0.6;
            {% endif %}
            position: relative;
            transform-origin: 50% 75%;
          }
          /* Flame layers */
          .shape::before,
          .shape::after {
            content: "";
            position: absolute;
            inset: -8px;
            border-radius: inherit;
            pointer-events: none;
            filter: blur(3px);
          }
          .shape::before {
            animation: var(--flame-layer1);
          }
          .shape::after {
            animation: var(--flame-layer2);
          }
          /* Core flame motion: chaotic vertical flicker + heat ripple */
          @keyframes flame-core {
            0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
            25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
            40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
            55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
            70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
            85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
            100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          }
          /* Outer flame shape: shifting blurred glow */
          @keyframes flame-layers {
            0% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
            33% {
              box-shadow:
                0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                0 -16px 30px -8px rgba(255, 160, 0, 0.5);
            }
            66% {
              box-shadow:
                0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                0 -8px 20px -6px rgba(255, 220, 0, 0.35);
            }
            100% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
          }
          /* Ember pulse: slow breathing glow */
          @keyframes ember-pulse {
            0% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
            50% {
              box-shadow:
                0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                0 0 90px 35px rgba(255, 150, 0, 0.25);
            }
            100% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
          }
        .: |
          mushroom-shape-icon {
            /* On définit les variables directment sur le composant */
            {% if is_state('light.salon', 'on') %}
              --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
              --icon-color: rgb(var(--rgb-deep-orange)) !important;
            {% else %}
              --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
              --icon-color: rgb(var(--rgb-disabled)) !important;
            {% endif %}
            
            --icon-size: 65px;
            display: flex;
            margin: -18px 30px -20px !important;
            padding-right: 20px;
          }
          ha-card {
            clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
            border: 1px solid {% if is_state('light.salon', 'on') %} transparent {% else %} grey {% endif %};
            background-color: {% if is_state('light.salon', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
            height: 120px !important;
            width: auto !important;
          }
    grid_options:
      columns: 6
      rows: 2
  - type: custom:mushroom-entity-card
    entity: sensor.lumiere_table_etat
    secondary_info: state
    icon_color: deep-orange
    name: Table
    tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id:
          - light.table
    layout: horizontal
    card_mod:
      style:
        mushroom-shape-icon$: |
          .shape {
            {# ========== USER CONFIG ========== #}
            {# true = number mode, false = state mode #}
            {% set use_number      = false %}
            {# STATE MODE SETTINGS #}
            {% set state_entity    = 'light.table' %}
            {% set active_value    = 'on' %}
            {# OPTIONAL: NUMBER MODE SETTINGS #}
            {% set number_entity   = 'sensor.plug_power' %}
            
            {# '>' '<' '=' '>=' '<=' #}
            {% set number_operator = '>' %}
            
            {% set threshold       = 0.0 %}
            {# ========== END USER CONFIG ====== #}
            {# ----------- TRIGGER LOGIC ----------- #}
            {% if use_number %}
              {% set num = states(number_entity) | float(0) %}
              {% if number_operator == '>' %}
                {% set trigger_active = (num > threshold) %}
              {% elif number_operator == '<' %}
                {% set trigger_active = (num < threshold) %}
              {% elif number_operator == '=' %}
                {% set trigger_active = (num == threshold) %}
              {% elif number_operator == '>=' %}
                {% set trigger_active = (num >= threshold) %}
              {% elif number_operator == '<=' %}
                {% set trigger_active = (num <= threshold) %}
              {% else %}
                {% set trigger_active = false %}
              {% endif %}
            {% else %}
              {% set trigger_active = (states(state_entity) == active_value) %}
            {% endif %}
            {# --------- END TRIGGER LOGIC --------- #}
            {% if trigger_active %}
              --shape-animation: flame-core 1.4s infinite;
              --flame-layer1: flame-layers 1.8s infinite;
              --flame-layer2: ember-pulse 2.4s infinite;
              opacity: 1;
            {% else %}
              --shape-animation: none;
              --flame-layer1: none;
              --flame-layer2: none;
              opacity: 0.6;
            {% endif %}
            position: relative;
            transform-origin: 50% 75%;
          }
          /* Flame layers */
          .shape::before,
          .shape::after {
            content: "";
            position: absolute;
            inset: -8px;
            border-radius: inherit;
            pointer-events: none;
            filter: blur(3px);
          }
          .shape::before {
            animation: var(--flame-layer1);
          }
          .shape::after {
            animation: var(--flame-layer2);
          }
          /* Core flame motion: chaotic vertical flicker + heat ripple */
          @keyframes flame-core {
            0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
            25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
            40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
            55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
            70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
            85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
            100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          }
          /* Outer flame shape: shifting blurred glow */
          @keyframes flame-layers {
            0% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
            33% {
              box-shadow:
                0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                0 -16px 30px -8px rgba(255, 160, 0, 0.5);
            }
            66% {
              box-shadow:
                0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                0 -8px 20px -6px rgba(255, 220, 0, 0.35);
            }
            100% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
          }
          /* Ember pulse: slow breathing glow */
          @keyframes ember-pulse {
            0% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
            50% {
              box-shadow:
                0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                0 0 90px 35px rgba(255, 150, 0, 0.25);
            }
            100% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
          }
        .: |
          mushroom-shape-icon {
            /* On définit les variables directment sur le composant */
            {% if is_state('light.table', 'on') %}
              --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
              --icon-color: rgb(var(--rgb-deep-orange)) !important;
            {% else %}
              --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
              --icon-color: rgb(var(--rgb-disabled)) !important;
            {% endif %}
            
            --icon-size: 65px;
            display: flex;
            margin: -18px 30px -20px !important;
            padding-right: 20px;
          }
          ha-card {
            clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
            border: 1px solid {% if is_state('light.table', 'on') %} transparent {% else %} grey {% endif %};
            background-color: {% if is_state('light.table', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
            height: 120px !important;
            width: auto !important;
          }
    grid_options:
      columns: 6
      rows: 2
  - type: heading
    icon: mdi:fridge
    heading: Cuisine
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.th_cuisine_temperature
        color: green
      - type: entity
        show_state: true
        show_icon: true
        entity: light.cuisine
        color: state
        name: "Cuisine "
        state_content:
          - name
          - state
        icon: mdi:ceiling-light
  - type: custom:mushroom-entity-card
    entity: sensor.lumiere_cuisine_etat
    secondary_info: state
    icon_color: deep-orange
    name: Cuisine
    tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id:
          - light.cuisine
    layout: horizontal
    card_mod:
      style:
        mushroom-shape-icon$: |
          .shape {
            {# ========== USER CONFIG ========== #}
            {# true = number mode, false = state mode #}
            {% set use_number      = false %}
            {# STATE MODE SETTINGS #}
            {% set state_entity    = 'light.cuisine' %}
            {% set active_value    = 'on' %}
            {# OPTIONAL: NUMBER MODE SETTINGS #}
            {% set number_entity   = 'sensor.plug_power' %}
            
            {# '>' '<' '=' '>=' '<=' #}
            {% set number_operator = '>' %}
            
            {% set threshold       = 0.0 %}
            {# ========== END USER CONFIG ====== #}
            {# ----------- TRIGGER LOGIC ----------- #}
            {% if use_number %}
              {% set num = states(number_entity) | float(0) %}
              {% if number_operator == '>' %}
                {% set trigger_active = (num > threshold) %}
              {% elif number_operator == '<' %}
                {% set trigger_active = (num < threshold) %}
              {% elif number_operator == '=' %}
                {% set trigger_active = (num == threshold) %}
              {% elif number_operator == '>=' %}
                {% set trigger_active = (num >= threshold) %}
              {% elif number_operator == '<=' %}
                {% set trigger_active = (num <= threshold) %}
              {% else %}
                {% set trigger_active = false %}
              {% endif %}
            {% else %}
              {% set trigger_active = (states(state_entity) == active_value) %}
            {% endif %}
            {# --------- END TRIGGER LOGIC --------- #}
            {% if trigger_active %}
              --shape-animation: flame-core 1.4s infinite;
              --flame-layer1: flame-layers 1.8s infinite;
              --flame-layer2: ember-pulse 2.4s infinite;
              opacity: 1;
            {% else %}
              --shape-animation: none;
              --flame-layer1: none;
              --flame-layer2: none;
              opacity: 0.6;
            {% endif %}
            position: relative;
            transform-origin: 50% 75%;
          }
          /* Flame layers */
          .shape::before,
          .shape::after {
            content: "";
            position: absolute;
            inset: -8px;
            border-radius: inherit;
            pointer-events: none;
            filter: blur(3px);
          }
          .shape::before {
            animation: var(--flame-layer1);
          }
          .shape::after {
            animation: var(--flame-layer2);
          }
          /* Core flame motion: chaotic vertical flicker + heat ripple */
          @keyframes flame-core {
            0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
            25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
            40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
            55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
            70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
            85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
            100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          }
          /* Outer flame shape: shifting blurred glow */
          @keyframes flame-layers {
            0% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
            33% {
              box-shadow:
                0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                0 -16px 30px -8px rgba(255, 160, 0, 0.5);
            }
            66% {
              box-shadow:
                0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                0 -8px 20px -6px rgba(255, 220, 0, 0.35);
            }
            100% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
          }
          /* Ember pulse: slow breathing glow */
          @keyframes ember-pulse {
            0% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
            50% {
              box-shadow:
                0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                0 0 90px 35px rgba(255, 150, 0, 0.25);
            }
            100% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
          }
        .: |
          mushroom-shape-icon {
            /* On définit les variables directment sur le composant */
            {% if is_state('light.cuisine', 'on') %}
              --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
              --icon-color: rgb(var(--rgb-deep-orange)) !important;
            {% else %}
              --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
              --icon-color: rgb(var(--rgb-disabled)) !important;
            {% endif %}
            
            --icon-size: 65px;
            display: flex;
            margin: -18px 30px -20px !important;
            padding-right: 20px;
          }
          ha-card {
            clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
            border: 1px solid {% if is_state('light.cuisine', 'on') %} transparent {% else %} grey {% endif %};
            background-color: {% if is_state('light.cuisine', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
            height: 120px !important;
            width: auto !important;
          }
    grid_options:
      columns: 12
      rows: 2
  - type: heading
    icon: mdi:home-import-outline
    heading: Couloir
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.couloir
        color: state
        name: Couloir
        state_content:
          - name
          - state
        icon: mdi:ceiling-light
  - type: custom:mushroom-entity-card
    entity: sensor.lumiere_couloir_etat
    secondary_info: state
    icon_color: deep-orange
    name: Couloir
    tap_action:
      action: call-service
      service: light.toggle
      target:
        entity_id:
          - light.couloir
    layout: horizontal
    card_mod:
      style:
        mushroom-shape-icon$: |
          .shape {
            {# ========== USER CONFIG ========== #}
            {# true = number mode, false = state mode #}
            {% set use_number      = false %}
            {# STATE MODE SETTINGS #}
            {% set state_entity    = 'light.couloir' %}
            {% set active_value    = 'on' %}
            {# OPTIONAL: NUMBER MODE SETTINGS #}
            {% set number_entity   = 'sensor.plug_power' %}
            
            {# '>' '<' '=' '>=' '<=' #}
            {% set number_operator = '>' %}
            
            {% set threshold       = 0.0 %}
            {# ========== END USER CONFIG ====== #}
            {# ----------- TRIGGER LOGIC ----------- #}
            {% if use_number %}
              {% set num = states(number_entity) | float(0) %}
              {% if number_operator == '>' %}
                {% set trigger_active = (num > threshold) %}
              {% elif number_operator == '<' %}
                {% set trigger_active = (num < threshold) %}
              {% elif number_operator == '=' %}
                {% set trigger_active = (num == threshold) %}
              {% elif number_operator == '>=' %}
                {% set trigger_active = (num >= threshold) %}
              {% elif number_operator == '<=' %}
                {% set trigger_active = (num <= threshold) %}
              {% else %}
                {% set trigger_active = false %}
              {% endif %}
            {% else %}
              {% set trigger_active = (states(state_entity) == active_value) %}
            {% endif %}
            {# --------- END TRIGGER LOGIC --------- #}
            {% if trigger_active %}
              --shape-animation: flame-core 1.4s infinite;
              --flame-layer1: flame-layers 1.8s infinite;
              --flame-layer2: ember-pulse 2.4s infinite;
              opacity: 1;
            {% else %}
              --shape-animation: none;
              --flame-layer1: none;
              --flame-layer2: none;
              opacity: 0.6;
            {% endif %}
            position: relative;
            transform-origin: 50% 75%;
          }
          /* Flame layers */
          .shape::before,
          .shape::after {
            content: "";
            position: absolute;
            inset: -8px;
            border-radius: inherit;
            pointer-events: none;
            filter: blur(3px);
          }
          .shape::before {
            animation: var(--flame-layer1);
          }
          .shape::after {
            animation: var(--flame-layer2);
          }
          /* Core flame motion: chaotic vertical flicker + heat ripple */
          @keyframes flame-core {
            0%   { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
            12%  { transform: translateY(-2px) scale(1.05);  filter: brightness(1.4) hue-rotate(-10deg); }
            25%  { transform: translateY(1px)  scale(0.98);  filter: brightness(0.9) hue-rotate(8deg); }
            40%  { transform: translateY(-3px) scale(1.07);  filter: brightness(1.5) hue-rotate(-18deg); }
            55%  { transform: translateY(0)    scale(1.02);  filter: brightness(1.2) hue-rotate(10deg); }
            70%  { transform: translateY(-1px) scale(1.04);  filter: brightness(1.35) hue-rotate(-6deg); }
            85%  { transform: translateY(2px)  scale(0.97);  filter: brightness(0.95) hue-rotate(6deg); }
            100% { transform: translateY(0)    scale(1);     filter: brightness(1.1) hue-rotate(0deg); }
          }
          /* Outer flame shape: shifting blurred glow */
          @keyframes flame-layers {
            0% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
            33% {
              box-shadow:
                0 0 20px 10px rgba(var(--rgb-{{ config.icon_color }}), 1),
                0 -16px 30px -8px rgba(255, 160, 0, 0.5);
            }
            66% {
              box-shadow:
                0 0 18px 9px rgba(var(--rgb-{{ config.icon_color }}), 0.9),
                0 -8px 20px -6px rgba(255, 220, 0, 0.35);
            }
            100% {
              box-shadow:
                0 0 14px 8px rgba(var(--rgb-{{ config.icon_color }}), 0.8),
                0 -12px 24px -6px rgba(255, 200, 0, 0.4);
            }
          }
          /* Ember pulse: slow breathing glow */
          @keyframes ember-pulse {
            0% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
            50% {
              box-shadow:
                0 0 50px 18px rgba(var(--rgb-{{ config.icon_color }}), 0.5),
                0 0 90px 35px rgba(255, 150, 0, 0.25);
            }
            100% {
              box-shadow:
                0 0 30px 10px rgba(var(--rgb-{{ config.icon_color }}), 0.25),
                0 0 60px 20px rgba(255, 120, 0, 0.15);
            }
          }
        .: |
          mushroom-shape-icon {
            /* On définit les variables directment sur le composant */
            {% if is_state('light.couloir', 'on') %}
              --shape-color: rgba(var(--rgb-deep-orange), 0.2) !important;
              --icon-color: rgb(var(--rgb-deep-orange)) !important;
            {% else %}
              --shape-color: rgba(var(--rgb-disabled), 0.1) !important;
              --icon-color: rgb(var(--rgb-disabled)) !important;
            {% endif %}
            
            --icon-size: 65px;
            display: flex;
            margin: -18px 30px -20px !important;
            padding-right: 20px;
          }
          ha-card {
            clip-path: inset(0 0 0 0 round var(--ha-card-border-radius, 12px));
            border: 1px solid {% if is_state('light.couloir', 'on') %} transparent {% else %} grey {% endif %};
            background-color: {% if is_state('light.couloir', 'on') %} rgba(255, 160, 0, 0.1) {% else %} transparent {% endif %};
            height: 120px !important;
            width: auto !important;
          }
    grid_options:
      columns: 12
      rows: 2
```

---

## Points à vérifier

- L'ancien MD (`PAGE_ECLAIRAGE.md`, 2026-03-21) ne décrivait pas Entrée, Salon, Cuisine ni Couloir en détail : cette page n'était documentée que par son schéma d'architecture. Le contenu de ce MD vient du YAML.
- Dans l'ancien MD, le fichier de templates était cité `templates/P3_eclairage/ui_dashboard/etats_status.yaml`. Le chemin actuel est `templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml`.
- L'animation flame (CSS dans `card_mod`) n'a pas été vérifiée visuellement.

---

## 🔗 FICHIERS LIÉS

- [`PAGE_ECLAIRAGE_DROITE.md`](../03_page_droite/PAGE_ECLAIRAGE_DROITE.md) - page droite (Bureau, Écran, Salle de Bain, Chambre, Têtes de Lit, popups)
- [`L3C1_Vignette_ECLAIRAGE.md`](../01_vignette/L3C1_Vignette_ECLAIRAGE.md) - vignette d'accès à cette page
- [`PAGE_PRISES.md`](../../L3C2_PRISES/02_page/PAGE_PRISES.md) - page prises (même structure)

---

← Retour : [`L3C1_Vignette_ECLAIRAGE.md`](../01_vignette/L3C1_Vignette_ECLAIRAGE.md) | → Suite : [`L3C2_PRISES/`](../../L3C2_PRISES/)


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L3C1_Vignette_ECLAIRAGE]]  [[PAGE_ECLAIRAGE_DROITE]]*
