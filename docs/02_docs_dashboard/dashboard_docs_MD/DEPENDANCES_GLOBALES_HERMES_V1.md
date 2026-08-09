# DEPENDANCES GLOBALES HERMES - TABLEAU DE BORD HA
*Version Hermes - architecture par CARTE : vignettes dashboard (L0C0-L6C3) + scripts sh + automations par pole + scripts + complement + orphelines. Types auto-detectes, annotations Claude conservees. Genere automatiquement.*

## LEGENDE

| Symbole | Signification |
|:-------:|:-------------|
| [type] | Type de carte |
| (TPL) | Entite definie dans un template (templates/) |
| (SEN) | Entite definie dans sensors/ |
| (UM) | Entite definie dans utility_meter/ |
| (NAT) | Entite native/UI ou autre fichier |
| ORPHELINE | Entite dans aucun dashboard, automation ni script |

## MATRICE DES VIGNETTES

| ID | Vignette | Entites | Cartes |
|:---|:---------|:-------:|:------:|
| **L0C0** | PAGE_Home | 20 | 13 |
| **L1C1** | Meteo | 46 | 120 |
| **L1C2** | Temperatures | 50 | 93 |
| **L1C3** | Commandes_Clim | 87 | 207 |
| **L2C1** | Energie_Generale | 181 | 153 |
| **L2C2** | Energie_Clim | 104 | 180 |
| **L2C3** | Energie_Eclairage | 85 | 79 |
| **L3C1** | Commandes_Eclairage | 44 | 85 |
| **L3C2** | Commandes_Prises | 24 | 22 |
| **L3C3** | Stores_Fenetres | 17 | 53 |
| **L4C1** | Proxmox | 63 | 100 |
| **L4C2** | Mini_PC | 28 | 99 |
| **L4C3** | MAJ_HA | 10 | 110 |
| **L5C1** | Batteries_Piles | 37 | 11 |
| **L5C2** | Batteries_Portables | 49 | 35 |
| **L5C3** | MariaDB | 25 | 73 |
| **L6C1** | Air_Qualite | 15 | 30 |
| **L6C2** | Pollution_Pollen | 19 | 32 |
| **L6C3** | VigiEau | 2 | 16 |

## SOMMAIRE

- Vignettes dashboard : 19 sections (L0C0 a L6C3), cartes detaillees
- Scripts .sh : 8
- Automations : 44 (par pole)
- Scripts non-sh : 2
- Complement : fichiers racine et repertoires hors dashboard
- Entites orphelines : 281

## 1. VIGNETTES DASHBOARD (L0C0 -> L6C3) - PAR CARTE

### L0C0 - PAGE_Home

*Validée le 2026-06-13*

> Les 18 vignettes de la grille sont documentées dans leurs sections respectives (L1C1–L6C3). Cette section couvre **uniquement les cartes permanentes en haut de la HOME page** qui n'appartiennent à aucune vignette. Ces fichiers font partie intégrante de la config HA et sont audités par `audit_md5.sh`. Ils n'alimentent pas directement d'entités dashboard - référencés ici pour inventaire complet. *Ajouté le 2026-06-15* Configurée via : Paramètres → Appareils & Services → Ajouter → File Génère des services `notify.file_*` utilisés par les automations. ✅ **Note 2026-08-08** : ligne ci-dessus confirmée par Eric (2026-08-08). La phrase tronquée (coupure sur "docs_da") a été complétée par hypothèse le 2026-07-19 ; hypothèse validée - `docs_dashboard/` est bien l'ancien répertoire supprimé le 2026-07-14 tel que documenté dans CLAUDE.md.

*20 entites, 13 cartes, 7 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 17)
  └─→ TPL: M_01_meteo_alertes_card.yaml (1)
  └─→ TPL: M_03_meteo_blitzortung.yaml (1)
  └─→ TPL: P4_wifi_detection.yaml (1)
        └─→ VIGNETTE L0C0
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | NAT | (native/UI) |
| `device_tracker.mamour` | NAT | idem |
| `device_tracker.poco` | NAT | idem |
| `person.eric` | NAT | idem |
| `person.mamour` | NAT | idem |
| `sensor.maison_lightning_azimuth` | NAT | idem |
| `sensor.maison_lightning_counter` | NAT | idem |
| `sensor.maison_lightning_distance` | NAT | idem |
| `sensor.maison_lightning_localisation` | NAT | idem |
| `sensor.prise_lave_linge_nous_power` | NAT | idem |
| `sensor.prise_lave_vaisselle_nous_power` | NAT | idem |
| `sensor.studio_code_server_pourcentage_du_processeur` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.vence_original_condition` | NAT | idem |
| `sun.sun` | NAT | idem |
| `switch.plug_6_local` | NAT | idem |
| `weather.vence` | NAT | idem |
| `sensor.alerte_meteo` | TPL | M_01_meteo_alertes_card.yaml |
| `sensor.dernier_impact_temps_reel` | TPL | M_03_meteo_blitzortung.yaml |
| `sensor.etat_wifi_maison` | TPL | P4_wifi_detection.yaml |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_detecteur_fuite_home_2026-06-13.yaml` | ✅ |
| `card_foudre_home_2026-06-13.yaml` | ✅ |
| `card_lave_linge_home_2026-06-13.yaml` | ✅ |
| `card_lave_vaisselle_home_2026-06-13.yaml` | ✅ |
| `card_meteocss_home_2026-06-28.yaml` | ✅ |
| `card_presence_home_2026-06-13.yaml` | ✅ |
| `card_vscode_home_2026-06-13.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_detecteur_fuite_home_2026-06-13.yaml (1 cartes, 1 entites)

- [custom:mushroom-entity-card] Détecteur de fuite sous évier cuisine: binary_sensor.detecteur_de_fuite_ikea_water_leak (NAT)

#### card_foudre_home_2026-06-13.yaml (1 cartes, 5 entites)

- [custom:button-card] [[[
  const distRaw = states['sensor.maison_lightning_distan: sensor.dernier_impact_temps_reel (TPL), sensor.maison_lightning_azimuth (NAT), sensor.maison_lightning_counter (NAT), sensor.maison_lightning_distance (NAT), sensor.maison_lightning_localisation (NAT)

#### card_lave_linge_home_2026-06-13.yaml (1 cartes, 2 entites)

- [custom:mushroom-entity-card] Lave-linge: sensor.prise_lave_linge_nous_power (NAT), switch.plug_6_local (NAT)

#### card_lave_vaisselle_home_2026-06-13.yaml (1 cartes, 2 entites)

- [custom:mushroom-entity-card] Lave-vaisselle: sensor.prise_lave_vaisselle_nous_power (NAT), switch.plug_6_local (NAT)

#### card_meteocss_home_2026-06-28.yaml (6 cartes, 5 entites)

- [picture-elements]  (aucune entite)
---
- [custom:meteo-card] : sun.sun (NAT), weather.vence (NAT)
---
- [custom:html-template-card]  (aucune entite)
---
- [custom:html-template-card] : sensor.alerte_meteo (TPL)
---
- [custom:html-template-card] : sensor.th_balcon_nord_temperature (NAT), sensor.vence_original_condition (NAT)
---
- [custom:html-template-card]  (aucune entite)

#### card_presence_home_2026-06-13.yaml (1 cartes, 5 entites)

- [(parse erreur)] : device_tracker.mamour (NAT), device_tracker.poco (NAT), person.eric (NAT), person.mamour (NAT), sensor.etat_wifi_maison (TPL)

#### card_vscode_home_2026-06-13.yaml (2 cartes, 1 entites)

- [conditional] : sensor.studio_code_server_pourcentage_du_processeur (NAT)
---
- [custom:button-card] Visual Server Code: sensor.studio_code_server_pourcentage_du_processeur (NAT)

### L1C1 - Meteo

*Validée le 2026-05-09*

> La vignette `custom:button-card` est statique : icône `mdi:weather-partly-cloudy`, nom "Météo". Aucun `triggers_update`, aucun `custom_fields`, aucune entité référencée.
> ⚠️ Corrigé le 2026-07-19 : cette section décrivait des noms d'entités obsolètes/inexistants (`binary_sensor.meteo_france_alerte_*`, `sensor.meteo_france_wind_speed/_bearing`, `camera.carte_vigilance_meteo_france`, les 4 `*_card_content` génériques). Noms réels vérifiés directement dans le corps des fichiers yaml le 2026-07-19. `M_05_cycle_solaire.yaml` (absent de cette doc jusqu'ici) ajouté - c'est lui qui calcule la durée du jour, pas `sun.sun`. `templates/meteo/M_04_tendances_th_ext_card.yaml` retiré de cette liste le 2026-07-19 - son entête déclare lui-même `AVAL : L1C2 Températures`, pas L1C1. Voir section L1C2.

*46 entites, 120 cartes, 3 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 29)
  └─→ TPL: M_01_meteo_alertes_card.yaml (10)
  └─→ TPL: M_03_meteo_blitzortung.yaml (4)
  └─→ TPL: M_05_cycle_solaire.yaml (3)
        └─→ VIGNETTE L1C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.06_weather_alert` | NAT | (native/UI) |
| `sensor.direction_du_vent_vence` | NAT | idem |
| `sensor.direction_du_vent_vence_label` | NAT | idem |
| `sensor.duree_du_jour_brut` | NAT | idem |
| `sensor.eclairs_annuel` | NAT | idem |
| `sensor.eclairs_hebdomadaire` | NAT | idem |
| `sensor.eclairs_horaire` | NAT | idem |
| `sensor.eclairs_mensuel` | NAT | idem |
| `sensor.eclairs_quotidien` | NAT | idem |
| `sensor.maison_lightning_azimuth` | NAT | idem |
| `sensor.maison_lightning_counter` | NAT | idem |
| `sensor.maison_lightning_distance` | NAT | idem |
| `sensor.maison_lightning_localisation` | NAT | idem |
| `sensor.moon_phase` | NAT | idem |
| `sensor.season` | NAT | idem |
| `sensor.sun_next_rising` | NAT | idem |
| `sensor.sun_next_setting` | NAT | idem |
| `sensor.th_balcon_nord_humidity` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.vence_daily_precipitation` | NAT | idem |
| `sensor.vence_original_condition` | NAT | idem |
| `sensor.vence_pressure` | NAT | idem |
| `sensor.vence_uv` | NAT | idem |
| `sensor.vence_wind_gust` | NAT | idem |
| `sensor.vence_wind_speed` | NAT | idem |
| `sensor.vitesse_du_vent_vence` | NAT | idem |
| `sun.sun` | NAT | idem |
| `weather.vence` | NAT | idem |
| `zone.home` | NAT | idem |
| `sensor.alerte_avalanches` | TPL | M_01_meteo_alertes_card.yaml |
| `sensor.alerte_canicule` | TPL | idem |
| `sensor.alerte_grand_froid` | TPL | idem |
| `sensor.alerte_inondation` | TPL | idem |
| `sensor.alerte_meteo` | TPL | idem |
| `sensor.alerte_neige_verglas` | TPL | idem |
| `sensor.alerte_orages` | TPL | idem |
| `sensor.alerte_pluie_inondation` | TPL | idem |
| `sensor.alerte_vagues_submersion` | TPL | idem |
| `sensor.alerte_vent_violent` | TPL | idem |
| `sensor.dernier_impact_temps_reel` | TPL | M_03_meteo_blitzortung.yaml |
| `sensor.lightning_bearing` | TPL | idem |
| `sensor.lightning_direction_label` | TPL | idem |
| `sensor.lightning_distance_km` | TPL | idem |
| `sensor.duree_du_jour` | TPL | M_05_cycle_solaire.yaml |
| `sensor.tendance_duree_jour` | TPL | idem |
| `sensor.variation_quotidienne` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_duree_du_jour_2026-05-23.yaml` | ✅ |
| `page_L1C1_meteo_2026-06-13.yaml` | ✅ |
| `vignette_L1C1_meteo_2026-05-16.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_duree_du_jour_2026-05-23.yaml (5 cartes, 5 entites)

- [custom:apexcharts-card] : sensor.duree_du_jour (TPL)
---
- [area]  (aucune entite)
---
- [area] Durée du jour: sensor.duree_du_jour_brut (NAT)
---
- [area] : sun.sun (NAT), zone.home (NAT)
---
- [area] Gain/Perte: sensor.variation_quotidienne (TPL)

#### page_L1C1_meteo_2026-06-13.yaml (114 cartes, 45 entites)

- [grid]  (aucune entite)
---
- [heading] METEO: sensor.th_balcon_nord_temperature (NAT)
---
- [entity] : sensor.th_balcon_nord_temperature (NAT)
---
- [custom:bubble-card] Appartement (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [markdown] : sensor.th_balcon_nord_temperature (NAT)
---
- [markdown] : sensor.th_balcon_nord_humidity (NAT)
---
- [custom:bubble-card] Prévision Météo France & Carte Windy (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [weather-forecast] : weather.vence (NAT)
---
- [custom:swipe-card]  (aucune entite)
---
- [progressbar]  (aucune entite)
---
- [iframe]  (aucune entite)
---
- [iframe]  (aucune entite)
---
- [iframe]  (aucune entite)
---
- [iframe]  (aucune entite)
---
- [weather-forecast] : weather.vence (NAT)
---
- [heading] Vitesse du Vent - Baromètre - U.V. - Pluie (aucune entite)
---
- [custom:bubble-card] Vent (aucune entite)
---
- [custom:windrose-card] Direction et Vitesse du Vent avec Rafales: sensor.direction_du_vent_vence (NAT), sensor.direction_du_vent_vence_label (NAT), sensor.vence_wind_gust (NAT), sensor.vence_wind_speed (NAT), sensor.vitesse_du_vent_vence (NAT), weather.vence (NAT)
---
- [period_selector]  (aucune entite)
---
- [period_selector]  (aucune entite)
---
- [period_selector]  (aucune entite)
---
- [period_selector]  (aucune entite)
---
- [custom:bubble-card] Baromètre (aucune entite)
---
- [custom:ha-tbaro-card] : sensor.vence_pressure (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bubble-card] UV (aucune entite)
---
- [custom:bubble-card] Pluie (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:uv-index-card] : sensor.vence_uv (NAT)
---
- [custom:rain-gauge-card] : sensor.vence_daily_precipitation (NAT)
---
- [custom:bubble-card] Pluie ces dernières 24 heures (Météo France) (aucune entite)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] : sensor.vence_daily_precipitation (NAT)
---
- [custom:bubble-card]  (aucune entite)
---
- [custom:bubble-card] Impacts de foudre (30 Km) (aucune entite)
---
- [custom:button-card] [[[
  const distRaw = states['sensor.maison_lightning_distan: sensor.dernier_impact_temps_reel (TPL), sensor.maison_lightning_azimuth (NAT), sensor.maison_lightning_counter (NAT), sensor.maison_lightning_distance (NAT), sensor.maison_lightning_localisation (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.eclairs_horaire (NAT)
---
- [custom:bar-card] : sensor.eclairs_quotidien (NAT)
---
- [custom:bar-card] : sensor.eclairs_hebdomadaire (NAT)
---
- [custom:bar-card] : sensor.eclairs_mensuel (NAT)
---
- [custom:bar-card] : sensor.eclairs_annuel (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:windrose-card] : sensor.eclairs_quotidien (NAT), sensor.lightning_bearing (TPL), sensor.lightning_direction_label (TPL), sensor.lightning_distance_km (TPL)
---
- [period_selector]  (aucune entite)
---
- [period_selector]  (aucune entite)
---
- [period_selector]  (aucune entite)
---
- [period_selector]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Nb éclairs ce jour: sensor.eclairs_quotidien (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Nb éclairs ce mois: sensor.eclairs_mensuel (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:swipe-card]  (aucune entite)
---
- [progressbar]  (aucune entite)
---
- [iframe]  (aucune entite)
---
- [iframe]  (aucune entite)
---
- [custom:bubble-card] Carte d'alerte(s) Météo France (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] Alerte météo <br/>Aujourd'hui (aucune entite)
---
- [custom:button-card] Alerte météo <br/>Demain (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.alerte_meteo (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_orages (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_pluie_inondation (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_vent_violent (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_avalanches (TPL)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.alerte_canicule (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_inondation (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_neige_verglas (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_grand_froid (TPL)
---
- [custom:mushroom-template-card] : sensor.alerte_vagues_submersion (TPL)
---
- [custom:meteoalarm-card] : sensor.06_weather_alert (NAT)
---
- [custom:bubble-card] Lever et coucher du Soleil (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:horizon-card]  (aucune entite)
---
- [custom:tsmoon-card] : sensor.moon_phase (NAT)
---
- [custom:entity-progress-card] {% set sunrise = as_datetime(states('sensor.sun_next_rising': sensor.sun_next_rising (NAT), sensor.sun_next_setting (NAT), sun.sun (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [glance] : sensor.duree_du_jour (TPL), sensor.season (NAT), sensor.tendance_duree_jour (TPL), sensor.variation_quotidienne (TPL), sun.sun (NAT)
---
- [custom:apexcharts-card] : sensor.duree_du_jour (TPL)
---
- [area]  (aucune entite)
---
- [area] Durée du jour: sensor.duree_du_jour_brut (NAT)
---
- [area] : sun.sun (NAT), zone.home (NAT)
---
- [area] Gain/Perte: sensor.variation_quotidienne (TPL)

#### vignette_L1C1_meteo_2026-05-16.yaml (1 cartes, 3 entites)

- [custom:button-card] Météo: sensor.th_balcon_nord_temperature (NAT), sensor.vence_original_condition (NAT), weather.vence (NAT)

### L1C2 - Temperatures

*Validée le 2026-05-13*

> ⚠️ **Corrigé le 2026-07-19** : `temperature_moyenne_interieure`, `temperature_delta_affichage`, `delta_ademe_recommande` étaient attribués à tort à `P1_ui_dashboard/P1_ui_dashboard.yaml` (ce fichier ne produit que des entités power_status/clim_*_etat - vérifié dans son propre corps, AVAL déclaré L1C3/L2C2, pas L1C2). Vrai fichier source : `P1_01_clim_logique_system_autom.yaml` (son AVAL déclare lui-même "L1C2 Températures" pour ces 4 sensors). Les entrées fictives `sensor.th_*_temperature_trend` / `_humidity_trend` (génériques, toutes pièces) ont été retirées - seule la sonde balcon nord a un calcul de tendance réel (`M_04_tendances_th_ext_card.yaml`, absent de cette section jusqu'ici - ajouté). `sensor.*_power_status` / `clim_*_etat` retirés d'ici - ce sont des entités Clim ON/OFF, déjà documentées dans la section L1C3 ci-dessous, pas des données de température.
> ⚠️ **Flag** : `custom:temperature-heatmap-card` utilisé dans le pop-up `#exterieur` - **absent du référentiel HACS officiel**. À vérifier / ajouter si installé.

*50 entites, 93 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 29)
  └─→ TPL: M_04_tendances_th_ext_card.yaml (2)
  └─→ TPL: P1_01_clim_logique_system_autom.yaml (3)
  └─→ TPL: P1_AVG_AMHQ_TOTAL.yaml (1)
  └─→ TPL: P1_TOTAL_AMHQ.yaml (3)
  └─→ TPL: P1_ui_dashboard.yaml (12)
        └─→ VIGNETTE L1C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `climate.clim_bureau_rm4_mini` | NAT | (native/UI) |
| `climate.clim_chambre_rm4_mini` | NAT | idem |
| `climate.clim_du_bureau` | NAT | idem |
| `climate.clim_salon_rm4_mini` | NAT | idem |
| `climate.radiateur_cuisine` | NAT | idem |
| `sensor.th_balcon_nord_battery` | NAT | idem |
| `sensor.th_balcon_nord_humidity` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.th_bureau_battery` | NAT | idem |
| `sensor.th_bureau_humidity` | NAT | idem |
| `sensor.th_bureau_temperature` | NAT | idem |
| `sensor.th_cellier_battery` | NAT | idem |
| `sensor.th_cellier_humidity` | NAT | idem |
| `sensor.th_cellier_temperature` | NAT | idem |
| `sensor.th_chambre_battery` | NAT | idem |
| `sensor.th_chambre_humidity` | NAT | idem |
| `sensor.th_chambre_temperature` | NAT | idem |
| `sensor.th_cuisine_battery` | NAT | idem |
| `sensor.th_cuisine_humidity` | NAT | idem |
| `sensor.th_cuisine_temperature` | NAT | idem |
| `sensor.th_salle_de_bain_battery` | NAT | idem |
| `sensor.th_salle_de_bain_humidity` | NAT | idem |
| `sensor.th_salle_de_bain_temperature` | NAT | idem |
| `sensor.th_salon_battery` | NAT | idem |
| `sensor.th_salon_humidity` | NAT | idem |
| `sensor.th_salon_temperature` | NAT | idem |
| `sensor.vence_temperature` | NAT | idem |
| `switch.radiateur_elec_cuisine` | NAT | idem |
| `weather.vence` | NAT | idem |
| `sensor.th_balcon_nord_humidity_trend` | TPL | M_04_tendances_th_ext_card.yaml |
| `sensor.th_balcon_nord_temperature_trend` | TPL | idem |
| `sensor.temperature_corrige_chambre` | TPL | P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_delta_affichage` | TPL | idem |
| `sensor.temperature_moyenne_interieure` | TPL | idem |
| `sensor.clim_rad_total_avg_watts_quotidien` | TPL | P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.conso_clim_rad_total` | TPL | P1_TOTAL_AMHQ.yaml |
| `sensor.conso_clim_rad_total_mensuel` | TPL | idem |
| `sensor.conso_clim_rad_total_quotidien` | TPL | idem |
| `sensor.bureau_power_status` | TPL | P1_ui_dashboard.yaml |
| `sensor.chambre_power_status` | TPL | idem |
| `sensor.clim_bureau_etat` | TPL | idem |
| `sensor.clim_chambre_etat` | TPL | idem |
| `sensor.clim_salon_etat` | TPL | idem |
| `sensor.cuisine_power_status` | TPL | idem |
| `sensor.radiateur_cuisine_etat` | TPL | idem |
| `sensor.salon_power_status` | TPL | idem |
| `sensor.sdb_seche_serviette_etat` | TPL | idem |
| `sensor.sdb_seche_serviette_power_status` | TPL | idem |
| `sensor.sdb_soufflant_etat` | TPL | idem |
| `sensor.sdb_soufflant_power_status` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L1C2_temperatures_2026-07-14.yaml` | ✅ |
| `vignette_L1C2_temperatures_2026-05-12.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L1C2_temperatures_2026-07-14.yaml (92 cartes, 50 entites)

- [grid]  (aucune entite)
---
- [heading] TEMPERATURE - HUMIDITEES: sensor.th_balcon_nord_battery (NAT)
---
- [entity] : sensor.th_balcon_nord_battery (NAT)
---
- [custom:apexcharts-card] : sensor.th_balcon_nord_temperature (NAT), sensor.vence_temperature (NAT)
---
- [column] Humi.Bal.Nrd: sensor.th_balcon_nord_humidity (NAT)
---
- [heading] Tendances: sensor.temperature_delta_affichage (TPL)
---
- [entity] : sensor.temperature_delta_affichage (TPL)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.th_balcon_nord_temperature (NAT), sensor.th_balcon_nord_temperature_trend (TPL)
---
- [custom:mini-graph-card] : sensor.th_balcon_nord_temperature (NAT)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.th_balcon_nord_humidity (NAT), sensor.th_balcon_nord_humidity_trend (TPL)
---
- [custom:mini-graph-card] : sensor.th_balcon_nord_humidity (NAT)
---
- [heading] Consomation (aucune entite)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [conditional] : sensor.salon_power_status (TPL)
---
- [template] : sensor.clim_salon_etat (TPL)
---
- [conditional] : sensor.cuisine_power_status (TPL)
---
- [template] : sensor.radiateur_cuisine_etat (TPL)
---
- [conditional] : sensor.bureau_power_status (TPL)
---
- [template] : sensor.clim_bureau_etat (TPL)
---
- [conditional] : sensor.sdb_soufflant_power_status (TPL)
---
- [template] : sensor.sdb_soufflant_etat (TPL)
---
- [conditional] : sensor.sdb_seche_serviette_power_status (TPL)
---
- [template] : sensor.sdb_seche_serviette_etat (TPL)
---
- [conditional] : sensor.chambre_power_status (TPL)
---
- [template] : sensor.clim_chambre_etat (TPL)
---
- [custom:apexcharts-card] : sensor.conso_clim_rad_total_mensuel (TPL), sensor.conso_clim_rad_total_quotidien (TPL), sensor.temperature_moyenne_interieure (TPL), sensor.th_balcon_nord_temperature (NAT)
---
- [column] Conso. Instan.: sensor.conso_clim_rad_total (TPL)
---
- [line] Moy.depuis Minuit: sensor.clim_rad_total_avg_watts_quotidien (TPL)
---
- [heading] Récap. Températures (aucune entite)
---
- [custom:apexcharts-card] : sensor.th_bureau_temperature (NAT), sensor.th_cellier_temperature (NAT), sensor.th_chambre_temperature (NAT), sensor.th_cuisine_temperature (NAT), sensor.th_salle_de_bain_temperature (NAT), sensor.th_salon_temperature (NAT)
---
- [heading] Récap. Humiditée (aucune entite)
---
- [custom:apexcharts-card] : sensor.th_bureau_humidity (NAT), sensor.th_cellier_humidity (NAT), sensor.th_chambre_humidity (NAT), sensor.th_cuisine_humidity (NAT), sensor.th_salle_de_bain_humidity (NAT), sensor.th_salon_humidity (NAT)
---
- [heading] SALON: climate.clim_salon_rm4_mini (NAT), sensor.th_salon_battery (NAT), sensor.th_salon_temperature (NAT)
---
- [entity] Réglé à: climate.clim_salon_rm4_mini (NAT)
---
- [entity] Salon: sensor.th_salon_temperature (NAT)
---
- [entity] : sensor.th_salon_battery (NAT)
---
- [custom:bubble-card] : climate.clim_salon_rm4_mini (NAT)
---
- [custom:streamline-card] : sensor.th_salon_humidity (NAT), sensor.th_salon_temperature (NAT)
---
- [heading] CELLIER: sensor.th_cellier_battery (NAT)
---
- [entity] : sensor.th_cellier_battery (NAT)
---
- [custom:streamline-card] : sensor.th_cellier_humidity (NAT), sensor.th_cellier_temperature (NAT)
---
- [heading] CUISINE  (RADIATEUR): sensor.th_cuisine_battery (NAT), sensor.th_cuisine_temperature (NAT), switch.radiateur_elec_cuisine (NAT)
---
- [entity] : switch.radiateur_elec_cuisine (NAT)
---
- [entity] Cuisine: sensor.th_cuisine_temperature (NAT)
---
- [entity] : sensor.th_cuisine_battery (NAT)
---
- [custom:bubble-card] Radiateur de la Cuisine: climate.radiateur_cuisine (NAT)
---
- [custom:streamline-card] : sensor.th_cuisine_humidity (NAT), sensor.th_cuisine_temperature (NAT)
---
- [heading] BUREAU: climate.clim_bureau_rm4_mini (NAT), sensor.th_bureau_battery (NAT), sensor.th_bureau_temperature (NAT)
---
- [entity] Réglé à: climate.clim_bureau_rm4_mini (NAT)
---
- [entity] Bureau: sensor.th_bureau_temperature (NAT)
---
- [entity] : sensor.th_bureau_battery (NAT)
---
- [custom:bubble-card] : climate.clim_bureau_rm4_mini (NAT), climate.clim_du_bureau (NAT)
---
- [custom:streamline-card] : sensor.th_bureau_humidity (NAT), sensor.th_bureau_temperature (NAT)
---
- [heading] SALLE DE BAIN: sensor.th_salle_de_bain_battery (NAT), sensor.th_salle_de_bain_temperature (NAT)
---
- [entity] Salle de Bain: sensor.th_salle_de_bain_temperature (NAT)
---
- [entity] : sensor.th_salle_de_bain_battery (NAT)
---
- [custom:streamline-card] : sensor.th_salle_de_bain_humidity (NAT), sensor.th_salle_de_bain_temperature (NAT)
---
- [heading] CHAMBRE: sensor.temperature_corrige_chambre (TPL), sensor.th_chambre_battery (NAT), sensor.th_chambre_temperature (NAT)
---
- [entity] Réglé à: sensor.temperature_corrige_chambre (TPL)
---
- [entity] Chambre: sensor.th_chambre_temperature (NAT)
---
- [entity] : sensor.th_chambre_battery (NAT)
---
- [custom:bubble-card] : climate.clim_chambre_rm4_mini (NAT)
---
- [custom:streamline-card] : sensor.th_chambre_humidity (NAT), sensor.th_chambre_temperature (NAT)
---
- [custom:bubble-card] CALCUL DU DELTA Intérieur <-> Extérieur (aucune entite)
---
- [custom:streamline-card]  (aucune entite)
---
- [custom:bubble-card] SUIVI DES T° EXTÉRIEUR (aucune entite)
---
- [custom:temperature-heatmap-card] Carte des T° EXTÉRIEUR: sensor.th_balcon_nord_temperature (NAT), weather.vence (NAT)
---
- [custom:bubble-card] SUIVI DES T° DU SALON (aucune entite)
---
- [custom:streamline-card] : sensor.th_salon_temperature (NAT)
---
- [custom:bubble-card] SUIVI DES T° DU CELLIER (aucune entite)
---
- [custom:streamline-card] : sensor.th_cellier_temperature (NAT)
---
- [custom:bubble-card] SUIVI DES T° DE LA CUISINE (aucune entite)
---
- [custom:streamline-card] : sensor.th_cuisine_temperature (NAT)
---
- [custom:bubble-card] SUIVI DES T° DU BUREAU (aucune entite)
---
- [custom:streamline-card] : sensor.th_bureau_temperature (NAT)
---
- [custom:bubble-card] SUIVI DES T° DE LA SALLE DE BAIN (aucune entite)
---
- [custom:streamline-card] : sensor.th_salle_de_bain_temperature (NAT)
---
- [custom:bubble-card] SUIVI DES T° DE LA CHAMBRE (aucune entite)
---
- [custom:streamline-card] : sensor.th_chambre_temperature (NAT)
---
- [custom:bubble-card] Tendance (T°) (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.th_balcon_nord_temperature (NAT), sensor.th_balcon_nord_temperature_trend (TPL)
---
- [custom:mini-graph-card] : sensor.th_balcon_nord_temperature (NAT)
---
- [custom:bubble-card] Tendance (Humitidée %) (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.th_balcon_nord_humidity (NAT), sensor.th_balcon_nord_humidity_trend (TPL)
---
- [custom:mini-graph-card] : sensor.th_balcon_nord_humidity (NAT)

#### vignette_L1C2_temperatures_2026-05-12.yaml (1 cartes, 14 entites)

- [custom:button-card] : sensor.th_balcon_nord_humidity (NAT), sensor.th_balcon_nord_temperature (NAT), sensor.th_bureau_humidity (NAT), sensor.th_bureau_temperature (NAT), sensor.th_cellier_humidity (NAT), sensor.th_cellier_temperature (NAT), sensor.th_chambre_humidity (NAT), sensor.th_chambre_temperature (NAT), sensor.th_cuisine_humidity (NAT), sensor.th_cuisine_temperature (NAT), sensor.th_salle_de_bain_humidity (NAT), sensor.th_salle_de_bain_temperature (NAT), sensor.th_salon_humidity (NAT), sensor.th_salon_temperature (NAT)

### L1C3 - Commandes_Clim

*Validée le 2026-05-13 - chambre sur `climate.clim_chambre_rm4_mini` depuis le 2026-07-14*

> ⚠️ Corrigé le 2026-07-19 : `temperature_moyenne_interieure` attribué à tort à `P1_ui_dashboard.yaml` (ce fichier ne contient que des sensors power_status/*_etat, vérifié dans son corps) - vrai fichier source : `P1_01_clim_logique_system_autom.yaml`. `climate.soufflant_salle_de_bain` retiré - n'existe pas (le soufflant SDB est piloté via `switch.inter_soufflant_salle_de_bain` + `input_select.etat_resistance_soufflant_sdb`, pas une entité climate - vérifié, aucune occurrence dans tout `config_system_YAML/`). Appelé par A et B. Pilote les 3 clims (salon/bureau/chambre) jour/nuit selon parametre `periode`.

*87 entites, 207 cartes, 8 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 44)
  └─→ TPL: P1_01_clim_logique_system_autom.yaml (20)
  └─→ TPL: P1_BV_IB_SW_inter_souflant_sdb.yaml (1)
  └─→ TPL: P1_TOTAL_AMHQ.yaml (1)
  └─→ TPL: P1_ui_dashboard.yaml (18)
  └─→ TPL: P4_groupe_presence.yaml (1)
  └─→ TPL: jour_nuit.yaml (2)
        └─→ VIGNETTE L1C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `climate.clim_bureau_rm4_mini` | NAT | (native/UI) |
| `climate.clim_chambre_rm4_mini` | NAT | idem |
| `climate.clim_salon_rm4_mini` | NAT | idem |
| `climate.radiateur_cuisine` | NAT | idem |
| `climate.soufflant_salle_de_bain` | NAT | idem |
| `input_boolean.clim_bureau_arret_securise_en_cours` | NAT | idem |
| `input_boolean.clim_chambre_arret_securise_en_cours` | NAT | idem |
| `input_boolean.clim_salon_arret_securise_en_cours` | NAT | idem |
| `input_select.etat_resistance_soufflant_sdb` | NAT | idem |
| `person.eric` | NAT | idem |
| `script.j_1_1_salon_clim_on_off_intelligent` | NAT | idem |
| `script.j_1_2_bureau_clim_on_off_intelligent` | NAT | idem |
| `script.j_1_3_chambre_clim_on_off_intelligent` | NAT | idem |
| `sensor.bureau_power_lock` | NAT | idem |
| `sensor.chambre_power_lock` | NAT | idem |
| `sensor.clim_bureau_nous_power` | NAT | idem |
| `sensor.clim_chambre_nous_power` | NAT | idem |
| `sensor.clim_salon_nous_power` | NAT | idem |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | NAT | idem |
| `sensor.radiateur_elec_cuisine_power` | NAT | idem |
| `sensor.salon_power_lock` | NAT | idem |
| `sensor.sdb_seche_serviette_status_affichage` | NAT | idem |
| `sensor.temperature_hors_gel_hiver` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.th_bureau_temperature` | NAT | idem |
| `sensor.th_chambre_temperature` | NAT | idem |
| `sensor.th_cuisine_temperature` | NAT | idem |
| `sensor.th_salle_de_bain_temperature` | NAT | idem |
| `sensor.th_salon_temperature` | NAT | idem |
| `switch.clim_bureau_nous` | NAT | idem |
| `switch.clim_chambre_nous` | NAT | idem |
| `switch.clim_salon_nous` | NAT | idem |
| `switch.prise_soufflant_salle_de_bain_nous` | NAT | idem |
| `switch.radiateur_elec_cuisine` | NAT | idem |
| `switch.schedule_clim_de_la_chambre_week` | NAT | idem |
| `switch.schedule_clim_de_la_chambre_week_end` | NAT | idem |
| `switch.schedule_clim_du_bureau_week` | NAT | idem |
| `switch.schedule_clim_du_bureau_week_end` | NAT | idem |
| `switch.schedule_clim_du_salon_week` | NAT | idem |
| `switch.schedule_clim_du_salon_week_end` | NAT | idem |
| `switch.schedule_radiateur_cuisine_week` | NAT | idem |
| `switch.schedule_radiateur_cuisine_week_end` | NAT | idem |
| `switch.schedule_soufflant_salle_de_bain_week` | NAT | idem |
| `switch.schedule_soufflant_salle_de_bain_week_end` | NAT | idem |
| `sensor.consigne_de_base` | TPL | P1_01_clim_logique_system_autom.yaml |
| `sensor.delta_1` | TPL | idem |
| `sensor.delta_2` | TPL | idem |
| `sensor.delta_5` | TPL | idem |
| `sensor.delta_7` | TPL | idem |
| `sensor.delta_ademe_recommande` | TPL | idem |
| `sensor.mode_ete_hiver` | TPL | idem |
| `sensor.temperature_cible` | TPL | idem |
| `sensor.temperature_confort_jour` | TPL | idem |
| `sensor.temperature_confort_nuit` | TPL | idem |
| `sensor.temperature_corrige_chambre` | TPL | idem |
| `sensor.temperature_corrige_eric` | TPL | idem |
| `sensor.temperature_corrige_mamour` | TPL | idem |
| `sensor.temperature_delta_affichage` | TPL | idem |
| `sensor.temperature_differentielle` | TPL | idem |
| `sensor.temperature_eco_ete` | TPL | idem |
| `sensor.temperature_eco_ete_corrige` | TPL | idem |
| `sensor.temperature_eco_hiver` | TPL | idem |
| `sensor.temperature_eco_hiver_corrige` | TPL | idem |
| `sensor.temperature_moyenne_interieure` | TPL | idem |
| `switch.inter_soufflant_salle_de_bain` | TPL | P1_BV_IB_SW_inter_souflant_sdb.yaml |
| `sensor.conso_clim_rad_total` | TPL | P1_TOTAL_AMHQ.yaml |
| `sensor.bureau_power_status` | TPL | P1_ui_dashboard.yaml |
| `sensor.bureau_power_status_affichage` | TPL | idem |
| `sensor.chambre_power_status` | TPL | idem |
| `sensor.chambre_power_status_affichage` | TPL | idem |
| `sensor.clim_bureau_etat` | TPL | idem |
| `sensor.clim_chambre_etat` | TPL | idem |
| `sensor.clim_salon_etat` | TPL | idem |
| `sensor.cuisine_power_status` | TPL | idem |
| `sensor.cuisine_power_status_affichage` | TPL | idem |
| `sensor.mode_ete_hiver_etat` | TPL | idem |
| `sensor.radiateur_cuisine_etat` | TPL | idem |
| `sensor.salon_power_status` | TPL | idem |
| `sensor.salon_power_status_affichage` | TPL | idem |
| `sensor.sdb_power_status_affichage` | TPL | idem |
| `sensor.sdb_seche_serviette_etat` | TPL | idem |
| `sensor.sdb_seche_serviette_power_status` | TPL | idem |
| `sensor.sdb_soufflant_etat` | TPL | idem |
| `sensor.sdb_soufflant_power_status` | TPL | idem |
| `sensor.presence` | TPL | P4_groupe_presence.yaml |
| `binary_sensor.est_jour_7h30_21h` | TPL | jour_nuit.yaml |
| `binary_sensor.est_nuit_21h_7h30` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_calcule_temp_cible_2026-06-21.yaml` | ✅ |
| `card_prog_clim_bureau_2026-07-14.yaml` | ✅ |
| `card_prog_clim_chambre_2026-07-14.yaml` | ✅ |
| `card_prog_clim_salon_2026-07-14.yaml` | ✅ |
| `card_prog_radiateur_cuisine_2026-07-14.yaml` | ✅ |
| `card_prog_soufflant_sdb_2026-07-14.yaml` | ✅ |
| `page_L1C3_clim_2026-07-18.yaml` | ✅ |
| `vignette_L1C3_clim_2026-07-18.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_calcule_temp_cible_2026-06-21.yaml (14 cartes, 26 entites)

