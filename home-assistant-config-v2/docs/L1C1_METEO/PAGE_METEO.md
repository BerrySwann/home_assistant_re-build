<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--02--26-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/meteo` |
| 🔗 **Accès depuis** | Vignette L1C1 → Dashboard HOME |
| 🏗️ **Layout** | Grid (colonnes variables) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-02-26 |
| 🏠 **Version HA** | 2025.1.x → 2.0 |

---

# 🌤️ PAGE MÉTÉO — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section HEADER](#section-header)
4. [Section APPARTEMENT](#section-appartement)
5. [Section PRÉVISIONS](#section-prévisions)
6. [Section VENT](#section-vent)
7. [Section BAROMÈTRE](#section-baromètre)
8. [Section UV & PLUIE](#section-uv--pluie)
9. [POP-UP #FOUDRE](#pop-up-foudre)
10. [POP-UP #ALERT](#pop-up-alert)
11. [POP-UP #SUN](#pop-up-sun)
12. [Entités utilisées](#entités-utilisées-récapitulatif)
13. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Cette page regroupe toutes les informations météorologiques pour Vence (06140) :
- Température et humidité du balcon Nord (référence extérieure)
- Prévisions Météo France (horaires + quotidiennes)
- Cartes interactives Windy (radar, pluie, température, vent)
- Analyse du vent avec rose des vents (windrose-card)
- Baromètre graphique avec prédictions
- Indices UV et pluviométrie
- 3 pop-ups détaillés : Foudre, Alertes, Lever/Coucher du soleil

### Intégrations requises
- ✅ Météo France (intégration native HA)
- ✅ Blitzortung (via HACS - impacts de foudre)
- ✅ Sun (intégration native HA)
- ✅ Season (sensor template pour les saisons)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `bubble-card` | Séparateurs, pop-ups, navigation |
| `windrose-card` | Rose des vents |
| `ha-tbaro-card` | Baromètre graphique |
| `uv-index-card` | Indicateur UV |
| `rain-gauge-card` | Jauge de pluie |
| `apexcharts-card` | Graphique pluie 24h |
| `horizon-card` | Position soleil/lune |
| `tsmoon-card` | Phase lunaire |
| `meteoalarm-card` | Alertes Météo France |
| `swipe-card` | Carrousel Windy |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌─────────────────────────────────────────────┐
│  [HEADER] METEO + Badge Température         │
├─────────────────────────────────────────────┤
│  [SEPARATOR] Appartement                    │
│  Temp: XX°C | Humidité: XX%                 │
├─────────────────────────────────────────────┤
│  [SEPARATOR] Prévision Météo France         │
│  ┌─────────────────────────────────────┐    │
│  │  Weather Forecast (hourly)          │    │
│  ├─────────────────────────────────────┤    │
│  │  Swipe-Card: 4 iframes Windy        │    │
│  │  [Radar|Pluie|Temp|Vent]            │    │
│  ├─────────────────────────────────────┤    │
│  │  Weather Forecast (daily)           │    │
│  └─────────────────────────────────────┘    │
├─────────────────────────────────────────────┤
│  [HEADING] Vent - Baromètre - UV - Pluie   │
├─────────────────────────────────────────────┤
│  [SEPARATOR] Vent                           │
│  ┌─────────────────────────────────────┐    │
│  │  Windrose Card (Direction + Vitesse)│    │
│  └─────────────────────────────────────┘    │
├─────────────────────────────────────────────┤
│  [SEPARATOR] Baromètre                      │
│  ┌─────────────────────────────────────┐    │
│  │  HA-Tbaro-Card (Pression hPa)       │    │
│  └─────────────────────────────────────┘    │
├─────────────────────────────────────────────┤
│  [SEPARATOR] UV        [SEPARATOR] Pluie    │
│  ┌──────────┐         ┌──────────┐         │
│  │ UV Index │         │Rain Gauge│         │
│  └──────────┘         └──────────┘         │
├─────────────────────────────────────────────┤
│  [SEPARATOR] Pluie 24h (Météo France)      │
│  ┌─────────────────────────────────────┐    │
│  │  ApexCharts (Area graph)            │    │
│  └─────────────────────────────────────┘    │
├─────────────────────────────────────────────┤
│  [NAVIGATION BUBBLE]                        │
│  [#alert] [#foudre] [#sun]                 │
└─────────────────────────────────────────────┘

  ↓ CLICK #foudre
┌─────────────────────────────────────────────┐
│  POP-UP: Impacts de foudre (30 Km)         │
│  - Compteur d'impacts                       │
│  - Bar-cards (Heure/Jour/Semaine/Mois/An)  │
│  - Windrose direction dernier impact        │
│  - Graphiques ApexCharts                   │
│  - Cartes Windy + Blitzortung              │
└─────────────────────────────────────────────┘

  ↓ CLICK #alert
┌─────────────────────────────────────────────┐
│  POP-UP: Alertes Météo France              │
│  - Cartes alertes (Aujourd'hui/Demain)     │
│  - Mushroom cards par type d'alerte        │
│  - Meteoalarm-card intégration             │
└─────────────────────────────────────────────┘

  ↓ CLICK #sun
┌─────────────────────────────────────────────┐
│  POP-UP: Lever et coucher du Soleil        │
│  - Horizon card (trajectoire solaire)      │
│  - TSMoon card (phase lunaire)             │
│  - Progress bar lever/coucher              │
│  - État Soleil/Saison                      │
└─────────────────────────────────────────────┘
```

