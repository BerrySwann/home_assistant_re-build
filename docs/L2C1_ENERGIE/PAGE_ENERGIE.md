<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--20-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/page_energie_home.yaml` (Sections → Vue : energie) |
| 🔗 **Accès depuis** | Vignette L2C1 → Dashboard HOME → tap → `/dashboard-tablette/energie` |
| 🔗 **Liens vers** | Badge "Réel" → `/dashboard-tablette/energie-temps-reel` · Badge "Cumul Jrs" → `/dashboard-tablette/energie-mensuel` |
| 🏗️ **Layout** | `type: grid` (column_span: 1) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-20 |
| 🏠 **Version HA** | 2026.3.x |

---

# ⚡ PAGE ÉNERGIE HOME — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section HEADER](#section-header)
4. [Section RING TILES — Mini / Réel / Maxi](#section-ring-tiles--mini--réel--maxi)
5. [Section ENERGY OVERVIEW](#section-energy-overview)
6. [Section RATIOS LINKY](#section-ratios-linky)
7. [Section TABBED-CARD (3 onglets)](#section-tabbed-card-3-onglets)
   - [Onglet JOURNALIER](#onglet-journalier)
   - [Onglet HEBDOMADAIRE](#onglet-hebdomadaire)
   - [Onglet MENSUEL](#onglet-mensuel)
8. [Entités utilisées](#entités-utilisées--provenance-complète)
9. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Cette page regroupe toutes les informations de consommation électrique du logement en temps réel et sur les périodes passées :
- Puissance instantanée (Mini / Temps réel / Maxi) via ring-tile-card
- Flux Enedis → Maison via energy-overview-card
- Ratios Linky A-1 / Semaine / Annuel
- Coûts journaliers et mensuels HP/HC détaillés
- Pie charts HP/HC + sliders de rentabilité HC
- Graphique 24h temps réel + moyennes glissantes
- Historique 7 jours superposé (offset ApexCharts)
- Tableau Linky 8 jours (coût + HP/HC)
- Graphique mensuel par jours
- Synthèse par postes (7 catégories, jour + mois) avec donut

### Intégrations requises

- ✅ **Ecojoko** (`little_monkey`) — `sensor.ecojoko_*`
- ✅ **MyElectricalData / Linky** (`linky_card`) — `sensor.linky_*`
- ✅ **tarif_edf** (custom component) — `sensor.tarif_heures_*_ttc`
- ✅ Sensors natifs Ecojoko — `sensor.ecojoko_conso_mini_24h` / `sensor.ecojoko_conso_maxi_24h` (fournis directement par l'intégration Ecojoko)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `ring-tile-card` | Indicateurs circulaires Mini / Réel / Maxi |
| `energy-overview-card` | Flux Enedis → Maison animé |
| `content-card-linky` | Ratios Linky (mois / semaine / annuel) |
| `apexcharts-card` | Graphiques (24h, 7j, mensuel, pie, donut) |
| `tabbed-card` | Onglets JOURNALIER / HEBDOMADAIRE / MENSUEL |
| `button-card` | Slider de rentabilité HC (dans chaque onglet) |
| `flex-table-card` | Tableau Linky 8 jours |
| `auto-entities` + `bar-card` | Synthèse usages par postes |
| `stack-in-card` | Regroupement transparent |
| `mod-card` + `text-divider-row` | Séparateurs de sections |
| `card-mod` | Suppression bordures/ombres partout |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌─────────────────────────────────────────────────────┐
│  [HEADER] ENERGIE HOME + Badges Réel/Cumul          │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Appartement                            │
├─────────────────────────────────────────────────────┤
│  ┌────────┐   ┌────────┐   ┌────────┐              │
│  │  Mini  │   │  Réel  │   │  Maxi  │  ← ring-tile │
│  │  (W)   │   │  (W)   │   │  (W)   │              │
│  └────────┘   └────────┘   └────────┘              │
├─────────────────────────────────────────────────────┤
│  [energy-overview-card] Enedis → Maison             │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Ratio Mois A-1 / Semaine / A-1         │
│  [linky] RatioMois | [linky] RatioSem | [linky] A-1 │
├─────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────┐   │
│  │  [tabbed-card]  --mdc-theme-primary: #FFB347 │   │
│  │  swipeable: true    animated: true           │   │
│  ├──────────────┬─────────────┬─────────────────┤   │
│  │ JOURNALIER   │HEBDOMADAIRE │    MENSUEL       │   │
│  ├──────────────┴─────────────┴─────────────────┤   │
│  │  [Coût Total / HP / HC : kWh + €]            │   │
│  │  [Pie chart HP/HC]                           │   │
│  │  [Slider rentabilité HC]                     │   │
│  │  (JOURNALIER uniquement :)                   │   │
│  │    [ApexCharts 24h temps réel]               │   │
│  │    [ApexCharts Historique 7j offset]         │   │
│  │    [flex-table-card Linky 8 jours]           │   │
│  │  (MENSUEL uniquement :)                      │   │
│  │    [ApexCharts mensuel par jours]            │   │
│  │  [bar-card SYNTHÈSE USAGES]                  │   │
│  │  [donut Répartition conso]                   │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

---

## 📍 SECTION HEADER

```yaml
- type: heading
  icon: mdi:transmission-tower
  heading: ENERGIE HOME
  heading_style: title
  badges:
    - type: entity
      entity: sensor.ecojoko_consommation_temps_reel
      name: Réel
      color: green
      tap_action:
        action: navigate
        navigation_path: /dashboard-tablette/energie-temps-reel
    - type: entity
      entity: sensor.ecojoko_consommation_reseau
      name: Cumul Jrs
      color: green
      tap_action:
        action: navigate
        navigation_path: /dashboard-tablette/energie-mensuel
  tap_action:
    action: navigate
    navigation_path: /dashboard-tablette/0
  layout_options:
    grid_columns: full
    grid_rows: 1
