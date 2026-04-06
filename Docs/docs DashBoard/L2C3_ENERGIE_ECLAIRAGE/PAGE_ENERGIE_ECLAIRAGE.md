<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--18-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashboard-tablette` → page `/dashboard-tablette/energie-lampes` |
| 🔗 **Accès depuis** | Vignette L2C3 (tap_action navigate) |
| 🏗️ **Layout** | `type: grid` — `column_span: 3` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-18 |
| 🏠 **Version HA** | 2026.3 |

---

# 💡 PAGE — CONSO ÉNERGIE ÉCLAIRAGE (`/dashboard-tablette/energie-lampes`)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [YAML complet](#yaml-complet)
4. [Entités utilisées](#entités-utilisées)
5. [Cartes HACS requises](#cartes-hacs-requises)

---

## 🎯 VUE D'ENSEMBLE

Page de détail de la consommation éclairage par pièce. Accessible depuis la vignette L2C3 via `tap_action: navigate`. Chaque pièce dispose de 3 onglets (tabbed-card) :

- **JOUR** — donut ApexCharts avec diff 24h par ampoule (consommation du jour en cours)
- **MOIS** — donut ApexCharts avec somme mensuelle par ampoule
- **30 JOURS** — graphique colonnes (diff quotidien sur 730h) + ligne moyenne mensuelle

Un badge subtitle sous chaque tabbed-card affiche les 4 périodes Q/H/M/A de la zone.

---

## 🏗️ ARCHITECTURE

```
/dashboard-tablette/energie-lampes
│
├── Heading LAMPES (nav. retour → /home)
├── Séparateur ────────────────────────────
│
├── SALON (5 lampes — rgb(215, 95, 115))
│   ├── Heading title (badges light.salon + light.table)
│   ├── tabbed-card
│   │   ├── JOUR  → donut 5 lampes (sensor.hue_*_quotidien_kwh_um)
│   │   ├── MOIS  → donut 5 lampes (sensor.hue_*_mensuel_kwh_um)
│   │   └── 30J   → colonnes eclairage_salon_5 + AVG mensuel
│   ├── Heading subtitle (badges Q/H/M/A eclairage_salon_5_*)
│   └── Séparateur
│
├── ENTREE - CUISINE - COULOIR (3 lampes — blanc/violet/gris)
│   ├── Heading title (badges light.entree + light.cuisine + light.couloir)
│   ├── tabbed-card
│   │   ├── JOUR  → donut 3 lampes
│   │   ├── MOIS  → donut 3 lampes
│   │   └── 30J   → colonnes eclairage_appart_3 + AVG mensuel
│   ├── Heading subtitle (badges Q/H/M/A eclairage_appart_3_*)
│   └── Séparateur
│
├── BUREAU (5 lampes — rgb(255, 165, 0))
│   ├── Heading title (badges light.bureau x2)
│   ├── tabbed-card
│   │   ├── JOUR  → donut 5 lampes (HUE 1/2 + Play 1/2/3)
│   │   ├── MOIS  → donut 5 lampes
│   │   └── 30J   → colonnes eclairage_bureau_5 + AVG mensuel
│   ├── Heading subtitle (badges Q/H/M/A eclairage_bureau_5_*)
│   └── Séparateur
│
├── SALLE DE BAIN (2 lampes — rgb(3, 155, 229))
│   ├── Heading title (badges light.lampe_sdb + switch.miroir_sonoff)
│   ├── tabbed-card
│   │   ├── JOUR  → donut 2 lampes (Miroir + Hue SDB)
│   │   ├── MOIS  → donut 2 lampes
│   │   └── 30J   → colonnes eclairage_sdb_2 + AVG mensuel
│   ├── Heading subtitle (badges Q/H/M/A eclairage_sdb_2_*)
│   └── Séparateur
│
└── CHAMBRE (4 lampes — rgb(88, 130, 70))
    ├── Heading title (badges light.chambre + light.lit)
    ├── tabbed-card
    │   ├── JOUR  → donut 4 lampes (Eric TL2 + Géraldine TL1 + B1 + B2)
    │   ├── MOIS  → donut 4 lampes
    │   └── 30J   → colonnes eclairage_chambre_4 + AVG mensuel
    └── Heading subtitle (badges Q/H/M/A eclairage_chambre_4_*)