---

## 📍 SECTION HEADER

### Code

```yaml
- type: heading
  icon: mdi:clouds
  heading: METEO
  heading_style: title
  badges:
    - type: entity
      show_state: true
      show_icon: true
      entity: sensor.th_balcon_nord_temperature
      color: green
  tap_action:
    action: navigate
    navigation_path: /dashboard-tablette/home
  layout_options:
    grid_columns: full
    grid_rows: 1
```

### Rôle
- Titre principal : "METEO" avec icône nuage
- Badge température : Affiche la température extérieure en temps réel
- Navigation retour : Clic → retour au dashboard HOME

### Entités
- `sensor.th_balcon_nord_temperature` [Zigbee - UI] (Thermostat Sonoff Balcon Nord)

---

## 🏠 SECTION APPARTEMENT

### Code (simplifié)

```yaml
- type: custom:bubble-card
  card_type: separator
  name: Appartement
  icon: mdi:home-assistant

- type: horizontal-stack
  cards:
    - type: markdown
      content: >
        <center>Température: <ha-icon icon="mdi:home-thermometer"></ha-icon>
        {{ states("sensor.th_balcon_nord_temperature")}}°C</center>
    - type: markdown
      content: >
        <center>Humidité: <ha-icon icon="mdi:water-percent"></ha-icon>
        {{ states("sensor.th_balcon_nord_humidity") | round(0) }}%</center>
```

### Rôle
Affiche les conditions extérieures mesurées sur le balcon Nord (référence pour toutes les automations thermiques).

### Entités
- `sensor.th_balcon_nord_temperature` [Zigbee - UI]
- `sensor.th_balcon_nord_humidity` [Zigbee - UI]

### Card-mod appliqué

```css
ha-card {
  font-size: 17px;
  background: none !important;
  box-shadow: none !important;
  border: none !important;
}
```

---

## 🌦️ SECTION PRÉVISIONS

### Structure

```yaml
- type: vertical-stack
  cards:
    - type: weather-forecast        # Prévisions HORAIRES
      show_current: true
      show_forecast: true
      entity: weather.vence
      forecast_type: hourly

    - type: custom:swipe-card       # Carrousel 4 cartes Windy
      cards:
        - type: iframe              # Radar
          url: https://embed.windy.com/...overlay=radar...
        - type: iframe              # Pluie
          url: https://embed.windy.com/...overlay=rain...
        - type: iframe              # Température
          url: https://embed.windy.com/...overlay=temp...
        - type: iframe              # Vent
          url: https://embed.windy.com/...overlay=wind...

    - type: weather-forecast        # Prévisions QUOTIDIENNES
      show_current: false
      show_forecast: true
      entity: weather.vence
      forecast_type: daily
```

### Rôle
- **Weather Forecast** : Prévisions natives Météo France
- **Swipe-Card** : 4 cartes Windy interactives (Radar/Pluie/Temp/Vent)
  - Navigation par swipe (balayage tactile)
  - Barre de progression en bas
  - `pointer-events: none` → Désactive les interactions iframe (problème de touch sur mobile)

### Entités
- `weather.vence` [Météo France - UI] (Intégration Météo France)

### Paramètres Windy

| Paramètre | Valeur | Rôle |
|-----------|--------|------|
| `lat` | 43.612 | Latitude Vence |
| `lon` | 7.207 | Longitude Vence |
| `zoom` | 5 | Niveau de zoom initial |
| `overlay` | radar/rain/temp/wind | Couche météo affichée |
| `product` | ecmwf/radar | Modèle de prévision |

> **IMPORTANT :** Le `filter: invert(0%)` dans les iframes est là pour désactiver l'inversion des couleurs en mode sombre (si appliquée par le thème).

---

## 🌬️ SECTION VENT

### Code (structure simplifiée)