```

### Rôle
- Titre principal : "ENERGIE HOME" avec icône pylône électrique
- Badge **Réel** : Puissance instantanée Ecojoko (W) — tap → `/dashboard-tablette/energie-temps-reel` *(page dédiée temps réel)*
- Badge **Cumul Jrs** : Consommation réseau cumulée du jour (kWh) — tap → `/dashboard-tablette/energie-mensuel` *(page dédiée mensuel)*
- Navigation retour : Clic titre → `/dashboard-tablette/0` (dashboard HOME)

> **Pages liées** : `energie-temps-reel` et `energie-mensuel` sont 2 pages séparées accessibles uniquement depuis les badges. Documentation : `PAGE_ENERGIE_TEMPS_REEL.md` et `PAGE_ENERGIE_MENSUEL.md`.

### Entités
- `sensor.ecojoko_consommation_temps_reel` [Ecojoko - UI] Puissance instantanée (W)
- `sensor.ecojoko_consommation_reseau` [Ecojoko - UI] Consommation réseau cumulée (kWh)

---

## 🔴 SECTION RING TILES — Mini / Réel / Maxi

Grid 3 colonnes. Chaque ring-tile est un indicateur circulaire avec arc de couleur dynamique.

```yaml
- square: false
  type: grid
  columns: 3
  cards:
    - type: custom:ring-tile    # Mini
    - type: custom:ring-tile    # Réel
    - type: custom:ring-tile    # Maxi
```

### Ring-tile : Conso. Mini (talon standby)

| Paramètre | Valeur |
|-----------|--------|
| `entity` | `sensor.ecojoko_conso_mini_24h` |
| `min` | 0 |
| `max` | 100 |
| `ring_type` | `open` |

**Palette couleur :**

| Seuil (W) | Couleur | Signification |
|-----------|---------|---------------|
| 0–49 | Vert | Standby normal |
| 50–64 | Orange | Standby élevé |
| 65–74 | Orange | À surveiller |
| ≥ 75 | Rouge | Standby anormal |

> `ecojoko_conso_mini_24h` = puissance minimale native Ecojoko sur 24h. Reflète le talon de consommation irréductible (box, standby). Fourni directement par l'intégration Ecojoko [UI].

---

### Ring-tile : Conso. Temps Réel

| Paramètre | Valeur |
|-----------|--------|
| `entity` | `sensor.ecojoko_consommation_temps_reel` |
| `min` | 0 |
| `max` | 6000 |

**Palette couleur :**

| Seuil (W) | Couleur | Signification |
|-----------|---------|---------------|
| 0–1 699 | Vert | Consommation normale |
| 1 700–1 999 | Vert | Légère montée |
| 2 000–3 699 | Orange | Consommation élevée |
| 3 700–3 999 | Orange | Approche du seuil fort |
| ≥ 4 000 | Rouge | Forte consommation (clim + tout) |

---

### Ring-tile : Conso. Maxi

| Paramètre | Valeur |
|-----------|--------|
| `entity` | `sensor.ecojoko_conso_maxi_24h` |
| `min` | 0 |
| `max` | 6000 |

Même palette couleur que le Temps Réel (seuils 2 000 / 4 000 W).

> `ecojoko_conso_maxi_24h` = puissance maximale native Ecojoko sur 24h. Reflète le pic de consommation journalier. Fourni directement par l'intégration Ecojoko [UI].

---

## ⚡ SECTION ENERGY OVERVIEW

```yaml
- type: vertical-stack
  cards:
    - type: custom:vertical-stack-in-card
      cards:
        - type: custom:energy-overview-card
          entities:
            - power: sensor.ecojoko_consommation_reseau
              current: sensor.ecojoko_consommation_temps_reel
              label_leading: Enedis
              label_trailing: Maison
              icon_leading: mdi:transmission-tower
              icon_trailing: mdi:home-lightning-bolt
              color: "#488fc2"
              animation:
                power: 1000
                min_duration: 1
                max_duration: 5
  grid_options:
    columns: 24
    rows: auto
