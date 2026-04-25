<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--23-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `Dashboard/L2C1_Energie/page_L2C1_energie_2026-04-23.yaml` |
| 🔗 **Accès depuis** | Vignette L2C1 → Dashboard HOME → tap → `/dashboard-tablette/energie` |
| 🔗 **Liens vers** | Badge "Réel" → `/dashboard-tablette/energie-temps-reel` · Badge "Cumul Jrs" → `/dashboard-tablette/energie-mensuel` |
| 🏗️ **Layout** | `type: grid` (column_span: 1) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-23 |
| 🏠 **Version HA** | 2026.3.x |

---

# ⚡ PAGE ÉNERGIE HOME — DOCUMENTATION COMPLÈTE

> ⚠️ **[2026-04-23] Refonte structure onglets** : L'overlay 7 jours et le tableau Linky sont déplacés dans l'onglet HEBDOMADAIRE. L'onglet JOURNALIER ne contient plus que la conso 24h + pie + slider + synthèse.

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
- Puissance instantanée NODON (Mini kWh / Temps réel W / Maxi kWh) via ring-tile-card
- Flux Enedis → Maison via energy-overview-card (source : capteur NODON brut)
- Ratios Linky A-1 / Semaine / Annuel
- Coûts journaliers et mensuels HP/HC détaillés (UM Genelec Appart × tarif EDF Tempo Bleu)
- Pie charts HP/HC + sliders de rentabilité HC
- Graphique 24h temps réel + moyennes glissantes
- Historique 7 jours superposé (offset ApexCharts — source : UM quotidien NODON)
- Tableau Linky 8 jours (coût + HP/HC)
- Graphique mensuel par jours
- Synthèse par postes (7 catégories, jour + mois) avec donut

### Intégrations requises

- ✅ **NODON** (smart plug général appartement) — `sensor.general_electric_appart_*`
- ✅ **Riemann tampon** — `sensor.genelec_appart_totale_kwh` (source des UM)
- ✅ **UM Genelec Appart** — `sensor.genelec_appart_*_kwh_um` et `sensor.genelec_appart_hphc_*_um_hp/hc`
- ✅ **MyElectricalData / Linky** (`linky_card`) — `sensor.linky_*`
- ✅ **tarif_edf** (custom component) — `sensor.edf_tempo_price_blue_hp` / `sensor.edf_tempo_price_blue_hc`
- ✅ Sensors Genelec Appart mini/maxi — `sensor.genelec_appart_conso_mini_24h` / `sensor.genelec_appart_conso_maxi_24h` (via `Genelec_appart_mini_maxi_avg.yaml`)

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
│  │ (kWh)  │   │  (W)   │   │ (kWh)  │              │
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
│  │  (HEBDOMADAIRE uniquement :)                 │   │
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
      entity: sensor.general_electric_appart_power
      name: Réel
      color: green
      tap_action:
        action: navigate
        navigation_path: /dashboard-tablette/energie-temps-reel
    - type: entity
      entity: sensor.general_electric_appart_energy
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
- Badge **Réel** : Puissance instantanée NODON (W) — tap → `/dashboard-tablette/energie-temps-reel`
- Badge **Cumul Jrs** : Énergie cumulée brute NODON (kWh) — tap → `/dashboard-tablette/energie-mensuel`
- Navigation retour : Clic titre → `/dashboard-tablette/0` (dashboard HOME)

> **Pages liées** : `energie-temps-reel` et `energie-mensuel` sont 2 pages séparées. Documentation : `PAGE_ENERGIE_TEMPS_REEL.md` et `PAGE_ENERGIE_MENSUEL.md`.

### Entités
- `sensor.general_electric_appart_power` [NODON - UI] Puissance instantanée (W)
- `sensor.general_electric_appart_energy` [NODON - UI] Énergie cumulée brute (kWh)

---

## 🔴 SECTION RING TILES — Mini / Réel / Maxi

Grid 3 colonnes. Chaque ring-tile est un indicateur circulaire avec arc de couleur dynamique.

```yaml
- square: false
  type: grid
  columns: 3
  cards:
    - type: custom:ring-tile    # Mini (kWh)
    - type: custom:ring-tile    # Réel (W)
    - type: custom:ring-tile    # Maxi (kWh)
```

### Ring-tile : Conso. Mini (kWh — talon reset minuit)

| Paramètre | Valeur |
|-----------|--------|
| `entity` | `sensor.genelec_appart_conso_mini_24h` |
| `min` | 0 |
| `max` | 20 |
| `max_decimals` | 3 |
| `ring_type` | `open` |

