<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--14-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-03a9f4?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord_2026-03-05.yalm → Vue: energie-mensuel → section[0]` |
| 🔗 **Accès depuis** | `page_energie_home.yaml` → badge tap → `/dashboard-tablette/energie-mensuel` |
| 🏗️ **Type carte** | `type: grid` (section unique, `max_columns: 1`) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-14 |
| 🏠 **Version HA** | 2025.2.x |

---

# 📊 L2C1 — Page : Énergie Mensuelle (Détail Appareils)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Bloc 1 — En-tête](#bloc-1--en-tête)
4. [Bloc 2 — Donut Mensuel](#bloc-2--donut-mensuel)
5. [Blocs 3-7 — Détail Appareils (Streamline)](#blocs-3-7--détail-appareils-streamline)
6. [Template : conso_mensuelle_appareil](#template--conso_mensuelle_appareil)
7. [Palette de couleurs](#palette-de-couleurs)
8. [Entités utilisées](#entités-utilisées)

---

## 🎯 VUE D'ENSEMBLE

Page secondaire accessible depuis `page_energie_home.yaml` via un badge tap action. Elle présente la consommation **mensuelle depuis le début du mois en cours** pour chacun des 17 appareils/prises connectés.

Deux niveaux de lecture :
- **Donut** : vue globale (répartition visuelle en kWh par appareil)
- **Streamline cards** : vue détaillée par appareil (kWh mensuel cumulé + moyenne journalière en W)

Le retour vers la page principale se fait via le tap action du heading.

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌────────────────────────────────────────────────────────┐
│  En-tête : ENERGIE MENSUEL (Start Month)               │  ← tap → /energie
│  (heading, full width)                                  │
├────────────────────────────────────────────────────────┤
│  Donut mensuel (ApexCharts, chart_type: donut)         │  ← 17 séries _mensuel_kwh_um
│  Titre : "Conso. mensuel (kWh)"                        │
│  Hauteur : 580px                                       │
├────────────────────────────────────────────────────────┤
│  ENTRÉE (heading)                                      │
│  • Box Internet (Hue) / Horloge Entrée                 │  ← 2 streamline cards
├────────────────────────────────────────────────────────┤
│  SALON (heading)                                       │
│  • PC's Géraldine / Prise Salon (Chargeurs…)           │  ← 2 streamline cards
├────────────────────────────────────────────────────────┤
│  CUISINE (heading)                                     │
│  • Four M-O / P'tit Dej. / Lave-Linge / Vaisselle     │  ← 8 streamline cards
│  • Airfryer / Four & Plaque / Frigo / Congélateur      │
├────────────────────────────────────────────────────────┤
│  BUREAU (heading)                                      │
│  • PCe Bureau / Fer à Repasser / Têtes de Lit¹         │  ← 3 streamline cards
├────────────────────────────────────────────────────────┤
│  CHAMBRE (heading)                                     │
│  • TV Chambre                                          │  ← 1 streamline card
├────────────────────────────────────────────────────────┤
│  ALL STANDBY (heading)                                 │
│  • Veilles                                             │  ← 1 streamline card
└────────────────────────────────────────────────────────┘
```

> ¹ `Têtes de Lit` est physiquement en chambre mais placé sous le heading `Bureau` dans le YAML.

```yaml
type: grid
cards:
  - type: heading          # En-tête
  - type: custom:apexcharts-card   # Donut mensuel
  - type: heading          # ENTRÉE
  - type: custom:streamline-card   # × 2
  - type: heading          # SALON
  - type: custom:streamline-card   # × 2
  - type: heading          # CUISINE
  - type: custom:streamline-card   # × 8
  - type: heading          # BUREAU
  - type: custom:streamline-card   # × 3
  - type: heading          # CHAMBRE
  - type: custom:streamline-card   # × 1
  - type: heading          # ALL STANDBY
  - type: custom:streamline-card   # × 1
```

**Total cartes : 24** (1 donut + 5 headings + 18 streamline)

---

## 📌 BLOC 1 — EN-TÊTE

