<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--22-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/temperatures` |
| 🔗 **Accès depuis** | Vignette L1C2 → Dashboard HOME |
| 🏗️ **Layout** | `type: grid` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-14 |
| 🏠 **Version HA** | 2025.2.x → 2.0 |

---

# 🌡️ PAGE TEMPÉRATURES — DOCUMENTATION COMPLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section HEADER](#section-header)
4. [Section EXTÉRIEUR](#section-extérieur)
5. [Section TENDANCES](#section-tendances)
6. [Section CONSOMMATION](#section-consommation)
7. [Section RÉCAP. TEMPÉRATURES](#section-récap-températures)
8. [Section RÉCAP. HUMIDITÉ](#section-récap-humidité)
9. [Sections par pièce (SALON → CHAMBRE)](#sections-par-pièce)
10. [Pop-ups](#pop-ups)
11. [Entités utilisées](#entités-utilisées--provenance-complète)
12. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page complète de suivi thermique et hygrométrique de l'appartement. Elle regroupe :
- Graphique extérieur temps réel (T° + humidité balcon Nord vs Météo France)
- Tendances avec flèches directionnelles (montée/descente/stable)
- Section consommation clim/radiateurs (⚠️ à finaliser avec Pôle 1)
- Récapitulatifs graphiques 24h de toutes les températures et humidités
- Fiches détaillées par pièce (contrôle clim + jauge T°/Humidité)
- 10 pop-ups : delta, extérieur, 7 pièces + 2 courbes tendances

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:apexcharts-card` | Graphiques 24h (extérieur, consommation, récap T°, récap H%) |
| `custom:mushroom-template-card` | Flèches de tendance (T° et humidité balcon) |
| `custom:mini-graph-card` | Courbes 24h dans sections tendances |
| `custom:bubble-card` | Contrôles climate par pièce + pop-ups |
| `custom:streamline-card` | Templates réutilisables (temperature_humidite, carte_des_temperatures, calcule_temp_cible) |
| `custom:vertical-stack-in-card` | Empilement mushroom + mini-graph |
| `custom:temperature-heatmap-card` | Heatmap calendaire T° extérieure (pop-up #exterieur) |
| `custom:mushroom-chips-card` | Chips état clim par pièce (conditionnel) |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌────────────────────────────────────────────────────┐
│  HEADER : TEMPERATURE - HUMIDITÉS                  │
│  Badge: batterie balcon Nord   tap → /0            │
├────────────────────────────────────────────────────┤
│  ApexCharts [Extérieur] 24h                        │
│  humidity balcon (colonnes) + vence_temp + balcon  │
├────────────────────────────────────────────────────┤
│  HEADING : Tendances                               │
│  Badge: sensor.temperature_delta_affichage         │
│  tap → #exterieur                                  │
├────────────────────────────────────────────────────┤
│  horizontal-stack                                  │
│  ┌────────────────────┐  ┌────────────────────┐    │
│  │ Mushroom T° + flèche│  │ Mushroom H% + flèche│   │
│  │ mini-graph T° 24h  │  │ mini-graph H% 24h  │    │
│  │ tap → #tcourbe     │  │ tap → #hcourbe     │    │
│  └────────────────────┘  └────────────────────┘    │
├────────────────────────────────────────────────────┤
│  HEADING : Consommation                            │
│  mushroom-chips-card (chips clim conditionnels)    │
│  ApexCharts [Conso 24h] T° moy + conso clim        │
├────────────────────────────────────────────────────┤
│  HEADING : Récap. Températures                     │
│  ApexCharts 24h — 6 pièces                        │
├────────────────────────────────────────────────────┤
│  HEADING : Récap. Humidité                         │
│  ApexCharts 24h — 6 pièces                        │
├────────────────────────────────────────────────────┤
│  HEADING SALON   + badge clim + badge T° + batterie│
│  bubble-card climate (clim_salon_rm4_mini)         │
│  streamline temperature_humidite                   │
├────────────────────────────────────────────────────┤
│  HEADING CELLIER + badge batterie                  │
│  streamline temperature_humidite                   │
├────────────────────────────────────────────────────┤
│  HEADING CUISINE (RADIATEUR)                       │
│  + badge switch radiateur + badge T° + batterie    │
│  bubble-card climate (radiateur_cuisine)           │
│  streamline temperature_humidite                   │
├────────────────────────────────────────────────────┤
│  HEADING BUREAU  + badge clim + badge T° + batterie│
│  bubble-card climate (clim_bureau_rm4_mini)        │
│  streamline temperature_humidite                   │
├────────────────────────────────────────────────────┤
│  HEADING SALLE DE BAIN + badge T° + batterie       │
│  streamline temperature_humidite                   │
├────────────────────────────────────────────────────┤
│  HEADING CHAMBRE + badge clim + badge T° + batterie│
│  bubble-card climate (clim_chambre_rm4_mini)       │
│  streamline temperature_humidite                   │
├────────────────────────────────────────────────────┤
│  [POP-UPS — vertical-stack cachés]                 │
│  #tendances  #exterieur                            │
│  #salon  #cellier  #cuisine  #bureau               │
│  #salle_de_bain  #chambre                          │
│  #tcourbe  #hcourbe                                │
└────────────────────────────────────────────────────┘
```

---

## 📍 SECTION HEADER

```yaml
type: heading
icon: mdi:thermometer
heading: TEMPERATURE - HUMIDITÉS
heading_style: title
badges:
  - type: entity
    entity: sensor.th_balcon_nord_battery
    color: state
tap_action:
  action: navigate
  navigation_path: /dashboard-tablette/0
layout_options:
  grid_columns: full
  grid_rows: 1
```

### Rôle
- Titre principal de la page
- Badge batterie balcon Nord (couleur `state` → rouge si faible)
- Clic → retour au dashboard HOME

### Entités
- `sensor.th_balcon_nord_battery` [Zigbee - UI]

---

## 🌡️ SECTION EXTÉRIEUR

ApexCharts 24h superposant humidité (colonnes) et températures (courbes).

```yaml
yaxis:
  - id: humidity     # axe gauche  — min ~30, max ~70
  - id: temperature  # axe droit   — min ~10, max ~32
series:
  - sensor.th_balcon_nord_humidity  → colonnes bleues  rgb(19,160,255)
  - sensor.vence_temperature        → courbe orange    (Météo France)
  - sensor.th_balcon_nord_temperature → courbe verte
```

### Entités
- `sensor.th_balcon_nord_humidity` [Zigbee - UI]
- `sensor.th_balcon_nord_temperature` [Zigbee - UI]
- `sensor.vence_temperature` [Météo France - UI]

---

## 📈 SECTION TENDANCES

### Heading
- Badge `sensor.temperature_delta_affichage` [templates/P1] → tap → `#tendances`
- Tap heading → `#exterieur`

### horizontal-stack (2 colonnes)

**Colonne gauche — Température**

| Élément | Détail |
|---------|--------|
| `mushroom-template-card` | Flèche ↗ / ↘ / → selon `sensor.th_balcon_nord_temperature_trend` |
| Couleurs flèche | `increasing` → rouge, `decreasing` → bleu, stable → `#df6366` |
| Valeur secondaire | `{{ states('sensor.th_balcon_nord_temperature') }}°C` (19px) |
| `mini-graph-card` | Courbe T° 24h, couleur `#df6366`, hauteur 200px, `fill: fade` |
| tap_action mushroom | Navigue vers `#tcourbe` |

**Colonne droite — Humidité**

| Élément | Détail |
|---------|--------|
| `mushroom-template-card` | Flèche ↗ / ↘ / → selon `sensor.th_balcon_nord_humidity_trend` |
| Couleurs flèche | `increasing` → bleu, `decreasing` → `#ADD8E6`, stable → `#00CED1` |
| Valeur secondaire | `{{ states('sensor.th_balcon_nord_humidity') }}%` (19px) |
| `mini-graph-card` | Courbe H% 24h, couleur `#00CED1`, hauteur 200px, `fill: fade` |
| tap_action mushroom | Navigue vers `#hcourbe` |

### Entités
- `sensor.th_balcon_nord_temperature` [Zigbee - UI]
- `sensor.th_balcon_nord_humidity` [Zigbee - UI]
- `sensor.th_balcon_nord_temperature_trend` [templates/meteo/M_04]
- `sensor.th_balcon_nord_humidity_trend` [templates/meteo/M_04]

---

## ⚡ SECTION CONSOMMATION

### Chips clim (mushroom-chips-card)

Chips **conditionnels** — s'affichent uniquement si `sensor.{piece}_power_status ≠ "off"` :

| Chip | Icône | Entité état | États affichés |
|------|-------|------------|----------------|
| Salon | `mdi:air-conditioner` | `sensor.clim_salon_etat` | Cool / Heat / Fan / Off |
| Cuisine | `mdi:heating-coil` | `sensor.radiateur_cuisine_etat` | Heat / Off |
| Bureau | `mdi:air-conditioner` | `sensor.clim_bureau_etat` | Cool / Heat / Fan / Off |
| SdB soufflant | `mdi:heat-wave` | `sensor.soufflant_sdb_etat` | Heat / Off |
| SdB sèche-serviette | `mdi:heating-coil` | `sensor.sdb_seche_serviette_etat` | Heat / Off |
| Chambre | `mdi:air-conditioner` | `sensor.clim_chambre_etat` | Cool / Heat / Fan / Off |

Couleurs icônes : `Cool` → `#87CEEB`, `Heat` → `#ff6100`, `Fan` → `#40E0D0`, `Off` → `#FF0000`

### Graphique ApexCharts Consommation (400px)

```
Y-axis gauche : temperature (10-32°C)
Y-axis droite : conso_clim (150W-auto)

Series:
  sensor.temperature_moyenne_interieure  → T̄ Appart. (orange, stroke 4)
  sensor.th_balcon_nord_temperature      → T° Bal.Nrd (vert, stroke 4)
  sensor.conso_clim_rad_total            → Conso. Instan. (colonnes bleues, max/1h)
  sensor.conso_clim_rad_total_quotidien  → Conso. Total (kWh, légende seulement)
  sensor.clim_rad_total_avg_watts_daily  → Moy. depuis Minuit (ligne rouge, stroke 2)
  sensor.conso_clim_rad_total_mensuel    → Mois en cours (légende seulement)
```

Marqueur `Now` en darkred. `cache: true`, `span: start day`.

### Entités Pôle 1

| Entité | Fichier source | Rôle |
|--------|---------------|------|
| `sensor.salon_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance salon ≠ off |
| `sensor.cuisine_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance cuisine ≠ off |
| `sensor.bureau_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance bureau ≠ off |
| `sensor.sdb_soufflant_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance soufflant SdB |
| `sensor.sdb_seche_serviette_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance sèche-serviette |
| `sensor.chambre_power_status` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | Puissance chambre ≠ off |
| `sensor.clim_salon_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État clim salon |
| `sensor.radiateur_cuisine_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État radiateur cuisine |
| `sensor.clim_bureau_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État clim bureau |
| `sensor.soufflant_sdb_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État soufflant SdB |
| `sensor.sdb_seche_serviette_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État sèche-serviette |
| `sensor.clim_chambre_etat` | `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` | État clim chambre |
| `sensor.temperature_moyenne_interieure` | `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | Moyenne T° appart |
| `sensor.conso_clim_rad_total` | `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` | Puissance totale clim+rad (W) |
| `sensor.conso_clim_rad_total_quotidien` | `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | Conso journalière (kWh) |
| `sensor.conso_clim_rad_total_mensuel` | `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | Conso mensuelle (kWh) |
| `sensor.clim_rad_total_avg_watts_daily` | `templates/P1_clim_chauffage/P1_AVG/P1_avg.yaml` | Moyenne watts depuis minuit |
| `sensor.temperature_delta_affichage` | `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | Delta T° int/ext affiché |

---

## 🌡️ SECTION RÉCAP. TEMPÉRATURES

ApexCharts 24h — 6 pièces intérieures (y-axis droite, 10-32°C, groupé par 1h) :

| Pièce | Couleur | Entité |
|-------|---------|--------|
| Salon | `rgb(202, 135, 135)` | `sensor.th_salon_temperature` |
| Cellier | `skyblue` | `sensor.th_cellier_temperature` |
| Cuisine | `rgb(162, 148, 249)` | `sensor.th_cuisine_temperature` |
| Bureau | `orange` | `sensor.th_bureau_temperature` |
| Salle de bain | *(défaut)* | `sensor.th_salle_de_bain_temperature` |
| Chambre | `rgb(177, 194, 158)` | `sensor.th_chambre_temperature` |

---

## 💧 SECTION RÉCAP. HUMIDITÉ

ApexCharts 24h — 6 pièces intérieures (y-axis droite, 30-75%, groupé par 1h, `update_interval: 1m`) :

| Pièce | Couleur | Entité |
|-------|---------|--------|
| Salon | `rgb(202, 135, 135)` | `sensor.th_salon_humidity` |
| Cellier | `skyblue` | `sensor.th_cellier_humidity` |
| Cuisine | `rgb(162, 148, 249)` | `sensor.th_cuisine_humidity` |
| Bureau | `orange` | `sensor.th_bureau_humidity` |
| Salle de bain | *(défaut)* | `sensor.th_salle_de_bain_humidity` |
| Chambre | `rgb(177, 194, 158)` | `sensor.th_chambre_humidity` |

> ✅ Correction appliquée (2026-03-14) : `sensor.th_chambre_humidity` utilisait `yaxis_id: TH` (axe inexistant dans ce graphique → série invisible). Corrigé en `yaxis_id: humidity`.

---

## 🏠 SECTIONS PAR PIÈCE

Chaque pièce suit le même pattern :

```
HEADING [icône] [NOM PIÈCE]
  badges: [clim réglé à] + [T° pièce] + [batterie sonde]
  tap_action → pop-up #{piece}
↓
bubble-card climate (si clim présente)
↓
streamline-card template: temperature_humidite
  variables: card_title, temperature_entity, humidity_entity, icon
```

### Récapitulatif des pièces

| Pièce | Icône | Clim/Chauf | Entité climate | Badge switch |
|-------|-------|-----------|----------------|-------------|
| **SALON** | `mdi:sofa` | Clim | `climate.clim_salon_rm4_mini` [SmartIR - configuration.yaml] | — |
| **CELLIER** | `mdi:food-variant` | Aucun | — | — |
| **CUISINE** | `mdi:fridge` | Radiateur | `climate.radiateur_cuisine` | `switch.radiateur_elec_cuisine` |
| **BUREAU** | `mdi:desktop-tower-monitor` | Clim | `climate.clim_bureau_rm4_mini` [SmartIR - configuration.yaml] | — |
| **SALLE DE BAIN** | `mdi:bathtub` | Soufflant/Sèche-serv. | — *(pas de bubble climate)* | — |
| **CHAMBRE** | `mdi:bed` | Clim | `climate.clim_chambre_rm4_mini` [SmartIR - configuration.yaml] | — |

### bubble-card climate

Chaque bubble-card climate expose :
- Sélecteur mode HVAC (sous-bouton avec flèche)
- Sélecteur vitesse ventilateur (sous-bouton icône `mdi:fan`)
- Couleurs : `Heat` → `#ff6100`, `Fan only` → `#008B8B`

> Note Cuisine : `climate.radiateur_cuisine` utilise `entity:` redondant dans `sub_button` — pas d'impact fonctionnel.

> ✅ Correction appliquée (2026-03-14) : le sous-bouton fan du Bureau référençait `climate.clim_du_bureau` (entité inexistante → fan_modes inopérant). Corrigé en `climate.clim_bureau_rm4_mini`.

### streamline-card `temperature_humidite`

Template réutilisable. Variables requises :

```yaml
variables:
  card_title: "Nom de la pièce"
  temperature_entity: sensor.th_{piece}_temperature
  humidity_entity: sensor.th_{piece}_humidity
  icon: mdi:{icone_piece}
  margin_top: "-150"   # optionnel — Salon uniquement
```

---

## 🪟 POP-UPS

### `#tendances` — Delta Intérieur / Extérieur

```yaml
hash: "#tendances"
name: CALCUL DU DELTA Intérieur <-> Extérieur
icon: mdi:delta
```
Contenu : `streamline-card template: calcule_temp_cible`

#### Logique interne du template `calcule_temp_cible`

Ce template affiche un résumé textuel des **températures cibles actives** selon deux variables combinées :

**Variable 1 — Période de la journée** (via `templates/utilitaires/jour_nuit.yaml`) :

| Sensor | État | Plage horaire |
|--------|------|---------------|
| `binary_sensor.est_jour_7h30_21h` | `on` | 7h30 → 21h00 |
| `binary_sensor.est_nuit_21h_7h30` | `on` | 21h00 → 7h30 |

**Variable 2 — Groupe de présence** (`sensor.groupe`) :

| Valeur | Signification |
|--------|---------------|
| `groupe_1` | Absent / Éco |
| `groupe_2` | Présent partiel (Salon prioritaire) |
| `groupe_3` | Présent partiel (Bureau prioritaire) |
| `groupe_4` | Présent total (confort max) |

**Combinaison → Affichage** :

```
Jour (7h30-21h) + groupe_1  → T° éco_hiver_corrige (tous) / T° cible (Cool) / Fan Only
Jour (7h30-21h) + groupe_2  → Salon: T° confort / Bureau+Chambre: T° cible
Jour (7h30-21h) + groupe_3  → Bureau: T° confort / Salon+Chambre: T° cible
Jour (7h30-21h) + groupe_4  → Salon+Bureau: T° confort / Chambre: T° cible

Nuit (21h-7h30) + groupe_1  → T° éco_hiver_corrige (tous) / T° cible (Cool) / Fan Only
Nuit (21h-7h30) + groupe_2/3/4 → T° confort_nuit (tous) / T° cible (Cool)
```

> Ces entités proviennent de `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` :
> `sensor.groupe`, `sensor.mode_ete_hiver`, `sensor.presence_clim`,
> `sensor.temperature_cible`, `sensor.temperature_confort`,
> `sensor.temperature_confort_nuit`, `sensor.temperature_eco_hiver_corrige`.

### `#exterieur` — Heatmap T° Extérieure

```yaml
hash: "#exterieur"
name: SUIVI DES T° EXTÉRIEUR
icon: mdi:sun-thermometer-outline
```
Contenu : `custom:temperature-heatmap-card`

```yaml
entity: sensor.th_balcon_nord_temperature
forecast_entity: weather.vence
month_label: true
day_label: true
footer: true
day_trend: true
day_forecast: true
```

### `#salon` / `#cellier` / `#cuisine` / `#bureau` / `#salle_de_bain` / `#chambre`

Pattern identique pour chaque pièce :
```yaml
hash: "#[piece]"
name: SUIVI DES T° DE [LA/DU] [PIECE]
```
Contenu : `streamline-card template: carte_des_temperatures`

```yaml
variables:
  entity: sensor.th_{piece}_temperature
  card_title: "Carte des T° de/du [PIECE]"
```

### `#tcourbe` — Tendance Température (détail)

```yaml
hash: "#tcourbe"
name: Tendance (T°)
icon: mdi:thermometer-check
```
Contenu : mushroom-template-card (flèche T°) + mini-graph-card (300px, 24h, labels + extrema + points)

### `#hcourbe` — Tendance Humidité (détail)

```yaml
hash: "#hcourbe"
name: Tendance (Humidité %)
icon: mdi:water-check
```
Contenu : mushroom-template-card (flèche H%) + mini-graph-card (300px, 24h, labels + extrema + points)

> ✅ Corrections appliquées (2026-03-14) :
> - `secondary: }}°C` → `}}%` (unité incorrecte pour un capteur d'humidité)
> - `name: Température` → `name: Humidité` dans le mini-graph-card (label erroné)

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌿 Zigbee - UI (Sonoff SNZB-02)

| Entité | Pièce |
|--------|-------|
| `sensor.th_balcon_nord_temperature` + `_humidity` + `_battery` | Balcon Nord (ext.) |
| `sensor.th_salon_temperature` + `_humidity` + `_battery` | Salon |
| `sensor.th_cellier_temperature` + `_humidity` + `_battery` | Cellier |
| `sensor.th_cuisine_temperature` + `_humidity` + `_battery` | Cuisine |
| `sensor.th_bureau_temperature` + `_humidity` + `_battery` | Bureau |
| `sensor.th_salle_de_bain_temperature` + `_humidity` + `_battery` | Salle de Bain |
| `sensor.th_chambre_temperature` + `_humidity` + `_battery` | Chambre |

### 🌐 Intégrations natives HA (UI)

| Entité | Intégration | Rôle |
|--------|-------------|------|
| `sensor.vence_temperature` | Météo France | T° extérieure officielle (graphique extérieur) |
| `weather.vence` | Météo France | Prévisions (heatmap pop-up #exterieur) |

### ⚙️ SmartIR — configuration.yaml

| Entité | Pièce | Codes IR |
|--------|-------|----------|
| `climate.clim_salon_rm4_mini` | Salon | RM4-Mini, code 1082 |
| `climate.clim_bureau_rm4_mini` | Bureau | RM4-Mini, code 1108 |
| `climate.clim_chambre_rm4_mini` | Chambre | RM4-Mini, code 1108 |
| `climate.radiateur_cuisine` | Cuisine | — |
| `switch.radiateur_elec_cuisine` | Cuisine | Zigbee - UI |

### 📁 `templates/meteo/M_04_tendances_th_ext_card.yaml`

| Entité | Rôle |
|--------|------|
| `sensor.th_balcon_nord_temperature_trend` | `increasing` / `decreasing` / `stable` |
| `sensor.th_balcon_nord_humidity_trend` | `increasing` / `decreasing` / `stable` |

### 📁 `templates/utilitaires/jour_nuit.yaml`

| Entité | Rôle |
|--------|------|
| `binary_sensor.est_jour_7h30_21h` | `on` entre 7h30 et 21h — conditionne l'affichage dans `#tendances` |
| `binary_sensor.est_nuit_21h_7h30` | `on` entre 21h et 7h30 — conditionne l'affichage dans `#tendances` |

> Ces capteurs sont **indépendants du cycle solaire** (lever/coucher). Ils représentent le rythme d'activité du foyer.

### 📁 `templates/P1_clim_chauffage/`

| Fichier | Entités fournies |
|---------|-----------------|
| `ui_dashboard/ui_dashboard.yaml` | `sensor.*_power_status`, `sensor.*_etat` (statuts et états clim/rad par pièce) |
| `P1_TOTAL/P1_TOTAL_AMHQ.yaml` | `sensor.conso_clim_rad_total` (W), `sensor.conso_clim_rad_total_quotidien/mensuel` (kWh) |
| `P1_AVG/P1_avg.yaml` | `sensor.clim_rad_total_avg_watts_daily` (W — moy. depuis minuit) |
| `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | `sensor.temperature_moyenne_interieure`, `sensor.temperature_delta_affichage`, `sensor.groupe`, `sensor.mode_ete_hiver`, `sensor.temperature_cible/confort/confort_nuit/eco_hiver_corrige` |

---

## 🐛 DÉPANNAGE

### ✅ Bugs corrigés le 2026-03-14

| # | Emplacement | Symptôme | Cause | Correction |
|---|-------------|----------|-------|------------|
| 1 | Récap. Humidité — `th_chambre_humidity` | Courbe Chambre invisible | `yaxis_id: TH` (axe inexistant) | → `yaxis_id: humidity` |
| 2 | Popup `#hcourbe` — mushroom secondary | Valeur humidité affichée `°C` | `}}°C` au lieu de `}}%` | → `}}%` |
| 3 | Popup `#hcourbe` — mini-graph-card | Légende affiche "Température" | `name: Température` sur entité humidity | → `name: Humidité` |
| 4 | Bureau — bubble-card fan sub_button | Vitesse ventilateur inopérante | `entity: climate.clim_du_bureau` (inexistante) | → `climate.clim_bureau_rm4_mini` |

---

### Les mushroom-template-cards n'affichent pas de flèche
1. Vérifier que `sensor.th_balcon_nord_temperature_trend` existe → `templates/meteo/M_04_tendances_th_ext_card.yaml`
2. Si `unknown` → l'`input_number` de référence n'est pas encore mis à jour par l'automation associée

### Les bubble-card climate ne répondent pas
1. Vérifier que l'intégration SmartIR est active et que le RM4-Mini est joignable
2. Vérifier que `climate.clim_{piece}_rm4_mini` est dans un état valide dans `Outils de développement → États`

### Les pop-ups de pièces affichent une carte vide
1. Vérifier que le template `streamline-card: carte_des_temperatures` est défini dans la configuration Streamline
2. Les templates Streamline se configurent dans `configuration.yaml` sous `custom_templates:`

### Les chips de consommation ne s'affichent pas
Normal — ils sont `conditional` : ils n'apparaissent que si `sensor.{piece}_power_status ≠ "off"`. Si la clim ne consomme pas (puissance < 50 W), le chip est masqué. Source : `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml`.

### Le graphique de consommation est vide
Vérifier que les entités Pôle 1 sont chargées (`templates/P1_clim_chauffage/`). Si `sensor.conso_clim_rad_total` est `unknown`, recharger la config HA (`Configuration → Vérifier la config` puis `Redémarrer`).

---

## 🔗 FICHIERS LIÉS

### Configuration YAML

- `templates/meteo/M_04_tendances_th_ext_card.yaml` (tendances T° et humidité)
- `templates/utilitaires/jour_nuit.yaml` (binary_sensor jour/nuit — popup `#tendances`)
- `configuration.yaml` (SmartIR : clim salon, bureau, chambre)
- `templates/P1_clim_chauffage/ui_dashboard/ui_dashboard.yaml` (statuts et états clim/rad)
- `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` (totaux kWh + puissance W)
- `templates/P1_clim_chauffage/P1_AVG/P1_avg.yaml` (moyennes watts AMHQ)
- `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` (logique groupe, T° cible, delta)
- `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` (compteurs kWh clim)

### Documentation

- Vignette d'accès : `docs/L1C2_TEMPERATURES/L1C2_VIGNETTE_TEMPERATURES.md`
- Pôle 1 complet : *(doc à créer)*

---

← Retour : `docs/L1C2_TEMPERATURES/L1C2_VIGNETTE_TEMPERATURES.md` | → Suivant : `docs/L1C3_COMMANDES_CLIM/` *(à venir)*