```yaml
- type: custom:windrose-card
  title: Direction et Vitesse du Vent avec Rafales
  max_width: 300
  windspeed_bar_location: bottom
  windspeed_bar_full: true

  wind_direction_entity:
    entity: sensor.direction_du_vent_vence
    use_statistics: false
    direction_compensation: 0

  windspeed_entities:
    - entity: weather.vence
      attribute: wind_speed
      name: Moyenne
      speed_range_step: 5
      speed_range_max: 35

    - entity: sensor.vence_wind_gust
      name: Rafale
      speed_ranges:
        - from_value: 110
          color: rgb(101, 19, 19)   # Violet foncé
        - from_value: 100
          color: rgb(216, 88, 41)   # Rouge-orangé
        # ... (gradient de couleurs)
        - from_value: 0
          color: rgb(51, 51, 255)   # Bleu

  corner_info:
    top_left:
      label: Vitesse du Vent
      unit: " km/h"
      entity: sensor.vitesse_du_vent_vence
    top_right:
      label: Direction du Vent
      entity: sensor.direction_du_vent_vence_label
    bottom_left:
      label: Boussole
      unit: °
      entity: sensor.direction_du_vent_vence
    bottom_right:
      label: Vitesse de la rafale actuelle
      unit: " km/h"
      entity: sensor.vence_wind_gust

  data_period:
    period_selector:
      buttons:
        - hours: 24
          title: 1 day
          active: true
        - hours: 168
          title: 7 days
        - hours: 360
          title: 15 days
        - hours: 730
          title: 30 days
```

### Rôle
Rose des vents complète affichant :
- Direction du vent (sensor custom template)
- Vitesse moyenne (depuis `weather.vence` [Météo France - UI])
- Rafales (sensor Météo France)
- 4 coins d'infos : Vitesse, Direction, Boussole, Rafale actuelle
- Sélecteur de période : 1 jour / 7 jours / 15 jours / 30 jours

### Entités
- `sensor.direction_du_vent_vence` [templates/meteo/M_02] (Template sensor - voir `M_02_meteo_vent_vence_card.yaml`)
- `sensor.direction_du_vent_vence_label` [templates/meteo/M_02] (Template sensor - Nord/Sud/Est/Ouest)
- `sensor.vitesse_du_vent_vence` [templates/meteo/M_02] (Template sensor)
- `sensor.vence_wind_gust` [Météo France - UI] (Météo France)
- `weather.vence` [Météo France - UI] (attribute: wind_speed)

### Palette de couleurs rafales

```
110+ km/h → Rouge très foncé (danger extrême)
100-110   → Rouge-orangé
90-100    → Orange vif
80-90     → Jaune-vert
70-80     → Vert clair
60-70     → Vert-cyan
50-60     → Cyan
40-50     → Bleu clair
0-40      → Bleu foncé (calme)
```

---

## 🌡️ SECTION BAROMÈTRE

### Code (simplifié)

```yaml
- type: custom:ha-tbaro-card
  entity: sensor.vence_pressure
  show_weather_icon: true
  show_weather_text: true
  show_pressure: true
  stroke_width: 10
  show_icon: true
  needle_color: gainsboro
  tick_color: gainsboro
  show_border: false
  unit: hpa
  angle: 270
  size: 400

  segments:
    - from: 950
      to: 980
      color: "#FF4500"   # Rouge (tempête)
    - from: 980
      to: 1000
      color: "#FFD700"   # Or (pluie)
    - from: 1000
      to: 1020
      color: "#3399ff"   # Bleu (variable)
    - from: 1020
      to: 1050
      color: "#4CAF50"   # Vert (beau temps)

  language: fr
  icon_offset_y: 10
  icon_offset_x: 7
  icon_size: 30
```

### Rôle
Affiche un baromètre graphique avec prédiction météo (texte + icône) basé sur la pression atmosphérique.

### Entités
- `sensor.vence_pressure` [Météo France - UI] (Météo France)

### Interprétation

| Pression (hPa) | Couleur | Prévision |
|---------------|---------|-----------|
| < 980 | 🔴 Rouge | Tempête possible |
| 980-1000 | 🟡 Or | Pluie probable |
| 1000-1020 | 🔵 Bleu | Variable |
| > 1020 | 🟢 Vert | Beau temps |

### Paramètres clés
- `angle: 270` → Baromètre en arc de cercle (270° = 3/4 de cercle)
- `size: 400` → Taille en pixels
- `language: fr` → Texte de prédiction en français

---

## ☀️ SECTION UV & PLUIE

### Code (simplifié)

```yaml
- type: horizontal-stack
  cards:
    - type: custom:bubble-card
      card_type: separator
      name: UV
      icon: mdi:sunglasses

    - type: custom:bubble-card
      card_type: separator
      name: Pluie
      icon: mdi:weather-pouring

- type: horizontal-stack
  cards:
    - type: custom:uv-index-card
      entity: sensor.vence_uv
      name: ""
      icon: mdi:weather-sunny

    - type: custom:rain-gauge-card
      entity: sensor.vence_daily_precipitation
      fill_drop_colour: "#44739E"
      max_level: 60
      border_colour: grey
      name: ""
      icon: mdi:weather-rainy
```

### Entités
- `sensor.vence_uv` [Météo France - UI] (Météo France)
- `sensor.vence_daily_precipitation` [Météo France - UI] (Météo France)