**Palette couleur :**

| Seuil (kWh) | Couleur | Signification |
|-------------|---------|---------------|
| 0–7.99 | Vert | Normal (en pratique toujours 0) |
| 8–14.99 | Vert | — |
| ≥ 15 | Orange | Anormal — sensor à vérifier |

> `genelec_appart_conso_mini_24h` = `value_min` sur 24h de `sensor.genelec_appart_quotidien_kwh_um`.
> **Valeur toujours 0** — l'UM repart de 0 à minuit et ne peut que croître. Sert de marqueur de reset.
> Source : `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml`

---

### Ring-tile : Conso. Temps Réel (W)

| Paramètre | Valeur |
|-----------|--------|
| `entity` | `sensor.general_electric_appart_power` |
| `min` | 0 |
| `max` | 6000 |

**Palette couleur :**

| Seuil (W) | Couleur | Signification |
|-----------|---------|---------------|
| 0–1 699 | Vert | Consommation normale |
| 2 000–3 699 | Orange | Consommation élevée |
| ≥ 4 000 | Rouge | Forte consommation (clim + tout) |

---

### Ring-tile : Conso. Maxi (kWh — total journalier accumulé)

| Paramètre | Valeur |
|-----------|--------|
| `entity` | `sensor.genelec_appart_conso_maxi_24h` |
| `min` | 0 |
| `max` | 20 |
| `max_decimals` | 3 |

**Palette couleur :**

| Seuil (kWh) | Couleur | Signification |
|-------------|---------|---------------|
| 0–7.99 | Vert | Journée économique |
| 8–14.99 | Vert | Journée normale |
| 15–17.99 | Orange | Journée élevée |
| ≥ 18 | Rouge | Journée très élevée |