```

### Rôle
Affiche un flux animé Enedis → Maison. La vitesse d'animation est proportionnelle à la consommation (seuil : 1 000 W, durée 1–5s).

### Entités
- `sensor.ecojoko_consommation_reseau` [Ecojoko - UI] Consommation réseau cumulée (kWh)
- `sensor.ecojoko_consommation_temps_reel` [Ecojoko - UI] Puissance instantanée (W)

---

## 📊 SECTION RATIOS LINKY

3 cartes `content-card-linky` côte à côte (grid_options columns: 4 chacune) :

| Carte | Option activée | Description |
|-------|----------------|-------------|
| Linky 1 | `showCurrentMonthRatio: true` | Ratio mois en cours vs mois A-1 |
| Linky 2 | `showWeekRatio: true` | Ratio semaine en cours vs semaine dernière |
| Linky 3 | `showYearRatio: true` | Ratio année en cours vs année A-1 |

Toutes utilisent `entity: sensor.linky_25481620821301_consumption` et `ewEntity: sensor.linky_25481620821301_consumption`. Les options d'affichage superflues sont désactivées (`show_inject: true`, `showHistory: false`, `showIcon: false`, etc.).

### Entités
- `sensor.linky_25481620821301_consumption` [MyElectricalData - UI] Consommation Linky (index)

---

## 🗂️ SECTION TABBED-CARD (3 ONGLETS)

La zone principale de la page est une `custom:tabbed-card` englobant les 3 périodes de suivi. Chaque onglet contient la même structure logique adaptée à sa période.

```yaml
- type: custom:tabbed-card
  styles:
    "--mdc-theme-primary": "#FFB347"
    "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.6)
    max-width: 100%
  attributes:
    animated: true
    swipeable: true
  tabs:
    - attributes:
        label: JOURNALIER
        icon: mdi:calendar-today
      card: ...
    - attributes:
        label: HEBDOMADAIRE
        icon: mdi:calendar-week
      card: ...
    - attributes:
        label: MENSUEL
        icon: mdi:calendar-month
      card: ...
```

**Propriétés communes :**
- Couleur active : `#FFB347` (orange chaleureux)
- Onglets inactifs : blanc 60% opacité
- Swipe activé (`swipeable: true`) — navigation tactile
- Animation de transition (`animated: true`)

---

### Onglet JOURNALIER

Période : jour en cours (remise à zéro à minuit).

**Contenu dans l'ordre :**

**1. Coût Quotidien** — 2 rangées de 3 entités (kWh + €)

| Entité | Type | Rôle |
|--------|------|------|
| `sensor.ecojoko_reseau_quotidien_um` | entity | Total kWh quotidien (UM) |
| `sensor.ecojoko_hp_reseau_quotidien_um` | entity | H.P. kWh quotidien (UM) |
| `sensor.ecojoko_hc_reseau_quotidien_um` | entity | H.C. kWh quotidien (UM) |
| `sensor.ecojoko_cout_total_quotidien` | entity | Coût total € quotidien |
| `sensor.ecojoko_cout_hp_quotidien` | entity | H.P. € quotidien |
| `sensor.ecojoko_cout_hc_quotidien` | entity | H.C. € quotidien |

