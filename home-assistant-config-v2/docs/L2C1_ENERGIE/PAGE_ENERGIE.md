<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--14-44739e?style=flat-square)](.)&nbsp;
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
| 📅 **Modifié le** | 2026-03-14 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

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
7. [Section COÛT QUOTIDIEN](#section-coût-quotidien)
8. [Section PIE CHART QUOTIDIEN + SLIDER HC](#section-pie-chart-quotidien--slider-hc)
9. [Section COÛT MENSUEL](#section-coût-mensuel)
10. [Section PIE CHART MENSUEL + SLIDER HC](#section-pie-chart-mensuel--slider-hc)
11. [Section GRAPHIQUE 24H TEMPS RÉEL](#section-graphique-24h-temps-réel)
12. [Section HISTORIQUE 7 JOURS (OFFSET)](#section-historique-7-jours-offset)
13. [Section TABLEAU LINKY (flex-table)](#section-tableau-linky-flex-table)
14. [Section GRAPHIQUE MENSUEL PAR JOURS](#section-graphique-mensuel-par-jours)
15. [Section SYNTHÈSE USAGES (Jour + Mois)](#section-synthèse-usages-jour--mois)
16. [Entités utilisées](#entités-utilisées--provenance-complète)
17. [Dépannage](#dépannage)

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
- ✅ Sensors calculés P0 — `sensor.conso_mini` / `sensor.conso_maxi` / `sensor.ecojoko_*`

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `ring-tile-card` | Indicateurs circulaires Mini / Réel / Maxi |
| `energy-overview-card` | Flux Enedis → Maison animé |
| `content-card-linky` | Ratios Linky (mois / semaine / annuel) |
| `apexcharts-card` | Graphiques (24h, 7j, mensuel, pie, donut) |
| `button-card` | Slider de rentabilité HC (quotidien + mensuel) |
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
│  [SEPARATOR] Coût Quotidien                         │
│  Total kWh | HP kWh | HC kWh                        │
│  Total €   | HP €   | HC €                         │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Conso. réel sur 24 Heures              │
│  [Pie chart HP/HC quotidien]                        │
│  [Slider rentabilité HC quotidien]                  │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Coût Mensuel                           │
│  Total kWh | HP kWh | HC kWh                        │
│  Total €   | HP €   | HC €                         │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Conso. réel mensuel                    │
│  [Pie chart HP/HC mensuel]                          │
│  [Slider rentabilité HC mensuel]                    │
├─────────────────────────────────────────────────────┤
│  [ApexCharts 24h] Conso temps réel + moy glissante  │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Energie Totale consommée sur 7 Jours   │
│  [ApexCharts] Historique 7 jours (offset -1d→-7d)  │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Coût totale par Jours (hors Abo.)      │
│  [flex-table-card] Linky 8 jours                    │
├─────────────────────────────────────────────────────┤
│  [SEPARATOR] Conso. Mensuel par Jours               │
│  [ApexCharts] Colonnes par jour + moy glissante     │
├─────────────────────────────────────────────────────┤
│  [bar-card] SYNTHÈSE USAGES (Jour en cours)         │
│  [donut] Répartition conso aujourd'hui              │
│  [bar-card] SYNTHÈSE USAGES (Mois en cours)         │
│  [donut] Répartition conso mois en cours            │
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
| `entity` | `sensor.conso_mini` |
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

> `conso_mini` = valeur min statistique 24h de `sensor.ecojoko_consommation_temps_reel`. Reflète le talon de consommation irréductible (box, standby).

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
| `entity` | `sensor.conso_maxi` |
| `min` | 0 |
| `max` | 6000 |

Même palette couleur que le Temps Réel (seuils 2 000 / 4 000 W).

> `conso_maxi` = valeur max statistique 24h. Reflète le pic de consommation journalier.

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

## 💶 SECTION COÛT QUOTIDIEN

```
[separator] Coût Quotidien

[vertical-stack]
  [horizontal-stack]  Total kWh | HP kWh | HC kWh
  [horizontal-stack]  Total €   | HP €   | HC €
```

6 cartes `type: entity` avec `card_mod` transparent (fond/ombre/bordure supprimés). Icônes blanches forcées via `.icon { color: white }`.

### Entités

| Entité | Rôle |
|--------|------|
| `sensor.ecojoko_reseau_quotidien_um` | Total kWh quotidien (UM) |
| `sensor.ecojoko_hp_reseau_quotidien_um` | HP kWh quotidien (UM) |
| `sensor.ecojoko_hc_reseau_quotidien_um` | HC kWh quotidien (UM) |
| `sensor.ecojoko_cout_total_quotidien` | Coût total € quotidien |
| `sensor.ecojoko_cout_hp_quotidien` | Coût HP € quotidien |
| `sensor.ecojoko_cout_hc_quotidien` | Coût HC € quotidien |

> Sources UM : `utility_meter/P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml`
> Sources coûts : `templates/P0_Energie_total_diag/Ecojoko/01_ecojoko_AMHQ_cost.yaml`

---

## 🥧 SECTION PIE CHART QUOTIDIEN + SLIDER HC

### Pie Chart HP/HC quotidien (ApexCharts)

```yaml
- type: custom:apexcharts-card
  chart_type: pie
  graph_span: 24h
  span:
    start: day
  header:
    title: Conso. journalière H.P./H.C.
  series:
    - entity: sensor.ecojoko_hp_reseau_quotidien_um
      name: Heure pleine
      color: rgb(211, 58, 79)
    - entity: sensor.ecojoko_hc_reseau_quotidien_um
      name: Heure creuse
      color: rgb(72, 132, 213)
```

Affiche la répartition HP (rouge `rgb(211,58,79)`) / HC (bleu `rgb(72,132,213)`) du jour en cours. DataLabels en pourcentage arrondi.

---

### Slider Rentabilité HC quotidien (Button-card)

```yaml
- type: custom:button-card
  entity: sensor.ecojoko_ratio_hc_quotidien
  name: Rentabilité
  label: Heures Creuses
  show_state: true
  show_icon: false
```

**Layout CSS Grid :**
```
"n s"     ← Nom | État (%)
"l s"     ← Label | État (%)
"bar bar" ← Barre slider pleine largeur
```

**Barre de fond (gradient fixe) :**
- 0–25% → Rouge `#f44336` (mauvais)
- 25–33% → Orange `#ff9800` (limite)
- 33–100% → Vert `#4caf50` (rentable)

**Curseur mobile (JS) :**
- Pastille `gainsboro` (18px) positionnée à `left: ${val}%`
- Transition CSS `0.6s ease-in-out`
- Valeur clampée entre 0 et 100%

**Entité :** `sensor.ecojoko_ratio_hc_quotidien` [templates/P0_Energie_total_diag/Ecojoko/02_ratio_hp_hc.yaml]

---

## 💶 SECTION COÛT MENSUEL

Structure identique à Coût Quotidien mais sur la période mensuelle.

```
[separator] Coût Mensuel

[vertical-stack]
  [horizontal-stack]  Total kWh (statistic change) | HP kWh (UM) | HC kWh (UM)
  [horizontal-stack]  Total €   | HP €   | HC €
```

> ⚠️ **Différence technique** : Le Total kWh mensuel utilise `type: statistic` avec `stat_type: change` et `period: calendar / month` sur `sensor.ecojoko_consommation_reseau` — pas un UM. Les HP/HC utilisent les UM mensuels.

### Entités

| Entité | Type | Rôle |
|--------|------|------|
| `sensor.ecojoko_consommation_reseau` | `type: statistic` (change, mois) | Total kWh mensuel |
| `sensor.ecojoko_hp_reseau_mensuel_um` | entity | HP kWh mensuel (UM) |
| `sensor.ecojoko_hc_reseau_mensuel_um` | entity | HC kWh mensuel (UM) |
| `sensor.ecojoko_cout_total_mensuel` | entity | Coût total € mensuel |
| `sensor.ecojoko_cout_hp_mensuel` | entity | Coût HP € mensuel |
| `sensor.ecojoko_cout_hc_mensuel` | entity | Coût HC € mensuel |

---

## 🥧 SECTION PIE CHART MENSUEL + SLIDER HC

### Pie Chart HP/HC mensuel

```yaml
- type: custom:apexcharts-card
  chart_type: pie
  graph_span: 1month
  span:
    start: month
  header:
    title: Conso. mensuelle H.P./H.C.
  series:
    - entity: sensor.ecojoko_hp_reseau_mensuel_um
    - entity: sensor.ecojoko_hc_reseau_mensuel_um
```

Même structure et couleurs que le pie chart quotidien, mais sur le mois en cours (`group_by: func: last, duration: 1month`).

---

### Slider Rentabilité HC mensuel

Même structure que le slider quotidien.

**Entité :** `sensor.ecojoko_ratio_hc_mensuel` [templates/P0_Energie_total_diag/Ecojoko/02_ratio_hp_hc.yaml]

---

## 📈 SECTION GRAPHIQUE 24H TEMPS RÉEL

```yaml
- type: custom:apexcharts-card
  graph_span: 24h
  cache: false
  span:
    start: day
  now:
    show: true
    color: darkred
    label: Now
  apex_config:
    chart:
      height: 400px
```

### Séries

| Série | Entité | Type | Couleur | Rôle |
|-------|--------|------|---------|------|
| Conso. en temps réel | `sensor.ecojoko_consommation_temps_reel` | area | Vert | Courbe de puissance instantanée |
| Moy. glissante (24h) | `sensor.ecojoko_consommation_temps_reel` | line | Rouge | Moyenne glissante sur 24h (`func: avg, duration: 24h`) |
| Moy. depuis minuit | `sensor.ecojoko_avg_watts_quotidien` | line | `#FF5252` | Consommation moyenne depuis 00h00 (Wh) |
| Moy. 1er du mois | `sensor.ecojoko_avg_watts_mensuel` | — | — | Affichage en-tête uniquement (`in_chart: false`) |

### Double axe Y

| Axe | id | Côté | Usage |
|-----|----|------|-------|
| Puissance | `TempsReel` | Gauche | W (temps réel + moy glissante) |
| Quotidien | `Minuit` | Droite | Wh (moy depuis minuit) — max `|+30|` |

---

## 📅 SECTION HISTORIQUE 7 JOURS (OFFSET)

```yaml
- type: custom:apexcharts-card
  experimental:
    color_threshold: true
  graph_span: 24h
  cache: true
  span:
    end: day
  header:
    title: Historique 7 jours (offset)
  apex_config:
    chart:
      height: 450px
      type: area
```

### Principe technique
Toutes les séries utilisent **la même entité** `sensor.ecojoko_consommation_reseau` avec un `offset` décalant la fenêtre de lecture dans le passé. Le recorder HA fournit les données historiques.

### Séries

| Série | Offset | Couleur | Description |
|-------|--------|---------|-------------|
| (Aujourd'hui) | aucun | `gainsboro` | Jour en cours |
| J-1 | `-1d` | `rgb(204, 255, 204)` | Hier |
| J-2 | `-2d` | `rgb(153, 255, 153)` | Avant-hier |
| J-3 | `-3d` | `rgb(102, 255, 102)` | Il y a 3 jours |
| J-4 | `-4d` | `rgb(51, 204, 51)` | Il y a 4 jours |
| J-5 | `-5d` | `rgb(0, 153, 0)` | Il y a 5 jours |
| J-6 | `-6d` | `rgb(0, 102, 0)` | Il y a 6 jours |
| J-7 | `-7d` | `rgb(0, 70, 0)` | Il y a 7 jours |

Dégradé de vert clair → vert foncé. `extend_to: false` sur toutes les séries passées. `group_by: func: last, duration: 10m`.

> **Décision d'architecture** : Approche `offset` retenue (vs sensors J1-J7 abandonnés). Lit directement le recorder HA — aucune dépendance externe.

### Entité unique
- `sensor.ecojoko_consommation_reseau` [Ecojoko - UI]

---

## 📋 SECTION TABLEAU LINKY (flex-table)

```yaml
- type: custom:flex-table-card
  entities:
    - sensor.linky_jour_0
    - sensor.linky_jour_1
    - ...
    - sensor.linky_jour_7
  columns:
    - name: Jour       / data: jour
    - name: Total (kWh)/ data: total_kwh
    - name: Coût (€)   / data: cout
    - name: HP (kWh)   / data: hp_kwh
    - name: HC (kWh)   / data: hc_kwh
```

Tableau de 8 lignes (J0 = aujourd'hui → J7 = il y a 7 jours) affichant jour, total kWh, coût €, détail HP/HC.

### Entités
- `sensor.linky_jour_0` à `sensor.linky_jour_7` [MyElectricalData - UI]

---

## 📊 SECTION GRAPHIQUE MENSUEL PAR JOURS

```yaml
- type: custom:apexcharts-card
  graph_span: 31d
  cache: true
  span:
    start: month
  apex_config:
    chart:
      height: 400px
```

### Séries

| Série | Entité | Type | Axe | Rôle |
|-------|--------|------|-----|------|
| Conso. ce jour | `sensor.ecojoko_avg_watts_quotidien` | column | `daily` | Barres journalières kWh (`func: max, duration: 24h`) |
| Moy. glissante (Mois) | `sensor.ecojoko_consommation_reseau` | line | `daily` | Tendance mensuelle (`func: avg, duration: 730h`) |
| Moy. depuis minuit | `sensor.ecojoko_avg_watts_quotidien` | line | `moyenne` | Axe secondaire Wh |
| Moy. 1er du Mois | `sensor.ecojoko_avg_watts_mensuel` | — | `daily` | En-tête uniquement (`in_chart: false`) |

### Double axe Y

| Axe | id | Côté | Max |
|-----|----|------|-----|
| Journalier | `daily` | Gauche | auto |
| Moyenne | `moyenne` | Droite (caché) | `~500` |

---

## 🏭 SECTION SYNTHÈSE USAGES (JOUR + MOIS)

4 cartes organisées : 2 × bar-card + 2 × donut (ApexCharts).

### Bar-card SYNTHÈSE USAGES — Jour en cours

```yaml
- type: custom:auto-entities
  card:
    type: custom:bar-card
    title: SYNTHÈSE USAGES ( Jour en cours )
    height: 35px
    decimal: 2
    unit_of_measurement: kWh
    max: sensor.max_conso_quotidien_dynamique
```

Barre horizontale pour chaque poste, triée par état décroissant (`sort: method: state, reverse: true`).

### Bar-card SYNTHÈSE USAGES — Mois en cours

Identique avec les entités `_mensuel` et `max: sensor.max_conso_mensuelle_dynamique`.

### Les 7 postes de consommation

| Poste | Entité (quotidien) | Entité (mensuel) | Icône | Couleur |
|-------|-------------------|-----------------|-------|---------|
| Hygiène | `sensor.diag_poste_1_hygiene_quotidien` | `..._mensuel` | `mdi:water` | `#00BFFF` |
| Cuisson | `sensor.diag_poste_2_cuisson_quotidien` | `..._mensuel` | `mdi:stove` | `#FF4500` |
| Froid | `sensor.diag_poste_3_froid_quotidien` | `..._mensuel` | `mdi:snowflake` | `#87CEEB` |
| Chauffage | `sensor.diag_poste_4_chauffage_quotidien` | `..._mensuel` | `mdi:fire` | `#FFA500` |
| Multimedia | `sensor.diag_poste_5_multimedia_quotidien` | `..._mensuel` | `mdi:desktop-tower-monitor` | `#9370DB` |
| Lumière | `sensor.diag_poste_6_lumiere_quotidien` | `..._mensuel` | `mdi:lightbulb` | `#ADFF2F` |
| Autres | `sensor.diag_poste_7_autres_quotidien` | `..._mensuel` | `mdi:account` | `lightgrey` |

> Sources : `templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml` (quotidien)
> et `templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml` (mensuel)

---

### Donut ApexCharts — Répartition aujourd'hui

```yaml
- type: custom:auto-entities
  card:
    type: custom:apexcharts-card
    chart_type: donut
    graph_span: 24h
    header:
      title: Répartition consommation aujourd'hui
```

- DataLabels en `%` (1 décimale)
- Tooltip en `kWh` (2 décimales)
- Légende masquée (`show: false`)
- `group_by: func: last, duration: 24h`

---

### Donut ApexCharts — Répartition mois en cours

Identique mais avec les entités `_mensuel` et `group_by: func: diff, duration: 24h`.

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
| `sensor.conso_mini` | Puissance min du jour (W) — talon standby | `sensors/P0_Energie_total_diag/Ecojoko_mini_maxi/Ecojoko_mini_maxi_avg_1h.yaml` |
| `sensor.conso_maxi` | Puissance max du jour (W) — pic | idem |
| `sensor.ecojoko_avg_watts_quotidien` | Moyenne Wh depuis minuit | `templates/P0_Energie_total_diag/Ecojoko/04_AVG_ecojoko.yaml` |
| `sensor.ecojoko_avg_watts_mensuel` | Moyenne Wh depuis le 1er du mois | idem |

---

### 🔢 Utility Meters Quotidiens (Ecojoko)

| Entité | Cycle | Source |
|--------|-------|--------|
| `sensor.ecojoko_reseau_quotidien_um` | daily | `utility_meter/P0_Energie_total/Ecojoko/02_UM_ecojoko_quotidien_live.yaml` |
| `sensor.ecojoko_hp_reseau_quotidien_um` | daily | idem |
| `sensor.ecojoko_hc_reseau_quotidien_um` | daily | idem |

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
| `sensor.ecojoko_cout_total_mensuel` | Mensuel | idem |
| `sensor.ecojoko_cout_hp_mensuel` | Mensuel | idem |
| `sensor.ecojoko_cout_hc_mensuel` | Mensuel | idem |

---

### 📐 Ratios HP/HC

| Entité | Période | Source |
|--------|---------|--------|
| `sensor.ecojoko_ratio_hc_quotidien` | Quotidien (%) | `templates/P0_Energie_total_diag/Ecojoko/02_ratio_hp_hc.yaml` |
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

| Entité (quotidien) | Entité (mensuel) | Source |
|-------------------|-----------------|--------|
| `sensor.diag_poste_1_hygiene_quotidien` | `..._mensuel` | `templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml` |
| `sensor.diag_poste_2_cuisson_quotidien` | `..._mensuel` | idem |
| `sensor.diag_poste_3_froid_quotidien` | `..._mensuel` | idem |
| `sensor.diag_poste_4_chauffage_quotidien` | `..._mensuel` | idem |
| `sensor.diag_poste_5_multimedia_quotidien` | `..._mensuel` | idem |
| `sensor.diag_poste_6_lumiere_quotidien` | `..._mensuel` | idem |
| `sensor.diag_poste_7_autres_quotidien` | `..._mensuel` | idem |

---

### 📊 Max dynamiques (échelle bar-card)

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.max_conso_quotidien_dynamique` | Max du jour (pour échelle bar-card) | `templates/P0_Energie_total_diag/Diag/` |
| `sensor.max_conso_mensuelle_dynamique` | Max du mois (pour échelle bar-card) | idem |

---

## 🐛 DÉPANNAGE

### Les ring-tiles affichent "unavailable"
1. Vérifier que `sensor.conso_mini` et `sensor.conso_maxi` existent dans Outils de développement > États
2. Ces sensors utilisent `platform: statistics` sur `sensor.ecojoko_consommation_temps_reel` — vérifier le fichier `sensors/P0_Energie_total_diag/Ecojoko_mini_maxi/`
3. Attendre ~1h après redémarrage HA (les statistics ont besoin d'un historique minimal)

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
1. Vérifier que les sensors `diag_poste_*_quotidien` existent dans États
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
| Diag postes (mois) | `templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml` |
| Mini/Maxi/Moy 1h | `sensors/P0_Energie_total_diag/Ecojoko_mini_maxi/Ecojoko_mini_maxi_avg_1h.yaml` |
| Vignette d'accès | `docs/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md` |

---

← Retour : `docs/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md` | → Pages liées : `PAGE_ENERGIE_TEMPS_REEL.md` · `PAGE_ENERGIE_MENSUEL.md`