```yaml
- type: heading
  icon: mdi:transmission-tower
  heading: ENERGIE MENSUEL (Start Month)
  heading_style: title
  badges: []
  tap_action:
    action: navigate
    navigation_path: /dashboard-tablette/energie
  layout_options:
    grid_columns: full
    grid_rows: 1
```

- **Tap action** : retour vers `/dashboard-tablette/energie` (page principale énergie)
- **`badges: []`** : aucun badge sur ce heading (contrairement à la page principale)
- **"Start Month"** : précise que la fenêtre de mesure commence au 1er du mois courant

---

## 🍩 BLOC 2 — DONUT MENSUEL

```yaml
- type: custom:apexcharts-card
  chart_type: donut
  cache: true
  apex_config:
    chart:
      height: 580px
  header:
    show: true
    title: Conso. mensuel (kWh)
    show_states: true
    colorize_states: true
  all_series_config:
    show:
      legend_value: false
      extremas: false
  show:
    loading: true
    last_updated: false
```

### Données des séries

Chaque série pointe vers un `_mensuel_kwh_um` — compteur `utility_meter` réinitialisé le 1er du mois (`cycle: monthly`). La valeur affichée est donc la consommation **cumulée depuis le début du mois courant**.

> ⚠️ Pas de `group_by` / `func` ici : ApexCharts lit directement l'état courant du sensor (valeur accumulée par `utility_meter`).

| Nom affiché | Entité sensor | Couleur |
|:------------|:--------------|:--------|
| Box (+) | `sensor.prise_box_internet_ikea_mensuel_kwh_um` | `gainsboro` |
| Horloge (+) | `sensor.prise_horloge_ikea_mensuel_kwh_um` | `rgb(183,183,183)` |
| PCg | `sensor.prise_pc_s_gege_ikea_mensuel_kwh_um` | `rgb(202,135,135)` |
| Chargeurs (+) | `sensor.prise_salon_chargeur_nous_mensuel_kwh_um` | `rgb(174,68,90)` |
| Four M-O (+) | `sensor.prise_four_micro_ondes_nous_mensuel_kwh_um` | `rgb(98,78,136)` |
| P'tit Dej. (+) | `sensor.prise_petit_dejeune_nous_mensuel_kwh_um` | `rgb(118,93,160)` |
| Linge | `sensor.prise_lave_linge_nous_mensuel_kwh_um` | `rgb(137,103,179)` |
| Vaisselle | `sensor.prise_lave_vaisselle_nous_mensuel_kwh_um` | `rgb(129,116,180)` |
| Airfryer (+) | `sensor.prise_airfryer_ninja_nous_mensuel_kwh_um` | `rgb(142,122,181)` |
| Four & Plq Cui. | `sensor.four_et_plaque_de_cuisson_mensuel_kwh_um` | `rgb(162,148,249)` |
| frigo | `sensor.prise_frigo_cuisine_nous_mensuel_kwh_um` | `cyan` |
| congél. | `sensor.prise_congelateur_cuisine_nous_mensuel_kwh_um` | `rgb(19,160,255)` |
| PCe | `sensor.prise_bureau_pc_ikea_mensuel_kwh_um` | `orange` |
| FàR (+) | `sensor.prise_bureau_fer_a_repasser_nous_mensuel_kwh_um` | `gold` |
| Têtes L. (+) | `sensor.prise_tete_de_lit_chambre_mensuel_kwh_um` | `rgb(177,194,158)` |
| TV Salon | `sensor.prise_tv_salon_ikea_mensuel_kwh_um` | `rgb(215,95,115)` |
| TV (+) | `sensor.prise_tv_chambre_nous_mensuel_kwh_um` | `rgb(30,81,40)` |
| Veilles | `sensor.all_standby_mensuel_kwh_um` | `grey` |

> **(+)** : appareils à consommation irrégulière / intermittente.

### Style carte

```yaml
card_mod:
  style: |
    ha-card {
      background: none !important;
      box-shadow: none !important;
      border: none !important;
    }
```

---

## 📱 BLOCS 3-7 — DÉTAIL APPAREILS (STREAMLINE)

Chaque appareil est représenté par une `custom:streamline-card` avec le template `conso_mensuelle_appareil`.

