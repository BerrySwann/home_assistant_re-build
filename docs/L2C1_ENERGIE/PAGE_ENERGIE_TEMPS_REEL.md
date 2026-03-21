<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--20-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/page_energie_temps_reel.yaml` |
| 🔗 **Accès depuis** | Badge "Réel" de `page_energie_home.yaml` → `/dashboard-tablette/energie-temps-reel` |
| 🔗 **Retour vers** | Tap titre → `/dashboard-tablette/energie` |
| 🏗️ **Layout** | `type: grid` — 4 colonnes `column_span: 1` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-20 |
| 🏠 **Version HA** | 2026.3.x |

---

# ⚡ PAGE ÉNERGIE TEMPS RÉEL — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Col 1 — HEADER + Sections conditionnelles par catégorie](#col-1--header--sections-conditionnelles-par-catégorie)
4. [Col 2 — Donut journalier (cumul depuis minuit)](#col-2--donut-journalier-cumul-depuis-minuit)
5. [Col 3 — ApexCharts 24h (conso instantanée)](#col-3--apexcharts-24h-conso-instantanée)
6. [Col 4 — Tabbed-card par pièce (streamline)](#col-4--tabbed-card-par-pièce-streamline)
7. [Entités utilisées](#entités-utilisées--provenance-complète)
8. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Cette page offre une vue **temps réel** de la consommation électrique appareil par appareil, organisée en **4 colonnes** côte à côte :
- **Col 1** : Heading + 7 sections conditionnelles par catégorie (Chauffage, Multimédia, Cuisson, Froid, Hygiène, Lumière, Autres) — n'affiche que les catégories avec puissance > 0W
- **Col 2** : Donut de répartition par appareil sur la journée (kWh cumulés depuis minuit)
- **Col 3** : Courbe instantanée par appareil sur 24h (W)
- **Col 4** : Détail par pièce via onglets : puissance instantanée + moyenne + kWh du jour par appareil

### Intégrations requises

- ✅ **Zigbee2MQTT (Z2M)** — toutes les prises IKEA et NOUS sans pont : `sensor.prise_*_power` / `sensor.prise_*_current`
- ✅ **Sonoff** — `sensor.relais_*_power` (lumière SDB via relais Z2M)
- ✅ **Philips Hue** — `sensor.hue_*_power` / `sensor.lampe_*_hue_power`
- ✅ **Sensors calculés P2** — `sensor.*_quotidien_kwh_um` (Utility Meters quotidiens)
- ✅ **Sensors calculés AVG** — `sensor.*_avg_watts_quotidien` (moyennes glissantes quotidiennes)
- ✅ **custom:streamline-card** (HACS) — template `conso_temps_reel_appareil`
- ✅ **custom:tabbed-card** (HACS) — navigation par pièce

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `bar-card` + `auto-entities` | Prises et lumières actives triées dynamiquement |
| `apexcharts-card` (donut) | Répartition kWh par appareil depuis minuit |
| `apexcharts-card` (area) | Courbe W par appareil sur 24h |
| `tabbed-card` | Navigation par pièce |
| `streamline-card` | Template réutilisable par appareil |
| `card-mod` | Suppression bordures/ombres |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
type: grid  (4 colonnes — column_span: 1 chacune)

┌──────────────────┬──────────────────┬──────────────────┬──────────────────┐
│    COL 1         │    COL 2         │    COL 3         │    COL 4         │
│  [HEADER]        │  [DONUT]         │  [ApexCharts]    │ [bubble-card sep]│
│  Temps Réél      │  Cumul depuis    │  Conso.          │ Sélectionner     │
│  ← tap /energie  │  Minuit (Wh)     │  Instantanée     │ une pièce        │
│  ──────────────  │  18 prises ×     │  (W) 24h         │  ──────────────  │
│  [conditional]   │  transform ×1000 │  18 prises ×     │ [TABBED-CARD]    │
│  Chauffage (W)   │  kWh → Wh        │  _power          │ ┌──┬──┬──┬──┬──┐ │
│  si > 0W ───>   │  + all_standby   │  fill_raw: last  │ │1.│4.│5.│7.│9.│V│ │
│  bar-card        │                  │  group_by: 10m   │ │En│Sa│Cu│Bu│Ch│e│ │
│  [conditional]   │                  │                  │ └──┴──┴──┴──┴──┘ │
│  Multimédia (W)  │                  │                  │ [streamline-card] │
│  si > 0W ───>   │                  │                  │ template:         │
│  bar-card        │                  │                  │ conso_temps_reel  │
│  [conditional]   │                  │                  │ _appareil         │
│  Cuisson (W)     │                  │                  │ W + A + Moy + kWh │
│  [conditional]   │                  │                  │                   │
│  Froid (W)       │                  │                  │                   │
│  [conditional]   │                  │                  │                   │
│  Hygiène (W)     │                  │                  │                   │
│  [conditional]   │                  │                  │                   │
│  Lumière (W)     │                  │                  │                   │
│  [conditional]   │                  │                  │                   │
│  Autres (W)      │                  │                  │                   │
└──────────────────┴──────────────────┴──────────────────┴──────────────────┘
```