### UV Index Card
Couleurs automatiques selon l'indice UV :
- 0-2 : Vert (faible)
- 3-5 : Jaune (modéré)
- 6-7 : Orange (élevé)
- 8-10 : Rouge (très élevé)
- 11+ : Violet (extrême)

### Rain Gauge Card
- `max_level: 60` → Échelle max 60mm
- `fill_drop_colour: "#44739E"` → Bleu HA standard

### Graphique pluie 24h

```yaml
- type: custom:apexcharts-card
  graph_span: 24h
  header:
    show: false
  series:
    - entity: sensor.vence_daily_precipitation
      stroke_width: 2
      type: area
      color: "#44739E"
      opacity: 0.5
      group_by:
        func: avg
        duration: 1m
```

Courbe de pluie cumulée sur 24h (mise à jour toutes les minutes).

---

## ⚡ POP-UP #FOUDRE

### Activation

```yaml
- type: custom:bubble-card
  card_type: horizontal-buttons-stack
  1_link: "#alert"
  1_icon: mdi:alert-outline
  2_link: "#foudre"
  2_icon: mdi:weather-lightning
  3_link: "#sun"
  3_icon: mdi:sun-clock-outline
```

### Structure du pop-up

```
┌─────────────────────────────────────────┐
│  📌 HEADER                              │
│  Impacts de foudre (30 Km)             │
├─────────────────────────────────────────┤
│  🎯 BUTTON-CARD : Dernier impact        │
│  "Impact à X.X Km à [Ville] au [Dir]"  │
│  "Il y a XX minutes"                    │
│  "⚡ X impact(s) détecté(s)"            │
│  (Fond rouge si < 5km)                  │
├─────────────────────────────────────────┤
│  📊 BAR-CARDS : Compteurs               │
│  [Heure] [Jour] [Semaine] [Mois] [Année]│
│  (Gradient vert→rouge selon intensité)  │
├─────────────────────────────────────────┤
│  🧭 WINDROSE : Direction dernier impact │
│  (Distance + Bearing)                   │
├─────────────────────────────────────────┤
│  📈 APEXCHARTS : Graphiques historiques │
│  - Nb éclairs heure par heure (24h)    │
│  - Nb éclairs par jour (30j)           │
├─────────────────────────────────────────┤
│  🗺️ CARTES : Radar + Blitzortung        │
│  Swipe-card (2 iframes)                │
└─────────────────────────────────────────┘
```

### Entités principales

| Entité | Source | Rôle |
|--------|--------|------|
| `sensor.maison_lightning_counter` [HACS Blitzortung - UI] | Blitzortung | Compteur d'impacts |
| `sensor.maison_lightning_distance` [HACS Blitzortung - UI] | Blitzortung | Distance dernier impact (km) |
| `sensor.maison_lightning_azimuth` [HACS Blitzortung - UI] | Blitzortung | Direction dernier impact (°) |
| `sensor.dernier_impact_temps_reel` [templates/meteo/M_03] | Template | "Il y a XX minutes" |
| `sensor.maison_lightning_localisation` [sensors/meteo/M_03_...blitzortung.yaml] | REST API | Ville/lieu proche |
| `sensor.eclairs_horaire` [utility_meter/meteo/M_03] | Utility meter | Compteur heure |
| `sensor.eclairs_quotidien` [utility_meter/meteo/M_03] | Utility meter | Compteur jour |
| `sensor.eclairs_hebdomadaire` [utility_meter/meteo/M_03] | Utility meter | Compteur semaine |
| `sensor.eclairs_mensuel` [utility_meter/meteo/M_03] | Utility meter | Compteur mois |
| `sensor.eclairs_annuel` [utility_meter/meteo/M_03] | Utility meter | Compteur année |
| `sensor.lightning_bearing` [templates/meteo/M_03] | Template | Bearing pour windrose |
| `sensor.lightning_distance_km` [templates/meteo/M_03] | Template | Distance pour windrose |
| `sensor.lightning_direction_label` [templates/meteo/M_03] | Template | "Nord", "Sud-Est"... |

### Button-card dernier impact (logique JS)

