# 🔗 DÉPENDANCES GLOBALES - TABLEAU DE BORD HA
*Dernière mise à jour : 2026-08-08 S3 (Section SCRIPTS créée : script.p1_master_gestion_clim documenté A/B/C/D. MATRICE DES SCRIPTS ajoutée. HOME PAGE déplacée avant L1C1. COMPLÉMENT déplacé en dernière position. Réorganisation finale : HOME PAGE > L1C1-L6C3 > AUTOMATIONS > SCRIPTS > COMPLÉMENT.)*
*2026-08-08 S1-S2 (Resync GitHub->local : 6 fichiers mis a jour. Renommage ui_dashboard -> P3_ui_dashboard en prod + local. Confirmation section tronquee. Recheck L5C3/L6C1/L6C2/L6C3 : pages manquantes ajoutées, entités audit_md5_docs ajoutées L5C3, page 05-10 supprimée. L5C2 : 2 entités fantômes NE2213 Mamour confirmées. Section AUTOMATIONS créée + enrichissement complet A/B/C/D : 49 automations, 11 groupes, hiérarchie ## groupe / ### automation / #### A/B/C/D appliquée A-Z. MATRICE DES AUTOMATIONS 49 lignes. Emoji 🗂️ sur tous les groupes.)*
*2026-07-20 (P1_01 confort_nuit : palier nuit été dynamique selon vigilance canicule - nouvelle dépendance M_01_meteo_alertes_card → P1_01_MASTER → L1C3)*
*2026-07-19 (Audit complet intégralité du fichier : L1C1 à L6C3 + HOME PAGE + Complément fichiers racine, sur la réalité des yaml prod. Corrections : entités obsolètes/fictives, mauvaise attribution de fichiers, section tronquée complétée par hypothèse. Voir détail dans les sections concernées.)*
*2026-07-18 (Nettoyage résidu chambre : capteur MQTT dispo + bloc mqtt: de configuration.yaml + dossier mqtt/, local + prod H:\ - Versions L1C3 2026-07-18 ajoutées : consigne chambre via climate direct + badge remote rétabli)*
*2026-07-17 (Resync local ← GitHub/prod : configuration.yaml + scripts.yaml - fix chambre script J-2-0)*

---

## LÉGENDE

| Symbole | Signification |
|:-------:|:-------------|
| ✅ | Chaîne validée et opérationnelle |
| 🔲 | À documenter |
| ⚠️ | Rupture de chaîne ou entité obsolète - ex : `source:` pointe vers une entité supprimée/renommée, `unique_id` dupliqué, fichier YAML présent en prod mais absent de `TREE_CORRIGE`, ou entité référencée dans le dashboard mais inexistante dans HA |
| NAT | Entité native HA (intégration directe) |
| TPL | Template (`templates/`) |
| UM | Utility Meter (`utility_meter/`) |
| SEN | Sensor (`sensors/`) |

---

## MATRICE DES 18 VIGNETTES - STATUT DÉPENDANCES

| ID | Vignette | Statut |
|:---|:---------|:------:|
| **L1C1** | **Météo** | ✅ recheck 2026-08-08 |
| **L1C2** | **Températures** | ✅ recheck 2026-08-08 |
| **L1C3** | **Commandes Clim** | ✅ recheck 2026-08-08 |
| **L2C1** | **Énergie Générale** | ✅ recheck 2026-08-08 |
| **L2C2** | **Énergie Clim / Rad / Soufflant** | ✅ recheck 2026-08-08 |
| **L2C3** | **Énergie Éclairage** | ✅ recheck 2026-08-08 |
| **L3C1** | **Commandes Éclairage** | ✅ recheck 2026-08-08 |
| **L3C2** | **Commandes Éco/Prises** | ✅ recheck 2026-08-08 |
| **L3C3** | **Stores / Fenêtres** | ✅ recheck 2026-08-08 |
| **L4C1** | **Proxmox PVE** | ✅ recheck 2026-08-08 |
| **L4C2** | **Mini-PC** | ✅ recheck 2026-08-08 |
| **L4C3** | **Mises à jour HA** | ✅ recheck 2026-08-08 |
| **L5C1** | **Batteries / Piles** | ✅ recheck 2026-08-08 |
| **L5C2** | **Batteries portables** | ✅ recheck 2026-08-08 |
| **L5C3** | **MariaDB** | ✅ recheck 2026-08-08 |
| **L6C1** | **Qualité de l'air** | ✅ recheck 2026-08-08 |
| **L6C2** | **Pollution / Pollen** | ✅ recheck 2026-08-08 |
| **L6C3** | **Vigilance Eau** | ✅ recheck 2026-08-08 |

---

## ✅ HOME PAGE - CARTES PERMANENTES (hors grille 18 vignettes)
*Validée le 2026-06-13*

> Les 18 vignettes de la grille sont documentées dans leurs sections respectives (L1C1–L6C3).
> Cette section couvre **uniquement les cartes permanentes en haut de la HOME page** qui n'appartiennent à aucune vignette.

### Chaîne de dépendances globale

```
HOME PAGE (type: grid)
  ├─→ [1] picture-elements - meteocss v2.2.1
  │     ├─→ packages/cssmeteo.yaml + custom_templates/meteo.jinja
  │     │     └─→ (fond animé ciel + foreground nuages/pluie/neige)
  │     ├─→ custom_templates/rotation.jinja
  │     │     ├─→ sensor.sun_left / sun_top / sun_opacity  (TPL meteocss)
  │     │     └─→ sensor.moon_left / moon_top / moon_opacity / moon_phase  (TPL meteocss)
  │     ├─→ sensor.moon_api (attr: moon_parallactic_angle)  (NAT - intégration Moon)
  │     ├─→ sensor.vence_original_condition  (NAT - command_line/meteo/carte_meteo_france.yaml)
  │     ├─→ sensor.th_balcon_nord_temperature  (NAT - SONOFF via Z2M)
  │     └─→ sensor.alerte_meteo  (TPL - templates/meteo/M_01_meteo_alertes_card.yaml)
  ├─→ [2] meteofrance-weather-card  (toujours visible)
  │     └─→ weather.vence + sensor.vence_* (NAT - Météo France)
  ├─→ [3] conditional - VS Code Server  (visible si CPU > 1%)
  │     └─→ sensor.studio_code_server_pourcentage_du_processeur  (NAT - Studio Code Server add-on)
  ├─→ [4] button-card - Foudre  (visible si lightning_counter > 1)
  │     ├─→ sensor.maison_lightning_counter  (NAT - Blitzortung natif, PAS un TPL)
  │     ├─→ sensor.maison_lightning_distance  (NAT - Blitzortung natif)
  │     ├─→ sensor.blitzortung_lightning_localisation  (SEN - M_meteo_sensors_blitzortung.yaml, REST Nominatim)
  │     ├─→ sensor.maison_lightning_azimuth  (NAT - Blitzortung natif)
  │     └─→ sensor.dernier_impact_temps_reel  (TPL - M_03_meteo_blitzortung.yaml, seul vrai TPL de ce bloc)
  ├─→ [5] mushroom - Lave-linge  (visible si power > 50W)
  │     └─→ sensor.prise_lave_linge_nous_power  (NAT - NOUS SP via Z2M)
  ├─→ [6] mushroom - Lave-vaisselle  (visible si power > 50W)
  │     └─→ sensor.prise_lave_vaisselle_nous_power  (NAT - NOUS SP via Z2M)
  ├─→ [7] bubble-card separator + 2× button - Présence
  │     ├─→ sensor.etat_wifi_maison  (TPL - P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml)
  │     ├─→ device_tracker.poco  (NAT - Mobile App Eric)
  │     ├─→ person.eric  (NAT - HA Personnes)
  │     ├─→ device_tracker.mamour  (NAT - Mobile App Mamour)
  │     └─→ person.mamour  (NAT - HA Personnes)
  ├─→ [8] mushroom - Détecteur fuite  (visible si on | unavailable | unknown)
  │     └─→ binary_sensor.detecteur_de_fuite_ikea_water_leak  (NAT - IKEA Vallhorn via Z2M)
  └─→ [9] type: grid - 18 vignettes  (voir sections L1C1–L6C3)
```

### Entités consommées - Cartes permanentes HOME

| Entité | Type | Fichier source | Carte |
|:-------|:----:|:--------------|:------|
| `sensor.sun_left` | TPL | `custom_templates/rotation.jinja` (meteocss) | [1] picture-elements |
| `sensor.sun_top` | TPL | idem | [1] |
| `sensor.sun_opacity` | TPL | idem | [1] |
| `sensor.moon_left` | TPL | idem | [1] |
| `sensor.moon_top` | TPL | idem | [1] |
| `sensor.moon_opacity` | TPL | idem | [1] |
| `sensor.moon_phase` | TPL | idem | [1] |
| `sensor.moon_api` (attr: `moon_parallactic_angle`) | NAT | Intégration Moon (HACS) | [1] |
| `sensor.vence_original_condition` | NAT | `command_line/meteo/carte_meteo_france.yaml` | [1] |
| `sensor.th_balcon_nord_temperature` | NAT | SONOFF via Z2M | [1] |
| `sensor.alerte_meteo` | TPL | `templates/meteo/M_01_meteo_alertes_card.yaml` | [1] |
| `weather.vence` | NAT | Météo France | [2] |
| `sensor.vence_rain_chance` / `vence_uv` / `vence_cloud_cover` | NAT | Météo France | [2] |
| `sensor.vence_freeze_chance` / `vence_snow_chance` / `vence_next_rain` | NAT | Météo France | [2] |
| `sensor.06_weather_alert` | NAT | Météo France | [2] |
| `sensor.temperature_delta_affichage` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | [2] |
| `sensor.studio_code_server_pourcentage_du_processeur` | NAT | Studio Code Server add-on | [3] |
| `sensor.maison_lightning_counter` | NAT | Intégration Blitzortung (MQTT native) | [4] |
| `sensor.maison_lightning_distance` | NAT | Intégration Blitzortung (MQTT native) | [4] |
| `sensor.blitzortung_lightning_localisation` | SEN | `sensors/meteo/M_meteo_sensors_blitzortung.yaml` (REST Nominatim) | [4] |
| `sensor.maison_lightning_azimuth` | NAT | Intégration Blitzortung (MQTT native) | [4] |
| `sensor.dernier_impact_temps_reel` | TPL | `templates/meteo/M_03_meteo_blitzortung.yaml` | [4] |
| `sensor.prise_lave_linge_nous_power` | NAT | NOUS SP via Z2M (P2 - cuisine) | [5] |
| `sensor.prise_lave_vaisselle_nous_power` | NAT | NOUS SP via Z2M (P2 - cuisine) | [6] |
| `sensor.etat_wifi_maison` | TPL | `templates/P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml` | [7] |
| `device_tracker.poco` | NAT | Mobile App (Companion) - Eric | [7] |
| `person.eric` | NAT | HA Personnes | [7] |
| `device_tracker.mamour` | NAT | Mobile App (Companion) - Mamour | [7] |
| `person.mamour` | NAT | HA Personnes | [7] |
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | NAT | IKEA Vallhorn via Z2M | [8] |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/page_home_2026-06-13.yaml` | ✅ page complète |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_meteocss_home_2026-06-13.yaml` | ✅ picture-elements 7 layers |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_vscode_home_2026-06-13.yaml` | ✅ VS Code conditional |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_foudre_home_2026-06-13.yaml` | ✅ Foudre button-card |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_lave_linge_home_2026-06-13.yaml` | ✅ Lave-linge mushroom |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_lave_vaisselle_home_2026-06-13.yaml` | ✅ Lave-vaisselle mushroom |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_presence_home_2026-06-13.yaml` | ✅ Présence (separator + Eric + Mamour) |
| `docs/02_docs_dashboard/dashboard_docs_YAML/PAGE_Home/card_detecteur_fuite_home_2026-06-13.yaml` | ✅ Détecteur fuite mushroom |

### Documentation

| Fichier | Statut |
|:--------|:------:|
| `docs_dashboard/docs/HOME PAGE/PAGE_HOME.md` | ✅ (MàJ 2026-06-13) |

---

## ✅ L1C1 - MÉTÉO (VIGNETTE + PAGE)
*Validée le 2026-05-09*

### Vignette - Chaîne de dépendances

```
AUCUNE ENTITÉ - Vignette purement navigationnelle
  └─→ tap_action: navigate → /dashboard-tablette/meteo
        └─→ PAGE MÉTÉO DÉTAILLÉE (voir ci-dessous)
```

> La vignette `custom:button-card` est statique : icône `mdi:weather-partly-cloudy`, nom "Météo".
> Aucun `triggers_update`, aucun `custom_fields`, aucune entité référencée.

### Page - Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Météo France (intégration officielle)
  │     └─→ sensor.06_weather_alert / weather.vence / sensor.vence_*  (NAT)
  ├─→ command_line: carte_meteo_france.yaml
  │     └─→ meteo_france_alertes_image_today / _tomorrow  (PNG statique - PAS d'entité camera, camera: désactivé)
  ├─→ Blitzortung (intégration MQTT native)
  │     └─→ sensor.maison_lightning_azimuth / _distance / _counter  (NAT)
  │           └─→ UM: M_03_meteo_UM_blitzortung.yaml  (eclair_annuel/mensuel/hebdomadaire/quotidien/horaire)
  │           └─→ SEN: M_meteo_sensors_blitzortung.yaml  (blitzortung_lightning_localisation - API Nominatim)
  │           └─→ TPL: M_03_meteo_blitzortung.yaml  (lightning_direction_label / _distance_km / _bearing / temps_depuis_le_dernier_impact_de_foudre / dernier_impact_temps_reel)
  ├─→ Météo France (alertes) + MeteoAlarm (fallback)
  │     └─→ sensor.06_weather_alert / binary_sensor.meteoalarm  (NAT)
  │           └─→ TPL: M_01_meteo_alertes_card.yaml  (10 sensors : alerte_vent_violent, _inondation, _orages,
  │               _pluie_inondation, _neige_verglas, _grand_froid, _canicule, _avalanches, _vagues_submersion, alerte_meteo)
  ├─→ Météo France (vent)
  │     └─→ weather.vence attributs wind_bearing / wind_speed  (NAT)
  │           └─→ TPL: M_02_meteo_vent_vence_card.yaml  (vence_wind_direction_label / _bearing / _speed_kmh)
  └─→ zone.home (latitude) + horloge système  (calculé, PAS sun.sun)
        └─→ TPL: M_05_cycle_solaire.yaml  (duree_du_jour / tendance_duree_jour / variation_quotidienne)
```

> ⚠️ Corrigé le 2026-07-19 : cette section décrivait des noms d'entités obsolètes/inexistants
> (`binary_sensor.meteo_france_alerte_*`, `sensor.meteo_france_wind_speed/_bearing`,
> `camera.carte_vigilance_meteo_france`, les 4 `*_card_content` génériques). Noms réels
> vérifiés directement dans le corps des fichiers yaml le 2026-07-19. `M_05_cycle_solaire.yaml`
> (absent de cette doc jusqu'ici) ajouté - c'est lui qui calcule la durée du jour, pas `sun.sun`.

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.meteo_france_alertes_image_today` / `_tomorrow` | NAT (command_line) | `command_line/meteo/carte_meteo_france.yaml` |
| `sensor.06_weather_alert` | NAT | Intégration Météo France |
| `weather.vence` (+ `sensor.vence_*`) | NAT | Intégration Météo France |
| `sensor.maison_lightning_azimuth` / `_distance` / `_counter` | NAT | Intégration Blitzortung (MQTT native) |
| `sensor.eclair_quotidien` / `_hebdomadaire` / `_mensuel` / `_annuel` / `_horaire` | UM | `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml` |
| `sensor.blitzortung_lightning_localisation` | SEN (REST) | `sensors/meteo/M_meteo_sensors_blitzortung.yaml` |
| `sensor.alerte_vent_violent` / `_inondation` / `_orages` / `_pluie_inondation` / `_neige_verglas` / `_grand_froid` / `_canicule` / `_avalanches` / `_vagues_submersion` / `alerte_meteo` | TPL | `templates/meteo/M_01_meteo_alertes_card.yaml` |
| `sensor.vence_wind_direction_label` / `_bearing` / `_speed_kmh` | TPL | `templates/meteo/M_02_meteo_vent_vence_card.yaml` |
| `sensor.lightning_direction_label` / `_distance_km` / `_bearing` / `temps_depuis_le_dernier_impact_de_foudre` / `dernier_impact_temps_reel` | TPL | `templates/meteo/M_03_meteo_blitzortung.yaml` |
| `sensor.duree_du_jour` / `tendance_duree_jour` / `variation_quotidienne` | TPL | `templates/meteo/M_05_cycle_solaire.yaml` (calcul astronomique zone.home, PAS sun.sun) |

### Entités ApexCharts (data_generator JS - durée du jour)

| Données | Source | Note |
|:--------|:-------|:-----|
| Durée du jour (courbe annuelle théorique) | Calcul JS astronomique | `lat = 43.72°N` - formule déclinaison + angle horaire |
| Gain/Perte quotidien (area smooth) | Calcul JS différentiel | Plage complète 365j - pas de `extend_to` |
| `sensor.sun_next_rising` | NAT | Lever réel (graphe historique) |
| `sensor.sun_next_setting` | NAT | Coucher réel (graphe historique) |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/vignette_L1C1_meteo_2026-05-16.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/page_L1C1_meteo_2026-05-23.yaml` | ⚠️ obsolete |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/page_L1C1_meteo_2026-06-13.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/card_duree_du_jour_2026-05-23.yaml` | ✅ |
| `command_line/meteo/carte_meteo_france.yaml` | ✅ |
| `utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml` | ✅ |
| `sensors/meteo/M_meteo_sensors_blitzortung.yaml` | ✅ *(ajouté 2026-07-19 - manquait)* |
| `templates/meteo/M_01_meteo_alertes_card.yaml` | ✅ |
| `templates/meteo/M_02_meteo_vent_vence_card.yaml` | ✅ |
| `templates/meteo/M_03_meteo_blitzortung.yaml` | ✅ |
| `templates/meteo/M_05_cycle_solaire.yaml` | ✅ *(ajouté 2026-07-19 - manquait, calcule la durée du jour)* |

> `templates/meteo/M_04_tendances_th_ext_card.yaml` retiré de cette liste le 2026-07-19 -
> son entête déclare lui-même `AVAL : L1C2 Températures`, pas L1C1. Voir section L1C2.

---

## ✅ L1C2 - TEMPÉRATURES (VIGNETTE + PAGE)
*Validée le 2026-05-13*

### Vignette - Chaîne de dépendances

```
MATÉRIEL (SONOFF TH via Z2M)
  └─→ sensor.th_*_temperature / _humidity  (NAT - 7 pièces)
        └─→ VIGNETTE L1C2 (button-card - grille piece/temp/humidite)
              └─→ tap_action: navigate → /dashboard-tablette/temperatures
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.th_balcon_nord_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_balcon_nord_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_salon_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_salon_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_cellier_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_cellier_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_cuisine_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_cuisine_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_bureau_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_bureau_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_salle_de_bain_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_salle_de_bain_humidity` | NAT | SONOFF via Z2M |
| `sensor.th_chambre_temperature` | NAT | SONOFF via Z2M |
| `sensor.th_chambre_humidity` | NAT | SONOFF via Z2M |

### Page - Entités clés supplémentaires

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.vence_temperature` | NAT | Météo France |
| `sensor.temperature_moyenne_interieure` | TPL | `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.temperature_delta_value` | TPL | `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.temperature_delta_affichage` | TPL | `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.delta_ademe_recommande` | TPL | `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.th_balcon_nord_temperature_trend` / `_humidity_trend` | TPL | `templates/meteo/M_04_tendances_th_ext_card.yaml` |
| `sensor.th_balcon_nord_temperature` / `_humidity` | NAT | SONOFF via Z2M |
| `sensor.conso_clim_rad_total` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.conso_clim_rad_total_quotidien` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.conso_clim_rad_total_mensuel` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.clim_rad_total_avg_watts_quotidien` | TPL | `P1_AVG/P1_AVG_TOTAL_AMHQ.yaml` |
| `climate.clim_salon_rm4_mini` | NAT | SmartIR |
| `climate.radiateur_cuisine` | NAT | Meross |
| `climate.clim_bureau_rm4_mini` | NAT | SmartIR |
| `climate.clim_chambre_rm4_mini` | NAT | SmartIR |

> ⚠️ **Corrigé le 2026-07-19** : `temperature_moyenne_interieure`, `temperature_delta_affichage`,
> `delta_ademe_recommande` étaient attribués à tort à `P1_ui_dashboard/P1_ui_dashboard.yaml`
> (ce fichier ne produit que des entités power_status/clim_*_etat - vérifié dans son propre
> corps, AVAL déclaré L1C3/L2C2, pas L1C2). Vrai fichier source : `P1_01_clim_logique_system_autom.yaml`
> (son AVAL déclare lui-même "L1C2 Températures" pour ces 4 sensors). Les entrées fictives
> `sensor.th_*_temperature_trend` / `_humidity_trend` (génériques, toutes pièces) ont été
> retirées - seule la sonde balcon nord a un calcul de tendance réel (`M_04_tendances_th_ext_card.yaml`,
> absent de cette section jusqu'ici - ajouté). `sensor.*_power_status` / `clim_*_etat` retirés
> d'ici - ce sont des entités Clim ON/OFF, déjà documentées dans la section L1C3 ci-dessous,
> pas des données de température.

### Streamline templates utilisés

| Template | Rôle |
|:---------|:-----|
| `temperature_humidite` | Affichage T°+Humidité par pièce |
| `calcule_temp_cible` | Pop-up #tendances - calcul T° cible *(corrigé 2026-06-21 : entités + logique cool)* - fichier source : `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_calcule_temp_cible_2026-06-21.yaml` |
| `carte_des_temperatures` | Pop-ups #salon/#bureau/etc - historique T° |

> ⚠️ **Flag** : `custom:temperature-heatmap-card` utilisé dans le pop-up `#exterieur` - **absent du référentiel HACS officiel**. À vérifier / ajouter si installé.

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/vignette_L1C2_temperatures_2026-05-12.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/page_L1C2_temperatures_2026-05-22.yaml` | ⚠️ obsolète - `climate.clim_chambre_rm4_mini` |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/page_L1C2_temperatures_2026-05-22.yaml.bak` | ❓ origine inconnue - conservé en attendant clarification |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/page_L1C2_temperatures_2026-07-14.yaml` | ✅ `climate.clim_chambre_rm4_mini` + `sensor.temperature_corrige_chambre` |
| `templates/meteo/M_04_tendances_th_ext_card.yaml` | ✅ *(ajouté 2026-07-19 - manquait)* |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | ✅ *(fichier partagé - AVAL principal L1C3, voir aussi cette section)* |

---

## ✅ L1C3 - COMMANDES CLIM (VIGNETTE + PAGE)
*Validée le 2026-05-13 - chambre sur `climate.clim_chambre_rm4_mini` depuis le 2026-07-14*

### Vignette - Chaîne de dépendances

```
MATÉRIEL (NOUS SP via Z2M + SmartIR + Meross)
  └─→ sensor.*_power / climate.*   (NAT)
        └─→ TPL: P1_ui_dashboard.yaml  (*_power_status / *_etat)
              └─→ sensor.temperature_moyenne_interieure  (TPL P1_clim_logique)
              └─→ sensor.delta_ademe_recommande          (TPL P1_clim_logique)
              └─→ sensor.mode_ete_hiver_etat             (TPL P1_clim_logique)
                    └─→ VIGNETTE L1C3 (button-card - grille piece/mode/consigne)
                          └─→ tap_action: navigate → /dashboard-tablette/clim
```

> ⚠️ Corrigé le 2026-07-19 : `temperature_moyenne_interieure` attribué à tort à
> `P1_ui_dashboard.yaml` (ce fichier ne contient que des sensors power_status/*_etat,
> vérifié dans son corps) - vrai fichier source : `P1_01_clim_logique_system_autom.yaml`.
> `climate.soufflant_salle_de_bain` retiré - n'existe pas (le soufflant SDB est piloté
> via `switch.inter_soufflant_salle_de_bain` + `input_select.etat_resistance_soufflant_sdb`,
> pas une entité climate - vérifié, aucune occurrence dans tout `config_system_YAML/`).

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.temperature_moyenne_interieure` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.delta_ademe_recommande` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.mode_ete_hiver_etat` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.clim_salon_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.radiateur_cuisine_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.clim_bureau_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_soufflant_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_seche_serviette_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.clim_chambre_etat` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.salon_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.cuisine_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.bureau_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_soufflant_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.sdb_seche_serviette_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.chambre_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `climate.clim_salon_rm4_mini` | NAT | SmartIR |
| `climate.radiateur_cuisine` | NAT | Meross |
| `climate.clim_bureau_rm4_mini` | NAT | SmartIR |
| `climate.clim_chambre_rm4_mini` | NAT | SmartIR |
| `switch.inter_soufflant_salle_de_bain` | NAT (switch TPL) | `templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_sdb.yaml` |
| `input_select.etat_resistance_soufflant_sdb` | NAT | `input_select.yaml` |

### Entités clés de la page

| Entité | Type | Rôle |
|:-------|:----:|:-----|
| `sensor.conso_clim_rad_total` | TPL | Bar-card puissance totale P1 |
| `sensor.*_nous_power` (×4 clims) | NAT | Bar-cards puissance individuelle |
| `sensor.radiateur_elec_cuisine_power` | NAT | Bar-card puissance cuisine |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | NAT | Bar-card puissance SdB |
| `input_boolean.clim_*_arret_securise_en_cours` | NAT | Bandeaux avertissement arrêt sécurisé |
| `sensor.*_power_lock` | TPL | Verrou script J-2-0 |
| `sensor.*_power_status_affichage` | TPL | Conditional prise coupée |
| `switch.clim_*_nous` | NAT | Badge power + script J-1-x |
| `remote.clim_*` | NAT | Badge état télécommande IR |
| `switch.schedule_clim_*` | NAT | Badges planificateur Sem./W-E |
| `input_select.etat_resistance_soufflant_sdb` | NAT | Affichage puissance soufflant (0/1000/2000W) |
| `switch.inter_soufflant_salle_de_bain` | NAT | Affichage conditionnel soufflant |
| `sensor.th_salle_de_bain_temperature` | NAT | Delta T°/consigne soufflant |

### Scripts appelés depuis la page

| Script | Déclencheur | Statut |
|:-------|:------------|:------:|
| `script.j_1_1_salon_clim_on_off_intelligent` | Badge power Salon | ✅ |
| `script.j_1_2_bureau_clim_on_off_intelligent` | Badge power Bureau | ✅ |
| `script.j_1_3_chambre_clim_on_off_intelligent` | Badge power Chambre | ✅ |
| `script.j_2_0_secu_arret_clim_protege` | Verrou sécurité (déclenché en interne, pas depuis un badge) | ✅ *(fix 2026-07-17 : `clim_entity` chambre - condition spéciale ajoutée pour pointer sur `climate.clim_chambre_rm4_mini` au lieu du pattern générique `climate.clim_{{p}}_rm4_mini`, synchronisé depuis prod/GitHub)* |

### Streamline templates utilisés

| Template | Rôle |
|:---------|:-----|
| `calcule_temp_cible` | Pop-up `#calcul` - delta intérieur/extérieur *(corrigé 2026-06-21)* |
| `nav_bar` | Barre de navigation bas de page |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-05-13.yaml` | ⚠️ obsolète (rm4_mini) |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-05-22.yaml` | ⚠️ obsolète (rm4_mini) |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-07-08.yaml` | ⚠️ obsolète - consigne chambre via `sensor.temperature_corrige_chambre` |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-07-08.yaml` | ⚠️ obsolète - badge `remote.clim_chambre` absent |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-07-18.yaml` | ✅ consigne chambre lue sur `climate.clim_chambre_rm4_mini` |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-07-18.yaml` | ✅ badge `remote.clim_chambre` rétabli |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_calcule_temp_cible_2026-06-21.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_prog_clim_salon_2026-07-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_prog_radiateur_cuisine_2026-07-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_prog_clim_bureau_2026-07-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_prog_soufflant_sdb_2026-07-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_prog_clim_chambre_2026-07-14.yaml` | ✅ |

### Entités Chambre (RM4 Mini)

| Entité | Type | Rôle |
|:-------|:----:|:-----|
| `climate.clim_chambre_rm4_mini` | Climate (Broadlink) | Thermostat chambre - actif - consigne lue directement par la vignette depuis le 2026-07-18 |

### Entités Scheduler consommées - Programmation manuelle (ajout 2026-07-14)

| Entité | Equipment | Type |
|:-------|:----------|:-----|
| `switch.schedule_clim_du_salon_week` | Clim Salon | Scheduler (Semaine) |
| `switch.schedule_clim_du_salon_week_end` | Clim Salon | Scheduler (Week-End) |
| `switch.schedule_radiateur_cuisine_week` | Radiateur Cuisine | Scheduler (Semaine) |
| `switch.schedule_radiateur_cuisine_week_end` | Radiateur Cuisine | Scheduler (Week-End) |
| `switch.schedule_clim_du_bureau_week` | Clim Bureau | Scheduler (Semaine) |
| `switch.schedule_clim_du_bureau_week_end` | Clim Bureau | Scheduler (Week-End) |
| `switch.schedule_soufflant_salle_de_bain_week` | Soufflant SdB | Scheduler (Semaine) |
| `switch.schedule_soufflant_salle_de_bain_week_end` | Soufflant SdB | Scheduler (Week-End) |
| `switch.schedule_clim_de_la_chambre_week` | Clim Chambre | Scheduler (Semaine) |
| `switch.schedule_clim_de_la_chambre_week_end` | Clim Chambre | Scheduler (Week-End) |

### Script lié (P1 clim)

| Fichier | Alias | Statut |
|:--------|:------|:------:|
| `docs/04_docs_scripts/docs_scripts_YAML/p1_master_gestion_clim.yaml` | P1 - MASTER : Gestion centralisée climatisation | ✅ |

> Appelé par A et B. Pilote les 3 clims (salon/bureau/chambre) jour/nuit selon parametre `periode`.

### Automations liées (P1 clim chauffage - A a J)

| Fichier | Alias | Statut | Modifié le |
|:--------|:------|:------:|:-----------|
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml` | (A - 0) CLIM JOUR | ✅ | 2026-06-21 |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml` | (B - 0) CLIM NUIT | ✅ | 2026-06-21 |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/c_notification_temperature_up_ou_down_7h30_21h00.yaml` | (C) Notification temperature Up ou Down (7h30->21h00) | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/d_notification_temperature_up_ou_down_21h00_7h30.yaml` | (D) Notification temperature Up ou Down (21h00->7h30) | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/e_clim_notification_de_fermeture_des_fenetres.yaml` | (E) Notification de fermeture des fenetres | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/f_clim_automatisation_arret_clim_notification.yaml` | (F) Automatisation Arret Clim Notification | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml` | (G) Notification de changement de mode Ete/Fan/Hiver | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/h_clim_debug_force_mode_correct_securite.yaml` | (H) Force Mode Correct & Securite | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/i_synchro_notif_clim_si_prise_coupee.yaml` | (I) Synchro & Notif Clim si Prise Coupee | ✅ | - |
| `docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/j_debug_notifier_les_changements_de_message_clim_mobile.yaml` | (J) Notifier les changements de message clim Mobile | ✅ | - |

### Automations liées (P1 cuisine)

| Fichier | Alias | Statut |
|:--------|:------|:------:|
| `docs/03_docs_automations/docs_automations_YAML/P1_cuisine/a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml` | A - Chauffage Cuisine (4h45-7h LMMJ / 5h45-8h VSD, T° 19.9°) | ✅ |
| `docs/03_docs_automations/docs_automations_YAML/P1_cuisine/b_chauffage_cuisine_vacances.yaml` | B - Chauffage Cuisine Vacances | ✅ |

### Nouveaux sensors P1_MASTER - session 2026-06-21

| Entité | Type | Fichier source | Consommé par |
|:-------|:----:|:--------------|:-------------|
| `sensor.temperature_eco_ete` | TPL | `P1_MASTER_CLIM_TEMPLATES.yaml` | `temperature_eco_ete_corrige`, automations a_0/b_0 |
| `sensor.temperature_eco_ete_corrige` | TPL | `P1_MASTER_CLIM_TEMPLATES.yaml` | automations a_0 (temp_eco_ec) + b_0 (temp_eco_ec) |

### Corrections sensors P1_MASTER - session 2026-06-21

| Entité | Correction |
|:-------|:-----------|
| `sensor.temperature_corrige_mamour` | Été : `min(T°ext - 1, 27)` dynamique |
| `sensor.temperature_corrige_eric` | Été : `min(T°ext + 1, 28)` dynamique |
| `sensor.temperature_corrige_chambre` | Été : `min(T°ext + 1, 28)` - hiver : fallback `float(18)` à corriger |
| `sensor.temperature_eco_hiver_corrige` | Source corrigée : lit `temperature_eco_hiver` (était `temperature_eco_ete`) |
| `sensor.temperature_confort_jour` | À corriger : ajouter `cool` mode → retourner `base` (26°C) |

### Corrections sensors P1_MASTER - session 2026-06-29

| Entité | Correction | Statut |
|:-------|:-----------|:------:|
| `sensor.temperature_eco_ete_corrige` | Courbe validée : ≤28°C→30 / 29-32°C→29 / >32°C→28 (monotone décroissante ✓) | ✅ |
| `sensor.temperature_confort_nuit` | Seuil 29°C ajouté - zone 26-32°C scindée : ≤29→+d1(26°C) / >29→+d2(27°C) - floor nuit 27°C garanti - **remplacé, voir section 2026-07-19/20 ci-dessous** | ✅ |

### Corrections sensors P1_MASTER - sessions 2026-07-19 / 2026-07-20

| Entité | Correction | Statut |
|:-------|:-----------|:------:|
| `sensor.temperature_confort_nuit` | 07-19 : palier été +d2 relevé de >29 à >30 (confort nuit) | ✅ |
| `sensor.temperature_confort_nuit` | 07-20 : palier dynamique selon `sensor.alerte_canicule` (M_01_meteo_alertes_card) : Vert/indispo=29, Jaune=30, Orange=30, Rouge=31 - T°ext ≤ palier → 26°C, au-delà → 27°C - nouvelle dépendance M_01 → P1_01_MASTER → L1C3 | ✅ |
| `sensor.message_clim_personnalise_7h30_21h00` (P1_02) | 07-20 : 8 branches réalignées sur t_*_target du script p1_master_gestion_clim - g1 cool → [ECO COOL] eco_ete_corrige ; g2/g3/g4 cool → corrige_m/e/c ; g2 heat Bureau → eco ; g3 heat Salon → conf_e. Sources : + `temperature_eco_ete_corrige`, - `temperature_cible` / `temperature_confort_jour` | ✅ |
| `sensor.message_clim_personnalise_21h00_7h30` (P1_03) | 07-20 : g1 cool → [ECO COOL] eco_ete_corrige (était [COOL] cible). Sources : + `temperature_eco_ete_corrige`, - `temperature_cible` | ✅ |
| `sensor.temperature_corrige_eric` / `_chambre` (P1_01) | 07-20 (16h07, modif Eric en prod hors session) : plafond été relevé 27→28°C. Réintégré en local + boîtes ASCII 07.BUREAU/09.CHAMBRE/MOTEURS restaurées 37 car. | ✅ |
| `sensor.message_clim_personnalise_7h30_21h00` (P1_02) | 07-20 (16h, correction Eric en prod) : fix Ctrl+H ayant cassé entity_id/variables Jinja + `s_off/b_off/c_off` simplifiés en constantes. Local resynchronisé sur prod + fix commentaire ligne 17 | ✅ |
| `sensor.message_clim_personnalise_21h00_7h30` (P1_03) | 07-20 : préfixe "Mode: " + deux-points pièces (Salon:/Bureau:/Chambre:) aligné sur P1_02 | ✅ |

### Corrections Dashboard - session 2026-06-29

| Entité / Carte | Correction | Statut |
|:---------------|:-----------|:------:|
| `card_mod prise_tete_de_lit_chambre` | `position: relative !important` ajouté - suppression `flex/column/center` (conflit mushroom) - `watts=0` forcé si switch OFF (résidu 2W Zigbee) | ✅ |

---

## ✅ L2C1 - ÉNERGIE GÉNÉRALE (VIGNETTE + PAGE)
*Documentée le 2026-06-18*
*Source P0 depuis 2026-06-17 : Nodon SEM-4-1-00 (pince Z2M) - Ecojoko retiré*

> **Source énergie générale (depuis 2026-06-17) : Nodon SEM-4-1-00** (pince ampèremétrique Z2M)
> - `sensor.general_electric_appart_energy` (kWh) → source des UM P0
> - `sensor.general_electric_appart_power` (W) → puissance temps réel
>
> **Linky (MyElectricalData)** = J-1 uniquement (HP/HC historique) - source secondaire

### Chaîne de dépendances

```
MATÉRIEL (Nodon SEM-4-1-00 via Z2M)
  └─→ sensor.general_electric_appart_energy (kWh natif)
  └─→ sensor.general_electric_appart_power  (W natif)
        └─→ UM: P0_UM_AMHQ.yaml               (genelec_appart_*_um : Q/H/M/A)
        └─→ UM: P0_UM_AMHQ_HPHC.yaml        (HP/HC × 4 cycles)
              └─→ TPL: 01_genelec_appart_AMHQ_cost.yaml  (coûts € : cout_total/hp/hc_quotidien…)
              └─→ TPL: 02_ratio_hp_hc.yaml               (genelec_appart_ratio_hc_quotidien/hebdo/mensuel)
              └─→ TPL: 03_AVG_genelec_appart.yaml        (genelec_appart_avg_watts_quotidien/mensuel)
              └─→ TPL: MyElectricalData.yaml             (Linky J-1 - lecture seule)
MATÉRIEL (PowerCalc P2/P3 + calculé)
  └─→ sensor.diag_poste_*_quotidien → TPL: P0_Diag/P0_diag_conso_jour_en_cours.yaml
  └─→ sensor.diag_poste_*_hebdomadaire → TPL: P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml
  └─→ sensor.diag_poste_*_mensuel → TPL: P0_Diag/P0_diag_conso_mois_en_cours.yaml
  └─→ sensor.total_poste_*_puissance → TPL: P0_total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml
SENSORS P0
  └─→ sensor.genelec_appart_conso_mini_24h / _maxi_24h / _moyenne_1h → sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml
                    └─→ VIGNETTE L2C1 ✅
                    └─→ PAGE L2C1 Principale (3 onglets : Journalier/Hebdo/Mensuel) ✅
                    └─→ PAGE L2C1 Temps Réel ✅
                    └─→ PAGE L2C1 Mensuel (détail par appareil) ✅
```

> ⚠️ Corrigé le 2026-07-19 : le diagramme référençait un fichier `total_par_poste_7.yaml`
> qui n'existe pas - les vrais noms sont `P0_diag_conso_{jour,hebdomadaire,mois}_en_cours.yaml`
> (3 fichiers distincts pour `diag_poste_*`) et `P0_total_pour_les_7_postes.yaml` (pour
> `total_poste_*_puissance`), vérifiés par grep des `unique_id:` réels.

### Entités consommées - Vignette L2C1

| Entité | Fichier source | Role |
|:-------|:---------------|:-----|
| `sensor.genelec_appart_conso_mini_24h` | `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml` | Min W 24h |
| `sensor.general_electric_appart_power` | Nodon SEM-4-1-00 (natif Z2M) | W temps réel |
| `sensor.genelec_appart_conso_maxi_24h` | `sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml` | Max W 24h |
| `sensor.genelec_appart_cout_total_quotidien` | `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | Coût € total J |
| `sensor.genelec_appart_cout_hp_quotidien` | `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | Coût € HP J |
| `sensor.genelec_appart_cout_hc_quotidien` | `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | Coût € HC J |

### Fichiers YAML déployables (Dashboard versionnés)

| Fichier | Taille | Navigation | Statut |
|:--------|:-------|:-----------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/vignette_L2C1_energie_2026-06-18.yaml` | 4,4 Ko | (vignette) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-06-18.yaml` | 19,4 Ko | `/energie` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_temps_reel_2026-06-18.yaml` | 38,7 Ko | `/energie-temps-reel` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_mensuel_2026-06-18.yaml` | 12,5 Ko | `/energie-mensuel` | ✅ |

### Fichiers YAML impactés par changement P0 (Ecojoko → Nodon)

| Fichier | Entité modifiée | Statut |
|:--------|:----------------|:------:|
| `utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ.yaml` | source → `general_electric_appart_energy` | ✅ |
| `utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ_HPHC.yaml` | source → `general_electric_appart_energy` | ✅ |
| `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml` | source → Nodon | ✅ |
| `templates/P0_Energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml` | source → Nodon | ✅ |
| `templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml` | Linky J-1 conservé | ✅ |
| Docs vignettes L2C1, L2C2 | Impact Ecojoko → Nodon vérifié : L2C1 ✅, L2C2 ✅ (zero référence Ecojoko en L2C2 - entités P1 pures) | ✅ |

---

## ✅ L2C2 - ÉNERGIE CLIM / RAD / SOUFFLANT
*Validée le 2026-05-13*

### Chaîne de dépendances

```
MATÉRIEL (NOUS SP via Z2M)
  └─→ sensor.*_power / climate.*   (HA natif)
        └─→ UM: P1_UM_AMHQ.yaml          (6 appareils × 4 cycles AMHQ → *_um)
              └─→ TPL: P1_TOTAL_AMHQ.yaml (conso_clim_rad_total_Q/M)
              └─→ TPL: P1_ui_dashboard.yaml (*_power_status / *_etat)
                    └─→ VIGNETTE L2C2 (button-card 3 colonnes)
                    └─→ PAGE L2C2 (apexcharts + tabbed-card + streamline)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `climate.clim_salon_rm4_mini` | NAT | SmartIR |
| `climate.radiateur_cuisine` | NAT | Meross |
| `climate.clim_bureau_rm4_mini` | NAT | SmartIR |
| `climate.clim_chambre_rm4_mini` | NAT | SmartIR |
| `switch.inter_soufflant_salle_de_bain` | NAT (switch TPL) | `templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_sdb.yaml` |
| `sensor.salon_power_status` | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.cuisine_power_status` | TPL | idem |
| `sensor.bureau_power_status` | TPL | idem |
| `sensor.sdb_soufflant_etat` | TPL | idem |
| `sensor.sdb_seche_serviette_etat` | TPL | idem |
| `sensor.chambre_power_status` | TPL | idem |
| `sensor.clim_salon_quotidien_um` | UM | `P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| `sensor.radiateur_elec_cuisine_quotidien_um` | UM | idem |
| `sensor.clim_bureau_quotidien_um` | UM | idem |
| `sensor.soufflant_sdb_quotidien_um` | UM | idem |
| `sensor.seche_serviette_sdb_quotidien_um` | UM | idem |
| `sensor.clim_chambre_quotidien_um` | UM | idem |
| `sensor.conso_clim_rad_total_quotidien` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |
| `sensor.clim_salon_mensuel_um` | UM | `P1_clim_chauffage/P1_UM_AMHQ.yaml` |
| `sensor.radiateur_elec_cuisine_mensuel_um` | UM | idem |
| `sensor.clim_bureau_mensuel_um` | UM | idem |
| `sensor.soufflant_sdb_mensuel_um` | UM | idem |
| `sensor.seche_serviette_sdb_mensuel_um` | UM | idem |
| `sensor.clim_chambre_mensuel_um` | UM | idem |
| `sensor.conso_clim_rad_total_mensuel` | TPL | `P1_TOTAL/P1_TOTAL_AMHQ.yaml` |

### Entités JS uniquement (non dans `entities:`)

| Entité | Source |
|:-------|:-------|
| `sensor.clim_salon_etat` | `P1_ui_dashboard.yaml` |
| `sensor.radiateur_cuisine_etat` | idem |
| `sensor.clim_bureau_etat` | idem |
| `sensor.sdb_soufflant_power_status` | idem |
| `sensor.sdb_seche_serviette_power_status` | idem |
| `sensor.clim_chambre_etat` | idem |

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.temperature_delta_affichage` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.dut_clim_salon` | SEN | `P1_DUT/P1_DUT_clim_chauffage.yaml` |
| `sensor.dut_radiateur_cuisine` | SEN | idem |
| `sensor.dut_clim_bureau` | SEN | idem |
| `sensor.dut_sdb_total` | TPL | `P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml` |
| `sensor.dut_clim_chambre` | SEN | `P1_DUT/P1_DUT_clim_chauffage.yaml` |
| `sensor.mode_ete_hiver_etat` | TPL | `P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` |
| `sensor.conso_clim_rad_total` (puissance W) | TPL | `P1_ui_dashboard/P1_ui_dashboard.yaml` |
| `sensor.th_*_temperature` (×5 pièces) | NAT | SONOFF thermostats |
| `climate.*` (×5) | NAT | SmartIR / Meross |

### Streamline templates (page)

| Template | Usage |
|:---------|:------|
| `conso_temps_reel_clim_rad` | Onglet INSTANTANÉ - apexcharts conso en temps réel |
| `conso_mensuelle_clim` | Onglet MENSUEL - apexcharts conso mensuelle |
| `apex_dut_piece` | Onglet DUT - apexcharts durée utilisation par pièce |
| `clim_voltage_ring-tile` | ring-tile-card tension (V) par appareil |
| `clim_ampere_ring-tile` | ring-tile-card ampérage (A) par appareil |
| `calcule_temp_cible` | Pop-up #tendances - logique calcul T° cible *(corrigé 2026-06-21)* - fichier : `docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/card_calcule_temp_cible_2026-06-21.yaml` |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml` | ✅ |
| `templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml` | ✅ |
| `sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml` | ✅ |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/vignette_L2C2_energie_clim_2026-05-13.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-05-22.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-06-18.yaml` | ⚠️ obsolète - `climate.clim_chambre_rm4_mini` |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-07-14.yaml` | ✅ `climate.clim_chambre_rm4_mini` (NOUS SP1 conservé) |

---

## ✅ L2C3 - ÉNERGIE ÉCLAIRAGE (LAMPES)
*Validée le 2026-04-29 - Migration TPL kWh complète (_um → _um_kwh_tpl) | Dashboard archivé le 2026-05-13 | 2026-06-14 state_class total_increasing → total (× 116 sensors)*

### Chaîne de dépendances

```
MATÉRIEL (Hue Bridge / Sonoff via Z2M)
  └─→ _energy (firmware direct, kWh cumulatif)
        └─→ UM: P3_UM_AMHQ_1_UNITE.yaml  (19 ampoules × 4 cycles = 76 _um)
              └─→ TPL: P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml  (76 _um_kwh_tpl)
                    └─→ TPL: P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml  (9 zones → 36 _um_kwh_tpl)
                    └─→ TPL: P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml (4 total _kwh_tpl)
                    └─→ TPL: P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml (AVG W/ampoule, src _um_kwh_tpl)
                    └─→ TPL: P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml  (AVG W/zone, src _um_kwh_tpl)
                    └─→ TPL: P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml (AVG W total, src _um_kwh_tpl)
                    └─→ TPL: P3_ui_dashboard/P3_etats_status.yaml   (lumiere_*_etat)
                          └─→ VIGNETTE L2C3 (button-card 3 colonnes)
                          └─→ PAGE energie-lampes (tabbed-card 5 pièces)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.lumiere_appartement_etat` | TPL | `P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml` |
| `sensor.lumiere_salon_etat` | TPL | idem |
| `sensor.lumiere_cuisine_etat` | TPL | idem |
| `sensor.lumiere_bureau_etat` | TPL | idem |
| `sensor.lumiere_salle_de_bain_etat` | TPL | idem |
| `sensor.lumiere_chambre_etat` | TPL | idem |
| `sensor.eclairage_appart_2_quotidien_um_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml` |
| `sensor.eclairage_salon_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml` |
| `sensor.eclairage_appart_2_mensuel_um_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml` |
| `sensor.eclairage_salon_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl` | TPL | idem |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | TPL | `P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml` |

### TPL ENERGIE - Détail des 3 fichiers P3_ENERGIE_TPL

| Fichier TPL | Contenu | Nb sensors | Statut |
|:------------|:--------|:----------:|:------:|
| `P3_TPL_AMHQ_1_UNITE.yaml` | 19 ampoules × 4 cycles | 76 | ✅ |
| `P3_TPL_AMHQ_2_ZONE.yaml` | 9 zones × 4 cycles | 36 | ✅ *(corrigé 2026-07-19 - était 10 zones/40, doublon d'une erreur déjà présente dans le fichier yaml lui-même, corrigée le même jour)* |
| `P3_TPL_AMHQ_3_TOTAL.yaml` | 1 total × 4 cycles | 4 | ✅ |

### Zones couvertes par P3_TPL_AMHQ_2_ZONE

| Zone (unique_id prefix) | Ampoules |
|:------------------------|:--------:|
| `eclairage_entree_1` | 1 |
| `eclairage_salon_5` | 5 |
| `eclairage_cuisine_1` | 1 |
| `eclairage_couloir_1` | 1 |
| `eclairage_bureau_5` | 5 |
| `eclairage_sdb_2` | 2 |
| `eclairage_chambre_4` | 4 |
| `eclairage_appart_3` | 3 (entrée+cuisine+couloir) |
| `eclairage_appart_2` | 2 (entrée+couloir) |

### Entité puissance temps réel (W)

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eclairage_total_group_puissance_tpl` | TPL | `P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` |

> Somme des 19 `{slug}_power` (PowerCalc). Consommé par `total_pour_les_7_postes.yaml` (Pôle 6) → L2C1.

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml` | ✅ |
| `templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml` | ✅ |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml` | ✅ |
| `templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml` | ✅ |

### Entités supplémentaires (page uniquement)

| Entité | Type | Fichier source | Usage |
|:-------|:----:|:--------------|:------|
| `sensor.eclairage_appart_3_*_um_kwh_tpl` (Q/H/M/A) | TPL | `P3_TPL_AMHQ_2_ZONE.yaml` | Section Entrée-Cuisine-Couloir (3 ampoules) |
| `sensor.eclairage_*_hebdomadaire_um_kwh_tpl` | TPL | `P3_TPL_AMHQ_2_ZONE.yaml` | Badges H (hebdo) par zone |
| `sensor.eclairage_*_annuel_um_kwh_tpl` | TPL | `P3_TPL_AMHQ_2_ZONE.yaml` | Badges A (annuel) par zone |
| `sensor.eclairage_*_avg_watts_mensuel` | TPL | `P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml` | Ligne moyenne 30j (salon/bureau/sdb/chambre/appart_3) |
| `sensor.hue_*_quotidien_um_kwh_tpl` (19 ampoules) | TPL | `P3_TPL_AMHQ_1_UNITE.yaml` | Donuts journaliers par pièce |
| `sensor.hue_*_mensuel_um_kwh_tpl` (19 ampoules) | TPL | `P3_TPL_AMHQ_1_UNITE.yaml` | Donuts mensuels par pièce |
| `light.salon`, `light.table`, `light.entree`, `light.cuisine`, `light.couloir`, `light.bureau`, `light.chambre`, `light.lit` | NAT | Hue Bridge | Badges état ON/OFF heading |
| `light.hue_white_lamp_salle_de_bain` | NAT | Hue Bridge | Badge état SDB |
| `switch.relais_lumiere_sdb_sonoff` | NAT | Z2M Sonoff | Badge état miroir SDB |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/vignette_L2C3_energie_eclairage_2026-05-13.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/page_L2C3_energie_eclairage_2026-05-13.yaml` | ✅ |

---

## ✅ L3C1 - COMMANDES ÉCLAIRAGE (LAMPES)
*Validée le 2026-05-04 | Dashboard archivé le 2026-05-13*

### Chaîne de dépendances

```
MATÉRIEL (Hue Bridge / Sonoff)
  └─→ light.* / switch.*  (HA natif - state on/off)
        └─→ TPL: P3_ui_dashboard/P3_etats_status.yaml  (lumiere_*_etat / bureau_etat / chambre_etat)
              └─→ VIGNETTE L3C1 (button-card 3 colonnes : pièce / état / compteur X/N)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.lumiere_appartement_etat` | TPL | `P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml` |
| `sensor.lumiere_salon_etat` | TPL | idem |
| `sensor.lumiere_cuisine_etat` | TPL | idem |
| `sensor.bureau_etat` | TPL | idem |
| `sensor.lumiere_ecran_etat` | TPL | idem |
| `sensor.lumiere_salle_de_bain_etat` | TPL | idem |
| `sensor.chambre_etat` | TPL | idem |
| `light.entree` | NAT | Hue Bridge |
| `light.couloir` | NAT | Hue Bridge |
| `light.salon` | NAT | Hue Bridge |
| `light.table` | NAT | Hue Bridge |
| `light.cuisine` | NAT | Hue Bridge |
| `light.hue_white_lamp_salle_de_bain` | NAT | Hue Bridge |
| `light.chambre` | NAT | Hue Bridge |
| `light.hue_color_candle_chambre_gege` | NAT | Hue Bridge |
| `light.hue_color_candle_chambre_eric` | NAT | Hue Bridge |
| `light.lit` | NAT | Hue Bridge | Groupe tête de lit - cible du tap_action toggle (fix B4) |
| `switch.prise_tete_de_lit_chambre` | NAT | Intégration native |
| `input_select.saison` | NAT | `input_select.yaml` (icône appartement Été/Hiver - ajouté 2026-07-19, manquait) |

### Entités disponibles (etats_status) non encore intégrées

| Entité | Note |
|:-------|:-----|
| `sensor.lumiere_bureau_etat` | Nouveau slug unifié - remplacera `bureau_etat` à terme |
| `sensor.lumiere_chambre_etat` | Idem - remplacera `chambre_etat` à terme |
| `sensor.lumiere_tete_de_lit_etat` | Nouvel état dédié tête de lit |

### Entités page (toggle + badges + pop-ups)

| Entité | Type | Fichier source | Usage |
|:-------|:----:|:--------------|:------|
| `sensor.th_salon_temperature` | NAT | SONOFF via Z2M | Badge T° heading Salon |
| `sensor.th_cuisine_temperature` | NAT | SONOFF via Z2M | Badge T° heading Cuisine |
| `sensor.th_bureau_temperature` | NAT | SONOFF via Z2M | Badge T° heading Bureau |
| `sensor.th_salle_de_bain_temperature` | NAT | SONOFF via Z2M | Badge T° heading SdB |
| `sensor.th_chambre_temperature` | NAT | SONOFF via Z2M | Badge T° heading Chambre |
| `cover.store_salon` | NAT | MQTT/Z2M | Badge volet heading Salon |
| `cover.store_bureau` | NAT | MQTT/Z2M | Badge volet heading Bureau |
| `light.entree` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.salon` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.table` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.cuisine` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.couloir` | NAT | Hue Bridge | Mushroom toggle + heading badge |
| `light.bureau` | NAT | Hue Bridge | Mushroom toggle (Hue White bureau_1+2) + pop-up |
| `light.hue_white_lamp_salle_de_bain` | NAT | Hue Bridge | Mushroom toggle SdB + heading badge |
| `light.chambre` | NAT | Hue Bridge | Mushroom toggle Chambre + heading badge |
| `switch.relais_lumiere_sdb_sonoff` | NAT | Z2M Sonoff | Mushroom toggle SdB (miroir) + heading badge |
| `switch.ecran_p_c_3_play_hue` | NAT | Hue Bridge | Condition affichage section Écran PC |
| `light.moniteur_pc` | NAT | Hue Bridge | Pop-up #ecranpc (groupe Play 1/2/3) |
| `light.zone_gege` | NAT | Hue Bridge | Pop-up #tete_de_lit |
| `light.zone_eric` | NAT | Hue Bridge | Pop-up #tete_de_lit |
| `switch.prise_tete_de_lit_chambre` | NAT | Intégration native | Condition visibilité section Têtes de Lit |

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml` | ✅ |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/vignette_L3C1_eclairage_2026-05-13.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_gauche_2026-05-13.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-13.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-22.yaml` | ✅ |

---

## ✅ L3C2 - COMMANDES ÉCO/PRISES
*Archivée le 2026-05-14*

### Vignette - Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Zigbee2MQTT (Z2M) → MQTT → HA
  │     ├─→ switch.prise_horloge_ikea          (natif Z2M - IKEA TRADFRI)
  │     ├─→ switch.prise_tv_salon_ikea          (natif Z2M - IKEA TRADFRI)
  │     ├─→ switch.prise_tete_de_lit_chambre    (natif Z2M - IKEA TRADFRI)
  │     ├─→ light.hue_smart_eco_salon           (natif Z2M - Hue Smart Plug)
  │     ├─→ light.hue_smart_eco_pc_bureau       (natif Z2M - Hue Smart Plug)
  │     └─→ light.hue_smart_eco_tv_chambre      (natif Z2M - Hue Smart Plug)
  │           └─→ VIGNETTE L3C2 (button-card 2 colonnes : piece / etat)
  │                 tap_action → /dashboard-tablette/prises
```

### Entités utilisées - Vignette

| Entité | Type | Source | Rôle |
|:-------|:-----|:-------|:-----|
| `switch.prise_horloge_ikea` | switch | Z2M natif | État Horloge Entrée |
| `light.hue_smart_eco_salon` | light | Z2M natif | État Eco Salon (chargeur) |
| `switch.prise_tv_salon_ikea` | switch | Z2M natif | État TV Salon |
| `light.hue_smart_eco_pc_bureau` | light | Z2M natif | État PC Bureau |
| `switch.prise_tete_de_lit_chambre` | switch | Z2M natif | État Têtes de Lit |
| `light.hue_smart_eco_tv_chambre` | light | Z2M natif | État TV Chambre |

### Entités utilisées - Page

| Entité contrôlée | Sensor puissance | Sensor tension | Sensor courant | MAX |
|:-----------------|:-----------------|:---------------|:---------------|:----|
| `switch.prise_horloge_ikea` | `sensor.prise_horloge_ikea_power` | `sensor.prise_horloge_ikea_voltage` | `sensor.prise_horloge_ikea_current` | 2500W |
| `light.hue_smart_eco_salon` | `sensor.prise_salon_chargeur_nous_power` | `sensor.prise_salon_chargeur_nous_voltage` | `sensor.prise_salon_chargeur_nous_current` | 2500W |
| `switch.prise_tv_salon_ikea` | `sensor.prise_tv_salon_ikea_power` | `sensor.prise_tv_salon_ikea_voltage` | `sensor.prise_tv_salon_ikea_current` | 250W (mA) |
| `light.hue_smart_eco_pc_bureau` | `sensor.prise_bureau_pc_ikea_power` | `sensor.prise_bureau_pc_ikea_voltage` | `sensor.prise_bureau_pc_ikea_current` | 500W (couleur gris si OFF) |
| `light.hue_smart_eco_tv_chambre` | `sensor.prise_tv_chambre_nous_power` | `sensor.prise_tv_chambre_nous_voltage` | `sensor.prise_tv_chambre_nous_current` | 500W |
| `switch.prise_tete_de_lit_chambre` | `sensor.prise_tete_de_lit_chambre_power` | `sensor.prise_tete_de_lit_chambre_voltage` | `sensor.prise_tete_de_lit_chambre_current` | 50W |

### Fichiers YAML déployables

| Fichier | Rôle | Statut |
|:--------|:-----|:------:|
| `templates/P2_prise/P2_eCO_prises/P2_eco_prises_config.yaml` | Config liste prises Éco Dynamique (indirect - pilote automation eco_prises_dynamique) | ✅ |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/vignette_L3C2_prises_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/page_L3C2_prises_2026-05-14.yaml` | ✅ |

---

## ✅ L3C3 - STORES / FENÊTRES (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette - Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Zigbee2MQTT - SONOFF SNZB-04 (4 contacts de fenêtre)
  │     ├─→ binary_sensor.contact_fenetre_salon_sonoff_contact   (NAT/Z2M)
  │     ├─→ binary_sensor.contact_fenetre_cuisine_sonoff_contact (NAT/Z2M)
  │     ├─→ binary_sensor.contact_fenetre_bureau_sonoff_contact  (NAT/Z2M)
  │     └─→ binary_sensor.contact_fenetre_chambre_sonoff_contact (NAT/Z2M)
  │           └─→ VIGNETTE L3C3 - colonne "Fenêtres" (on=rouge Ouvert, off=vert Fermé)
  ├─→ TPL: templates/Stores/S_01_STORES.yaml
  │     ├─→ sensor.store_salon_status   (TPL - texte état store salon)
  │     └─→ sensor.store_bureau_status  (TPL - texte état store bureau)
  │           └─→ VIGNETTE L3C3 - colonne "Stores" (texte brut)
  └─→ sensor.store_cuisine_status / sensor.store_chambre_status
        └─→ VIGNETTE L3C3 - colonne "Stores" (placeholders N/A - stores non motorisés)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source | Rôle |
|:-------|:----:|:--------------|:-----|
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Salon - Ouvert/Fermé |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Cuisine - Ouvert/Fermé |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Bureau - Ouvert/Fermé |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Fenêtre Chambre - Ouvert/Fermé |
| `sensor.store_salon_status` | TPL | `templates/Stores/S_01_STORES.yaml` | Store Salon - texte état |
| `sensor.store_bureau_status` | TPL | `templates/Stores/S_01_STORES.yaml` | Store Bureau - texte état |

### Page - Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ SONOFF (Z2M - balcon nord)
  │     └─→ sensor.th_balcon_nord_temperature  (NAT)  ← badge condition seuil (+34° salon / +18°–+25° bureau)
  ├─→ Zigbee2MQTT - SONOFF SNZB-04
  │     ├─→ binary_sensor.contact_fenetre_salon_sonoff_contact   (NAT)  ← badge état fenêtre salon
  │     ├─→ sensor.contact_fenetre_salon_sonoff_battery           (NAT)  ← badge batterie fenêtre salon
  │     ├─→ binary_sensor.contact_fenetre_bureau_sonoff_contact  (NAT)  ← badge état fenêtre bureau
  │     └─→ sensor.contact_fenetre_bureau_sonoff_battery          (NAT)  ← badge batterie fenêtre bureau
  ├─→ Zigbee2MQTT - covers (stores motorisés)
  │     ├─→ cover.store_salon   (NAT/Z2M)  ← enhanced-shutter-card + boutons positions (100/85/70/49/20)
  │     └─→ cover.store_bureau  (NAT/Z2M)  ← enhanced-shutter-card + boutons positions (100/90/65/50/30)
  ├─→ sensor.store_salon_signal_strength   (NAT/Z2M)  ← signal_entity enhanced-shutter-card salon
  ├─→ sensor.store_bureau_signal_strength  (NAT/Z2M)  ← signal_entity enhanced-shutter-card bureau
  └─→ Hue Bridge
        ├─→ light.store_salon_dnd   (NAT)  ← voyant DnD mushroom-light-card salon
        └─→ light.store_bureau_dnd  (NAT)  ← voyant DnD mushroom-light-card bureau
```

### Entités consommées par la page

| Entité | Type | Fichier source | Rôle |
|:-------|:----:|:--------------|:-----|
| `sensor.th_balcon_nord_temperature` | NAT | Z2M (SONOFF balcon nord) | Badge condition seuil fermeture auto |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Badge état fenêtre Salon |
| `sensor.contact_fenetre_salon_sonoff_battery` | NAT | Z2M (SONOFF SNZB-04) | Badge batterie fenêtre Salon |
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | NAT | Z2M (SONOFF SNZB-04) | Badge état fenêtre Bureau |
| `sensor.contact_fenetre_bureau_sonoff_battery` | NAT | Z2M (SONOFF SNZB-04) | Badge batterie fenêtre Bureau |
| `cover.store_salon` | NAT | Z2M (store motorisé) | enhanced-shutter-card - commande store Salon |
| `cover.store_bureau` | NAT | Z2M (store motorisé) | enhanced-shutter-card - commande store Bureau |
| `sensor.store_salon_signal_strength` | NAT | Z2M | signal_entity - force signal store Salon |
| `sensor.store_bureau_signal_strength` | NAT | Z2M | signal_entity - force signal store Bureau |
| `light.store_salon_dnd` | NAT | Hue Bridge | Voyant DnD mushroom-light-card - Salon |
| `light.store_bureau_dnd` | NAT | Hue Bridge | Voyant DnD mushroom-light-card - Bureau |

### Fichiers YAML déployables

| Fichier | Rôle | Statut |
|:--------|:-----|:------:|
| `templates/Stores/S_01_STORES.yaml` | Sensors texte état stores (store_salon_status, store_bureau_status) | ✅ |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/vignette_L3C3_stores_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-06-02.yaml` | ✅ |

---

## ✅ L4C1 - PROXMOX PVE (VIGNETTE + PAGE)
*Validée le 2026-06-13 (docs entièrement réécrites - +5e section MyElectricalData)*

> Page complète supervision infrastructure Proxmox VE.
> Vignette : température CPU, CPU %, RAM %, Storage %, PVE Status.
> Page : **5 sections** (PVE, HA, Z2M, MariaDB, MyElectricalData) × métriques détaillées + apexcharts CPU 1h.
> Path → `/dashboard-tablette/systeme-proxmox`.

### Vignette - Entités consommées

| Entité | Type | Source |
|:-------|:----:|:-------|
| `sensor.proxmox_cpu_package` | NAT | Proxmox VE (MQTT Discovery) |
| `sensor.pve_utilisation_du_processeur` | NAT | Proxmox VE |
| `sensor.pve_memory_usage_percentage` | NAT | Proxmox VE |
| `sensor.storage_local_storage_usage_percentage` | NAT | Proxmox VE |
| `binary_sensor.pve_status` | NAT | Proxmox VE |

### Page - Entités consommées (complet)

**PROXMOX VE**
| Entité | Métrique |
|:-------|:---------|
| `sensor.pve_statut` | Status |
| `sensor.pve_utilisation_du_processeur` | CPU % |
| `sensor.pve_memory_usage_percentage` | RAM % |
| `sensor.pve_utilisation_du_disque` | Disk GiB |
| `sensor.pve_uptime` | Uptime |
| `binary_sensor.pve_backup_status` | Backup |
| `sensor.pve_max_cpu` | vCPU |
| `button.pve_tout_demarrer` | Start All |
| `button.pve_tout_stopper` | Stop All |
| `button.pve_redemarrer` | Reboot |
| `button.pve_shut_down` | Shutdown |

**HOME ASSISTANT**
| Entité | Métrique |
|:-------|:---------|
| `sensor.homeassistant_statut` | Status |
| `sensor.homeassistant_utilisation_du_processeur` | CPU % |
| `sensor.homeassistant_memory_usage_percentage` | RAM % |
| `sensor.homeassistant_utilisation_du_disque` | Disk GiB |
| `sensor.homeassistant_uptime` | Uptime |
| `sensor.homeassistant_max_cpu` | vCPU |
| `button.homeassistant_demarrer` | Start |
| `button.homeassistant_stopper` | Stop |
| `button.homeassistant_redemarrer` | Restart LXC |
| `button.homeassistant_restart` | Restart HA |
| `button.homeassistant_reload` | Reload |

**ZIGBEE2MQTT**
| Entité | Métrique |
|:-------|:---------|
| `sensor.z2m_statut` | Status |
| `sensor.z2m_utilisation_du_processeur` | CPU % |
| `sensor.z2m_memory_usage_percentage` | RAM % |
| `sensor.z2m_utilisation_du_disque` | Disk GiB |
| `sensor.z2m_uptime` | Uptime |
| `sensor.z2m_max_cpu` | vCPU |
| `button.z2m_demarrer` | Start |
| `button.z2m_stopper` | Stop |
| `button.z2m_redemarrer` | Restart |

**MARIADB**
| Entité | Métrique |
|:-------|:---------|
| `sensor.mariadb_statut` | Status |
| `sensor.mariadb_utilisation_du_processeur` | CPU % |
| `sensor.mariadb_memory_usage_percentage` | RAM % |
| `sensor.mariadb_utilisation_du_disque` | Disk GiB |
| `sensor.mariadb_uptime` | Uptime |
| `sensor.mariadb_max_cpu` | vCPU |
| `button.mariadb_demarrer` | Start |
| `button.mariadb_stopper` | Stop |
| `button.mariadb_redemarrer` | Restart |

**MYELECTRICALDATA (LXC 202)** ← *ajouté 2026-06-13*
| Entité | Métrique | Note |
|:-------|:---------|:-----|
| `sensor.myelectricaldata_statut` | Status (enum) | running/stopped/suspended |
| `binary_sensor.myelectricaldata_status` | Running (bool) | device_class: running |
| `sensor.myelectricaldata_utilisation_du_processeur` | CPU % | |
| `sensor.myelectricaldata_memory_usage_percentage` | RAM % | |
| `sensor.myelectricaldata_utilisation_de_la_memoire` | RAM GiB | |
| `sensor.myelectricaldata_utilisation_maximale_de_la_memoire` | RAM Max GiB | max allouée = 1.0 GiB |
| `sensor.myelectricaldata_utilisation_du_disque` | Disk GiB | ⚠️ PAS de % - GiB uniquement |
| `sensor.myelectricaldata_utilisation_maximale_du_disque` | Disk Max GiB | max = 3.86 GiB |
| `sensor.myelectricaldata_uptime` | Uptime (h float) | même format que pve_uptime |
| `sensor.myelectricaldata_max_cpu` | vCPU | = 1 |
| `sensor.myelectricaldata_network_input` | Réseau In GiB | total_increasing |
| `sensor.myelectricaldata_network_output` | Réseau Out GiB | total_increasing |
| `button.myelectricaldata_demarrer` | Start | |
| `button.myelectricaldata_stopper` | Stop | |
| `button.myelectricaldata_redemarrer` | Restart | |
| `button.myelectricaldata_create_snapshot` | Snapshot | |

> ⚠️ Pas de `binary_sensor.myelectricaldata_backup_status` (contrairement à PVE).
> Pas de `sensor.myelectricaldata_utilisation_du_disque` en % - seuils page à exprimer en GiB absolu.
> Badge : vert `rgb(15,157,88)` - couleur section : `#00bcd4`.

### Seuils de couleur

| Section | Métrique | Vert | Orange | Rouge |
|:--------|:---------|:-----|:--------|:------|
| **PVE** | CPU % | ≤75% | 75–90% | >90% |
| **PVE** | RAM % | ≤75% | 75–90% | >90% |
| **PVE** | Storage % | ≤60% | 60–80% | >80% |
| **HA** | CPU % | ≤75% | 75–90% | >90% |
| **HA** | RAM % | ≤75% | 75–90% | >90% |
| **HA** | Disk GiB | ≤20 | 20–28 | >28 |
| **Z2M** | CPU % | ≤40% | 40–60% | >60% |
| **Z2M** | RAM % | ≤50% | 50–70% | >70% |
| **Z2M** | Disk GiB | ≤2.5 | 2.5–3.4 | >3.4 |
| **MDB** | CPU % | ≤50% | 50–75% | >75% |
| **MDB** | RAM % | ≤60% | 60–80% | >80% |
| **MDB** | Disk GiB | ≤5 | 5–7 | >7 |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_MD/L4C1_PROXMOX/L4C1_VIGNETTE_PROXMOX.md` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-06-09.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-06-18.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-08-08.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_MD/L4C1_PROXMOX/PAGE_PROXMOX.md` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/page_L4C1_proxmox_2026-06-10.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/page_L4C1_proxmox_2026-06-18.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/page_L4C1_proxmox_2026-08-08.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/card_services_ha_z2m_mariadb_2026-05-19.yaml` | ⚠️ obsolète - contenu intégré dans page_08-08 |

---

## ✅ L4C2 - MINI PC (VIGNETTE + PAGE)
*Validée le 2026-06-18 - vignette refactorisée : proxmox_cpu_package direct (sans template) | ⚠️ uptime bug non encore corrigé en page*

> ⚠️ **BUG UPTIME CONNU** (non corrigé) : Jinja2 dans la page utilise `| int(0)` + `/ 86400` alors que `sensor.pve_uptime` retourne des **heures** (float), pas des secondes. Résultat : affiche ~0j 0h. Fix à appliquer :
> ```yaml
> {% set uptime = states('sensor.pve_uptime') | float(0) %}
> {% set jours = (uptime / 24) | int(0) %}
> {% set heures = (uptime % 24) | int(0) %}
> {% set minutes = ((uptime % 1) * 60) | int(0) %}
> ```

### Vignette - Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ Proxmox VE (intégration officielle HA)
  │     ├─→ sensor.proxmox_cpu_package                    (NAT)  ← entité principale (icône + champ temp)
  │     ├─→ sensor.pve_utilisation_du_processeur          (NAT)  ← CPU %
  │     ├─→ sensor.pve_memory_usage_percentage            (NAT)  ← RAM %
  │     └─→ sensor.storage_local_storage_usage_percentage (NAT)  ← Disk %
  └─→ Zigbee2MQTT (prise IKEA Inspelning)
        └─→ sensor.prise_mini_pc_ikea_power  (NAT)   ← Watts instantanés
              └─→ VIGNETTE L4C2 (button-card 6 zones CSS - icône phu:intel-nuc)
```

### Entités consommées par la vignette

| Entité | Type | Fichier source | Rôle |
|:-------|:----:|:--------------|:-----|
| `sensor.proxmox_cpu_package` | NAT | Proxmox VE (MQTT Discovery) | Entité principale - icône + champ `temp` |
| `sensor.pve_utilisation_du_processeur` | NAT | Proxmox VE | Champ `cpu` - CPU % |
| `sensor.pve_memory_usage_percentage` | NAT | Proxmox VE | Champ `ram` - RAM % |
| `sensor.storage_local_storage_usage_percentage` | NAT | Proxmox VE | Champ `sd` - Disk % |
| `sensor.prise_mini_pc_ikea_power` | NAT | Z2M (IKEA Inspelning) | Champ `conso` - Watts |

### Page - Chaîne de dépendances

```
MATÉRIEL / INTÉGRATION
  ├─→ local_ip (intégration System Monitor) + command_line api.ipify.org (fallback ifconfig.me)
  │     └─→ sensor.local_ip (NAT) / sensor.ip_externe_wan (command_line)  ← Bloc 1
  ├─→ system_monitor (intégration HA)
  │     ├─→ sensor.system_monitor_dernier_demarrage      ← Bloc 1 (Uptime Jinja2)
  │     ├─→ sensor.system_monitor_utilisation_du_processeur  ← Blocs 2, 6, 8
  │     ├─→ sensor.system_monitor_utilisation_de_la_memoire  ← Bloc 3
  │     ├─→ sensor.system_monitor_memoire_utilisee            ← Blocs 3, 15, 16, #memory
  │     ├─→ sensor.system_monitor_memoire_libre               ← Bloc 3
  │     ├─→ sensor.system_monitor_utilisation_du_disque       ← Bloc 4
  │     ├─→ sensor.system_monitor_espace_utilise              ← Pop-up #disk
  │     ├─→ sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18  ← Bloc 5
  │     ├─→ sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18  ← Bloc 5
  │     ├─→ sensor.system_monitor_charge_1m / 5m / 15m        ← Bloc 8
  │     └─→ sensor.cpu_speed  (NAT)                           ← Bloc 7
  ├─→ Proxmox VE (intégration officielle HA - MQTT Discovery)
  │     └─→ sensor.proxmox_cpu_package / sensor.proxmox_carte_mere / core_0/1/2/3  (NAT)
  │           ├─→ sensor.proxmox_cpu_package   ← Blocs 2, 9, 11
  │           ├─→ sensor.proxmox_core_0 / core_1 / core_2 / core_3  ← Bloc 10
  │           └─→ sensor.proxmox_carte_mere    ← Bloc 12
  └─→ Zigbee2MQTT (prise IKEA Inspelning)
        ├─→ sensor.prise_mini_pc_ikea_power   ← Blocs 13, 14, Pop-up #conso
        ├─→ sensor.prise_mini_pc_ikea_current ← Pop-up #conso
        ├─→ sensor.prise_mini_pc_ikea_energy  ← Pop-up #conso
        ├─→ sensor.mini_pc_avg_watts_quotidien  (TPL)  ← Pop-up #conso
        ├─→ sensor.mini_pc_avg_watts_mensuel    (TPL)  ← Pop-up #conso
        ├─→ sensor.prise_mini_pc_ikea_quotidien_um  (UM)  ← Pop-up #conso
        └─→ sensor.prise_mini_pc_ikea_mensuel_um    (UM)  ← Pop-up #conso
```

> ⚠️ Interface réseau : **`enp6s18`** (VirtIO KVM sous Proxmox) - PAS `enp1s0`.

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-04.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-09.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-18.yaml` | ✅ refonte - proxmox_cpu_package direct (sans template) |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-10.yaml` | ✅ icônes `mdi:cpu-64-bit` + `mdi:harddisk` ajoutées aux mini-graph-cards |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-18.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-08-02.yaml` | ✅ fix sensor.ip_externe → sensor.ip_externe_wan |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/card_popup_memory_2026-06-09.yaml` | ✅ |
| `utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml` | ✅ |
| `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml` | ✅ |

---

## ✅ L4C3 - MISES À JOUR HA (VIGNETTE + 2 PAGES)
*Validée le 2026-05-14*

### Vignette - Chaîne de dépendances

```
HA (domaine update.* natif)
  └─→ TPL: templates/utilitaires/Mise_a_jour_home_assistant.yaml
        └─→ sensor.available_updates  (compte les update.* à l'état 'on')
              └─→ VIGNETTE L4C3 (button-card - couleur orange si > 0, texte MàJ)
                    └─→ tap_action: navigate → /dashboard-tablette/maj
```

> ⚠️ Corrigé le 2026-07-19 : `sensor.available_updates` était marqué NAT - c'est en réalité
> un TPL (`templates/utilitaires/Mise_a_jour_home_assistant.yaml`, absent de cette section
> jusqu'ici), qui compte les entités `update.*` à l'état "on". Vérifié dans le corps du fichier.

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.available_updates` | TPL | `templates/utilitaires/Mise_a_jour_home_assistant.yaml` |

### Page gauche (H.A. SERVER) - Chaîne de dépendances

```
HA Core (intégration hassio)
  ├─→ update.home_assistant_core_update          (NAT) → mushroom-update-card + version info
  ├─→ update.home_assistant_operating_system_update (NAT) → mushroom-update-card
  ├─→ update.home_assistant_supervisor_update    (NAT) → mushroom-update-card
  ├─→ sensor.available_updates                   (TPL) → markdown ha-alert (compteur)
  └─→ HACS (intégration)
        ├─→ auto-entities domain:update → mushroom-chips-card (liste HACS updates)
        └─→ update.install (action) → bouton install
```

### Page droite (H.A. UPDATE + ADD-ON) - Chaîne de dépendances

```
HA Core
  ├─→ auto-entities domain:update state:on (excl. Home*, hacs, mqtt)
  │     └─→ button-card cardupload (MàJ HA hors HACS)
  ├─→ HACS (intégration)
  │     └─→ auto-entities integration:hacs
  │           ├─→ button-card cardurl (lien release)
  │           └─→ button-card cardupload (install update)
  ├─→ markdown (ha-alert error) → intégrations nécessitant redémarrage
  ├─→ Z2M (intégration mqtt)
  │     └─→ auto-entities integration:mqtt → entity-row Z2M
  └─→ HA Add-ons (hassio)
        ├─→ update.mosquitto_broker_update    (NAT) → mushroom-update-card
        └─→ update.studio_code_server_update  (NAT) → mushroom-update-card
              + chips cpu/memory (system_monitor)
```

### Fichiers YAML déployables

| Fichier | Statut |
|:--------|:------:|
| `templates/utilitaires/Mise_a_jour_home_assistant.yaml` | ✅ *(ajouté 2026-07-19 - manquait)* |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/vignette_L4C3_maj_ha_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/page_L4C3_maj_ha_gauche_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/page_L4C3_maj_ha_droite_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/page_L4C3_maj_ha_2026-06-15.yaml` | ✅ |

---

## ✅ L5C1 - BATTERIES / PILES (VIGNETTE + PAGE)
*Validée le 2026-05-14 - ⚠️ page partiellement tronquée (3 sections HUE/IKEA/SONOFF à compléter)*

### Vignette - Chaîne de dépendances

```
groups/ (GRP_01/02/03)
  ├─→ group.hue_devices   → 11 sensors sensor.hue_smart_button_*_batterie
  ├─→ group.ikea_devices  → 8 sensors IKEA (contacts, remotes, détecteurs)
  └─→ group.sonoff_devices → 7 sensors sensor.th_*_battery
        └─→ VIGNETTE L5C1 (button-card)
              ├─→ grid 6 colonnes : count | marque | 100-75 | 75-50 | 50-25 | 25-0
              ├─→ Alerte rouge ≤10% : icône ⚠️ + nom marque rouge
              └─→ tap_action: navigate → /dashboard-tablette/battery-bp
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `group.hue_devices` | GRP | `groups/GRP_01_batteries_hue.yaml` |
| `group.ikea_devices` | GRP | `groups/GRP_02_batteries_ikea.yaml` |
| `group.sonoff_devices` | GRP | `groups/GRP_03_batteries_sonoff.yaml` |

### Page - Chaîne de dépendances

```
Philips Hue Bridge / Z2M / SONOFF (ZHA/Z2M)
  ├─→ [HUE] 11× sensor.hue_smart_button_*_batterie
  │     └─→ battery-state-card collapse "Boutons HUE"
  ├─→ [IKEA] 8× sensor.*_ikea_battery (remotes, détecteurs fuite, Vallhorn, poussoir)
  │     └─→ battery-state-card collapse "Capteurs IKEA"
  ├─→ [IKEA] 4× sensor.contact_fenetre_*_ikea_battery
  │     └─→ battery-state-card collapse "Contacts IKEA"
  ├─→ [SONOFF] 4× sensor.contact_fenetre_*_sonoff_battery
  │     └─→ battery-state-card collapse "Contacts SONOFF"
  └─→ [SONOFF] 7× sensor.th_*_battery
        └─→ battery-state-card collapse "Thermostats SONOFF"
```

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/vignette_L5C1_batteries_piles_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/page_L5C1_batteries_piles_2026-05-14.yaml` | ⚠️ tronqué |

---

## ✅ L5C2 - BATTERIES PORTABLES (VIGNETTE + 2 PAGES)
*Validée le 2026-05-12 - ⚠️ CONFIRMÉ 2026-08-08 : sensor.ne2213_mamour_battery_health + sensor.ne2213_mamour_battery_temperature = entités inconnues (fantômes) dans la page droite. A corriger ou supprimer de la config card.*

### Vignette - Chaîne de dépendances

```
HA Companion App (iOS/Android)
  ├─→ sensor.eric_battery_level / sensor.eric_battery_state
  ├─→ sensor.mamour_battery_level / sensor.mamour_battery_state
  ├─→ sensor.ne2213_eric_battery_level / sensor.ne2213_eric_battery_state
  ├─→ sensor.ne2213_mamour_battery_level / sensor.ne2213_mamour_battery_state
  ├─→ sensor.gm1901_battery_level / sensor.gm1901_battery_state
  ├─→ sensor.sm_a530f_battery_level / sensor.sm_a530f_battery_state
  └─→ sensor.tablette_battery_level / sensor.tablette_battery_state
        └─→ VIGNETTE L5C2 (button-card)
              ├─→ grid 3 colonnes : nom | batterie (couleur) | réserve (icône charge)
              └─→ tap_action: navigate → /dashboard-tablette/phone
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eric_battery_level` | NAT | HA Companion (Poco X7 Pro Eric) |
| `sensor.mamour_battery_level` | NAT | HA Companion (Poco X7 Pro Mamour) |
| `sensor.ne2213_eric_battery_level` | NAT | HA Companion (OnePlus NE2213 Eric) |
| `sensor.ne2213_mamour_battery_level` | NAT | HA Companion (OnePlus NE2213 Mamour) |
| `sensor.gm1901_battery_level` | NAT | HA Companion (OnePlus GM1901) |
| `sensor.sm_a530f_battery_level` | NAT | HA Companion (Samsung SM-A530F) |
| `sensor.tablette_battery_level` | NAT | HA Companion (Tablette) |
| `sensor.*_battery_state` | NAT | HA Companion (état charge : charging/discharging/full) |

### Page gauche (Eric + SM-A530F + Tablette) - Chaîne de dépendances

```
HA Companion App
  ├─→ Poco X7 Pro Eric : conditional (state_not unavailable/unknown)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  ├─→ OnePlus NE2213 Eric : conditional (state_not unavailable/unknown)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  ├─→ Samsung SM-A530F : conditional (state_not unavailable/unknown)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  └─→ Tablette : conditional (state_not unavailable/unknown)
        ├─→ custom:streamline-card template:portable
        └─→ entities: level, state, charger_type, health, temperature, network, wifi
```

### Page droite (Mamour + GM1901) - Chaîne de dépendances

```
HA Companion App
  ├─→ Poco X7 Pro Mamour : vertical-stack (sans conditional)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  ├─→ OnePlus NE2213 Mamour : vertical-stack (sans conditional)
  │     ├─→ custom:streamline-card template:portable
  │     └─→ entities: level, state, charger_type, health, temperature, network, wifi
  │           ⚠️ health + temperature = entités inconnues dans HA (confirmé 2026-08-08)
  └─→ OnePlus GM1901 : vertical-stack (sans conditional)
        ├─→ custom:streamline-card template:portable
        └─→ entities: level, state, charger_type, health, temperature, network, wifi
```

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/vignette_L5C2_batteries_portables_2026-05-12.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_gauche_2026-05-12.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_droite_2026-05-12.yaml` | ✅ |

---

## ✅ L5C3 - MARIADB / SYSTÈME (VIGNETTE + PAGE)
*Validée le 2026-05-10*

### Vignette - Chaîne de dépendances

```
MariaDB (intégration sql.yaml)
  └─→ sensor.taille_db_home_assistant  (SQL - taille en MiB)
        └─→ VIGNETTE L5C3 (custom:flex-horseshoe-card dans button-card)
              ├─→ horseshoe colorstop : 0→vert, 1800→gold, 3500→orange, 4000→red
              └─→ tap_action: navigate → /dashboard-tablette/reserve
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.taille_db_home_assistant` | NAT | `sql.yaml` (requête MariaDB) |

### Page - Chaîne de dépendances

```
Audit MD5 (script + template/command_line)
  ├─→ script.audit_md5                  (scripts.yaml) → button-card déclencheur
  ├─→ sensor.audit_md5_journal          (attr: text) → markdown résultat + chemin log
  ├─→ script.audit_md5_docs             (scripts.yaml) → button-card déclencheur audit docs (AJOUT 2026-08-08)
  └─→ sensor.audit_md5_docs_journal     (attr: text) → markdown résultat audit docs (AJOUT 2026-08-08)
GitHub (shell_command + command_line)
  ├─→ sensor.backup_github_status       (NAT) → chip OK/KO + apexcharts 7j
  ├─→ sensor.backup_github_journal      (NAT) → markdown journal 10 derniers
  ├─→ sensor.git_last_weekly_tag        (NAT) → chip tag hebdo (vert si semaine courante)
  ├─→ sensor.github_default_branch      (NAT) → chip branche (vert si main)
  ├─→ shell_command.git_backup_push_weekly   → hold_action chip tag
  └─→ shell_command.git_backup_push_manual  → tap_action chip Push
MariaDB
  ├─→ sensor.taille_db_home_assistant   (NAT) → apexcharts 7j évolution
  └─→ automation.db_purge_mariadb_repack     → button-card déclencheur manuel
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `script.audit_md5` | NAT | `scripts.yaml` |
| `sensor.audit_md5_journal` | NAT | `command_line/audit/audit_logs.yaml` |
| `script.audit_md5_docs` | NAT | `scripts.yaml` (ajout 2026-08-08) |
| `sensor.audit_md5_docs_journal` | NAT | `command_line/audit/audit_logs.yaml` (ajout 2026-08-08) |
| `sensor.backup_github_status` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.backup_github_journal` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.git_last_weekly_tag` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.github_default_branch` | NAT | `command_line/github_maintenance/github_maintenance.yaml` |
| `sensor.taille_db_home_assistant` | NAT | `sql.yaml` |
| `automation.db_purge_mariadb_repack` | NAT | `automations/systeme/` |
| `shell_command.git_backup_push_weekly` | NAT | `shell_command/Ghithub/backup_github.yaml` |
| `shell_command.git_backup_push_manual` | NAT | `shell_command/Ghithub/backup_github.yaml` |

### Page - Chaîne de dépendances (NOUVEAU 2026-05-18)

```
Proxmox VE (intégration superviseur)
  ├─→ Home Assistant Container (Proxmox)
  │     ├─→ sensor.homeassistant_utilisation_du_processeur  (NAT)
  │     ├─→ sensor.homeassistant_uptime  (NAT)
  │     ├─→ sensor.homeassistant_memory_usage_percentage  (NAT)
  │     └─→ sensor.homeassistant_utilisation_de_la_memoire  (NAT)
  │           └─→ PAGE RÉSERVE SYSTÈME (page_L5C3_systeme_reserve)
  ├─→ Z2M (Zigbee2MQTT) Container (Proxmox)
  │     ├─→ sensor.z2m_utilisation_du_processeur  (NAT)
  │     ├─→ sensor.z2m_uptime  (NAT)
  │     ├─→ sensor.z2m_memory_usage_percentage  (NAT)
  │     └─→ sensor.z2m_utilisation_de_la_memoire  (NAT)
  └─→ MariaDB Container (Proxmox)
        ├─→ sensor.mariadb_utilisation_du_processeur  (NAT)
        ├─→ sensor.mariadb_uptime  (NAT)
        ├─→ sensor.mariadb_memory_usage_percentage  (NAT)
        ├─→ sensor.mariadb_utilisation_de_la_memoire  (NAT)
        └─→ sensor.taille_db_home_assistant  (NAT - SQL)
```

### Entités consommées par la page RÉSERVE SYSTÈME

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.homeassistant_utilisation_du_processeur` | NAT | `proxmox_ve` (intégration) |
| `sensor.homeassistant_uptime` | NAT | `proxmox_ve` (intégration) |
| `sensor.homeassistant_memory_usage_percentage` | NAT | `proxmox_ve` (intégration) |
| `sensor.homeassistant_utilisation_de_la_memoire` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_utilisation_du_processeur` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_uptime` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_memory_usage_percentage` | NAT | `proxmox_ve` (intégration) |
| `sensor.z2m_utilisation_de_la_memoire` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_utilisation_du_processeur` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_uptime` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_memory_usage_percentage` | NAT | `proxmox_ve` (intégration) |
| `sensor.mariadb_utilisation_de_la_memoire` | NAT | `proxmox_ve` (intégration) |
| `sensor.taille_db_home_assistant` | NAT | `sql.yaml` (requête MariaDB) |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/vignette_L5C3_mariadb_2026-05-10.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/card_mariadb_2026-05-18.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/page_L5C3_systeme_reserve_2026-05-18.yaml` (HA + Z2M + MariaDB) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/card_audit_buttons_2026-06-14.yaml` (boutons déclencheurs audit) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/card_audit_journal_2026-06-14.yaml` (journal résultat audit) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/card_audit_md5_2026-06-15.yaml` (carte audit MD5) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/card_audit_recap_2026-06-15.yaml` (recap audit MD5) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/page_L5C3_mariadb_2026-06-02.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/page_L5C3_mariadb_2026-06-15.yaml` (Audit MD5 + GitHub + MariaDB) | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/page_L5C3_mariadb_2026-08-08.yaml` (+ Audit MD5 Docs ajout 2026-08-08) | ✅ |

---

## ✅ L6C1 - QUALITÉ DE L'AIR (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette - Chaîne de dépendances

```
IKEA VINDSTYRKA (Zigbee via Z2M)
  ├─→ sensor.qualite_air_salon_ikea_pm25        (NAT) → vignette PM2.5 Salon (couleur JS)
  ├─→ sensor.qualite_air_bureau_ikea_pm25       (NAT) → vignette PM2.5 Bureau (couleur JS)
  ├─→ sensor.qualite_air_chambre_ikea_pm25      (NAT) → vignette PM2.5 Chambre (couleur JS)
  ├─→ sensor.qualite_air_salon_ikea_voc_index   (NAT) → vignette tCOV Salon (couleur JS)
  ├─→ sensor.qualite_air_bureau_ikea_voc_index  (NAT) → vignette tCOV Bureau (couleur JS)
  └─→ sensor.qualite_air_chambre_ikea_voc_index (NAT) → vignette tCOV Chambre (couleur JS)
        └─→ VIGNETTE L6C1 (custom:button-card)
              ├─→ Grid 3 colonnes × 9 zones (titre + 3×PM2.5 + 3×tCOV)
              ├─→ Seuils PM2.5 : >35→rouge, >11→orange, sinon blanc
              ├─→ Seuils tCOV/VOC index : >1000→rouge, >250→orange, sinon blanc
              ├─→ unavailable/unknown → gris #808080
              └─→ tap_action: navigate → /dashboard-tablette/air-quality
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_air_salon_ikea_pm25` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_pm25` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_pm25` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |
| `sensor.qualite_air_salon_ikea_voc_index` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_voc_index` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_voc_index` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |

### Page - Chaîne de dépendances

```
IKEA VINDSTYRKA (Zigbee via Z2M)
  ├─→ sensor.qualite_air_salon_ikea_pm25        (NAT) → streamline-card pm25_ring-tile + bouton + pop-up pm25
  ├─→ sensor.qualite_air_bureau_ikea_pm25       (NAT) → streamline-card pm25_ring-tile + bouton + pop-up pm25
  ├─→ sensor.qualite_air_chambre_ikea_pm25      (NAT) → streamline-card pm25_ring-tile + bouton + pop-up pm25
  ├─→ sensor.qualite_air_salon_ikea_voc_index   (NAT) → streamline-card cov_ring-tile + pop-up cov
  ├─→ sensor.qualite_air_bureau_ikea_voc_index  (NAT) → streamline-card cov_ring-tile + pop-up cov
  └─→ sensor.qualite_air_chambre_ikea_voc_index (NAT) → streamline-card cov_ring-tile + pop-up cov

sensors/Air_quality/A_01_AIR_QUALITY.yaml (SEN - stats mean 24h)
  ├─→ sensor.pm2_5_salon_moy_24h   (SEN) → marker2 ring-tile Salon PM2.5
  ├─→ sensor.pm2_5_bureau_moy_24h  (SEN) → marker2 ring-tile Bureau PM2.5
  ├─→ sensor.pm2_5_chambre_moy_24h (SEN) → marker2 ring-tile Chambre PM2.5
  ├─→ sensor.tcov_salon_moy_24h    (SEN) → marker2 ring-tile Salon tCOV
  ├─→ sensor.tcov_bureau_moy_24h   (SEN) → marker2 ring-tile Bureau tCOV
  └─→ sensor.tcov_chambre_moy_24h  (SEN) → marker2 ring-tile Chambre tCOV

templates/Air_quality/A_01_AIR_QUALITY.yaml (TPL - conversion ppb)
  ├─→ sensor.tcov_salon_ppb    (TPL) → entity bouton tCOV Salon + streamline-card cov
  ├─→ sensor.tcov_bureau_ppb   (TPL) → entity bouton tCOV Bureau + streamline-card cov
  └─→ sensor.tcov_chambre_ppb  (TPL) → entity bouton tCOV Chambre + streamline-card cov

        └─→ PAGE L6C1 - 3 sections (SALON / BUREAU / CHAMBRE)
              ├─→ custom:streamline-card templates : pm25_ring-tile, cov_ring-tile, pm25, cov
              ├─→ custom:bubble-card pop-up via hash (#spm25, #scov, #bpm25, #bcov, #cpm25, #ccov)
              └─→ bubble-card separator × 3 (SALON, BUREAU, CHAMBRE)
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_air_salon_ikea_pm25` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_pm25` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_pm25` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |
| `sensor.qualite_air_salon_ikea_voc_index` | NAT | IKEA VINDSTYRKA Salon (Z2M) |
| `sensor.qualite_air_bureau_ikea_voc_index` | NAT | IKEA VINDSTYRKA Bureau (Z2M) |
| `sensor.qualite_air_chambre_ikea_voc_index` | NAT | IKEA VINDSTYRKA Chambre (Z2M) |
| `sensor.pm2_5_salon_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.pm2_5_bureau_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.pm2_5_chambre_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_salon_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_bureau_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_chambre_moy_24h` | SEN | `sensors/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_salon_ppb` | TPL | `templates/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_bureau_ppb` | TPL | `templates/Air_quality/A_01_AIR_QUALITY.yaml` |
| `sensor.tcov_chambre_ppb` | TPL | `templates/Air_quality/A_01_AIR_QUALITY.yaml` |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/vignette_L6C1_air_qualite_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/page_L6C1_air_qualite_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/page_L6C1_air_qualite_2026-05-23.yaml` | ✅ |

---

## ✅ L6C2 - POLLUTION / POLLEN (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette - Chaîne de dépendances

```
Atmo France (intégration HACS)
  ├─→ sensor.qualite_globale_vence        (NAT) → score IQA 0-7 → couleur JS Air
  └─→ sensor.qualite_globale_pollen_vence (NAT) → score pollen 0-7 → couleur JS Pollen
        └─→ VIGNETTE L6C2 (custom:button-card - name JS)
              ├─→ Palette couleur 0-7 : grey→green→lightgreen→gold→orange→red→darkred→purple
              ├─→ Affichage : "Air X / Pollen Y" avec couleurs dynamiques
              └─→ tap_action: navigate → /dashboard-tablette/pollen-pollution
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_globale_vence` | NAT | Intégration Atmo France |
| `sensor.qualite_globale_pollen_vence` | NAT | Intégration Atmo France |

### Page - Chaîne de dépendances

```
Atmo France (intégration HACS) - Section POLLENS
  ├─→ sensor.qualite_globale_pollen_vence    (NAT) → entity-progress-card (barre globale)
  │     └─→ state_attr('Libellé') + state_attr('Couleur') → label + bar_color dynamiques
  ├─→ sensor.concentration_gramine_vence     (NAT) → ring-tile entity
  ├─→ sensor.niveau_gramine_vence            (NAT) → ring-tile ring_entity (index 0-7)
  ├─→ sensor.concentration_ambroisie_vence   (NAT) → ring-tile entity
  ├─→ sensor.niveau_ambroisie_vence          (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_armoise_vence     (NAT) → ring-tile entity
  ├─→ sensor.niveau_armoise_vence            (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_aulne_vence       (NAT) → ring-tile entity
  ├─→ sensor.niveau_aulne_vence              (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_bouleau_vence     (NAT) → ring-tile entity
  ├─→ sensor.niveau_bouleau_vence            (NAT) → ring-tile ring_entity
  ├─→ sensor.concentration_olivier_vence     (NAT) → ring-tile entity
  └─→ sensor.niveau_olivier_vence            (NAT) → ring-tile ring_entity

Atmo France (intégration HACS) - Section QUALITE DE L'AIR
  ├─→ sensor.qualite_globale_vence           (NAT) → entity-progress-card (barre globale)
  │     └─→ state_attr('Libellé') + state_attr('Couleur') → label + bar_color dynamiques
  ├─→ sensor.ozone_vence                     (NAT) → ring-tile O₃ (entity + ring_entity identiques)
  ├─→ sensor.dioxyde_d_azote_vence           (NAT) → ring-tile NO₂
  ├─→ sensor.dioxyde_de_soufre_vence         (NAT) → ring-tile SO₂
  ├─→ sensor.pm10_vence                      (NAT) → ring-tile PM10
  └─→ sensor.pm25_vence                      (NAT) → ring-tile PM25

        └─→ PAGE L6C2 - 2 sections (POLLENS / QUALITE DE L'AIR)
              ├─→ custom:entity-progress-card × 2 (barres globales)
              ├─→ custom:ring-tile × 6 (pollens, grid 3 colonnes, scale 0-7)
              ├─→ custom:ring-tile × 5 (polluants, grid 5 colonnes, scale 0-7)
              ├─→ custom:text-divider-row × 2 (séparateurs sections)
              └─→ custom:stack-in-card + custom:vertical-stack-in-card
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.qualite_globale_pollen_vence` | NAT | Intégration Atmo France |
| `sensor.qualite_globale_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_gramine_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_gramine_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_ambroisie_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_ambroisie_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_armoise_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_armoise_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_aulne_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_aulne_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_bouleau_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_bouleau_vence` | NAT | Intégration Atmo France |
| `sensor.concentration_olivier_vence` | NAT | Intégration Atmo France |
| `sensor.niveau_olivier_vence` | NAT | Intégration Atmo France |
| `sensor.ozone_vence` | NAT | Intégration Atmo France |
| `sensor.dioxyde_d_azote_vence` | NAT | Intégration Atmo France |
| `sensor.dioxyde_de_soufre_vence` | NAT | Intégration Atmo France |
| `sensor.pm10_vence` | NAT | Intégration Atmo France |
| `sensor.pm25_vence` | NAT | Intégration Atmo France |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/vignette_L6C2_pollution_pollen_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/page_L6C2_pollution_pollen_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/page_L6C2_pollution_pollen_2026-06-13.yaml` | ✅ |

---

## ✅ L6C3 - VIGILANCE EAU / VIGIEAU (VIGNETTE + PAGE)
*Validée le 2026-05-14*

### Vignette - Chaîne de dépendances

```
VigiEau (intégration HACS)
  └─→ sensor.alert_level_in_vence         (NAT) → icon dynamique (attr.icon) + couleur (attr.Couleur)
        └─→ VIGNETTE L6C3 (custom:button-card - icon + name JS)
              ├─→ Icon : sensor.attributes.icon (fourni par l'intégration) ou mdi:water-outline
              ├─→ Couleur icône : sensor.attributes.Couleur ou white
              ├─→ Niveaux : null / vigilance (pas de restriction) / vigilance / alerte / alerte_renforcee / crise
              └─→ tap_action: navigate → /dashboard-tablette/vigieau
```

### Entités consommées par la vignette

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.alert_level_in_vence` | NAT | Intégration VigiEau (HACS) |

### Page - Chaîne de dépendances

```
VigiEau (intégration HACS) - Section SÉCHERESSE
  ├─→ sensor.alert_level_in_vence          (NAT) → button-card état global (6 niveaux colorés)
  │     └─→ states : null/vigilance/alerte/alerte_renforcee/crise → icône + couleur dédiés
  ├─→ sensor.alert_level_in_vence_numeric  (NAT) → bar-card jauge 0-4 (severity colorée)
  │     └─→ attributes.icon + attributes.Couleur → icône et couleur dynamiques
  └─→ sensor.*_restrictions_vence          (NAT, auto-entities glob) → grille 4 colonnes button-cards
        ├─→ Couleur border + icône selon état : Aucune restriction / Sensibilisation /
        │   Interdiction sauf exception / Interdiction (+ fallback longueur > 30 car.)
        ├─→ tap_action: browser_mod.popup → détail complet de la restriction
        └─→ exclude: state = "Aucune restriction" (masque les usages sans restriction)
```

### Entités consommées par la page

| Entité | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.alert_level_in_vence` | NAT | Intégration VigiEau (HACS) |
| `sensor.alert_level_in_vence_numeric` | NAT | Intégration VigiEau (HACS) |
| `sensor.*_restrictions_vence` (glob) | NAT | Intégration VigiEau (HACS) - entités dynamiques par usage |

### Fichiers YAML Dashboard

| Fichier | Statut |
|:--------|:------:|
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/vignette_L6C3_vigieau_2026-05-14.yaml` | ✅ |
| `docs/02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/page_L6C3_vigieau_2026-05-14.yaml` | ✅ |

---

## AUTOMATIONS - INDEX PAR DOMAINE
*Ajouté le 2026-08-08*

> Mapping automations -> vignettes dashboard impactées.
> "- notif" = automation purement operationnelle (notification/log/maintenance, sans vignette).
> Fichiers sources : `docs/03_docs_automations/docs_automations_YAML/`

### MATRICE DES AUTOMATIONS - STATUT DÉPENDANCES

| Groupe | Automation | Vignette | Statut |
|:-------|:-----------|:--------:|:------:|
| P1 CLIM / CHAUFFAGE | (A) CLIM JOUR (07H30-21H00) | L1C3 | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (B) CLIM NUIT (21H00-07H30) | L1C3 | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (C) NOTIF T° UP/DOWN JOUR | - notif | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (D) NOTIF T° UP/DOWN NUIT | - notif | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (E) NOTIF FERMETURE FENÊTRES | - notif | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (F) ARRÊT CLIM NOTIFICATION | - notif | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (G) NOTIF CHANGEMENT MODE ÉTÉ/FAN/HIVER | - notif | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (H) DEBUG FORCE MODE CORRECT & SÉCURITÉ | L1C3 | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (I) SYNCHRO & NOTIF CLIM SI PRISE COUPÉE | - notif | ✅ enrichi 2026-08-08 |
| P1 CLIM / CHAUFFAGE | (J) DEBUG NOTIFIER CHANGEMENTS MESSAGE CLIM | - notif | ✅ enrichi 2026-08-08 |
| P1 CUISINE | (A) CHAUFFAGE CUISINE HORAIRES SEMAINE | L1C3 | ✅ enrichi 2026-08-08 |
| P1 CUISINE | (B) CHAUFFAGE CUISINE VACANCES | L1C3 | ✅ enrichi 2026-08-08 |
| P1 SALLE DE BAIN | (A) GESTION INTELLIGENTE SOUFFLANT SDB | L1C3 | ✅ enrichi 2026-08-08 |
| P1 SALLE DE BAIN | (D) WATCHDOG SÉCURITÉ RADIATEUR SDB | L1C3 | ✅ enrichi 2026-08-08 |
| P1 SALLE DE BAIN | (E) MINUTERIE SECHE-SERVIETTES (2H) | L1C3 | ✅ enrichi 2026-08-08 |
| P2 PRISES | ECO PRISES DYNAMIQUE BY PRÉSENCE/GROUPE | L3C2 | ✅ enrichi 2026-08-08 |
| P2 PRISES | GESTION PC BUREAU : SCENE DE FIN + NOTIF | - notif | ✅ enrichi 2026-08-08 |
| P2 PRISES | GESTION TV CHAMBRE : SCENE DE FIN + NOTIF | - notif | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | ACTIVATION ÉCRAN SYNCHRO | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | BOUTON RODRET TOGGLE BLANCHES | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | FORCER PLAY ON SI PC TOURNE | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | WATCHDOG SYNCHRO LAMPES BLANCHES | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | ALLUMAGE LUMIÈRE ENTRÉE | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | BOUTON IKEA INTER SALON (4) | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | BOUTON IKEA SOMRIG | L3C1 | ✅ enrichi 2026-08-08 |
| P3 ECLAIRAGE | SYNC MIROIR LAMPE ET RELAIS SDB | L3C1 | ✅ enrichi 2026-08-08 |
| P4 PRESENCE | [P4] ERIC LOG ZONES | - proto abandon | ✅ enrichi 2026-08-08 |
| ENERGIE (P0) | BASCULEMENT TARIF HC/HP GENELEC APPART | L2C1 | ✅ enrichi 2026-08-08 |
| ENERGIE (P0) | LOG ECART LINKY VS NODON | L2C1 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [00] ALERTE SI KO 15 MIN | L5C3 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [01] GIT HOURLY H+10 | L5C3 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [02] GIT DAILY (03:00) | L5C3 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [03] GIT WEEKLY (DIM 01:30) | L5C3 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [04] GIT PUSH MANUEL | L5C3 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [05] GIT PUSH WEEKLY MANUEL | L5C3 | ✅ enrichi 2026-08-08 |
| GITHUB BACKUP | [06] GIT AU DÉMARRAGE HA | L5C3 | ✅ enrichi 2026-08-08 |
| METEO | ALERTE MÉTÉO FRANCE ACTUALISATION CARTES | L1C1 | ✅ enrichi 2026-08-08 |
| METEO | METTRE À JOUR DERNIER IMPACT FOUDRE | L1C1 | ✅ enrichi 2026-08-08 |
| METEO | NOTIFICATION DE LA FOUDRE | - notif | ✅ enrichi 2026-08-08 |
| METEO | UPDATE PREVIOUS HUMIDITY | L1C2 | ✅ enrichi 2026-08-08 |
| METEO | UPDATE PREVIOUS TEMPERATURE | L1C2 | ✅ enrichi 2026-08-08 |
| STORES | GESTION OPTIMISÉE DU STORE BUREAU | L3C3 | ✅ enrichi 2026-08-08 |
| STORES | GESTION SIMPLE DU STORE SALON (MATIN/SOIR) | L3C3 | ✅ enrichi 2026-08-08 |
| SYSTEME | DB PURGE MARIADB + REPACK | L5C3 | ✅ enrichi 2026-08-08 |
| SYSTEME | DIAG ENREGISTREMENT JOURNALIER (7 POSTES + DUT) | - log | ✅ enrichi 2026-08-08 |
| SYSTEME | ÉCONOMIE ÉNERGIE VS CODE | HOME PAGE | ✅ enrichi 2026-08-08 |
| SYSTEME | WATCHDOG PILES (HUE/IKEA/SONOFF) | L5C1 | ✅ enrichi 2026-08-08 |
| SYSTEME | VEILLE GITHUB NOUVELLE RELEASE DÉTECTÉE | L4C3 | ✅ enrichi 2026-08-08 |
| SYSTEME | Z2M LAST_SEEN | L5C3 | ✅ enrichi 2026-08-08 |

---

## 🗂️ P1 CLIM / CHAUFFAGE - Salon / Bureau / Chambre - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ (A) AUTOMATISATION CLIM JOUR (07H30-21H00)
*Fichier : `P1_clim_chauffage/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml`*

#### A - Rôle

Pilote les clims en période diurne (07h30-21h00) en déléguant au script `p1_master_gestion_clim`. Réagit aux démarrages HA, changements réseau, changements état prises clim, ouverture/fermeture fenêtres et mises à jour températures/mode.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | HA start / 07:30 / changement réseau (mamour + eric) / changement état switch clim / ouverture fenêtre / fermeture fenêtre / changement sensor (groupe/T°/mode) |
| Condition | `time after 07:30 before 21:00` |
| Entités lues | `sensor.mamour_network_type`, `sensor.eric_network_type`, `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous`, `binary_sensor.contact_fenetre_*_sonoff_contact` (x4), `sensor.groupe`, `sensor.th_balcon_nord_temperature`, `sensor.temperature_cible`, `sensor.mode_ete_hiver`, `sensor.temperature_confort_jour` |
| Action | `script.p1_master_gestion_clim` (periode: "jour") - délégation complète |

#### C - Chaîne de dépendances

```
HA (start) / Horaire 07:30
  ├─→ sensor.mamour_network_type / sensor.eric_network_type   (NAT - réseau)
  ├─→ switch.clim_salon_nous / clim_bureau_nous / clim_chambre_nous  (NAT - prises)
  ├─→ binary_sensor.contact_fenetre_salon/cuisine/bureau/chambre_sonoff_contact  (NAT)
  ├─→ sensor.groupe                   (NAT - présence P4)
  ├─→ sensor.th_balcon_nord_temperature (NAT - T° ext)
  ├─→ sensor.temperature_cible        (TPL)
  ├─→ sensor.mode_ete_hiver           (TPL)
  └─→ sensor.temperature_confort_jour (TPL)
        [condition : 07:30 < now < 21:00]
        └─→ script.p1_master_gestion_clim (periode: "jour")
              └─→ L1C3 (Commandes Clim)
```

#### D - Vignette : L1C3

---

---

### ✅ (B) AUTOMATISATION CLIM NUIT (21H00-07H30)
*Fichier : `P1_clim_chauffage/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml`*

#### A - Rôle

Pilote les clims en période nocturne (21h00-07h30) en déléguant au script `p1_master_gestion_clim`. Même logique que (A) mais avec la température de confort nuit et la fenêtre horaire inversée.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | HA start / 21:00 / changement réseau (mamour + eric) / changement état switch clim / ouverture fenêtre / fermeture fenêtre / changement sensor (groupe/T°/mode) |
| Condition | `time after 21:00 before 07:30` |
| Entités lues | `sensor.mamour_network_type`, `sensor.eric_network_type`, `switch.clim_salon_nous`, `switch.clim_bureau_nous`, `switch.clim_chambre_nous`, `binary_sensor.contact_fenetre_*_sonoff_contact` (x4), `sensor.groupe`, `sensor.th_balcon_nord_temperature`, `sensor.temperature_cible`, `sensor.mode_ete_hiver`, `sensor.temperature_confort_nuit` |
| Action | `script.p1_master_gestion_clim` (periode: "nuit") - délégation complète |

#### C - Chaîne de dépendances

```
HA (start) / Horaire 21:00
  ├─→ sensor.mamour_network_type / sensor.eric_network_type   (NAT - réseau)
  ├─→ switch.clim_salon_nous / clim_bureau_nous / clim_chambre_nous  (NAT - prises)
  ├─→ binary_sensor.contact_fenetre_salon/cuisine/bureau/chambre_sonoff_contact  (NAT)
  ├─→ sensor.groupe                    (NAT - présence P4)
  ├─→ sensor.th_balcon_nord_temperature (NAT - T° ext)
  ├─→ sensor.temperature_cible         (TPL)
  ├─→ sensor.mode_ete_hiver            (TPL)
  └─→ sensor.temperature_confort_nuit  (TPL)
        [condition : 21:00 < now < 07:30]
        └─→ script.p1_master_gestion_clim (periode: "nuit")
              └─→ L1C3 (Commandes Clim)
```

#### D - Vignette : L1C3

---

---

### ✅ (C) NOTIFICATION TEMPÉRATURE UP/DOWN (07H30-21H00)
*Fichier : `P1_clim_chauffage/c_notification_temperature_up_ou_down_7h30_21h00.yaml`*

#### A - Rôle

Envoie une notification mobile avec le message clim personnalisé si la T° extérieure change, ou au réveil à 07h30. En cas de capteur indisponible, envoie une notif d'erreur à la place.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.th_balcon_nord_temperature` / 07:30 fixe |
| Condition | `time after 07:30 before 21:00` |
| Entités lues | `sensor.message_clim_personnalise_7h30_21h00`, `sensor.mamour_wi_fi_connection`, `sensor.eric_wi_fi_connection`, `sensor.th_balcon_nord_temperature` |
| Action | `notify.mobile_app_eric` - message = `sensor.message_clim_personnalise_7h30_21h00` (ou notif erreur si capteur KO) |

#### C - Chaîne de dépendances

```
sensor.th_balcon_nord_temperature (NAT) / Horaire 07:30
  [condition : 07:30 < now < 21:00]
  ├─→ sensor.message_clim_personnalise_7h30_21h00 (TPL) → contenu notif
  ├─→ sensor.mamour_wi_fi_connection / sensor.eric_wi_fi_connection (NAT) → garde-fou
  └─→ notify.mobile_app_eric (notif mobile Eric)
        → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

---

### ✅ (D) NOTIFICATION TEMPÉRATURE UP/DOWN (21H00-07H30)
*Fichier : `P1_clim_chauffage/d_notification_temperature_up_ou_down_21h00_7h30.yaml`*

#### A - Rôle

Miroir nocturne de (C) : envoie une notification mobile avec le message clim personnalisé nuit si la T° change, ou au début de nuit à 21h00. Notif d'erreur si capteur indisponible.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.th_balcon_nord_temperature` / 21:00 fixe |
| Condition | `time after 21:00 before 07:30` |
| Entités lues | `sensor.message_clim_personnalise_21h00_7h30`, `sensor.mamour_wi_fi_connection`, `sensor.eric_wi_fi_connection`, `sensor.th_balcon_nord_temperature` |
| Action | `notify.mobile_app_eric` - message = `sensor.message_clim_personnalise_21h00_7h30` (ou notif erreur si capteur KO) |

#### C - Chaîne de dépendances

```
sensor.th_balcon_nord_temperature (NAT) / Horaire 21:00
  [condition : 21:00 < now < 07:30]
  ├─→ sensor.message_clim_personnalise_21h00_7h30 (TPL) → contenu notif
  ├─→ sensor.mamour_wi_fi_connection / sensor.eric_wi_fi_connection (NAT) → garde-fou
  └─→ notify.mobile_app_eric (notif mobile Eric)
        → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

---

### ✅ (E) NOTIFICATION FERMETURE DES FENÊTRES
*Fichier : `P1_clim_chauffage/e_clim_notification_de_fermeture_des_fenetres.yaml`*

#### A - Rôle

Envoie une notification mobile quand une fenêtre passe de ouverte à fermée. Identifie la pièce concernée et signale si toutes les fenêtres sont désormais fermées.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `binary_sensor.contact_fenetre_salon/cuisine/bureau/chambre_sonoff_contact` : `on` -> `off` |
| Condition | Aucune |
| Entités lues | `sensor.nombre_de_fenetres_fermees` (TPL - pour le message "toutes fermées") |
| Action | `notify.mobile_app_eric` - message identifie la pièce + état global fenêtres |

#### C - Chaîne de dépendances

```
binary_sensor.contact_fenetre_*_sonoff_contact (NAT - Sonoff Z2M)
  [on -> off : fermeture]
  ├─→ sensor.nombre_de_fenetres_fermees (TPL) → condition "toutes fermées"
  └─→ notify.mobile_app_eric
        → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

---

### ✅ (F) AUTOMATISATION ARRÊT CLIM NOTIFICATION
*Fichier : `P1_clim_chauffage/f_clim_automatisation_arret_clim_notification.yaml`*

#### A - Rôle

Notifie quand une clim passe à `off` (coupure manuelle), mais seulement si les prises clim sont actives ET toutes les fenêtres fermées. Evite les faux positifs d'arrêt lors d'une fenêtre ouverte.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `climate.clim_salon/bureau/chambre_rm4_mini` -> `off` |
| Conditions | `switch.clim_salon/bureau/chambre_nous` = on ET `binary_sensor.contact_fenetre_*` = off (x4) |
| Entités lues | `climate.clim_*_rm4_mini` (x3), `switch.clim_*_nous` (x3), `binary_sensor.contact_fenetre_*` (x4) |
| Action | `notify.mobile_app_eric` - identifie la pièce (Salon/Bureau/Chambre) |

#### C - Chaîne de dépendances

```
climate.clim_salon/bureau/chambre_rm4_mini (NAT - Broadlink RM4 Mini)
  [-> off]
  [condition : switches clim ON + fenêtres toutes fermées]
  └─→ notify.mobile_app_eric (titre : ARRÊT CLIM, pièce identifiée)
        → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

---

### ✅ (G) NOTIFICATION CHANGEMENT DE MODE ÉTÉ/FAN/HIVER
*Fichier : `P1_clim_chauffage/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml`*

#### A - Rôle

Notifie quand le mode clim change entre Été (cool), Ventilateur (fan_only) et Hiver (heat), via le sensor de mode.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.mode_ete_hiver` |
| Condition | Aucune |
| Entités lues | `sensor.mode_ete_hiver` (TPL), `sensor.mode_ete_hiver_etat` (TPL - libellé lisible) |
| Action | `notify.mobile_app_eric` - message = état du mode en majuscules |

#### C - Chaîne de dépendances

```
sensor.mode_ete_hiver (TPL)
  └─→ sensor.mode_ete_hiver_etat (TPL) → libellé (Été/Fan/Hiver)
        └─→ notify.mobile_app_eric (titre : CHANGEMENT DE MODE)
              → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

---

### ✅ (H) DEBUG FORCE MODE CORRECT & SÉCURITÉ
*Fichier : `P1_clim_chauffage/h_clim_debug_force_mode_correct_securite.yaml`*

#### A - Rôle

Watchdog double : (1) force OFF si une clim tente de démarrer alors que la prise est coupée ou qu'un arrêt sécurisé est en cours ; (2) force le mode saison correct si une clim tourne dans le mauvais mode (ex: cool au lieu de heat). Notifie à chaque correction.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `climate.clim_salon/bureau/chambre_rm4_mini` (tout état) + changement `sensor.mode_ete_hiver` |
| Condition | Aucune (logique dans les variables) |
| Entités lues | `climate.clim_*_rm4_mini` (x3), `switch.clim_*_nous` (x3), `input_boolean.clim_*_arret_securise_en_cours` (x3), `sensor.mode_ete_hiver` |
| Actions | `climate.set_hvac_mode` (off ou mode saison) + `notify.mobile_app_eric` |

#### C - Chaîne de dépendances

```
climate.clim_salon/bureau/chambre_rm4_mini (NAT) / sensor.mode_ete_hiver (TPL)
  └─→ switch.clim_*_nous (NAT) → garde-fou prise
  └─→ input_boolean.clim_*_arret_securise_en_cours (Helper UI) → garde-fou ACS
        [si force_off] → climate.set_hvac_mode = off + notify.mobile_app_eric (SÉCURITÉ CLIM)
        [si force_mode] → climate.set_hvac_mode = mode_saison + notify.mobile_app_eric (CORRECTION MODE)
              └─→ L1C3 (état clim corrigé)
```

#### D - Vignette : L1C3

---

---

### ✅ (I) SYNCHRO & NOTIF CLIM SI PRISE COUPÉE
*Fichier : `P1_clim_chauffage/i_synchro_notif_clim_si_prise_coupee.yaml`*

#### A - Rôle

Quand une prise clim passe de on à off, force immédiatement le thermostat correspondant à off pour garder les états cohérents. Si c'est en période diurne (07h30-21h00), envoie aussi une notification.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `switch.clim_salon/bureau/chambre_nous` : `on` -> `off` |
| Condition | Aucune (la notif est conditionnée en interne : 07:30-21:00) |
| Entités lues | `switch.clim_*_nous` (trigger), `climate.clim_*_rm4_mini` (cible) |
| Actions | `climate.set_hvac_mode = off` (synchro état) + `notify.mobile_app_eric` si période diurne |

#### C - Chaîne de dépendances

```
switch.clim_salon/bureau/chambre_nous (NAT - prise NOUS)
  [on -> off]
  ├─→ climate.clim_salon/bureau/chambre_rm4_mini → set_hvac_mode: off (synchro état)
  └─→ [si 07:30 < now < 21:00] notify.mobile_app_eric (titre : CLIM COUPÉE)
        → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

---

### ✅ (J) DEBUG NOTIFIER LES CHANGEMENTS DE MESSAGE CLIM
*Fichier : `P1_clim_chauffage/j_debug_notifier_les_changements_de_message_clim_mobile.yaml`*

#### A - Rôle

Surveille `sensor.message_clim_personnalise_7h30_21h00` et notifie chaque changement en décodant son contenu : présence (CELLULAR/MAMOUR/ERIC/LES DEUX), tendance T° (Up/Down/stable), mode actif (HEAT/COOL/FAN). Outil de debug pour suivre les transitions du message clim.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.message_clim_personnalise_7h30_21h00` |
| Condition | Aucune |
| Entités lues | `sensor.message_clim_personnalise_7h30_21h00` (TPL - contenu du message) |
| Action | `notify.mobile_app_eric` - 8 cas détectés par parsing du contenu du sensor |

#### C - Chaîne de dépendances

```
sensor.message_clim_personnalise_7h30_21h00 (TPL)
  └─→ parsing contenu (CELLULAR / MAMOUR / ERIC / LES DEUX / Up / Down / stable / HEAT / COOL / FAN)
        └─→ notify.mobile_app_eric (message debug contextualisé)
              → Aucune vignette dashboard (debug pur)
```

#### D - Vignette : - notif

---

## 🗂️ P1 CUISINE - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ (A) CHAUFFAGE CUISINE HORAIRES SEMAINE
*Fichier : `P1_cuisine/a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml`*

#### A - Rôle

Régule le radiateur cuisine ON/OFF sur plages horaires spécifiques : 04:45-07:00 (LMMJ) ou 05:45-08:00 (VSD). Si T° < 19.9° -> heat, si T° > 20.5° -> off. Arrêt forcé à la fin de chaque plage. Actif seulement si Eric ou Mamour est à la maison.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 04:45 / 05:45 / 07:00 / 08:00 (horaires) + `sensor.th_cuisine_temperature` < 19.9 ou > 20.5 |
| Conditions | Présence `person.eric` OU `person.mamour` + plage horaire selon jour |
| Entités lues | `sensor.th_cuisine_temperature`, `person.eric`, `person.mamour` |
| Actions | `climate.radiateur_cuisine` set_hvac_mode (heat/off) + `notify.mobile_app_eric` |

#### C - Chaîne de dépendances

```
sensor.th_cuisine_temperature (NAT - Z2M) / Horaires 04:45/05:45/07:00/08:00
  [condition : présence + plage horaire]
  ├─→ [< 19.9°] climate.radiateur_cuisine → heat + notify.mobile_app_eric
  ├─→ [> 20.5°] climate.radiateur_cuisine → off + notify.mobile_app_eric
  └─→ [fin plage] climate.radiateur_cuisine → off forcé + notify.mobile_app_eric
        └─→ L1C3 (état radiateur cuisine)
```

#### D - Vignette : L1C3

---

### ✅ (B) CHAUFFAGE CUISINE VACANCES
*Fichier : `P1_cuisine/b_chauffage_cuisine_vacances.yaml`*

#### A - Rôle

Version vacances du chauffage cuisine : plage 06:00-08:30 tous les jours, même logique T° (19.9°<->20.5°), arrêt forcé à 08:30. Actif seulement si présence Eric ou Mamour.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 06:00 / 08:30 (horaires) + `sensor.th_cuisine_temperature` < 19.9 ou > 20.5 |
| Conditions | Présence + plage 06:00-08:30 (dans l'action choose) |
| Entités lues | `sensor.th_cuisine_temperature`, `person.eric`, `person.mamour` |
| Actions | `climate.radiateur_cuisine` set_hvac_mode (heat/off) + `notify.mobile_app_eric` |

#### C - Chaîne de dépendances

```
sensor.th_cuisine_temperature (NAT) / Horaires 06:00/08:30
  [condition : présence + 06:00 < now < 08:30]
  ├─→ [< 19.9°] climate.radiateur_cuisine → heat + notify.mobile_app_eric
  ├─→ [> 20.5°] climate.radiateur_cuisine → off + notify.mobile_app_eric
  └─→ [08:30] climate.radiateur_cuisine → off forcé + notify.mobile_app_eric
        └─→ L1C3 (état radiateur cuisine)
```

#### D - Vignette : L1C3

---

## 🗂️ P1 SALLE DE BAIN - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ (A) GESTION INTELLIGENTE SOUFFLANT SDB
*Fichier : `P1_sdb/a_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml`*

#### A - Rôle

Gestion complète du soufflant SDB : allumage via interrupteur virtuel avec sélection puissance selon T° (2000W si < 21°, 1000W sinon), régulation thermique (coupe résistance si > 23°C, rallume si < 22°C), auto-off 60 min, et cycle de refroidissement avant coupure physique de la prise.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `switch.inter_soufflant_salle_de_bain` / T° SDB > 22.9°C (1min) / T° SDB < 21.9°C / auto-off 60min si inter ON |
| Entités lues | `switch.inter_soufflant_salle_de_bain`, `sensor.th_salle_de_bain_temperature`, `input_select.etat_resistance_soufflant_sdb` |
| Actions | `switch.prise_soufflant_salle_de_bain_nous` (ON/OFF), `remote.send_command` IR (soufflant_sdb), `climate.soufflant_salle_de_bain` (heat/off), `input_select.etat_resistance_soufflant_sdb` |

#### C - Chaîne de dépendances

```
switch.inter_soufflant_salle_de_bain (Helper - interrupteur virtuel)
  [ON] → switch.prise_soufflant_salle_de_bain_nous → ON
       → remote.soufflant_sdb IR on_off + 1000w (x2 si 2000W)
       → input_select.etat_resistance_soufflant_sdb → 2000W / 1000W
       → climate.soufflant_salle_de_bain → heat

sensor.th_salle_de_bain_temperature (NAT - Z2M)
  [> 23°C] → remote.soufflant_sdb IR 1000w → input_select → 0W (coupe résistance)
  [< 22°C] → remote.soufflant_sdb IR 1000w → input_select → 1000W (rallume)

auto-off 60min → switch.inter_soufflant OFF → remote IR on_off → delay 1min
  → climate.soufflant_salle_de_bain → off → switch.prise → OFF → input_select → 0W

        └─→ L1C3 (état soufflant SDB)
```

#### D - Vignette : L1C3

---

### ✅ (D) WATCHDOG SÉCURITÉ RADIATEUR SDB
*Fichier : `P1_sdb/d_salle_de_bain_watchdog_securite_radiateur.yaml`*

#### A - Rôle

Watchdog thermique de sécurité : si T° SDB > 25°C avec dérive rapide (>= +0.5°C), coupe le soufflant via reset IR + coupure physique de la prise après délai de refroidissement. Notifie sur mobile. Ne s'active que si la prise est alimentée et l'inter ON.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.th_salle_de_bain_temperature` |
| Conditions | `switch.prise_soufflant_salle_de_bain_nous` = on + `input_boolean.inter_soufflant_salle_de_bain` = on + T° > 25°C + dérive >= +0.5°C |
| Entités lues | `sensor.th_salle_de_bain_temperature`, `switch.prise_soufflant_salle_de_bain_nous`, `input_boolean.inter_soufflant_salle_de_bain` |
| Actions | delay 1min + `remote.soufflant_sdb` IR on_off (reset) + `input_boolean.inter_soufflant_salle_de_bain` off + delay 1min + `switch.prise_soufflant_salle_de_bain_nous` off + `notify.mobile_app_eric` |

#### C - Chaîne de dépendances

```
sensor.th_salle_de_bain_temperature (NAT)
  [> 25°C + dérive +0.5°C + prise ON + inter ON]
  → delay 1min (stabilisation)
  → remote.soufflant_sdb IR on_off (reset physique)
  → input_boolean.inter_soufflant_salle_de_bain → off
  → delay 1min (refroidissement)
  → switch.prise_soufflant_salle_de_bain_nous → off
  → notify.mobile_app_eric (⚠️ Watchdog SDB)
        └─→ L1C3 (état soufflant)
```

#### D - Vignette : L1C3

---

### ✅ (E) MINUTERIE SECHE-SERVIETTES (2H)
*Fichier : `P1_sdb/e_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml`*

#### A - Rôle

Timer de sécurité 2h sur le sèche-serviettes : se déclenche dès détection de puissance > 50W, attend 2h, puis coupe si encore allumé. Réarme en veille (rallume la prise) après 1 min pour la prochaine utilisation.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `sensor.prise_seche_serviette_salle_de_bain_nous_power` > 50W |
| Conditions | Aucune (vérif état dans l'action) |
| Entités lues | `sensor.prise_seche_serviette_salle_de_bain_nous_power`, `switch.prise_seche_serviette_salle_de_bain_nous` |
| Actions | delay 2h + `switch.prise_seche_serviette_salle_de_bain_nous` off + notify + delay 1min + switch ON (réarmement veille) |

#### C - Chaîne de dépendances

```
sensor.prise_seche_serviette_salle_de_bain_nous_power (NAT - NOUS)
  [> 50W]
  → delay 2h
  → [si switch encore ON] switch.prise_seche_serviette_salle_de_bain_nous → off
  → notify.mobile_app_eric (Sèche-Serv. OFF)
  → delay 1min → switch → on (réarmement veille)
        → Aucune vignette dashboard (sécurité pure)
```

#### D - Vignette : L1C3

---

## 🗂️ P2 PRISES - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ ECO PRISES DYNAMIQUE BY PRÉSENCE/GROUPE
*Fichier : `P2_prises/eco_prises_dinamique_by_presence_groupe.yaml`*

**A - Rôle**

Pilote dynamiquement les prises selon le groupe de présence actif (G1=absent, G2=Mamour, G3=Eric, G4=tous). La liste des prises et leurs groupes autorisés est externalisée dans `sensor.eco_prises_config` (template). Chaque changement de groupe déclenche un ON/OFF de chaque prise selon sa config. Envoie un résumé du nombre de prises ON.

**B - Triggers / Entités**

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.groupe` |
| Condition | Ignore les transitions depuis `unavailable`/`unknown` (boot HA) |
| Entités lues | `sensor.groupe`, `sensor.eco_prises_config` (attr `prises` = liste entity+groupes) |
| Actions | `homeassistant.turn_on/off` sur chaque prise de la liste + `notify.mobile_app_eric` (résumé X/N prises ON) |

**C - Chaîne de dépendances**

```
sensor.groupe (TPL - P4)
  └─→ sensor.eco_prises_config (TPL P2 - liste prises + groupes autorisés)
        └─→ [pour chaque prise] homeassistant.turn_on/off si groupe dans groupes
              └─→ notify.mobile_app_eric (ECO PRISES: G1/G2/G3/G4)
                    └─→ L3C2 (vignette Commandes Éco Prises)
```

**D - Vignette : L3C2**

---

### ✅ GESTION PC BUREAU : SCENE DE FIN + NOTIF
*Fichier : `P2_prises/gestion_pc_bureau_scene_de_fin_notif.yaml`*

**A - Rôle**

Double pilotage via bouton IKEA TRADFRI (MQTT) et détection veille (puissance prise PC < 40W 2min). Bouton ON : allume Hue Smart Eco PC. Bouton OFF ou veille détectée : éteint la lumière et notifie "PC Bureau [OFF]". La prise reste ON pour le suivi conso.

**B - Triggers / Entités**

| | Détail |
|:--|:--|
| Triggers | MQTT `zigbee2mqtt2/Poussoir (IKEA TRADFRI)/action` (on/off) + `sensor.prise_bureau_pc_ikea_power` < 40W pendant 2min |
| Entités lues | `sensor.prise_bureau_pc_ikea_power`, `light.hue_smart_eco_pc_bureau` |
| Actions | `light.turn_on/off hue_smart_eco_pc_bureau` + `notify.mobile_app_eric` (titre: Veille détectée) |

**C - Chaîne de dépendances**

```
MQTT zigbee2mqtt2/Poussoir (IKEA TRADFRI) (NAT)
  └─→ [ON] light.hue_smart_eco_pc_bureau → turn_on

sensor.prise_bureau_pc_ikea_power (NAT - IKEA)
  [< 40W 2min] → light.hue_smart_eco_pc_bureau → turn_off
              → notify.mobile_app_eric (Veille détectée / PC Bureau [OFF])
        → Aucune vignette dashboard (notification pure)
```

**D - Vignette : - notif**

---

### ✅ GESTION TV CHAMBRE : SCENE DE FIN + NOTIF
*Fichier : `P2_prises/gestion_tv_chambre_scene_de_fin_notif.yaml`*

**A - Rôle**

Même logique que PC bureau, adaptée à la TV chambre : bouton IKEA TRADFRI TV (MQTT) pour ON/OFF, détection veille TV (puissance < 20W 2min). Allume lumière ambiance et prise TV à l'allumage, éteint la lumière et notifie à la mise en veille.

**B - Triggers / Entités**

| | Détail |
|:--|:--|
| Triggers | MQTT `zigbee2mqtt2/Poussoir TV (IKEA TRADFRI)/action` (on/off) + `sensor.prise_tv_chambre_nous_power` < 20W 2min |
| Entités lues | `sensor.prise_tv_chambre_nous_power`, `switch.prise_tv_chambre_nous`, `light.hue_smart_eco_tv_chambre` |
| Actions | [ON] `light.turn_on + switch.turn_on` / [OFF/veille] `light.turn_off + notify.mobile_app_eric` |

**C - Chaîne de dépendances**

```
MQTT zigbee2mqtt2/Poussoir TV (IKEA TRADFRI) (NAT)
  └─→ [ON] light.hue_smart_eco_tv_chambre ON + switch.prise_tv_chambre_nous ON

sensor.prise_tv_chambre_nous_power (NAT - NOUS)
  [< 20W 2min] → light.hue_smart_eco_tv_chambre → turn_off
              → notify.mobile_app_eric (Veille détectée / Prise TV [OFF])
        → Aucune vignette dashboard (notification pure)
```

**D - Vignette : - notif**

---

## 🗂️ P3 ECLAIRAGE - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ ACTIVATION ÉCRAN SYNCHRO
*Fichier : `P3_eclairage/p3_bureau_activation_ecran_synchro.yaml`*

#### A - Rôle

Synchronise l'interrupteur de l'écran (switch Hue Play) avec l'état du PC bureau. Allume l'écran dès que le moniteur est détecté actif. L'extinction est gérée par l'automation "Forcer Play ON" (logique inverse via présence PC).

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `binary_sensor.moniteur_pc` → ON (id: pc_on) / OFF 2min (id: pc_off) |
| Condition | Aucune |
| Entités lues | `binary_sensor.moniteur_pc` |
| Actions | [pc_on] `switch.turn_on ecran_p_c_3_play_hue` |

#### C - Chaîne de dépendances

```
binary_sensor.moniteur_pc (NAT - Browser Mod ou sensor PC)
  [→ on] switch.ecran_p_c_3_play_hue → ON
        └─→ L3C1 (vignette Commandes Éclairage)
```

#### D - Vignette : L3C1

---

### ✅ BOUTON RODRET TOGGLE BLANCHES
*Fichier : `P3_eclairage/p3_bureau_bouton_rodret_toggle_blanches.yaml`*

#### A - Rôle

Toggle des 2 lampes blanches bureau (hue_white_lamp_bureau_1+2) via bouton IKEA RODRET (MQTT). Si l'une des deux est ON : éteint tout. Si tout est OFF : allume tout. Met à jour sensor.bureau_etat après action.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | MQTT `zigbee2mqtt2/Inter Bureau (RODRET)` (payload action in [on, off]) |
| Condition | Aucune |
| Entités lues | `light.hue_white_lamp_bureau_1`, `light.hue_white_lamp_bureau_2` |
| Actions | `light.turn_on/off` sur les 2 lampes blanches + `homeassistant.update_entity sensor.bureau_etat` |

#### C - Chaîne de dépendances

```
MQTT zigbee2mqtt2/Inter Bureau (RODRET) (NAT - Z2M)
  [payload on/off] → [si une lampe ON] light.hue_white_lamp_bureau_1+2 → off
                  → [si tout OFF] light.hue_white_lamp_bureau_1+2 → on
  → homeassistant.update_entity sensor.bureau_etat
        └─→ L3C1
```

#### D - Vignette : L3C1

---

### ✅ FORCER PLAY ON SI PC TOURNE
*Fichier : `P3_eclairage/p3_bureau_forcer_play_on_si_pc_tourne.yaml`*

#### A - Rôle

Watchdog des Hue Play bureau : si l'une des 3 lampes Play s'éteint manuellement alors que le PC tourne (moniteur actif), la rallume immédiatement. Empêche l'extinction manuelle accidentelle pendant la session de travail.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `light.hue_play_1/2/3_pc_bureau` → off |
| Condition | `binary_sensor.moniteur_pc` = on |
| Entités lues | `light.hue_play_1/2/3_pc_bureau`, `binary_sensor.moniteur_pc` |
| Actions | `light.turn_on trigger.entity_id` (rallumage de la lampe déclenchante) |

#### C - Chaîne de dépendances

```
light.hue_play_1/2/3_pc_bureau (NAT - Hue)
  [→ off + binary_sensor.moniteur_pc = on]
  → light.turn_on trigger.entity_id (rallumage immédiat)
        └─→ L3C1
```

#### D - Vignette : L3C1

---

### ✅ WATCHDOG SYNCHRO LAMPES BLANCHES
*Fichier : `P3_eclairage/p3_bureau_watchdog_synchronisation_lampes_blanches.yaml`*

#### A - Rôle

Assure que les 2 lampes blanches bureau sont toujours synchronisées. Si l'une s'allume et que l'autre reste éteinte après 5s, force l'allumage des deux. Met à jour sensor.bureau_etat.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `light.hue_white_lamp_bureau_1` → on (5s) / `light.hue_white_lamp_bureau_2` → on (5s) |
| Condition | L'une des deux lampes est encore off |
| Entités lues | `light.hue_white_lamp_bureau_1`, `light.hue_white_lamp_bureau_2` |
| Actions | `light.turn_on` sur les 2 lampes + `homeassistant.update_entity sensor.bureau_etat` |

#### C - Chaîne de dépendances

```
light.hue_white_lamp_bureau_1 ou 2 (NAT - Hue) → on (5s)
  [condition : l'autre lampe encore off]
  → light.turn_on hue_white_lamp_bureau_1+2 (synchro forcée)
  → homeassistant.update_entity sensor.bureau_etat
        └─→ L3C1
```

#### D - Vignette : L3C1

---

### ✅ ALLUMAGE LUMIÈRE
*Fichier : `P3_eclairage/p3_entree_allumage_lumiere.yaml`*

#### A - Rôle

Allume la lumière de l'entrée lors de deux cas : (1) premier retour à la maison en période diurne (G1 → G2/3/4, soleil levé), (2) retour de Mamour quand Eric est déjà là (G3 → G4). Pas d'extinction automatique - gérée manuellement.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.groupe` |
| Conditions | CAS 1 : from=groupe_1 + to in [groupe_2/3/4] + sun above_horizon / CAS 2 : from=groupe_3 + to=groupe_4 |
| Entités lues | `sensor.groupe`, `sun.sun` |
| Actions | `light.turn_on light.entree` |

#### C - Chaîne de dépendances

```
sensor.groupe (TPL - P4)
  [G1→G2/3/4 + soleil levé] → light.entree → on
  [G3→G4]                   → light.entree → on
        └─→ L3C1
```

#### D - Vignette : L3C1

---

### ✅ BOUTON IKEA INTER SALON (4)
*Fichier : `P3_eclairage/p3_salon_bouton_ikea_inter_salon.yaml`*

#### A - Rôle

Pilotage direct de `light.salon` via le bouton IKEA 4 touches Salon (MQTT). Bouton ON → allume, Bouton OFF → éteint. Logique simple sans condition.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | MQTT `zigbee2mqtt2/Inter Salon (4) (IKEA)/action` payload=on (id: bouton_on) / payload=off (id: bouton_off) |
| Condition | Aucune |
| Entités modifiées | `light.salon` |
| Actions | `light.turn_on/off light.salon` |

#### C - Chaîne de dépendances

```
MQTT zigbee2mqtt2/Inter Salon (4) (IKEA) (NAT - Z2M)
  [on] → light.salon → turn_on
  [off] → light.salon → turn_off
        └─→ L3C1
```

#### D - Vignette : L3C1

---

### ✅ BOUTON IKEA SOMRIG
*Fichier : `P3_eclairage/p3_salon_bouton_ikea_somrig.yaml`*

#### A - Rôle

Pilotage simplifié de `light.salon` via le bouton IKEA SOMRIG (2 boutons, MQTT). N'importe quel appui bouton 1 (simple/double/long) → allume. N'importe quel appui bouton 2 → éteint. 6 triggers au total.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | MQTT `zigbee2mqtt2/Inter (SOMRIG)/action` : 3 payloads bouton 1 (1_short/double/long_release) + 3 payloads bouton 2 (2_*) |
| Condition | Aucune |
| Entités modifiées | `light.salon` |
| Actions | `light.turn_on/off light.salon` |

#### C - Chaîne de dépendances

```
MQTT zigbee2mqtt2/Inter (SOMRIG) (NAT - Z2M)
  [bouton 1 any] → light.salon → turn_on
  [bouton 2 any] → light.salon → turn_off
        └─→ L3C1
```

#### D - Vignette : L3C1

---

### ✅ SYNC MIROIR LAMPE ET RELAIS SDB
*Fichier : `P3_eclairage/p3_sdb_sync_miroir_lampe_et_relais_sdb.yaml`*

#### A - Rôle

Maintient la synchronisation entre la lampe Hue SDB et le relais Sonoff. Tout changement d'état de la lampe Hue est reproduit sur le relais. Si la lampe passe ON, force aussi le relais ON (double sécurité).

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `light.hue_white_lamp_salle_de_bain` |
| Condition | Aucune |
| Entités lues | `light.hue_white_lamp_salle_de_bain` |
| Actions | `switch.turn_{{ trigger.to_state.state }} relais_lumiere_sdb_sonoff` + [si ON] force turn_on des deux |

#### C - Chaîne de dépendances

```
light.hue_white_lamp_salle_de_bain (NAT - Hue)
  [→ on] → switch.relais_lumiere_sdb_sonoff → turn_on + light → turn_on (sécurité)
  [→ off] → switch.relais_lumiere_sdb_sonoff → turn_off
        └─→ L3C1
```

#### D - Vignette : L3C1

---

## 🗂️ P4 PRESENCE - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ [P4] ERIC LOG ZONES
*Fichier : `P4_presence/P4_log_zones_eric.yaml`*

#### A - Rôle

Prototype abandonné : loggait les changements de zone d'Eric dans un fichier texte. Conservé en archive, non actif en prod.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement de zone `person.eric` |
| Condition | - |
| Entités lues | `person.eric` |
| Actions | `notify.file_zone_eric_txt` (log dans zone_eric.txt) |

#### C - Chaîne de dépendances

```
person.eric (NAT)
  [changement de zone]
  → notify.file_zone_eric_txt → /config/.logs/zone_eric.txt
        → Proto à l'abandon - pas de vignette
```

#### D - Vignette : - proto à l'abandon (conservé)

---

## 🗂️ ENERGIE (P0) - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ BASCULEMENT TARIF HC/HP GENELEC APPART
*Fichier : `energie/auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml`*

#### A - Rôle

Bascule le tarif (HC/HP) des 4 Utility Meters Genelec Appart (quotidien/hebdo/mensuel/annuel) aux heures de transition Linky : HC à 01h00 et 13h00, HP à 07h30 et 14h30. Critique pour la comptabilisation séparée HP/HC.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 01:00 (hc_1) / 07:30 (hp_1) / 13:00 (hc_2) / 14:30 (hp_2) |
| Condition | Aucune |
| Entités modifiées | `select.genelec_appart_hphc_quotidien/hebdomadaire/mensuel/annuel_um` |
| Actions | `select.select_option` : option=HC ou HP selon trigger |

#### C - Chaîne de dépendances

```
Horloge HA
  [01:00 / 13:00] → select.genelec_appart_hphc_*_um → HC (x4 UM)
  [07:30 / 14:30] → select.genelec_appart_hphc_*_um → HP (x4 UM)
        └─→ L2C1 (vignette Conso Générale - compteurs HP/HC)
```

#### D - Vignette : L2C1

---

### ✅ LOG ECART LINKY VS NODON
*Fichier : `energie/log_ecart_linky_vs_nodon.yaml`*

#### A - Rôle

Enregistre chaque nuit à 23:59 l'écart entre la mesure Linky (J-1) et les mesures Nodon (Riemann + direct) dans un fichier log. Permet de suivre la dérive entre les deux sources d'énergie.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 23:59 fixe |
| Condition | Aucune |
| Entités lues | `sensor.linky_25481620821301_consumption_history`, `sensor.genelec_appart_quotidien_um` (attr last_period x2) |
| Actions | `notify.send_message → notify.log_ecart_energie` → `/config/notifs/ecart_liky_vs_nodon.txt` |

#### C - Chaîne de dépendances

```
sensor.linky_*_consumption_history (NAT - MyElectricalData)
  [23:59]
  ├─→ sensor.genelec_appart_quotidien_um attr last_period (NAT - Nodon UM)
  └─→ calcul écart kWh + %
        → notify.log_ecart_energie → ecart_liky_vs_nodon.txt
              └─→ L2C1 (Conso Générale - suivi dérive Linky/Nodon)
```

#### D - Vignette : L2C1

---

## 🗂️ GITHUB BACKUP - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ [00] ALERTE SI KO 15 MIN
*Fichier : `github_backup/00_backup_alerte_si_ko_15_min.yaml`*

#### A - Rôle

Chien de garde : si `sensor.backup_github_status` reste en KO pendant 15 minutes, envoie une notification d'alerte. Détecte les échecs de push git prolongés.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `sensor.backup_github_status` → KO pendant 15min |
| Condition | Aucune |
| Entités lues | `sensor.backup_github_status` |
| Actions | `notify.mobile_app_eric` (alerte backup KO) |

#### C - Chaîne de dépendances

```
sensor.backup_github_status (CMD - command_line)
  [= KO 15min]
  → notify.mobile_app_eric (alerte backup KO)
        └─→ L5C3 (vignette MariaDB / Backup)
```

#### D - Vignette : L5C3

---

### ✅ [01] GIT HOURLY H+10
*Fichier : `github_backup/01_backup_git_hourly_h_10.yaml`*

#### A - Rôle

Push Git automatique toutes les heures à H+10 (ex: 07:10, 08:10...) + backup natif HA. Garde une trace horaire de l'état de la config.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `time_pattern minutes: '10'` |
| Condition | Aucune |
| Entités modifiées | `sensor.backup_github_status` (mis à jour par script) |
| Actions | `shell_command.git_backup_push` + `backup.create` HA |

#### C - Chaîne de dépendances

```
Horloge HA (toutes les heures à H+10)
  → shell_command.git_backup_push → GitHub repo
  → backup.create HA
  → sensor.backup_github_status (MAJ statut)
        └─→ L5C3
```

#### D - Vignette : L5C3

---

### ✅ [02] GIT DAILY (03:00)
*Fichier : `github_backup/02_backup_git_daily_03_00.yaml`*

#### A - Rôle

Backup natif HA + push Git quotidien à 03h00. Sécurité nocturne en complément du push horaire.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 03:00 fixe |
| Condition | Aucune |
| Actions | `backup.create` HA + `shell_command.git_backup_push` |

#### C - Chaîne de dépendances

```
Horloge HA (03:00)
  → backup.create HA
  → shell_command.git_backup_push → GitHub
        └─→ L5C3
```

#### D - Vignette : L5C3

---

### ✅ [03] GIT WEEKLY (DIM 01:30)
*Fichier : `github_backup/03_backup_git_weekly_dim_01_30.yaml`*

#### A - Rôle

Backup hebdomadaire : chaque dimanche à 01h30, backup natif HA + push Git + tag git weekly pour archivage long terme.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 01:30 fixe + condition weekday=dimanche |
| Condition | `condition: time weekday: sun` |
| Actions | `backup.create` + `shell_command.git_backup_push_weekly` (avec tag) |

#### C - Chaîne de dépendances

```
Horloge HA (dimanche 01:30)
  → backup.create HA
  → shell_command.git_backup_push_weekly → GitHub (tag weekly)
        └─→ L5C3
```

#### D - Vignette : L5C3

---

### ✅ [04] GIT PUSH MANUEL
*Fichier : `github_backup/04_backup_git_push_manuel.yaml`*

#### A - Rôle

Déclenche un push Git manuel via le bouton virtuel `input_button.git_push_manuel` (accessible depuis la vignette L5C3).

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `input_button.git_push_manuel` pressé |
| Condition | Aucune |
| Actions | `shell_command.git_backup_push_manual` |

#### C - Chaîne de dépendances

```
input_button.git_push_manuel (UI - L5C3)
  → shell_command.git_backup_push_manual → GitHub
        └─→ L5C3
```

#### D - Vignette : L5C3

---

### ✅ [05] GIT PUSH WEEKLY MANUEL
*Fichier : `github_backup/05_backup_git_push_weekly_manuel.yaml`*

#### A - Rôle

Déclenche un push Git hebdomadaire manuel (avec tag) via le bouton `input_button.git_push_weekly_manuel`.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `input_button.git_push_weekly_manuel` pressé |
| Condition | Aucune |
| Actions | `shell_command.git_backup_push_weekly` |

#### C - Chaîne de dépendances

```
input_button.git_push_weekly_manuel (UI - L5C3)
  → shell_command.git_backup_push_weekly → GitHub (tag weekly)
        └─→ L5C3
```

#### D - Vignette : L5C3

---

### ✅ [06] GIT AU DÉMARRAGE HA
*Fichier : `github_backup/git_push_au_demarrage_ha.yaml`*

#### A - Rôle

Push Git automatique au démarrage complet de HA, après délai de stabilisation. Garantit que la dernière config est sauvegardée même après un redémarrage inopiné.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `homeassistant event: start` |
| Condition | Aucune |
| Actions | Délai stabilisation + `shell_command.git_backup_push` |

#### C - Chaîne de dépendances

```
homeassistant start (event)
  → délai stabilisation
  → shell_command.git_backup_push → GitHub
        └─→ L5C3
```

#### D - Vignette : L5C3

---

## 🗂️ METEO - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ Alerte Météo France actualisation des "CARTES"
*Fichier : `meteo/alerte_meteo_france_actualisation_des_cartes.yaml`*

#### A - Rôle

Force la mise à jour des images d'alerte Météo France au démarrage, aux heures clés (6h32, 16h32), ou toutes les 5 min si les sensors sont unavailable.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | HA start / 06:32 / 16:32 / toutes les 5 min (si sensor unavailable) |
| Entités lues | `sensor.meteo_france_alertes_image_today`, `sensor.meteo_france_alertes_image_tomorrow` |
| Entités modifiées | `camera.mf_alerte_today`, `camera.mf_alerte_tomorrow` (update_entity forcé) |

#### C - Chaîne de dépendances

```
Météo France (intégration)
  ├─→ sensor.meteo_france_alertes_image_today    (NAT) → condition unavailable + update_entity
  └─→ sensor.meteo_france_alertes_image_tomorrow (NAT) → condition unavailable + update_entity
        └─→ camera.mf_alerte_today / camera.mf_alerte_tomorrow (MAJ forcée)
              └─→ L1C1 (vignette Météo - cartes alertes)
```

#### D - Vignette : L1C1

---

### ✅ METTRE À JOUR LE TEMPS DU DERNIER IMPACT DE FOUDRE
*Fichier : `meteo/mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml`*

#### A - Rôle

Enregistre le timestamp du dernier éclair détecté dans `input_datetime.dernier_eclair`, dès que `sensor.maison_lightning_counter` change et est > 0.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.maison_lightning_counter` |
| Condition | `sensor.maison_lightning_counter` > 0 |
| Entités lues | `sensor.maison_lightning_counter` |
| Actions | `input_datetime.set_datetime dernier_eclair = now()` |

#### C - Chaîne de dépendances

```
sensor.maison_lightning_counter (NAT - Blitzortung)
  [> 0] → input_datetime.dernier_eclair = now()
        └─→ L1C1 (vignette Météo - affiché dans notif foudre)
```

#### D - Vignette : L1C1

---

### ✅ NOTIFICATION DE LA FOUDRE
*Fichier : `meteo/notification_de_la_foudre.yaml`*

#### A - Rôle

Envoie une notification mobile détaillée à chaque impact détecté : distance, direction (16 points cardinaux via azimuth), ville (geocoding Blitzortung), nombre d'impacts. Délai 1min anti-spam entre notifs.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Changement `sensor.maison_lightning_counter` |
| Condition | `sensor.maison_lightning_counter` > 0 |
| Entités lues | `sensor.maison_lightning_distance`, `sensor.maison_lightning_azimuth`, `sensor.maison_lightning_counter`, `sensor.blitzortung_lightning_localisation`, `input_datetime.dernier_eclair` |
| Actions | `homeassistant.update_entity sensor.blitzortung_lightning_localisation` + `notify.mobile_app_eric` (message détaillé) + delay 1min |

#### C - Chaîne de dépendances

```
sensor.maison_lightning_counter (NAT - Blitzortung) [> 0]
  → homeassistant.update_entity sensor.blitzortung_lightning_localisation
  ├─→ sensor.maison_lightning_distance / azimuth (NAT)
  └─→ input_datetime.dernier_eclair (Helper)
        → notify.mobile_app_eric (/!\ Attention foudre)
              → Aucune vignette dashboard (notification pure)
```

#### D - Vignette : - notif

---

### ✅ UPDATE PREVIOUS HUMIDITY
*Fichier : `meteo/update_previous_humidity.yaml`*

#### A - Rôle

Capture l'humidité balcon toutes les 30min et la stocke dans `input_number.th_balcon_nord_humidity_previous`. Alimente le calcul de tendance humidité sur L1C2.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `time_pattern minutes: /30` |
| Condition | Aucune |
| Entités lues | `sensor.th_balcon_nord_humidity` |
| Actions | `input_number.set_value th_balcon_nord_humidity_previous = valeur courante` |

#### C - Chaîne de dépendances

```
Horloge HA (toutes les 30min)
  → sensor.th_balcon_nord_humidity (NAT - Z2M)
  → input_number.th_balcon_nord_humidity_previous (Helper)
        └─→ L1C2 (vignette Températures - tendance humidité)
```

#### D - Vignette : L1C2

---

### ✅ UPDATE PREVIOUS TEMPERATURE
*Fichier : `meteo/update_previous_temperature.yaml`*

#### A - Rôle

Capture la T° balcon toutes les 30min et la stocke dans `input_number.th_balcon_nord_temperature_previous`. Alimente le calcul de tendance T° extérieure sur L1C2 et les messages clim (Up/Down/stable).

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `time_pattern minutes: /30` |
| Condition | Aucune |
| Entités lues | `sensor.th_balcon_nord_temperature` |
| Actions | `input_number.set_value th_balcon_nord_temperature_previous = valeur courante` |

#### C - Chaîne de dépendances

```
Horloge HA (toutes les 30min)
  → sensor.th_balcon_nord_temperature (NAT - Z2M)
  → input_number.th_balcon_nord_temperature_previous (Helper)
        └─→ L1C2 (vignette Températures - tendance T° ext)
              + messages clim (C), (D) → indicateur Up/Down/stable
```

#### D - Vignette : L1C2

---

## 🗂️ STORES - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ GESTION OPTIMISÉE DU STORE BUREAU
*Fichier : `stores/gestion_optimisee_du_store_bureau.yaml`*

#### A - Rôle

Pilotage intelligent du store bureau selon 3 scénarios : A (printemps/automne 18-25°C, diurne : ouvre), B (été > 25°C, avant coucher : ferme), C (coucher soleil : ferme). Sécurité absolue : bloque tout mouvement si fenêtre bureau ouverte.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 07:00 / changement `sensor.th_balcon_nord_temperature` / `sun.sun` sunset / fermeture `binary_sensor.contact_fenetre_bureau_sonoff_contact` |
| Condition | `binary_sensor.contact_fenetre_bureau_sonoff_contact` = off (sécurité) |
| Entités lues | `sensor.th_balcon_nord_temperature`, `sun.sun`, `cover.store_bureau`, `binary_sensor.contact_fenetre_bureau_sonoff_contact` |
| Actions | `cover.open_cover / close_cover store_bureau` |

#### C - Chaîne de dépendances

```
sensor.th_balcon_nord_temperature (NAT) / sun.sun (NAT)
  [condition : fenêtre bureau fermée]
  ├─→ [18°<T°<25° + diurne] cover.store_bureau → open
  ├─→ [T°>25° + avant coucher] cover.store_bureau → close
  └─→ [sunset] cover.store_bureau → close
        └─→ L3C3 (vignette Fenêtres + Stores)
```

#### D - Vignette : L3C3

---

### ✅ GESTION SIMPLE DU STORE SALON (MATIN/SOIR)
*Fichier : `stores/gestion_simple_du_store_salon_matin_soir.yaml`*

#### A - Rôle

Pilotage simple du store salon : ouvre au lever du soleil (pas avant 06:30), ferme au coucher. Sécurité identique : bloque si fenêtre salon ouverte.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 06:30 (id: ouverture) / `sun.sun` sunrise (id: ouverture) / `sun.sun` sunset (id: fermeture) |
| Condition | `binary_sensor.contact_fenetre_salon_sonoff_contact` = off (sécurité) |
| Entités lues | `sun.sun`, `binary_sensor.contact_fenetre_salon_sonoff_contact` |
| Actions | `cover.open_cover / close_cover store_salon` |

#### C - Chaîne de dépendances

```
sun.sun (NAT) / Horloge 06:30
  [condition : fenêtre salon fermée]
  ├─→ [sunrise + > 06:30] cover.store_salon → open
  └─→ [sunset] cover.store_salon → close
        └─→ L3C3
```

#### D - Vignette : L3C3

---

## 🗂️ SYSTEME - AUTOMATIONS
*Ajouté le 2026-08-08*

---

### ✅ DB PURGE MARIADB + REPACK
*Fichier : `systeme/db_purge_mariadb_repack.yaml`*

#### A - Rôle

Ménage nocturne : purge la base MariaDB à 7 jours de rétention puis Repack pour libérer l'espace disque. Se déclenche chaque nuit à 00:30.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 00:30 fixe |
| Condition | Aucune |
| Actions | `recorder.purge keep_days: 7` + `recorder.purge_entities` (repack) |

#### C - Chaîne de dépendances

```
Horloge HA (00:30)
  → recorder.purge (7j rétention) → MariaDB (LXC 201)
  → recorder.purge_entities (repack)
        └─→ L5C3 (vignette MariaDB - taille DB)
```

#### D - Vignette : L5C3

---

### ✅ DIAG ENREGISTREMENT JOURNALIER (7 POSTES + DUT)
*Fichier : `systeme/diag_enregistrement_journalier.yaml`*

#### A - Rôle

Log toutes les 15 min la consommation des 7 postes énergétiques, la T° extérieure et le DUT chauffage dans un fichier texte. Outil de diagnostic continu, sans vignette dashboard.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `time_pattern minutes: /15` |
| Condition | Aucune |
| Entités lues | Sensors des 7 postes conso + `sensor.th_balcon_nord_temperature` + DUT chauffage |
| Actions | `notify.send_message → notify.file_diag_conso_elec_txt` → `/config/notifs/diag_conso_elec.txt` |

#### C - Chaîne de dépendances

```
Horloge HA (toutes les 15min)
  → sensors 7 postes conso + T° ext + DUT
  → notify.file_diag_conso_elec_txt → diag_conso_elec.txt
        → - log (pas de vignette dashboard)
```

#### D - Vignette : - log (écrit dans diag_conso_elec.txt toutes les 15min)

---

### ✅ ÉCONOMIE ÉNERGIE VS CODE
*Fichier : `systeme/systeme_economie_energie_vs_code.yaml`*

#### A - Rôle

Coupe VS Code si son CPU dépasse 10% pendant 10min ou si inactif. Demande confirmation avant coupure. Fonctionne H24. Impacte la vignette HOME PAGE (état serveur Studio Code Server).

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | `sensor.studio_code_server_pourcentage_du_processeur` > 10% 10min + inactivité |
| Condition | Aucune |
| Entités lues | `sensor.studio_code_server_pourcentage_du_processeur` |
| Actions | Notification confirmation + `shell_command` coupure VS Code |

#### C - Chaîne de dépendances

```
sensor.studio_code_server_pourcentage_du_processeur (NAT - Studio Code Server add-on)
  [> 10% 10min ou inactif]
  → notify.mobile_app_eric (confirmation)
  → shell_command coupure VS Code
        └─→ HOME PAGE (état serveur)
```

#### D - Vignette : HOME PAGE

---

### ✅ WATCHDOG PILES (HUE/IKEA/SONOFF)
*Fichier : `systeme/systeme_watchdog_piles_hue_ikea_sonoff.yaml`*

#### A - Rôle

Vérifie 3 fois par jour (08:00/14:00/20:00) l'état des piles des équipements Zigbee via les groupes de la vue synthétique (seuil < 11%). Envoie une notification si des piles sont faibles.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 08:00 / 14:00 / 20:00 |
| Condition | `sensors != ''` + filtre jour de la semaine |
| Entités lues | Groupes batteries HUE/IKEA/SONOFF (via `groups/`) |
| Actions | `notify.mobile_app_eric` si piles < 11% |

#### C - Chaîne de dépendances

```
Horloge HA (08:00 / 14:00 / 20:00)
  → groups/GRP_HUE_batteries / GRP_IKEA_batteries / GRP_SONOFF_batteries
  [< 11%] → notify.mobile_app_eric (liste appareils à piles faibles)
        └─→ L5C1 (vignette Piles / Batteries)
```

#### D - Vignette : L5C1

---

### ✅ VEILLE GITHUB NOUVELLE RELEASE DÉTECTÉE
*Fichier : `systeme/veille_github_nouvelle_release_detectee.yaml`*

#### A - Rôle

Surveille les flux Feedreader GitHub (HA core + HACS + cartes HACS). Envoie une notification Telegram à chaque nouvelle release. Double notification si le titre contient un breaking change ou une deprecation.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | Event `feedreader_entry_added` (intégration Feedreader) |
| Condition | Aucune |
| Entités lues | Feedreader (flux RSS GitHub HA/HACS/cartes) |
| Actions | `notify.telegram` (ou mobile) - double notif si breaking change |

#### C - Chaîne de dépendances

```
Feedreader (intégration HA) - flux RSS GitHub
  [nouvelle entrée] → event feedreader_entry_added
  → [si breaking change] double notify
  → notify.telegram / notify.mobile_app_eric (titre release)
        └─→ L4C3 (vignette Mises à jour HA)
```

#### D - Vignette : L4C3

---

### ✅ Z2M LAST_SEEN
*Fichier : `systeme/z2m_last_seen.yaml`*

#### A - Rôle

Surveille les capteurs Zigbee2MQTT injoignables (last_seen > 8h ou unavailable). Se déclenche à 06:00 et toutes les 15min si des capteurs sont hors ligne. Notifie la liste des capteurs perdus.

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Triggers | 06:00 / `time_pattern minutes: /15` |
| Condition | `sensors != ''` + filtre jour (variable) |
| Entités lues | Tous les capteurs Zigbee Z2M (last_seen via template) |
| Actions | `notify.mobile_app_eric` (liste capteurs last_seen > 8h ou unavailable) |

#### C - Chaîne de dépendances

```
Horloge HA (06:00 + toutes les 15min)
  → template : liste sensors Z2M avec last_seen > 8h ou unavailable
  [si liste non vide] → notify.mobile_app_eric (capteurs Z2M perdus)
        └─→ L5C3 (vignette MariaDB - santé système)
```

#### D - Vignette : L5C3

---

## 🗂️ SCRIPTS
*Ajouté le 2026-08-08*
> Scripts HA appelés par les automations. Un script = logique centralisée réutilisable entre plusieurs automations.
> Fichiers sources : `docs/04_docs_scripts/docs_scripts_YAML/`

### MATRICE DES SCRIPTS - STATUT DÉPENDANCES

| Script | Appelé par | Vignette | Statut |
|:-------|:-----------|:--------:|:------:|
| P1 MASTER GESTION CLIM | P1-A (CLIM JOUR) + P1-B (CLIM NUIT) | L1C3 | ✅ enrichi 2026-08-08 |

---

### ✅ P1 MASTER GESTION CLIM
*Fichier : `docs/04_docs_scripts/docs_scripts_YAML/p1_master_gestion_clim.yaml`*
*Service HA : `script.p1_master_gestion_clim`*

#### A - Rôle

Centralise le pilotage des 3 climatisations (Salon, Bureau, Chambre) selon la période (jour/nuit) et la présence. Appelé par les automations P1-A (CLIM JOUR) et P1-B (CLIM NUIT). Mode `queued` (max 10) - garantit qu'aucun appel concurrent n'est perdu.

Sequence en 6 étapes :
1. Prefix période (`[AJ]` jour / `[AN]` nuit)
2. Délai 1min si redémarrage HA détecté
3. Boucle d'attente capteurs (10 tentatives x 30s max)
4. Calcul des variables globales (mode_saison, groupe_presence, fenetres_ouvertes, temperatures eco/confort)
5. Calcul des cibles par pièce (Salon / Bureau / Chambre selon période + présence)
6. Branche sécurité fenêtres (arrêt forcé) OU commandes standard en parallèle + notif résumé

#### B - Triggers / Entités

| | Détail |
|:--|:--|
| Appelé par | Automation P1-A (CLIM JOUR) + Automation P1-B (CLIM NUIT) |
| Paramètres | `periode` (jour/nuit, obligatoire), `trigger_id`, `trigger_entity_id` |
| Capteurs lus | `sensor.mode_ete_hiver`, `sensor.groupe`, `sensor.temperature_cible`, `sensor.temperature_confort_nuit`, `sensor.temperature_corrige_mamour/_eric/_chambre`, `sensor.temperature_eco_hiver_corrige`, `sensor.temperature_eco_ete_corrige`, `sensor.presence`, `sensor.nombre_de_fenetres_ouvertes` |
| Fenêtres | `binary_sensor.contact_fenetre_salon/cuisine/bureau/chambre_sonoff_contact` (4) |
| Prises clim | `switch.clim_salon/bureau/chambre_nous` |
| Flags sécurité | `input_boolean.clim_salon/bureau/chambre_arret_securise_en_cours` |
| Entités pilotées | `climate.clim_salon/bureau/chambre_rm4_mini` |
| Notif | `notify.mobile_app_eric` (attente capteurs / alerte fenêtre / résumé état) |

#### C - Chaîne de dépendances

```
automation P1-A (CLIM JOUR) --+
automation P1-B (CLIM NUIT) --+--> script.p1_master_gestion_clim [periode, trigger_id, trigger_entity_id]
  --> sensor.mode_ete_hiver + sensor.groupe
  --> sensor.temperature_cible (JOUR) / sensor.temperature_confort_nuit (NUIT)
  --> sensor.temperature_corrige_mamour / _eric / _chambre
  --> binary_sensor.contact_fenetre_* (4 pieces)
    [fenetre ouverte] --> climate.set_hvac_mode OFF (3 clims) + notify ALERTE FENETRE
                         stop : arrêt immédiat
    [fenetres fermees] --> switch.clim_*_nous + input_boolean.clim_*_arret_securise_en_cours
      --> climate.set_temperature + climate.set_hvac_mode (Salon / Bureau / Chambre en parallel)
      --> notify RESUME ETAT CLIMS
            L->  L1C3 (Commandes Clim)
```

#### D - Vignette : L1C3
## 📁 COMPLÉMENT - FICHIERS CONFIG RACINE & RÉPERTOIRES HORS DASHBOARD

> Ces fichiers font partie intégrante de la config HA et sont audités par `audit_md5.sh`.
> Ils n'alimentent pas directement d'entités dashboard - référencés ici pour inventaire complet.
> *Ajouté le 2026-06-15*

### Fichiers racine `/config/`

| Fichier | Rôle | Audité |
|:--------|:-----|:------:|
| `automations.yaml` | Toutes les automations HA (géré via UI) | ✅ |
| `scripts.yaml` | Scripts HA (J-1-x, J-2-0, audit_md5) | ✅ |
| `shell_command/` (répertoire) | Commandes shell (git backup, audit MD5, zone log P4) - `!include_dir_merge_named` | ✅ |
| `configuration.yaml` | Point d'entrée HA - includes, intégrations | ✅ |
| `sql.yaml` | Capteurs SQL (taille MariaDB) → L5C3 | ✅ |
| `input_button.yaml` | Boutons virtuels (déclencheurs UI) | ✅ |
| `input_datetime.yaml` | Helpers date/heure | ✅ |
| `input_select.yaml` | Helpers liste (mode soufflant SDB, etc.) | ✅ |
| `scenes.yaml` | Scènes HA | ❌ hors scope |
| `secrets.yaml` | Identifiants - **NE PAS auditer / synchroniser** | ⛔ |

### Répertoires audités (DIRS)

| Répertoire | Contenu | Audité |
|:-----------|:--------|:------:|
| `sensors/` | Intégrations kWh, stats min/max, qualité air | ✅ |
| `templates/` | Calculs, AVG, UI, météo, présence, stores | ✅ |
| `utility_meter/` | Compteurs AMHQ (P0→P3, météo) | ✅ |
| `command_line/` | Météo France, GitHub maintenance, audit MD5, IP externe | ✅ |
| `groups/` | Groupes batteries HUE/IKEA/SONOFF → L5C1 | ✅ |
| `input_booleans/` | Helpers booléens (verrous clim, présence…) | ✅ |
| `input_number/` | Helpers numériques | ✅ |
| `packages/` | Packages CSS météo (cssmeteo.yaml, demometeo.yaml) - Moon API | ✅ |
| `shell_command/` | Commandes shell (backup Git, audit MD5, zone log P4) | ✅ |

### Intégration FILE (UI uniquement - notify.file interdit en YAML)

> Configurée via : Paramètres → Appareils & Services → Ajouter → File
> Génère des services `notify.file_*` utilisés par les automations.

| Service généré | Fichier destination | Utilisé par |
|:---------------|:--------------------|:------------|
| `notify.file_zone_eric_txt` | `/config/.logs/zone_eric.txt` | `shell_command/P4/P4_log_eric_zone.yaml` → automation P4 présence |
| `notify.file_diag_conso_elec_txt` | `/config/notifs/diag_conso_elec.txt` | automation `energie/diag_enregistrement_journalier.yaml` |
| `notify.file_ecart_liky_vs_nodon_txt` | `/config/notifs/ecart_liky_vs_nodon.txt` | automation `energie/log_ecart_linky_vs_nodon.yaml` |

### Répertoires hors scope audit

| Répertoire | Raison |
|:-----------|:-------|
| `.scripts/` | Scripts shell - pas des entités HA |
| `notifs/` | Fichiers .txt - hors périmètre YAML |
| `blueprints/` | Blueprints HA - non modifiés manuellement |
| `custom_components/` | Intégrations HACS - non versionnées ici |
| `www/` | Ressources frontend - hors config HA |
| `docs_dashboard/` | Ancien répertoire, supprimé le 2026-07-14, remplacé par `docs/02_docs_dashboard/` |

> ✅ **Note 2026-08-08** : ligne ci-dessus confirmée par Eric (2026-08-08). La phrase tronquée
> (coupure sur "docs_da") a été complétée par hypothèse le 2026-07-19 ; hypothèse validée -
> `docs_dashboard/` est bien l'ancien répertoire supprimé le 2026-07-14 tel que documenté dans CLAUDE.md.

---