> `genelec_appart_conso_maxi_24h` = `value_max` sur 24h de `sensor.genelec_appart_quotidien_kwh_um`.
> Représente le **total journalier kWh accumulé** (pic = valeur courante de l'UM).
> Source : `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml`

---

## ⚡ SECTION ENERGY OVERVIEW

```yaml
- type: vertical-stack
  cards:
    - type: custom:vertical-stack-in-card
      cards:
        - type: custom:energy-overview-card
          entities:
            - power: sensor.general_electric_appart_energy
              current: sensor.general_electric_appart_power
              label_leading: Enedis
              label_trailing: Maison
              icon_leading: mdi:transmission-tower
              icon_trailing: mdi:home-lightning-bolt
              color: "#488fc2"
              animation:
                power: 1000
                min_duration: 1
                max_duration: 5
```

### Rôle
Affiche un flux animé Enedis → Maison. La vitesse d'animation est proportionnelle à la consommation (seuil : 1 000 W, durée 1–5s).

### Entités
- `sensor.general_electric_appart_energy` [NODON - UI] Énergie cumulée brute (kWh) — champ `power` de la carte
- `sensor.general_electric_appart_power` [NODON - UI] Puissance instantanée (W) — champ `current`

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

La zone principale de la page est une `custom:tabbed-card` englobant les 3 périodes de suivi.

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
    - attributes:
        label: HEBDOMADAIRE
        icon: mdi:calendar-week
    - attributes:
        label: MENSUEL
        icon: mdi:calendar-month
```

**Propriétés communes :**
- Couleur active : `#FFB347` (orange chaleureux)
- Onglets inactifs : blanc 60% opacité
- Swipe activé (`swipeable: true`) — navigation tactile
- Animation de transition (`animated: true`)

---

### Onglet JOURNALIER

Période : jour en cours (remise à zéro à minuit).

**1. Coût Quotidien** — 2 rangées de 3 entités (kWh + €)

| Entité | Type | Rôle |
|--------|------|------|
| `sensor.genelec_appart_quotidien_kwh_um` | entity | Total kWh quotidien (UM) |
| `sensor.genelec_appart_hphc_quotidien_um_hp` | entity | H.P. kWh quotidien (UM HP) |
| `sensor.genelec_appart_hphc_quotidien_um_hc` | entity | H.C. kWh quotidien (UM HC) |
| `sensor.genelec_appart_cout_total_quotidien` | entity | Coût total € quotidien |
| `sensor.genelec_appart_cout_hp_quotidien` | entity | H.P. € quotidien |
| `sensor.genelec_appart_cout_hc_quotidien` | entity | H.C. € quotidien |

> Sources UM total : `utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml`
> Sources UM HP/HC : `utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml`
> Sources coûts : `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml`

**2. Pie Chart HP/HC journalier (ApexCharts)**

```yaml
chart_type: pie
graph_span: 24h
span:
  start: day
series:
  - entity: sensor.genelec_appart_hphc_quotidien_um_hp
    name: Heure pleine
    color: rgb(211, 58, 79)
  - entity: sensor.genelec_appart_hphc_quotidien_um_hc
    name: Heure creuse
    color: rgb(72, 132, 213)
```

**3. Slider Rentabilité HC quotidien (Button-card)**

**Entité :** `sensor.genelec_appart_ratio_hc_quotidien`

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
| Conso. temps réel | `sensor.general_electric_appart_power` | area | Courbe puissance instantanée (W) |
| Moy. glissante 24h | `sensor.general_electric_appart_power` | line | `func: avg, duration: 24h` |
| Moy. depuis minuit | `sensor.genelec_appart_avg_watts_quotidien` | line | Axe secondaire |
| Moy. 1er du mois | `sensor.genelec_appart_avg_watts_mensuel` | — | En-tête uniquement (`in_chart: false`) |

Double axe Y : `TempsReel` (gauche — W) / `Minuit` (droite).

**5. Synthèse Usages Journaliers + Donut**

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
| `sensor.genelec_appart_hebdomadaire_kwh_um` | Total kWh hebdo (UM) |
| `sensor.genelec_appart_hphc_hebdomadaire_um_hp` | H.P. kWh hebdo (UM HP) |
| `sensor.genelec_appart_hphc_hebdomadaire_um_hc` | H.C. kWh hebdo (UM HC) |
| `sensor.genelec_appart_cout_total_hebdomadaire` | Coût total € hebdo |
| `sensor.genelec_appart_cout_hp_hebdomadaire` | H.P. € hebdo |
| `sensor.genelec_appart_cout_hc_hebdomadaire` | H.C. € hebdo |

> Source UM total : `utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml`
> Source UM HP/HC : `utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml`
> Source coûts : `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml`

**2. Pie Chart HP/HC hebdomadaire**

```yaml
chart_type: pie
graph_span: 7d
span:
  start: week
series:
  - entity: sensor.genelec_appart_hphc_hebdomadaire_um_hp
    color: rgb(211, 58, 79)
  - entity: sensor.genelec_appart_hphc_hebdomadaire_um_hc
    color: rgb(72, 132, 213)
```

**3. Slider Rentabilité HC hebdomadaire**

**Entité :** `sensor.genelec_appart_ratio_hc_hebdomadaire` — même structure que le slider journalier.

**4. Historique 7 jours superposé (Overlay — ApexCharts)**

Principe : 8 séries sur `sensor.genelec_appart_quotidien_kwh_um` avec `offset` décalant la fenêtre de lecture. Chaque courbe représente un jour complet de 0 → total kWh, toutes alignées sur le même axe 24h.

```yaml
graph_span: 24h
span:
  end: day
experimental:
  color_threshold: true
cache: true
```

| Série | Offset | Couleur |
|-------|--------|---------|
| Aujourd'hui | aucun | `gainsboro` (stroke_width: 3) |
| J-1 | `-1d` | `rgb(204, 255, 204)` |
| J-2 | `-2d` | `rgb(153, 255, 153)` |
| J-3 | `-3d` | `rgb(102, 255, 102)` |
| J-4 | `-4d` | `rgb(51, 204, 51)` |
| J-5 | `-5d` | `rgb(0, 153, 0)` |
| J-6 | `-6d` | `rgb(0, 102, 0)` |
| J-7 | `-7d` | `rgb(0, 70, 0)` |

`extend_to: false` sur toutes les séries. `group_by: func: last, duration: 10m`. DataLabels activés. Recorder HA ≥ 8 jours requis.

**5. Tableau Linky 8 jours (flex-table-card)**

```yaml
entities:
  - sensor.linky_jour_0   # Aujourd'hui (NODON temps réel)
  - sensor.linky_jour_7   # J-7
  - sensor.linky_jour_1 … sensor.linky_jour_6
columns: Jour | Total (kWh) | Coût (€) | HP (kWh) | HC (kWh)
```

> `linky_jour_0` = conso NODON du jour en temps réel. `linky_jour_1-7` = attributs Linky (Wh ÷ 1000). Source : `templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml`

**6. Synthèse Usages Hebdomadaires + Donut**

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

| Entité | Type | Rôle |
|--------|------|------|
| `sensor.genelec_appart_mensuel_kwh_um` | entity | Total kWh mensuel (UM) |
| `sensor.genelec_appart_hphc_mensuel_um_hp` | entity | H.P. kWh mensuel (UM HP) |
| `sensor.genelec_appart_hphc_mensuel_um_hc` | entity | H.C. kWh mensuel (UM HC) |
| `sensor.genelec_appart_cout_total_mensuel` | entity | Coût total € mensuel |
| `sensor.genelec_appart_cout_hp_mensuel` | entity | H.P. € mensuel |
| `sensor.genelec_appart_cout_hc_mensuel` | entity | H.C. € mensuel |

> Source UM total : `utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml`
> Source UM HP/HC : `utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml`
> Source coûts : `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml`

**2. Pie Chart HP/HC mensuel**

```yaml
chart_type: pie
graph_span: 1month
span:
  start: month
series:
  - entity: sensor.genelec_appart_hphc_mensuel_um_hp
    color: rgb(211, 58, 79)
  - entity: sensor.genelec_appart_hphc_mensuel_um_hc
    color: rgb(72, 132, 213)
```

**3. Slider Rentabilité HC mensuel**

**Entité :** `sensor.genelec_appart_ratio_hc_mensuel` — même structure que le slider journalier.

**4. Graphique Mensuel par Jours (ApexCharts)**

```yaml
graph_span: 31d
cache: true
span:
  start: month
```

| Série | Entité | Type | Axe | Rôle |
|-------|--------|------|-----|------|
| Conso. ce jour | `sensor.genelec_appart_avg_watts_quotidien` | column | `daily` | Barres kWh (`func: max, duration: 24h`) |
| Moy. glissante mois | `sensor.genelec_appart_totale_kwh` | line | `daily` | `func: avg, duration: 730h` |
| Moy. depuis minuit | `sensor.genelec_appart_avg_watts_quotidien` | line | `moyenne` | Axe secondaire |
| Moy. 1er du mois | `sensor.genelec_appart_avg_watts_mensuel` | — | `daily` | En-tête uniquement (`in_chart: false`) |

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

### ⚡ NODON — Puissance & Énergie brute

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.general_electric_appart_power` | Puissance instantanée (W) | Smart plug NODON [UI] |
| `sensor.general_electric_appart_energy` | Énergie cumulée brute (kWh) | Smart plug NODON [UI] |

---

### 🔄 Riemann tampon

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.genelec_appart_totale_kwh` | kWh local stable (Riemann left) — source des UM | `sensors/P0_Energie_total_diag/Genelec_appart/P0_kWh_genelec_appart.yaml` |

---

### 📈 Statistiques P0 — Mini / Maxi / Moyennes

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.genelec_appart_conso_mini_24h` | `value_min` 24h UM quotidien — toujours 0 (reset minuit) | `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml` |
| `sensor.genelec_appart_conso_maxi_24h` | `value_max` 24h UM quotidien — total journalier kWh | idem |
| `sensor.genelec_appart_conso_moyenne_1h` | `mean` 1h UM quotidien — conso lissée (kWh) | idem |
| `sensor.genelec_appart_avg_watts_quotidien` | Moyenne Watts depuis minuit | `templates/P0_Energie_total_diag/Genelec_appart/03_AVG_genelec_appart.yaml` |
| `sensor.genelec_appart_avg_watts_hebdomadaire` | Moyenne Watts depuis lundi | idem |
| `sensor.genelec_appart_avg_watts_mensuel` | Moyenne Watts depuis le 1er du mois | idem |
| `sensor.genelec_appart_avg_watts_annuel` | Moyenne Watts depuis le 1er janvier | idem |

---

### 🔢 Utility Meters — Total kWh (sans split HP/HC)

| Entité | Cycle | Source |
|--------|-------|--------|
| `sensor.genelec_appart_quotidien_kwh_um` | daily | `utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml` |
| `sensor.genelec_appart_hebdomadaire_kwh_um` | weekly | idem |
| `sensor.genelec_appart_mensuel_kwh_um` | monthly | idem |
| `sensor.genelec_appart_annuel_kwh_um` | yearly | idem |

---

### 🔢 Utility Meters — HP/HC (avec split tarifaire)

| Entité | Cycle | Tarif | Source |
|--------|-------|-------|--------|
| `sensor.genelec_appart_hphc_quotidien_um_hp` | daily | HP | `utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml` |
| `sensor.genelec_appart_hphc_quotidien_um_hc` | daily | HC | idem |
| `sensor.genelec_appart_hphc_hebdomadaire_um_hp` | weekly | HP | idem |
| `sensor.genelec_appart_hphc_hebdomadaire_um_hc` | weekly | HC | idem |
| `sensor.genelec_appart_hphc_mensuel_um_hp` | monthly | HP | idem |
| `sensor.genelec_appart_hphc_mensuel_um_hc` | monthly | HC | idem |
| `sensor.genelec_appart_hphc_annuel_um_hp` | yearly | HP | idem |
| `sensor.genelec_appart_hphc_annuel_um_hc` | yearly | HC | idem |

> Basculement HP ↔ HC piloté par : `automations_corrige/energie/basculement_tarif_hphc.yaml`

---

### 💰 Coûts calculés (Templates)

| Entité | Période | Source |
|--------|---------|--------|
| `sensor.genelec_appart_cout_hp_quotidien` | Quotidien | `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml` |
| `sensor.genelec_appart_cout_hc_quotidien` | Quotidien | idem |
| `sensor.genelec_appart_cout_total_quotidien` | Quotidien | idem |
| `sensor.genelec_appart_cout_hp_hebdomadaire` | Hebdomadaire | idem |
| `sensor.genelec_appart_cout_hc_hebdomadaire` | Hebdomadaire | idem |
| `sensor.genelec_appart_cout_total_hebdomadaire` | Hebdomadaire | idem |
| `sensor.genelec_appart_cout_hp_mensuel` | Mensuel | idem |
| `sensor.genelec_appart_cout_hc_mensuel` | Mensuel | idem |
| `sensor.genelec_appart_cout_total_mensuel` | Mensuel | idem |
| `sensor.genelec_appart_cout_hp_annuel` | Annuel | idem |
| `sensor.genelec_appart_cout_hc_annuel` | Annuel | idem |
| `sensor.genelec_appart_cout_total_annuel` | Annuel | idem |

> Tarifs EDF Tempo Bleu : HP = `sensor.edf_tempo_price_blue_hp` (0.1494 €/kWh) · HC = `sensor.edf_tempo_price_blue_hc` (0.1232 €/kWh)

---

### 📐 Ratios HP/HC

| Entité | Période | Source |
|--------|---------|--------|
| `sensor.genelec_appart_ratio_hc_quotidien` | Quotidien (%) | `templates/P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml` |
| `sensor.genelec_appart_ratio_hc_hebdomadaire` | Hebdomadaire (%) | idem |
| `sensor.genelec_appart_ratio_hc_mensuel` | Mensuel (%) | idem |
| `sensor.genelec_appart_ratio_hc_annuel` | Annuel (%) | idem |

---

### 📡 Linky / MyElectricalData

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.linky_25481620821301_consumption` | Index Linky brut (ratios linky-card) | MyElectricalData [UI] |

### 🔢 Templates Linky — Tableau journalier (flex-table)

| Entité | Rôle | Source réelle |
|--------|------|---------------|
| `sensor.linky_jour_0` | Aujourd'hui : HP+HC (kWh) + coût (€) | **NODON** — `sensor.general_electric_appart_power` × tarif EDF Tempo Bleu |
| `sensor.linky_jour_1` à `sensor.linky_jour_7` | J-1 à J-7 : HP+HC (kWh) + coût + jour de semaine | **Attributs Linky** — `state_attr('sensor.linky_25481620821301_consumption', 'day_X_HP/HC')` + `dailyweek_cost` |

> Fichier source : `templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml`
> ⚠️ `linky_jour_0` n'est **pas** une donnée Linky — c'est la conso NODON du jour en temps réel (J0 = Aujourd'hui).
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

---

### 📊 Max dynamiques (échelle bar-card)

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.diag_max_poste_quotidien_dynamique` | Max du jour (pour échelle bar-card) | `templates/P0_Energie_total_diag/Diag/` |
| `sensor.diag_max_poste_hebdomadaire_dynamique` | Max de la semaine | idem |
| `sensor.diag_max_poste_mensuel_dynamique` | Max du mois | idem |

---

## 🐛 DÉPANNAGE

### Les ring-tiles Mini/Maxi affichent "unavailable"
1. Vérifier que `sensor.genelec_appart_conso_mini_24h` et `sensor.genelec_appart_conso_maxi_24h` existent dans Outils de développement > États
2. Ces sensors sont des `platform: statistics` sur `sensor.genelec_appart_quotidien_kwh_um` — vérifier que l'UM quotidien est actif
3. La moyenne 1h peut être indisponible pendant les 60 premières minutes après redémarrage HA
4. Source : `sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml`

### Le ring-tile Mini affiche toujours 0
C'est **normal**. `value_min` sur 24h d'un UM qui repart de 0 à minuit sera toujours 0. Ce champ sert de marqueur visuel de reset plutôt que de donnée opérationnelle.

### Les coûts affichent 0 ou "unknown"
1. Vérifier que `sensor.genelec_appart_cout_total_quotidien` (et `_hp`, `_hc`) existent dans États
2. Vérifier les UM HP/HC dans `03_UM_genelec_appart_HPHC_AMHQ.yaml`
3. Vérifier que l'automation de basculement HP/HC est active
4. Source coûts pré-calculés : `templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml`

### Le graphique overlay 7 jours (onglet HEBDOMADAIRE) ne montre pas tous les jours
1. Le recorder HA doit avoir au moins 7 jours d'historique pour `sensor.genelec_appart_quotidien_kwh_um`
2. Vérifier `configuration.yaml` → paramètre `recorder: purge_keep_days:` (doit être ≥ 8)
3. L'UM a été créé récemment → les données historiques ne remontent qu'à sa date de création

### Le graphique Moy. glissante (onglet MENSUEL) ne s'affiche pas
Source : `sensor.genelec_appart_totale_kwh` (Riemann tampon). Ce sensor démarre à 0 à la création — il n'y a pas de back-fill historique. Attendre quelques jours pour avoir un historique suffisant.

### Le pie chart HP/HC affiche une seule tranche
Normal si aucune consommation HC aujourd'hui (hors plage horaire HC). Vérifier les plages HC et l'automation de basculement.

### Les donuts SYNTHÈSE USAGES affichent des valeurs incohérentes
1. Vérifier que les sensors `diag_poste_hygiene_quotidien`, etc. existent dans États
2. Source : `templates/P0_Energie_total_diag/Diag/` — vérifier les fichiers source

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| Smart plug NODON (appartement général) | Intégration HA [UI] | ✅ Essentiel |
| `sensor.genelec_appart_totale_kwh` (Riemann) | Sensor integration | ✅ Essentiel — tampon NODON |
| UM Genelec Appart (01 + 03) | Utility Meter | ✅ Essentiel — kWh + HP/HC |
| `01_genelec_appart_AMHQ_cost.yaml` (templates) | Template coûts | ✅ Requis — fournit `cout_total/hp/hc_*` |
| Automation basculement HP/HC | HA Automation | ✅ Requis — split HP/HC correct |
| MyElectricalData / Linky | HACS Integration | ✅ Requis pour ratios + tableau |
| `ring-tile-card` | HACS Frontend | ✅ Essentiel (Mini/Réel/Maxi) |
| `tabbed-card` | HACS Frontend | ✅ Essentiel (onglets) |
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
| Dashboard YAML corrigé | `Dashboard/L2C1_Energie/page_L2C1_energie_2026-04-23.yaml` |
| Riemann tampon NODON | `TREE_CORRIGE/sensors/P0_Energie_total_diag/Genelec_appart/P0_kWh_genelec_appart.yaml` |
| UM kWh total AMHQ | `TREE_CORRIGE/utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ_cost.yaml` |
| UM HP/HC AMHQ | `TREE_CORRIGE/utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml` |
| Statistiques mini/maxi/moy | `TREE_CORRIGE/sensors/P0_Energie_total_diag/Genelec_appart/Genelec_appart_mini_maxi_avg.yaml` |
| Coûts HP/HC (12 sensors) | `TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml` |
| Ratios HC (4 sensors) | `TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml` |
| Moyennes AVG Watts | `TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/03_AVG_genelec_appart.yaml` |
| Diag postes (jour/hebdo/mois) | `TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/` |
| Linky / MyElectricalData | `TREE_CORRIGE/templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml` |
| Vignette d'accès | `docs DashBoard/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md` |

---

← Retour : `docs DashBoard/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md` | → Pages liées : `PAGE_ENERGIE_TEMPS_REEL.md` · `PAGE_ENERGIE_MENSUEL.md`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L2C1_VIGNETTE_ENERGIE]]  [[PAGE_ENERGIE_MENSUEL]]  [[PAGE_ENERGIE_TEMPS_REEL]]*