> **Principe Col 1** : Chaque catégorie est une `type: conditional` — visible uniquement si `sensor.total_poste_*_puissance ≠ "0"`. La colonne ne montre que les postes actifs au moment de la consultation.

> **Séparateur horizontal** : Un `type: markdown` de 1px blanc semi-transparent (`rgba(255,255,255,0.4)`) sert de diviseur visuel entre les catégories en Col 1.

---

## 📍 COL 1 — HEADER + Sections conditionnelles par catégorie

### Header

```yaml
- type: heading
  icon: mdi:lightning-bolt
  heading: Temps Réél
  heading_style: title
  badges:
    - type: entity
      entity: sensor.ecojoko_consommation_temps_reel
      name: Réel
      color: green
      show_state: true
      show_icon: true
  tap_action:
    action: navigate
    navigation_path: /dashboard-tablette/energie
```

> ⚠️ Typo dans le titre original : "Temps Réél" (double accent) — conservé tel quel pour cohérence avec le YAML en production.

**Entité :** `sensor.ecojoko_consommation_temps_reel` [Ecojoko - UI] Puissance instantanée totale (W)

---

### 7 sections conditionnelles (bar-card par catégorie)

Chaque section est un `type: conditional` avec les conditions :
- `sensor.total_poste_*_puissance` state_not `"0"` (ET)
- `sensor.total_poste_*_puissance` state_not `unavailable`

Quand la condition est vraie, s'affiche un `heading` avec badge + `auto-entities bar-card` listant les appareils de la catégorie (état > 1W, triés décroissant) + séparateur `markdown` 1px.

**Palette couleur commune (bar-card catégories) :**

| Seuil | Couleur |
|-------|---------|
| 0–4 W | `gainsboro` (veille) |
| 5–249 W | `#4caf50` (vert) |
| 250–749 W | `#FFCC99` (orange clair) |
| ≥ 750 W | `#ff4444` (rouge) |

#### Section 1 : Chauffage

| Sensor déclencheur | `sensor.total_poste_chauffage_puissance` |
| Badge icône | `mdi:hvac` — couleur orange |
| Appareils | clim_salon_nous_power, radiateur_elec_cuisine_power, clim_bureau_nous_power, prise_soufflant_salle_de_bain_nous_power, prise_seche_serviette_salle_de_bain_nous_power, clim_chambre_nous_power |

#### Section 2 : Multimédia

| Sensor déclencheur | `sensor.total_poste_multimedia_puissance` |
| Badge icône | `mdi:monitor-screenshot` — couleur blue |
| Appareils | prise_box_internet_ikea_power, prise_tv_salon_ikea_power, prise_tv_chambre_nous_power, prise_pc_s_gege_ikea_power, prise_bureau_pc_ikea_power |