> Sources UM : `utility_meter/P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml`
> Sources coûts : `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml`

**2. Pie Chart HP/HC journalier (ApexCharts)**

```yaml
chart_type: pie
graph_span: 24h
span:
  start: day
series:
  - entity: sensor.ecojoko_hp_reseau_quotidien_um
    name: Heure pleine
    color: rgb(211, 58, 79)
  - entity: sensor.ecojoko_hc_reseau_quotidien_um
    name: Heure creuse
    color: rgb(72, 132, 213)
```

**3. Slider Rentabilité HC quotidien (Button-card)**

**Entité :** `sensor.ecojoko_ratio_hc_quotidien`

Layout CSS Grid : `"n s" / "l s" / "bar bar"`. Gradient de fond : rouge < 25% → orange 25–33% → vert > 33%. Curseur `gainsboro` 18px positionné à `left: ${val}%` avec transition `0.6s ease-in-out`.

**4. Graphique 24h Temps Réel (ApexCharts)**

```yaml
graph_span: 24h
cache: false
span:
  start: day
```

| Série | Entité | Type | Rôle |
|-------|--------|------|------|
| Conso. temps réel | `sensor.ecojoko_consommation_temps_reel` | area | Courbe puissance instantanée |
| Moy. glissante 24h | `sensor.ecojoko_consommation_temps_reel` | line | `func: avg, duration: 24h` |
| Moy. depuis minuit | `sensor.ecojoko_avg_watts_quotidien` | line | Axe secondaire Wh |
| Moy. 1er du mois | `sensor.ecojoko_avg_watts_mensuel` | — | En-tête uniquement (`in_chart: false`) |

Double axe Y : `TempsReel` (gauche — W) / `Minuit` (droite — Wh).

**5. Historique 7 jours (Offset — ApexCharts)**

Principe : toutes les séries utilisent `sensor.ecojoko_consommation_reseau` avec un `offset` décalant la fenêtre de lecture. Le recorder HA fournit les données historiques.

| Série | Offset | Couleur |
|-------|--------|---------|
| Aujourd'hui | aucun | `gainsboro` |
| J-1 | `-1d` | `rgb(204, 255, 204)` |
| J-2 | `-2d` | `rgb(153, 255, 153)` |
| J-3 | `-3d` | `rgb(102, 255, 102)` |
| J-4 | `-4d` | `rgb(51, 204, 51)` |
| J-5 | `-5d` | `rgb(0, 153, 0)` |
| J-6 | `-6d` | `rgb(0, 102, 0)` |
| J-7 | `-7d` | `rgb(0, 70, 0)` |

`extend_to: false` sur toutes les séries passées. `group_by: func: last, duration: 10m`. Recorder HA ≥ 8 jours requis.

**6. Tableau Linky 8 jours (flex-table-card)**

```yaml
entities: [sensor.linky_jour_0 … sensor.linky_jour_7]
columns: Jour | Total kWh | Coût € | HP kWh | HC kWh
```

> `linky_jour_0` = conso Ecojoko du jour en temps réel (pas données Linky). `linky_jour_1-7` = attributs Linky (Wh ÷ 1000). Source : `templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml`

**7. Synthèse Usages Journaliers + Donut**

Bar-card `auto-entities` triée par état décroissant. Max dynamique : `sensor.diag_max_poste_quotidien_dynamique`.

| Poste | Entité | Icône | Couleur |
|-------|--------|-------|---------|
| Hygiène | `sensor.diag_poste_hygiene_quotidien` | `mdi:water` | `#00BFFF` |
| Cuisson | `sensor.diag_poste_cuisine_quotidien` | `mdi:stove` | `#FF4500` |
| Froid | `sensor.diag_poste_froid_quotidien` | `mdi:snowflake` | `#87CEEB` |
| Chauffage | `sensor.diag_poste_chauffage_quotidien` | `mdi:fire` | `#FFA500` |
| Multimedia | `sensor.diag_poste_multimedia_quotidien` | `mdi:desktop-tower-monitor` | `#9370DB` |
| Lumière | `sensor.diag_poste_eclairage_quotidien` | `mdi:lightbulb` | `#ADFF2F` |
| Autres | `sensor.diag_poste_autre_quotidien` | `mdi:account` | `lightgrey` |

Donut ApexCharts : `graph_span: 24h`, `group_by: func: last, duration: 24h`, DataLabels `%` (1 décimale), tooltip `kWh` (2 décimales).