- [vertical-stack]  (aucune entite)
---
- [markdown] : sensor.consigne_de_base (TPL), sensor.delta_1 (TPL), sensor.delta_2 (TPL), sensor.delta_5 (TPL), sensor.delta_7 (TPL), sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_cible (TPL), sensor.temperature_confort_jour (TPL), sensor.temperature_confort_nuit (TPL), sensor.temperature_corrige_chambre (TPL), sensor.temperature_corrige_eric (TPL), sensor.temperature_corrige_mamour (TPL), sensor.temperature_delta_affichage (TPL), sensor.temperature_differentielle (TPL), sensor.temperature_eco_ete (TPL), sensor.temperature_eco_ete_corrige (TPL), sensor.temperature_eco_hiver (TPL), sensor.temperature_eco_hiver_corrige (TPL), sensor.temperature_hors_gel_hiver (NAT), sensor.th_balcon_nord_temperature (NAT)
---
- [conditional] : binary_sensor.est_jour_7h30_21h (TPL)
---
- [markdown] : sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_eco_ete_corrige (TPL), sensor.temperature_eco_hiver_corrige (TPL), switch.clim_bureau_nous (NAT), switch.clim_chambre_nous (NAT), switch.clim_salon_nous (NAT)
---
- [conditional] : binary_sensor.est_jour_7h30_21h (TPL)
---
- [markdown] : sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_corrige_chambre (TPL), sensor.temperature_corrige_mamour (TPL), sensor.temperature_eco_ete_corrige (TPL), sensor.temperature_eco_hiver_corrige (TPL), switch.clim_bureau_nous (NAT), switch.clim_chambre_nous (NAT), switch.clim_salon_nous (NAT)
---
- [conditional] : binary_sensor.est_jour_7h30_21h (TPL)
---
- [markdown] : sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_corrige_chambre (TPL), sensor.temperature_corrige_eric (TPL), switch.clim_bureau_nous (NAT), switch.clim_chambre_nous (NAT), switch.clim_salon_nous (NAT)
---
- [conditional] : binary_sensor.est_jour_7h30_21h (TPL)
---
- [markdown] : sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_corrige_chambre (TPL), sensor.temperature_corrige_eric (TPL), sensor.temperature_corrige_mamour (TPL), switch.clim_bureau_nous (NAT), switch.clim_chambre_nous (NAT), switch.clim_salon_nous (NAT)
---
- [conditional] : binary_sensor.est_nuit_21h_7h30 (TPL)
---
- [markdown] : sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_eco_ete_corrige (TPL), sensor.temperature_eco_hiver_corrige (TPL), switch.clim_bureau_nous (NAT), switch.clim_chambre_nous (NAT), switch.clim_salon_nous (NAT)
---
- [conditional] : binary_sensor.est_nuit_21h_7h30 (TPL)
---
- [markdown] : sensor.mode_ete_hiver (TPL), sensor.presence (TPL), sensor.temperature_confort_nuit (TPL), switch.clim_bureau_nous (NAT), switch.clim_chambre_nous (NAT), switch.clim_salon_nous (NAT)

#### card_prog_clim_bureau_2026-07-14.yaml (16 cartes, 5 entites)

