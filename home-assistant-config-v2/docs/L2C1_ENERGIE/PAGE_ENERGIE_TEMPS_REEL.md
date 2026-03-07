<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--07-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `dashbord/page_energie_temps_reel.yaml` |
| 🔗 **Accès depuis** | Badge "Réel" de `page_energie_home.yaml` → `/dashboard-tablette/energie-temps-reel` |
| 🔗 **Retour vers** | Tap titre → `/dashboard-tablette/energie` |
| 🏗️ **Layout** | `type: grid` — 6 blocs `vertical-stack` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-07 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# ⚡ PAGE ÉNERGIE TEMPS RÉEL — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Bloc 1 — HEADER](#bloc-1--header)
4. [Bloc 2 — Bar-card Prises (puissance instantanée)](#bloc-2--bar-card-prises-puissance-instantanée)
5. [Bloc 3 — Bar-card Lumières (puissance instantanée)](#bloc-3--bar-card-lumières-puissance-instantanée)
6. [Bloc 4 — Donut journalier (cumul depuis minuit)](#bloc-4--donut-journalier-cumul-depuis-minuit)
7. [Bloc 5 — ApexCharts 24h (conso instantanée)](#bloc-5--apexcharts-24h-conso-instantanée)
8. [Bloc 6 — Tabbed-card par pièce (streamline)](#bloc-6--tabbed-card-par-pièce-streamline)
9. [Entités utilisées](#entités-utilisées--provenance-complète)
10. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Cette page offre une vue **temps réel** de la consommation électrique appareil par appareil :
- Toutes les prises connectées actives triées par puissance décroissante (bar-card dynamique)
- Toutes les lumières actives triées par puissance décroissante (bar-card dynamique)
- Donut de répartition par appareil sur la journée (kWh cumulés depuis minuit)
- Courbe instantanée par appareil sur 24h (W)
- Détail par pièce via onglets : puissance instantanée + moyenne + kWh du jour par appareil

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
┌─────────────────────────────────────────────────────┐
│  [HEADER] Temps Réél + Badge conso réelle           │
│  ← tap : retour /energie                            │
├─────────────────────────────────────────────────────┤
│  [BAR-CARD auto-entities] PRISES actives (W)        │
│  Filtres: exclut hue, relais, poco, device, Freebox │
│  Inclut: sensor.*power (>1W, tri décroissant)       │
├─────────────────────────────────────────────────────┤
│  [BAR-CARD auto-entities] LUMIÈRES actives (W)      │
│  Inclut: sensor.*relais*power, hue*power            │
│  Exclut: last_updated > 1m, state ≤ 1              │
├─────────────────────────────────────────────────────┤
│  [DONUT ApexCharts] Cumul depuis Minuit (Wh)        │
│  18 prises × transform: x * 1000 (kWh → Wh)       │
│  + sensor.all_standby_quotidien_kwh_um              │
├─────────────────────────────────────────────────────┤
│  [ApexCharts 24h] Conso. Instantanée (W)            │
│  18 prises × sensor.*_power + sensor.all_standby   │
│  group_by: last, duration: 10m — fill_raw: last    │
├─────────────────────────────────────────────────────┤
│  [bubble-card separator] Sélectionner une pièce :   │
│  [TABBED-CARD]                                      │
│  ┌────────┬────────┬────────┬────────┬────────┬─────┐│
│  │ Entrée │ Salon  │Cuisine │ Bureau │Chambre │Veill││
│  └────────┴────────┴────────┴────────┴────────┴─────┘│
│  [streamline-card × N] par pièce                   │
│  template: conso_temps_reel_appareil               │
│  → W instantané + Ampères + Moy. W/j + kWh du jour │
└─────────────────────────────────────────────────────┘
```

---

## 📍 BLOC 1 — HEADER

```yaml
- type: vertical-stack
  cards:
    - type: heading
      icon: mdi:lightning-bolt
      heading: Temps Réél
      heading_style: title
      badges:
        - type: entity
          entity: sensor.ecojoko_consommation_temps_reel
          name: Réel
          color: green
      tap_action:
        action: navigate
        navigation_path: /dashboard-tablette/energie
```

> ⚠️ Typo dans le titre original : "Temps Réél" (double accent) — à corriger lors du re-build.

### Entités
- `sensor.ecojoko_consommation_temps_reel` [Ecojoko - UI] Puissance instantanée totale (W)

---

## 📊 BLOC 2 — Bar-card Prises (puissance instantanée)

```yaml
- type: custom:auto-entities
  card:
    type: custom:bar-card
    icon: mdi:lightning-bolt
    height: 38
    unit_of_measurement: W
    severity:
      - color: gainsboro      from: 0    to: 5
      - color: rgb(102,255,102) from: 5  to: 49
      - color: rgb(0,102,0)   from: 50   to: 249
      - color: orange         from: 250  to: 499
      - color: darkorange     from: 500  to: 749
      - color: red            from: 750  to: 999
      - color: darkred        from: 1000 to: 6000
  filter:
    exclude:
      - entity_id: ^sensor.oneplus*power$
      - entity_id: ^sensor.eclairage*$
      - entity_id: ^sensor.lampe*ikea*power$
      - entity_id: ^*hue*$
      - entity_id: ^*poco*$
      - entity_id: ^*device*$
      - entity_id: ^*relais*$
      - entity_id: sensor.entree_freebox_pop_power
      - entity_id: sensor.freebox_v8_r1_power
      - entity_id: sensor.nvidia_*_gpu_package_power
      - state: unavailable
      - state: unknown
      - state: <= 0.999
    include:
      - entity_id: ^sensor.*power$
  sort:
    method: state
    numeric: true
    reverse: true
```

### Palette couleur (seuils W)

| Seuil | Couleur | Signification |
|-------|---------|---------------|
| 0–5 W | Gris clair | Veille/standby |
| 5–49 W | Vert clair | Faible |
| 50–249 W | Vert foncé | Normal |
| 250–499 W | Orange | Élevé |
| 500–749 W | Orange foncé | Fort |
| 750–999 W | Rouge | Très fort |
| ≥ 1 000 W | Rouge foncé | Gros appareil actif |

### Filtres clés
- **Inclus** : tous `sensor.*power` (regex)
- **Exclus** : hue, relais, poco (téléphone), device_tracker, Freebox, GPU Nvidia, état ≤ 1W / unavailable / unknown
- **Tri** : état numérique décroissant → l'appareil le plus gourmand en haut
- **Dynamique** : seuls les appareils actifs apparaissent

---

## 💡 BLOC 3 — Bar-card Lumières (puissance instantanée)

Même structure que le Bloc 2 mais ciblant uniquement les lumières.

```yaml
  filter:
    exclude:
      - last_updated: 1m ago   # exclut les entités non mises à jour depuis 1 min
      - state: <= 1
      - state: unavailable
    include:
      - entity_id: ^*relais*power$         # Sonoff relais (lumière SDB via relais)
      - entity_id: sensor.lampe_salle_de_bain_hue_power
      - entity_id: ^sensor.hue*power$      # Toutes les ampoules Hue
```

### Palette couleur (seuils W — lumières)

| Seuil | Couleur |
|-------|---------|
| 0–0.99 W | Gris (éteint/veille) |
| 1–4.99 W | Vert clair |
| 5–9.99 W | Vert foncé |
| 10–14.99 W | Orange |
| ≥ 15 W | Rouge |

> Les lumières consomment 1–15 W → échelle adaptée (vs 6 000 W max pour les prises).

---

## 🥧 BLOC 4 — Donut journalier (cumul depuis minuit)

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
| Horloge Entrée | `prise_horloge_ikea_quotidien_kwh_um` | rgb(183,183,183) |
| PCg (Géraldine) | `prise_pc_s_gege_ikea_quotidien_kwh_um` | rgb(202,135,135) |
| Chargeurs Salon | `prise_salon_chargeur_nous_quotidien_kwh_um` | rgb(174,68,90) |
| TV Salon | `prise_tv_salon_ikea_quotidien_kwh_um` | rgb(215,95,115) |
| Four Micro-Ondes | `prise_four_micro_ondes_nous_quotidien_kwh_um` | rgb(98,78,136) |
| Petit Déjeuner | `prise_petit_dejeune_nous_quotidien_kwh_um` | rgb(118,93,160) |
| Lave-Linge | `prise_lave_linge_nous_quotidien_kwh_um` | rgb(137,103,179) |
| Lave-Vaisselle | `prise_lave_vaisselle_nous_quotidien_kwh_um` | rgb(129,116,180) |
| Airfryer | `prise_airfryer_ninja_nous_quotidien_kwh_um` | rgb(142,122,181) |
| Four & Plaque | `four_et_plaque_de_cuisson_quotidien_kwh_um` | rgb(162,148,249) |
| Frigo | `prise_frigo_cuisine_nous_quotidien_kwh_um` | cyan |
| Congélateur | `prise_congelateur_cuisine_nous_quotidien_kwh_um` | rgb(19,160,255) |
| PCe (Bureau) | `prise_bureau_pc_ikea_quotidien_kwh_um` | orange |
| Fer à Repasser | `prise_bureau_fer_a_repasser_nous_quotidien_kwh_um` | gold |
| Têtes de lit | `prise_tete_de_lit_chambre_quotidien_kwh_um` | rgb(177,194,158) |
| TV Chambre | `prise_tv_chambre_nous_quotidien_kwh_um` | rgb(30,81,40) |
| Veilles | `all_standby_quotidien_kwh_um` | grey |

> Sources UM : `utility_meter/P2_prise/P2_UM_AMHQ.yaml` (quotidien cycle)

---

## 📈 BLOC 5 — ApexCharts 24h (conso instantanée)

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

## 📱 BLOC 6 — Tabbed-card par pièce (streamline)

```yaml
- type: vertical-stack
  cards:
    - type: custom:bubble-card
      card_type: separator
      name: 'Sélectionner une pièce :'
      icon: mdi:arrow-right-bottom-bold

    - type: custom:tabbed-card
      styles:
        '--mdc-theme-primary': white
        '--mdc-tab-text-label-color-default': rgba(255,255,255,0.25)
      tabs:
        - attributes:
            label: Entrée
            icon: mdi:door
          card:
            type: vertical-stack
            cards:
              - type: custom:streamline-card
                template: conso_temps_reel_appareil
                variables: ...
```

### 6 onglets

| Onglet | Icône | Appareils |
|--------|-------|-----------|
| Entrée | `mdi:door` | Box Internet, Horloge |
| Salon | `mdi:sofa` | PCg Géraldine, Chargeurs Salon, TV Salon |
| Cuisine | `mdi:fridge` | Four M-O, Petit Déj., Lave-Linge, Lave-Vaisselle, Airfryer, Four & Plaque, Frigo, Congélateur |
| Bureau | `mdi:desk` | PCe Bureau, Fer à Repasser |
| Chambre | `mdi:bed` | Tête de lit, TV Chambre |
| Veilles | `mdi:sleep` | All Standby |

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