> Source : `templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml`

---

### Onglet HEBDOMADAIRE

Période : semaine en cours (remise à zéro le lundi à minuit).

**1. Coût Hebdomadaire** — 2 rangées de 3 entités (kWh + €)

| Entité | Rôle |
|--------|------|
| `sensor.ecojoko_reseau_hebdomadaire_um` | Total kWh hebdo (UM) |
| `sensor.ecojoko_hp_reseau_hebdomadaire_um` | H.P. kWh hebdo (UM) |
| `sensor.ecojoko_hc_reseau_hebdomadaire_um` | H.C. kWh hebdo (UM) |
| `sensor.ecojoko_cout_total_hebdomadaire` | Coût total € hebdo |
| `sensor.ecojoko_cout_hp_hebdomadaire` | H.P. € hebdo |
| `sensor.ecojoko_cout_hc_hebdomadaire` | H.C. € hebdo |

> Source UM : `utility_meter/P0_Energie_total/Ecojoko/01_UM_AMHQ_cost.yaml`
> Source coûts : `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml`

**2. Pie Chart HP/HC hebdomadaire**

```yaml
chart_type: pie
graph_span: 7d
span:
  start: week
series:
  - entity: sensor.ecojoko_hp_reseau_hebdomadaire_um
    color: rgb(211, 58, 79)
  - entity: sensor.ecojoko_hc_reseau_hebdomadaire_um
    color: rgb(72, 132, 213)
```

**3. Slider Rentabilité HC hebdomadaire**

**Entité :** `sensor.ecojoko_ratio_hc_hebdomadaire` — même structure que le slider journalier.

**4. Synthèse Usages Hebdomadaires + Donut**

Max dynamique : `sensor.diag_max_poste_hebdomadaire_dynamique`.

| Poste | Entité |
|-------|--------|
| Hygiène | `sensor.diag_poste_hygiene_hebdomadaire` |
| Cuisson | `sensor.diag_poste_cuisine_hebdomadaire` |
| Froid | `sensor.diag_poste_froid_hebdomadaire` |
| Chauffage | `sensor.diag_poste_chauffage_hebdomadaire` |
| Multimedia | `sensor.diag_poste_multimedia_hebdomadaire` |
| Lumière | `sensor.diag_poste_eclairage_hebdomadaire` |
| Autres | `sensor.diag_poste_autre_hebdomadaire` |

Donut : `group_by: func: last, duration: 7d`.

> Source : `templates/P0_Energie_total_diag/Diag/diag_conso_hebdomadaire_en_cours.yaml`

---

### Onglet MENSUEL

Période : mois en cours (remise à zéro le 1er du mois à minuit).

**1. Coût Mensuel** — 2 rangées de 3 entités (kWh + €)

> ⚠️ **Différence technique** : Le Total kWh mensuel utilise `type: statistic` avec `stat_type: change` et `period: calendar / month` sur `sensor.ecojoko_consommation_reseau` — pas un UM. Les HP/HC utilisent les UM mensuels.

| Entité | Type | Rôle |
|--------|------|------|
| `sensor.ecojoko_consommation_reseau` | `type: statistic` (change, mois) | Total kWh mensuel |
| `sensor.ecojoko_hp_reseau_mensuel_um` | entity | H.P. kWh mensuel (UM) |
| `sensor.ecojoko_hc_reseau_mensuel_um` | entity | H.C. kWh mensuel (UM) |
| `sensor.ecojoko_cout_total_mensuel` | entity | Coût total € mensuel |
| `sensor.ecojoko_cout_hp_mensuel` | entity | H.P. € mensuel |
| `sensor.ecojoko_cout_hc_mensuel` | entity | H.C. € mensuel |

**2. Pie Chart HP/HC mensuel**

```yaml
chart_type: pie
graph_span: 1month
span:
  start: month
series:
  - entity: sensor.ecojoko_hp_reseau_mensuel_um
    color: rgb(211, 58, 79)
  - entity: sensor.ecojoko_hc_reseau_mensuel_um
    color: rgb(72, 132, 213)
```

**3. Slider Rentabilité HC mensuel**

**Entité :** `sensor.ecojoko_ratio_hc_mensuel` — même structure que le slider journalier.

**4. Graphique Mensuel par Jours (ApexCharts)**