```javascript
const distRaw = parseFloat(states['sensor.maison_lightning_distance'].state);
const localisation = states['sensor.maison_lightning_localisation'];
const azimuth = parseFloat(states['sensor.maison_lightning_azimuth'].state);
const impactCount = parseInt(entity.state) || 0;
const timePhrase = states['sensor.dernier_impact_temps_reel'].state;

let message = '';

if (distRaw > 0) {
  const distance = distRaw.toFixed(1);
  message = `Impact à <strong>${distance} Km</strong>`;

  if (localisation?.attributes?.features?.[0]?.properties?.geocoding?.city) {
    const city = localisation.attributes.features[0].properties.geocoding.city;
    message += ` à ${city}`;
  } else if (azimuth !== null) {
    const directions = [
      "au nord", "au nord-nord-est", "au nord-est", "à l'est-nord-est",
      "à l'est", "à l'est-sud-est", "au sud-est", "au sud-sud-est",
      "au sud", "au sud-sud-ouest", "au sud-ouest", "à l'ouest-sud-ouest",
      "à l'ouest", "à l'ouest-nord-ouest", "au nord-ouest", "au nord-nord-ouest"
    ];
    const index = Math.round(azimuth / 22.5) % 16;
    message += ` ${directions[index]}`;
  }
} else {
  message = "Aucun impact récent détecté";
}

const impactLine = impactCount > 0
  ? `<br><span style="color: #ffeb3b; font-weight: bold; font-size: 17px;">⚡ ${impactCount} impact(s) détecté(s)</span>`
  : '';

return `<div style="line-height: 1.6;">
  <span style="font-size: 14px;">${message}</span><br>
  <span style="font-size: 13px; opacity: 0.9; font-weight: 500;">${timePhrase}</span>
  ${impactLine}
</div>`;
```

### Logique du fond coloré

```javascript
background: |
  [[[
    const d = parseFloat(states['sensor.maison_lightning_distance']?.state);
    if (d > 0 && d <= 5) return 'rgba(255, 0, 0, 0.2)';   // Rouge danger
    if (d > 5) return 'rgba(255, 123, 0, 0.1)';            // Orange attention
    return 'rgba(0, 255, 0, 0.05)';                         // Vert ok
  ]]]
```

### Bar-cards compteurs

| Période | Entité | Échelle max | Seuil vert | Seuil rouge |
|---------|--------|-------------|------------|-------------|
| Heure | `sensor.eclairs_horaire` [utility_meter/meteo/M_03] | 3 000 | 0-428 | 1715+ |
| Jour | `sensor.eclairs_quotidien` [utility_meter/meteo/M_03] | 30 000 | 0-4285 | 17143+ |
| Semaine | `sensor.eclairs_hebdomadaire` [utility_meter/meteo/M_03] | 50 000 | 0-7142 | 28572+ |
| Mois | `sensor.eclairs_mensuel` [utility_meter/meteo/M_03] | 70 000 | 0-10000 | 40001+ |
| Année | `sensor.eclairs_annuel` [utility_meter/meteo/M_03] | 150 000 | 0-22000 | 88001+ |

Gradient de couleurs (7 paliers) : `Green → Gold → Orange → Dark Orange → Red → Dark Red → Purple`

---

## 🚨 POP-UP #ALERT

### Structure

```
┌─────────────────────────────────────────┐
│  📌 HEADER                              │
│  Carte d'alerte(s) Météo France        │
├─────────────────────────────────────────┤
│  🗺️ CARTES ALERTES                      │
│  [Aujourd'hui]  [Demain]                │
│  (Images camera entity)                 │
├─────────────────────────────────────────┤
│  🟢🟡🟠🔴 MUSHROOM CARDS               │
│  [Météo] [Orages] [Pluie] [Vent] [Aval]│
│  [Canicule] [Inond] [Neige] [Froid] [Vag]│
│  (Couleur = niveau vigilance)           │
├─────────────────────────────────────────┤
│  📋 METEOALARM-CARD                     │
│  Détails textuels des alertes          │
└─────────────────────────────────────────┘
```