#### Section 3 : Cuisson

| Sensor déclencheur | `sensor.total_poste_cuisine_puissance` |
| Badge icône | `mdi:stove` — couleur red |
| Appareils | prise_four_micro_ondes_nous_power, prise_petit_dejeune_nous_power, prise_airfryer_ninja_nous_power, four_et_plaque_de_cuisson_power |

#### Section 4 : Froid

| Sensor déclencheur | `sensor.total_poste_froid_puissance` |
| Badge icône | `mdi:fridge-outline` — couleur cyan |
| Appareils | prise_frigo_cuisine_nous_power, prise_congelateur_cuisine_nous_power |

#### Section 5 : Hygiène

| Sensor déclencheur | `sensor.total_poste_hygiene_puissance` |
| Badge icône | `mdi:bubbles` — couleur teal |
| Appareils | prise_lave_linge_nous_power, prise_lave_vaisselle_nous_power |

#### Section 6 : Lumière

| Sensor déclencheur | `sensor.total_poste_lumiere_puissance` *(ou équivalent)* |
| Badge icône | `mdi:lightbulb` — couleur yellow |
| Appareils | Ampoules Hue actives + relais Sonoff SDB |

#### Section 7 : Autres

| Sensor déclencheur | `sensor.total_poste_autres_puissance` *(ou équivalent)* |
| Badge icône | `mdi:account` |
| Appareils | Divers (Fer à repasser, etc.) |

---

## 🥧 COL 2 — Donut journalier (cumul depuis minuit)

```yaml
- type: custom:apexcharts-card
  chart_type: donut
  cache: true
  apex_config:
    chart:
      height: 580px
  header:
    title: Conso. journalière (Cumul depuis Minuit )
  all_series_config:
    show:
      legend_value: false
      extremas: false
  series:
    - entity: sensor.prise_box_internet_ikea_quotidien_kwh_um
      transform: return x * 1000;
      unit: Wh
      name: Box (+)
      color: gainsboro
    # ... 16 autres appareils
    - entity: sensor.all_standby_quotidien_kwh_um
      transform: return x * 1000;
      unit: Wh
      name: Veilles
      color: grey
```

### Principe
- **Source** : Utility Meters quotidiens (`_quotidien_kwh_um`) — se remettent à 0 à minuit
- **Transform** : `× 1000` pour convertir kWh → Wh (meilleure lisibilité pour les petits appareils)
- **18 séries** : 17 prises individuelles + 1 TV Salon + `sensor.all_standby_quotidien_kwh_um`
- Pas de `graph_span` / `span` → lecture directe de l'état actuel des UM

### Palette de couleurs (18 appareils)