```yaml
graph_span: 31d
cache: true
span:
  start: month
```

| Série | Entité | Type | Axe | Rôle |
|-------|--------|------|-----|------|
| Conso. ce jour | `sensor.ecojoko_avg_watts_quotidien` | column | `daily` | Barres kWh (`func: max, duration: 24h`) |
| Moy. glissante mois | `sensor.ecojoko_consommation_reseau` | line | `daily` | `func: avg, duration: 730h` |
| Moy. depuis minuit | `sensor.ecojoko_avg_watts_quotidien` | line | `moyenne` | Axe secondaire Wh |
| Moy. 1er du mois | `sensor.ecojoko_avg_watts_mensuel` | — | `daily` | En-tête uniquement (`in_chart: false`) |

**5. Synthèse Usages Mensuels + Donut**

Max dynamique : `sensor.diag_max_poste_mensuel_dynamique`.

| Poste | Entité |
|-------|--------|
| Hygiène | `sensor.diag_poste_hygiene_mensuel` |
| Cuisson | `sensor.diag_poste_cuisine_mensuel` |
| Froid | `sensor.diag_poste_froid_mensuel` |
| Chauffage | `sensor.diag_poste_chauffage_mensuel` |
| Multimedia | `sensor.diag_poste_multimedia_mensuel` |
| Lumière | `sensor.diag_poste_eclairage_mensuel` |
| Autres | `sensor.diag_poste_autre_mensuel` |

Donut : `group_by: func: diff, duration: 24h`.

> Source : `templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml`

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### ⚡ Ecojoko — Temps réel

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.ecojoko_consommation_temps_reel` | Puissance instantanée (W) | Intégration Ecojoko [UI] |
| `sensor.ecojoko_consommation_reseau` | Consommation réseau cumulée (kWh) | Intégration Ecojoko [UI] |

---

### 📈 Statistiques P0 — Mini / Maxi / Moyennes

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.ecojoko_conso_mini_24h` | Puissance min sur 24h (W) — talon standby | Intégration Ecojoko [UI] |
| `sensor.ecojoko_conso_maxi_24h` | Puissance max sur 24h (W) — pic | Intégration Ecojoko [UI] |
| `sensor.ecojoko_avg_watts_quotidien` | Moyenne Wh depuis minuit | `templates/P0_Energie_total_diag/Ecojoko/03_AVG_ecojoko.yaml` |
| `sensor.ecojoko_avg_watts_mensuel` | Moyenne Wh depuis le 1er du mois | idem |

---

### 🔢 Utility Meters Quotidiens (Ecojoko)

| Entité | Cycle | Source |
|--------|-------|--------|
| `sensor.ecojoko_reseau_quotidien_um` | daily | `utility_meter/P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml` |
| `sensor.ecojoko_hp_reseau_quotidien_um` | daily | idem |
| `sensor.ecojoko_hc_reseau_quotidien_um` | daily | idem |

---

### 🔢 Utility Meters Hebdomadaires (Ecojoko)

| Entité | Cycle | Source |
|--------|-------|--------|
| `sensor.ecojoko_reseau_hebdomadaire_um` | weekly | `utility_meter/P0_Energie_total/Ecojoko/01_UM_AMHQ_cost.yaml` |
| `sensor.ecojoko_hp_reseau_hebdomadaire_um` | weekly | idem |
| `sensor.ecojoko_hc_reseau_hebdomadaire_um` | weekly | idem |

---

### 🔢 Utility Meters Mensuels (Ecojoko)

| Entité | Cycle | Source |
|--------|-------|--------|
| `sensor.ecojoko_hp_reseau_mensuel_um` | monthly | `utility_meter/P0_Energie_total/Ecojoko/01_UM_AMHQ_cost.yaml` |
| `sensor.ecojoko_hc_reseau_mensuel_um` | monthly | idem |

---

### 💰 Coûts calculés (Templates)

| Entité | Période | Source |
|--------|---------|--------|
| `sensor.ecojoko_cout_total_quotidien` | Quotidien | `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml` |
| `sensor.ecojoko_cout_hp_quotidien` | Quotidien | idem |
| `sensor.ecojoko_cout_hc_quotidien` | Quotidien | idem |
| `sensor.ecojoko_cout_total_hebdomadaire` | Hebdomadaire | idem |
| `sensor.ecojoko_cout_hp_hebdomadaire` | Hebdomadaire | idem |
| `sensor.ecojoko_cout_hc_hebdomadaire` | Hebdomadaire | idem |
| `sensor.ecojoko_cout_total_mensuel` | Mensuel | idem |
| `sensor.ecojoko_cout_hp_mensuel` | Mensuel | idem |
| `sensor.ecojoko_cout_hc_mensuel` | Mensuel | idem |