### Entités Camera
- `camera.mf_alerte_today` [command_line/meteo/carte_meteo_france.yaml] (Carte des alertes aujourd'hui)
- `camera.mf_alerte_tomorrow` [command_line/meteo/carte_meteo_france.yaml] (Carte des alertes demain)

### Sensors alertes

| Entité | Type d'alerte |
|--------|---------------|
| `sensor.alerte_meteo` [templates/meteo/M_01] | Vigilance générale |
| `sensor.alerte_orages` [templates/meteo/M_01] | Orages |
| `sensor.alerte_pluie_inondation` [templates/meteo/M_01] | Pluie-Inondation |
| `sensor.alerte_vent_violent` [templates/meteo/M_01] | Vent violent |
| `sensor.alerte_avalanches` [templates/meteo/M_01] | Avalanches |
| `sensor.alerte_canicule` [templates/meteo/M_01] | Canicule |
| `sensor.alerte_inondation` [templates/meteo/M_01] | Crues |
| `sensor.alerte_neige_verglas` [templates/meteo/M_01] | Neige/Verglas |
| `sensor.alerte_grand_froid` [templates/meteo/M_01] | Grand froid |
| `sensor.alerte_vagues_submersion` [templates/meteo/M_01] | Vagues-Submersion |

### États possibles
- `Vert` → Pas de vigilance particulière
- `Jaune` → Soyez attentifs
- `Orange` → Soyez très vigilants
- `Rouge` → Vigilance absolue

### Meteoalarm Card

```yaml
- type: custom:meteoalarm-card
  entities:
    - entity: sensor.06_weather_alert
  integration: meteofrance
  hide_when_no_warning: true
```

---

## 🌅 POP-UP #SUN

### Structure

```
┌─────────────────────────────────────────┐
│  📌 HEADER                              │
│  Lever et coucher du Soleil             │
├─────────────────────────────────────────┤
│  🌄 HORIZON CARD                        │
│  Trajectoire du soleil & de la lune    │
│  (Graphique hémisphérique)              │
├─────────────────────────────────────────┤
│  🌙 TSMOON CARD                         │
│  Phase lunaire graphique                │
├─────────────────────────────────────────┤
│  ⏱️ PROGRESS BAR                        │
│  "Levé du soleil à HH:MM"               │
│  [████████░░░░░░] XX%                  │
│  "dans HH:MM:SS"                        │
├─────────────────────────────────────────┤
│  ☀️ GLANCE CARD                         │
│  [Soleil: above/below] [Saison: Hiver] │
└─────────────────────────────────────────┘
```

### Horizon Card

```yaml
- type: custom:horizon-card
  title: " "
  moon: true
  refresh_period: 60
  fields:
    sunrise: true
    sunset: true
    dawn: true        # Aube
    noon: true        # Midi solaire
    dusk: true        # Crépuscule
    azimuth: true
    sun_azimuth: true
    moon_azimuth: true
    elevation: true
    sun_elevation: true
    moon_elevation: true
  southern_flip: false
  language: fr
  time_format: fr
  number_format: fr
  latitude: 43.716667
  longitude: 7.116667
  elevation: 330
  time_zone: Europe/paris
```

> **IMPORTANT :** `elevation: 330` correspond à l'altitude de Vence en mètres (pas l'angle du soleil).

### TSMoon Card

```yaml
- type: custom:tsmoon-card
  title: ""
  entity: sensor.moon_phase
  icon_type: round
  time_format: 24h
  language: fr
  hemisphere: "N"   # Hémisphère Nord
```

Phases : 🌑 🌒 🌓 🌔 🌕 🌖 🌗 🌘

### Progress Bar (logique Jinja2)

```jinja2
name: >
  {% set sunrise = as_datetime(states('sensor.sun_next_rising')) %}
  {% set sunset = as_datetime(states('sensor.sun_next_setting')) %}
  {% if sunrise and sunset %}
    {% if sunrise < sunset %}
      Levé du soleil à {{ sunrise.timestamp() | timestamp_custom('%H:%M', true) }}
    {% else %}
      Couché du soleil à {{ sunset.timestamp() | timestamp_custom('%H:%M', true) }}
    {% endif %}
  {% else %}
    Sun information not available
  {% endif %}

percent: >
  {% set sunrise = as_datetime(states('sensor.sun_next_rising')) %}
  {% set sunset = as_datetime(states('sensor.sun_next_setting')) %}
  {% set now_time = now() %}
  {% if sunrise and sunset %}
    {% if sunrise < sunset %}
      {% set next_event = sunrise %}
      {% set last_event = sunrise - timedelta(days=1) %}
    {% else %}
      {% set next_event = sunset %}
      {% set last_event = sunset - timedelta(days=1) %}
    {% endif %}
    {% set total = (next_event - last_event).total_seconds() %}
    {% set elapsed = (now_time - last_event).total_seconds() %}
    {% if total > 0 %}
      {{ ((elapsed / total) * 100) | round(2) }}
    {% else %}
      0
    {% endif %}
  {% else %}
    0
  {% endif %}
```

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

> Chaque entité est listée avec son **fichier source exact** dans le repo ReBuild.

---

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | unique_id | Intégration | Configuré via |
|--------|-----------|-------------|---------------|
| `weather.vence` [Météo France - UI] | — | Météo France | Paramètres > Intégrations > Météo France |
| `sensor.vence_pressure` [Météo France - UI] | — | Météo France | idem |
| `sensor.vence_uv` [Météo France - UI] | — | Météo France | idem |
| `sensor.vence_wind_gust` [Météo France - UI] | — | Météo France | idem |
| `sensor.vence_daily_precipitation` [Météo France - UI] | — | Météo France | idem |
| `sensor.06_weather_alert` [Météo France - UI] | — | Météo France | idem (département 06) |
| `sun.sun` [Sun - natif] | — | Sun | Native automatique |
| `sensor.sun_next_rising` [Sun - natif] | — | Sun | Native automatique |
| `sensor.sun_next_setting` [Sun - natif] | — | Sun | Native automatique |
| `sensor.moon_phase` [Moon - natif] | — | Moon | Native automatique |
| `sensor.season` [Season - natif] | — | Season | Native automatique |
| `sensor.th_balcon_nord_temperature` [Zigbee - UI] | — | Sonoff SNZB-02 | Zigbee (intégration UI) |
| `sensor.th_balcon_nord_humidity` [Zigbee - UI] | — | Sonoff SNZB-02 | Zigbee (intégration UI) |

