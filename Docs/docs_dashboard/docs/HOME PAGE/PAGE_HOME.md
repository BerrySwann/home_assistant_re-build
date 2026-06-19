<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--06--13-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `Dashboard 2026-06-13 → Vue: Home (page principale)` |
| 🔗 **Accès depuis** | Vue par défaut au démarrage |
| 🏗️ **Layout** | `type: grid` — 1 col (cartes permanentes) + grille 3×6 (18 vignettes) |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-06-13 |
| 🏠 **Version HA** | 2026.6.x |

---

# 🏠 PAGE HOME — Dashboard Principal

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Cartes permanentes](#cartes-permanentes)
   - [Météo animée (meteocss)](#1--météo-animée-meteocss--picture-elements)
   - [Météo France (détails)](#2--météo-france-détails--meteofrance-weather-card)
   - [VS Code Server](#3--vs-code-server-conditionnel)
   - [Foudre Blitzortung](#4--foudre-blitzortung-conditionnel)
   - [Lave-linge](#5--lave-linge-conditionnel)
   - [Lave-vaisselle](#6--lave-vaisselle-conditionnel)
   - [Présence Personne(s)](#7--présence-personnes)
   - [Détecteur de fuite](#8--détecteur-de-fuite-conditionnel)
4. [Grille 18 vignettes](#grille-18-vignettes)
5. [Entités utilisées](#entités-utilisées--provenance-complète)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page d'accueil du dashboard. Structure en deux parties :

- **Cartes permanentes** (haut) : météo, présence, alertes conditionnelles
- **Grille 3×6** (bas) : 18 vignettes de navigation vers les sous-pages, chacune affichant un résumé des données en temps réel

### Intégrations requises

- ✅ `meteofrance` (HACS) — détails météo + alertes
- ✅ `meteocss` (HACS) — carte météo animée (picture-elements)
- ✅ `blitzortung` (HACS) — détection foudre
- ✅ `mobile_app` — trackers téléphones
- ✅ `person` (natif HA) — présence globale
- ✅ `ecojoko` (HACS) — consommation électrique temps réel
- ✅ `smartir` — entités `climate.*` (clims)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:html-template-card` | Météo animée — 7 layers picture-elements (meteocss) |
| `meteofrance-weather-card` | Détails météo (prévisions, alertes, UV, pluie…) |
| `custom:button-card` | Toutes les 18 vignettes + foudre + VS Code |
| `custom:bubble-card` | Séparateur présence + boutons Eric/Mamour |
| `custom:mushroom-entity-card` | Lave-linge · Lave-vaisselle · Détecteur fuite |
| `custom:flex-horseshoe-card` | Jauge MariaDB (L5C3) |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────┐
│  picture-elements / meteocss  (7 layers animés)                 │
├─────────────────────────────────────────────────────────────────┤
│  meteofrance-weather-card  (weather.vence — prévisions/alertes) │
├─────────────────────────────────────────────────────────────────┤
│  [CONDITIONNEL] button-card VS Code Server  (CPU > 1%)          │
├─────────────────────────────────────────────────────────────────┤
│  [CONDITIONNEL] button-card Foudre  (lightning_counter > 1)     │
├────────────────────────────┬────────────────────────────────────┤
│  [COND.] mushroom Lave-lin │ [COND.] mushroom Lave-vaisselle    │
│  (prise_lave_linge > 50W)  │ (prise_lave_vaisselle > 50W)       │
├─────────────────────────────────────────────────────────────────┤
│  bubble-card separator  "Personne(s)"  (sensor.etat_wifi_maison)│
│  bubble-card button  Eric  /  bubble-card button  Mamour        │
├─────────────────────────────────────────────────────────────────┤
│  [CONDITIONNEL] mushroom-entity-card  Détecteur fuite           │
├──────────────────────┬───────────────────┬──────────────────────┤
│  L1C1  Météo         │ L1C2  Températures│ L1C3  Clim           │
├──────────────────────┼───────────────────┼──────────────────────┤
│  L2C1  Énergie       │ L2C2  Clim kWh    │ L2C3  Éclairage kWh  │
├──────────────────────┼───────────────────┼──────────────────────┤
│  L3C1  Lumières      │ L3C2  Prises      │ L3C3  Stores         │
├──────────────────────┼───────────────────┼──────────────────────┤
│  L4C1  FreeBox       │ L4C2  Mini PC     │ L4C3  MAJ HA         │
├──────────────────────┼───────────────────┼──────────────────────┤
│  L5C1  Batteries     │ L5C2  Portables   │ L5C3  MariaDB        │
├──────────────────────┼───────────────────┼──────────────────────┤
│  L6C1  Air Quality   │ L6C2  Pollen/Poll.│ L6C3  Vigieau        │
└──────────────────────┴───────────────────┴──────────────────────┘
```

---

## 📍 CARTES PERMANENTES

### 1 — Météo animée meteocss *(picture-elements)*

**Type :** `type: picture-elements` — 7 layers `custom:html-template-card`
**Toujours visible**
**Fichier YAML :** `Dashboard/PAGE_Home/card_meteocss_home_2026-06-13.yaml`

Carte météo animée générée par le package **meteocss v2.2.1**. Les macros Jinja2 (`meteo.jinja`, `meteo_settings.jinja`, `rotation.jinja`) produisent le rendu du ciel, des nuages, du soleil, de la lune et du foreground. L'ordre des 7 layers dans `elements:` définit le z-index (dernier = devant).

| # | Layer | Entités / Source |
|---|-------|-----------------|
| 1 | Ciel animé (background) | `meteo.jinja → generate_content('background')` |
| 2 | Rose des vents SVG | Statique (perspective rotateX 62°, opacity 0.25) |
| 3 | Soleil + Lune | `sensor.sun_left/top/opacity` · `sensor.moon_left/top/opacity/phase` · `sensor.moon_api (moon_parallactic_angle)` |
| 4 | Foreground (nuages/pluie) | `meteo.jinja → generate_content('foreground')` |
| 5 | Alerte météo (conditionnel) | `sensor.alerte_meteo` (Orange/Rouge) |
| 6 | Statut + T°ext (bas) | `sensor.vence_original_condition` · `sensor.th_balcon_nord_temperature` |
| 7 | Titre VENCE + heure (haut) | `now().strftime('%H:%M')` — font-size 18px |

> ⚠️ **Ordre z-index critique** : la rose des vents doit être en position 2 (après le ciel, avant le soleil). Si inversé, elle masque les textes.

---

### 2 — Météo France détails *(meteofrance-weather-card)*

**Type :** `custom:meteofrance-weather-card`
**Entité principale :** `weather.vence`
**Toujours visible**

Affiche prévisions, alertes vigilance, chances de pluie, UV, couverture nuageuse et gel. Le champ `detailEntity` pointe sur `sensor.temperature_delta_affichage` pour afficher le delta de température personnalisé.

| Entité | Rôle |
|--------|------|
| `weather.vence` | Météo principale (Météo France) |
| `sensor.vence_rain_chance` | Probabilité de pluie |
| `sensor.vence_uv` | Indice UV |
| `sensor.vence_cloud_cover` | Couverture nuageuse |
| `sensor.vence_freeze_chance` | Risque de gel |
| `sensor.vence_snow_chance` | Risque de neige |
| `sensor.06_weather_alert` | Alertes vigilance Alpes-Maritimes |
| `sensor.temperature_delta_affichage` | Delta T° personnalisé (detailEntity) |
| `sensor.vence_next_rain` | Prévision prochaine pluie |

---

### 3 — VS Code Server *(conditionnel)*

**Type :** `custom:button-card` dans `vertical-stack` + `conditional`
**Visible si :** `sensor.studio_code_server_pourcentage_du_processeur` > 1

Affiche la charge CPU du serveur VS Code. Fond rouge + animation clignotante si CPU > 20%. Tap = restart de l'add-on via `hassio.addon_restart`.
**Fichier YAML :** `Dashboard/PAGE_Home/card_vscode_home_2026-06-13.yaml`

| Entité | Rôle |
|--------|------|
| `sensor.studio_code_server_pourcentage_du_processeur` | Condition (> 1%) + valeur affichée |

---

### 4 — Foudre Blitzortung *(conditionnel)*

**Type :** `custom:button-card`
**Visible si :** `sensor.maison_lightning_counter` > 1
**Fichier YAML :** `Dashboard/PAGE_Home/card_foudre_home_2026-06-13.yaml`

Affiche la distance, la localisation (géocodage) ou l'azimut du dernier impact, le temps écoulé et le compteur total. Bordure et fond colorés selon la distance :

| Distance | Couleur bordure | Fond |
|----------|-----------------|------|
| 0–5 km | rouge | `rgba(255,0,0,0.2)` + clignotant |
| > 5 km | orange | `rgba(255,123,0,0.1)` |
| Aucun | vert | `rgba(0,255,0,0.05)` |

Tap → `/meteo/#foudre`

| Entité | Rôle |
|--------|------|
| `sensor.maison_lightning_counter` | Compteur impacts (condition + affichage) |
| `sensor.dernier_impact_temps_reel` | Temps depuis dernier impact |
| `sensor.maison_lightning_distance` | Distance dernier impact (km) |
| `sensor.maison_lightning_localisation` | Géocodage ville (attr.features[0].properties.geocoding.city) |
| `sensor.maison_lightning_azimuth` | Direction (azimut degrés — fallback si pas de ville) |

---

### 5 — Lave-linge *(conditionnel)*

**Type :** `custom:mushroom-entity-card`
**Visible si :** `sensor.prise_lave_linge_nous_power` > 50 W
**Animation :** `washer-chaos` (rotation irrégulière 1.1s) si puissance > 1 W
**grid_options :** columns: 6, rows: 2 (demi-largeur, à gauche)
**Fichier YAML :** `Dashboard/PAGE_Home/card_lave_linge_home_2026-06-13.yaml`

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.prise_lave_linge_nous_power` | Puissance instantanée (W) — condition + animation | NOUS SP via Z2M (P2) |

---

### 6 — Lave-vaisselle *(conditionnel)*

**Type :** `custom:mushroom-entity-card`
**Visible si :** `sensor.prise_lave_vaisselle_nous_power` > 50 W
**Animation :** `dishwasher-swash` (oscillation scale+rotate 1.5s) si puissance > 5 W
**grid_options :** columns: 6, rows: 2 (demi-largeur, à droite)
**Fichier YAML :** `Dashboard/PAGE_Home/card_lave_vaisselle_home_2026-06-13.yaml`

| Entité | Rôle | Source |
|--------|------|--------|
| `sensor.prise_lave_vaisselle_nous_power` | Puissance instantanée (W) — condition + animation | NOUS SP via Z2M (P2) |

---

### 7 — Présence Personne(s)

Groupe de 3 cartes. Voir doc dédiée : [`VIGNETTE_WIFI_PRESENCE.md`](./VIGNETTE_WIFI_PRESENCE.md)
**Fichier YAML :** `Dashboard/PAGE_Home/card_presence_home_2026-06-13.yaml`

**Séparateur** — couleur selon `sensor.etat_wifi_maison` :

| État | Couleur | Signification |
|------|---------|---------------|
| `'2'` | `darkgreen` | Eric + Mamour présents |
| `'Eric'` | `darkorange` | Eric seul |
| `'Mamour'` | `darkorange` | Mamour seule |
| autre | `grey` | Personne |

**Carte Eric** — `device_tracker.poco` + photo `person.eric`

Couleurs de fond selon état :

| État | Couleur |
|------|---------|
| `home` | vert |
| `not_home` | orange `rgb(255,103,0)` |
| `Boulot` | `rgb(0,87,81)` |
| autre | gris |

**Carte Mamour** — `device_tracker.mamour` + photo `person.mamour`

Zones supplémentaires reconnues : `LECLERC VENCE` (bleu `rgb(0,102,204)`), `Primark` (bleu clair `rgb(4,155,216)`).

---

### 8 — Détecteur de fuite *(conditionnel)*

**Type :** `custom:mushroom-entity-card`
**Visible si :** `binary_sensor.detecteur_de_fuite_ikea_water_leak` = `on`, `unavailable` ou `unknown`
**Fichier YAML :** `Dashboard/PAGE_Home/card_detecteur_fuite_home_2026-06-13.yaml`

Alerte visuelle pleine largeur (12 colonnes). Aucune action tap/hold/double_tap.

---

## 📍 GRILLE 18 VIGNETTES

Toutes les vignettes sont des `custom:button-card` (aspect-ratio 1/1, fond transparent, bordure double blanche) et naviguent vers leur sous-page respective.

| Position | Titre affiché | Navigation | Données clés |
|----------|--------------|------------|--------------|
| **L1C1** | Météo | `/meteo` | Icône météo (nav uniquement) |
| **L1C2** | Courbes Température | `/temperatures` | T° + humidité 7 pièces (couleurs par seuil) |
| **L1C3** | Commande Clim. | `/clim` | T̄ appart, Δ ADEME, mode + consigne 5 appareils |
| **L2C1** | Conso. Appart. | `/energie` | Mini/Realtime/Maxi (W) + coûts HP/HC (€) |
| **L2C2** | Consommation CLIM | `/energie-clim` | kWh quotidien + mensuel par appareil (6 + TOTAL) |
| **L2C3** | Éclairage | `/energie-lampes` | État allumé/éteint par pièce + kWh |
| **L3C1** | Lumières | `/lumieres` | Commandes lampes (nav uniquement) |
| **L3C2** | Prises | `/prises` | Commandes prises (nav uniquement) |
| **L3C3** | Stores | `/stores` | État volets + fenêtres |
| **L4C1** | Proxmox (PVE) | `/dashboard-tablette/proxmox` | État CPU/RAM/Disque Proxmox |
| **L4C2** | Mini - P.C. | `/systeme-mini-pc` | T° CPU, CPU%, RAM%, Disque%, Power (W) |
| **L4C3** | Software \| modules | `/maj` | Nb mises à jour disponibles (`sensor.available_updates`) |
| **L5C1** | Batteries | `/battery-bp` | Comptage piles faibles par marque (Hue/IKEA/Sonoff) |
| **L5C2** | État Batterie Portables | `/phone` | % batterie 7 appareils (POCO_E, POCO_G, 1+10P_E, 1+10P_G, GM1901, SM-A53, Tablette) |
| **L5C3** | MARIADB | `/reserve` | Jauge horseshoe `sensor.taille_db_home_assistant` |
| **L6C1** | Air Quality | `/air-quality` | Qualité air intérieur (PM2.5 / tVOC) |
| **L6C2** | Pollen / Pollution | `/pollen-pollution` | AtmoFrance + pollen extérieur |
| **L6C3** | Vigieau | `/vigieau` | Restrictions eau en vigueur |

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

---

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| `weather.vence` | `meteofrance` (HACS) | Intégrations → Météo France |
| `sensor.vence_rain_chance` | `meteofrance` | idem |
| `sensor.vence_uv` / `vence_cloud_cover` | `meteofrance` | idem |
| `sensor.vence_freeze_chance` / `vence_snow_chance` | `meteofrance` | idem |
| `sensor.06_weather_alert` / `vence_next_rain` | `meteofrance` | idem |
| `sensor.moon_api` (attr: `moon_parallactic_angle`) | `moon` (HACS) | Intégrations → Moon |
| `climate.clim_*_rm4_mini` | `smartir` | configuration.yaml |
| `climate.radiateur_cuisine` | `smartir` | configuration.yaml |
| `climate.soufflant_salle_de_bain` | `smartir` | configuration.yaml |
| `device_tracker.poco` | `mobile_app` | App Companion (Eric) |
| `device_tracker.mamour` | `mobile_app` | App Companion (Mamour) |
| `person.eric` / `person.mamour` | `person` | Paramètres > Personnes |
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | Zigbee IKEA Vallhorn | Z2M |
| `sensor.prise_lave_linge_nous_power` | NOUS SP via Z2M | Z2M (P2 cuisine) |
| `sensor.prise_lave_vaisselle_nous_power` | NOUS SP via Z2M | Z2M (P2 cuisine) |
| `sensor.studio_code_server_pourcentage_du_processeur` | Studio Code Server (add-on) | HA Supervisor |
| `sensor.taille_db_home_assistant` | `sql` | sql.yaml |
| `sensor.ecojoko_*` | `ecojoko` (HACS) | Intégrations → Ecojoko |

---

### 📁 `packages/meteocss.yaml` + macros Jinja2 (meteocss v2.2.1)
> Carte météo animée — picture-elements HOME page.

| Entité | unique_id | Source | Rôle |
|--------|-----------|--------|------|
| `sensor.sun_left` | `sun_left` | `rotation.jinja` | Position X soleil (%) |
| `sensor.sun_top` | `sun_top` | `rotation.jinja` | Position Y soleil (%) |
| `sensor.sun_opacity` | `sun_opacity` | `rotation.jinja` | Opacité soleil |
| `sensor.moon_left` | `moon_left` | `rotation.jinja` | Position X lune (%) |
| `sensor.moon_top` | `moon_top` | `rotation.jinja` | Position Y lune (%) |
| `sensor.moon_opacity` | `moon_opacity` | `rotation.jinja` | Opacité lune |
| `sensor.moon_phase` | `moon_phase` | `rotation.jinja` | Phase (nom image) |
| `sensor.vence_original_condition` | — | `command_line/meteo/carte_meteo_france.yaml` | Condition texte (ex: "Ensoleillé") |
| `sensor.alerte_meteo` | `alerte_meteo` | `templates/meteo/M_01_meteo_alertes_card.yaml` | Niveau alerte (Vert/Orange/Rouge) |
| `sensor.th_balcon_nord_temperature` | — | SONOFF via Z2M | T° extérieure affichée (bas carte) |

> ⚠️ **Macros non-modifiables via UI** : `meteo.jinja`, `meteo_settings.jinja`, `rotation.jinja` → édition via Studio Code Server dans `/config/custom_templates/`.

---

### 📁 `templates/P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml`
> Capteurs WiFi et état agrégé présence maison.

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.condition_eric_wifi` | `condition_eric_wifi` | `true` si Eric sur Freebox_GG |
| `sensor.condition_mamour_wifi` | `condition_mamour_wifi` | `true` si Mamour sur Freebox_GG |
| `sensor.etat_wifi_maison` | `etat_wifi_maison` | Agrégat : `2` / `Eric` / `Mamour` / `0` |

---

### 📁 `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml`
> États logiques des appareils de chauffage/clim pour affichage dashboard.

| Entité | Rôle |
|--------|------|
| `sensor.clim_salon_etat` | Mode clim salon (cool/heat/fan/off) |
| `sensor.radiateur_cuisine_etat` | État radiateur cuisine |
| `sensor.clim_bureau_etat` | Mode clim bureau |
| `sensor.sdb_soufflant_etat` | État soufflant SDB |
| `sensor.sdb_seche_serviette_etat` | État sèche-serviette SDB |
| `sensor.clim_chambre_etat` | Mode clim chambre |
| `sensor.salon_power_status` | Puissance salon (on/off) |
| `sensor.cuisine_power_status` | Puissance cuisine (on/off) |
| `sensor.bureau_power_status` | Puissance bureau (on/off) |
| `sensor.sdb_soufflant_power_status` | Puissance soufflant (on/off) |
| `sensor.chambre_power_status` | Puissance chambre (on/off) |
| `sensor.temperature_moyenne_interieure` | T° moyenne appartement |
| `sensor.delta_ademe_recommande` | Écart T° vs recommandation ADEME |
| `sensor.mode_ete_hiver_etat` | Mode saison actuel |

---

### 📁 `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml`
> Compteurs kWh quotidiens et mensuels par appareil (Pôle 1).

| Entité | Rôle |
|--------|------|
| `sensor.clim_salon_quotidien_kwh_um` / `_mensuel_kwh_um` | Conso clim salon |
| `sensor.radiateur_elec_cuisine_quotidien_kwh_um` / `_mensuel_kwh_um` | Conso radiateur cuisine |
| `sensor.clim_bureau_quotidien_kwh_um` / `_mensuel_kwh_um` | Conso clim bureau |
| `sensor.soufflant_sdb_quotidien_kwh_um` / `_mensuel_kwh_um` | Conso soufflant SDB |
| `sensor.seche_serviette_sdb_quotidien_kwh_um` / `_mensuel_kwh_um` | Conso sèche-serviette |
| `sensor.clim_chambre_quotidien_kwh_um` / `_mensuel_kwh_um` | Conso clim chambre |
| `sensor.conso_clim_rad_total_quotidien` / `_mensuel` | Totaux Pôle 1 |

---

### 📁 `templates/P3_eclairage/ui_dashboard/etats_status.yaml`
> États agrégés d'éclairage par pièce pour la vignette L2C3/L3C1.

| Entité | Rôle |
|--------|------|
| `sensor.lumiere_appartement_etat` | État global appartement |
| `sensor.lumiere_salon_etat` | État éclairage salon |
| `sensor.lumiere_cuisine_etat` | État éclairage cuisine |
| `sensor.lumiere_bureau_etat` | État éclairage bureau |
| `sensor.lumiere_salle_de_bain_etat` | État éclairage SDB |
| `sensor.lumiere_chambre_etat` | État éclairage chambre |

---

### 📁 `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml`
> Mini et maxi de consommation sur fenêtre glissante 24h.

| Entité | Rôle |
|--------|------|
| `sensor.genelec_appart_conso_mini_24h` | Consommation minimale 24h (W) |
| `sensor.genelec_appart_conso_maxi_24h` | Consommation maximale 24h (W) |

---

### 📁 `templates/utilitaires/Mise_a_jour_home_assistant.yaml`
> Compteur de mises à jour disponibles (domaine update.*).

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.available_updates` | `available_updates` | Nb MAJ en attente (vignette L4C3) |

---

## 🐛 DÉPANNAGE

### Une vignette affiche "unavailable"

1. Identifier l'entité principale dans Outils de développement → États
2. Vérifier le fichier YAML source correspondant (voir tableau ENTITÉS ci-dessus)
3. Recharger la configuration : Paramètres → Système → Recharger

### Le séparateur Présence reste gris

→ Voir [`VIGNETTE_WIFI_PRESENCE.md`](./VIGNETTE_WIFI_PRESENCE.md) section Dépannage

### L4C3 affiche 0 alors que des MAJ existent

1. Vérifier `sensor.available_updates` dans les États
2. Si absent : copier `templates/utilitaires/Mise_a_jour_home_assistant.yaml` dans `/config/templates/utilitaires/` et recharger les templates
3. Vérifier que les entités `update.*` sont bien présentes dans HA

### La carte Foudre ne disparaît pas alors qu'il n'y a pas d'orage

1. Vérifier `sensor.maison_lightning_counter` — doit être ≤ 1 pour masquer la carte
2. La carte utilise `visibility: condition: numeric_state above: 1` — elle s'affiche dès que counter > 1

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `meteofrance-weather-card` | HACS | ✅ Essentiel |
| `custom:button-card` | HACS | ✅ Essentiel |
| `custom:bubble-card` | HACS | ✅ Essentiel |
| `custom:mushroom-entity-card` | HACS | ✅ Essentiel |
| `custom:flex-horseshoe-card` | HACS | ✅ Essentiel (L5C3) |
| `ecojoko` intégration | HACS | ✅ Essentiel (L2C1) |
| `blitzortung` intégration | HACS | ✅ Essentiel (carte foudre) |
| `sensor.available_updates` | Template YAML | ✅ Essentiel (L4C3) |
| `sql.yaml` → MariaDB | Natif HA | ✅ Essentiel (L5C3) |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)

- `packages/cssmeteo.yaml` — configuration meteocss (macros Jinja2)
- `custom_templates/meteo.jinja` — rendu background + foreground
- `custom_templates/rotation.jinja` — positions soleil/lune
- `custom_templates/meteo_settings.jinja` — paramètres visuels (nuages, couleurs)
- `templates/meteo/M_01_meteo_alertes_card.yaml` — sensor.alerte_meteo
- `command_line/meteo/carte_meteo_france.yaml` — sensor.vence_original_condition
- `templates/P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml`
- `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml`
- `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml`
- `templates/P1_clim_chauffage/P1_AVG/P1_AVG.yaml`
- `templates/P3_eclairage/ui_dashboard/etats_status.yaml`
- `templates/utilitaires/Mise_a_jour_home_assistant.yaml`
- `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml`
- `sql.yaml`

### Dashboard YAML (cartes individuelles HOME)

| Fichier | Carte |
|:--------|:------|
| `Dashboard/PAGE_Home/page_home_2026-06-13.yaml` | Page complète (référence) |
| `Dashboard/PAGE_Home/card_meteocss_home_2026-06-13.yaml` | Météo animée (picture-elements 7 layers) |
| `Dashboard/PAGE_Home/card_vscode_home_2026-06-13.yaml` | VS Code Server (conditional) |
| `Dashboard/PAGE_Home/card_foudre_home_2026-06-13.yaml` | Foudre Blitzortung (button-card) |
| `Dashboard/PAGE_Home/card_lave_linge_home_2026-06-13.yaml` | Lave-linge (mushroom animée) |
| `Dashboard/PAGE_Home/card_lave_vaisselle_home_2026-06-13.yaml` | Lave-vaisselle (mushroom animée) |
| `Dashboard/PAGE_Home/card_presence_home_2026-06-13.yaml` | Présence (separator + Eric + Mamour) |
| `Dashboard/PAGE_Home/card_detecteur_fuite_home_2026-06-13.yaml` | Détecteur de fuite (mushroom) |

### Documentation liée

- [`VIGNETTE_WIFI_PRESENCE.md`](./VIGNETTE_WIFI_PRESENCE.md) — détail cartes présence

---

← Retour : `docs/` | → Détail présence : `VIGNETTE_WIFI_PRESENCE.md`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[VIGNETTE_WIFI_PRESENCE]]*