| Appareil | Entité UM | Couleur |
|----------|-----------|---------|
| Box Internet | `prise_box_internet_ikea_quotidien_kwh_um` | gainsboro |
| Horloge Entrée | `prise_horloge_ikea_quotidien_kwh_um` | `rgb(183, 183, 183)` |
| PCg (Géraldine) | `prise_pc_s_gege_ikea_quotidien_kwh_um` | `rgb(174, 68, 90)` |
| Chargeurs Salon | `prise_salon_chargeur_nous_quotidien_kwh_um` | `rgb(196, 75, 97)` |
| TV Salon | `prise_tv_salon_ikea_quotidien_kwh_um` | `rgb(215,95,115)` |
| Four Micro-Ondes | `prise_four_micro_ondes_nous_quotidien_kwh_um` | `rgb(98,78,136)` |
| Petit Déjeuner | `prise_petit_dejeune_nous_quotidien_kwh_um` | `rgb(118,93,160)` |
| Lave-Linge | `prise_lave_linge_nous_quotidien_kwh_um` | `rgb(137,103,179)` |
| Lave-Vaisselle | `prise_lave_vaisselle_nous_quotidien_kwh_um` | `rgb(129,116,180)` |
| Airfryer | `prise_airfryer_ninja_nous_quotidien_kwh_um` | `rgb(142,122,181)` |
| Four & Plaque | `four_et_plaque_de_cuisson_quotidien_kwh_um` | `rgb(162,148,249)` |
| Frigo | `prise_frigo_cuisine_nous_quotidien_kwh_um` | `cyan` |
| Congélateur | `prise_congelateur_cuisine_nous_quotidien_kwh_um` | `rgb(0, 255, 255)` ← `cyan` |
| PCe (Bureau) | `prise_bureau_pc_ikea_quotidien_kwh_um` | `orange` |
| Fer à Repasser | `prise_bureau_fer_a_repasser_nous_quotidien_kwh_um` | `gold` |
| Têtes de lit | `prise_tete_de_lit_chambre_quotidien_kwh_um` | `rgb(75, 130, 85)` |
| TV Chambre | `prise_tv_chambre_nous_quotidien_kwh_um` | `rgb(105, 155, 110)` |
| Veilles | `all_standby_quotidien_kwh_um` | `rgb(109, 76, 65)` |

> ⚠️ **[modif 2026-03-20]** : Couleurs mises à jour — PCg `rgb(202,135,135)` → `rgb(174,68,90)`, Chargeurs `rgb(174,68,90)` → `rgb(196,75,97)`, Congél `rgb(19,160,255)` → `rgb(0,255,255)` (cyan), Têtes de Lit `rgb(177,194,158)` → `rgb(75,130,85)`, TV Chambre `rgb(30,81,40)` → `rgb(105,155,110)`, Veilles `grey` → `rgb(109,76,65)`.

> Sources UM : `utility_meter/P2_prise/P2_UM_AMHQ.yaml` (quotidien cycle)

---

## 📈 COL 3 — ApexCharts 24h (conso instantanée)

```yaml
- type: custom:apexcharts-card
  graph_span: 24h
  cache: false
  update_interval: 1m
  apex_config:
    chart:
      height: 300px
  header:
    title: Conso. Instantanée
  yaxis:
    - id: Watts
      min: 0
      max: auto
      opposite: true
      apex_config:
        tickAmount: 4
  all_series_config:
    group_by:
      func: last
      duration: 10m
    show:
      legend_value: false
      extremas: true
  series:
    # 17 appareils + all_standby
    - entity: sensor.prise_box_internet_ikea_power
      name: Box (+)
      yaxis_id: Watts
      unit: W
      fill_raw: last   # ← maintient la dernière valeur connue (pas de null)
    # ...
```

### Paramètres clés
- `update_interval: 1m` — rafraîchissement forcé toutes les minutes
- `cache: false` — pas de cache (données en direct)
- `fill_raw: last` — évite les trous dans les courbes (maintient la dernière valeur)
- `group_by: func: last, duration: 10m` — lisse sur 10 min
- Axe Y unique `Watts` côté droit, auto-scale

### Même 18 appareils + Veilles que le Donut

Même palette de couleurs que le donut (cohérence visuelle).

---

## 📱 COL 4 — Tabbed-card par pièce (streamline)

```yaml
- type: custom:bubble-card
  card_type: separator
  name: 'Sélectionner une pièce :'
  icon: mdi:arrow-right-bottom-bold
  rows: 2

- type: custom:tabbed-card
  styles:
    "--mdc-theme-primary": white
    "--mdc-tab-text-label-color-default": rgba(255, 255, 255, 0.25)
  options: {}
  tabs:
    - attributes:
        label: 1. Entrée
        icon: mdi:door
      card: ...
```

### 6 onglets (labels numériques conformes à la nomenclature pièces)

