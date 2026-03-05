<div align="center">

[![Statut](https://img.shields.io/badge/Statut-%E2%9B%94%20A%20terminer-f44336?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--01-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20Doc-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/temperatures` |
| 🔗 **Accès depuis** | Vignette L1C3 → Dashboard HOME |
| 🏗️ **Layout** | `type: grid` |
| 🔴 **Statut** | Page à terminer — bloquée sur Pôle 1 |
| 🚧 **Bloquant** | Sensors Pôle 1 (clim/rad) non encore créés dans ReBuild |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-01 |
| 🏠 **Version HA** | 2025.1.x → 2.0 |

---

# 🌡️ PAGE TEMPÉRATURES — DOCUMENTATION COMPLÈTE

---

> ## ⛔ PAGE À TERMINER — BLOCAGE PARTIEL
>
> **Cause : Pôle 1 (Chauffage / Clim) non finalisé dans ReBuild**
>
> Sections bloquées — **ne pas implémenter avant Pôle 1** :
> - Section **CONSOMMATION** (chips + graphique conso) → dépend de `p1_0_sensors_clim_rad.yaml`
> - Blocs **par pièce** → `bubble-card climate` + entités `power_status` / `*_etat` (Pôle 1)
> - Pop-up **#tendances** → ~~`streamline-card: calcule_temp_cible`~~ ✅ implémentable — sensor disponible
>
> **Ce qui fonctionne déjà :**
> - Section Extérieur (ApexCharts Balcon Nord + Météo France) ✅
> - Section Tendances Balcon Nord (mushroom-template + mini-graph) ✅
> - Récap températures et humidités (6 pièces) ✅
> - Headings par pièce + streamline `temperature_humidite` ✅
>
> **En cours d'implémentation (indépendant du Pôle 1) :**
> - Pop-ups heatmaps par pièce (`#exterieur`, `#salon` → `#chambre`) 🔧
> - Pop-ups courbes tendance (`#tcourbe`, `#hcourbe`) 🔧
> - Pop-up **#tendances** → `custom:streamline-card` template `calcule_temp_cible` 🔧
>   *(sensor `sensor.temperature_delta_affichage` disponible dans `templates/P1_/P1_01_MASTER`)*
>
> **Reprendre la partie bloquée quand :** `sensors/p1_0_sensors_clim_rad.yaml` et `utility_meter/p1_...` sont migrés dans ReBuild.

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture de la page](#architecture-de-la-page)
3. [Section HEADER](#section-header)
4. [Section EXTÉRIEUR](#section-extérieur)
5. [Section TENDANCES — Balcon Nord](#section-tendances--balcon-nord)
6. [Section CONSOMMATION](#section-consommation)
7. [Section RÉCAP TEMPÉRATURES](#section-récap-températures)
8. [Section RÉCAP HUMIDITÉ](#section-récap-humidité)
9. [Sections PAR PIÈCE](#sections-par-pièce)
10. [Pop-ups](#pop-ups)
11. [Streamline Templates](#streamline-templates)
12. [Entités utilisées](#entités-utilisées--provenance-complète)
13. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page de suivi thermique complet de l'appartement. Elle regroupe :

- Graphique extérieur (Balcon Nord + Météo France, 24h)
- Tendances temp/humidité Balcon Nord avec flèches directionnelles
- Chips consommation chauffage/clim actifs en temps réel
- Graphique combiné T° moyenne intérieure + consommation clim/rad
- Récapitulatifs 24h températures et humidités (6 pièces)
- Blocs par pièce : heading avec badges + contrôle clim + courbes
- 9 pop-ups : delta, extérieur heatmap, 6 heatmaps pièces, courbe T°, courbe humidité

> ⚠️ Page en cours de reconstruction — certaines sections sont provisoires ou incomplètes.

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `apexcharts-card` | Graphiques 24h (extérieur, récap, conso) |
| `mini-graph-card` | Courbes tendance (pop-ups tcourbe/hcourbe) |
| `mushroom-template-card` | Flèches tendance + valeur actuelle |
| `mushroom-chips-card` | Chips conditionnels chauffage actif |
| `bubble-card` (climate) | Contrôle clim/radiateur par pièce |
| `bubble-card` (pop-up) | 9 pop-ups de détail |
| `vertical-stack-in-card` | Groupement mushroom + mini-graph |
| `streamline-card` | Templates réutilisables (temp_humidite, heatmaps, delta) |
| `temperature-heatmap-card` | Heatmap calendrier T° extérieure |

---

## 🏗️ ARCHITECTURE DE LA PAGE

```
┌─────────────────────────────────────────────────────┐
│  [HEADER] TEMPERATURE - HUMIDITES                   │
│  Badge: batterie Balcon Nord                        │
├─────────────────────────────────────────────────────┤
│  [APEXCHARTS] Extérieur 24h                         │
│  Balcon Nord T° + Humidité + Météo France Vence     │
├─────────────────────────────────────────────────────┤
│  [HEADING] Tendances                                │
│  Badge: Δ Température (→ pop-up #tendances)         │
├─────────────────────────────────────────────────────┤
│  [HORIZONTAL-STACK]                                 │
│  ┌────────────────────┐ ┌────────────────────┐      │
│  │ Mushroom T° trend  │ │ Mushroom H% trend  │      │
│  │ Mini-graph 24h T°  │ │ Mini-graph 24h H%  │      │
│  └────────────────────┘ └────────────────────┘      │
├─────────────────────────────────────────────────────┤
│  [HEADING] Consommation                             │
├─────────────────────────────────────────────────────┤
│  [MUSHROOM-CHIPS] Chauffage actif (conditionnel)    │
│  Salon | Cuisine | Bureau | SdB×2 | Chambre         │
├─────────────────────────────────────────────────────┤
│  [APEXCHARTS] T° Moy. Appart + T° Balcon           │
│  + Conso Clim/Rad (colonnes) + Moy. depuis minuit  │
├─────────────────────────────────────────────────────┤
│  [HEADING] Récap. Températures                      │
│  [APEXCHARTS] 6 pièces / 24h                        │
├─────────────────────────────────────────────────────┤
│  [HEADING] Récap. Humidité                          │
│  [APEXCHARTS] 6 pièces / 24h                        │
├─────────────────────────────────────────────────────┤
│  [HEADING SALON] badges clim + T° + batterie        │
│  [BUBBLE-CARD climate] clim_salon_rm4_mini          │
│  [STREAMLINE] temperature_humidite → Salon          │
├─────────────────────────────────────────────────────┤
│  [HEADING CELLIER] badge batterie                   │
│  [STREAMLINE] temperature_humidite → Cellier        │
├─────────────────────────────────────────────────────┤
│  [HEADING CUISINE] badges switch + T° + batterie    │
│  [BUBBLE-CARD climate] radiateur_cuisine            │
│  [STREAMLINE] temperature_humidite → Cuisine        │
├─────────────────────────────────────────────────────┤
│  [HEADING BUREAU] badges clim + T° + batterie       │
│  [BUBBLE-CARD climate] clim_bureau_rm4_mini         │
│  [STREAMLINE] temperature_humidite → Bureau         │
├─────────────────────────────────────────────────────┤
│  [HEADING SDB] badges T° + batterie                 │
│  [STREAMLINE] temperature_humidite → Salle de Bain  │
├─────────────────────────────────────────────────────┤
│  [HEADING CHAMBRE] badges clim + T° + batterie      │
│  [BUBBLE-CARD climate] clim_chambre_rm4_mini        │
│  [STREAMLINE] temperature_humidite → Chambre        │
├─────────────────────────────────────────────────────┤
│  POP-UPS (vertical-stack, hors vue)                 │
│  #tendances #exterieur #salon #cellier #cuisine     │
│  #bureau #salle_de_bain #chambre #tcourbe #hcourbe  │
└─────────────────────────────────────────────────────┘
```

---

## 📍 SECTION HEADER

```yaml
- type: heading
  icon: mdi:thermometer
  heading: TEMPERATURE - HUMIDITEES
  heading_style: title
  badges:
    - type: entity
      show_state: true
      show_icon: true
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
Titre principal de la page. Le badge batterie surveille la sonde Zigbee du Balcon Nord (critique car c'est la référence extérieure de tout le système thermique). Clic → retour au dashboard principal `/0`.

### Entités
- `sensor.th_balcon_nord_battery` [Zigbee - UI] — Batterie sonde Sonoff Balcon Nord

---

## 🌡️ SECTION EXTÉRIEUR

Graphique ApexCharts double axe sur 24h.

```yaml
- type: custom:apexcharts-card
  graph_span: 24h
  apex_config:
    chart:
      height: 250px
  header:
    show: true
    title: Extèrieur
    show_states: true
    colorize_states: true
  yaxis:
    - id: humidity       # Axe gauche: 30~70%, 10 ticks
    - id: temperature    # Axe droit (opposite): 10~32°C, 10 ticks
  all_series_config:
    group_by:
      func: last
      duration: 30m
    show:
      legend_value: false
      extremas: true
  series:
    - entity: sensor.th_balcon_nord_humidity   # colonnes, bleu
    - entity: sensor.vence_temperature         # ligne orange = Météo France
    - entity: sensor.th_balcon_nord_temperature # ligne verte = sonde physique
```

### Double axe Y

| Axe | ID | Plage | Côté | Données |
|:----|:---|:------|:-----|:--------|
| Gauche | `humidity` | 30~70% | gauche | Humidité Balcon Nord (colonnes) |
| Droit | `temperature` | 10~32°C | opposé | T° Météo France + T° Balcon Nord (lignes) |

> **Intérêt de la double série température :** comparer la mesure physique de la sonde (`sensor.th_balcon_nord_temperature`) avec la valeur officielle de Météo France (`sensor.vence_temperature`) — les écarts révèlent l'exposition solaire ou l'effet de masse thermique du balcon.

### Entités
- `sensor.th_balcon_nord_humidity` [Zigbee - UI]
- `sensor.vence_temperature` [Météo France - UI]
- `sensor.th_balcon_nord_temperature` [Zigbee - UI]

---

## 📈 SECTION TENDANCES — BALCON NORD

Bloc horizontal composé de deux colonnes symétriques (température gauche, humidité droite).

### Structure d'une colonne

```
vertical-stack-in-card
  └── mushroom-template-card   ← flèche tendance + valeur actuelle
  └── mini-graph-card          ← courbe 24h (200px)
```

### Mushroom template — Logique flèche

```yaml
# Icône (même logique pour T° et humidité)
icon: >
  {% if is_state('sensor.th_balcon_nord_temperature_trend', 'increasing') %}
    mdi:arrow-top-right-thick       # ↗ rouge
  {% elif is_state('sensor.th_balcon_nord_temperature_trend', 'decreasing') %}
    mdi:arrow-bottom-right-thick    # ↘ bleu
  {% else %}
    mdi:arrow-right-thick           # → couleur neutre
  {% endif %}
```

### Palette couleurs tendance

| État sensor_trend | T° couleur | H% couleur | Icône |
|:------------------|:-----------|:-----------|:------|
| `increasing` | `red` | `blue` | ↗ |
| `decreasing` | `blue` | `#ADD8E6` | ↘ |
| stable | `#df6366` | `#00CED1` | → |

> Les couleurs sont **inversées** entre T° et H% : une humidité qui monte = bleu (froid/humide), alors qu'une T° qui monte = rouge (chaud).

### Card-mod CSS — Shadow DOM

Ces cartes utilisent le **shadow DOM piercing** (`$:`) pour styler les sous-composants Mushroom :

```css
mushroom-state-info$: |
  .secondary { font-size: 19px !important; }   /* Valeur principale */
  .primary   { font-size: 12px !important; }   /* Label secondaire */

mushroom-shape-icon$: |
  .shape { position: relative; }               /* Icône */

.: |
  :host { --mush-icon-size: 50px; }           /* Taille icône via CSS var */
```

> ⚠️ La syntaxe `$:` est spécifique à `card-mod` et permet d'accéder aux slots shadow DOM de Mushroom. Sans le `$`, les styles n'ont aucun effet sur les composants internes.

### Entités tendances
- `sensor.th_balcon_nord_temperature_trend` [templates/meteo/M_04] — `increasing` / `decreasing` / `stable`
- `sensor.th_balcon_nord_humidity_trend` [templates/meteo/M_04]

### Navigation pop-up
- Clic T° → `#tcourbe` (courbe tendance T° 300px, détaillée)
- Clic H% → `#hcourbe` (courbe tendance H% 300px, détaillée)

---

## ⚡ SECTION CONSOMMATION

### Chips conditionnels (mushroom-chips-card)

6 chips, tous conditionnels — **n'apparaissent que si l'appareil consomme** (power_status ≠ "off").

| Chip | Condition | Icône | Modes affichés |
|:-----|:----------|:------|:---------------|
| Salon | `sensor.salon_power_status ≠ off` | `mdi:air-conditioner` | Cool / Heat / Fan / Off |
| Cuisine | `sensor.cuisine_power_status ≠ off` | `mdi:heating-coil` | Heat / Off |
| Bureau | `sensor.bureau_power_status ≠ off` | `mdi:air-conditioner` | Cool / Heat / Fan / Off |
| SdB Soufflant | `sensor.sdb_soufflant_power_status ≠ off` | `mdi:heat-wave` | Heat / Off |
| SdB Sèche-serviette | `sensor.sdb_seche_serviette_power_status ≠ off` | `mdi:heating-coil` | Heat / Off |
| Chambre | `sensor.chambre_power_status ≠ off` | `mdi:air-conditioner` | Cool / Heat / Fan / Off |

### Palette couleurs mode clim

| Mode | Couleur | HEX |
|:-----|:--------|:----|
| Cool | Bleu ciel | `#87CEEB` |
| Heat | Orange vif | `#ff6100` |
| Fan | Turquoise | `#40E0D0` |
| Off | Rouge | `#FF0000` |

### Graphique combiné T° + Conso

```yaml
- type: custom:apexcharts-card
  graph_span: 24h
  span:
    start: day      # Depuis minuit, pas les dernières 24h glissantes
  series:
    - entity: sensor.temperature_moyenne_interieure  # ligne orange, yaxis: temperature
    - entity: sensor.th_balcon_nord_temperature      # ligne verte, yaxis: temperature
    - entity: sensor.conso_clim_rad_total            # colonnes bleues, yaxis: conso_clim
    - entity: sensor.conso_clim_rad_total_quotidien  # in_chart: false → légende seulement
    - entity: sensor.clim_rad_total_avg_watts_daily  # ligne rouge (moy. depuis minuit)
    - entity: sensor.conso_clim_rad_total_mensuel    # in_chart: false → légende seulement
```

> **`span: start: day`** : le graphique repart à zéro à minuit, contrairement à `graph_span: 24h` qui est glissant. Idéal pour les consommations journalières.

> **`show: in_chart: false`** sur les entités quotidien/mensuel : ces valeurs apparaissent uniquement dans l'en-tête du graphique (show_states: true) sans courbe dans le graphique — c'est un affichage de KPI discret.

### Entités consommation
- `sensor.temperature_moyenne_interieure` [sensors/p1] — Moyenne T° intérieure calculée
- `sensor.conso_clim_rad_total` [sensors/p1] — Conso instantanée totale clim+rad (W)
- `sensor.conso_clim_rad_total_quotidien` [utility_meter/p1] — Total jour (kWh)
- `sensor.conso_clim_rad_total_mensuel` [utility_meter/p1] — Total mois (kWh)
- `sensor.clim_rad_total_avg_watts_daily` [sensors/p1] — Moyenne W depuis minuit

---

## 🌡️ SECTION RÉCAP TEMPÉRATURES

ApexCharts 24h, axe Y droit uniquement (10~32°C), 6 séries pièces.

```yaml
series:
  - entity: sensor.th_salon_temperature       # rgb(202,135,135) — rose
  - entity: sensor.th_cellier_temperature     # skyblue
  - entity: sensor.th_cuisine_temperature     # rgb(162,148,249) — violet
  - entity: sensor.th_bureau_temperature      # orange
  - entity: sensor.th_salle_de_bain_temperature  # défaut
  - entity: sensor.th_chambre_temperature     # rgb(177,194,158) — vert sauge
```

> Pas de Balcon Nord ici — il est déjà dans le graphique Extérieur en haut de page.

---

## 💧 SECTION RÉCAP HUMIDITÉ

Même structure que le récap températures, axe Y droit (30~75%), `update_interval: 1m`.

> ⚠️ **Bug repéré** : la série `sensor.th_chambre_humidity` est associée à `yaxis_id: TH` au lieu de `yaxis_id: humidity`. Elle ne sera pas rendue sur le bon axe. À corriger.

```yaml
# Correction à appliquer :
- entity: sensor.th_chambre_humidity
  yaxis_id: humidity    # était: TH
```

---

## 🏠 SECTIONS PAR PIÈCE

Chaque pièce suit le même pattern :

```
[HEADING] NOM_PIECE
  badges: [clim_target] [temp_actuelle] [batterie]  ← selon pièce
[BUBBLE-CARD climate] ← si pièce a clim ou radiateur (pas Cellier, pas SdB)
[STREAMLINE-CARD] template: temperature_humidite
```

### Récapitulatif par pièce

| Pièce | Heading icon | Bubble-card climate | Entity clim |
|:------|:-------------|:--------------------|:------------|
| SALON | `mdi:sofa` | ✅ | `climate.clim_salon_rm4_mini` |
| CELLIER | `mdi:food-variant` | ❌ | — |
| CUISINE | `mdi:fridge` | ✅ | `climate.radiateur_cuisine` |
| BUREAU | `mdi:desktop-tower-monitor` | ✅ | `climate.clim_bureau_rm4_mini` |
| SALLE DE BAIN | `mdi:bathtub` | ❌ | — |
| CHAMBRE | `mdi:bed` | ✅ | `climate.clim_chambre_rm4_mini` |

### Bubble-card climate — Sub-buttons

Les clims (Salon, Bureau, Chambre) ont 2 sub-buttons :
- **HVAC modes** : sélecteur de mode (heat/cool/fan/off) avec flèche
- **Fan modes** : sélecteur vitesse ventilateur avec icône `mdi:fan`

La Cuisine n'a qu'un sub-button HVAC (pas de fan_mode sur radiateur bain d'huile).

```yaml
styles: |
  ha-card {
    --bubble-state-climate-fan-only-color: #008B8B;   # turquoise
    --bubble-state-climate-heat-color: #ff6100;        # orange
  }
```

### Streamline template `temperature_humidite`

Utilisé 6 fois (une par pièce). Variables injectées :

```yaml
- type: custom:streamline-card
  template: temperature_humidite
  variables:
    card_title: Salon
    temperature_entity: sensor.th_salon_temperature
    humidity_entity: sensor.th_salon_humidity
    margin_top: "-150"   # Uniquement Salon (chevauchement avec bubble-card)
    icon: mdi:sofa
```

> `margin_top: "-150"` sur le Salon uniquement — compense la hauteur de la bubble-card climate pour éviter un espace vide trop important entre la carte clim et la carte streamline.

> 📌 Le contenu exact du template `temperature_humidite` est à documenter séparément — voir section [Streamline Templates](#streamline-templates).

---

## 🪟 POP-UPS

9 pop-ups déclarés en bas de page dans des `vertical-stack`. Tous utilisent `bubble-card: pop-up` avec `bg_opacity: "0"`.

| Hash | Nom affiché | Contenu |
|:-----|:------------|:--------|
| `#tendances` | CALCUL DU DELTA Intérieur ↔ Extérieur | `custom:streamline-card` → template `calcule_temp_cible` · sensor : `sensor.temperature_delta_affichage` [templates/P1_/P1_01_MASTER] · bas de pop-up : `sensor.groupe` + `sensor.presence` [templates/P4_groupe_presence] |
| `#exterieur` | SUIVI DES T° EXTÉRIEUR | `temperature-heatmap-card` — Balcon Nord |
| `#salon` | SUIVI DES T° DU SALON | `streamline-card: carte_des_temperatures` |
| `#cellier` | SUIVI DES T° DU CELLIER | `streamline-card: carte_des_temperatures` |
| `#cuisine` | SUIVI DES T° DE LA CUISINE | `streamline-card: carte_des_temperatures` |
| `#bureau` | SUIVI DES T° DU BUREAU | `streamline-card: carte_des_temperatures` |
| `#salle_de_bain` | SUIVI DES T° DE LA SALLE DE BAIN | `streamline-card: carte_des_temperatures` |
| `#chambre` | SUIVI DES T° DE LA CHAMBRE | `streamline-card: carte_des_temperatures` |
| `#tcourbe` | Tendance (T°) | mushroom-template + mini-graph 300px |
| `#hcourbe` | Tendance (Humidité %) | mushroom-template + mini-graph 300px |

### Accès aux pop-ups

| Pop-up | Déclencheur |
|:-------|:------------|
| `#tendances` | Badge Δ dans le heading Tendances |
| `#exterieur` | Heading Tendances (tap_action) |
| `#salon` → `#chambre` | Heading de chaque pièce (tap_action) |
| `#tcourbe` | Tap sur mushroom T° dans section Tendances |
| `#hcourbe` | Tap sur mushroom H% dans section Tendances |

### Pop-up #tendances — Détail `calcule_temp_cible`

Le bas du pop-up affiche une ligne de diagnostic résumant le groupe de présence actif et le statut réseau :

```jinja2
Groupe = {{ states('sensor.groupe') }}  -  Presence = {{ states('sensor.presence') }}
```

> ⚠️ **Migration requise dans le template `calcule_temp_cible`** (dans le dashboard)
>
> Le template référence encore les **anciens noms** `sensor.groupe_clim` et `sensor.presence_clim` qui **n'existent plus**.
> Depuis la création du **Pôle 4**, ces sensors ont été généralisés (ils pilotent clim ET prises) et renommés :
>
> | Ancien nom (orphelin) | Nouveau nom P4 | Source |
> |:----------------------|:---------------|:-------|
> | `sensor.groupe_clim` | `sensor.groupe` | `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml` |
> | `sensor.presence_clim` | `sensor.presence` | `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml` |
>
> **Action :** dans le dashboard, remplacer les 2 occurrences dans la définition du streamline template `calcule_temp_cible`.

### States `sensor.groupe`

| Valeur | Signification |
|:-------|:--------------|
| `groupe_1` | Personne à la maison |
| `groupe_2` | Mamour seule |
| `groupe_3` | Eric seul |
| `groupe_4` | Eric + Mamour |

### States `sensor.presence`

Affichage textuel du statut réseau des deux téléphones sur `Freebox_GG` :

| Exemple | Signification |
|:--------|:--------------|
| `[2] en [WIFI]` | Les deux en WiFi maison |
| `[Mamour: WIFI/CELL]` | Mamour WiFi, Eric 4G |
| `[Eric: WIFI/CELL]` | Eric WiFi, Mamour 4G |
| `[CELL / CELL]` | Tous les deux hors maison |
| `[2] en [WIFI_!?]` | WiFi mais pas sur Freebox_GG |

---

### Temperature-heatmap-card (pop-up #exterieur)

```yaml
- type: custom:temperature-heatmap-card
  entity: sensor.th_balcon_nord_temperature
  title: Carte des T° EXTÉRIEUR
  month_label: true
  day_label: true
  footer: true
  day_trend: true
  day_forecast: true
  forecast_entity: weather.vence    # Prévisions MF intégrées
  force_fahrenheit: false
  decimal_point: true
```

---

## 📦 STREAMLINE TEMPLATES

Ces templates sont appelés par `custom:streamline-card` mais définis dans un fichier de configuration séparé. Ils sont à documenter individuellement.

| Template | Utilisé | Rôle estimé |
|:---------|:--------|:------------|
| `temperature_humidite` | ×6 (une par pièce) | Affichage T° + H% avec mini-graph ou jauge |
| `carte_des_temperatures` | ×7 (extérieur + 6 pièces) | Heatmap ou graphique historique T° de la pièce |
| `calcule_temp_cible` | ×1 (pop-up #tendances) | Affiche `sensor.temperature_delta_affichage` — source : `templates/P1_/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |

> 📌 **À documenter** : récupérer le YAML de chaque template streamline pour compléter cette section.

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Zigbee — Sondes Sonoff SNZB-02 (UI)

| Entité | Pièce | Type |
|:-------|:------|:-----|
| `sensor.th_balcon_nord_temperature` [Zigbee - UI] | Balcon Nord | Température |
| `sensor.th_balcon_nord_humidity` [Zigbee - UI] | Balcon Nord | Humidité |
| `sensor.th_balcon_nord_battery` [Zigbee - UI] | Balcon Nord | Batterie |
| `sensor.th_salon_temperature` [Zigbee - UI] | Salon | Température |
| `sensor.th_salon_humidity` [Zigbee - UI] | Salon | Humidité |
| `sensor.th_salon_battery` [Zigbee - UI] | Salon | Batterie |
| `sensor.th_cellier_temperature` [Zigbee - UI] | Cellier | Température |
| `sensor.th_cellier_humidity` [Zigbee - UI] | Cellier | Humidité |
| `sensor.th_cellier_battery` [Zigbee - UI] | Cellier | Batterie |
| `sensor.th_cuisine_temperature` [Zigbee - UI] | Cuisine | Température |
| `sensor.th_cuisine_humidity` [Zigbee - UI] | Cuisine | Humidité |
| `sensor.th_cuisine_battery` [Zigbee - UI] | Cuisine | Batterie |
| `sensor.th_bureau_temperature` [Zigbee - UI] | Bureau | Température |
| `sensor.th_bureau_humidity` [Zigbee - UI] | Bureau | Humidité |
| `sensor.th_bureau_battery` [Zigbee - UI] | Bureau | Batterie |
| `sensor.th_salle_de_bain_temperature` [Zigbee - UI] | SdB | Température |
| `sensor.th_salle_de_bain_humidity` [Zigbee - UI] | SdB | Humidité |
| `sensor.th_salle_de_bain_battery` [Zigbee - UI] | SdB | Batterie |
| `sensor.th_chambre_temperature` [Zigbee - UI] | Chambre | Température |
| `sensor.th_chambre_humidity` [Zigbee - UI] | Chambre | Humidité |
| `sensor.th_chambre_battery` [Zigbee - UI] | Chambre | Batterie |

### 🌐 Météo France — Intégration native (UI)

| Entité | Rôle |
|:-------|:-----|
| `sensor.vence_temperature` [Météo France - UI] | T° officielle Vence (comparaison) |
| `weather.vence` [Météo France - UI] | Prévisions (temperature-heatmap forecast) |

### 🏠 Climate — Intégrations clim/radiateur (UI)

| Entité | Pièce | Type |
|:-------|:------|:-----|
| `climate.clim_salon_rm4_mini` [RM4 Mini - UI] | Salon | Climatiseur |
| `climate.radiateur_cuisine` [Sonoff - UI] | Cuisine | Radiateur bain d'huile |
| `climate.clim_bureau_rm4_mini` [RM4 Mini - UI] | Bureau | Climatiseur |
| `climate.clim_chambre_rm4_mini` [RM4 Mini - UI] | Chambre | Climatiseur |
| `switch.radiateur_elec_cuisine` [Sonoff - UI] | Cuisine | Switch direct radiateur |

### 📁 `sensors/p1_...` — Sensors calculés Pôle 1

| Entité | Rôle |
|:-------|:-----|
| `sensor.temperature_moyenne_interieure` [sensors/p1] | Moyenne T° toutes pièces |
| `sensor.conso_clim_rad_total` [sensors/p1] | Conso instantanée totale clim+rad (W) |
| `sensor.clim_rad_total_avg_watts_daily` [sensors/p1] | Moyenne W depuis minuit |
| `sensor.salon_power_status` [sensors/p1] | État ON/OFF clim salon |
| `sensor.cuisine_power_status` [sensors/p1] | État ON/OFF radiateur cuisine |
| `sensor.bureau_power_status` [sensors/p1] | État ON/OFF clim bureau |
| `sensor.sdb_soufflant_power_status` [sensors/p1] | État ON/OFF soufflant SdB |
| `sensor.sdb_seche_serviette_power_status` [sensors/p1] | État ON/OFF sèche-serviette |
| `sensor.chambre_power_status` [sensors/p1] | État ON/OFF clim chambre |
| `sensor.clim_salon_etat` [sensors/p1] | Mode clim Salon (Cool/Heat/Fan/Off) |
| `sensor.radiateur_cuisine_etat` [sensors/p1] | Mode radiateur Cuisine |
| `sensor.clim_bureau_etat` [sensors/p1] | Mode clim Bureau |
| `sensor.soufflant_sdb_etat` [sensors/p1] | Mode soufflant SdB |
| `sensor.sdb_seche_serviette_etat` [sensors/p1] | Mode sèche-serviette SdB |
| `sensor.clim_chambre_etat` [sensors/p1] | Mode clim Chambre |

### 📁 `utility_meter/p1_...` — Compteurs énergie

| Entité | Cycle |
|:-------|:------|
| `sensor.conso_clim_rad_total_quotidien` [utility_meter/p1] | Journalier (kWh) |
| `sensor.conso_clim_rad_total_mensuel` [utility_meter/p1] | Mensuel (kWh) |

### 📁 `templates/P4_groupe_presence/` — Présence & Groupe (P4)

> Utilisés dans le bas du pop-up `#tendances` via le streamline template `calcule_temp_cible`.

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.groupe` | `groupe` | Groupe actif : `groupe_1` (personne) / `groupe_2` (Mamour) / `groupe_3` (Eric) / `groupe_4` (tous) |
| `sensor.presence` | `presence` | Affichage statut réseau des 2 téléphones sur `Freebox_GG` |

> Ces sensors sont définis dans `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml` et remplacent les anciens `sensor.groupe_clim` / `sensor.presence_clim` (orphelins — à corriger dans le dashboard).

---

### 📁 `templates/meteo/M_04` — Tendances T°/H%

| Entité | Rôle |
|:-------|:-----|
| `sensor.th_balcon_nord_temperature_trend` [templates/meteo/M_04] | `increasing` / `decreasing` / `stable` |
| `sensor.th_balcon_nord_humidity_trend` [templates/meteo/M_04] | `increasing` / `decreasing` / `stable` |
| `sensor.temperature_delta_affichage` [templates/P1_/P1_01_MASTER] | Affichage formaté : `T̄i X.X°C  Te X.X°C  ΔT = X.X°C` |

---

## 🐛 DÉPANNAGE

### Bug yaxis_id humidité Chambre

```yaml
# Dans la section Récap Humidité, corriger :
- entity: sensor.th_chambre_humidity
  yaxis_id: humidity    # ← était "TH", mauvais axe
```

### Les chips consommation ne disparaissent pas

Vérifier que les `power_status` sensors ont bien l'état `"off"` (string, pas booléen) quand l'appareil est inactif. La condition `state_not: "off"` est strictement textuelle.

### Le mushroom-template ne se met pas à jour

Si la flèche tendance reste fixe : vérifier que `sensor.th_balcon_nord_temperature_trend` existe et change bien d'état. Ce sensor dépend de `templates/meteo/M_04`.

### `streamline-card` affiche une erreur

Vérifier que `custom:streamline-card` est installé via HACS et que les templates sont définis dans la configuration streamline. Les templates `temperature_humidite`, `carte_des_temperatures` et `calcule_temp_cible` doivent être déclarés.

---

## 🔗 FICHIERS LIÉS

### Configuration YAML
- `templates/P1_/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` — `sensor.temperature_delta_affichage` + logique système clim
- `templates/P1_/P1_AVG/P1_avg.yaml` — moyennes W par appareil
- `templates/meteo/M_04_tendances_th_ext_card.yaml` — tendances T°/H% balcon
- `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml` — `sensor.groupe` + `sensor.presence` *(pop-up #tendances bas)*
- `sensors/p1_0_sensors_clim_rad.yaml` — sensors power_status, états *(à migrer)*
- `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` — compteurs kWh clim/rad

### Documentation
- Vignette d'accès : `docs/L1C3_TEMPERATURES/L1C3_VIGNETTE_TEMPERATURES.md`
- Streamline templates : à documenter *(à venir)*

---

← Retour : `docs/L1C3_TEMPERATURES/L1C3_VIGNETTE_TEMPERATURES.md` | → Suivant : *(page en cours de reconstruction)*