```

---

## 📍 YAML COMPLET

```yaml
type: grid
cards:
  - type: heading
    icon: hue:bulb-group-filament-hung
    heading: LAMPES
    heading_style: title
    badges: []
    tap_action:
      action: navigate
      navigation_path: /dashboard-tablette/home
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: custom:button-card
    styles:
      card:
        - height: 1px
        - background: rgba(255, 255, 255, 1)
        - border: none
        - box-shadow: none
        - border-radius: 0
        - padding: 0
        - margin: 10px

  # ─────────────────────────────────────────
  # SALON
  # ─────────────────────────────────────────
  - type: heading
    icon: mdi:sofa
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.salon
        color: state
        icon: hue:flourish-alt
        tap_action:
          action: more-info
        state_content: state
      - type: entity
        show_state: true
        show_icon: true
        entity: light.table
        color: state
        icon: mdi:ceiling-light
        tap_action:
          action: more-info
    layout_options:
      grid_columns: full
      grid_rows: 1
    heading: SALON
  - type: custom:tabbed-card
    styles:
      "--mdc-theme-primary": rgb(215, 95, 115)
      "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.6)
      max-width: 100%
    attributes:
      animated: true
      swipeable: true
    tabs:
      - attributes:
          label: JOUR
          icon: mdi:weather-sunny
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: day
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: LAMPES SALON CONSO. PAR JOURS
            show_states: true
            colorize_states: true
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_table_quotidien_kwh_um
              name: Table
              color: rgb(174, 68, 90)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_color_candle_salon_1_quotidien_kwh_um
              name: Salon 1C (L1)
              color: rgb(196, 75, 97)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_ambiance_lamp_salon_3_quotidien_kwh_um
              name: Salon 3A (L1)
              color: rgb(215, 95, 115)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_ambiance_lamp_salon_2_quotidien_kwh_um
              name: Salon 2A (B2)
              color: rgb(235, 165, 175)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_ambiance_lamp_salon_1_quotidien_kwh_um
              name: Salon 1A (B1)
              color: rgb(248, 210, 215)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: MOIS
          icon: mdi:calendar-month
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: month
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: LAMPES SALON CONSO. PAR MOIS
            show_states: true
            colorize_states: true
          all_series_config:
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_table_mensuel_kwh_um
              name: Table
              color: rgb(174, 68, 90)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_color_candle_salon_1_mensuel_kwh_um
              name: Salon 1C (L1)
              color: rgb(196, 75, 97)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_ambiance_lamp_salon_3_mensuel_kwh_um
              name: Salon 3A (L1)
              color: rgb(215, 95, 115)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_ambiance_lamp_salon_2_mensuel_kwh_um
              name: Salon 2A (B2)
              color: rgb(235, 165, 175)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_ambiance_lamp_salon_1_mensuel_kwh_um
              name: Salon 1A (B1)
              color: rgb(248, 210, 215)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: 30 JOURS
          icon: mdi:chart-bar
        card:
          type: custom:apexcharts-card
          graph_span: 730h
          span:
            end: day
          apex_config:
            chart:
              height: 500px
          header:
            show: true
            title: Conso. Mensuel Lampes Salon
            show_states: true
            colorize_states: true
          yaxis:
            - id: Watts
              min: 0
              max: auto
              opposite: false
              decimals: 0
              apex_config:
                tickAmount: 4
            - id: Avg
              min: 0
              max: auto
              opposite: true
              decimals: 1
              apex_config:
                tickAmount: 4
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: true
              extremas: true
          series:
            - entity: sensor.eclairage_salon_5_mensuel_kwh_um
              transform: return x * 1000;
              unit: W
              name: Conso. par jours
              yaxis_id: Watts
              color: rgb(215, 95, 115)
              type: column
            - entity: sensor.eclairage_salon_5_avg_watts_mensuel
              yaxis_id: Avg
              type: line
              stroke_dash: 8
              color: red
              unit: W
              stroke_width: 1
              name: Moy. 1er du mois
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:sofa
    heading_style: subtitle
    badges:
      - type: entity
        show_state: true
        show_icon: true
        color: amber
        state_content:
          - name
          - state
        entity: sensor.eclairage_salon_5_quotidien_kwh_um
        name: Q
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_salon_5_hebdomadaire_kwh_um
        name: H
        color: orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_salon_5_mensuel_kwh_um
        name: M
        color: deep-orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_salon_5_annuel_kwh_um
        name: A
        color: red
        state_content:
          - name
          - state
    grid_options:
      columns: 36
      rows: 1
  - type: custom:button-card
    styles:
      card:
        - height: 1px
        - background: rgba(255, 255, 255, 1)
        - border: none
        - box-shadow: none
        - border-radius: 0
        - padding: 0
        - margin: 10px

  # ─────────────────────────────────────────
  # ENTREE - CUISINE - COULOIR
  # ─────────────────────────────────────────
  - type: heading
    icon: mdi:home
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.entree
        color: state
        icon: mdi:ceiling-light
        tap_action:
          action: more-info
      - type: entity
        show_state: true
        show_icon: true
        entity: light.cuisine
        icon: mdi:ceiling-light
        color: state
        tap_action:
          action: more-info
      - type: entity
        show_state: true
        show_icon: true
        entity: light.couloir
        color: state
        icon: mdi:ceiling-light
        tap_action:
          action: more-info
    heading: ENTREE - CUISINE - COULOIR
  - type: custom:tabbed-card
    styles:
      "--mdc-theme-primary": (255, 255, 255)
      "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.6)
      max-width: 100%
    attributes:
      animated: true
      swipeable: true
    tabs:
      - attributes:
          label: JOUR
          icon: mdi:weather-sunny
        card:
          type: custom:apexcharts-card
          chart_type: donut
          span:
            start: day
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: Lampes Entrée - Cuisine - Couloir Conso. / Jrs
            show_states: true
            colorize_states: true
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_entree_quotidien_kwh_um
              name: Entrée
              color: rgb(220, 220, 220)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_cuisine_quotidien_kwh_um
              name: Cuisine
              color: rgb(137, 103, 179)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_couloir_quotidien_kwh_um
              name: Couloir
              color: rgb(150, 150, 150)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: MOIS
          icon: mdi:calendar-month
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: month
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: Lampes Entrée - Cuisine - Couloir Conso. / Mois
            show_states: true
            colorize_states: true
          all_series_config:
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_couloir_mensuel_kwh_um
              name: Couloir
              color: rgb(150, 150, 150)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_cuisine_mensuel_kwh_um
              name: Cuisine
              color: rgb(137, 103, 179)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_entree_mensuel_kwh_um
              name: Entrée
              color: rgb(220, 220, 220)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: 30 JOURS
          icon: mdi:chart-bar
        card:
          type: custom:apexcharts-card
          graph_span: 730h
          span:
            end: day
          apex_config:
            chart:
              height: 500px
          header:
            show: true
            title: Conso. Mensuel Lampes Entrée, Cuisine & Couloir
            show_states: true
            colorize_states: true
          yaxis:
            - id: Watts
              min: 0
              max: auto
              opposite: false
              decimals: 0
              apex_config:
                tickAmount: 4
            - id: Avg
              min: 0
              max: auto
              opposite: true
              decimals: 1
              apex_config:
                tickAmount: 4
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: true
              extremas: true
          series:
            - entity: sensor.eclairage_appart_3_mensuel_kwh_um
              transform: return x * 1000;
              unit: W
              name: Conso. par jours
              yaxis_id: Watts
              color: rgb(118, 93, 160)
              type: column
            - entity: sensor.eclairage_appart_3_avg_watts_mensuel
              yaxis_id: Avg
              type: line
              stroke_dash: 8
              color: red
              unit: W
              stroke_width: 1
              name: Moy. 1er du mois
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:home-lightbulb-outline
    heading_style: subtitle
    badges:
      - type: entity
        show_state: true
        show_icon: true
        color: amber
        state_content:
          - name
          - state
        entity: sensor.eclairage_appart_3_quotidien_kwh_um
        name: Q
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_appart_3_hebdomadaire_kwh_um
        name: H
        color: orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_appart_3_mensuel_kwh_um
        name: M
        color: deep-orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_appart_3_annuel_kwh_um
        name: A
        color: red
        state_content:
          - name
          - state
    grid_options:
      columns: 36
      rows: 1
  - type: custom:button-card
    styles:
      card:
        - height: 1px
        - background: rgba(255, 255, 255, 1)
        - border: none
        - box-shadow: none
        - border-radius: 0
        - padding: 0
        - margin: 10px

  # ─────────────────────────────────────────
  # BUREAU
  # ─────────────────────────────────────────
  - type: heading
    icon: mdi:desktop-tower-monitor
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.bureau
        color: state
        state_content: name
        icon: mdi:desktop-tower-monitor
        name: Pc
        tap_action:
          action: more-info
      - type: entity
        show_state: true
        show_icon: true
        entity: light.bureau
        name: Bureau
        icon: hue:wellner-solid
        color: state
        state_content: name
        tap_action:
          action: more-info
    heading: BUREAU
  - type: custom:tabbed-card
    styles:
      "--mdc-theme-primary": rgb(255, 165, 0)
      "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.6)
      max-width: 100%
    attributes:
      animated: true
      swipeable: true
    tabs:
      - attributes:
          label: JOUR
          icon: mdi:weather-sunny
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: day
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: LAMPES BUREAU CONSO. PAR JOURS
            show_states: true
            colorize_states: true
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_bureau_2_quotidien_kwh_um
              name: Bureau HUE 2
              color: rgb(255, 165, 0)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_bureau_1_quotidien_kwh_um
              name: Bureau HUE 1
              color: rgb(255, 183, 51)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_play_3_pc_bureau_quotidien_kwh_um
              name: play 3
              color: rgb(255, 201, 102)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_play_2_pc_bureau_quotidien_kwh_um
              name: play 2
              color: rgb(255, 219, 153)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_play_1_pc_bureau_quotidien_kwh_um
              name: play 1
              color: rgb(255, 237, 204)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: MOIS
          icon: mdi:calendar-month
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: month
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: LAMPES BUREAU CONSO. PAR MOIS
            show_states: true
            colorize_states: true
          all_series_config:
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_bureau_2_mensuel_kwh_um
              name: Bureau HUE 2
              color: rgb(255, 165, 0)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_bureau_1_mensuel_kwh_um
              name: Bureau HUE 1
              color: rgb(255, 183, 51)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_play_3_pc_bureau_mensuel_kwh_um
              name: play 3
              color: rgb(255, 201, 102)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_play_2_pc_bureau_mensuel_kwh_um
              name: play 2
              color: rgb(255, 219, 153)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_play_1_pc_bureau_mensuel_kwh_um
              name: play 1
              color: rgb(255, 237, 204)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: 30 JOURS
          icon: mdi:chart-bar
        card:
          type: custom:apexcharts-card
          graph_span: 730h
          span:
            end: day
          apex_config:
            chart:
              height: 500px
          header:
            show: true
            title: Conso. mensuel Lampes Bureau
            show_states: true
            colorize_states: true
          yaxis:
            - id: Watts
              min: 0
              max: auto
              opposite: false
              decimals: 0
              apex_config:
                tickAmount: 4
            - id: Avg
              min: 0
              max: auto
              opposite: true
              decimals: 1
              apex_config:
                tickAmount: 4
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: true
              extremas: true
          series:
            - entity: sensor.eclairage_bureau_5_mensuel_kwh_um
              transform: return x * 1000;
              unit: W
              name: Conso. par jours
              yaxis_id: Watts
              color: rgb(255, 165, 0)
              type: column
            - entity: sensor.eclairage_bureau_5_avg_watts_mensuel
              yaxis_id: Avg
              type: line
              stroke_dash: 8
              color: red
              unit: W
              stroke_width: 1
              name: Moy. 1er du mois
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:sofa
    heading_style: subtitle
    badges:
      - type: entity
        show_state: true
        show_icon: true
        color: amber
        state_content:
          - name
          - state
        entity: sensor.eclairage_bureau_5_quotidien_kwh_um
        name: Q
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_bureau_5_hebdomadaire_kwh_um
        name: H
        color: orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_bureau_5_mensuel_kwh_um
        name: M
        color: deep-orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_bureau_5_annuel_kwh_um
        name: A
        color: red
        state_content:
          - name
          - state
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: custom:button-card
    styles:
      card:
        - height: 1px
        - background: rgba(255, 255, 255, 1)
        - border: none
        - box-shadow: none
        - border-radius: 0
        - padding: 0
        - margin: 10px

  # ─────────────────────────────────────────
  # SALLE DE BAIN
  # ─────────────────────────────────────────
  - type: heading
    icon: mdi:shower
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.lampe_salle_de_bain_hue
        color: state
        icon: mdi:ceiling-light
        tap_action:
          action: more-info
      - type: entity
        show_state: true
        show_icon: true
        entity: switch.relais_lumiere_sdb_sonoff
        icon: hue:adore-alt
        color: state
        tap_action:
          action: more-info
    heading: SALLE DE BAIN
  - type: custom:tabbed-card
    styles:
      "--mdc-theme-primary": rgb(3, 155, 229)
      "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.6)
      max-width: 100%
    attributes:
      animated: true
      swipeable: true
    tabs:
      - attributes:
          label: JOUR
          icon: mdi:weather-sunny
        card:
          type: custom:apexcharts-card
          chart_type: donut
          span:
            start: day
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: Lampes Salle de bain Conso. / Jrs
            show_states: true
            colorize_states: true
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.relais_lumiere_sdb_sonoff_quotidien_kwh_um
              name: Miroir
              color: rgb(3, 155, 229)
              transform: return x * 1000;
              unit: W
            - entity: sensor.lampe_salle_de_bain_hue_quotidien_kwh_um
              name: Salle de bain
              color: rgb(119, 210, 235)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: MOIS
          icon: mdi:calendar-month
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: month
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: Lampes Salle de Bain Conso. / Mois
            show_states: true
            colorize_states: true
          all_series_config:
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.relais_lumiere_sdb_sonoff_mensuel_kwh_um
              name: Miroir
              color: rgb(3, 155, 229)
              transform: return x * 1000;
              unit: W
            - entity: sensor.lampe_salle_de_bain_hue_mensuel_kwh_um
              name: Salle de bain
              color: rgb(119, 210, 235)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: 30 JOURS
          icon: mdi:chart-bar
        card:
          type: custom:apexcharts-card
          graph_span: 730h
          span:
            end: day
          apex_config:
            chart:
              height: 500px
          header:
            show: true
            title: Conso. Mensuel Lampes Salle de Bain
            show_states: true
            colorize_states: true
          yaxis:
            - id: Watts
              min: 0
              max: auto
              opposite: false
              decimals: 0
              apex_config:
                tickAmount: 4
            - id: Avg
              min: 0
              max: auto
              opposite: true
              decimals: 1
              apex_config:
                tickAmount: 4
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: true
              extremas: true
          series:
            - entity: sensor.eclairage_sdb_2_mensuel_kwh_um
              transform: return x * 1000;
              unit: W
              name: Conso. par jours
              yaxis_id: Watts
              color: rgb(3, 155, 229)
              type: column
            - entity: sensor.eclairage_sdb_2_avg_watts_mensuel
              yaxis_id: Avg
              type: line
              stroke_dash: 8
              color: red
              unit: W
              stroke_width: 1
              name: Moy. 1er du mois
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:shower
    heading_style: subtitle
    badges:
      - type: entity
        show_state: true
        show_icon: true
        color: amber
        state_content:
          - name
          - state
        entity: sensor.eclairage_sdb_2_quotidien_kwh_um
        name: Q
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_sdb_2_hebdomadaire_kwh_um
        name: H
        color: orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_sdb_2_mensuel_kwh_um
        name: M
        color: deep-orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_sdb_2_annuel_kwh_um
        name: A
        color: red
        state_content:
          - name
          - state
    layout_options:
      grid_columns: full
      grid_rows: 1
  - type: custom:button-card
    styles:
      card:
        - height: 1px
        - background: rgba(255, 255, 255, 1)
        - border: none
        - box-shadow: none
        - border-radius: 0
        - padding: 0
        - margin: 10px

  # ─────────────────────────────────────────
  # CHAMBRE
  # ─────────────────────────────────────────
  - type: heading
    icon: mdi:bed
    heading_style: title
    badges:
      - type: entity
        show_state: true
        show_icon: true
        entity: light.chambre
        color: state
        icon: hue:flourish-alt
        tap_action:
          action: more-info
      - type: entity
        show_state: true
        show_icon: true
        entity: light.lit
        icon: mdi:bed
        color: state
        tap_action:
          action: more-info
    heading: CHAMBRE
  - type: custom:tabbed-card
    styles:
      "--mdc-theme-primary": rgb(88, 130, 70)
      "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.6)
      max-width: 100%
    attributes:
      animated: true
      swipeable: true
    tabs:
      - attributes:
          label: JOUR
          icon: mdi:weather-sunny
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: day
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: LAMPES CHAMBRE CONSO. PAR JOURS
            show_states: true
            colorize_states: true
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_color_candle_chambre_eric_quotidien_kwh_um
              name: Eric (TL2)
              color: rgb(75, 130, 85)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_color_candle_chambre_gege_quotidien_kwh_um
              name: Géraldine (TL1)
              color: rgb(105, 155, 110)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_chambre_2_quotidien_kwh_um
              name: Chambre 2 (B2)
              color: rgb(135, 180, 135)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_chambre_1_quotidien_kwh_um
              name: Chambre 1 (B1)
              color: rgb(165, 205, 160)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: MOIS
          icon: mdi:calendar-month
        card:
          type: custom:apexcharts-card
          chart_type: donut
          cache: true
          span:
            start: month
          apex_config:
            chart:
              height: 700px
          header:
            show: true
            title: LAMPES CHAMBRE CONSO. PAR MOIS
            show_states: true
            colorize_states: true
          all_series_config:
            show:
              legend_value: false
              extremas: false
          show:
            loading: true
            last_updated: false
          series:
            - entity: sensor.hue_white_lamp_chambre_1_mensuel_kwh_um
              name: Chambre 1 (B1)
              color: rgb(165, 205, 160)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_white_lamp_chambre_2_mensuel_kwh_um
              name: Chambre 2 (B2)
              color: rgb(135, 180, 135)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_color_candle_chambre_gege_mensuel_kwh_um
              name: Géraldine (TL1)
              color: rgb(105, 155, 110)
              transform: return x * 1000;
              unit: W
            - entity: sensor.hue_color_candle_chambre_eric_mensuel_kwh_um
              name: Eric (TL2)
              color: rgb(75, 130, 85)
              transform: return x * 1000;
              unit: W
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
      - attributes:
          label: 30 JOURS
          icon: mdi:chart-bar
        card:
          type: custom:apexcharts-card
          graph_span: 730h
          span:
            end: day
          apex_config:
            chart:
              height: 500px
          header:
            show: true
            title: Conso. mensuel Lampes Chambre
            show_states: true
            colorize_states: true
          yaxis:
            - id: Watts
              min: 0
              max: auto
              opposite: false
              decimals: 0
              apex_config:
                tickAmount: 4
            - id: Avg
              min: 0
              max: auto
              opposite: true
              decimals: 1
              apex_config:
                tickAmount: 4
          all_series_config:
            group_by:
              func: diff
              duration: 24h
            show:
              legend_value: true
              extremas: true
          series:
            - entity: sensor.eclairage_chambre_4_mensuel_kwh_um
              transform: return x * 1000;
              unit: W
              name: Conso. par jours
              yaxis_id: Watts
              color: rgb(75, 130, 85)
              type: column
            - entity: sensor.eclairage_chambre_4_avg_watts_mensuel
              yaxis_id: Avg
              type: line
              stroke_dash: 8
              color: red
              unit: W
              stroke_width: 1
              name: Moy. 1er du mois
          card_mod:
            style: |
              ha-card {
                background: none !important;
                box-shadow: none !important;
                border: none !important;
              }
    card_mod:
      style: |
        ha-card {
          background: none !important;
          box-shadow: none !important;
          border: none !important;
        }
  - type: heading
    icon: mdi:bed
    heading_style: subtitle
    badges:
      - type: entity
        show_state: true
        show_icon: true
        color: amber
        state_content:
          - name
          - state
        entity: sensor.eclairage_chambre_4_quotidien_kwh_um
        name: Q
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_chambre_4_hebdomadaire_kwh_um
        name: H
        color: orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_chambre_4_mensuel_kwh_um
        name: M
        color: deep-orange
        state_content:
          - name
          - state
      - type: entity
        show_state: true
        show_icon: true
        entity: sensor.eclairage_chambre_4_annuel_kwh_um
        name: A
        color: red
        state_content:
          - name
          - state
    layout_options:
      grid_columns: full
      grid_rows: 1