| Onglet | Icône | Appareils |
|--------|-------|-----------|
| `1. Entrée` | `mdi:door` | Box Internet (Hue), Horloge Entrée (Chargeur) |
| `4. Salon` | `mdi:sofa` | PC's Géraldine, Prise Salon (Chargeurs/Vapote/Aspi.), TV Salon |
| `5. Cuisine` | `mdi:fridge` | Four Micro-Ondes, Petit Déjeuner, Lave-Linge, Lave-Vaisselle, Airfryer, Four & Plaque, Frigo, Congélateur |
| `7. Bureau` | `mdi:desk` | PCe Bureau, Fer à Repasser |
| `9. Chambre` | `mdi:bed` | Têtes de Lit chambre, TV Chambre |
| `Veilles` | `mdi:sleep` | All Standby |

> ⚠️ **[modif 2026-03-20]** : Les labels des onglets ont été préfixés par le numéro officiel de pièce (`Entrée` → `1. Entrée`, `Salon` → `4. Salon`, etc.) pour cohérence avec la nomenclature du projet. `Veilles` reste sans numéro (hors-pièce).

### Template `conso_temps_reel_appareil`

Chaque appareil utilise ce template streamline avec 5 variables :

| Variable | Rôle |
|----------|------|
| `card_title` | Nom affiché de l'appareil |
| `energy_entity` | `sensor.*_power` — puissance instantanée (W) |
| `energy_color` | Couleur cohérente avec donut/graphique |
| `current_entity` | `sensor.*_current` — intensité (A) |
| `avg_daily_entity` | `sensor.*_avg_watts_quotidien` — moyenne W depuis minuit |
| `conso_daily_kwh_entity` | `sensor.*_quotidien_kwh_um` — kWh depuis minuit |

> **Note** : Le template `conso_temps_reel_appareil` est défini dans le fichier de configuration streamline (non inclus dans le re-build à ce stade).

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 📊 Totaux par poste — Sensors conditionnels Col 1

| Entité | Poste | Usage |
|--------|-------|-------|
| `sensor.total_poste_chauffage_puissance` | Chauffage | Condition affichage section + badge |
| `sensor.total_poste_multimedia_puissance` | Multimédia | Condition affichage section + badge |
| `sensor.total_poste_cuisine_puissance` | Cuisson | Condition affichage section + badge |
| `sensor.total_poste_froid_puissance` | Froid | Condition affichage section + badge |
| `sensor.total_poste_hygiene_puissance` | Hygiène | Condition affichage section + badge |

> Ces sensors sont des sommes de puissances instantanées par catégorie — fournis par `templates/P2_prise/P2_I_all_standby_power/` ou `P1_clim_chauffage/`.

---

### ⚡ Prises Connectées — Puissance instantanée (W)

| Entité | Appareil | Intégration |
|--------|----------|-------------|
| `sensor.prise_box_internet_ikea_power` | Box Internet | Zigbee2MQTT [Z2M] |
| `sensor.prise_horloge_ikea_power` | Horloge Entrée | Zigbee2MQTT [Z2M] |
| `sensor.prise_pc_s_gege_ikea_power` | PC Géraldine | Zigbee2MQTT [Z2M] |
| `sensor.prise_salon_chargeur_nous_power` | Chargeurs Salon | Zigbee2MQTT [Z2M] |
| `sensor.prise_tv_salon_ikea_power` | TV Salon | Zigbee2MQTT [Z2M] |
| `sensor.prise_four_micro_ondes_nous_power` | Four Micro-Ondes | Zigbee2MQTT [Z2M] |
| `sensor.prise_petit_dejeune_nous_power` | Petit Déjeuner | Zigbee2MQTT [Z2M] |
| `sensor.prise_lave_linge_nous_power` | Lave-Linge | Zigbee2MQTT [Z2M] |
| `sensor.prise_lave_vaisselle_nous_power` | Lave-Vaisselle | Zigbee2MQTT [Z2M] |
| `sensor.prise_airfryer_ninja_nous_power` | Airfryer | Zigbee2MQTT [Z2M] |
| `sensor.four_et_plaque_de_cuisson_power` | Four & Plaque | Zigbee2MQTT [Z2M] |
| `sensor.prise_frigo_cuisine_nous_power` | Frigo | Zigbee2MQTT [Z2M] |
| `sensor.prise_congelateur_cuisine_nous_power` | Congélateur | Zigbee2MQTT [Z2M] |
| `sensor.prise_bureau_pc_ikea_power` | PCe Bureau | Zigbee2MQTT [Z2M] |
| `sensor.prise_bureau_fer_a_repasser_nous_power` | Fer à Repasser | Zigbee2MQTT [Z2M] |
| `sensor.prise_tete_de_lit_chambre_power` | Tête de lit | Zigbee2MQTT [Z2M] |
| `sensor.prise_tv_chambre_nous_power` | TV Chambre | Zigbee2MQTT [Z2M] |
| `sensor.all_standby_power` | Veilles totales | Template calculé [P2] |