---

### 📐 Ratios HP/HC

| Entité | Période | Source |
|--------|---------|--------|
| `sensor.ecojoko_ratio_hc_quotidien` | Quotidien (%) | `templates/P0_Energie_total_diag/Ecojoko/02_ratio_hp_hc.yaml` |
| `sensor.ecojoko_ratio_hc_hebdomadaire` | Hebdomadaire (%) | idem |
| `sensor.ecojoko_ratio_hc_mensuel` | Mensuel (%) | idem |

---

### 📡 Linky / MyElectricalData

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.linky_25481620821301_consumption` | Index Linky brut (ratios linky-card) | MyElectricalData [UI] |

### 🔢 Templates Linky — Tableau journalier (flex-table)

| Entité | Rôle | Source réelle |
|--------|------|---------------|
| `sensor.linky_jour_0` | Aujourd'hui : HP+HC (kWh) + coût (€) | **Ecojoko** — `sensor.ecojoko_consommation_hp/hc_reseau` × `sensor.tarif_heures_*_ttc` |
| `sensor.linky_jour_1` à `sensor.linky_jour_7` | J-1 à J-7 : HP+HC (kWh) + coût + jour de semaine | **Attributs Linky** — `state_attr('sensor.linky_25481620821301_consumption', 'day_X_HP/HC')` + `dailyweek_cost` |

> Fichier source : `templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml`
> ⚠️ `linky_jour_0` n'est **pas** une donnée Linky — c'est la conso Ecojoko du jour en temps réel (J0 = Aujourd'hui).
> ⚠️ Les attributs Linky sont en **Wh** dans l'intégration → division par 1000 dans le template pour obtenir des kWh.

---

### 🏭 Diagnostic Postes (7 catégories)

| Entité (quotidien) | Entité (hebdomadaire) | Entité (mensuel) | Source |
|-------------------|-----------------------|-----------------|--------|
| `sensor.diag_poste_hygiene_quotidien` | `..._hebdomadaire` | `..._mensuel` | `templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml` |
| `sensor.diag_poste_cuisine_quotidien` | `..._hebdomadaire` | `..._mensuel` | idem |
| `sensor.diag_poste_froid_quotidien` | `..._hebdomadaire` | `..._mensuel` | idem |
| `sensor.diag_poste_chauffage_quotidien` | `..._hebdomadaire` | `..._mensuel` | idem |
| `sensor.diag_poste_multimedia_quotidien` | `..._hebdomadaire` | `..._mensuel` | idem |
| `sensor.diag_poste_eclairage_quotidien` | `..._hebdomadaire` | `..._mensuel` | idem |
| `sensor.diag_poste_autre_quotidien` | `..._hebdomadaire` | `..._mensuel` | idem |

> ⚠️ **[modif 2026-03-20]** : Les noms de sensors ont été simplifiés — suppression du numéro de poste (ex: `diag_poste_1_hygiene_*` → `diag_poste_hygiene_*`). Le nom `lumiere` a été renommé en `eclairage`. Le nom `cuisson` remplace `2_cuisson`. Vérifier dans États HA les noms exacts en production.

---

### 📊 Max dynamiques (échelle bar-card)

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.diag_max_poste_quotidien_dynamique` | Max du jour (pour échelle bar-card) | `templates/P0_Energie_total_diag/Diag/` |
| `sensor.diag_max_poste_hebdomadaire_dynamique` | Max de la semaine (pour échelle bar-card) | idem |
| `sensor.diag_max_poste_mensuel_dynamique` | Max du mois (pour échelle bar-card) | idem |

---

## 🐛 DÉPANNAGE

### Les ring-tiles affichent "unavailable"
1. Vérifier que `sensor.ecojoko_conso_mini_24h` et `sensor.ecojoko_conso_maxi_24h` existent dans Outils de développement > États
2. Ces sensors sont fournis nativement par l'intégration Ecojoko (`little_monkey`) — vérifier que l'intégration est active et configurée
3. Attendre quelques minutes après redémarrage HA si les valeurs n'apparaissent pas immédiatement