column_span: 3
```

---

## 📊 ENTITÉS UTILISÉES

### Lampes individuelles — Utility Meters quotidiens/mensuels

| Pièce | Entité (quotidien `_kwh_um`) | Entité (mensuel `_kwh_um`) |
|-------|------------------------------|----------------------------|
| **Salon — Table** | `sensor.hue_white_lamp_table_quotidien_kwh_um` | `..._mensuel_...` |
| **Salon — Color 1** | `sensor.hue_color_candle_salon_1_quotidien_kwh_um` | `..._mensuel_...` |
| **Salon — Ambiance 3** | `sensor.hue_ambiance_lamp_salon_3_quotidien_kwh_um` | `..._mensuel_...` |
| **Salon — Ambiance 2** | `sensor.hue_ambiance_lamp_salon_2_quotidien_kwh_um` | `..._mensuel_...` |
| **Salon — Ambiance 1** | `sensor.hue_ambiance_lamp_salon_1_quotidien_kwh_um` | `..._mensuel_...` |
| **Entrée** | `sensor.hue_white_lamp_entree_quotidien_kwh_um` | `..._mensuel_...` |
| **Cuisine** | `sensor.hue_white_lamp_cuisine_quotidien_kwh_um` | `..._mensuel_...` |
| **Couloir** | `sensor.hue_white_lamp_couloir_quotidien_kwh_um` | `..._mensuel_...` |
| **Bureau — HUE 1** | `sensor.hue_white_lamp_bureau_1_quotidien_kwh_um` | `..._mensuel_...` |
| **Bureau — HUE 2** | `sensor.hue_white_lamp_bureau_2_quotidien_kwh_um` | `..._mensuel_...` |
| **Bureau — Play 1** | `sensor.hue_play_1_pc_bureau_quotidien_kwh_um` | `..._mensuel_...` |
| **Bureau — Play 2** | `sensor.hue_play_2_pc_bureau_quotidien_kwh_um` | `..._mensuel_...` |
| **Bureau — Play 3** | `sensor.hue_play_3_pc_bureau_quotidien_kwh_um` | `..._mensuel_...` |
| **SDB — Miroir Sonoff** | `sensor.relais_lumiere_sdb_sonoff_quotidien_kwh_um` | `..._mensuel_...` |
| **SDB — Hue** | `sensor.lampe_salle_de_bain_hue_quotidien_kwh_um` | `..._mensuel_...` |
| **Chambre — Eric TL2** | `sensor.hue_color_candle_chambre_eric_quotidien_kwh_um` | `..._mensuel_...` |
| **Chambre — Géraldine TL1** | `sensor.hue_color_candle_chambre_gege_quotidien_kwh_um` | `..._mensuel_...` |
| **Chambre — B1** | `sensor.hue_white_lamp_chambre_1_quotidien_kwh_um` | `..._mensuel_...` |
| **Chambre — B2** | `sensor.hue_white_lamp_chambre_2_quotidien_kwh_um` | `..._mensuel_...` |

> Source : `utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml`

### Zones — Utility Meters Q/H/M/A (badges subtitle)

| Zone | Q/H/M/A |
|------|---------|
| `sensor.eclairage_salon_5_[quotidien/hebdomadaire/mensuel/annuel]_kwh_um` | SALON |
| `sensor.eclairage_appart_3_[...]_kwh_um` | ENTREE + CUISINE + COULOIR |
| `sensor.eclairage_bureau_5_[...]_kwh_um` | BUREAU |
| `sensor.eclairage_sdb_2_[...]_kwh_um` | SALLE DE BAIN |
| `sensor.eclairage_chambre_4_[...]_kwh_um` | CHAMBRE |

> Source : `utility_meter/P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml`

### Moyennes mensuelles — AVG (ligne rouge 30 JOURS)

| Zone | Entité AVG |
|------|-----------|
| Salon | `sensor.eclairage_salon_5_avg_watts_mensuel` |
| Entrée+Cuisine+Couloir | `sensor.eclairage_appart_3_avg_watts_mensuel` |
| Bureau | `sensor.eclairage_bureau_5_avg_watts_mensuel` |
| SDB | `sensor.eclairage_sdb_2_avg_watts_mensuel` |
| Chambre | `sensor.eclairage_chambre_4_avg_watts_mensuel` |

> Source : `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml`

---

## 🃏 CARTES HACS REQUISES

| Carte | Usage |
|-------|-------|
| `custom:tabbed-card` | Onglets JOUR / MOIS / 30 JOURS par pièce |
| `custom:apexcharts-card` | Donuts (JOUR/MOIS) et graphiques colonnes (30 JOURS) |

---

## 🔗 FICHIERS LIÉS

- [`L2C3_VIGNETTE_ECLAIRAGE.md`](./L2C3_VIGNETTE_ECLAIRAGE.md) — Vignette button-card → accès à cette page
- [`docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md) — vue d'ensemble des 18 vignettes
- [`docs/DEPENDANCES_GLOBALES.md`](../DEPENDANCES_GLOBALES.md) — chaîne de dépendances L2C3

---

← Retour : [`L2C3_VIGNETTE_ECLAIRAGE.md`](./L2C3_VIGNETTE_ECLAIRAGE.md) | ← Home : [`PAGE_HOME.md`](../WIFI_PRESENCE%20(Home%20Page)/PAGE_HOME.md)