---

### 🔢 Utility Meters Quotidiens (kWh)

> Source : `utility_meter/P2_prise/P2_UM_AMHQ.yaml`

| Entité | Appareil |
|--------|----------|
| `sensor.prise_box_internet_ikea_quotidien_kwh_um` | Box Internet |
| `sensor.prise_horloge_ikea_quotidien_kwh_um` | Horloge |
| `sensor.prise_pc_s_gege_ikea_quotidien_kwh_um` | PCg |
| `sensor.prise_salon_chargeur_nous_quotidien_kwh_um` | Chargeurs |
| `sensor.prise_tv_salon_ikea_quotidien_kwh_um` | TV Salon |
| `sensor.prise_four_micro_ondes_nous_quotidien_kwh_um` | Four M-O |
| `sensor.prise_petit_dejeune_nous_quotidien_kwh_um` | Petit Déj. |
| `sensor.prise_lave_linge_nous_quotidien_kwh_um` | Lave-Linge |
| `sensor.prise_lave_vaisselle_nous_quotidien_kwh_um` | Lave-Vaisselle |
| `sensor.prise_airfryer_ninja_nous_quotidien_kwh_um` | Airfryer |
| `sensor.four_et_plaque_de_cuisson_quotidien_kwh_um` | Four & Plaque |
| `sensor.prise_frigo_cuisine_nous_quotidien_kwh_um` | Frigo |
| `sensor.prise_congelateur_cuisine_nous_quotidien_kwh_um` | Congélateur |
| `sensor.prise_bureau_pc_ikea_quotidien_kwh_um` | PCe |
| `sensor.prise_bureau_fer_a_repasser_nous_quotidien_kwh_um` | Fer à Repasser |
| `sensor.prise_tete_de_lit_chambre_quotidien_kwh_um` | Tête de lit |
| `sensor.prise_tv_chambre_nous_quotidien_kwh_um` | TV Chambre |
| `sensor.all_standby_quotidien_kwh_um` | Veilles |

---

### 📈 Moyennes Quotidiennes (Wh — AVG)

> Source : `sensors/P2_prise/P2_kWh.yaml` (sensors AVG)

| Entité | Appareil |
|--------|----------|
| `sensor.box_internet_avg_watts_quotidien` | Box Internet |
| `sensor.horloge_avg_watts_quotidien` | Horloge |
| `sensor.pc_gege_avg_watts_quotidien` | PCg |
| `sensor.chargeurs_salon_avg_watts_quotidien` | Chargeurs |
| `sensor.tv_salon_avg_watts_quotidien` | TV Salon |
| `sensor.four_mo_avg_watts_quotidien` | Four M-O |
| `sensor.petit_dej_avg_watts_quotidien` | Petit Déj. |
| `sensor.lave_linge_avg_watts_quotidien` | Lave-Linge |
| `sensor.lave_vaisselle_avg_watts_quotidien` | Lave-Vaisselle |
| `sensor.airfryer_avg_watts_quotidien` | Airfryer |
| `sensor.four_plaque_avg_watts_quotidien` | Four & Plaque |
| `sensor.frigo_avg_watts_quotidien` | Frigo |
| `sensor.congelateur_avg_watts_quotidien` | Congélateur |
| `sensor.pc_bureau_avg_watts_quotidien` | PCe |
| `sensor.fer_repasser_avg_watts_quotidien` | Fer à Repasser |
| `sensor.tete_lit_avg_watts_quotidien` | Tête de lit |
| `sensor.tv_chambre_avg_watts_quotidien` | TV Chambre |
| `sensor.veilles_avg_watts_quotidien` | Veilles |