- [grid]  (aucune entite)
---
- [heading] CLIM. DU BUREAU: sensor.th_bureau_temperature (NAT)
---
- [entity] : sensor.th_bureau_temperature (NAT)
---
- [area]  (aucune entite)
---
- [clock]  (aucune entite)
---
- [custom:scheduler-card] Planificateur Clim. Bureau: climate.clim_bureau_rm4_mini (NAT), person.eric (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_clim_du_bureau_week (NAT)
---
- [entities] : switch.schedule_clim_du_bureau_week (NAT)
---
- [markdown] : switch.schedule_clim_du_bureau_week (NAT)
---
- [markdown] : switch.schedule_clim_du_bureau_week (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_clim_du_bureau_week_end (NAT)
---
- [entities] : switch.schedule_clim_du_bureau_week_end (NAT)
---
- [markdown] : switch.schedule_clim_du_bureau_week_end (NAT)
---
- [markdown] : switch.schedule_clim_du_bureau_week_end (NAT)

#### card_prog_clim_chambre_2026-07-14.yaml (1 cartes, 4 entites)

- [(parse erreur)] : climate.clim_chambre_rm4_mini (NAT), sensor.th_chambre_temperature (NAT), switch.schedule_clim_de_la_chambre_week (NAT), switch.schedule_clim_de_la_chambre_week_end (NAT)

#### card_prog_clim_salon_2026-07-14.yaml (16 cartes, 4 entites)

- [grid]  (aucune entite)
---
- [heading] CLIM. DU SALON: sensor.th_salon_temperature (NAT)
---
- [entity] : sensor.th_salon_temperature (NAT)
---
- [area]  (aucune entite)
---
- [clock]  (aucune entite)
---
- [custom:scheduler-card] Planificateur Clim. Salon: climate.clim_salon_rm4_mini (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_clim_du_salon_week (NAT)
---
- [entities] : switch.schedule_clim_du_salon_week (NAT)
---
- [markdown] : switch.schedule_clim_du_salon_week (NAT)
---
- [markdown] : switch.schedule_clim_du_salon_week (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_clim_du_salon_week_end (NAT)
---
- [entities] : switch.schedule_clim_du_salon_week_end (NAT)
---
- [markdown] : switch.schedule_clim_du_salon_week_end (NAT)
---
- [markdown] : switch.schedule_clim_du_salon_week_end (NAT)

#### card_prog_radiateur_cuisine_2026-07-14.yaml (16 cartes, 5 entites)

- [grid]  (aucune entite)
---
- [heading] RADIATEUR CUISINE: sensor.th_cuisine_temperature (NAT)
---
- [entity] : sensor.th_cuisine_temperature (NAT)
---
- [area]  (aucune entite)
---
- [clock]  (aucune entite)
---
- [custom:scheduler-card] Planificateur Radiateur Cuisine: climate.radiateur_cuisine (NAT), person.eric (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_radiateur_cuisine_week (NAT)
---
- [entities] : switch.schedule_radiateur_cuisine_week (NAT)
---
- [markdown] : switch.schedule_radiateur_cuisine_week (NAT)
---
- [markdown] : switch.schedule_radiateur_cuisine_week (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_radiateur_cuisine_week_end (NAT)
---
- [entities] : switch.schedule_radiateur_cuisine_week_end (NAT)
---
- [markdown] : switch.schedule_radiateur_cuisine_week_end (NAT)
---
- [markdown] : switch.schedule_radiateur_cuisine_week_end (NAT)

#### card_prog_soufflant_sdb_2026-07-14.yaml (16 cartes, 4 entites)

- [grid]  (aucune entite)
---
- [heading] Soufflant Salle de Bain: sensor.th_salle_de_bain_temperature (NAT)
---
- [entity] : sensor.th_salle_de_bain_temperature (NAT)
---
- [area]  (aucune entite)
---
- [clock]  (aucune entite)
---
- [custom:scheduler-card] Planificateur Soufflant Salle de Bain: climate.soufflant_salle_de_bain (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_soufflant_salle_de_bain_week (NAT)
---
- [entities] : switch.schedule_soufflant_salle_de_bain_week (NAT)
---
- [markdown] : switch.schedule_soufflant_salle_de_bain_week (NAT)
---
- [markdown] : switch.schedule_soufflant_salle_de_bain_week (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [markdown] : switch.schedule_soufflant_salle_de_bain_week_end (NAT)
---
- [entities] : switch.schedule_soufflant_salle_de_bain_week_end (NAT)
---
- [markdown] : switch.schedule_soufflant_salle_de_bain_week_end (NAT)
---
- [markdown] : switch.schedule_soufflant_salle_de_bain_week_end (NAT)

#### page_L1C3_clim_2026-07-18.yaml (127 cartes, 57 entites)

- [grid]  (aucune entite)
---
- [heading] CLIM.  / RADIATEUR: sensor.temperature_delta_affichage (TPL)
---
- [entity] : sensor.temperature_delta_affichage (TPL)
---
- [conditional] : sensor.bureau_power_status_affichage (TPL), sensor.chambre_power_status_affichage (TPL), sensor.cuisine_power_status_affichage (TPL), sensor.salon_power_status_affichage (TPL), sensor.sdb_power_status_affichage (TPL), sensor.sdb_seche_serviette_status_affichage (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [conditional] : sensor.salon_power_status (TPL)
---
- [template] : sensor.clim_salon_etat (TPL)
---
- [conditional] : sensor.cuisine_power_status (TPL)
---
- [template] : sensor.radiateur_cuisine_etat (TPL)
---
- [conditional] : sensor.bureau_power_status (TPL)
---
- [template] : sensor.clim_bureau_etat (TPL)
---
- [conditional] : sensor.sdb_soufflant_power_status (TPL)
---
- [template] : sensor.sdb_soufflant_etat (TPL)
---
- [conditional] : sensor.sdb_seche_serviette_power_status (TPL)
---
- [template] : sensor.sdb_seche_serviette_etat (TPL)
---
- [conditional] : sensor.chambre_power_status (TPL)
---
- [template] : sensor.clim_chambre_etat (TPL)
---
- [vertical-stack] : sensor.conso_clim_rad_total (TPL)
---
- [custom:auto-entities] : sensor.conso_clim_rad_total (TPL)
---
- [custom:bar-card]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [conditional] : input_boolean.clim_salon_arret_securise_en_cours (NAT), sensor.salon_power_lock (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [conditional] : input_boolean.clim_salon_arret_securise_en_cours (NAT), sensor.salon_power_status_affichage (TPL), switch.clim_salon_nous (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] Clim. Salon: script.j_1_1_salon_clim_on_off_intelligent (NAT), sensor.clim_salon_nous_power (NAT), switch.clim_salon_nous (NAT), switch.schedule_clim_du_salon_week (NAT), switch.schedule_clim_du_salon_week_end (NAT)
---
- [entity]  (aucune entite)
---
- [entity] Sem.: switch.schedule_clim_du_salon_week (NAT)
---
- [entity] Week-End: switch.schedule_clim_du_salon_week_end (NAT)
---
- [entity] : sensor.clim_salon_nous_power (NAT)
---
- [entity] : script.j_1_1_salon_clim_on_off_intelligent (NAT), switch.clim_salon_nous (NAT)
---
- [thermostat] Clim SALON: climate.clim_salon_rm4_mini (NAT)
---
- [climate-hvac-modes]  (aucune entite)
---
- [climate-fan-modes]  (aucune entite)
---
- [vertical-stack] : sensor.clim_salon_nous_power (NAT)
---
- [custom:auto-entities] : sensor.clim_salon_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] Rad. Cuisine: sensor.radiateur_elec_cuisine_power (NAT), switch.radiateur_elec_cuisine (NAT), switch.schedule_radiateur_cuisine_week (NAT), switch.schedule_radiateur_cuisine_week_end (NAT)
---
- [entity] : switch.radiateur_elec_cuisine (NAT)
---
- [entity] Sem.: switch.schedule_radiateur_cuisine_week (NAT)
---
- [entity] Week-End: switch.schedule_radiateur_cuisine_week_end (NAT)
---
- [entity] : sensor.radiateur_elec_cuisine_power (NAT)
---
- [entity] : switch.radiateur_elec_cuisine (NAT)
---
- [thermostat] : climate.radiateur_cuisine (NAT)
---
- [climate-hvac-modes]  (aucune entite)
---
- [vertical-stack] : sensor.radiateur_elec_cuisine_power (NAT)
---
- [custom:auto-entities] : sensor.radiateur_elec_cuisine_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [conditional] : input_boolean.clim_bureau_arret_securise_en_cours (NAT), sensor.bureau_power_lock (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [conditional] : input_boolean.clim_bureau_arret_securise_en_cours (NAT), sensor.bureau_power_status_affichage (TPL), switch.clim_bureau_nous (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] clim. Bureau: script.j_1_2_bureau_clim_on_off_intelligent (NAT), sensor.clim_bureau_nous_power (NAT), switch.clim_bureau_nous (NAT), switch.schedule_clim_du_bureau_week (NAT), switch.schedule_clim_du_bureau_week_end (NAT)
---
- [entity]  (aucune entite)
---
- [entity] Sem.: switch.schedule_clim_du_bureau_week (NAT)
---
- [entity] Week-End: switch.schedule_clim_du_bureau_week_end (NAT)
---
- [entity] : sensor.clim_bureau_nous_power (NAT)
---
- [entity] : script.j_1_2_bureau_clim_on_off_intelligent (NAT), switch.clim_bureau_nous (NAT)
---
- [thermostat] Clim du BUREAU: climate.clim_bureau_rm4_mini (NAT)
---
- [climate-hvac-modes]  (aucune entite)
---
- [climate-fan-modes]  (aucune entite)
---
- [vertical-stack] : sensor.clim_bureau_nous_power (NAT)
---
- [custom:auto-entities] : sensor.clim_bureau_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] Soullant SdB: sensor.prise_soufflant_salle_de_bain_nous_power (NAT), switch.prise_soufflant_salle_de_bain_nous (NAT), switch.schedule_soufflant_salle_de_bain_week (NAT), switch.schedule_soufflant_salle_de_bain_week_end (NAT)
---
- [entity]  (aucune entite)
---
- [entity] Sem.: switch.schedule_soufflant_salle_de_bain_week (NAT)
---
- [entity] Week-End: switch.schedule_soufflant_salle_de_bain_week_end (NAT)
---
- [entity] : sensor.prise_soufflant_salle_de_bain_nous_power (NAT)
---
- [entity] : switch.prise_soufflant_salle_de_bain_nous (NAT)
---
- [thermostat] : climate.soufflant_salle_de_bain (NAT)
---
- [climate-hvac-modes]  (aucune entite)
---
- [custom:button-card] Soufflant SDB: climate.soufflant_salle_de_bain (NAT), input_select.etat_resistance_soufflant_sdb (NAT), sensor.sdb_soufflant_power_status (TPL), sensor.th_salle_de_bain_temperature (NAT), switch.inter_soufflant_salle_de_bain (TPL)
---
- [vertical-stack] : sensor.prise_soufflant_salle_de_bain_nous_power (NAT)
---
- [custom:auto-entities] : sensor.prise_soufflant_salle_de_bain_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [conditional] : input_boolean.clim_chambre_arret_securise_en_cours (NAT), sensor.chambre_power_lock (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [conditional] : input_boolean.clim_chambre_arret_securise_en_cours (NAT), sensor.chambre_power_status_affichage (TPL), switch.clim_chambre_nous (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] clim. Chambre: script.j_1_3_chambre_clim_on_off_intelligent (NAT), sensor.clim_chambre_nous_power (NAT), switch.clim_chambre_nous (NAT), switch.schedule_clim_de_la_chambre_week (NAT), switch.schedule_clim_de_la_chambre_week_end (NAT)
---
- [entity]  (aucune entite)
---
- [entity] Sem.: switch.schedule_clim_de_la_chambre_week (NAT)
---
- [entity] Week-End: switch.schedule_clim_de_la_chambre_week_end (NAT)
---
- [entity] : sensor.clim_chambre_nous_power (NAT)
---
- [entity] : script.j_1_3_chambre_clim_on_off_intelligent (NAT), switch.clim_chambre_nous (NAT)
---
- [thermostat] Clim de la CHAMBRE: climate.clim_chambre_rm4_mini (NAT)
---
- [climate-hvac-modes]  (aucune entite)
---
- [climate-fan-modes]  (aucune entite)
---
- [vertical-stack] : sensor.clim_chambre_nous_power (NAT)
---
- [custom:auto-entities] : sensor.clim_chambre_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [custom:bubble-card] CALCUL DU DELTA Intérieur <-> Extérieur (aucune entite)
---
- [custom:streamline-card]  (aucune entite)
---
- [custom:streamline-card]  (aucune entite)

#### vignette_L1C3_clim_2026-07-18.yaml (1 cartes, 21 entites)

- [custom:button-card] : climate.clim_bureau_rm4_mini (NAT), climate.clim_chambre_rm4_mini (NAT), climate.clim_salon_rm4_mini (NAT), climate.radiateur_cuisine (NAT), climate.soufflant_salle_de_bain (NAT), sensor.bureau_power_status (TPL), sensor.chambre_power_status (TPL), sensor.clim_bureau_etat (TPL), sensor.clim_chambre_etat (TPL), sensor.clim_salon_etat (TPL), sensor.cuisine_power_status (TPL), sensor.delta_ademe_recommande (TPL), sensor.mode_ete_hiver (TPL), sensor.mode_ete_hiver_etat (TPL), sensor.radiateur_cuisine_etat (TPL), sensor.salon_power_status (TPL), sensor.sdb_seche_serviette_etat (TPL), sensor.sdb_seche_serviette_power_status (TPL), sensor.sdb_soufflant_etat (TPL), sensor.sdb_soufflant_power_status (TPL), sensor.temperature_moyenne_interieure (TPL)

### L2C1 - Energie_Generale


> **Source énergie générale (depuis 2026-06-17) : Nodon SEM-4-1-00** (pince ampèremétrique Z2M) - `sensor.general_electric_appart_energy` (kWh) → source des UM P0 - `sensor.general_electric_appart_power` (W) → puissance temps réel **Linky (MyElectricalData)** = J-1 uniquement (HP/HC historique) - source secondaire
> ⚠️ Corrigé le 2026-07-19 : le diagramme référençait un fichier `total_par_poste_7.yaml` qui n'existe pas - les vrais noms sont `P0_diag_conso_{jour,hebdomadaire,mois}_en_cours.yaml` (3 fichiers distincts pour `diag_poste_*`) et `P0_total_pour_les_7_postes.yaml` (pour `total_poste_*_puissance`), vérifiés par grep des `unique_id:` réels.

*181 entites, 153 cartes, 4 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 66)
  └─→ UM: P0_UM_AMHQ.yaml (3)
  └─→ UM: P2_UM_AMHQ_prises.yaml (34)
  └─→ UM: P2_UM_AMHQ_veilles.yaml (2)
  └─→ TPL: P0_01_genelec_appart_AMHQ_cost.yaml (4)
  └─→ TPL: P0_02_ratio_hp_hc.yaml (3)
  └─→ TPL: P0_03_AVG_genelec_appart.yaml (2)
  └─→ TPL: P0_diag_conso_hebdomadaire_en_cours.yaml (7)
  └─→ TPL: P0_diag_conso_jour_en_cours.yaml (7)
  └─→ TPL: P0_diag_conso_mois_en_cours.yaml (7)
  └─→ TPL: P0_total_pour_les_7_postes.yaml (6)
  └─→ TPL: P2_AVG_AMHQ_prises.yaml (34)
  └─→ TPL: P2_AVG_AMHQ_veilles.yaml (2)
  └─→ TPL: P2_current_all_standby.yaml (1)
  └─→ TPL: P3_POWER_3_TOTAL_ZONE.yaml (1)
  └─→ SEN: P0_MINI_MAXI_AVG_Genelec_appart.yaml (2)
        └─→ VIGNETTE L2C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.all_standby_power` | NAT | (native/UI) |
| `sensor.clim_bureau_nous_power` | NAT | idem |
| `sensor.clim_chambre_nous_power` | NAT | idem |
| `sensor.clim_salon_nous_power` | NAT | idem |
| `sensor.four_et_plaque_de_cuisson_current` | NAT | idem |
| `sensor.four_et_plaque_de_cuisson_power` | NAT | idem |
| `sensor.genelec_appart_hphc_hebdo_um_hc` | NAT | idem |
| `sensor.genelec_appart_hphc_hebdo_um_hp` | NAT | idem |
| `sensor.genelec_appart_hphc_mensuel_um_hc` | NAT | idem |
| `sensor.genelec_appart_hphc_mensuel_um_hp` | NAT | idem |
| `sensor.genelec_appart_hphc_quotidien_um_hc` | NAT | idem |
| `sensor.genelec_appart_hphc_quotidien_um_hp` | NAT | idem |
| `sensor.general_electric_appart_energy` | NAT | idem |
| `sensor.general_electric_appart_power` | NAT | idem |
| `sensor.hue_ambiance_lamp_salon_` | NAT | idem |
| `sensor.hue_color_candle_chambre_eric_power` | NAT | idem |
| `sensor.hue_color_candle_chambre_gege_power` | NAT | idem |
| `sensor.hue_color_candle_salon_1_power` | NAT | idem |
| `sensor.hue_play_1_pc_bureau_power` | NAT | idem |
| `sensor.hue_play_2_pc_bureau_power` | NAT | idem |
| `sensor.hue_play_3_pc_bureau_power` | NAT | idem |
| `sensor.hue_white_lamp_bureau_1_power` | NAT | idem |
| `sensor.hue_white_lamp_bureau_2_power` | NAT | idem |
| `sensor.hue_white_lamp_chambre_` | NAT | idem |
| `sensor.hue_white_lamp_couloir_power` | NAT | idem |
| `sensor.hue_white_lamp_cuisine_power` | NAT | idem |
| `sensor.hue_white_lamp_entree_power` | NAT | idem |
| `sensor.hue_white_lamp_salle_de_bain_power` | NAT | idem |
| `sensor.hue_white_lamp_table_power` | NAT | idem |
| `sensor.linky_25481620821301_consumption_history` | NAT | idem |
| `sensor.prise_airfryer_ninja_nous_current` | NAT | idem |
| `sensor.prise_airfryer_ninja_nous_power` | NAT | idem |
| `sensor.prise_box_internet_ikea_current` | NAT | idem |
| `sensor.prise_box_internet_ikea_power` | NAT | idem |
| `sensor.prise_bureau_fer_a_repasser_nous_current` | NAT | idem |
| `sensor.prise_bureau_fer_a_repasser_nous_power` | NAT | idem |
| `sensor.prise_bureau_pc_ikea_current` | NAT | idem |
| `sensor.prise_bureau_pc_ikea_power` | NAT | idem |
| `sensor.prise_congelateur_cuisine_nous_current` | NAT | idem |
| `sensor.prise_congelateur_cuisine_nous_power` | NAT | idem |
| `sensor.prise_four_micro_ondes_nous_current` | NAT | idem |
| `sensor.prise_four_micro_ondes_nous_power` | NAT | idem |
| `sensor.prise_frigo_cuisine_nous_current` | NAT | idem |
| `sensor.prise_frigo_cuisine_nous_power` | NAT | idem |
| `sensor.prise_horloge_ikea_current` | NAT | idem |
| `sensor.prise_horloge_ikea_power` | NAT | idem |
| `sensor.prise_lave_linge_nous_current` | NAT | idem |
| `sensor.prise_lave_linge_nous_power` | NAT | idem |
| `sensor.prise_lave_vaisselle_nous_current` | NAT | idem |
| `sensor.prise_lave_vaisselle_nous_power` | NAT | idem |
| `sensor.prise_pc_s_gege_ikea_current` | NAT | idem |
| `sensor.prise_pc_s_gege_ikea_power` | NAT | idem |
| `sensor.prise_petit_dejeune_nous_current` | NAT | idem |
| `sensor.prise_petit_dejeune_nous_power` | NAT | idem |
| `sensor.prise_salon_chargeur_nous_current` | NAT | idem |
| `sensor.prise_salon_chargeur_nous_power` | NAT | idem |
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | NAT | idem |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | NAT | idem |
| `sensor.prise_tete_de_lit_chambre_current` | NAT | idem |
| `sensor.prise_tete_de_lit_chambre_power` | NAT | idem |
| `sensor.prise_tv_chambre_nous_current` | NAT | idem |
| `sensor.prise_tv_chambre_nous_power` | NAT | idem |
| `sensor.prise_tv_salon_ikea_current` | NAT | idem |
| `sensor.prise_tv_salon_ikea_power` | NAT | idem |
| `sensor.radiateur_elec_cuisine_power` | NAT | idem |
| `sensor.relais_lumiere_sdb_sonoff_power` | NAT | idem |
| `sensor.genelec_appart_cout_hc_quotidien` | TPL | P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_cout_hp_quotidien` | TPL | idem |
| `sensor.genelec_appart_cout_total_mensuel` | TPL | idem |
| `sensor.genelec_appart_cout_total_quotidien` | TPL | idem |
| `sensor.genelec_appart_ratio_hc_hebdomadaire` | TPL | P0_02_ratio_hp_hc.yaml |
| `sensor.genelec_appart_ratio_hc_mensuel` | TPL | idem |
| `sensor.genelec_appart_ratio_hc_quotidien` | TPL | idem |
| `sensor.genelec_appart_avg_watts_mensuel` | TPL | P0_03_AVG_genelec_appart.yaml |
| `sensor.genelec_appart_avg_watts_quotidien` | TPL | idem |
| `sensor.genelec_appart_conso_maxi_24h` | SEN | P0_MINI_MAXI_AVG_Genelec_appart.yaml |
| `sensor.genelec_appart_conso_mini_24h` | SEN | idem |
| `sensor.genelec_appart_hebdomadaire_um` | UM | P0_UM_AMHQ.yaml |
| `sensor.genelec_appart_mensuel_um` | UM | idem |
| `sensor.genelec_appart_quotidien_um` | UM | idem |
| `sensor.diag_poste_autre_hebdomadaire` | TPL | P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_chauffage_hebdomadaire` | TPL | idem |
| `sensor.diag_poste_cuisine_hebdomadaire` | TPL | idem |
| `sensor.diag_poste_eclairage_hebdomadaire` | TPL | idem |
| `sensor.diag_poste_froid_hebdomadaire` | TPL | idem |
| `sensor.diag_poste_hygiene_hebdomadaire` | TPL | idem |
| `sensor.diag_poste_multimedia_hebdomadaire` | TPL | idem |
| `sensor.diag_poste_autre_quotidien` | TPL | P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_chauffage_quotidien` | TPL | idem |
| `sensor.diag_poste_cuisine_quotidien` | TPL | idem |
| `sensor.diag_poste_eclairage_quotidien` | TPL | idem |
| `sensor.diag_poste_froid_quotidien` | TPL | idem |
| `sensor.diag_poste_hygiene_quotidien` | TPL | idem |
| `sensor.diag_poste_multimedia_quotidien` | TPL | idem |
| `sensor.diag_poste_autre_mensuel` | TPL | P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_chauffage_mensuel` | TPL | idem |
| `sensor.diag_poste_cuisine_mensuel` | TPL | idem |
| `sensor.diag_poste_eclairage_mensuel` | TPL | idem |
| `sensor.diag_poste_froid_mensuel` | TPL | idem |
| `sensor.diag_poste_hygiene_mensuel` | TPL | idem |
| `sensor.diag_poste_multimedia_mensuel` | TPL | idem |
| `sensor.total_poste_autre_puissance` | TPL | P0_total_pour_les_7_postes.yaml |
| `sensor.total_poste_chauffage_puissance` | TPL | idem |
| `sensor.total_poste_cuisine_puissance` | TPL | idem |
| `sensor.total_poste_froid_puissance` | TPL | idem |
| `sensor.total_poste_hygiene_puissance` | TPL | idem |
| `sensor.total_poste_multimedia_puissance` | TPL | idem |
| `sensor.airfryer_avg_watts_mensuel` | TPL | P2_AVG_AMHQ_prises.yaml |
| `sensor.airfryer_avg_watts_quotidien` | TPL | idem |
| `sensor.box_internet_avg_watts_mensuel` | TPL | idem |
| `sensor.box_internet_avg_watts_quotidien` | TPL | idem |
| `sensor.chargeurs_salon_avg_watts_mensuel` | TPL | idem |
| `sensor.chargeurs_salon_avg_watts_quotidien` | TPL | idem |
| `sensor.congelateur_avg_watts_mensuel` | TPL | idem |
| `sensor.congelateur_avg_watts_quotidien` | TPL | idem |
| `sensor.fer_repasser_avg_watts_mensuel` | TPL | idem |
| `sensor.fer_repasser_avg_watts_quotidien` | TPL | idem |
| `sensor.four_mo_avg_watts_mensuel` | TPL | idem |
| `sensor.four_mo_avg_watts_quotidien` | TPL | idem |
| `sensor.frigo_avg_watts_mensuel` | TPL | idem |
| `sensor.frigo_avg_watts_quotidien` | TPL | idem |
| `sensor.horloge_avg_watts_mensuel` | TPL | idem |
| `sensor.horloge_avg_watts_quotidien` | TPL | idem |
| `sensor.lave_linge_avg_watts_mensuel` | TPL | idem |
| `sensor.lave_linge_avg_watts_quotidien` | TPL | idem |
| `sensor.lave_vaisselle_avg_watts_mensuel` | TPL | idem |
| `sensor.lave_vaisselle_avg_watts_quotidien` | TPL | idem |
| `sensor.pc_bureau_avg_watts_mensuel` | TPL | idem |
| `sensor.pc_bureau_avg_watts_quotidien` | TPL | idem |
| `sensor.pc_gege_avg_watts_mensuel` | TPL | idem |
| `sensor.pc_gege_avg_watts_quotidien` | TPL | idem |
| `sensor.petit_dej_avg_watts_mensuel` | TPL | idem |
| `sensor.petit_dej_avg_watts_quotidien` | TPL | idem |
| `sensor.plaques_cuisson_avg_watts_mensuel` | TPL | idem |
| `sensor.plaques_cuisson_avg_watts_quotidien` | TPL | idem |
| `sensor.tetes_lit_avg_watts_mensuel` | TPL | idem |
| `sensor.tetes_lit_avg_watts_quotidien` | TPL | idem |
| `sensor.tv_chambre_avg_watts_mensuel` | TPL | idem |
| `sensor.tv_chambre_avg_watts_quotidien` | TPL | idem |
| `sensor.tv_salon_avg_watts_mensuel` | TPL | idem |
| `sensor.tv_salon_avg_watts_quotidien` | TPL | idem |
| `sensor.all_standby_avg_watts_mensuel` | TPL | P2_AVG_AMHQ_veilles.yaml |
| `sensor.all_standby_avg_watts_quotidien` | TPL | idem |
| `sensor.four_et_plaque_de_cuisson_mensuel_um` | UM | P2_UM_AMHQ_prises.yaml |
| `sensor.four_et_plaque_de_cuisson_quotidien_um` | UM | idem |
| `sensor.prise_airfryer_ninja_nous_mensuel_um` | UM | idem |
| `sensor.prise_airfryer_ninja_nous_quotidien_um` | UM | idem |
| `sensor.prise_box_internet_ikea_mensuel_um` | UM | idem |
| `sensor.prise_box_internet_ikea_quotidien_um` | UM | idem |
| `sensor.prise_bureau_fer_a_repasser_nous_mensuel_um` | UM | idem |
| `sensor.prise_bureau_fer_a_repasser_nous_quotidien_um` | UM | idem |
| `sensor.prise_bureau_pc_ikea_mensuel_um` | UM | idem |
| `sensor.prise_bureau_pc_ikea_quotidien_um` | UM | idem |
| `sensor.prise_congelateur_cuisine_nous_mensuel_um` | UM | idem |
| `sensor.prise_congelateur_cuisine_nous_quotidien_um` | UM | idem |
| `sensor.prise_four_micro_ondes_nous_mensuel_um` | UM | idem |
| `sensor.prise_four_micro_ondes_nous_quotidien_um` | UM | idem |
| `sensor.prise_frigo_cuisine_nous_mensuel_um` | UM | idem |
| `sensor.prise_frigo_cuisine_nous_quotidien_um` | UM | idem |
| `sensor.prise_horloge_ikea_mensuel_um` | UM | idem |
| `sensor.prise_horloge_ikea_quotidien_um` | UM | idem |
| `sensor.prise_lave_linge_nous_mensuel_um` | UM | idem |
| `sensor.prise_lave_linge_nous_quotidien_um` | UM | idem |
| `sensor.prise_lave_vaisselle_nous_mensuel_um` | UM | idem |
| `sensor.prise_lave_vaisselle_nous_quotidien_um` | UM | idem |
| `sensor.prise_pc_s_gege_ikea_mensuel_um` | UM | idem |
| `sensor.prise_pc_s_gege_ikea_quotidien_um` | UM | idem |
| `sensor.prise_petit_dejeune_nous_mensuel_um` | UM | idem |
| `sensor.prise_petit_dejeune_nous_quotidien_um` | UM | idem |
| `sensor.prise_salon_chargeur_nous_mensuel_um` | UM | idem |
| `sensor.prise_salon_chargeur_nous_quotidien_um` | UM | idem |
| `sensor.prise_tete_de_lit_chambre_mensuel_um` | UM | idem |
| `sensor.prise_tete_de_lit_chambre_quotidien_um` | UM | idem |
| `sensor.prise_tv_chambre_nous_mensuel_um` | UM | idem |
| `sensor.prise_tv_chambre_nous_quotidien_um` | UM | idem |
| `sensor.prise_tv_salon_ikea_mensuel_um` | UM | idem |
| `sensor.prise_tv_salon_ikea_quotidien_um` | UM | idem |
| `sensor.all_standby_mensuel_um` | UM | P2_UM_AMHQ_veilles.yaml |
| `sensor.all_standby_quotidien_um` | UM | idem |
| `sensor.all_standby_current` | TPL | P2_current_all_standby.yaml |
| `sensor.eclairage_total_group_puissance_tpl` | TPL | P3_POWER_3_TOTAL_ZONE.yaml |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L2C1_energie_mensuel_2026-06-18.yaml` | ✅ |
| `page_L2C1_energie_principale_2026-06-18.yaml` | ✅ |
| `page_L2C1_energie_temps_reel_2026-06-18.yaml` | ✅ |
| `vignette_L2C1_energie_2026-06-18.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L2C1_energie_mensuel_2026-06-18.yaml (33 cartes, 38 entites)

- [grid]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Consommations Mensuelles: sensor.genelec_appart_cout_total_mensuel (TPL), sensor.genelec_appart_mensuel_um (UM)
---
- [entity] Mois: sensor.genelec_appart_mensuel_um (UM)
---
- [entity] Coût: sensor.genelec_appart_cout_total_mensuel (TPL)
---
- [custom:apexcharts-card] : sensor.all_standby_mensuel_um (UM), sensor.four_et_plaque_de_cuisson_mensuel_um (UM), sensor.prise_airfryer_ninja_nous_mensuel_um (UM), sensor.prise_box_internet_ikea_mensuel_um (UM), sensor.prise_bureau_fer_a_repasser_nous_mensuel_um (UM), sensor.prise_bureau_pc_ikea_mensuel_um (UM), sensor.prise_congelateur_cuisine_nous_mensuel_um (UM), sensor.prise_four_micro_ondes_nous_mensuel_um (UM), sensor.prise_frigo_cuisine_nous_mensuel_um (UM), sensor.prise_horloge_ikea_mensuel_um (UM), sensor.prise_lave_linge_nous_mensuel_um (UM), sensor.prise_lave_vaisselle_nous_mensuel_um (UM), sensor.prise_pc_s_gege_ikea_mensuel_um (UM), sensor.prise_petit_dejeune_nous_mensuel_um (UM), sensor.prise_salon_chargeur_nous_mensuel_um (UM), sensor.prise_tete_de_lit_chambre_mensuel_um (UM), sensor.prise_tv_chambre_nous_mensuel_um (UM), sensor.prise_tv_salon_ikea_mensuel_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:bubble-card] Détails par pièce (aucune entite)
---
- [custom:tabbed-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.box_internet_avg_watts_mensuel (TPL), sensor.prise_box_internet_ikea_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.horloge_avg_watts_mensuel (TPL), sensor.prise_horloge_ikea_mensuel_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.pc_gege_avg_watts_mensuel (TPL), sensor.prise_pc_s_gege_ikea_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.chargeurs_salon_avg_watts_mensuel (TPL), sensor.prise_salon_chargeur_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.prise_tv_salon_ikea_mensuel_um (UM), sensor.tv_salon_avg_watts_mensuel (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.four_mo_avg_watts_mensuel (TPL), sensor.prise_four_micro_ondes_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.petit_dej_avg_watts_mensuel (TPL), sensor.prise_petit_dejeune_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.lave_linge_avg_watts_mensuel (TPL), sensor.prise_lave_linge_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.lave_vaisselle_avg_watts_mensuel (TPL), sensor.prise_lave_vaisselle_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.airfryer_avg_watts_mensuel (TPL), sensor.prise_airfryer_ninja_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.four_et_plaque_de_cuisson_mensuel_um (UM), sensor.plaques_cuisson_avg_watts_mensuel (TPL)
---
- [custom:streamline-card] : sensor.frigo_avg_watts_mensuel (TPL), sensor.prise_frigo_cuisine_nous_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.congelateur_avg_watts_mensuel (TPL), sensor.prise_congelateur_cuisine_nous_mensuel_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.pc_bureau_avg_watts_mensuel (TPL), sensor.prise_bureau_pc_ikea_mensuel_um (UM)
---
- [custom:streamline-card] : sensor.fer_repasser_avg_watts_mensuel (TPL), sensor.prise_bureau_fer_a_repasser_nous_mensuel_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.prise_tete_de_lit_chambre_mensuel_um (UM), sensor.tetes_lit_avg_watts_mensuel (TPL)
---
- [custom:streamline-card] : sensor.prise_tv_chambre_nous_mensuel_um (UM), sensor.tv_chambre_avg_watts_mensuel (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.all_standby_avg_watts_mensuel (TPL), sensor.all_standby_mensuel_um (UM)

#### page_L2C1_energie_principale_2026-06-18.yaml (39 cartes, 50 entites)

- [grid]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Énergie Générale: sensor.genelec_appart_conso_maxi_24h (SEN), sensor.genelec_appart_conso_mini_24h (SEN), sensor.general_electric_appart_power (NAT)
---
- [entity] Réel: sensor.general_electric_appart_power (NAT)
---
- [entity] Mini 24h: sensor.genelec_appart_conso_mini_24h (SEN)
---
- [entity] Maxi 24h: sensor.genelec_appart_conso_maxi_24h (SEN)
---
- [custom:tabbed-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [grid]  (aucune entite)
---
- [custom:ring-tile] Mini: sensor.genelec_appart_conso_mini_24h (SEN)
---
- [custom:ring-tile] Réel J: sensor.genelec_appart_quotidien_um (UM)
---
- [custom:ring-tile] Maxi: sensor.genelec_appart_conso_maxi_24h (SEN)
---
- [grid]  (aucune entite)
---
- [custom:ring-tile] Coût Total J: sensor.genelec_appart_cout_total_quotidien (TPL)
---
- [custom:ring-tile] Coût HP J: sensor.genelec_appart_cout_hp_quotidien (TPL)
---
- [custom:ring-tile] Coût HC J: sensor.genelec_appart_cout_hc_quotidien (TPL)
---
- [custom:bar-card] Analyse de Précision — Linky vs Nodon: sensor.general_electric_appart_energy (NAT), sensor.linky_25481620821301_consumption_history (NAT)
---
- [custom:apexcharts-card] : sensor.eclairage_total_group_puissance_tpl (TPL), sensor.total_poste_autre_puissance (TPL), sensor.total_poste_chauffage_puissance (TPL), sensor.total_poste_cuisine_puissance (TPL), sensor.total_poste_froid_puissance (TPL), sensor.total_poste_hygiene_puissance (TPL), sensor.total_poste_multimedia_puissance (TPL)
---
- [area]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.genelec_appart_hphc_quotidien_um_hc (NAT), sensor.genelec_appart_hphc_quotidien_um_hp (NAT)
---
- [custom:button-card] Rentabilité HC: sensor.genelec_appart_ratio_hc_quotidien (TPL)
---
- [custom:auto-entities] : sensor.diag_poste_autre_quotidien (TPL), sensor.diag_poste_chauffage_quotidien (TPL), sensor.diag_poste_cuisine_quotidien (TPL), sensor.diag_poste_eclairage_quotidien (TPL), sensor.diag_poste_froid_quotidien (TPL), sensor.diag_poste_hygiene_quotidien (TPL), sensor.diag_poste_multimedia_quotidien (TPL)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [grid]  (aucune entite)
---
- [custom:ring-tile] Conso Hebdo: sensor.genelec_appart_hebdomadaire_um (UM)
---
- [custom:ring-tile] Moy. Watts/J: sensor.genelec_appart_avg_watts_quotidien (TPL)
---
- [custom:ring-tile] Ratio HC %: sensor.genelec_appart_ratio_hc_hebdomadaire (TPL)
---
- [custom:apexcharts-card] : sensor.diag_poste_autre_hebdomadaire (TPL), sensor.diag_poste_chauffage_hebdomadaire (TPL), sensor.diag_poste_cuisine_hebdomadaire (TPL), sensor.diag_poste_eclairage_hebdomadaire (TPL), sensor.diag_poste_froid_hebdomadaire (TPL), sensor.diag_poste_hygiene_hebdomadaire (TPL), sensor.diag_poste_multimedia_hebdomadaire (TPL)
---
- [custom:apexcharts-card] : sensor.genelec_appart_hphc_hebdo_um_hc (NAT), sensor.genelec_appart_hphc_hebdo_um_hp (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [grid]  (aucune entite)
---
- [custom:ring-tile] Conso Mensuel: sensor.genelec_appart_mensuel_um (UM)
---
- [custom:ring-tile] Moy. Watts/J: sensor.genelec_appart_avg_watts_mensuel (TPL)
---
- [custom:ring-tile] Ratio HC %: sensor.genelec_appart_ratio_hc_mensuel (TPL)
---
- [custom:apexcharts-card] : sensor.diag_poste_autre_mensuel (TPL), sensor.diag_poste_chauffage_mensuel (TPL), sensor.diag_poste_cuisine_mensuel (TPL), sensor.diag_poste_eclairage_mensuel (TPL), sensor.diag_poste_froid_mensuel (TPL), sensor.diag_poste_hygiene_mensuel (TPL), sensor.diag_poste_multimedia_mensuel (TPL)
---
- [custom:apexcharts-card] : sensor.genelec_appart_hphc_mensuel_um_hc (NAT), sensor.genelec_appart_hphc_mensuel_um_hp (NAT)
---
- [custom:content-card-linky]  (aucune entite)
---
- [custom:flex-table-card] Historique Linky (J-1 à J-7): sensor.linky_25481620821301_consumption_history (NAT)

#### page_L2C1_energie_temps_reel_2026-06-18.yaml (80 cartes, 102 entites)

- [grid]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Temps Réél: sensor.general_electric_appart_power (NAT)
---
- [entity] Réel: sensor.general_electric_appart_power (NAT)
---
- [markdown]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [conditional] : sensor.total_poste_chauffage_puissance (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Chauffage: sensor.total_poste_chauffage_puissance (TPL)
---
- [entity] : sensor.total_poste_chauffage_puissance (TPL)
---
- [custom:auto-entities] : sensor.clim_bureau_nous_power (NAT), sensor.clim_chambre_nous_power (NAT), sensor.clim_salon_nous_power (NAT), sensor.prise_seche_serviette_salle_de_bain_nous_power (NAT), sensor.prise_soufflant_salle_de_bain_nous_power (NAT), sensor.radiateur_elec_cuisine_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional] : sensor.total_poste_multimedia_puissance (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Multimédia: sensor.total_poste_multimedia_puissance (TPL)
---
- [entity] : sensor.total_poste_multimedia_puissance (TPL)
---
- [custom:auto-entities] : sensor.prise_box_internet_ikea_power (NAT), sensor.prise_bureau_pc_ikea_power (NAT), sensor.prise_pc_s_gege_ikea_power (NAT), sensor.prise_tv_chambre_nous_power (NAT), sensor.prise_tv_salon_ikea_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional] : sensor.total_poste_cuisine_puissance (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Cuisson: sensor.total_poste_cuisine_puissance (TPL)
---
- [entity] : sensor.total_poste_cuisine_puissance (TPL)
---
- [custom:auto-entities] : sensor.four_et_plaque_de_cuisson_power (NAT), sensor.prise_airfryer_ninja_nous_power (NAT), sensor.prise_four_micro_ondes_nous_power (NAT), sensor.prise_petit_dejeune_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional] : sensor.total_poste_froid_puissance (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Froid: sensor.total_poste_froid_puissance (TPL)
---
- [entity] : sensor.total_poste_froid_puissance (TPL)
---
- [custom:auto-entities] : sensor.prise_congelateur_cuisine_nous_power (NAT), sensor.prise_frigo_cuisine_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional] : sensor.total_poste_hygiene_puissance (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Hygiène: sensor.total_poste_hygiene_puissance (TPL)
---
- [entity] : sensor.total_poste_hygiene_puissance (TPL)
---
- [custom:auto-entities] : sensor.prise_bureau_fer_a_repasser_nous_power (NAT), sensor.prise_lave_linge_nous_power (NAT), sensor.prise_lave_vaisselle_nous_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional] : sensor.eclairage_total_group_puissance_tpl (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Lumière: sensor.eclairage_total_group_puissance_tpl (TPL)
---
- [entity] : sensor.eclairage_total_group_puissance_tpl (TPL)
---
- [custom:auto-entities] : sensor.hue_ambiance_lamp_salon_ (NAT), sensor.hue_color_candle_chambre_eric_power (NAT), sensor.hue_color_candle_chambre_gege_power (NAT), sensor.hue_color_candle_salon_1_power (NAT), sensor.hue_play_1_pc_bureau_power (NAT), sensor.hue_play_2_pc_bureau_power (NAT), sensor.hue_play_3_pc_bureau_power (NAT), sensor.hue_white_lamp_bureau_1_power (NAT), sensor.hue_white_lamp_bureau_2_power (NAT), sensor.hue_white_lamp_chambre_ (NAT), sensor.hue_white_lamp_couloir_power (NAT), sensor.hue_white_lamp_cuisine_power (NAT), sensor.hue_white_lamp_entree_power (NAT), sensor.hue_white_lamp_salle_de_bain_power (NAT), sensor.hue_white_lamp_table_power (NAT), sensor.relais_lumiere_sdb_sonoff_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional] : sensor.total_poste_autre_puissance (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [heading] Autres: sensor.total_poste_autre_puissance (TPL)
---
- [entity] : sensor.total_poste_autre_puissance (TPL)
---
- [custom:auto-entities] : sensor.all_standby_power (NAT), sensor.prise_horloge_ikea_power (NAT), sensor.prise_salon_chargeur_nous_power (NAT), sensor.prise_tete_de_lit_chambre_power (NAT)
---
- [custom:bar-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.all_standby_quotidien_um (UM), sensor.four_et_plaque_de_cuisson_quotidien_um (UM), sensor.prise_airfryer_ninja_nous_quotidien_um (UM), sensor.prise_box_internet_ikea_quotidien_um (UM), sensor.prise_bureau_fer_a_repasser_nous_quotidien_um (UM), sensor.prise_bureau_pc_ikea_quotidien_um (UM), sensor.prise_congelateur_cuisine_nous_quotidien_um (UM), sensor.prise_four_micro_ondes_nous_quotidien_um (UM), sensor.prise_frigo_cuisine_nous_quotidien_um (UM), sensor.prise_horloge_ikea_quotidien_um (UM), sensor.prise_lave_linge_nous_quotidien_um (UM), sensor.prise_lave_vaisselle_nous_quotidien_um (UM), sensor.prise_pc_s_gege_ikea_quotidien_um (UM), sensor.prise_petit_dejeune_nous_quotidien_um (UM), sensor.prise_salon_chargeur_nous_quotidien_um (UM), sensor.prise_tete_de_lit_chambre_quotidien_um (UM), sensor.prise_tv_chambre_nous_quotidien_um (UM), sensor.prise_tv_salon_ikea_quotidien_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.all_standby_power (NAT), sensor.four_et_plaque_de_cuisson_power (NAT), sensor.prise_airfryer_ninja_nous_power (NAT), sensor.prise_box_internet_ikea_power (NAT), sensor.prise_bureau_fer_a_repasser_nous_power (NAT), sensor.prise_bureau_pc_ikea_power (NAT), sensor.prise_congelateur_cuisine_nous_power (NAT), sensor.prise_four_micro_ondes_nous_power (NAT), sensor.prise_frigo_cuisine_nous_power (NAT), sensor.prise_horloge_ikea_power (NAT), sensor.prise_lave_linge_nous_power (NAT), sensor.prise_lave_vaisselle_nous_power (NAT), sensor.prise_pc_s_gege_ikea_power (NAT), sensor.prise_petit_dejeune_nous_power (NAT), sensor.prise_salon_chargeur_nous_power (NAT), sensor.prise_tete_de_lit_chambre_power (NAT), sensor.prise_tv_chambre_nous_power (NAT), sensor.prise_tv_salon_ikea_power (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:bubble-card] Sélectionner une pièce : (aucune entite)
---
- [custom:tabbed-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.box_internet_avg_watts_quotidien (TPL), sensor.prise_box_internet_ikea_current (NAT), sensor.prise_box_internet_ikea_power (NAT), sensor.prise_box_internet_ikea_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.horloge_avg_watts_quotidien (TPL), sensor.prise_horloge_ikea_current (NAT), sensor.prise_horloge_ikea_power (NAT), sensor.prise_horloge_ikea_quotidien_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.pc_gege_avg_watts_quotidien (TPL), sensor.prise_pc_s_gege_ikea_current (NAT), sensor.prise_pc_s_gege_ikea_power (NAT), sensor.prise_pc_s_gege_ikea_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.chargeurs_salon_avg_watts_quotidien (TPL), sensor.prise_salon_chargeur_nous_current (NAT), sensor.prise_salon_chargeur_nous_power (NAT), sensor.prise_salon_chargeur_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.prise_tv_salon_ikea_current (NAT), sensor.prise_tv_salon_ikea_power (NAT), sensor.prise_tv_salon_ikea_quotidien_um (UM), sensor.tv_salon_avg_watts_quotidien (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.four_mo_avg_watts_quotidien (TPL), sensor.prise_four_micro_ondes_nous_current (NAT), sensor.prise_four_micro_ondes_nous_power (NAT), sensor.prise_four_micro_ondes_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.petit_dej_avg_watts_quotidien (TPL), sensor.prise_petit_dejeune_nous_current (NAT), sensor.prise_petit_dejeune_nous_power (NAT), sensor.prise_petit_dejeune_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.lave_linge_avg_watts_quotidien (TPL), sensor.prise_lave_linge_nous_current (NAT), sensor.prise_lave_linge_nous_power (NAT), sensor.prise_lave_linge_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.lave_vaisselle_avg_watts_quotidien (TPL), sensor.prise_lave_vaisselle_nous_current (NAT), sensor.prise_lave_vaisselle_nous_power (NAT), sensor.prise_lave_vaisselle_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.airfryer_avg_watts_quotidien (TPL), sensor.prise_airfryer_ninja_nous_current (NAT), sensor.prise_airfryer_ninja_nous_power (NAT), sensor.prise_airfryer_ninja_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.four_et_plaque_de_cuisson_current (NAT), sensor.four_et_plaque_de_cuisson_power (NAT), sensor.four_et_plaque_de_cuisson_quotidien_um (UM), sensor.plaques_cuisson_avg_watts_quotidien (TPL)
---
- [custom:streamline-card] : sensor.frigo_avg_watts_quotidien (TPL), sensor.prise_frigo_cuisine_nous_current (NAT), sensor.prise_frigo_cuisine_nous_power (NAT), sensor.prise_frigo_cuisine_nous_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.congelateur_avg_watts_quotidien (TPL), sensor.prise_congelateur_cuisine_nous_current (NAT), sensor.prise_congelateur_cuisine_nous_power (NAT), sensor.prise_congelateur_cuisine_nous_quotidien_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.pc_bureau_avg_watts_quotidien (TPL), sensor.prise_bureau_pc_ikea_current (NAT), sensor.prise_bureau_pc_ikea_power (NAT), sensor.prise_bureau_pc_ikea_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.fer_repasser_avg_watts_quotidien (TPL), sensor.prise_bureau_fer_a_repasser_nous_current (NAT), sensor.prise_bureau_fer_a_repasser_nous_power (NAT), sensor.prise_bureau_fer_a_repasser_nous_quotidien_um (UM)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.prise_tete_de_lit_chambre_current (NAT), sensor.prise_tete_de_lit_chambre_power (NAT), sensor.prise_tete_de_lit_chambre_quotidien_um (UM), sensor.tetes_lit_avg_watts_quotidien (TPL)
---
- [custom:streamline-card] : sensor.prise_tv_chambre_nous_current (NAT), sensor.prise_tv_chambre_nous_power (NAT), sensor.prise_tv_chambre_nous_quotidien_um (UM), sensor.tv_chambre_avg_watts_quotidien (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.all_standby_avg_watts_quotidien (TPL), sensor.all_standby_current (TPL), sensor.all_standby_power (NAT), sensor.all_standby_quotidien_um (UM)

#### vignette_L2C1_energie_2026-06-18.yaml (1 cartes, 6 entites)

- [custom:button-card] : sensor.genelec_appart_conso_maxi_24h (SEN), sensor.genelec_appart_conso_mini_24h (SEN), sensor.genelec_appart_cout_hc_quotidien (TPL), sensor.genelec_appart_cout_hp_quotidien (TPL), sensor.genelec_appart_cout_total_quotidien (TPL), sensor.general_electric_appart_power (NAT)

### L2C2 - Energie_Clim

*Validée le 2026-05-13*

*104 entites, 180 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 38)
  └─→ UM: P1_UM_AMHQ.yaml (24)
  └─→ TPL: M_04_tendances_th_ext_card.yaml (1)
  └─→ TPL: P1_01_clim_logique_system_autom.yaml (3)
  └─→ TPL: P1_AVG_AMHQ_TOTAL.yaml (1)
  └─→ TPL: P1_AVG_AMHQ_UNITE.yaml (12)
  └─→ TPL: P1_DUT_TOTAL_SDB.yaml (1)
  └─→ TPL: P1_TOTAL_AMHQ.yaml (3)
  └─→ TPL: P1_ui_dashboard.yaml (17)
  └─→ SEN: P1_DUT_clim_chauffage.yaml (4)
        └─→ VIGNETTE L2C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `climate.clim_bureau_rm4_mini` | NAT | (native/UI) |
| `climate.clim_chambre_rm4_mini` | NAT | idem |
| `climate.clim_salon_rm4_mini` | NAT | idem |
| `climate.radiateur_cuisine` | NAT | idem |
| `climate.soufflant_salle_de_bain` | NAT | idem |
| `sensor.clim_bureau_nous_current` | NAT | idem |
| `sensor.clim_bureau_nous_energy` | NAT | idem |
| `sensor.clim_bureau_nous_power` | NAT | idem |
| `sensor.clim_bureau_nous_voltage` | NAT | idem |
| `sensor.clim_chambre_nous_current` | NAT | idem |
| `sensor.clim_chambre_nous_energy` | NAT | idem |
| `sensor.clim_chambre_nous_power` | NAT | idem |
| `sensor.clim_chambre_nous_voltage` | NAT | idem |
| `sensor.clim_salon_nous_current` | NAT | idem |
| `sensor.clim_salon_nous_energy` | NAT | idem |
| `sensor.clim_salon_nous_power` | NAT | idem |
| `sensor.clim_salon_nous_voltage` | NAT | idem |
| `sensor.ete_hiver` | NAT | idem |
| `sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power` | NAT | idem |
| `sensor.prise_seche_serviette_salle_de_bain_nous_current` | NAT | idem |
| `sensor.prise_seche_serviette_salle_de_bain_nous_energy` | NAT | idem |
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | NAT | idem |
| `sensor.prise_seche_serviette_salle_de_bain_nous_voltage` | NAT | idem |
| `sensor.prise_soufflant_salle_de_bain_nous_current` | NAT | idem |
| `sensor.prise_soufflant_salle_de_bain_nous_energy` | NAT | idem |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | NAT | idem |
| `sensor.prise_soufflant_salle_de_bain_nous_voltage` | NAT | idem |
| `sensor.radiateur_elec_cuisine_current` | NAT | idem |
| `sensor.radiateur_elec_cuisine_energy` | NAT | idem |
| `sensor.radiateur_elec_cuisine_power` | NAT | idem |
| `sensor.radiateur_elec_cuisine_voltage` | NAT | idem |
| `sensor.sdb_seche_serviettes_power_status_affichage` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.th_bureau_temperature` | NAT | idem |
| `sensor.th_chambre_temperature` | NAT | idem |
| `sensor.th_cuisine_temperature` | NAT | idem |
| `sensor.th_salle_de_bain_temperature` | NAT | idem |
| `sensor.th_salon_temperature` | NAT | idem |
| `sensor.th_balcon_nord_temperature_trend` | TPL | M_04_tendances_th_ext_card.yaml |
| `sensor.temperature_corrige_chambre` | TPL | P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_delta_affichage` | TPL | idem |
| `sensor.temperature_moyenne_interieure` | TPL | idem |
| `sensor.clim_rad_total_avg_watts_quotidien` | TPL | P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_bureau_avg_watts_mensuel` | TPL | P1_AVG_AMHQ_UNITE.yaml |
| `sensor.clim_bureau_avg_watts_quotidien` | TPL | idem |
| `sensor.clim_chambre_avg_watts_mensuel` | TPL | idem |
| `sensor.clim_chambre_avg_watts_quotidien` | TPL | idem |
| `sensor.clim_salon_avg_watts_mensuel` | TPL | idem |
| `sensor.clim_salon_avg_watts_quotidien` | TPL | idem |
| `sensor.radiateur_elec_cuisine_avg_watts_mensuel` | TPL | idem |
| `sensor.radiateur_elec_cuisine_avg_watts_quotidien` | TPL | idem |
| `sensor.seche_serviette_sdb_avg_watts_mensuel` | TPL | idem |
| `sensor.seche_serviette_sdb_avg_watts_quotidien` | TPL | idem |
| `sensor.soufflant_sdb_avg_watts_mensuel` | TPL | idem |
| `sensor.soufflant_sdb_avg_watts_quotidien` | TPL | idem |
| `sensor.dut_sdb_total` | TPL | P1_DUT_TOTAL_SDB.yaml |
| `sensor.dut_clim_bureau` | SEN | P1_DUT_clim_chauffage.yaml |
| `sensor.dut_clim_chambre` | SEN | idem |
| `sensor.dut_clim_salon` | SEN | idem |
| `sensor.dut_radiateur_cuisine` | SEN | idem |
| `sensor.conso_clim_rad_total` | TPL | P1_TOTAL_AMHQ.yaml |
| `sensor.conso_clim_rad_total_mensuel` | TPL | idem |
| `sensor.conso_clim_rad_total_quotidien` | TPL | idem |
| `sensor.clim_bureau_annuel_um` | UM | P1_UM_AMHQ.yaml |
| `sensor.clim_bureau_hebdomadaire_um` | UM | idem |
| `sensor.clim_bureau_mensuel_um` | UM | idem |
| `sensor.clim_bureau_quotidien_um` | UM | idem |
| `sensor.clim_chambre_annuel_um` | UM | idem |
| `sensor.clim_chambre_hebdomadaire_um` | UM | idem |
| `sensor.clim_chambre_mensuel_um` | UM | idem |
| `sensor.clim_chambre_quotidien_um` | UM | idem |
| `sensor.clim_salon_annuel_um` | UM | idem |
| `sensor.clim_salon_hebdomadaire_um` | UM | idem |
| `sensor.clim_salon_mensuel_um` | UM | idem |
| `sensor.clim_salon_quotidien_um` | UM | idem |
| `sensor.radiateur_elec_cuisine_annuel_um` | UM | idem |
| `sensor.radiateur_elec_cuisine_hebdomadaire_um` | UM | idem |
| `sensor.radiateur_elec_cuisine_mensuel_um` | UM | idem |
| `sensor.radiateur_elec_cuisine_quotidien_um` | UM | idem |
| `sensor.seche_serviette_sdb_annuel_um` | UM | idem |
| `sensor.seche_serviette_sdb_hebdomadaire_um` | UM | idem |
| `sensor.seche_serviette_sdb_mensuel_um` | UM | idem |
| `sensor.seche_serviette_sdb_quotidien_um` | UM | idem |
| `sensor.soufflant_sdb_annuel_um` | UM | idem |
| `sensor.soufflant_sdb_hebdomadaire_um` | UM | idem |
| `sensor.soufflant_sdb_mensuel_um` | UM | idem |
| `sensor.soufflant_sdb_quotidien_um` | UM | idem |
| `sensor.bureau_power_status` | TPL | P1_ui_dashboard.yaml |
| `sensor.bureau_power_status_affichage` | TPL | idem |
| `sensor.chambre_power_status` | TPL | idem |
| `sensor.chambre_power_status_affichage` | TPL | idem |
| `sensor.clim_bureau_etat` | TPL | idem |
| `sensor.clim_chambre_etat` | TPL | idem |
| `sensor.clim_salon_etat` | TPL | idem |
| `sensor.cuisine_power_status` | TPL | idem |
| `sensor.cuisine_power_status_affichage` | TPL | idem |
| `sensor.radiateur_cuisine_etat` | TPL | idem |
| `sensor.salon_power_status` | TPL | idem |
| `sensor.salon_power_status_affichage` | TPL | idem |
| `sensor.sdb_power_status_affichage` | TPL | idem |
| `sensor.sdb_seche_serviette_etat` | TPL | idem |
| `sensor.sdb_seche_serviette_power_status` | TPL | idem |
| `sensor.sdb_soufflant_etat` | TPL | idem |
| `sensor.sdb_soufflant_power_status` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L2C2_energie_clim_2026-07-14.yaml` | ✅ |
| `vignette_L2C2_energie_clim_2026-05-13.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L2C2_energie_clim_2026-07-14.yaml (179 cartes, 104 entites)

- [grid]  (aucune entite)
---
- [heading] ENERGIE (C)LIM / (R)ADIATEUR: sensor.temperature_delta_affichage (TPL)
---
- [entity] : sensor.temperature_delta_affichage (TPL)
---
- [conditional] : sensor.bureau_power_status_affichage (TPL), sensor.chambre_power_status_affichage (TPL), sensor.cuisine_power_status_affichage (TPL), sensor.salon_power_status_affichage (TPL), sensor.sdb_power_status_affichage (TPL), sensor.sdb_seche_serviettes_power_status_affichage (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [template] : sensor.dut_clim_salon (SEN), sensor.ete_hiver (NAT)
---
- [template] : sensor.dut_radiateur_cuisine (SEN)
---
- [template] : sensor.dut_clim_bureau (SEN), sensor.ete_hiver (NAT)
---
- [template] : sensor.dut_clim_chambre (SEN), sensor.ete_hiver (NAT)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [conditional] : sensor.salon_power_status (TPL)
---
- [template] : sensor.clim_salon_etat (TPL)
---
- [conditional] : sensor.cuisine_power_status (TPL)
---
- [template] : sensor.radiateur_cuisine_etat (TPL)
---
- [conditional] : sensor.bureau_power_status (TPL)
---
- [template] : sensor.clim_bureau_etat (TPL)
---
- [conditional] : sensor.sdb_soufflant_power_status (TPL)
---
- [template] : sensor.sdb_soufflant_etat (TPL)
---
- [conditional] : sensor.sdb_seche_serviette_power_status (TPL)
---
- [template] : sensor.sdb_seche_serviette_etat (TPL)
---
- [conditional] : sensor.chambre_power_status (TPL)
---
- [template] : sensor.clim_chambre_etat (TPL)
---
- [vertical-stack]  (aucune entite)
---
- [custom:auto-entities] : sensor.conso_clim_rad_total (TPL)
---
- [custom:bar-card]  (aucune entite)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.clim_bureau_quotidien_um (UM), sensor.clim_chambre_quotidien_um (UM), sensor.clim_salon_quotidien_um (UM), sensor.radiateur_elec_cuisine_quotidien_um (UM), sensor.seche_serviette_sdb_quotidien_um (UM), sensor.soufflant_sdb_quotidien_um (UM)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.clim_bureau_mensuel_um (UM), sensor.clim_chambre_mensuel_um (UM), sensor.clim_salon_mensuel_um (UM), sensor.radiateur_elec_cuisine_mensuel_um (UM), sensor.seche_serviette_sdb_mensuel_um (UM), sensor.soufflant_sdb_mensuel_um (UM)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] Tendances (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.th_balcon_nord_temperature (NAT), sensor.th_balcon_nord_temperature_trend (TPL)
---
- [custom:mini-graph-card] : sensor.th_balcon_nord_temperature (NAT)
---
- [custom:apexcharts-card] : sensor.conso_clim_rad_total_mensuel (TPL), sensor.conso_clim_rad_total_quotidien (TPL), sensor.temperature_moyenne_interieure (TPL), sensor.th_balcon_nord_temperature (NAT)
---
- [column] Conso. Instan.: sensor.conso_clim_rad_total (TPL)
---
- [line] Moy.depuis Minuit: sensor.clim_rad_total_avg_watts_quotidien (TPL)
---
- [custom:apexcharts-card] : sensor.dut_clim_bureau (SEN), sensor.dut_clim_chambre (SEN), sensor.dut_clim_salon (SEN), sensor.dut_radiateur_cuisine (SEN), sensor.dut_sdb_total (TPL)
---
- [area] Temp. Ext.: sensor.th_balcon_nord_temperature (NAT)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] SALON: climate.clim_salon_rm4_mini (NAT), sensor.th_salon_temperature (NAT)
---
- [entity] Réglé à: climate.clim_salon_rm4_mini (NAT)
---
- [entity] Salon: sensor.th_salon_temperature (NAT)
---
- [custom:bubble-card] : climate.clim_salon_rm4_mini (NAT)
---
- [custom:streamline-card] : sensor.clim_salon_nous_voltage (NAT)
---
- [custom:streamline-card] : sensor.clim_salon_nous_current (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:streamline-card] : sensor.clim_salon_avg_watts_quotidien (TPL), sensor.clim_salon_nous_current (NAT), sensor.clim_salon_nous_power (NAT), sensor.clim_salon_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.clim_salon_avg_watts_mensuel (TPL), sensor.clim_salon_mensuel_um (UM), sensor.clim_salon_nous_energy (NAT), sensor.th_balcon_nord_temperature (NAT)
---
- [custom:streamline-card] : sensor.dut_clim_salon (SEN)
---
- [heading] : sensor.clim_salon_annuel_um (UM), sensor.clim_salon_hebdomadaire_um (UM), sensor.clim_salon_mensuel_um (UM), sensor.clim_salon_quotidien_um (UM)
---
- [entity] Q: sensor.clim_salon_quotidien_um (UM)
---
- [entity] H: sensor.clim_salon_hebdomadaire_um (UM)
---
- [entity] M: sensor.clim_salon_mensuel_um (UM)
---
- [entity] A: sensor.clim_salon_annuel_um (UM)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] CUISINE  (RADIATEUR): climate.radiateur_cuisine (NAT), sensor.th_cuisine_temperature (NAT)
---
- [entity] Réglé à: climate.radiateur_cuisine (NAT)
---
- [entity] Cuisine: sensor.th_cuisine_temperature (NAT)
---
- [custom:bubble-card] Radiateur de la Cuisine: climate.radiateur_cuisine (NAT)
---
- [custom:streamline-card] : sensor.radiateur_elec_cuisine_voltage (NAT)
---
- [custom:streamline-card] : sensor.radiateur_elec_cuisine_current (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:streamline-card] : sensor.radiateur_elec_cuisine_avg_watts_quotidien (TPL), sensor.radiateur_elec_cuisine_current (NAT), sensor.radiateur_elec_cuisine_power (NAT), sensor.radiateur_elec_cuisine_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.radiateur_elec_cuisine_avg_watts_mensuel (TPL), sensor.radiateur_elec_cuisine_energy (NAT), sensor.radiateur_elec_cuisine_mensuel_um (UM), sensor.th_balcon_nord_temperature (NAT)
---
- [custom:streamline-card] : sensor.dut_radiateur_cuisine (SEN)
---
- [heading] : sensor.radiateur_elec_cuisine_annuel_um (UM), sensor.radiateur_elec_cuisine_hebdomadaire_um (UM), sensor.radiateur_elec_cuisine_mensuel_um (UM), sensor.radiateur_elec_cuisine_quotidien_um (UM)
---
- [entity] Q: sensor.radiateur_elec_cuisine_quotidien_um (UM)
---
- [entity] H: sensor.radiateur_elec_cuisine_hebdomadaire_um (UM)
---
- [entity] M: sensor.radiateur_elec_cuisine_mensuel_um (UM)
---
- [entity] A: sensor.radiateur_elec_cuisine_annuel_um (UM)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] BUREAU: climate.clim_bureau_rm4_mini (NAT), sensor.th_bureau_temperature (NAT)
---
- [entity] Réglé à: climate.clim_bureau_rm4_mini (NAT)
---
- [entity] Bureau: sensor.th_bureau_temperature (NAT)
---
- [custom:bubble-card] : climate.clim_bureau_rm4_mini (NAT)
---
- [custom:streamline-card] : sensor.clim_bureau_nous_voltage (NAT)
---
- [custom:streamline-card] : sensor.clim_bureau_nous_current (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:streamline-card] : sensor.clim_bureau_avg_watts_quotidien (TPL), sensor.clim_bureau_nous_current (NAT), sensor.clim_bureau_nous_power (NAT), sensor.clim_bureau_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.clim_bureau_avg_watts_mensuel (TPL), sensor.clim_bureau_mensuel_um (UM), sensor.clim_bureau_nous_energy (NAT), sensor.th_balcon_nord_temperature (NAT)
---
- [custom:streamline-card] : sensor.dut_clim_bureau (SEN)
---
- [heading] : sensor.clim_bureau_annuel_um (UM), sensor.clim_bureau_hebdomadaire_um (UM), sensor.clim_bureau_mensuel_um (UM), sensor.clim_bureau_quotidien_um (UM)
---
- [entity] Q: sensor.clim_bureau_quotidien_um (UM)
---
- [entity] H: sensor.clim_bureau_hebdomadaire_um (UM)
---
- [entity] M: sensor.clim_bureau_mensuel_um (UM)
---
- [entity] A: sensor.clim_bureau_annuel_um (UM)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] SALLE DE BAIN: climate.soufflant_salle_de_bain (NAT), sensor.th_salle_de_bain_temperature (NAT)
---
- [entity] Réglé à: climate.soufflant_salle_de_bain (NAT)
---
- [entity] : sensor.th_salle_de_bain_temperature (NAT)
---
- [area]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:bubble-card] Soufflant de la Salle de Bain: climate.soufflant_salle_de_bain (NAT)
---
- [custom:streamline-card] : sensor.prise_soufflant_salle_de_bain_nous_voltage (NAT)
---
- [custom:streamline-card] : sensor.prise_soufflant_salle_de_bain_nous_current (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:streamline-card] : sensor.prise_soufflant_salle_de_bain_nous_current (NAT), sensor.prise_soufflant_salle_de_bain_nous_power (NAT), sensor.soufflant_sdb_avg_watts_quotidien (TPL), sensor.soufflant_sdb_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.prise_soufflant_salle_de_bain_nous_energy (NAT), sensor.soufflant_sdb_avg_watts_mensuel (TPL), sensor.soufflant_sdb_mensuel_um (UM), sensor.th_balcon_nord_temperature (NAT)
---
- [custom:streamline-card] : sensor.dut_sdb_total (TPL)
---
- [heading] : sensor.soufflant_sdb_annuel_um (UM), sensor.soufflant_sdb_hebdomadaire_um (UM), sensor.soufflant_sdb_mensuel_um (UM), sensor.soufflant_sdb_quotidien_um (UM)
---
- [entity] Q: sensor.soufflant_sdb_quotidien_um (UM)
---
- [entity] H: sensor.soufflant_sdb_hebdomadaire_um (UM)
---
- [entity] M: sensor.soufflant_sdb_mensuel_um (UM)
---
- [entity] A: sensor.soufflant_sdb_annuel_um (UM)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:streamline-card] : sensor.prise_seche_serviette_salle_de_bain_nous_voltage (NAT)
---
- [custom:streamline-card] : sensor.prise_seche_serviette_salle_de_bain_nous_current (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:streamline-card] : sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power (NAT), sensor.prise_seche_serviette_salle_de_bain_nous_current (NAT), sensor.prise_seche_serviette_salle_de_bain_nous_power (NAT), sensor.seche_serviette_sdb_avg_watts_quotidien (TPL), sensor.seche_serviette_sdb_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.prise_seche_serviette_salle_de_bain_nous_energy (NAT), sensor.seche_serviette_sdb_avg_watts_mensuel (TPL), sensor.seche_serviette_sdb_mensuel_um (UM), sensor.th_balcon_nord_temperature (NAT)
---
- [custom:streamline-card] : sensor.dut_sdb_total (TPL)
---
- [heading] : sensor.seche_serviette_sdb_annuel_um (UM), sensor.seche_serviette_sdb_hebdomadaire_um (UM), sensor.seche_serviette_sdb_mensuel_um (UM), sensor.seche_serviette_sdb_quotidien_um (UM)
---
- [entity] Q: sensor.seche_serviette_sdb_quotidien_um (UM)
---
- [entity] H: sensor.seche_serviette_sdb_hebdomadaire_um (UM)
---
- [entity] M: sensor.seche_serviette_sdb_mensuel_um (UM)
---
- [entity] A: sensor.seche_serviette_sdb_annuel_um (UM)
---
- [conditional]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [heading] CHAMBRE: sensor.temperature_corrige_chambre (TPL), sensor.th_chambre_temperature (NAT)
---
- [entity] Réglé à: sensor.temperature_corrige_chambre (TPL)
---
- [entity] Chambre: sensor.th_chambre_temperature (NAT)
---
- [custom:bubble-card] : climate.clim_chambre_rm4_mini (NAT)
---
- [custom:streamline-card] : sensor.clim_chambre_nous_voltage (NAT)
---
- [custom:streamline-card] : sensor.clim_chambre_nous_current (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:streamline-card] : sensor.clim_chambre_avg_watts_quotidien (TPL), sensor.clim_chambre_nous_current (NAT), sensor.clim_chambre_nous_power (NAT), sensor.clim_chambre_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.clim_chambre_avg_watts_mensuel (TPL), sensor.clim_chambre_mensuel_um (UM), sensor.clim_chambre_nous_energy (NAT), sensor.th_balcon_nord_temperature (NAT)
---
- [custom:streamline-card] : sensor.dut_clim_chambre (SEN)
---
- [heading] : sensor.clim_chambre_annuel_um (UM), sensor.clim_chambre_hebdomadaire_um (UM), sensor.clim_chambre_mensuel_um (UM), sensor.clim_chambre_quotidien_um (UM)
---
- [entity] Q: sensor.clim_chambre_quotidien_um (UM)
---
- [entity] H: sensor.clim_chambre_hebdomadaire_um (UM)
---
- [entity] M: sensor.clim_chambre_mensuel_um (UM)
---
- [entity] A: sensor.clim_chambre_annuel_um (UM)
---
- [custom:bubble-card] CALCUL DU DELTA Intérieur <-> Extérieur (aucune entite)
---
- [custom:streamline-card]  (aucune entite)

#### vignette_L2C2_energie_clim_2026-05-13.yaml (1 cartes, 31 entites)

- [custom:button-card] : climate.clim_bureau_rm4_mini (NAT), climate.clim_chambre_rm4_mini (NAT), climate.clim_salon_rm4_mini (NAT), climate.radiateur_cuisine (NAT), climate.soufflant_salle_de_bain (NAT), sensor.bureau_power_status (TPL), sensor.chambre_power_status (TPL), sensor.clim_bureau_etat (TPL), sensor.clim_bureau_mensuel_um (UM), sensor.clim_bureau_quotidien_um (UM), sensor.clim_chambre_etat (TPL), sensor.clim_chambre_mensuel_um (UM), sensor.clim_chambre_quotidien_um (UM), sensor.clim_salon_etat (TPL), sensor.clim_salon_mensuel_um (UM), sensor.clim_salon_quotidien_um (UM), sensor.conso_clim_rad_total_mensuel (TPL), sensor.conso_clim_rad_total_quotidien (TPL), sensor.cuisine_power_status (TPL), sensor.radiateur_cuisine_etat (TPL), sensor.radiateur_elec_cuisine_mensuel_um (UM), sensor.radiateur_elec_cuisine_quotidien_um (UM), sensor.salon_power_status (TPL), sensor.sdb_seche_serviette_etat (TPL), sensor.sdb_seche_serviette_power_status (TPL), sensor.sdb_soufflant_etat (TPL), sensor.sdb_soufflant_power_status (TPL), sensor.seche_serviette_sdb_mensuel_um (UM), sensor.seche_serviette_sdb_quotidien_um (UM), sensor.soufflant_sdb_mensuel_um (UM), sensor.soufflant_sdb_quotidien_um (UM)

### L2C3 - Energie_Eclairage

*Validée le 2026-04-29 - Migration TPL kWh complète (_um → _um_kwh_tpl) | Dashboard archivé le 2026-05-13 | 2026-06-14 state_class total_increasing → total (× 116 sensors)*

> Somme des 19 `{slug}_power` (PowerCalc). Consommé par `total_pour_les_7_postes.yaml` (Pôle 6) → L2C1.

*85 entites, 79 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 10)
  └─→ TPL: P3_AVG_AMHQ_2_ZONE.yaml (5)
  └─→ TPL: P3_TPL_AMHQ_1_UNITE.yaml (38)
  └─→ TPL: P3_TPL_AMHQ_2_ZONE.yaml (24)
  └─→ TPL: P3_TPL_AMHQ_3_TOTAL.yaml (2)
  └─→ TPL: P3_etats_status.yaml (6)
        └─→ VIGNETTE L2C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `light.bureau` | NAT | (native/UI) |
| `light.chambre` | NAT | idem |
| `light.couloir` | NAT | idem |
| `light.cuisine` | NAT | idem |
| `light.entree` | NAT | idem |
| `light.hue_white_lamp_salle_de_bain` | NAT | idem |
| `light.lit` | NAT | idem |
| `light.salon` | NAT | idem |
| `light.table` | NAT | idem |
| `switch.relais_lumiere_sdb_sonoff` | NAT | idem |
| `sensor.eclairage_appart_3_avg_watts_mensuel` | TPL | P3_AVG_AMHQ_2_ZONE.yaml |
| `sensor.eclairage_bureau_5_avg_watts_mensuel` | TPL | idem |
| `sensor.eclairage_chambre_4_avg_watts_mensuel` | TPL | idem |
| `sensor.eclairage_salon_5_avg_watts_mensuel` | TPL | idem |
| `sensor.eclairage_sdb_2_avg_watts_mensuel` | TPL | idem |
| `sensor.hue_ambiance_lamp_salon_1_mensuel_um_kwh_tpl` | TPL | P3_TPL_AMHQ_1_UNITE.yaml |
| `sensor.hue_ambiance_lamp_salon_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_ambiance_lamp_salon_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_ambiance_lamp_salon_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_ambiance_lamp_salon_3_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_ambiance_lamp_salon_3_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_color_candle_chambre_eric_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_color_candle_chambre_eric_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_color_candle_chambre_gege_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_color_candle_chambre_gege_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_color_candle_salon_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_color_candle_salon_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_play_1_pc_bureau_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_play_1_pc_bureau_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_play_2_pc_bureau_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_play_2_pc_bureau_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_play_3_pc_bureau_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_play_3_pc_bureau_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_bureau_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_bureau_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_bureau_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_bureau_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_chambre_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_chambre_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_chambre_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_chambre_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_couloir_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_couloir_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_cuisine_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_cuisine_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_entree_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_entree_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_salle_de_bain_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_salle_de_bain_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_table_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.hue_white_lamp_table_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.relais_lumiere_sdb_sonoff_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.relais_lumiere_sdb_sonoff_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_appart_2_mensuel_um_kwh_tpl` | TPL | P3_TPL_AMHQ_2_ZONE.yaml |
| `sensor.eclairage_appart_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_appart_3_annuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_appart_3_hebdomadaire_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_appart_3_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_appart_3_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_annuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_hebdomadaire_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_annuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_hebdomadaire_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_salon_5_annuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_salon_5_hebdomadaire_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_salon_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_salon_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_annuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_hebdomadaire_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | TPL | P3_TPL_AMHQ_3_TOTAL.yaml |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | TPL | idem |
| `sensor.lumiere_appartement_etat` | TPL | P3_etats_status.yaml |
| `sensor.lumiere_bureau_etat` | TPL | idem |
| `sensor.lumiere_chambre_etat` | TPL | idem |
| `sensor.lumiere_cuisine_etat` | TPL | idem |
| `sensor.lumiere_salle_de_bain_etat` | TPL | idem |
| `sensor.lumiere_salon_etat` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L2C3_energie_eclairage_2026-05-13.yaml` | ✅ |
| `vignette_L2C3_energie_eclairage_2026-05-13.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L2C3_energie_eclairage_2026-05-13.yaml (78 cartes, 73 entites)

- [grid]  (aucune entite)
---
- [heading] LAMPES (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [heading] SALON: light.salon (NAT), light.table (NAT)
---
- [entity] : light.salon (NAT)
---
- [entity] : light.table (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.hue_ambiance_lamp_salon_1_quotidien_um_kwh_tpl (TPL), sensor.hue_ambiance_lamp_salon_2_quotidien_um_kwh_tpl (TPL), sensor.hue_ambiance_lamp_salon_3_quotidien_um_kwh_tpl (TPL), sensor.hue_color_candle_salon_1_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_table_quotidien_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card] : sensor.hue_ambiance_lamp_salon_1_mensuel_um_kwh_tpl (TPL), sensor.hue_ambiance_lamp_salon_2_mensuel_um_kwh_tpl (TPL), sensor.hue_ambiance_lamp_salon_3_mensuel_um_kwh_tpl (TPL), sensor.hue_color_candle_salon_1_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_table_mensuel_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Conso. par jours: sensor.eclairage_salon_5_mensuel_um_kwh_tpl (TPL)
---
- [line] Moy. 1er du mois: sensor.eclairage_salon_5_avg_watts_mensuel (TPL)
---
- [heading] : sensor.eclairage_salon_5_annuel_um_kwh_tpl (TPL), sensor.eclairage_salon_5_hebdomadaire_um_kwh_tpl (TPL), sensor.eclairage_salon_5_mensuel_um_kwh_tpl (TPL), sensor.eclairage_salon_5_quotidien_um_kwh_tpl (TPL)
---
- [entity] Q: sensor.eclairage_salon_5_quotidien_um_kwh_tpl (TPL)
---
- [entity] H: sensor.eclairage_salon_5_hebdomadaire_um_kwh_tpl (TPL)
---
- [entity] M: sensor.eclairage_salon_5_mensuel_um_kwh_tpl (TPL)
---
- [entity] A: sensor.eclairage_salon_5_annuel_um_kwh_tpl (TPL)
---
- [custom:button-card]  (aucune entite)
---
- [heading] ENTREE - CUISINE - COULOIR: light.couloir (NAT), light.cuisine (NAT), light.entree (NAT)
---
- [entity] : light.entree (NAT)
---
- [entity] : light.cuisine (NAT)
---
- [entity] : light.couloir (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.hue_white_lamp_couloir_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_cuisine_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_entree_quotidien_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card] : sensor.hue_white_lamp_couloir_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_cuisine_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_entree_mensuel_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Conso. par jours: sensor.eclairage_appart_3_mensuel_um_kwh_tpl (TPL)
---
- [line] Moy. 1er du mois: sensor.eclairage_appart_3_avg_watts_mensuel (TPL)
---
- [heading] : sensor.eclairage_appart_3_annuel_um_kwh_tpl (TPL), sensor.eclairage_appart_3_hebdomadaire_um_kwh_tpl (TPL), sensor.eclairage_appart_3_mensuel_um_kwh_tpl (TPL), sensor.eclairage_appart_3_quotidien_um_kwh_tpl (TPL)
---
- [entity] Q: sensor.eclairage_appart_3_quotidien_um_kwh_tpl (TPL)
---
- [entity] H: sensor.eclairage_appart_3_hebdomadaire_um_kwh_tpl (TPL)
---
- [entity] M: sensor.eclairage_appart_3_mensuel_um_kwh_tpl (TPL)
---
- [entity] A: sensor.eclairage_appart_3_annuel_um_kwh_tpl (TPL)
---
- [custom:button-card]  (aucune entite)
---
- [heading] BUREAU: light.bureau (NAT)
---
- [entity] Pc: light.bureau (NAT)
---
- [entity] Bureau: light.bureau (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.hue_play_1_pc_bureau_quotidien_um_kwh_tpl (TPL), sensor.hue_play_2_pc_bureau_quotidien_um_kwh_tpl (TPL), sensor.hue_play_3_pc_bureau_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_bureau_1_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_bureau_2_quotidien_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card] : sensor.hue_play_1_pc_bureau_mensuel_um_kwh_tpl (TPL), sensor.hue_play_2_pc_bureau_mensuel_um_kwh_tpl (TPL), sensor.hue_play_3_pc_bureau_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_bureau_1_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_bureau_2_mensuel_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Conso. par jours: sensor.eclairage_bureau_5_mensuel_um_kwh_tpl (TPL)
---
- [line] Moy. 1er du mois: sensor.eclairage_bureau_5_avg_watts_mensuel (TPL)
---
- [heading] : sensor.eclairage_bureau_5_annuel_um_kwh_tpl (TPL), sensor.eclairage_bureau_5_hebdomadaire_um_kwh_tpl (TPL), sensor.eclairage_bureau_5_mensuel_um_kwh_tpl (TPL), sensor.eclairage_bureau_5_quotidien_um_kwh_tpl (TPL)
---
- [entity] Q: sensor.eclairage_bureau_5_quotidien_um_kwh_tpl (TPL)
---
- [entity] H: sensor.eclairage_bureau_5_hebdomadaire_um_kwh_tpl (TPL)
---
- [entity] M: sensor.eclairage_bureau_5_mensuel_um_kwh_tpl (TPL)
---
- [entity] A: sensor.eclairage_bureau_5_annuel_um_kwh_tpl (TPL)
---
- [custom:button-card]  (aucune entite)
---
- [heading] SALLE DE BAIN: light.hue_white_lamp_salle_de_bain (NAT), switch.relais_lumiere_sdb_sonoff (NAT)
---
- [entity] : light.hue_white_lamp_salle_de_bain (NAT)
---
- [entity] : switch.relais_lumiere_sdb_sonoff (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.hue_white_lamp_salle_de_bain_quotidien_um_kwh_tpl (TPL), sensor.relais_lumiere_sdb_sonoff_quotidien_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card] : sensor.hue_white_lamp_salle_de_bain_mensuel_um_kwh_tpl (TPL), sensor.relais_lumiere_sdb_sonoff_mensuel_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Conso. par jours: sensor.eclairage_sdb_2_mensuel_um_kwh_tpl (TPL)
---
- [line] Moy. 1er du mois: sensor.eclairage_sdb_2_avg_watts_mensuel (TPL)
---
- [heading] : sensor.eclairage_sdb_2_annuel_um_kwh_tpl (TPL), sensor.eclairage_sdb_2_hebdomadaire_um_kwh_tpl (TPL), sensor.eclairage_sdb_2_mensuel_um_kwh_tpl (TPL), sensor.eclairage_sdb_2_quotidien_um_kwh_tpl (TPL)
---
- [entity] Q: sensor.eclairage_sdb_2_quotidien_um_kwh_tpl (TPL)
---
- [entity] H: sensor.eclairage_sdb_2_hebdomadaire_um_kwh_tpl (TPL)
---
- [entity] M: sensor.eclairage_sdb_2_mensuel_um_kwh_tpl (TPL)
---
- [entity] A: sensor.eclairage_sdb_2_annuel_um_kwh_tpl (TPL)
---
- [custom:button-card]  (aucune entite)
---
- [heading] CHAMBRE: light.chambre (NAT), light.lit (NAT)
---
- [entity] : light.chambre (NAT)
---
- [entity] : light.lit (NAT)
---
- [custom:tabbed-card]  (aucune entite)
---
- [custom:apexcharts-card] : sensor.hue_color_candle_chambre_eric_quotidien_um_kwh_tpl (TPL), sensor.hue_color_candle_chambre_gege_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_chambre_1_quotidien_um_kwh_tpl (TPL), sensor.hue_white_lamp_chambre_2_quotidien_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card] : sensor.hue_color_candle_chambre_eric_mensuel_um_kwh_tpl (TPL), sensor.hue_color_candle_chambre_gege_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_chambre_1_mensuel_um_kwh_tpl (TPL), sensor.hue_white_lamp_chambre_2_mensuel_um_kwh_tpl (TPL)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Conso. par jours: sensor.eclairage_chambre_4_mensuel_um_kwh_tpl (TPL)
---
- [line] Moy. 1er du mois: sensor.eclairage_chambre_4_avg_watts_mensuel (TPL)
---
- [heading] : sensor.eclairage_chambre_4_annuel_um_kwh_tpl (TPL), sensor.eclairage_chambre_4_hebdomadaire_um_kwh_tpl (TPL), sensor.eclairage_chambre_4_mensuel_um_kwh_tpl (TPL), sensor.eclairage_chambre_4_quotidien_um_kwh_tpl (TPL)
---
- [entity] Q: sensor.eclairage_chambre_4_quotidien_um_kwh_tpl (TPL)
---
- [entity] H: sensor.eclairage_chambre_4_hebdomadaire_um_kwh_tpl (TPL)
---
- [entity] M: sensor.eclairage_chambre_4_mensuel_um_kwh_tpl (TPL)
---
- [entity] A: sensor.eclairage_chambre_4_annuel_um_kwh_tpl (TPL)

#### vignette_L2C3_energie_eclairage_2026-05-13.yaml (1 cartes, 20 entites)

- [custom:button-card] : sensor.eclairage_appart_2_mensuel_um_kwh_tpl (TPL), sensor.eclairage_appart_2_quotidien_um_kwh_tpl (TPL), sensor.eclairage_bureau_5_mensuel_um_kwh_tpl (TPL), sensor.eclairage_bureau_5_quotidien_um_kwh_tpl (TPL), sensor.eclairage_chambre_4_mensuel_um_kwh_tpl (TPL), sensor.eclairage_chambre_4_quotidien_um_kwh_tpl (TPL), sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl (TPL), sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl (TPL), sensor.eclairage_salon_5_mensuel_um_kwh_tpl (TPL), sensor.eclairage_salon_5_quotidien_um_kwh_tpl (TPL), sensor.eclairage_sdb_2_mensuel_um_kwh_tpl (TPL), sensor.eclairage_sdb_2_quotidien_um_kwh_tpl (TPL), sensor.eclairage_total_unit_mensuel_kwh_tpl (TPL), sensor.eclairage_total_unit_quotidien_kwh_tpl (TPL), sensor.lumiere_appartement_etat (TPL), sensor.lumiere_bureau_etat (TPL), sensor.lumiere_chambre_etat (TPL), sensor.lumiere_cuisine_etat (TPL), sensor.lumiere_salle_de_bain_etat (TPL), sensor.lumiere_salon_etat (TPL)

### L3C1 - Commandes_Eclairage

*Validée le 2026-05-04 | Dashboard archivé le 2026-05-13*

*44 entites, 85 cartes, 3 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 30)
  └─→ TPL: P3_etats_status.yaml (14)
        └─→ VIGNETTE L3C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `cover.store_bureau` | NAT | (native/UI) |
| `cover.store_salon` | NAT | idem |
| `light.bureau` | NAT | idem |
| `light.chambre` | NAT | idem |
| `light.couloir` | NAT | idem |
| `light.cuisine` | NAT | idem |
| `light.entree` | NAT | idem |
| `light.hue_color_candle_chambre_eric` | NAT | idem |
| `light.hue_color_candle_chambre_gege` | NAT | idem |
| `light.hue_play_1_pc_bureau` | NAT | idem |
| `light.hue_play_2_pc_bureau` | NAT | idem |
| `light.hue_play_3_pc_bureau` | NAT | idem |
| `light.hue_white_lamp_bureau_1` | NAT | idem |
| `light.hue_white_lamp_bureau_2` | NAT | idem |
| `light.hue_white_lamp_salle_de_bain` | NAT | idem |
| `light.lit` | NAT | idem |
| `light.moniteur_pc` | NAT | idem |
| `light.salon` | NAT | idem |
| `light.table` | NAT | idem |
| `light.zone_eric` | NAT | idem |
| `light.zone_gege` | NAT | idem |
| `sensor.plug_power` | NAT | idem |
| `sensor.th_bureau_temperature` | NAT | idem |
| `sensor.th_chambre_temperature` | NAT | idem |
| `sensor.th_cuisine_temperature` | NAT | idem |
| `sensor.th_salle_de_bain_temperature` | NAT | idem |
| `sensor.th_salon_temperature` | NAT | idem |
| `switch.ecran_p_c_3_play_hue` | NAT | idem |
| `switch.prise_tete_de_lit_chambre` | NAT | idem |
| `switch.relais_lumiere_sdb_sonoff` | NAT | idem |
| `sensor.bureau_etat` | TPL | P3_etats_status.yaml |
| `sensor.chambre_etat` | TPL | idem |
| `sensor.chambre_nb_allumes` | TPL | idem |
| `sensor.lumiere_appartement_etat` | TPL | idem |
| `sensor.lumiere_bureau_etat` | TPL | idem |
| `sensor.lumiere_chambre_etat` | TPL | idem |
| `sensor.lumiere_couloir_etat` | TPL | idem |
| `sensor.lumiere_cuisine_etat` | TPL | idem |
| `sensor.lumiere_ecran_etat` | TPL | idem |
| `sensor.lumiere_entree_etat` | TPL | idem |
| `sensor.lumiere_salle_de_bain_etat` | TPL | idem |
| `sensor.lumiere_salon_etat` | TPL | idem |
| `sensor.lumiere_table_etat` | TPL | idem |
| `sensor.lumiere_tete_de_lit_etat` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L3C1_eclairage_droite_2026-05-22.yaml` | ✅ |
| `page_L3C1_eclairage_gauche_2026-05-13.yaml` | ✅ |
| `vignette_L3C1_eclairage_2026-05-13.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L3C1_eclairage_droite_2026-05-22.yaml (65 cartes, 28 entites)

- [grid]  (aucune entite)
---
- [heading] LUMIERES (aucune entite)
---
- [heading] Bureau: cover.store_bureau (NAT), sensor.lumiere_bureau_etat (TPL), sensor.lumiere_ecran_etat (TPL), sensor.th_bureau_temperature (NAT)
---
- [entity] : sensor.th_bureau_temperature (NAT)
---
- [entity] : sensor.lumiere_bureau_etat (TPL)
---
- [entity] : sensor.lumiere_ecran_etat (TPL)
---
- [entity] : cover.store_bureau (NAT)
---
- [custom:vertical-stack-in-card] : sensor.lumiere_bureau_etat (TPL)
---
- [custom:mushroom-entity-card] Bureau: light.hue_white_lamp_bureau_1 (NAT), light.hue_white_lamp_bureau_2 (NAT), sensor.lumiere_bureau_etat (TPL)
---
- [custom:mushroom-chips-card] : sensor.lumiere_bureau_etat (TPL)
---
- [template] : sensor.lumiere_bureau_etat (TPL)
---
- [conditional] : switch.ecran_p_c_3_play_hue (NAT)
---
- [custom:vertical-stack-in-card] : light.moniteur_pc (NAT)
---
- [custom:mushroom-entity-card] Ecran: light.hue_play_1_pc_bureau (NAT), light.hue_play_2_pc_bureau (NAT), light.hue_play_3_pc_bureau (NAT), light.moniteur_pc (NAT), sensor.lumiere_ecran_etat (TPL), sensor.plug_power (NAT)
---
- [custom:mushroom-chips-card] : light.moniteur_pc (NAT), sensor.lumiere_ecran_etat (TPL)
---
- [template] : sensor.lumiere_ecran_etat (TPL)
---
- [heading] Salle de Bain: light.hue_white_lamp_salle_de_bain (NAT), sensor.th_salle_de_bain_temperature (NAT), switch.relais_lumiere_sdb_sonoff (NAT)
---
- [entity] : sensor.th_salle_de_bain_temperature (NAT)
---
- [entity] : light.hue_white_lamp_salle_de_bain (NAT)
---
- [entity] : switch.relais_lumiere_sdb_sonoff (NAT)
---
- [custom:mushroom-entity-card] Salle de Bain: light.hue_white_lamp_salle_de_bain (NAT), sensor.lumiere_salle_de_bain_etat (TPL), sensor.plug_power (NAT), switch.relais_lumiere_sdb_sonoff (NAT)
---
- [heading] Chambre: light.chambre (NAT), sensor.chambre_nb_allumes (TPL), sensor.th_chambre_temperature (NAT)
---
- [entity] : sensor.th_chambre_temperature (NAT)
---
- [entity] : light.chambre (NAT)
---
- [entity] : sensor.chambre_nb_allumes (TPL)
---
- [custom:mushroom-entity-card] Chambre: light.chambre (NAT), sensor.lumiere_chambre_etat (TPL), sensor.plug_power (NAT)
---
- [heading] Têtes de Lit: light.zone_eric (NAT), light.zone_gege (NAT), switch.prise_tete_de_lit_chambre (NAT)
---
- [entity] zE: light.zone_eric (NAT)
---
- [entity] zG: light.zone_gege (NAT)
---
- [conditional] : switch.prise_tete_de_lit_chambre (NAT)
---
- [custom:vertical-stack-in-card] : light.lit (NAT)
---
- [custom:mushroom-entity-card] Tête de Lit: light.lit (NAT), sensor.lumiere_tete_de_lit_etat (TPL), sensor.plug_power (NAT)
---
- [custom:mushroom-chips-card] : light.lit (NAT)
---
- [template] : light.lit (NAT)
---
- [custom:bubble-card] Têtes de Lit (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-light-card] Tête de Lit Gégé: light.hue_color_candle_chambre_gege (NAT)
---
- [custom:layout-card]  (aucune entite)
---
- [custom:button-card] : light.hue_color_candle_chambre_gege (NAT)
---
- [custom:button-card] : light.hue_color_candle_chambre_gege (NAT)
---
- [custom:button-card] : light.hue_color_candle_chambre_gege (NAT)
---
- [custom:button-card] : light.hue_color_candle_chambre_gege (NAT)
---
- [custom:mushroom-light-card] Tête de Lit Eric: light.hue_color_candle_chambre_eric (NAT)
---
- [custom:layout-card]  (aucune entite)
---
- [custom:button-card] : light.hue_color_candle_chambre_eric (NAT)
---
- [custom:button-card] : light.hue_color_candle_chambre_eric (NAT)
---
- [custom:button-card] : light.hue_color_candle_chambre_eric (NAT)
---
- [custom:button-card] : light.hue_color_candle_chambre_eric (NAT)
---
- [custom:bubble-card] Lampes Bureau (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-light-card] Lampes Bureau: light.bureau (NAT)
---
- [custom:layout-card]  (aucune entite)
---
- [custom:button-card] : light.bureau (NAT)
---
- [custom:button-card] : light.bureau (NAT)
---
- [custom:button-card] : light.bureau (NAT)
---
- [custom:button-card] : light.bureau (NAT)
---
- [custom:bubble-card] Ecrans P.C. (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-light-card] Ecrans P.C.: light.moniteur_pc (NAT)
---
- [custom:layout-card]  (aucune entite)
---
- [custom:button-card] : light.moniteur_pc (NAT)
---
- [custom:button-card] : light.moniteur_pc (NAT)
---
- [custom:button-card] : light.moniteur_pc (NAT)
---
- [custom:button-card] : light.moniteur_pc (NAT)
---
- [custom:streamline-card]  (aucune entite)

#### page_L3C1_eclairage_gauche_2026-05-13.yaml (19 cartes, 14 entites)

- [grid]  (aucune entite)
---
- [heading] LUMIERES (aucune entite)
---
- [heading] Entrée: light.entree (NAT)
---
- [entity] Entrée: light.entree (NAT)
---
- [custom:mushroom-entity-card] Entrée: light.entree (NAT), sensor.lumiere_entree_etat (TPL), sensor.plug_power (NAT)
---
- [heading] Salon: cover.store_salon (NAT), light.salon (NAT), light.table (NAT), sensor.th_salon_temperature (NAT)
---
- [entity] : sensor.th_salon_temperature (NAT)
---
- [entity] : cover.store_salon (NAT)
---
- [entity] : light.salon (NAT)
---
- [entity] : light.table (NAT)
---
- [custom:mushroom-entity-card] Salon: light.salon (NAT), sensor.lumiere_salon_etat (TPL), sensor.plug_power (NAT)
---
- [custom:mushroom-entity-card] Table: light.table (NAT), sensor.lumiere_table_etat (TPL), sensor.plug_power (NAT)
---
- [heading] Cuisine: light.cuisine (NAT), sensor.th_cuisine_temperature (NAT)
---
- [entity] : sensor.th_cuisine_temperature (NAT)
---
- [entity] Cuisine: light.cuisine (NAT)
---
- [custom:mushroom-entity-card] Cuisine: light.cuisine (NAT), sensor.lumiere_cuisine_etat (TPL), sensor.plug_power (NAT)
---
- [heading] Couloir: light.couloir (NAT)
---
- [entity] Couloir: light.couloir (NAT)
---
- [custom:mushroom-entity-card] Couloir: light.couloir (NAT), sensor.lumiere_couloir_etat (TPL), sensor.plug_power (NAT)

#### vignette_L3C1_eclairage_2026-05-13.yaml (1 cartes, 17 entites)

- [custom:button-card] : light.chambre (NAT), light.couloir (NAT), light.cuisine (NAT), light.entree (NAT), light.hue_color_candle_chambre_eric (NAT), light.hue_color_candle_chambre_gege (NAT), light.hue_white_lamp_salle_de_bain (NAT), light.salon (NAT), light.table (NAT), sensor.bureau_etat (TPL), sensor.chambre_etat (TPL), sensor.lumiere_appartement_etat (TPL), sensor.lumiere_cuisine_etat (TPL), sensor.lumiere_ecran_etat (TPL), sensor.lumiere_salle_de_bain_etat (TPL), sensor.lumiere_salon_etat (TPL), switch.prise_tete_de_lit_chambre (NAT)

### L3C2 - Commandes_Prises


*24 entites, 22 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 24)
        └─→ VIGNETTE L3C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `light.hue_smart_eco_pc_bureau` | NAT | (native/UI) |
| `light.hue_smart_eco_salon` | NAT | idem |
| `light.hue_smart_eco_tv_chambre` | NAT | idem |
| `sensor.prise_bureau_pc_ikea_current` | NAT | idem |
| `sensor.prise_bureau_pc_ikea_power` | NAT | idem |
| `sensor.prise_bureau_pc_ikea_voltage` | NAT | idem |
| `sensor.prise_horloge_ikea_current` | NAT | idem |
| `sensor.prise_horloge_ikea_power` | NAT | idem |
| `sensor.prise_horloge_ikea_voltage` | NAT | idem |
| `sensor.prise_salon_chargeur_nous_current` | NAT | idem |
| `sensor.prise_salon_chargeur_nous_power` | NAT | idem |
| `sensor.prise_salon_chargeur_nous_voltage` | NAT | idem |
| `sensor.prise_tete_de_lit_chambre_current` | NAT | idem |
| `sensor.prise_tete_de_lit_chambre_power` | NAT | idem |
| `sensor.prise_tete_de_lit_chambre_voltage` | NAT | idem |
| `sensor.prise_tv_chambre_nous_current` | NAT | idem |
| `sensor.prise_tv_chambre_nous_power` | NAT | idem |
| `sensor.prise_tv_chambre_nous_voltage` | NAT | idem |
| `sensor.prise_tv_salon_ikea_current` | NAT | idem |
| `sensor.prise_tv_salon_ikea_power` | NAT | idem |
| `sensor.prise_tv_salon_ikea_voltage` | NAT | idem |
| `switch.prise_horloge_ikea` | NAT | idem |
| `switch.prise_tete_de_lit_chambre` | NAT | idem |
| `switch.prise_tv_salon_ikea` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L3C2_prises_2026-05-14.yaml` | ✅ |
| `vignette_L3C2_prises_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L3C2_prises_2026-05-14.yaml (21 cartes, 24 entites)

- [grid]  (aucune entite)
---
- [heading] PRISES éCO. (aucune entite)
---
- [heading] Entrée (aucune entite)
---
- [custom:mushroom-entity-card] Prise Eco. Horloge: sensor.prise_horloge_ikea_current (NAT), sensor.prise_horloge_ikea_power (NAT), sensor.prise_horloge_ikea_voltage (NAT), switch.prise_horloge_ikea (NAT)
---
- [heading]  (aucune entite)
---
- [heading] Salon (aucune entite)
---
- [custom:mushroom-entity-card] Prise Eco. Salon: light.hue_smart_eco_salon (NAT), sensor.prise_salon_chargeur_nous_current (NAT), sensor.prise_salon_chargeur_nous_power (NAT), sensor.prise_salon_chargeur_nous_voltage (NAT)
---
- [heading]  (aucune entite)
---
- [heading] TV Salon (aucune entite)
---
- [custom:mushroom-entity-card] Prise Eco. TV Salon: sensor.prise_tv_salon_ikea_current (NAT), sensor.prise_tv_salon_ikea_power (NAT), sensor.prise_tv_salon_ikea_voltage (NAT), switch.prise_tv_salon_ikea (NAT)
---
- [heading]  (aucune entite)
---
- [heading] Bureau (aucune entite)
---
- [custom:mushroom-entity-card] Prise PC Bureau: light.hue_smart_eco_pc_bureau (NAT), sensor.prise_bureau_pc_ikea_current (NAT), sensor.prise_bureau_pc_ikea_power (NAT), sensor.prise_bureau_pc_ikea_voltage (NAT)
---
- [heading]  (aucune entite)
---
- [heading] Chambre (aucune entite)
---
- [custom:mushroom-entity-card] Prise Eco. TV Chambre: light.hue_smart_eco_tv_chambre (NAT), sensor.prise_tv_chambre_nous_current (NAT), sensor.prise_tv_chambre_nous_power (NAT), sensor.prise_tv_chambre_nous_voltage (NAT)
---
- [heading]  (aucune entite)
---
- [heading] Tête de Lit (aucune entite)
---
- [custom:mushroom-entity-card] Prise Eco. Têtes de Lit: sensor.prise_tete_de_lit_chambre_current (NAT), sensor.prise_tete_de_lit_chambre_power (NAT), sensor.prise_tete_de_lit_chambre_voltage (NAT), switch.prise_tete_de_lit_chambre (NAT)
---
- [heading]  (aucune entite)
---
- [custom:streamline-card]  (aucune entite)

#### vignette_L3C2_prises_2026-05-14.yaml (1 cartes, 6 entites)

- [custom:button-card] : light.hue_smart_eco_pc_bureau (NAT), light.hue_smart_eco_salon (NAT), light.hue_smart_eco_tv_chambre (NAT), switch.prise_horloge_ikea (NAT), switch.prise_tete_de_lit_chambre (NAT), switch.prise_tv_salon_ikea (NAT)

### L3C3 - Stores_Fenetres

*Validée le 2026-05-14*

*17 entites, 53 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 15)
  └─→ TPL: S_01_STORES.yaml (2)
        └─→ VIGNETTE L3C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | NAT | (native/UI) |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | NAT | idem |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | NAT | idem |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | NAT | idem |
| `cover.store_bureau` | NAT | idem |
| `cover.store_salon` | NAT | idem |
| `light.store_bureau_dnd` | NAT | idem |
| `light.store_salon_dnd` | NAT | idem |
| `sensor.contact_fenetre_bureau_sonoff_battery` | NAT | idem |
| `sensor.contact_fenetre_salon_sonoff_battery` | NAT | idem |
| `sensor.store_bureau_signal_strength` | NAT | idem |
| `sensor.store_chambre_status` | NAT | idem |
| `sensor.store_cuisine_status` | NAT | idem |
| `sensor.store_salon_signal_strength` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.store_bureau_status` | TPL | S_01_STORES.yaml |
| `sensor.store_salon_status` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L3C3_stores_2026-06-02.yaml` | ✅ |
| `vignette_L3C3_stores_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L3C3_stores_2026-06-02.yaml (52 cartes, 13 entites)

- [grid]  (aucune entite)
---
- [heading] STORES (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [heading] Auto close at +34°: sensor.th_balcon_nord_temperature (NAT)
---
- [entity] : sensor.th_balcon_nord_temperature (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [heading] Fenêtre Salon: binary_sensor.contact_fenetre_salon_sonoff_contact (NAT), sensor.contact_fenetre_salon_sonoff_battery (NAT)
---
- [entity] : binary_sensor.contact_fenetre_salon_sonoff_contact (NAT)
---
- [entity] : sensor.contact_fenetre_salon_sonoff_battery (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:enhanced-shutter-card] : cover.store_salon (NAT), sensor.store_salon_signal_strength (NAT)
---
- [custom:button-card] : cover.store_salon (NAT), sensor.store_salon_status (TPL)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] 100%: cover.store_salon (NAT)
---
- [custom:button-card] 75%: cover.store_salon (NAT)
---
- [custom:button-card] 50%: cover.store_salon (NAT)
---
- [custom:button-card] 25%: cover.store_salon (NAT)
---
- [custom:button-card] 10%: cover.store_salon (NAT)
---
- [custom:button-card] 0%: cover.store_salon (NAT)
---
- [custom:mushroom-light-card] Store Salon (Voyants commandes): light.store_salon_dnd (NAT)
---
- [heading] STORES (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [heading] Auto open at +18° or auto close at +25°: sensor.th_balcon_nord_temperature (NAT)
---
- [entity] : sensor.th_balcon_nord_temperature (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [heading] Fenêtre Bureau: binary_sensor.contact_fenetre_bureau_sonoff_contact (NAT), sensor.contact_fenetre_bureau_sonoff_battery (NAT)
---
- [entity] : binary_sensor.contact_fenetre_bureau_sonoff_contact (NAT)
---
- [entity] : sensor.contact_fenetre_bureau_sonoff_battery (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:enhanced-shutter-card] : cover.store_bureau (NAT), sensor.store_bureau_signal_strength (NAT)
---
- [custom:button-card] : cover.store_bureau (NAT), sensor.store_bureau_status (TPL)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] 100%: cover.store_bureau (NAT)
---
- [custom:button-card] 75%: cover.store_bureau (NAT)
---
- [custom:button-card] 50%: cover.store_bureau (NAT)
---
- [custom:button-card] 25%: cover.store_bureau (NAT)
---
- [custom:button-card] 10%: cover.store_bureau (NAT)
---
- [custom:button-card] 0%: cover.store_bureau (NAT)
---
- [custom:mushroom-light-card] Store Bureau (Voyants commandes): light.store_bureau_dnd (NAT)
---
- [custom:streamline-card]  (aucune entite)

#### vignette_L3C3_stores_2026-05-14.yaml (1 cartes, 8 entites)

- [custom:button-card] : binary_sensor.contact_fenetre_bureau_sonoff_contact (NAT), binary_sensor.contact_fenetre_chambre_sonoff_contact (NAT), binary_sensor.contact_fenetre_cuisine_sonoff_contact (NAT), binary_sensor.contact_fenetre_salon_sonoff_contact (NAT), sensor.store_bureau_status (TPL), sensor.store_chambre_status (NAT), sensor.store_cuisine_status (NAT), sensor.store_salon_status (TPL)

### L4C1 - Proxmox

*Validée le 2026-06-13 (docs entièrement réécrites - +5e section MyElectricalData)*

> Page complète supervision infrastructure Proxmox VE. Vignette : température CPU, CPU %, RAM %, Storage %, PVE Status. Page : **5 sections** (PVE, HA, Z2M, MariaDB, MyElectricalData) × métriques détaillées + apexcharts CPU 1h. Path → `/dashboard-tablette/systeme-proxmox`.
> ⚠️ Pas de `binary_sensor.myelectricaldata_backup_status` (contrairement à PVE). Pas de `sensor.myelectricaldata_utilisation_du_disque` en % - seuils page à exprimer en GiB absolu. Badge : vert `rgb(15,157,88)` - couleur section : `#00bcd4`.

*63 entites, 100 cartes, 3 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 63)
        └─→ VIGNETTE L4C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.pve_backup_status` | NAT | (native/UI) |
| `binary_sensor.pve_status` | NAT | idem |
| `button.homeassistant_create_snapshot` | NAT | idem |
| `button.homeassistant_demarrer` | NAT | idem |
| `button.homeassistant_redemarrer` | NAT | idem |
| `button.homeassistant_reload` | NAT | idem |
| `button.homeassistant_restart` | NAT | idem |
| `button.homeassistant_stopper` | NAT | idem |
| `button.mariadb_create_snapshot` | NAT | idem |
| `button.mariadb_demarrer` | NAT | idem |
| `button.mariadb_redemarrer` | NAT | idem |
| `button.mariadb_stopper` | NAT | idem |
| `button.z2m_create_snapshot` | NAT | idem |
| `button.z2m_demarrer` | NAT | idem |
| `button.z2m_redemarrer` | NAT | idem |
| `button.z2m_stopper` | NAT | idem |
| `sensor.homeassistant_max_cpu` | NAT | idem |
| `sensor.homeassistant_memory_usage_percentage` | NAT | idem |
| `sensor.homeassistant_statut` | NAT | idem |
| `sensor.homeassistant_uptime` | NAT | idem |
| `sensor.homeassistant_utilisation_de_la_memoire` | NAT | idem |
| `sensor.homeassistant_utilisation_du_disque` | NAT | idem |
| `sensor.homeassistant_utilisation_du_processeur` | NAT | idem |
| `sensor.homeassistant_utilisation_maximale_de_la_memoire` | NAT | idem |
| `sensor.homeassistant_utilisation_maximale_du_disque` | NAT | idem |
| `sensor.mariadb_max_cpu` | NAT | idem |
| `sensor.mariadb_memory_usage_percentage` | NAT | idem |
| `sensor.mariadb_statut` | NAT | idem |
| `sensor.mariadb_uptime` | NAT | idem |
| `sensor.mariadb_utilisation_de_la_memoire` | NAT | idem |
| `sensor.mariadb_utilisation_du_disque` | NAT | idem |
| `sensor.mariadb_utilisation_du_processeur` | NAT | idem |
| `sensor.mariadb_utilisation_maximale_de_la_memoire` | NAT | idem |
| `sensor.mariadb_utilisation_maximale_du_disque` | NAT | idem |
| `sensor.myelectricaldata_max_cpu` | NAT | idem |
| `sensor.myelectricaldata_statut` | NAT | idem |
| `sensor.myelectricaldata_uptime` | NAT | idem |
| `sensor.myelectricaldata_utilisation_de_la_memoire` | NAT | idem |
| `sensor.myelectricaldata_utilisation_du_disque` | NAT | idem |
| `sensor.myelectricaldata_utilisation_du_processeur` | NAT | idem |
| `sensor.myelectricaldata_utilisation_maximale_de_la_memoire` | NAT | idem |
| `sensor.myelectricaldata_utilisation_maximale_du_disque` | NAT | idem |
| `sensor.proxmox_cpu_package` | NAT | idem |
| `sensor.pve_max_cpu` | NAT | idem |
| `sensor.pve_memory_usage_percentage` | NAT | idem |
| `sensor.pve_statut` | NAT | idem |
| `sensor.pve_uptime` | NAT | idem |
| `sensor.pve_utilisation_de_la_memoire` | NAT | idem |
| `sensor.pve_utilisation_du_disque` | NAT | idem |
| `sensor.pve_utilisation_du_processeur` | NAT | idem |
| `sensor.pve_utilisation_maximale_de_la_memoire` | NAT | idem |
| `sensor.pve_utilisation_maximale_du_disque` | NAT | idem |
| `sensor.storage_local_storage_usage_percentage` | NAT | idem |
| `sensor.system_monitor_utilisation_du_disque` | NAT | idem |
| `sensor.z2m_max_cpu` | NAT | idem |
| `sensor.z2m_memory_usage_percentage` | NAT | idem |
| `sensor.z2m_statut` | NAT | idem |
| `sensor.z2m_uptime` | NAT | idem |
| `sensor.z2m_utilisation_de_la_memoire` | NAT | idem |
| `sensor.z2m_utilisation_du_disque` | NAT | idem |
| `sensor.z2m_utilisation_du_processeur` | NAT | idem |
| `sensor.z2m_utilisation_maximale_de_la_memoire` | NAT | idem |
| `sensor.z2m_utilisation_maximale_du_disque` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_services_ha_z2m_mariadb_2026-05-19.yaml` | ✅ |
| `page_L4C1_proxmox_2026-08-08.yaml` | ✅ |
| `vignette_L4C1_proxmox_2026-08-08.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_services_ha_z2m_mariadb_2026-05-19.yaml (44 cartes, 26 entites)

- [grid]  (aucune entite)
---
- [heading] EMPTY (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] HOME ASSISTANT: sensor.homeassistant_statut (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] CPU %: sensor.homeassistant_utilisation_du_processeur (NAT)
---
- [custom:bar-card] RAM %: sensor.homeassistant_memory_usage_percentage (NAT)
---
- [custom:bar-card] Disk GiB: sensor.homeassistant_utilisation_du_disque (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] Démarrer: button.homeassistant_demarrer (NAT)
---
- [custom:button-card] Stopper: button.homeassistant_stopper (NAT)
---
- [custom:button-card] LXC: button.homeassistant_redemarrer (NAT)
---
- [custom:button-card] HA: button.homeassistant_restart (NAT)
---
- [custom:button-card] Reload: button.homeassistant_reload (NAT)
---
- [custom:button-card] Snapshot: button.homeassistant_create_snapshot (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] ZIGBEE2MQTT: sensor.z2m_statut (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] CPU %: sensor.z2m_utilisation_du_processeur (NAT)
---
- [custom:bar-card] RAM %: sensor.z2m_memory_usage_percentage (NAT)
---
- [custom:bar-card] Disk GiB: sensor.z2m_utilisation_du_disque (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] Démarrer: button.z2m_demarrer (NAT)
---
- [custom:button-card] Stopper: button.z2m_stopper (NAT)
---
- [custom:button-card] Relancer: button.z2m_redemarrer (NAT)
---
- [custom:button-card] Snapshot: button.z2m_create_snapshot (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] MARIADB: sensor.mariadb_statut (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] CPU %: sensor.mariadb_utilisation_du_processeur (NAT)
---
- [custom:bar-card] RAM %: sensor.mariadb_memory_usage_percentage (NAT)
---
- [custom:bar-card] Disk GiB: sensor.mariadb_utilisation_du_disque (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] Démarrer: button.mariadb_demarrer (NAT)
---
- [custom:button-card] Stopper: button.mariadb_stopper (NAT)
---
- [custom:button-card] Relancer: button.mariadb_redemarrer (NAT)
---
- [custom:button-card] Snapshot: button.mariadb_create_snapshot (NAT)

#### page_L4C1_proxmox_2026-08-08.yaml (55 cartes, 41 entites)

- [grid]  (aucune entite)
---
- [heading] PROXMOX (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] PROXMOX VE: sensor.pve_statut (NAT)
---
- [custom:button-card] : sensor.pve_max_cpu (NAT), sensor.pve_utilisation_du_processeur (NAT)
---
- [custom:button-card] : sensor.pve_utilisation_de_la_memoire (NAT), sensor.pve_utilisation_maximale_de_la_memoire (NAT)
---
- [custom:button-card] : sensor.pve_utilisation_du_disque (NAT), sensor.pve_utilisation_maximale_du_disque (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] : sensor.pve_uptime (NAT)
---
- [custom:button-card] : binary_sensor.pve_backup_status (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] : sensor.pve_utilisation_du_processeur (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] HOME ASSISTANT: sensor.homeassistant_statut (NAT)
---
- [custom:button-card] : sensor.homeassistant_max_cpu (NAT), sensor.homeassistant_utilisation_du_processeur (NAT)
---
- [custom:button-card] : sensor.homeassistant_utilisation_de_la_memoire (NAT), sensor.homeassistant_utilisation_maximale_de_la_memoire (NAT)
---
- [custom:button-card] : sensor.homeassistant_utilisation_maximale_du_disque (NAT), sensor.system_monitor_utilisation_du_disque (NAT)
---
- [custom:button-card] : sensor.homeassistant_uptime (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] : sensor.homeassistant_utilisation_du_processeur (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] ZIGBEE2MQTT: sensor.z2m_statut (NAT)
---
- [custom:button-card] : sensor.z2m_max_cpu (NAT), sensor.z2m_utilisation_du_processeur (NAT)
---
- [custom:button-card] : sensor.z2m_utilisation_de_la_memoire (NAT), sensor.z2m_utilisation_maximale_de_la_memoire (NAT)
---
- [custom:button-card] : sensor.z2m_utilisation_du_disque (NAT), sensor.z2m_utilisation_maximale_du_disque (NAT)
---
- [custom:button-card] : sensor.z2m_uptime (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] : sensor.z2m_utilisation_du_processeur (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] MARIADB: sensor.mariadb_statut (NAT)
---
- [custom:button-card] : sensor.mariadb_max_cpu (NAT), sensor.mariadb_utilisation_du_processeur (NAT)
---
- [custom:button-card] : sensor.mariadb_utilisation_de_la_memoire (NAT), sensor.mariadb_utilisation_maximale_de_la_memoire (NAT)
---
- [custom:button-card] : sensor.mariadb_utilisation_du_disque (NAT), sensor.mariadb_utilisation_maximale_du_disque (NAT)
---
- [custom:button-card] : sensor.mariadb_uptime (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] : sensor.mariadb_utilisation_du_processeur (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:button-card] MYELECTRICALDATA: sensor.myelectricaldata_statut (NAT)
---
- [custom:button-card] : sensor.myelectricaldata_max_cpu (NAT), sensor.myelectricaldata_utilisation_du_processeur (NAT)
---
- [custom:button-card] : sensor.myelectricaldata_utilisation_de_la_memoire (NAT), sensor.myelectricaldata_utilisation_maximale_de_la_memoire (NAT)
---
- [custom:button-card] : sensor.myelectricaldata_utilisation_du_disque (NAT), sensor.myelectricaldata_utilisation_maximale_du_disque (NAT)
---
- [custom:button-card] : sensor.myelectricaldata_uptime (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] : sensor.myelectricaldata_utilisation_du_processeur (NAT)

#### vignette_L4C1_proxmox_2026-08-08.yaml (1 cartes, 5 entites)

- [custom:button-card] _____ Proxmox _____: binary_sensor.pve_status (NAT), sensor.proxmox_cpu_package (NAT), sensor.pve_memory_usage_percentage (NAT), sensor.pve_utilisation_du_processeur (NAT), sensor.storage_local_storage_usage_percentage (NAT)

### L4C2 - Mini_PC

*Validée le 2026-06-18 - vignette refactorisée : proxmox_cpu_package direct (sans template) | ⚠️ uptime bug non encore corrigé en page*

> ⚠️ **BUG UPTIME CONNU** (non corrigé) : Jinja2 dans la page utilise `| int(0)` + `/ 86400` alors que `sensor.pve_uptime` retourne des **heures** (float), pas des secondes. Résultat : affiche ~0j 0h. Fix à appliquer : ```yaml {% set uptime = states('sensor.pve_uptime') | float(0) %} {% set jours = (uptime / 24) | int(0) %} {% set heures = (uptime % 24) | int(0) %} {% set minutes = ((uptime % 1) * 60) | int(0) %} ```
> ⚠️ Interface réseau : **`enp6s18`** (VirtIO KVM sous Proxmox) - PAS `enp1s0`.

*28 entites, 99 cartes, 3 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 24)
  └─→ UM: P2_UM_AMHQ_mini_pc.yaml (2)
  └─→ TPL: P2_AVG_AMHQ_mini_pc.yaml (2)
        └─→ VIGNETTE L4C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.cpu_speed` | NAT | (native/UI) |
| `sensor.ip_externe_wan` | NAT | idem |
| `sensor.local_ip` | NAT | idem |
| `sensor.prise_mini_pc_ikea_current` | NAT | idem |
| `sensor.prise_mini_pc_ikea_energy` | NAT | idem |
| `sensor.prise_mini_pc_ikea_power` | NAT | idem |
| `sensor.proxmox_carte_mere` | NAT | idem |
| `sensor.proxmox_core_0` | NAT | idem |
| `sensor.proxmox_core_1` | NAT | idem |
| `sensor.proxmox_core_2` | NAT | idem |
| `sensor.proxmox_core_3` | NAT | idem |
| `sensor.proxmox_cpu_package` | NAT | idem |
| `sensor.pve_memory_usage_percentage` | NAT | idem |
| `sensor.pve_uptime` | NAT | idem |
| `sensor.pve_utilisation_du_disque` | NAT | idem |
| `sensor.pve_utilisation_du_processeur` | NAT | idem |
| `sensor.storage_local_storage_usage_percentage` | NAT | idem |
| `sensor.system_monitor_charge_15m` | NAT | idem |
| `sensor.system_monitor_charge_1m` | NAT | idem |
| `sensor.system_monitor_charge_5m` | NAT | idem |
| `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18` | NAT | idem |
| `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18` | NAT | idem |
| `sensor.system_monitor_memoire_libre` | NAT | idem |
| `sensor.system_monitor_memoire_utilisee` | NAT | idem |
| `sensor.mini_pc_avg_watts_mensuel` | TPL | P2_AVG_AMHQ_mini_pc.yaml |
| `sensor.mini_pc_avg_watts_quotidien` | TPL | idem |
| `sensor.prise_mini_pc_ikea_mensuel_um` | UM | P2_UM_AMHQ_mini_pc.yaml |
| `sensor.prise_mini_pc_ikea_quotidien_um` | UM | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_popup_memory_2026-06-09.yaml` | ✅ |
| `page_L4C2_mini_pc_2026-08-02.yaml` | ✅ |
| `vignette_L4C2_mini_pc_2026-06-18.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_popup_memory_2026-06-09.yaml (4 cartes, 1 entites)

- [custom:bubble-card] Mémoire RAM (aucune entite)
---
- [custom:apexcharts-card] : sensor.pve_memory_usage_percentage (NAT)
---
- [area] RAM %: sensor.pve_memory_usage_percentage (NAT)
---
- [line] Moy.(24h): sensor.pve_memory_usage_percentage (NAT)

#### page_L4C2_mini_pc_2026-08-02.yaml (94 cartes, 27 entites)

- [grid]  (aucune entite)
---
- [heading] Mini - P.C. (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [picture]  (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.local_ip (NAT)
---
- [custom:mushroom-template-card] : sensor.ip_externe_wan (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mushroom-template-card]  (aucune entite)
---
- [custom:mushroom-template-card] : sensor.pve_uptime (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.pve_utilisation_du_processeur (NAT)
---
- [custom:bar-card] : sensor.proxmox_cpu_package (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.pve_memory_usage_percentage (NAT)
---
- [custom:bar-card] : sensor.system_monitor_memoire_utilisee (NAT)
---
- [custom:bar-card] : sensor.system_monitor_memoire_libre (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:bar-card] : sensor.pve_utilisation_du_disque (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18 (NAT)
---
- [custom:bar-card] : sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18 (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:ring-tile] Utilisation CPU: sensor.pve_utilisation_du_processeur (NAT)
---
- [custom:mini-graph-card] : sensor.pve_utilisation_du_processeur (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.cpu_speed (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.system_monitor_charge_1m (NAT)
---
- [custom:bar-card] : sensor.system_monitor_charge_5m (NAT)
---
- [custom:bar-card] : sensor.system_monitor_charge_15m (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:ring-tile] Température CPU: sensor.proxmox_cpu_package (NAT)
---
- [custom:mini-graph-card] : sensor.proxmox_cpu_package (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.proxmox_core_0 (NAT)
---
- [custom:bar-card] : sensor.proxmox_core_1 (NAT)
---
- [custom:bar-card] : sensor.proxmox_core_2 (NAT)
---
- [custom:bar-card] : sensor.proxmox_core_3 (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.proxmox_cpu_package (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.proxmox_carte_mere (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:ring-tile] Mini-PC Conso: sensor.prise_mini_pc_ikea_power (NAT)
---
- [custom:mini-graph-card] : sensor.prise_mini_pc_ikea_power (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.prise_mini_pc_ikea_power (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:ring-tile] Conso. Mem.: sensor.system_monitor_memoire_utilisee (NAT)
---
- [custom:mini-graph-card] : sensor.system_monitor_memoire_utilisee (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.system_monitor_memoire_utilisee (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:ring-tile] Disque PVE (VM): sensor.pve_utilisation_du_disque (NAT)
---
- [custom:mini-graph-card] : sensor.pve_utilisation_du_disque (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.pve_utilisation_du_disque (NAT)
---
- [custom:bubble-card] Utilisation du CPU (aucune entite)
---
- [custom:apexcharts-card] : sensor.pve_utilisation_du_processeur (NAT)
---
- [area] SM Instantané: sensor.pve_utilisation_du_processeur (NAT)
---
- [area] PVE Instantané: sensor.pve_utilisation_du_processeur (NAT)
---
- [line] Moy.(24h): sensor.pve_utilisation_du_processeur (NAT)
---
- [custom:bubble-card] Températures processeur (aucune entite)
---
- [custom:apexcharts-card] : sensor.proxmox_cpu_package (NAT)
---
- [area] CPU Package: sensor.proxmox_cpu_package (NAT)
---
- [line] Carte Mère: sensor.proxmox_carte_mere (NAT)
---
- [line] Moy.(24h): sensor.proxmox_cpu_package (NAT)
---
- [custom:bubble-card] Consommation Mini-PC (aucune entite)
---
- [custom:streamline-card] : sensor.mini_pc_avg_watts_quotidien (TPL), sensor.prise_mini_pc_ikea_current (NAT), sensor.prise_mini_pc_ikea_power (NAT), sensor.prise_mini_pc_ikea_quotidien_um (UM)
---
- [custom:streamline-card] : sensor.mini_pc_avg_watts_mensuel (TPL), sensor.prise_mini_pc_ikea_energy (NAT), sensor.prise_mini_pc_ikea_mensuel_um (UM)
---
- [custom:bubble-card] Mémoire RAM (aucune entite)
---
- [custom:apexcharts-card] : sensor.pve_memory_usage_percentage (NAT)
---
- [area] RAM %: sensor.pve_memory_usage_percentage (NAT)
---
- [line] Moy.(24h): sensor.pve_memory_usage_percentage (NAT)
---
- [custom:bubble-card] Espace disque — PVE VM (aucune entite)
---
- [custom:apexcharts-card] : sensor.pve_utilisation_du_disque (NAT)
---
- [area] Disque utilisé GiB: sensor.pve_utilisation_du_disque (NAT)
---
- [line] Moy.(24h): sensor.pve_utilisation_du_disque (NAT)

#### vignette_L4C2_mini_pc_2026-06-18.yaml (1 cartes, 5 entites)

- [custom:button-card] _____ Mini - P.C. _____: sensor.prise_mini_pc_ikea_power (NAT), sensor.proxmox_cpu_package (NAT), sensor.pve_memory_usage_percentage (NAT), sensor.pve_utilisation_du_processeur (NAT), sensor.storage_local_storage_usage_percentage (NAT)

### L4C3 - MAJ_HA

*Validée le 2026-05-14*

> ⚠️ Corrigé le 2026-07-19 : `sensor.available_updates` était marqué NAT - c'est en réalité un TPL (`templates/utilitaires/Mise_a_jour_home_assistant.yaml`, absent de cette section jusqu'ici), qui compte les entités `update.*` à l'état "on". Vérifié dans le corps du fichier.

*10 entites, 110 cartes, 4 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 9)
  └─→ TPL: Mise_a_jour_home_assistant.yaml (1)
        └─→ VIGNETTE L4C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.home_assistant_core_cpu_percent` | NAT | (native/UI) |
| `sensor.home_assistant_core_memory_percent` | NAT | idem |
| `sensor.home_assistant_supervisor_cpu_percent` | NAT | idem |
| `sensor.home_assistant_supervisor_memory_percent` | NAT | idem |
| `update.hacs_update` | NAT | idem |
| `update.home` | NAT | idem |
| `update.home_assistant_core_update` | NAT | idem |
| `update.home_assistant_operating_system_update` | NAT | idem |
| `update.home_assistant_supervisor_update` | NAT | idem |
| `sensor.available_updates` | TPL | Mise_a_jour_home_assistant.yaml |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L4C3_maj_ha_2026-06-15.yaml` | ✅ |
| `page_L4C3_maj_ha_droite_2026-05-14.yaml` | ✅ |
| `page_L4C3_maj_ha_gauche_2026-05-14.yaml` | ✅ |
| `vignette_L4C3_maj_ha_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L4C3_maj_ha_2026-06-15.yaml (40 cartes, 8 entites)

- [grid]  (aucune entite)
---
- [heading] H.A. UPDATE (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] Addons updates (aucune entite)
---
- [markdown] : update.home_assistant_core_update (NAT), update.home_assistant_operating_system_update (NAT), update.home_assistant_supervisor_update (NAT)
---
- [custom:auto-entities]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('Home A (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] HACS updates (aucune entite)
---
- [markdown] : update.hacs_update (NAT)
---
- [markdown]  (aucune entite)
---
- [custom:auto-entities] : update.hacs_update (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('update (aucune entite)
---
- [custom:button-card] [[[
 if (variables.url == null)return ""
 else
  {return '<a (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] ZigBee2MQTT (aucune entite)
---
- [markdown]  (aucune entite)
---
- [custom:auto-entities]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('Home A (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [heading] H.A. ADD-ON (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-update-card] Home Assistant Core: update.home_assistant_core_update (NAT)
---
- [custom:mushroom-chips-card] : sensor.home_assistant_core_cpu_percent (NAT), sensor.home_assistant_core_memory_percent (NAT)
---
- [template]  (aucune entite)
---
- [entity] : sensor.home_assistant_core_cpu_percent (NAT)
---
- [entity] : sensor.home_assistant_core_memory_percent (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-update-card] Home Assistant Supervisor: update.home_assistant_supervisor_update (NAT)
---
- [custom:mushroom-chips-card] : sensor.home_assistant_supervisor_cpu_percent (NAT), sensor.home_assistant_supervisor_memory_percent (NAT)
---
- [template]  (aucune entite)
---
- [entity] : sensor.home_assistant_supervisor_cpu_percent (NAT)
---
- [entity] : sensor.home_assistant_supervisor_memory_percent (NAT)

#### page_L4C3_maj_ha_droite_2026-05-14.yaml (40 cartes, 8 entites)

- [grid]  (aucune entite)
---
- [heading] H.A. UPDATE (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] Addons updates (aucune entite)
---
- [markdown] : update.home_assistant_core_update (NAT), update.home_assistant_operating_system_update (NAT), update.home_assistant_supervisor_update (NAT)
---
- [custom:auto-entities]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('Home A (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] HACS updates (aucune entite)
---
- [markdown] : update.hacs_update (NAT)
---
- [markdown]  (aucune entite)
---
- [custom:auto-entities] : update.hacs_update (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('update (aucune entite)
---
- [custom:button-card] [[[
 if (variables.url == null)return ""
 else
  {return '<a (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] ZigBee2MQTT (aucune entite)
---
- [markdown]  (aucune entite)
---
- [custom:auto-entities]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('Home A (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [heading] H.A. ADD-ON (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-update-card] Home Assistant Core: update.home_assistant_core_update (NAT)
---
- [custom:mushroom-chips-card] : sensor.home_assistant_core_cpu_percent (NAT), sensor.home_assistant_core_memory_percent (NAT)
---
- [template]  (aucune entite)
---
- [entity] : sensor.home_assistant_core_cpu_percent (NAT)
---
- [entity] : sensor.home_assistant_core_memory_percent (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-update-card] Home Assistant Supervisor: update.home_assistant_supervisor_update (NAT)
---
- [custom:mushroom-chips-card] : sensor.home_assistant_supervisor_cpu_percent (NAT), sensor.home_assistant_supervisor_memory_percent (NAT)
---
- [template]  (aucune entite)
---
- [entity] : sensor.home_assistant_supervisor_cpu_percent (NAT)
---
- [entity] : sensor.home_assistant_supervisor_memory_percent (NAT)

#### page_L4C3_maj_ha_gauche_2026-05-14.yaml (29 cartes, 5 entites)

- [grid]  (aucune entite)
---
- [heading] H.A. SERVER (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] Home Assistant Server: update.home_assistant_core_update (NAT), update.home_assistant_operating_system_update (NAT), update.home_assistant_supervisor_update (NAT)
---
- [markdown] : update.home (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mushroom-update-card] HA Core: update.home_assistant_core_update (NAT)
---
- [custom:mushroom-template-card] : update.home_assistant_core_update (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mushroom-update-card] HA OS: update.home_assistant_operating_system_update (NAT)
---
- [custom:mushroom-template-card] : update.home_assistant_operating_system_update (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:mushroom-update-card] HA Supervisor: update.home_assistant_supervisor_update (NAT)
---
- [custom:mushroom-template-card] : update.home_assistant_core_update (NAT), update.home_assistant_supervisor_update (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card]  (aucune entite)
---
- [custom:mushroom-title-card] HACS: update.hacs_update (NAT)
---
- [markdown] : update.hacs_update (NAT)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [template]  (aucune entite)
---
- [template] : update.hacs_update (NAT)
---
- [template] : update.hacs_update (NAT)
---
- [custom:auto-entities] : update.hacs_update (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:button-card] [[[
  return entity.attributes.friendly_name.replace('update (aucune entite)
---
- [custom:button-card] [[[
 if (variables.url == null)return ""
 else
  {return '<a (aucune entite)
---
- [custom:button-card]  (aucune entite)

#### vignette_L4C3_maj_ha_2026-05-14.yaml (1 cartes, 1 entites)

- [custom:button-card] Software | modules: sensor.available_updates (TPL)

### L5C1 - Batteries_Piles

*Validée le 2026-05-14 - ⚠️ page partiellement tronquée (3 sections HUE/IKEA/SONOFF à compléter)*

*37 entites, 11 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 37)
        └─→ VIGNETTE L5C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `group.hue_devices` | NAT | (native/UI) |
| `group.ikea_devices` | NAT | idem |
| `group.sonoff_devices` | NAT | idem |
| `sensor.boutton_salle_de_bain_hue_battery` | NAT | idem |
| `sensor.contact_fenetre_bureau_sonoff_battery` | NAT | idem |
| `sensor.contact_fenetre_chambre_sonoff_battery` | NAT | idem |
| `sensor.contact_fenetre_cuisine_sonoff_battery` | NAT | idem |
| `sensor.contact_fenetre_salon_sonoff_battery` | NAT | idem |
| `sensor.detecteur_de_fuite_ikea_battery` | NAT | idem |
| `sensor.detecteur_vallhorn_battery` | NAT | idem |
| `sensor.gm1901_battery_level` | NAT | idem |
| `sensor.hue_smart_button_bureau_batterie` | NAT | idem |
| `sensor.hue_smart_button_chambre_batterie` | NAT | idem |
| `sensor.hue_smart_button_chambre_eric_batterie` | NAT | idem |
| `sensor.hue_smart_button_chambre_gege_batterie` | NAT | idem |
| `sensor.hue_smart_button_couloir_batterie` | NAT | idem |
| `sensor.hue_smart_button_cuisine_batterie` | NAT | idem |
| `sensor.hue_smart_button_eco_batterie` | NAT | idem |
| `sensor.hue_smart_button_entee_1_batterie` | NAT | idem |
| `sensor.hue_smart_button_entee_2_batterie` | NAT | idem |
| `sensor.hue_smart_button_table_batterie` | NAT | idem |
| `sensor.inter_bureau_rodret_battery` | NAT | idem |
| `sensor.inter_radiateur_salle_de_bain_ikea_rodret_battery` | NAT | idem |
| `sensor.inter_salon_4_ikea_battery` | NAT | idem |
| `sensor.inter_somrig_battery` | NAT | idem |
| `sensor.inter_tv_chambre_ikea_rodret_battery` | NAT | idem |
| `sensor.ne2213_` | NAT | idem |
| `sensor.poussoir_ikea_tradfri_battery` | NAT | idem |
| `sensor.sm_a530f_battery_level` | NAT | idem |
| `sensor.tablette_battery_level` | NAT | idem |
| `sensor.th_balcon_nord_battery` | NAT | idem |
| `sensor.th_bureau_battery` | NAT | idem |
| `sensor.th_cellier_battery` | NAT | idem |
| `sensor.th_chambre_battery` | NAT | idem |
| `sensor.th_cuisine_battery` | NAT | idem |
| `sensor.th_salle_de_bain_battery` | NAT | idem |
| `sensor.th_salon_battery` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L5C1_batteries_piles_2026-05-14.yaml` | ✅ |
| `vignette_L5C1_batteries_piles_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L5C1_batteries_piles_2026-05-14.yaml (10 cartes, 34 entites)

- [grid]  (aucune entite)
---
- [heading] BATTERIES (Boutons / Thermostats / Détecteurs…) (aucune entite)
---
- [heading] Batteries des boutons-poussoirs HUE (aucune entite)
---
- [custom:battery-state-card] : sensor.boutton_salle_de_bain_hue_battery (NAT), sensor.gm1901_battery_level (NAT), sensor.hue_smart_button_bureau_batterie (NAT), sensor.hue_smart_button_chambre_batterie (NAT), sensor.hue_smart_button_chambre_eric_batterie (NAT), sensor.hue_smart_button_chambre_gege_batterie (NAT), sensor.hue_smart_button_couloir_batterie (NAT), sensor.hue_smart_button_cuisine_batterie (NAT), sensor.hue_smart_button_eco_batterie (NAT), sensor.hue_smart_button_entee_1_batterie (NAT), sensor.hue_smart_button_entee_2_batterie (NAT), sensor.hue_smart_button_table_batterie (NAT), sensor.ne2213_ (NAT), sensor.sm_a530f_battery_level (NAT), sensor.tablette_battery_level (NAT)
---
- [heading] Batteries — boutons & détecteurs IKEA (aucune entite)
---
- [custom:battery-state-card] : sensor.detecteur_de_fuite_ikea_battery (NAT), sensor.detecteur_vallhorn_battery (NAT), sensor.gm1901_battery_level (NAT), sensor.inter_bureau_rodret_battery (NAT), sensor.inter_radiateur_salle_de_bain_ikea_rodret_battery (NAT), sensor.inter_salon_4_ikea_battery (NAT), sensor.inter_somrig_battery (NAT), sensor.inter_tv_chambre_ikea_rodret_battery (NAT), sensor.ne2213_ (NAT), sensor.poussoir_ikea_tradfri_battery (NAT), sensor.sm_a530f_battery_level (NAT), sensor.tablette_battery_level (NAT)
---
- [heading] Batteries — contacts de fenêtres SONOFF (aucune entite)
---
- [custom:battery-state-card] : sensor.contact_fenetre_bureau_sonoff_battery (NAT), sensor.contact_fenetre_chambre_sonoff_battery (NAT), sensor.contact_fenetre_cuisine_sonoff_battery (NAT), sensor.contact_fenetre_salon_sonoff_battery (NAT), sensor.gm1901_battery_level (NAT), sensor.ne2213_ (NAT), sensor.sm_a530f_battery_level (NAT), sensor.tablette_battery_level (NAT)
---
- [heading] Batteries — thermostats SONOFF (aucune entite)
---
- [custom:battery-state-card] : sensor.gm1901_battery_level (NAT), sensor.ne2213_ (NAT), sensor.sm_a530f_battery_level (NAT), sensor.tablette_battery_level (NAT), sensor.th_balcon_nord_battery (NAT), sensor.th_bureau_battery (NAT), sensor.th_cellier_battery (NAT), sensor.th_chambre_battery (NAT), sensor.th_cuisine_battery (NAT), sensor.th_salle_de_bain_battery (NAT), sensor.th_salon_battery (NAT)

#### vignette_L5C1_batteries_piles_2026-05-14.yaml (1 cartes, 3 entites)

- [custom:button-card] : group.hue_devices (NAT), group.ikea_devices (NAT), group.sonoff_devices (NAT)

### L5C2 - Batteries_Portables

*Validée le 2026-05-12 - ⚠️ todo: vérifier sensor.ne2213_mamour_battery_health + temperature*

*49 entites, 35 cartes, 3 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 49)
        └─→ VIGNETTE L5C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eric_battery_health` | NAT | (native/UI) |
| `sensor.eric_battery_level` | NAT | idem |
| `sensor.eric_battery_state` | NAT | idem |
| `sensor.eric_battery_temperature` | NAT | idem |
| `sensor.eric_charger_type` | NAT | idem |
| `sensor.eric_network_type` | NAT | idem |
| `sensor.eric_wi_fi_connection` | NAT | idem |
| `sensor.gm1901_battery_health` | NAT | idem |
| `sensor.gm1901_battery_level` | NAT | idem |
| `sensor.gm1901_battery_state` | NAT | idem |
| `sensor.gm1901_battery_temperature` | NAT | idem |
| `sensor.gm1901_charger_type` | NAT | idem |
| `sensor.gm1901_network_type` | NAT | idem |
| `sensor.gm1901_wi_fi_connection` | NAT | idem |
| `sensor.mamour_battery_health` | NAT | idem |
| `sensor.mamour_battery_level` | NAT | idem |
| `sensor.mamour_battery_state` | NAT | idem |
| `sensor.mamour_battery_temperature` | NAT | idem |
| `sensor.mamour_charger_type` | NAT | idem |
| `sensor.mamour_network_type` | NAT | idem |
| `sensor.mamour_wi_fi_connection` | NAT | idem |
| `sensor.ne2213_eric_battery_health` | NAT | idem |
| `sensor.ne2213_eric_battery_level` | NAT | idem |
| `sensor.ne2213_eric_battery_state` | NAT | idem |
| `sensor.ne2213_eric_battery_temperature` | NAT | idem |
| `sensor.ne2213_eric_charger_type` | NAT | idem |
| `sensor.ne2213_eric_network_type` | NAT | idem |
| `sensor.ne2213_eric_wi_fi_connection` | NAT | idem |
| `sensor.ne2213_mamour_battery_health` | NAT | idem |
| `sensor.ne2213_mamour_battery_level` | NAT | idem |
| `sensor.ne2213_mamour_battery_state` | NAT | idem |
| `sensor.ne2213_mamour_battery_temperature` | NAT | idem |
| `sensor.ne2213_mamour_charger_type` | NAT | idem |
| `sensor.ne2213_mamour_network_type` | NAT | idem |
| `sensor.ne2213_mamour_wi_fi_connection` | NAT | idem |
| `sensor.sm_a530f_battery_health` | NAT | idem |
| `sensor.sm_a530f_battery_level` | NAT | idem |
| `sensor.sm_a530f_battery_state` | NAT | idem |
| `sensor.sm_a530f_battery_temperature` | NAT | idem |
| `sensor.sm_a530f_charger_type` | NAT | idem |
| `sensor.sm_a530f_network_type` | NAT | idem |
| `sensor.sm_a530f_wi_fi_connection` | NAT | idem |
| `sensor.tablette_battery_health` | NAT | idem |
| `sensor.tablette_battery_level` | NAT | idem |
| `sensor.tablette_battery_state` | NAT | idem |
| `sensor.tablette_battery_temperature` | NAT | idem |
| `sensor.tablette_charger_type` | NAT | idem |
| `sensor.tablette_network_type` | NAT | idem |
| `sensor.tablette_wi_fi_connection` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L5C2_batteries_portables_droite_2026-05-12.yaml` | ✅ |
| `page_L5C2_batteries_portables_gauche_2026-05-12.yaml` | ✅ |
| `vignette_L5C2_batteries_portables_2026-05-12.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L5C2_batteries_portables_droite_2026-05-12.yaml (13 cartes, 21 entites)

- [grid]  (aucune entite)
---
- [heading] Xiaomi POCO X7 Pro Mamour (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.mamour_battery_level (NAT)
---
- [entities] : sensor.mamour_battery_health (NAT), sensor.mamour_battery_level (NAT), sensor.mamour_battery_state (NAT), sensor.mamour_battery_temperature (NAT), sensor.mamour_charger_type (NAT), sensor.mamour_network_type (NAT), sensor.mamour_wi_fi_connection (NAT)
---
- [heading] Oneplus 10Pro NE2213 (M) (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.ne2213_mamour_battery_level (NAT)
---
- [entities] : sensor.ne2213_mamour_battery_health (NAT), sensor.ne2213_mamour_battery_level (NAT), sensor.ne2213_mamour_battery_state (NAT), sensor.ne2213_mamour_battery_temperature (NAT), sensor.ne2213_mamour_charger_type (NAT), sensor.ne2213_mamour_network_type (NAT), sensor.ne2213_mamour_wi_fi_connection (NAT)
---
- [heading] Oneplus 7 GM1901 (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.gm1901_battery_level (NAT)
---
- [entities] : sensor.gm1901_battery_health (NAT), sensor.gm1901_battery_level (NAT), sensor.gm1901_battery_state (NAT), sensor.gm1901_battery_temperature (NAT), sensor.gm1901_charger_type (NAT), sensor.gm1901_network_type (NAT), sensor.gm1901_wi_fi_connection (NAT)

#### page_L5C2_batteries_portables_gauche_2026-05-12.yaml (21 cartes, 28 entites)

- [grid]  (aucune entite)
---
- [heading] Xiaomi POCO X7 Pro (aucune entite)
---
- [conditional] : sensor.eric_battery_level (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.eric_battery_level (NAT)
---
- [entities] : sensor.eric_battery_health (NAT), sensor.eric_battery_level (NAT), sensor.eric_battery_state (NAT), sensor.eric_battery_temperature (NAT), sensor.eric_charger_type (NAT), sensor.eric_network_type (NAT), sensor.eric_wi_fi_connection (NAT)
---
- [heading] Oneplus 10Pro NE2213 (E) (aucune entite)
---
- [conditional] : sensor.ne2213_eric_battery_level (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.ne2213_eric_battery_level (NAT)
---
- [entities] : sensor.ne2213_eric_battery_health (NAT), sensor.ne2213_eric_battery_level (NAT), sensor.ne2213_eric_battery_state (NAT), sensor.ne2213_eric_battery_temperature (NAT), sensor.ne2213_eric_charger_type (NAT), sensor.ne2213_eric_network_type (NAT), sensor.ne2213_eric_wi_fi_connection (NAT)
---
- [heading] Samsung A8 SM-A530F (aucune entite)
---
- [conditional] : sensor.sm_a530f_battery_level (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.sm_a530f_battery_level (NAT)
---
- [entities] : sensor.sm_a530f_battery_health (NAT), sensor.sm_a530f_battery_level (NAT), sensor.sm_a530f_battery_state (NAT), sensor.sm_a530f_battery_temperature (NAT), sensor.sm_a530f_charger_type (NAT), sensor.sm_a530f_network_type (NAT), sensor.sm_a530f_wi_fi_connection (NAT)
---
- [heading] Tablette (aucune entite)
---
- [conditional] : sensor.tablette_battery_level (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:streamline-card] : sensor.tablette_battery_level (NAT)
---
- [entities] : sensor.tablette_battery_health (NAT), sensor.tablette_battery_level (NAT), sensor.tablette_battery_state (NAT), sensor.tablette_battery_temperature (NAT), sensor.tablette_charger_type (NAT), sensor.tablette_network_type (NAT), sensor.tablette_wi_fi_connection (NAT)

#### vignette_L5C2_batteries_portables_2026-05-12.yaml (1 cartes, 14 entites)

- [custom:button-card] : sensor.eric_battery_level (NAT), sensor.eric_battery_state (NAT), sensor.gm1901_battery_level (NAT), sensor.gm1901_battery_state (NAT), sensor.mamour_battery_level (NAT), sensor.mamour_battery_state (NAT), sensor.ne2213_eric_battery_level (NAT), sensor.ne2213_eric_battery_state (NAT), sensor.ne2213_mamour_battery_level (NAT), sensor.ne2213_mamour_battery_state (NAT), sensor.sm_a530f_battery_level (NAT), sensor.sm_a530f_battery_state (NAT), sensor.tablette_battery_level (NAT), sensor.tablette_battery_state (NAT)

### L5C3 - MariaDB

*Validée le 2026-05-10*

*25 entites, 73 cartes, 8 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 25)
        └─→ VIGNETTE L5C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `automation.db_purge_mariadb_repack` | NAT | (native/UI) |
| `script.audit_md5` | NAT | idem |
| `script.audit_md5_docs` | NAT | idem |
| `sensor.audit_md5_docs_journal` | NAT | idem |
| `sensor.audit_md5_journal` | NAT | idem |
| `sensor.backup_github_journal` | NAT | idem |
| `sensor.backup_github_status` | NAT | idem |
| `sensor.git_last_weekly_tag` | NAT | idem |
| `sensor.github_default_branch` | NAT | idem |
| `sensor.homeassistant_memory_usage_percentage` | NAT | idem |
| `sensor.homeassistant_uptime` | NAT | idem |
| `sensor.homeassistant_utilisation_de_la_memoire` | NAT | idem |
| `sensor.homeassistant_utilisation_du_processeur` | NAT | idem |
| `sensor.mariadb_memory_usage_percentage` | NAT | idem |
| `sensor.mariadb_uptime` | NAT | idem |
| `sensor.mariadb_utilisation_de_la_memoire` | NAT | idem |
| `sensor.mariadb_utilisation_du_processeur` | NAT | idem |
| `sensor.taille_db_home_assistant` | NAT | idem |
| `sensor.z2m_memory_usage_percentage` | NAT | idem |
| `sensor.z2m_uptime` | NAT | idem |
| `sensor.z2m_utilisation_de_la_memoire` | NAT | idem |
| `sensor.z2m_utilisation_du_processeur` | NAT | idem |
| `shell_command.audit_md5` | NAT | idem |
| `shell_command.git_backup_push_manual` | NAT | idem |
| `shell_command.git_backup_push_weekly` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_audit_buttons_2026-06-14.yaml` | ✅ |
| `card_audit_journal_2026-06-14.yaml` | ✅ |
| `card_audit_md5_2026-06-15.yaml` | ✅ |
| `card_audit_recap_2026-06-15.yaml` | ✅ |
| `card_mariadb_2026-05-18.yaml` | ✅ |
| `page_L5C3_mariadb_2026-08-08.yaml` | ✅ |
| `page_L5C3_systeme_reserve_2026-05-18.yaml` | ✅ |
| `vignette_L5C3_mariadb_2026-05-10.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_audit_buttons_2026-06-14.yaml (4 cartes, 1 entites)

- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-title-card] 🔍 Audit MD5 GitHub (aucune entite)
---
- [button] LANCER AUDIT MD5: shell_command.audit_md5 (NAT)
---
- [markdown]  (aucune entite)

#### card_audit_journal_2026-06-14.yaml (3 cartes, 1 entites)

- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-title-card] Journal Audit MD5 (25 dernières lignes) (aucune entite)
---
- [markdown] : sensor.audit_md5_journal (NAT)

#### card_audit_md5_2026-06-15.yaml (5 cartes, 2 entites)

- [vertical-stack]  (aucune entite)
---
- [custom:bubble-card] Audit GitHub MD5 (aucune entite)
---
- [custom:button-card] [[[
  return entity.state === 'on' ? 'Audit en cours...' : ': script.audit_md5 (NAT)
---
- [custom:button-card] : script.audit_md5 (NAT)
---
- [markdown] : sensor.audit_md5_journal (NAT)

#### card_audit_recap_2026-06-15.yaml (4 cartes, 2 entites)

- [vertical-stack]  (aucune entite)
---
- [custom:bubble-card] MD5 (aucune entite)
---
- [custom:button-card] Lancer Audit MD5: shell_command.audit_md5 (NAT)
---
- [markdown] : sensor.audit_md5_journal (NAT)

#### card_mariadb_2026-05-18.yaml (2 cartes, 1 entites)

- [custom:button-card] Taille DB MariaDB: sensor.taille_db_home_assistant (NAT)
---
- [custom:flex-horseshoe-card] : sensor.taille_db_home_assistant (NAT)

#### page_L5C3_mariadb_2026-08-08.yaml (28 cartes, 12 entites)

- [grid]  (aucune entite)
---
- [heading] Système (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:bubble-card] Audit MD5 GitHub (aucune entite)
---
- [custom:button-card] [[[
  return entity.state === 'on' ? 'Audit en cours...' : ': script.audit_md5 (NAT)
---
- [custom:button-card] : script.audit_md5 (NAT)
---
- [markdown] : sensor.audit_md5_journal (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [custom:bubble-card] Audit MD5 Docs (aucune entite)
---
- [custom:button-card] [[[
  return entity.state === 'on' ? 'Audit en cours...' : ': script.audit_md5_docs (NAT)
---
- [custom:button-card] : script.audit_md5_docs (NAT)
---
- [markdown] : sensor.audit_md5_docs_journal (NAT)
---
- [custom:bubble-card] GitHub (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [template] : sensor.backup_github_status (NAT)
---
- [custom:mushroom-chips-card]  (aucune entite)
---
- [template] : sensor.git_last_weekly_tag (NAT), shell_command.git_backup_push_weekly (NAT)
---
- [template] : sensor.github_default_branch (NAT)
---
- [template] : shell_command.git_backup_push_manual (NAT)
---
- [custom:mushroom-title-card] Journal Backup (10 derniers) (aucune entite)
---
- [markdown] : sensor.backup_github_journal (NAT)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [column] Statut: sensor.backup_github_status (NAT)
---
- [custom:bubble-card] MariaDB (aucune entite)
---
- [custom:apexcharts-card]  (aucune entite)
---
- [area] Taille (MiB): sensor.taille_db_home_assistant (NAT)
---
- [custom:button-card] [DB] Purge MariaDB + Repack: automation.db_purge_mariadb_repack (NAT)

#### page_L5C3_systeme_reserve_2026-05-18.yaml (25 cartes, 12 entites)

- [custom:button-card] Réserve Système (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:button-card] HOME ASSISTANT (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.homeassistant_utilisation_du_processeur (NAT)
---
- [custom:bar-card] : sensor.homeassistant_uptime (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.homeassistant_memory_usage_percentage (NAT)
---
- [custom:bar-card] : sensor.homeassistant_utilisation_de_la_memoire (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:button-card] ZIGBEE2MQTT (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.z2m_utilisation_du_processeur (NAT)
---
- [custom:bar-card] : sensor.z2m_uptime (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.z2m_memory_usage_percentage (NAT)
---
- [custom:bar-card] : sensor.z2m_utilisation_de_la_memoire (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:button-card] MARIADB (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.mariadb_utilisation_du_processeur (NAT)
---
- [custom:bar-card] : sensor.mariadb_uptime (NAT)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:bar-card] : sensor.mariadb_memory_usage_percentage (NAT)
---
- [custom:bar-card] : sensor.mariadb_utilisation_de_la_memoire (NAT)

#### vignette_L5C3_mariadb_2026-05-10.yaml (2 cartes, 1 entites)

- [custom:button-card]  (aucune entite)
---
- [custom:flex-horseshoe-card] : sensor.taille_db_home_assistant (NAT)

### L6C1 - Air_Qualite

*Validée le 2026-05-14*

*15 entites, 30 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 6)
  └─→ TPL: A_01_AIR_QUALITY.yaml (3)
  └─→ SEN: A_01_AIR_QUALITY.yaml (6)
        └─→ VIGNETTE L6C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_air_bureau_ikea_pm25` | NAT | (native/UI) |
| `sensor.qualite_air_bureau_ikea_voc_index` | NAT | idem |
| `sensor.qualite_air_chambre_ikea_pm25` | NAT | idem |
| `sensor.qualite_air_chambre_ikea_voc_index` | NAT | idem |
| `sensor.qualite_air_salon_ikea_pm25` | NAT | idem |
| `sensor.qualite_air_salon_ikea_voc_index` | NAT | idem |
| `sensor.pm2_5_bureau_moy_24h` | SEN | A_01_AIR_QUALITY.yaml |
| `sensor.pm2_5_chambre_moy_24h` | SEN | idem |
| `sensor.pm2_5_salon_moy_24h` | SEN | idem |
| `sensor.tcov_bureau_moy_24h` | SEN | idem |
| `sensor.tcov_chambre_moy_24h` | SEN | idem |
| `sensor.tcov_salon_moy_24h` | SEN | idem |
| `sensor.tcov_bureau_ppb` | TPL | idem |
| `sensor.tcov_chambre_ppb` | TPL | idem |
| `sensor.tcov_salon_ppb` | TPL | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L6C1_air_qualite_2026-05-23.yaml` | ✅ |
| `vignette_L6C1_air_qualite_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L6C1_air_qualite_2026-05-23.yaml (29 cartes, 15 entites)

- [grid]  (aucune entite)
---
- [heading] AIR QUALITY (aucune entite)
---
- [custom:bubble-card] SALON (aucune entite)
---
- [custom:streamline-card] : sensor.pm2_5_salon_moy_24h (SEN), sensor.qualite_air_salon_ikea_pm25 (NAT)
---
- [custom:streamline-card] : sensor.tcov_salon_moy_24h (SEN), sensor.tcov_salon_ppb (TPL)
---
- [custom:bubble-card] Graph. PM2.5 Salon: sensor.qualite_air_salon_ikea_pm25 (NAT)
---
- [custom:bubble-card] Graph. tCOV Salon: sensor.tcov_salon_ppb (TPL)
---
- [custom:bubble-card] Air Quality SALON (aucune entite)
---
- [custom:streamline-card] : sensor.pm2_5_salon_moy_24h (SEN), sensor.qualite_air_salon_ikea_pm25 (NAT)
---
- [custom:bubble-card] Air Quality SALON (aucune entite)
---
- [custom:streamline-card] : sensor.qualite_air_salon_ikea_voc_index (NAT), sensor.tcov_salon_moy_24h (SEN)
---
- [custom:bubble-card] BUREAU (aucune entite)
---
- [custom:streamline-card] : sensor.pm2_5_bureau_moy_24h (SEN), sensor.qualite_air_bureau_ikea_pm25 (NAT)
---
- [custom:streamline-card] : sensor.tcov_bureau_moy_24h (SEN), sensor.tcov_bureau_ppb (TPL)
---
- [custom:bubble-card] Graph. PM2.5 Bureau: sensor.qualite_air_bureau_ikea_pm25 (NAT)
---
- [custom:bubble-card] Graph. tCOV Bureau: sensor.tcov_bureau_ppb (TPL)
---
- [custom:bubble-card] Air Quality BUREAU (aucune entite)
---
- [custom:streamline-card] : sensor.pm2_5_bureau_moy_24h (SEN), sensor.qualite_air_bureau_ikea_pm25 (NAT)
---
- [custom:bubble-card] Air Quality BUREAU (aucune entite)
---
- [custom:streamline-card] : sensor.qualite_air_bureau_ikea_voc_index (NAT), sensor.tcov_bureau_moy_24h (SEN)
---
- [custom:bubble-card] CHAMBRE (aucune entite)
---
- [custom:streamline-card] : sensor.pm2_5_chambre_moy_24h (SEN), sensor.qualite_air_chambre_ikea_pm25 (NAT)
---
- [custom:streamline-card] : sensor.tcov_chambre_moy_24h (SEN), sensor.tcov_chambre_ppb (TPL)
---
- [custom:bubble-card] Graph. PM2.5 Chambre: sensor.qualite_air_chambre_ikea_pm25 (NAT)
---
- [custom:bubble-card] Graph. tCOV Chambre: sensor.tcov_chambre_ppb (TPL)
---
- [custom:bubble-card] Air Quality CHAMBRE (aucune entite)
---
- [custom:streamline-card] : sensor.pm2_5_chambre_moy_24h (SEN), sensor.qualite_air_chambre_ikea_pm25 (NAT)
---
- [custom:bubble-card] Air Quality CHAMBRE (aucune entite)
---
- [custom:streamline-card] : sensor.qualite_air_chambre_ikea_voc_index (NAT), sensor.tcov_chambre_moy_24h (SEN)

#### vignette_L6C1_air_qualite_2026-05-14.yaml (1 cartes, 6 entites)

- [custom:button-card] : sensor.qualite_air_bureau_ikea_pm25 (NAT), sensor.qualite_air_bureau_ikea_voc_index (NAT), sensor.qualite_air_chambre_ikea_pm25 (NAT), sensor.qualite_air_chambre_ikea_voc_index (NAT), sensor.qualite_air_salon_ikea_pm25 (NAT), sensor.qualite_air_salon_ikea_voc_index (NAT)

### L6C2 - Pollution_Pollen

*Validée le 2026-05-14*

*19 entites, 32 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 19)
        └─→ VIGNETTE L6C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.concentration_ambroisie_vence` | NAT | (native/UI) |
| `sensor.concentration_armoise_vence` | NAT | idem |
| `sensor.concentration_aulne_vence` | NAT | idem |
| `sensor.concentration_bouleau_vence` | NAT | idem |
| `sensor.concentration_gramine_vence` | NAT | idem |
| `sensor.concentration_olivier_vence` | NAT | idem |
| `sensor.dioxyde_d_azote_vence` | NAT | idem |
| `sensor.dioxyde_de_soufre_vence` | NAT | idem |
| `sensor.niveau_ambroisie_vence` | NAT | idem |
| `sensor.niveau_armoise_vence` | NAT | idem |
| `sensor.niveau_aulne_vence` | NAT | idem |
| `sensor.niveau_bouleau_vence` | NAT | idem |
| `sensor.niveau_gramine_vence` | NAT | idem |
| `sensor.niveau_olivier_vence` | NAT | idem |
| `sensor.ozone_vence` | NAT | idem |
| `sensor.pm10_vence` | NAT | idem |
| `sensor.pm25_vence` | NAT | idem |
| `sensor.qualite_globale_pollen_vence` | NAT | idem |
| `sensor.qualite_globale_vence` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L6C2_pollution_pollen_2026-06-13.yaml` | ✅ |
| `vignette_L6C2_pollution_pollen_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L6C2_pollution_pollen_2026-06-13.yaml (31 cartes, 19 entites)

- [grid]  (aucune entite)
---
- [heading] POLLULÈNE © (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:entity-progress-card] Qualité Pollens: sensor.qualite_globale_pollen_vence (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [grid]  (aucune entite)
---
- [custom:ring-tile] Graminées: sensor.concentration_gramine_vence (NAT), sensor.niveau_gramine_vence (NAT)
---
- [custom:ring-tile] Ambroisie: sensor.concentration_ambroisie_vence (NAT), sensor.niveau_ambroisie_vence (NAT)
---
- [custom:ring-tile] Armoise: sensor.concentration_armoise_vence (NAT), sensor.niveau_armoise_vence (NAT)
---
- [custom:ring-tile] Aulne: sensor.concentration_aulne_vence (NAT), sensor.niveau_aulne_vence (NAT)
---
- [custom:ring-tile] Bouleau: sensor.concentration_bouleau_vence (NAT), sensor.niveau_bouleau_vence (NAT)
---
- [custom:ring-tile] Olivier: sensor.concentration_olivier_vence (NAT), sensor.niveau_olivier_vence (NAT)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:vertical-stack-in-card]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [custom:entity-progress-card] Qualité Air: sensor.qualite_globale_vence (NAT)
---
- [vertical-stack]  (aucune entite)
---
- [vertical-stack]  (aucune entite)
---
- [grid]  (aucune entite)
---
- [custom:ring-tile] O₃ (Ozone): sensor.ozone_vence (NAT)
---
- [custom:ring-tile] NO₂ (Azote): sensor.dioxyde_d_azote_vence (NAT)
---
- [custom:ring-tile] SO₂ (Souffre): sensor.dioxyde_de_soufre_vence (NAT)
---
- [custom:ring-tile] PM10: sensor.pm10_vence (NAT)
---
- [custom:ring-tile] PM25: sensor.pm25_vence (NAT)

#### vignette_L6C2_pollution_pollen_2026-05-14.yaml (1 cartes, 2 entites)

- [custom:button-card] [[[
  var airQuality = states['sensor.qualite_globale_vence': sensor.qualite_globale_pollen_vence (NAT), sensor.qualite_globale_vence (NAT)

### L6C3 - VigiEau

*Validée le 2026-05-14*

*2 entites, 16 cartes, 2 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 2)
        └─→ VIGNETTE L6C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.alert_level_in_vence` | NAT | (native/UI) |
| `sensor.alert_level_in_vence_numeric` | NAT | idem |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `page_L6C3_vigieau_2026-05-14.yaml` | ✅ |
| `vignette_L6C3_vigieau_2026-05-14.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### page_L6C3_vigieau_2026-05-14.yaml (15 cartes, 2 entites)

- [grid]  (aucune entite)
---
- [heading] VIGIEAU / VIGI - EAU (aucune entite)
---
- [custom:stack-in-card]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:text-divider-row]  (aucune entite)
---
- [custom:mod-card]  (aucune entite)
---
- [horizontal-stack]  (aucune entite)
---
- [custom:button-card] Vigi - Eau Vence:: sensor.alert_level_in_vence (NAT)
---
- [custom:bar-card] : sensor.alert_level_in_vence_numeric (NAT)
---
- [conditional] : sensor.alert_level_in_vence (NAT)
---
- [custom:mod-card]  (aucune entite)
---
- [custom:auto-entities]  (aucune entite)
---
- [grid]  (aucune entite)
---
- [custom:button-card] [[[ return entity.attributes.friendly_name; ]]] (aucune entite)
---
- [custom:button-card] [[[ return entity.attributes.friendly_name; ]]] (aucune entite)

#### vignette_L6C3_vigieau_2026-05-14.yaml (1 cartes, 1 entites)

- [custom:button-card] [[[
  var sensor = states['sensor.alert_level_in_vence'];
  : sensor.alert_level_in_vence (NAT)

## 2. SCRIPTS .SH

### audit_md5.sh
*docs\04_docs_scripts\docs_scripts_SH\audit_md5.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### audit_md5_md.sh
*scripts\audit_md5_md.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### audit_md5_yaml.sh
*scripts\audit_md5_yaml.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### ha_git_backup.sh
*scripts\ha_git_backup.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### hermes_audit_md5_docs.sh
*docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_docs.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### hermes_audit_md5_trigul_3md.sh
*docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### setup_z2m.sh
*Infra_Proxmox\setup_z2m.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### snapshot_rolling.sh
*Infra_Proxmox\snapshot_rolling.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

## 3. AUTOMATIONS (PAR POLE)

### Pole P1_clim_chauffage (12 automations)

#### P1_clim_chauffage/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml
*14 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
script.p1_master_gestion_clim
sensor.eric_network_type
sensor.mamour_network_type
sensor.mode_ete_hiver
sensor.temperature_cible
sensor.temperature_confort_jour
sensor.th_balcon_nord_temperature
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

#### P1_clim_chauffage/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml
*14 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
script.p1_master_gestion_clim
sensor.eric_network_type
sensor.mamour_network_type
sensor.mode_ete_hiver
sensor.temperature_cible
sensor.temperature_confort_nuit
sensor.th_balcon_nord_temperature
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

#### P1_clim_chauffage/c_notification_temperature_up_ou_down_7h30_21h00.yaml
*5 entites*

```
notify.mobile_app_eric
sensor.eric_wi_fi_connection
sensor.mamour_wi_fi_connection
sensor.message_clim_personnalise_7h30_21h00
sensor.th_balcon_nord_temperature
```

#### P1_clim_chauffage/d_notification_temperature_up_ou_down_21h00_7h30.yaml
*5 entites*

```
notify.mobile_app_eric
sensor.eric_wi_fi_connection
sensor.mamour_wi_fi_connection
sensor.message_clim_personnalise_21h00_7h30
sensor.th_balcon_nord_temperature
```

#### P1_clim_chauffage/e_clim_notification_de_fermeture_des_fenetres.yaml
*6 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
notify.mobile_app_eric
sensor.nombre_de_fenetres_fermees
```

#### P1_clim_chauffage/f_clim_automatisation_arret_clim_notification.yaml
*11 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
notify.mobile_app_eric
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

#### P1_clim_chauffage/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml
*3 entites*

```
notify.mobile_app_eric
sensor.mode_ete_hiver
sensor.mode_ete_hiver_etat
```

#### P1_clim_chauffage/h_clim_debug_force_mode_correct_securite.yaml
*11 entites*

```
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
input_boolean.clim_bureau_arret_securise_en_cours
input_boolean.clim_chambre_arret_securise_en_cours
input_boolean.clim_salon_arret_securise_en_cours
notify.mobile_app_eric
sensor.mode_ete_hiver
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

#### P1_clim_chauffage/i_synchro_notif_clim_si_prise_coupee.yaml
*7 entites*

```
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
notify.mobile_app_eric
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

#### P1_clim_chauffage/j_debug_notifier_les_changements_de_message_clim_mobile.yaml
*2 entites*

```
notify.mobile_app_eric
sensor.message_clim_personnalise_7h30_21h00
```

#### P1_clim_chauffage/old/A0_clim_jour_2026-01-01.yaml
*24 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
input_boolean.clim_bureau_arret_securise_en_cours
input_boolean.clim_chambre_arret_securise_en_cours
input_boolean.clim_salon_arret_securise_en_cours
notify.mobile_app_eric
sensor.eric_network_type
sensor.mamour_network_type
sensor.mode_ete_hiver
sensor.presence
sensor.temperature_cible
sensor.temperature_confort_jour
sensor.temperature_corrige_eric_hivers
sensor.temperature_corrige_mamour_hivers
sensor.temperature_eco_hiver_corrige
sensor.th_balcon_nord_temperature
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

#### P1_clim_chauffage/old/B0_clim_nuit_2026-01-02.yaml
*24 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
input_boolean.clim_bureau_arret_securise_en_cours
input_boolean.clim_chambre_arret_securise_en_cours
input_boolean.clim_salon_arret_securise_en_cours
notify.mobile_app_eric
sensor.eric_network_type
sensor.mamour_network_type
sensor.mode_ete_hiver
sensor.presence
sensor.temperature_cible
sensor.temperature_confort_nuit
sensor.temperature_corrige_eric_hivers
sensor.temperature_corrige_mamour_hivers
sensor.temperature_eco_hiver_corrige
sensor.th_balcon_nord_temperature
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

### Pole P1_cuisine (2 automations)

#### P1_cuisine/a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml
*6 entites*

```
climate.radiateur_cuisine
notify.mobile_app_eric
person.eric
person.mamour
sensor.th_cuisine_temperature
zone.home
```

#### P1_cuisine/b_chauffage_cuisine_vacances.yaml
*6 entites*

```
climate.radiateur_cuisine
notify.mobile_app_eric
person.eric
person.mamour
sensor.th_cuisine_temperature
zone.home
```

### Pole P1_sdb (3 automations)

#### P1_sdb/a_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml
*5 entites*

```
climate.soufflant_salle_de_bain
input_select.etat_resistance_soufflant_sdb
sensor.th_salle_de_bain_temperature
switch.inter_soufflant_salle_de_bain
switch.prise_soufflant_salle_de_bain_nous
```

#### P1_sdb/d_salle_de_bain_watchdog_securite_radiateur.yaml
*4 entites*

```
input_boolean.inter_soufflant_salle_de_bain
notify.mobile_app_eric
sensor.th_salle_de_bain_temperature
switch.prise_soufflant_salle_de_bain_nous
```

#### P1_sdb/e_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml
*3 entites*

```
notify.mobile_app_eric
sensor.prise_seche_serviette_salle_de_bain_nous_power
switch.prise_seche_serviette_salle_de_bain_nous
```

### Pole P2_prises (3 automations)

#### P2_prises/eco_prises_dinamique_by_presence_groupe.yaml
*2 entites*

```
notify.mobile_app_eric
sensor.eco_prises_config
```

#### P2_prises/gestion_pc_bureau_scene_de_fin_notif.yaml
*3 entites*

```
light.hue_smart_eco_pc_bureau
notify.mobile_app_eric
sensor.prise_bureau_pc_ikea_power
```

#### P2_prises/gestion_tv_chambre_scene_de_fin_notif.yaml
*4 entites*

```
light.hue_smart_eco_tv_chambre
notify.mobile_app_eric
sensor.prise_tv_chambre_nous_power
switch.prise_tv_chambre_nous
```

### Pole P3_eclairage (8 automations)

#### P3_eclairage/p3_bureau_activation_ecran_synchro.yaml
*2 entites*

```
binary_sensor.moniteur_pc
switch.ecran_p_c_3_play_hue
```

#### P3_eclairage/p3_bureau_bouton_rodret_toggle_blanches.yaml
*3 entites*

```
light.hue_white_lamp_bureau_1
light.hue_white_lamp_bureau_2
sensor.bureau_etat
```

#### P3_eclairage/p3_bureau_forcer_play_on_si_pc_tourne.yaml
*4 entites*

```
binary_sensor.moniteur_pc
light.hue_play_1_pc_bureau
light.hue_play_2_pc_bureau
light.hue_play_3_pc_bureau
```

#### P3_eclairage/p3_bureau_watchdog_synchronisation_lampes_blanches.yaml
*3 entites*

```
light.hue_white_lamp_bureau_1
light.hue_white_lamp_bureau_2
sensor.bureau_etat
```

#### P3_eclairage/p3_entree_allumage_lumiere.yaml
*2 entites*

```
light.entree
sun.sun
```

#### P3_eclairage/p3_salon_bouton_ikea_inter_salon.yaml
*1 entites*

```
light.salon
```

#### P3_eclairage/p3_salon_bouton_ikea_somrig.yaml
*1 entites*

```
light.salon
```

#### P3_eclairage/p3_sdb_sync_miroir_lampe_et_relais_sdb.yaml
*3 entites*

```
light.hue_white_lamp_salle_de_bain
switch.relais_lumiere_sdb_sonoff
switch.turn_
```

### Pole P4_presence (1 automations)

#### P4_presence/P4_log_zones_eric.yaml
*3 entites*

```
device_tracker.poco
notify.send_message
notify.zone_eric
```

### Pole energie (2 automations)

#### energie/auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml
*4 entites*

```
select.genelec_appart_hphc_annuel_um
select.genelec_appart_hphc_hebdomadaire_um
select.genelec_appart_hphc_mensuel_um
select.genelec_appart_hphc_quotidien_um
```

#### energie/log_ecart_linky_vs_nodon.yaml
*5 entites*

```
notify.log_ecart_energie
notify.send_message
sensor.genelec_appart_quotidien_um
sensor.linky_25481620821301_consumption_history
sensor.linky_quotidien
```

### Pole meteo (5 automations)

#### meteo/alerte_meteo_france_actualisation_des_cartes.yaml
*2 entites*

```
sensor.meteo_france_alertes_image_today
sensor.meteo_france_alertes_image_tomorrow
```

#### meteo/mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml
*2 entites*

```
input_datetime.dernier_eclair
sensor.maison_lightning_counter
```

#### meteo/notification_de_la_foudre.yaml
*6 entites*

```
input_datetime.dernier_eclair
notify.mobile_app_eric
sensor.blitzortung_lightning_localisation
sensor.maison_lightning_azimuth
sensor.maison_lightning_counter
sensor.maison_lightning_distance
```

#### meteo/update_previous_humidity.yaml
*2 entites*

```
input_number.th_balcon_nord_humidity_previous
sensor.th_balcon_nord_humidity
```

#### meteo/update_previous_temperature.yaml
*2 entites*

```
input_number.th_balcon_nord_temperature_previous
sensor.th_balcon_nord_temperature
```

### Pole stores (2 automations)

#### stores/gestion_optimisee_du_store_bureau.yaml
*3 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
cover.store_bureau
sensor.th_balcon_nord_temperature
```

#### stores/gestion_simple_du_store_salon_matin_soir.yaml
*3 entites*

```
binary_sensor.contact_fenetre_salon_sonoff_contact
cover.store_salon
sun.sun
```

### Pole systeme (6 automations)

#### systeme/db_purge_mariadb_repack.yaml
*0 entites*

```
```

#### systeme/diag_enregistrement_journalier.yaml
*17 entites*

```
notify.file_diag_log_file
notify.send_message
sensor.clim_rad_total_avg_watts_quotidien
sensor.diag_poste_autre_quotidien
sensor.diag_poste_chauffage_quotidien
sensor.diag_poste_cuisine_quotidien
sensor.diag_poste_eclairage_quotidien
sensor.diag_poste_froid_quotidien
sensor.diag_poste_hygiene_quotidien
sensor.diag_poste_multimedia_quotidien
sensor.dut_clim_bureau
sensor.dut_clim_chambre
sensor.dut_clim_salon
sensor.dut_radiateur_cuisine
sensor.presence
sensor.temperature_moyenne_interieure
sensor.th_balcon_nord_temperature
```

#### systeme/systeme_economie_energie_vs_code.yaml
*3 entites*

```
binary_sensor.studio_code_server_en_cours_d_execution
notify.mobile_app_eric
sensor.studio_code_server_pourcentage_du_processeur
```

#### systeme/systeme_watchdog_piles_hue_ikea_sonoff.yaml
*4 entites*

```
group.hue_devices
group.ikea_devices
group.sonoff_devices
notify.mobile_app_eric
```

#### systeme/veille_github_nouvelle_release_detectee.yaml
*1 entites*

```
notify.mobile_app_eric
```

#### systeme/z2m_last_seen.yaml
*1 entites*

```
notify.mobile_app_eric
```

## 4. SCRIPTS NON-SH

### p1_master_gestion_clim.yaml
*04_docs_scripts\docs_scripts_YAML\p1_master_gestion_clim.yaml - 27 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
input_boolean.clim_bureau_arret_securise_en_cours
input_boolean.clim_chambre_arret_securise_en_cours
input_boolean.clim_salon_arret_securise_en_cours
notify.mobile_app_eric
sensor.consigne_de_base
sensor.mode_ete_hiver
sensor.nombre_de_fenetres_ouvertes
sensor.presence
sensor.temperature_cible
sensor.temperature_confort_nuit
sensor.temperature_corrige_chambre
sensor.temperature_corrige_eric
sensor.temperature_corrige_mamour
sensor.temperature_eco_ete
sensor.temperature_eco_ete_corrige
sensor.temperature_eco_hiver
sensor.temperature_eco_hiver_corrige
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

### scripts.yaml
*01_docs_config_system\config_system_YAML\scripts.yaml - 32 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
climate.clim_
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
input_boolean.clim_
input_boolean.clim_bureau_arret_securise_en_cours
input_boolean.clim_chambre_arret_securise_en_cours
input_boolean.clim_salon_arret_securise_en_cours
notify.mobile_app_eric
script.j_2_0_secu_arret_clim_protege
sensor.consigne_de_base
sensor.mode_ete_hiver
sensor.nombre_de_fenetres_ouvertes
sensor.presence
sensor.temperature_cible
sensor.temperature_confort_nuit
sensor.temperature_corrige_chambre
sensor.temperature_corrige_eric
sensor.temperature_corrige_mamour
sensor.temperature_eco_ete
sensor.temperature_eco_ete_corrige
sensor.temperature_eco_hiver
sensor.temperature_eco_hiver_corrige
shell_command.audit_md5
switch.clim_
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

## 5. COMPLEMENT - FICHIERS CONFIG RACINE & REPERTOIRES HORS DASHBOARD

> Ces fichiers font partie integrante de la config HA et sont audites par `audit_md5.sh`.
> Ils n'alimentent pas directement d'entites dashboard - references ici pour inventaire complet.

### Fichiers racine /config/

| Fichier | Role | Audite |
|:--------|:-----|:------:|
| `automations.yaml` | Toutes les automations HA (gere via UI) | ✅ |
| `scripts.yaml` | Scripts HA (J-1-x, J-2-0, audit_md5) | ✅ |
| `shell_command/` (repertoire) | Commandes shell (git backup, audit MD5, zone log P4) - `!include_dir_merge_named` | ✅ |
| `configuration.yaml` | Point d'entree HA - includes, integrations | ✅ |
| `sql.yaml` | Capteurs SQL (taille MariaDB) → L5C3 | ✅ |
| `input_button.yaml` | Boutons virtuels (declencheurs UI) | ✅ |
| `input_datetime.yaml` | Helpers date/heure | ✅ |
| `input_select.yaml` | Helpers liste (mode soufflant SDB, etc.) | ✅ |
| `scenes.yaml` | Scenes HA | ❌ hors scope |
| `secrets.yaml` | Identifiants - NE PAS auditer / synchroniser | ⛔ |

### Repertoires audites (DIRS)

| Repertoire | Contenu | Audite |
|:-----------|:--------|:------:|
| `sensors/` | Integrations kWh, stats min/max, qualite air | ✅ |
| `templates/` | Calculs, AVG, UI, meteo, presence, stores | ✅ |
| `utility_meter/` | Compteurs AMHQ (P0→P3, meteo) | ✅ |
| `command_line/` | Meteo France, GitHub maintenance, audit MD5, IP externe | ✅ |
| `groups/` | Groupes batteries HUE/IKEA/SONOFF → L5C1 | ✅ |
| `input_booleans/` | Helpers booleens (verrous clim, presence…) | ✅ |
| `input_number/` | Helpers numeriques | ✅ |
| `packages/` | Packages CSS meteo (cssmeteo.yaml, demometeo.yaml) - Moon API | ✅ |
| `shell_command/` | Commandes shell (backup Git, audit MD5, zone log P4) | ✅ |

### Integration FILE (UI uniquement - notify.file interdit en YAML)

> Configuree via : Parametres → Appareils & Services → Ajouter → File
> Genere des services `notify.file_*` utilises par les automations.

| Service genere | Fichier destination | Utilise par |
|:---------------|:--------------------|:------------|
| `notify.file_zone_eric_txt` | `/config/.logs/zone_eric.txt` | `shell_command/P4/P4_log_eric_zone.yaml` → automation P4 presence |
| `notify.file_diag_conso_elec_txt` | `/config/notifs/diag_conso_elec.txt` | automation `energie/diag_enregistrement_journalier.yaml` |
| `notify.file_ecart_liky_vs_nodon_txt` | `/config/notifs/ecart_liky_vs_nodon.txt` | automation `energie/log_ecart_linky_vs_nodon.yaml` |

### Repertoires hors scope audit

| Repertoire | Raison |
|:-----------|:-------|
| `.scripts/` | Scripts shell - pas des entites HA |
| `notifs/` | Fichiers .txt - hors perimetre YAML |
| `blueprints/` | Blueprints HA - non modifies manuellement |
| `custom_components/` | Integrations HACS - non versionnees ici |
| `www/` | Ressources frontend - hors config HA |
| `docs_dashboard/` | Ancien repertoire, supprime le 2026-07-14, remplace par `docs/02_docs_dashboard/` |

## 6. ENTITES ORPHELINES (NI DASHBOARD, NI AUTOMATIONS, NI SCRIPTS)

*192 reelles (potentiellement mortes) + 66 intermediaires de calcul + 23 familles (prefixes `xxx_`).*

### 5.1 Intermediaires de calcul (alimentent d'autres capteurs config)

```
sensor.all_standby_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml
sensor.dut_sdb_seche_serviettes (SEN)  ->  01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml, 01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml
sensor.dut_sdb_soufflant (SEN)  ->  01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml, 01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml
sensor.edf_tempo_price_blue_hc (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml
sensor.edf_tempo_price_blue_hp (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml
sensor.four_et_plaque_de_cuisson_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.genelec_appart_hphc_annuel_um_hc (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml
sensor.genelec_appart_hphc_annuel_um_hp (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml
sensor.genelec_appart_hphc_hebdomadaire_um_hc (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml, 02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-05-12.yaml
sensor.genelec_appart_hphc_hebdomadaire_um_hp (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml, 02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-05-12.yaml
sensor.hue_ambiance_lamp_salon_1_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_ambiance_lamp_salon_1_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_ambiance_lamp_salon_2_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_ambiance_lamp_salon_2_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_ambiance_lamp_salon_3_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_ambiance_lamp_salon_3_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_color_candle_chambre_eric_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_color_candle_chambre_eric_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_color_candle_chambre_gege_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_color_candle_chambre_gege_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_color_candle_salon_1_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_color_candle_salon_1_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_1_pc_bureau_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_1_pc_bureau_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_2_pc_bureau_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_2_pc_bureau_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_3_pc_bureau_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_3_pc_bureau_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_bureau_1_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_bureau_1_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_bureau_2_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_bureau_2_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_chambre_1_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_chambre_1_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_chambre_2_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_chambre_2_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_couloir_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_couloir_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_cuisine_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_cuisine_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_entree_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_entree_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_salle_de_bain_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_salle_de_bain_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_table_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_white_lamp_table_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.linky_25481620821301_consumption (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml, 01_docs_config_system/config_system_YAML/utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ_HPHC.yaml, 02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-05-12.yaml
sensor.prise_airfryer_ninja_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_box_internet_ikea_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_bureau_fer_a_repasser_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_bureau_pc_ikea_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_congelateur_cuisine_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_four_micro_ondes_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_frigo_cuisine_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_horloge_ikea_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_lave_linge_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_lave_vaisselle_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_pc_s_gege_ikea_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_petit_dejeune_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_salon_chargeur_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_tete_de_lit_chambre_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_tv_chambre_nous_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_tv_salon_ikea_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.radiateur_elec_cuisine_energie_totale_kwh (SEN)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_kWh_riemann_cuisine/P1_kWh_riemann_cuisine.yaml, 01_docs_config_system/config_system_YAML/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml
sensor.relais_lumiere_sdb_sonoff_annuel_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.relais_lumiere_sdb_sonoff_hebdomadaire_um_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
```

### 5.2 Reelles (definies, jamais reutilisees - candidates a suppression/verification)

```
binary_sensor.meteoalarm (NAT)  ->  01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml
binary_sensor.radiateur_salle_de_bain_actif (NAT)  ->  01_docs_config_system/config_system_YAML/input_booleans/P1/P1_BV_IB_inter_soufflant_sdb.yaml
input_boolean.inter_rodret_salon (NAT)  ->  01_docs_config_system/config_system_YAML/templates/Inter_BP_Virtuel/P3/P3_BV_IB_SW_inter_rodret_salon.yaml
input_boolean.inter_somrig_salon (NAT)  ->  01_docs_config_system/config_system_YAML/templates/Inter_BP_Virtuel/P3/P3_BV_IB_SW_inter_smorig_salon.yaml
input_boolean.inter_soufflant_sdb (NAT)  ->  01_docs_config_system/config_system_YAML/templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_sdb.yaml
input_select.saison (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml
light.hue_play_1 (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml
light.hue_smart_eco_tv_salon (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_eCO_prises/P2_eco_prises_config.yaml
notify.diag_log_file (NAT)  ->  01_docs_config_system/config_system_YAML/configuration.yaml
sensor.P1 (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml
sensor.all_standby (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml
sensor.all_standby_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml
sensor.all_standby_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml
sensor.blitzortung_lightning_last_impact_time (NAT)  ->  01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml
sensor.clim_bureau_avg_watts_annuel (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.clim_bureau_avg_watts_hebdomadaire (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.clim_bureau_power_status (NAT)  ->  01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml
sensor.clim_chambre_avg_watts_annuel (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.clim_chambre_avg_watts_hebdomadaire (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.clim_chambre_power_status (NAT)  ->  01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml
sensor.clim_salon_avg_watts_annuel (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.clim_salon_avg_watts_hebdomadaire (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.clim_salon_power_status (NAT)  ->  01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml
sensor.condition_eric_wifi (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P4_groupe_presence/P4_wifi_detection.yaml
sensor.condition_mamour_wifi (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P4_groupe_presence/P4_wifi_detection.yaml
sensor.date (NAT)  ->  01_docs_config_system/config_system_YAML/configuration.yaml
sensor.detecteur_ikea_vallhorn_battery (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_02_batteries_ikea.yaml
sensor.eclairage_total_group_puissance (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml
sensor.eclairage_total_unit_hebdomadaire_kwh_tpl (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml
sensor.four_et_plaque_de_cuisson_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.four_et_plaque_de_cuisson_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.genelec_appart_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml
sensor.genelec_appart_hebdo (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml
sensor.genelec_appart_mensuel (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml
sensor.genelec_appart_quotidien (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml
sensor.hue_ambiance_lamp_salon_1_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_1_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_1_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_1_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_1_power (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml
sensor.hue_ambiance_lamp_salon_1_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_2_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_2_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_2_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_2_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_2_power (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml
sensor.hue_ambiance_lamp_salon_2_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_3_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_3_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_3_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_3_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_ambiance_lamp_salon_3_power (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml
sensor.hue_ambiance_lamp_salon_3_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_eric_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_eric_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_eric_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_eric_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_eric_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_gege_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_gege_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_gege_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_gege_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_chambre_gege_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_salon_1_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_salon_1_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_salon_1_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_salon_1_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_color_candle_salon_1_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_1_pc_bureau_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_1_pc_bureau_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_play_1_pc_bureau_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_1_pc_bureau_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_1_pc_bureau_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_2_pc_bureau_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_2_pc_bureau_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_play_2_pc_bureau_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_2_pc_bureau_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_2_pc_bureau_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_3_pc_bureau_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_3_pc_bureau_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_play_3_pc_bureau_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_3_pc_bureau_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_play_3_pc_bureau_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_smart_button_salle_de_bain_batterie (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_01_batteries_hue.yaml
sensor.hue_white_lamp_bureau_1_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_1_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_1_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_1_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_1_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_2_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_2_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_2_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_2_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_bureau_2_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_1_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_1_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_1_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_1_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_1_power (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml
sensor.hue_white_lamp_chambre_1_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_2_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_2_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_2_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_2_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_chambre_2_power (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml
sensor.hue_white_lamp_chambre_2_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_couloir_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_couloir_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_couloir_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_couloir_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_couloir_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_cuisine_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_cuisine_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_cuisine_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_cuisine_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_cuisine_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_entree_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_entree_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_entree_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_entree_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_entree_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_salle_de_bain_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_salle_de_bain_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_salle_de_bain_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_salle_de_bain_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_salle_de_bain_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_table_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_table_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_table_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_table_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.hue_white_lamp_table_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.poussoir_pc_ikea_tradfri_battery (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_02_batteries_ikea.yaml
sensor.poussoir_tv_ikea_tradfri_battery (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_02_batteries_ikea.yaml
sensor.prise_airfryer_ninja_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_airfryer_ninja_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_box_internet_ikea_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_box_internet_ikea_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_bureau_fer_a_repasser_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_bureau_fer_a_repasser_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_bureau_pc_ikea_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_bureau_pc_ikea_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_congelateur_cuisine_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_congelateur_cuisine_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_four_micro_ondes_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_four_micro_ondes_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_frigo_cuisine_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_frigo_cuisine_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_horloge_ikea_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_horloge_ikea_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_lave_linge_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_lave_linge_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_lave_vaisselle_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_lave_vaisselle_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_mini_pc_ikea_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml
sensor.prise_mini_pc_ikea_energie_totale_wh (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml
sensor.prise_mini_pc_ikea_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml
sensor.prise_pc_s_gege_ikea_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_pc_s_gege_ikea_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_petit_dejeune_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_petit_dejeune_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_salon_chargeur_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_salon_chargeur_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_tete_de_lit_chambre_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_tete_de_lit_chambre_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_tv_chambre_nous_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_tv_chambre_nous_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.prise_tv_salon_ikea_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
sensor.prise_tv_salon_ikea_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.radiateur_cuisine_power_status (NAT)  ->  01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml
sensor.radiateur_elec_cuisine_avg_watts_annuel (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.radiateur_elec_cuisine_avg_watts_hebdomadaire (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.relais_lumiere_sdb_sonoff_annuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.relais_lumiere_sdb_sonoff_energy (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
sensor.relais_lumiere_sdb_sonoff_hebdomadaire_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.relais_lumiere_sdb_sonoff_mensuel_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.relais_lumiere_sdb_sonoff_quotidien_um (UM)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml
sensor.seche_serviette_sdb_avg_watts_annuel (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.seche_serviette_sdb_avg_watts_hebdomadaire (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.seuil_non_chauffage (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
sensor.seuil_non_clim (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
sensor.soufflant_sdb_avg_watts_annuel (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.soufflant_sdb_avg_watts_hebdomadaire (TPL)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml
sensor.tarif_heures_creuses_ttc (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml
sensor.tarif_heures_pleines_ttc (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml
sensor.temperature_corrige_Chambre (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml
sensor.th_salon (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
sensor.time (NAT)  ->  01_docs_config_system/config_system_YAML/configuration.yaml
shell_command.audit_md5_docs (NAT)  ->  01_docs_config_system/config_system_YAML/command_line/audit/audit_md5_md.yaml
switch.clim_Bureau (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml
switch.clim_Chambre (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml
switch.inter_rodret_salon (TPL)  ->  01_docs_config_system/config_system_YAML/templates/Inter_BP_Virtuel/P3/P3_BV_IB_SW_inter_rodret_salon.yaml
utility_meter.select_tariff (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ_HPHC.yaml
```

### 5.3 Familles (prefixes de templates, non resolues)

```
binary_sensor.contact_fenetre_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml
select.genelec_appart_hphc_ (NAT)  ->  01_docs_config_system/config_system_YAML/utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ_HPHC.yaml
sensor.all_standby_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml
sensor.clim_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml, 01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_03_automation_message_clim_21h_7h30.yaml
sensor.contact_fenetre_ (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_03_batteries_sonoff.yaml
sensor.eclairage_total_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.genelec_appart_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml
sensor.genelec_appart_hphc_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml, 01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml, 01_docs_config_system/config_system_YAML/utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ_HPHC.yaml
sensor.hue_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml, 01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
sensor.hue_play_1_pc_bureau_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.hue_smart_button_ (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_01_batteries_hue.yaml
sensor.hue_white_lamp_chambre_1_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.hue_white_lamp_couloir_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.hue_white_lamp_cuisine_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.hue_white_lamp_entree_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.hue_white_lamp_table_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.maison_lightning_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml
sensor.prise_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml, 01_docs_config_system/config_system_YAML/templates/P2_prise/P2_ui_dashboard/P2_ui_dashboard.yaml, 01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
sensor.qualite_air_ (NAT)  ->  01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml, 01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml
sensor.relais_lumiere_sdb_sonoff_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml
sensor.store_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/Stores/S_01_STORES.yaml
sensor.tcov_ (NAT)  ->  01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml
sensor.th_ (NAT)  ->  01_docs_config_system/config_system_YAML/groups/GRP_03_batteries_sonoff.yaml
```

## STATISTIQUES

- Total entites YAML actives : 1064
- Couvertes (dashboard + scripts sh + automations + scripts non-sh) : 783
- Orphelines : 192 reelles + 66 intermediaires + 23 familles