### Récapitulatif par section

#### 1. ENTRÉE (2 appareils)

| Title | energy_entity | color | avg_monthly | conso_monthly_kwh |
|:------|:-------------|:------|:-----------|:-----------------|
| Box Internet (Hue) | `sensor.prise_box_internet_ikea_energie_totale_kwh` | `gainsboro` | `sensor.box_internet_avg_watts_mensuel` | `sensor.prise_box_internet_ikea_mensuel_kwh_um` |
| Horloge Entrée (Chargeur) | `sensor.prise_horloge_ikea_energie_totale_kwh` | `rgb(183,183,183)` | `sensor.horloge_avg_watts_mensuel` | `sensor.prise_horloge_ikea_mensuel_kwh_um` |

#### 2. SALON (3 appareils)

| Title | energy_entity | color | avg_monthly | conso_monthly_kwh |
|:------|:-------------|:------|:-----------|:-----------------|
| PC's Géraldine | `sensor.prise_pc_s_gege_ikea_energie_totale_kwh` | `rgb(202,135,135)` | `sensor.pc_gege_avg_watts_mensuel` | `sensor.prise_pc_s_gege_ikea_mensuel_kwh_um` |
| Prise Salon (Chargeurs, Vapote, Aspi. & iRobot) | `sensor.prise_salon_chargeur_nous_energie_totale_kwh` | `rgb(174,68,90)` | `sensor.chargeurs_salon_avg_watts_mensuel` | `sensor.prise_salon_chargeur_nous_mensuel_kwh_um` |
| TV Salon (TV, Barre de son, ect...) | `sensor.prise_tv_salon_ikea_energie_totale_kwh` | `rgb(215,95,115)` | `sensor.tv_salon_avg_watts_mensuel` | `sensor.prise_tv_salon_ikea_mensuel_kwh_um` |

#### 3. CUISINE (8 appareils)

| Title | energy_entity | color | avg_monthly | conso_monthly_kwh |
|:------|:-------------|:------|:-----------|:-----------------|
| Four Micro-Ondes (Alexa) | `sensor.prise_four_micro_ondes_nous_energie_totale_kwh` | `rgb(98,78,136)` | `sensor.four_mo_avg_watts_mensuel` | `sensor.prise_four_micro_ondes_nous_mensuel_kwh_um` |
| P'tit Dej. (grille pain, Théière, machine à café) | `sensor.prise_petit_dejeune_nous_energie_totale_kwh` | `rgb(118,93,160)` | `sensor.petit_dej_avg_watts_mensuel` | `sensor.prise_petit_dejeune_nous_mensuel_kwh_um` |
| Lave-Linge | `sensor.prise_lave_linge_nous_energie_totale_kwh` | `rgb(137,103,179)` | `sensor.lave_linge_avg_watts_mensuel` | `sensor.prise_lave_linge_nous_mensuel_kwh_um` |
| Lave-Vaisselle | `sensor.prise_lave_vaisselle_nous_energie_totale_kwh` | `rgb(129,116,180)` | `sensor.lave_vaisselle_avg_watts_mensuel` | `sensor.prise_lave_vaisselle_nous_mensuel_kwh_um` |
| Airfryer (Cookéo, mixer, ect...) | `sensor.prise_airfryer_ninja_nous_energie_totale_kwh` | `rgb(142,122,181)` | `sensor.airfryer_avg_watts_mensuel` | `sensor.prise_airfryer_ninja_nous_mensuel_kwh_um` |
| Four et plaque de Cuisson | `sensor.four_et_plaque_de_cuisson_energie_totale_kwh` | `rgb(162,148,249)` | `sensor.plaques_cuisson_avg_watts_mensuel` | `sensor.four_et_plaque_de_cuisson_mensuel_kwh_um` |
| Frigo | `sensor.prise_frigo_cuisine_nous_energie_totale_kwh` | `cyan` | `sensor.frigo_avg_watts_mensuel` | `sensor.prise_frigo_cuisine_nous_mensuel_kwh_um` |
| Congélateur | `sensor.prise_congelateur_cuisine_nous_energie_totale_kwh` | `rgb(19,160,255)` | `sensor.congelateur_avg_watts_mensuel` | `sensor.prise_congelateur_cuisine_nous_mensuel_kwh_um` |