---

### 🔌 Courant instantané (A — pour streamline-card)

`sensor.prise_*_ikea_current` / `sensor.prise_*_nous_current` — Zigbee2MQTT [Z2M]

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| Intégration Zigbee2MQTT | Native HA (Z2M add-on) | ✅ Essentiel (toutes prises IKEA + NOUS) |
| `bar-card` | HACS Frontend | ✅ Essentiel |
| `auto-entities` | HACS Frontend | ✅ Essentiel |
| `apexcharts-card` | HACS Frontend | ✅ Essentiel |
| `tabbed-card` | HACS Frontend | ✅ Essentiel |
| `streamline-card` | HACS Frontend | ✅ Essentiel (template `conso_temps_reel_appareil`) |
| `bubble-card` | HACS Frontend | ✅ Essentiel (séparateur) |
| UM quotidiens P2 | `utility_meter/P2_prise/P2_UM_AMHQ.yaml` | ✅ Essentiel (donut) |
| Sensors AVG P2 | `sensors/P2_prise/P2_kWh.yaml` | ✅ Essentiel (streamline-card) |

---

## 🐛 DÉPANNAGE

### Le bar-card prises n'affiche rien
1. Vérifier que des `sensor.*power` ont un état > 1W dans Outils de développement > États
2. Les filtres `state: <= 0.999` et `state: unavailable` masquent les appareils inactifs — c'est normal
3. Vérifier l'intégration NOUS/IKEA dans Paramètres > Appareils

### Le donut affiche des tranches vides
1. Au début de journée (minuit), tous les UM sont à 0 → le donut peut être vide ou mono-tranche
2. Normal si aucun appareil n'a consommé sur la période

### La tabbed-card n'affiche pas les onglets
1. Vérifier l'installation : HACS > Frontend > `tabbed-card`
2. Vider le cache navigateur (`Ctrl+Shift+R`)

### Les streamline-cards affichent une erreur
1. Vérifier que le template `conso_temps_reel_appareil` est défini dans la configuration streamline
2. Vérifier que les variables `energy_entity`, `current_entity`, etc. correspondent à des entités existantes

### Les courbes ApexCharts ont des trous
1. `fill_raw: last` devrait éviter les trous — vérifier que l'option est bien présente
2. Si l'entité n'a pas de données récentes (appareil absent), des trous peuvent apparaître malgré `fill_raw`

---

## 🔗 FICHIERS LIÉS

| Rôle | Chemin |
|------|--------|
| Dashboard principal | `dashbord/page_energie_temps_reel.yaml` |
| UM quotidiens P2 | `utility_meter/P2_prise/P2_UM_AMHQ.yaml` |
| Sensors AVG P2 | `sensors/P2_prise/P2_kWh.yaml` |
| Page d'origine | `page_energie_home.yaml` |
| Documentation énergie home | `docs/L2C1_ENERGIE/PAGE_ENERGIE.md` |
| Page mensuelle | `docs/L2C1_ENERGIE/PAGE_ENERGIE_MENSUEL.md` |

---

← Retour : `docs/L2C1_ENERGIE/PAGE_ENERGIE.md` | → Suivant : `PAGE_ENERGIE_MENSUEL.md`