---

### 📁 `sensors/meteo/M_03_meteo_sensors_blitzortung.yaml`
> Sensor REST — Localisation géographique du dernier éclair (API Nominatim / OpenStreetMap)

| Entité | unique_id | Type | MAJ |
|--------|-----------|------|-----|
| `sensor.maison_lightning_localisation` [sensors/meteo/M_03_...blitzortung.yaml] | `blitzortung_lightning_localisation` | REST API | toutes les 3600s |

> **Source des données brutes Blitzortung** (`sensor.maison_lightning_counter` [HACS Blitzortung - UI], `sensor.maison_lightning_distance` [HACS Blitzortung - UI], `sensor.maison_lightning_azimuth` [HACS Blitzortung - UI]) → créées automatiquement par l'**intégration HACS Blitzortung** (UI).

---

### 📁 `templates/meteo/M_01_meteo_alertes_card.yaml`
> 10 sensors template — Alertes Météo France département 06

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.alerte_vent_violent` [templates/meteo/M_01] | `sensor.alerte_vent_violent` [templates/meteo/M_01] | Vigilance vent |
| `sensor.alerte_inondation` [templates/meteo/M_01] | `sensor.alerte_inondation` [templates/meteo/M_01] | Vigilance crues |
| `sensor.alerte_orages` [templates/meteo/M_01] | `sensor.alerte_orages` [templates/meteo/M_01] | Vigilance orages |
| `sensor.alerte_pluie_inondation` [templates/meteo/M_01] | `sensor.alerte_pluie_inondation` [templates/meteo/M_01] | Vigilance pluie-inondation |
| `sensor.alerte_neige_verglas` [templates/meteo/M_01] | `sensor.alerte_neige_verglas` [templates/meteo/M_01] | Vigilance neige/verglas |
| `sensor.alerte_grand_froid` [templates/meteo/M_01] | `sensor.alerte_grand_froid` [templates/meteo/M_01] | Vigilance grand froid |
| `sensor.alerte_canicule` [templates/meteo/M_01] | `sensor.alerte_canicule` [templates/meteo/M_01] | Vigilance canicule |
| `sensor.alerte_avalanches` [templates/meteo/M_01] | `sensor.alerte_avalanches` [templates/meteo/M_01] | Vigilance avalanches |
| `sensor.alerte_vagues_submersion` [templates/meteo/M_01] | `sensor.alerte_vagues_submersion` [templates/meteo/M_01] | Vigilance vagues |
| `sensor.alerte_meteo` [templates/meteo/M_01] | `sensor.alerte_meteo` [templates/meteo/M_01] | Synthèse globale (agrège les 9 autres) |

États possibles : `Vert` / `Jaune` / `Orange` / `Rouge`

---

### 📁 `templates/meteo/M_02_meteo_vent_vence_card.yaml`
> 3 sensors template — Vent extrait de `weather.vence` [Météo France - UI] pour windrose-card

| Entité | unique_id | Unité | Rôle |
|--------|-----------|-------|------|
| `sensor.direction_du_vent_vence` [templates/meteo/M_02] | `vence_wind_bearing` | `°` | Angle du vent (0-360°) |
| `sensor.direction_du_vent_vence_label` [templates/meteo/M_02] | `vence_wind_direction_label` | — | Direction cardinale (Nord, Sud-Est…) |
| `sensor.vitesse_du_vent_vence` [templates/meteo/M_02] | `vence_wind_speed_kmh` | `km/h` | Vitesse convertie depuis `weather.vence` [Météo France - UI] |

---

### 📁 `templates/meteo/M_03_meteo_templates_blitzortung.yaml`
> 5 sensors template — Traitement des données Blitzortung pour affichage

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.lightning_direction_label` [templates/meteo/M_03] | `lightning_direction_label` | Direction cardinale de l'éclair (Nord, Nord-Est…) |
| `sensor.lightning_distance_km` [templates/meteo/M_03] | `lightning_distance_km` | Distance en km (pour windrose) |
| `sensor.lightning_bearing` [templates/meteo/M_03] | `lightning_bearing` | Azimut de l'éclair en ° (pour windrose) |
| `sensor.temps_depuis_dernier_impact` [templates/meteo/M_03] | `temps_depuis_le_dernier_impact_de_foudre` | Temps écoulé format h/m/s |
| `sensor.dernier_impact_temps_reel` [templates/meteo/M_03] | `dernier_impact_temps_reel` | Texte "il y a X minutes/heures/jours" |

---