#### 4. BUREAU (2 appareils + 1 chambre¹)

| Title | energy_entity | color | avg_monthly | conso_monthly_kwh |
|:------|:-------------|:------|:-----------|:-----------------|
| PCe Bureau | `sensor.prise_bureau_pc_ikea_energie_totale_kwh` | `orange` | `sensor.pc_bureau_avg_watts_mensuel` | `sensor.prise_bureau_pc_ikea_mensuel_kwh_um` |
| Fer à Repasser Bureau (Store) | `sensor.prise_bureau_fer_a_repasser_nous_energie_totale_kwh` | `gold` | `sensor.fer_repasser_avg_watts_mensuel` | `sensor.prise_bureau_fer_a_repasser_nous_mensuel_kwh_um` |
| Têtes de Lit chambre¹ | `sensor.prise_tete_de_lit_chambre_energie_totale_kwh` | `rgb(177,194,158)` | `sensor.tetes_lit_avg_watts_mensuel` | `sensor.prise_tete_de_lit_chambre_mensuel_kwh_um` |

#### 5. CHAMBRE (1 appareil)

| Title | energy_entity | color | avg_monthly | conso_monthly_kwh |
|:------|:-------------|:------|:-----------|:-----------------|
| TV Chambre (Casques, FireTV, ect...) | `sensor.prise_tv_chambre_nous_energie_totale_kwh` | `rgb(30,81,40)` | `sensor.tv_chambre_avg_watts_mensuel` | `sensor.prise_tv_chambre_nous_mensuel_kwh_um` |

#### 6. ALL STANDBY (1 appareil)

| Title | energy_entity | color | avg_monthly | conso_monthly_kwh |
|:------|:-------------|:------|:-----------|:-----------------|
| Veilles | `sensor.all_standby_energie_totale_kwh` | `grey` | `sensor.veilles_avg_watts_mensuel` | `sensor.all_standby_mensuel_kwh_um` |