### Les coûts affichent 0 ou "unknown"
1. Vérifier que `sensor.tarif_heures_pleines_ttc` et `sensor.tarif_heures_creuses_ttc` existent (intégration `tarif_edf`)
2. Vérifier les sensors dans `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml`
3. Les UM quotidiens se remettent à 0 à minuit — normal si c'est le début de journée

### Le graphique offset 7 jours ne montre pas tous les jours
1. Le recorder HA doit avoir au moins 7 jours d'historique pour `sensor.ecojoko_consommation_reseau`
2. Vérifier `configuration.yaml` → paramètre `recorder: purge_keep_days:` (doit être ≥ 8)
3. Si récent redémarrage : les données sont présentes, `cache: true` peut ralentir l'affichage (vider cache navigateur)

### Le pie chart HP/HC affiche une seule tranche
1. Normal si aucune consommation HC aujourd'hui (hors plage horaire HC)
2. Vérifier les plages HC configurées dans l'intégration Ecojoko

### Le tableau flex-table-card ne s'affiche pas
1. Vérifier que les entités `sensor.linky_jour_0` à `sensor.linky_jour_7` existent
2. Ces entités sont créées par l'intégration MyElectricalData
3. Si les données Linky sont en retard (J-1 max), c'est normal (données Enedis transmises le lendemain)

### Les donuts SYNTHÈSE USAGES affichent des valeurs incohérentes
1. Vérifier que les sensors `diag_poste_hygiene_quotidien`, `diag_poste_cuisine_quotidien`, etc. existent dans États (sans numérotation)
2. Ces sensors proviennent de `templates/P0_Energie_total_diag/Diag/` — vérifier le fichier source
3. Le `group_by: func: diff, duration: 24h` sur le donut mensuel peut donner des valeurs nulles en début de mois

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| Intégration Ecojoko (`little_monkey`) | Custom component | ✅ Essentiel |
| MyElectricalData / Linky | HACS Integration | ✅ Essentiel |
| `tarif_edf` | Custom component | ✅ Requis pour les coûts |
| `ring-tile-card` | HACS Frontend | ✅ Essentiel (Mini/Réel/Maxi) |
| `tabbed-card` | HACS Frontend | ✅ Essentiel (onglets JOURNALIER/HEBDO/MENSUEL) |
| `energy-overview-card` | HACS Frontend | ✅ Essentiel (flux Enedis) |
| `content-card-linky` | HACS Frontend | ✅ Essentiel (ratios Linky) |
| `apexcharts-card` | HACS Frontend | ✅ Essentiel (tous graphiques) |
| `button-card` | HACS Frontend | ✅ Essentiel (sliders HC) |
| `flex-table-card` | HACS Frontend | ✅ Essentiel (tableau Linky) |
| `bar-card` | HACS Frontend | ✅ Essentiel (synthèse usages) |
| `auto-entities` | HACS Frontend | ✅ Essentiel (synthèse dynamique) |
| `stack-in-card` | HACS Frontend | ✅ Essentiel (regroupements) |
| Recorder HA (≥ 8 jours) | HA natif | ✅ Requis pour offset 7j |

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Dashboard principal | `dashbord/page_energie_home.yaml` |
| UM quotidien HP/HC (live) | `utility_meter/P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml` |
| UM AMHQ (coûts) | `utility_meter/P0_Energie_total/Ecojoko/01_UM_AMHQ_cost.yaml` |
| Coûts HP/HC (4 périodes) | `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml` |
| Ratios HP/HC | `templates/P0_Energie_total_diag/Ecojoko/02_ratio_hp_hc.yaml` |
| Moyennes Ecojoko | `templates/P0_Energie_total_diag/Ecojoko/04_AVG_ecojoko.yaml` |
| Diag postes (jour) | `templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml` |
| Diag postes (hebdo) | `templates/P0_Energie_total_diag/Diag/diag_conso_hebdomadaire_en_cours.yaml` |
| Diag postes (mois) | `templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml` |
| Mini / Maxi (W) | Intégration Ecojoko [UI] — `sensor.ecojoko_conso_mini/maxi_24h` |
| Vignette d'accès | `docs/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md` |

---

← Retour : `docs/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md` | → Pages liées : `PAGE_ENERGIE_TEMPS_REEL.md` · `PAGE_ENERGIE_MENSUEL.md`