### 📁 `templates/meteo/M_04_tendances_th_ext_card.yaml`
> 2 sensors template — Tendances température/humidité balcon Nord

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.th_balcon_nord_temperature_trend` [templates/meteo/M_04] | `th_balcon_nord_temperature_trend` | Hausse / Stable / Baisse (T°) |
| `sensor.th_balcon_nord_humidity_trend` [templates/meteo/M_04] | `th_balcon_nord_humidity_trend` | Hausse / Stable / Baisse (humidité) |

> Dépend des `input_number` pour stocker la valeur précédente.

---

### 📁 `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml`
> 5 utility meters — Compteurs éclairs par période (source : `sensor.maison_lightning_counter` [HACS Blitzortung - UI])

| Entité | Cycle | unique_id |
|--------|-------|-----------|
| `sensor.eclairs_horaire` [utility_meter/meteo/M_03] | hourly | — |
| `sensor.eclairs_quotidien` [utility_meter/meteo/M_03] | daily | — |
| `sensor.eclairs_hebdomadaire` [utility_meter/meteo/M_03] | weekly | — |
| `sensor.eclairs_mensuel` [utility_meter/meteo/M_03] | monthly | — |
| `sensor.eclairs_annuel` [utility_meter/meteo/M_03] | yearly | — |

---

### 📁 `command_line/meteo/carte_meteo_france.yaml`
> 2 sensors command_line — Images de vigilance Météo France (téléchargées toutes les 4h)

| Entité | unique_id | Source API | Endpoint |
|--------|-----------|------------|---------|
| `sensor.meteo_france_alertes_image_today` [command_line/meteo/carte_meteo_france.yaml] | `meteo_france_alertes_image_today` | api.meteofrance.fr | `vignettenationale-J/encours` |
| `sensor.meteo_france_alertes_image_tomorrow` [command_line/meteo/carte_meteo_france.yaml] | `meteo_france_alertes_image_tomorrow` | api.meteofrance.fr | `vignettenationale-J1/encours` |

> Images sauvegardées localement avec retry (5 tentatives) et image par défaut si indisponible.
> ⚠️ Ces sensors génèrent les `camera.mf_alerte_today` [command_line/meteo/carte_meteo_france.yaml] et `camera.mf_alerte_tomorrow` [command_line/meteo/carte_meteo_france.yaml] utilisées dans le pop-up #ALERT.

---

## 🐛 DÉPANNAGE

### Les iframes Windy ne chargent pas
1. Vérifier que les URLs Windy sont accessibles depuis un navigateur classique
2. Désactiver les bloqueurs de pub/contenu
3. Vérifier les logs HA : `Paramètres > Système > Journaux`

### La windrose-card ne s'affiche pas
1. Vérifier l'installation : HACS > Frontend > `windrose-card`
2. Vider le cache navigateur (`Ctrl+Shift+R`)
3. Vérifier que l'entité `sensor.direction_du_vent_vence` [templates/meteo/M_02] existe

### Le baromètre affiche "N/A"
1. Vérifier l'état de `sensor.vence_pressure` [Météo France - UI] dans Outils de développement > États
2. Re-configurer l'intégration Météo France si nécessaire

### Les compteurs d'éclairs ne se mettent pas à jour
1. Vérifier que l'intégration Blitzortung est active
2. Vérifier les utility_meters dans `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml`
3. Vérifier que `sensor.maison_lightning_counter` [HACS Blitzortung - UI] incrémente bien

### Les pop-ups ne s'ouvrent pas
1. Vérifier que les hashs correspondent exactement (sensibles à la casse)
   - Bouton : `1_link: "#foudre"`
   - Pop-up : `hash: "#foudre"`
2. Vider le cache navigateur

### Progress Bar lever/coucher affiche "--:--:--"
1. Ces sensors sont créés automatiquement par l'intégration Sun
2. Vérifier dans Outils de développement > États qu'ils existent
3. Si absents : `Paramètres > Appareils et services > Sun > Supprimer` puis redémarrer HA

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| Météo France | Intégration native | ✅ Essentiel |
| Blitzortung | HACS | ⚠️ Optionnel (pop-up #foudre uniquement) |
| windrose-card | HACS Frontend | ✅ Recommandé |
| bubble-card | HACS Frontend | ✅ Essentiel |
| ha-tbaro-card | HACS Frontend | ⚠️ Optionnel (baromètre graphique) |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)

- `sensors/meteo/M_03_meteo_sensors_blitzortung.yaml`
- `templates/meteo/M_01_meteo_alertes_card.yaml`
- `templates/meteo/M_02_meteo_vent_vence_card.yaml`
- `templates/meteo/M_03_meteo_templates_blitzortung.yaml`
- `templates/meteo/M_04_tendances_th_ext_card.yaml`
- `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml`
- `command_line/meteo/carte_meteo_france.yaml`

### Documentation
- Vignette d'accès : `docs/L1C1_METEO/L1C1_VIGNETTE_METEO.md`
- Tutoriel cameras : `docs/L1C1_METEO/TUTO_IMAGES_ALERTES_METEO_FRANCE.md`

---

← Retour : `docs/L1C1_METEO/L1C1_VIGNETTE_METEO.md` | → Suivant : `docs/L1C2_METEO/` *(à venir)*