> ¹ `Têtes de Lit chambre` est positionné sous le heading `Bureau` dans le YAML (ordre d'insertion). Physiquement en chambre.

---

## 🔧 TEMPLATE : conso_mensuelle_appareil

Le template `conso_mensuelle_appareil` est le pendant mensuel de `conso_temps_reel_appareil` (utilisé dans `page_energie_temps_reel.yaml`). Il affiche les métriques sur la **fenêtre mensuelle** plutôt que journalière.

### Variables (5)

| Variable | Type | Description |
|:---------|:-----|:------------|
| `title` | string | Nom affiché de l'appareil |
| `energy_entity` | sensor | Énergie totale cumulée (kWh) — `_energie_totale_kwh` |
| `color` | color | Couleur identique au segment donut correspondant |
| `avg_monthly_entity` | sensor | Puissance moyenne mensuelle (W) — `_avg_watts_mensuel` |
| `conso_monthly_kwh_entity` | sensor | Consommation mensuelle (kWh) — `_mensuel_kwh_um` |

### Comparaison avec conso_temps_reel_appareil

| Variable | `conso_temps_reel_appareil` | `conso_mensuelle_appareil` |
|:---------|:---------------------------|:--------------------------|
| `current_entity` | ✅ Puissance instantanée (W) | ❌ Absent |
| `avg_daily_entity` | ✅ Moyenne quotidienne (W) | ❌ Absent |
| `avg_monthly_entity` | ❌ Absent | ✅ Moyenne mensuelle (W) |
| `conso_daily_kwh_entity` | ✅ kWh du jour | ❌ Absent |
| `conso_monthly_kwh_entity` | ❌ Absent | ✅ kWh du mois |

---

## 🎨 PALETTE DE COULEURS

### Logique chromatique du donut

La palette suit une logique **par fonction** plus que par pièce :

| Gamme | Devices | Teinte |
|:------|:--------|:-------|
| Gris clair | Box, Horloge (Standby bas) | `gainsboro`, `rgb(183,183,183)` |
| Rose/Rouge | PC Géraldine, Chargeurs Salon, TV Salon | `rgb(202,135,135)`, `rgb(174,68,90)`, `rgb(215,95,115)` |
| Violet foncé → clair | Cuisine (Four M-O → Airfryer) | `rgb(98,78,136)` → `rgb(142,122,181)` |
| Lavande | Four & Plaque | `rgb(162,148,249)` |
| Cyan → Bleu | Frigo, Congélateur (froid) | `cyan`, `rgb(19,160,255)` |
| Orange / Gold | PCe Bureau, Fer à Repasser | `orange`, `gold` |
| Vert pâle | Têtes de Lit | `rgb(177,194,158)` |
| Vert foncé | TV Chambre | `rgb(30,81,40)` |
| Gris | Veilles (All Standby) | `grey` |

---

## 📊 ENTITÉS UTILISÉES

### Utility Meters mensuels (`_mensuel_kwh_um`)

Source : `utility_meter.yaml` — cycle `monthly`, réinitialisé le 1er du mois.

| Entité | Appareil |
|:-------|:---------|
| `sensor.prise_box_internet_ikea_mensuel_kwh_um` | Box Internet Entrée |
| `sensor.prise_horloge_ikea_mensuel_kwh_um` | Horloge Entrée |
| `sensor.prise_pc_s_gege_ikea_mensuel_kwh_um` | PC's Géraldine (Salon) |
| `sensor.prise_salon_chargeur_nous_mensuel_kwh_um` | Chargeurs Salon |
| `sensor.prise_tv_salon_ikea_mensuel_kwh_um` | TV Salon |
| `sensor.prise_four_micro_ondes_nous_mensuel_kwh_um` | Four Micro-Ondes Cuisine |
| `sensor.prise_petit_dejeune_nous_mensuel_kwh_um` | P'tit Dej. Cuisine |
| `sensor.prise_lave_linge_nous_mensuel_kwh_um` | Lave-Linge Cuisine |
| `sensor.prise_lave_vaisselle_nous_mensuel_kwh_um` | Lave-Vaisselle Cuisine |
| `sensor.prise_airfryer_ninja_nous_mensuel_kwh_um` | Airfryer Cuisine |
| `sensor.four_et_plaque_de_cuisson_mensuel_kwh_um` | Four & Plaque Cuisine |
| `sensor.prise_frigo_cuisine_nous_mensuel_kwh_um` | Frigo Cuisine |
| `sensor.prise_congelateur_cuisine_nous_mensuel_kwh_um` | Congélateur Cuisine |
| `sensor.prise_bureau_pc_ikea_mensuel_kwh_um` | PCe Bureau |
| `sensor.prise_bureau_fer_a_repasser_nous_mensuel_kwh_um` | Fer à Repasser Bureau |
| `sensor.prise_tete_de_lit_chambre_mensuel_kwh_um` | Têtes de Lit Chambre |
| `sensor.prise_tv_chambre_nous_mensuel_kwh_um` | TV Chambre |
| `sensor.all_standby_mensuel_kwh_um` | All Standby (Veilles) |

### Énergie totale cumulée (`_energie_totale_kwh`)

Source : sensors Pôle 2 — `platform: integration` ou `state_class: total_increasing`.

| Entité | Appareil |
|:-------|:---------|
| `sensor.prise_box_internet_ikea_energie_totale_kwh` | Box Internet |
| `sensor.prise_horloge_ikea_energie_totale_kwh` | Horloge Entrée |
| `sensor.prise_pc_s_gege_ikea_energie_totale_kwh` | PC's Géraldine |
| `sensor.prise_salon_chargeur_nous_energie_totale_kwh` | Chargeurs Salon |
| `sensor.prise_tv_salon_ikea_energie_totale_kwh` | TV Salon |
| `sensor.prise_four_micro_ondes_nous_energie_totale_kwh` | Four M-O |
| `sensor.prise_petit_dejeune_nous_energie_totale_kwh` | P'tit Dej. |
| `sensor.prise_lave_linge_nous_energie_totale_kwh` | Lave-Linge |
| `sensor.prise_lave_vaisselle_nous_energie_totale_kwh` | Lave-Vaisselle |
| `sensor.prise_airfryer_ninja_nous_energie_totale_kwh` | Airfryer |
| `sensor.four_et_plaque_de_cuisson_energie_totale_kwh` | Four & Plaque |
| `sensor.prise_frigo_cuisine_nous_energie_totale_kwh` | Frigo |
| `sensor.prise_congelateur_cuisine_nous_energie_totale_kwh` | Congélateur |
| `sensor.prise_bureau_pc_ikea_energie_totale_kwh` | PCe Bureau |
| `sensor.prise_bureau_fer_a_repasser_nous_energie_totale_kwh` | Fer à Repasser |
| `sensor.prise_tete_de_lit_chambre_energie_totale_kwh` | Têtes de Lit |
| `sensor.prise_tv_chambre_nous_energie_totale_kwh` | TV Chambre |
| `sensor.all_standby_energie_totale_kwh` | All Standby |

### Moyennes mensuelles (`_avg_watts_mensuel`)

Source : sensors Pôle 2 — `platform: statistics` sur énergie ou puissance.

| Entité | Appareil |
|:-------|:---------|
| `sensor.box_internet_avg_watts_mensuel` | Box Internet |
| `sensor.horloge_avg_watts_mensuel` | Horloge |
| `sensor.pc_gege_avg_watts_mensuel` | PC's Géraldine |
| `sensor.chargeurs_salon_avg_watts_mensuel` | Chargeurs Salon |
| `sensor.tv_salon_avg_watts_mensuel` | TV Salon |
| `sensor.four_mo_avg_watts_mensuel` | Four M-O |
| `sensor.petit_dej_avg_watts_mensuel` | P'tit Dej. |
| `sensor.lave_linge_avg_watts_mensuel` | Lave-Linge |
| `sensor.lave_vaisselle_avg_watts_mensuel` | Lave-Vaisselle |
| `sensor.airfryer_avg_watts_mensuel` | Airfryer |
| `sensor.plaques_cuisson_avg_watts_mensuel` | Four & Plaque |
| `sensor.frigo_avg_watts_mensuel` | Frigo |
| `sensor.congelateur_avg_watts_mensuel` | Congélateur |
| `sensor.pc_bureau_avg_watts_mensuel` | PCe Bureau |
| `sensor.fer_repasser_avg_watts_mensuel` | Fer à Repasser |
| `sensor.tetes_lit_avg_watts_mensuel` | Têtes de Lit |
| `sensor.tv_chambre_avg_watts_mensuel` | TV Chambre |
| `sensor.veilles_avg_watts_mensuel` | All Standby |

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `custom:apexcharts-card` | HACS | ✅ Essentiel |
| `custom:streamline-card` | HACS | ✅ Essentiel |
| Template `conso_mensuelle_appareil` | Streamline template | ✅ Requis |
| `utility_meter` `_mensuel_kwh_um` × 18 | HA native | ✅ Cycle `monthly` |
| Sensors `_energie_totale_kwh` × 18 | Sensors Pôle 2 | ✅ `p2_sensors_prises.yaml` |
| Sensors `_avg_watts_mensuel` × 18 | Sensors Pôle 2 | ✅ `p2_sensors_prises.yaml` |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Page mensuelle (YAML) | `dashbord/page_energie_mensuel.yaml` |
| Page principale énergie | `dashbord/page_energie_home.yaml` |
| Page temps réel | `dashbord/page_energie_temps_reel.yaml` |
| Utility Meters (Pôle 2) | `utility_meter.yaml` |
| Sensors Prises (Pôle 2) | `sensors/p2_sensors_prises.yaml` |
| Doc page principale | `docs/L2C1_ENERGIE/PAGE_ENERGIE.md` |
| Doc page temps réel | `docs/L2C1_ENERGIE/PAGE_ENERGIE_TEMPS_REEL.md` |

---

← Retour : `docs/L2C1_ENERGIE/PAGE_ENERGIE_TEMPS_REEL.md` | → Suivant : `docs/L2C2_*/`
