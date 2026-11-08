# DEPENDANCES GLOBALES HERMES - TABLEAU DE BORD HA
<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

*Genere par `ReBuild/scripts/hermes_gen_dependances.py` (reconstruction Hermes du 2026-10-25) a partir de l'arbre local : vignettes dashboard, scripts, automations par pole, orphelines. Types deduits de l'emplacement du fichier de definition.*

*Genere le 2026-10-26 19:02. Regles : une entite est rattachee a une vignette si son identifiant apparait dans un YAML de son dossier ; une carte est une ligne `type: ...` ; une entite est ORPHELINE si elle est definie dans la config et n'apparait ni dans un dashboard, ni dans une automation, ni dans un script.*

## LEGENDE

| Symbole | Signification |
|:-------:|:-------------|
| [type] | Type de carte |
| (TPL) | Entite definie dans templates/ |
| (SEN) | Entite definie dans sensors/ |
| (UM) | Entite definie dans utility_meter/ |
| (NAT) | Entite native/UI, command_line, ou fichier non classe |
| ORPHELINE | Entite dans aucun dashboard, automation ni script |

## MATRICE DES VIGNETTES

| ID | Vignette | Entites | Cartes |
|:---|:---------|:-------:|:------:|
| **L0C0** | PAGE_Home | 30 | 19 |
| **L1C1** | METEO | 49 | 120 |
| **L1C2** | TEMPERATURES | 61 | 106 |
| **L1C3** | CLIM | 93 | 222 |
| **L2C1** | ENERGIE_GENERALE | 199 | 237 |
| **L2C2** | ENERGIE_CLIM | 109 | 180 |
| **L2C3** | ENERGIE_ECLAIRAGE | 85 | 79 |
| **L3C1** | ECLAIRAGE | 46 | 85 |
| **L3C2** | PRISES | 24 | 22 |
| **L3C3** | STORES | 18 | 53 |
| **L4C1** | MINI_PC | 28 | 99 |
| **L4C2** | PROXMOX | 69 | 115 |
| **L4C3** | MAJ_HA | 7 | 102 |
| **L5C1** | PILES_BATTERIES | 41 | 11 |
| **L5C2** | BATTERIES_PORTABLES | 49 | 35 |
| **L5C3** | MARIADB | 13 | 48 |
| **L6C1** | AIR_QUALITE | 15 | 30 |
| **L6C2** | POLLUTION_POLLEN | 19 | 32 |
| **L6C3** | VIGIEAU | 4 | 16 |

## SOMMAIRE

- 1. Vignettes dashboard, par carte
- 2. Scripts .sh
- 3. Automations par pole
- 4. Scripts non-sh
- 5. Entites orphelines
- 6. Statistiques

## 1. VIGNETTES DASHBOARD (L0C0 -> L6C3) - PAR CARTE

### L0C0 - PAGE_Home

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-06-13*

> Les 18 vignettes de la grille sont documentées dans leurs sections respectives (L1C1–L6C3). Cette section couvre **uniquement les cartes permanentes en haut de la HOME page** qui n'appartiennent à aucune vignette. Ces fichiers font partie intégrante de la config HA et sont audités par `audit_md5.sh`. Ils n'alimentent pas directement d'entités dashboard - référencés ici pour inventaire complet. *Ajouté le 2026-06-15* Configurée via : Paramètres → Appareils & Services → Ajouter → File Génère des services `notify.file_*` utilisés par les automations. ✅ **Note 2026-08-08** : ligne ci-dessus confirmée par Eric (2026-08-08). La phrase tronquée (coupure sur "docs_da") a été complétée par hypothèse le 2026-07-19 ; hypothèse validée - `docs_dashboard/` est bien l'ancien répertoire supprimé le 2026-07-14 tel que documenté dans CLAUDE.md.

*30 entites, 19 cartes, 9 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home`*

### Chaine de dependances

```
MATERIEL (NAT: 21)
  - NAT: (native/UI) (21)
TPL (TPL: 8)
  - TPL: templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml (1)
  - TPL: templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml (1)
  - TPL: templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml (1)
  - TPL: templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml (1)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml (1)
  - TPL: templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml (3)
SEN (SEN: 1)
  - SEN: sensors/Meteo/M_meteo_sensors_blitzortung.yaml (1)
  -> VIGNETTE L0C0
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | NAT | (native/UI) |
| `binary_sensor.porte_congel_contact` | NAT | (native/UI) |
| `device_tracker.mamour` | NAT | (native/UI) |
| `device_tracker.poco` | NAT | (native/UI) |
| `person.eric` | NAT | (native/UI) |
| `person.mamour` | NAT | (native/UI) |
| `sensor.06_weather_alert` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_meteo` | NAT | (native/UI) |
| `sensor.dernier_impact_temps_reel` | NAT | (native/UI) |
| `sensor.etat_wifi_maison` | NAT | (native/UI) |
| `sensor.lave_linge_etat` | NAT | (native/UI) |
| `sensor.lave_linge_progres` | NAT | (native/UI) |
| `sensor.lave_linge_temps_restant` | NAT | (native/UI) |
| `sensor.lave_vaisselle_etat` | NAT | (native/UI) |
| `sensor.lave_vaisselle_progres` | NAT | (native/UI) |
| `sensor.lave_vaisselle_temps_restant` | NAT | (native/UI) |
| `sensor.maison_lightning_azimuth` | TPL | templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml |
| `sensor.maison_lightning_counter` | TPL | templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml |
| `sensor.maison_lightning_distance` | SEN | sensors/Meteo/M_meteo_sensors_blitzortung.yaml |
| `sensor.maison_lightning_localisation` | NAT | (native/UI) |
| `sensor.prise_congelateur_cuisine_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_lave_linge_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_lave_vaisselle_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.studio_code_server_pourcentage_du_processeur` | NAT | (native/UI) |
| `sensor.th_balcon_nord_temperature` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml |
| `sensor.tongel_temperature` | NAT | (native/UI) |
| `sensor.vence_original_condition` | NAT | (native/UI) |
| `sun.sun` | NAT | (native/UI) |
| `switch.prise_congelateur_cuisine_nous` | NAT | (native/UI) |
| `weather.vence` | TPL | templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `sensors/Meteo/M_meteo_sensors_blitzortung.yaml` | `H:\sensors\Meteo\M_meteo_sensors_blitzortung.yaml` | identique |
| `templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml` | `H:\templates\Meteo\M_01_meteo_alerte\M_01_meteo_alertes_card.yaml` | identique |
| `templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml` | `H:\templates\Meteo\M_02_meteo_vent\M_02_meteo_direction_vent_vence_deg_card.yaml` | identique |
| `templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml` | `H:\templates\Meteo\M_03_meteo_orage_eclaires\M_03_meteo_direction_foudre_deg_card.yaml` | identique |
| `templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml` | `H:\templates\Meteo\M_03_meteo_orage_eclaires\M_03_meteo_timer_foudre_card.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_ext_temperature_card.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml` | `H:\templates\P0_energie_total_diag\P0_Total_pour_les_7_postes\P0_total_pour_les_7_postes.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/03_Carte météo/Card_meteocss_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/04_Studio code server/Card_vscode_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/05_Impacte de foudre/Card_foudre_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/06_Lave linge/Card_lave_linge_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/07_Lave vaisselle/Card_lave_vaisselle_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/08_Congélateur/Card_congelateur_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/09_Détecteur de fuite/Card_detecteur_fuite_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/10_Carte meteoalarm/Card_meteoalarm_home.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L0C0_PAGE_Home/11_Carte présence/Card_presence_home.yaml`

### L1C1 - METEO

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-09*

> La vignette `custom:button-card` est statique : icône `mdi:weather-partly-cloudy`, nom "Météo". Aucun `triggers_update`, aucun `custom_fields`, aucune entité référencée.
> ⚠️ Corrigé le 2026-07-19 : cette section décrivait des noms d'entités obsolètes/inexistants (`binary_sensor.meteo_france_alerte_*`, `sensor.meteo_france_wind_speed/_bearing`, `camera.carte_vigilance_meteo_france`, les 4 `*_card_content` génériques). Noms réels vérifiés directement dans le corps des fichiers yaml le 2026-07-19. `M_05_cycle_solaire.yaml` (absent de cette doc jusqu'ici) ajouté - c'est lui qui calcule la durée du jour, pas `sun.sun`. `templates/meteo/M_04_tendances_th_ext_card.yaml` retiré de cette liste le 2026-07-19 - son entête déclare lui-même `AVAL : L1C2 Températures`, pas L1C1. Voir section L1C2.

*49 entites, 120 cartes, 3 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L1C1_METEO`*

### Chaine de dependances

```
MATERIEL (NAT: 31)
  - NAT: (native/UI) (31)
TPL (TPL: 17)
  - TPL: templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml (10)
  - TPL: templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml (1)
  - TPL: templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml (1)
  - TPL: templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml (1)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml (1)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml (1)
  - TPL: templates/Meteo/M_05_meteo_cycle_solaire/M_05_meteo_duree_du_jour_card.yaml (1)
  - TPL: templates/Meteo/M_05_meteo_cycle_solaire/M_05_meteo_variation_quotidienne_card.yaml (1)
SEN (SEN: 1)
  - SEN: sensors/Meteo/M_meteo_sensors_blitzortung.yaml (1)
  -> VIGNETTE L1C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `camera.mf_alerte_today` | NAT | (native/UI) |
| `camera.mf_alerte_tomorrow` | NAT | (native/UI) |
| `date.get` | NAT | (native/UI) |
| `sensor.06_weather_alert` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_avalanches` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_canicule` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_grand_froid` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_inondation` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_meteo` | NAT | (native/UI) |
| `sensor.alerte_neige_verglas` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_orages` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_pluie_inondation` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_vagues_submersion` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.alerte_vent_violent` | TPL | templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml |
| `sensor.direction_foudre_deg` | NAT | (native/UI) |
| `sensor.direction_foudre_label` | NAT | (native/UI) |
| `sensor.direction_vent_vence_deg` | NAT | (native/UI) |
| `sensor.direction_vent_vence_label` | NAT | (native/UI) |
| `sensor.distance_foudre_km` | NAT | (native/UI) |
| `sensor.duree_du_jour` | NAT | (native/UI) |
| `sensor.duree_du_jour_brut` | NAT | (native/UI) |
| `sensor.eclair_annuel` | NAT | (native/UI) |
| `sensor.eclair_hebdomadaire` | NAT | (native/UI) |
| `sensor.eclair_horaire` | NAT | (native/UI) |
| `sensor.eclair_mensuel` | NAT | (native/UI) |
| `sensor.eclair_quotidien` | NAT | (native/UI) |
| `sensor.maison_lightning_azimuth` | TPL | templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml |
| `sensor.maison_lightning_counter` | TPL | templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml |
| `sensor.maison_lightning_distance` | SEN | sensors/Meteo/M_meteo_sensors_blitzortung.yaml |
| `sensor.maison_lightning_localisation` | NAT | (native/UI) |
| `sensor.moon_phase` | NAT | (native/UI) |
| `sensor.season` | NAT | (native/UI) |
| `sensor.sun_next_rising` | NAT | (native/UI) |
| `sensor.sun_next_setting` | NAT | (native/UI) |
| `sensor.tendance_duree_jour` | NAT | (native/UI) |
| `sensor.th_balcon_nord_humidity` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml |
| `sensor.th_balcon_nord_temperature` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml |
| `sensor.timer_foudre` | NAT | (native/UI) |
| `sensor.variation_quotidienne` | TPL | templates/Meteo/M_05_meteo_cycle_solaire/M_05_meteo_variation_quotidienne_card.yaml |
| `sensor.vence_daily_precipitation` | NAT | (native/UI) |
| `sensor.vence_original_condition` | NAT | (native/UI) |
| `sensor.vence_pressure` | NAT | (native/UI) |
| `sensor.vence_uv` | NAT | (native/UI) |
| `sensor.vence_wind_gust` | NAT | (native/UI) |
| `sensor.vence_wind_speed` | NAT | (native/UI) |
| `sensor.vitesse_vent_vence_kmh` | NAT | (native/UI) |
| `sun.sun` | NAT | (native/UI) |
| `weather.vence` | TPL | templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml |
| `zone.home` | TPL | templates/Meteo/M_05_meteo_cycle_solaire/M_05_meteo_duree_du_jour_card.yaml |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `sensors/Meteo/M_meteo_sensors_blitzortung.yaml` | `H:\sensors\Meteo\M_meteo_sensors_blitzortung.yaml` | identique |
| `templates/Meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml` | `H:\templates\Meteo\M_01_meteo_alerte\M_01_meteo_alertes_card.yaml` | identique |
| `templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml` | `H:\templates\Meteo\M_02_meteo_vent\M_02_meteo_direction_vent_vence_deg_card.yaml` | identique |
| `templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml` | `H:\templates\Meteo\M_03_meteo_orage_eclaires\M_03_meteo_direction_foudre_deg_card.yaml` | identique |
| `templates/Meteo/M_03_meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml` | `H:\templates\Meteo\M_03_meteo_orage_eclaires\M_03_meteo_timer_foudre_card.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_est_humidity_card.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_ext_temperature_card.yaml` | identique |
| `templates/Meteo/M_05_meteo_cycle_solaire/M_05_meteo_duree_du_jour_card.yaml` | `H:\templates\Meteo\M_05_meteo_cycle_solaire\M_05_meteo_duree_du_jour_card.yaml` | identique |
| `templates/Meteo/M_05_meteo_cycle_solaire/M_05_meteo_variation_quotidienne_card.yaml` | `H:\templates\Meteo\M_05_meteo_cycle_solaire\M_05_meteo_variation_quotidienne_card.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L1C1_METEO/Card_duree_du_jour.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C1_METEO/L1C1_METEO_01_Vignette/L1C1_Vignette_METEO.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C1_METEO/L1C1_METEO_02_Page/L1C1_Page_METEO.yaml`

### L1C2 - TEMPERATURES

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-13*

> ⚠️ **Corrigé le 2026-07-19** : `temperature_moyenne_interieure`, `temperature_delta_affichage`, `delta_ademe_recommande` étaient attribués à tort à `P1_ui_dashboard/P1_ui_dashboard.yaml` (ce fichier ne produit que des entités power_status/clim_*_etat - vérifié dans son propre corps, AVAL déclaré L1C3/L2C2, pas L1C2). Vrai fichier source : `P1_01_clim_logique_system_autom.yaml` (son AVAL déclare lui-même "L1C2 Températures" pour ces 4 sensors). Les entrées fictives `sensor.th_*_temperature_trend` / `_humidity_trend` (génériques, toutes pièces) ont été retirées - seule la sonde balcon nord a un calcul de tendance réel (`M_04_tendances_th_ext_card.yaml`, absent de cette section jusqu'ici - ajouté). `sensor.*_power_status` / `clim_*_etat` retirés d'ici - ce sont des entités Clim ON/OFF, déjà documentées dans la section L1C3 ci-dessous, pas des données de température.
> ⚠️ **Flag** : `custom:temperature-heatmap-card` utilisé dans le pop-up `#exterieur` - **absent du référentiel HACS officiel**. À vérifier / ajouter si installé.

*61 entites, 106 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L1C2_TEMPERATURES`*

### Chaine de dependances

```
MATERIEL (NAT: 37)
  - NAT: (native/UI) (23)
  - NAT: configuration.yaml (6)
  - NAT: groups/GRP_03_batteries_sonoff.yaml (8)
TPL (TPL: 18)
  - TPL: templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml (1)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml (1)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml (1)
  - TPL: templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml (6)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml (4)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml (1)
  - TPL: templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml (4)
SEN (SEN: 6)
  - SEN: sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml (6)
  -> VIGNETTE L1C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.porte_congel_contact` | NAT | (native/UI) |
| `climate.clim_bureau_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.clim_chambre_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.clim_salon_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.radiateur_cuisine` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.soufflant_salle_de_bain` | NAT | (native/UI) |
| `fan.includes` | NAT | (native/UI) |
| `sensor.bureau_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.chambre_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.clim_bureau_etat` | NAT | (native/UI) |
| `sensor.clim_bureau_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_chambre_etat` | NAT | (native/UI) |
| `sensor.clim_chambre_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_rad_total_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.clim_salon_etat` | NAT | (native/UI) |
| `sensor.clim_salon_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.conso_clim_rad_total` | NAT | (native/UI) |
| `sensor.conso_clim_rad_total_mensuel` | NAT | (native/UI) |
| `sensor.conso_clim_rad_total_quotidien` | NAT | (native/UI) |
| `sensor.cuisine_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.prise_congelateur_cuisine_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.radiateur_cuisine_etat` | NAT | (native/UI) |
| `sensor.radiateur_elec_cuisine_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.salon_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_seche_serviette_etat` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_seche_serviette_power_status` | NAT | (native/UI) |
| `sensor.sdb_soufflant_etat` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_soufflant_power_status` | NAT | (native/UI) |
| `sensor.temperature_delta_affichage` | NAT | (native/UI) |
| `sensor.temperature_moyenne_interieure` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_balcon_nord_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_balcon_nord_humidity` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml |
| `sensor.th_balcon_nord_humidity_trend` | NAT | (native/UI) |
| `sensor.th_balcon_nord_temperature` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml |
| `sensor.th_balcon_nord_temperature_trend` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.th_bureau_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_bureau_humidity` | NAT | configuration.yaml |
| `sensor.th_bureau_temperature` | NAT | configuration.yaml |
| `sensor.th_cellier_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_cellier_humidity` | NAT | (native/UI) |
| `sensor.th_cellier_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_chambre_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_chambre_humidity` | NAT | configuration.yaml |
| `sensor.th_chambre_temperature` | NAT | configuration.yaml |
| `sensor.th_cuisine_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_cuisine_humidity` | NAT | (native/UI) |
| `sensor.th_cuisine_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salle_de_bain_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_salle_de_bain_humidity` | NAT | (native/UI) |
| `sensor.th_salle_de_bain_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salon_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_salon_humidity` | NAT | configuration.yaml |
| `sensor.th_salon_temperature` | NAT | configuration.yaml |
| `sensor.tongel_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.tongel_humidity` | NAT | (native/UI) |
| `sensor.tongel_temperature` | NAT | (native/UI) |
| `sensor.vence_temperature` | NAT | (native/UI) |
| `switch.prise_congelateur_cuisine_nous` | NAT | (native/UI) |
| `switch.radiateur_elec_cuisine` | NAT | (native/UI) |
| `weather.vence` | TPL | templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `configuration.yaml` | `H:\configuration.yaml` | identique |
| `groups/GRP_03_batteries_sonoff.yaml` | `H:\groups\GRP_03_batteries_sonoff.yaml` | identique |
| `sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml` | `H:\sensors\P1_clim_chauffage\P1_DUT\P1_DUT_clim_chauffage.yaml` | identique |
| `templates/Meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml` | `H:\templates\Meteo\M_02_meteo_vent\M_02_meteo_direction_vent_vence_deg_card.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_est_humidity_card.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_ext_temperature_card.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml` | `H:\templates\P0_energie_total_diag\P0_Total_pour_les_7_postes\P0_total_pour_les_7_postes.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_01_clim_logique_system_autom.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_02_automation_message_clim_7h30_21h.yaml` | identique |
| `templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml` | `H:\templates\P1_clim_chauffage\P1_UI_DASHBOARD\P1_UI_DASHBOARD.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L1C2_TEMPERATURES/L1C2_TEMPERATURES_01_Vignette/L1C2_Vignette_TEMPERATURES.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C2_TEMPERATURES/L1C2_TEMPERATURES_02_Page/L1C2_Page_TEMPERATURES.yaml`

### L1C3 - CLIM

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-13 - chambre sur `climate.clim_chambre_rm4_mini` depuis le 2026-07-14*

> ⚠️ Corrigé le 2026-07-19 : `temperature_moyenne_interieure` attribué à tort à `P1_ui_dashboard.yaml` (ce fichier ne contient que des sensors power_status/*_etat, vérifié dans son corps) - vrai fichier source : `P1_01_clim_logique_system_autom.yaml`. `climate.soufflant_salle_de_bain` retiré - n'existe pas (le soufflant SDB est piloté via `switch.inter_soufflant_salle_de_bain` + `input_select.etat_resistance_soufflant_sdb`, pas une entité climate - vérifié, aucune occurrence dans tout `config_system_YAML/`). Appelé par A et B. Pilote les 3 clims (salon/bureau/chambre) jour/nuit selon parametre `periode`.

*93 entites, 222 cartes, 8 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM`*

### Chaine de dependances

```
MATERIEL (NAT: 52)
  - NAT: (native/UI) (46)
  - NAT: configuration.yaml (6)
TPL (TPL: 35)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml (1)
  - TPL: templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml (5)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml (14)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml (10)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_03_automation_message_clim_21h_7h30.yaml (1)
  - TPL: templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml (4)
SEN (SEN: 6)
  - SEN: sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml (6)
  -> VIGNETTE L1C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.est_jour_7h30_21h` | NAT | (native/UI) |
| `binary_sensor.est_nuit_21h_7h30` | NAT | (native/UI) |
| `climate.clim_bureau_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.clim_chambre_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.clim_salon_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.radiateur_cuisine` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.soufflant_salle_de_bain` | NAT | (native/UI) |
| `climate.turn_off` | NAT | (native/UI) |
| `input_boolean.clim_bureau_arret_securise_en_cours` | NAT | (native/UI) |
| `input_boolean.clim_chambre_arret_securise_en_cours` | NAT | (native/UI) |
| `input_boolean.clim_salon_arret_securise_en_cours` | NAT | (native/UI) |
| `input_select.etat_resistance_soufflant_sdb` | NAT | (native/UI) |
| `person.eric` | NAT | (native/UI) |
| `remote.clim_bureau` | NAT | configuration.yaml |
| `remote.clim_chambre` | NAT | configuration.yaml |
| `remote.clim_salon` | NAT | configuration.yaml |
| `remote.soufflant_sdb` | NAT | (native/UI) |
| `script.j_1_1_salon_clim_on_off_intelligent` | NAT | (native/UI) |
| `script.j_1_2_bureau_clim_on_off_intelligent` | NAT | (native/UI) |
| `script.j_1_3_chambre_clim_on_off_intelligent` | NAT | (native/UI) |
| `sensor.bureau_power_lock` | NAT | (native/UI) |
| `sensor.bureau_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.bureau_power_status_affichage` | NAT | (native/UI) |
| `sensor.chambre_power_lock` | NAT | (native/UI) |
| `sensor.chambre_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.chambre_power_status_affichage` | NAT | (native/UI) |
| `sensor.clim_bureau_etat` | NAT | (native/UI) |
| `sensor.clim_bureau_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_chambre_etat` | NAT | (native/UI) |
| `sensor.clim_chambre_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_salon_etat` | NAT | (native/UI) |
| `sensor.clim_salon_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.consigne_de_base` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.conso_clim_rad_total` | NAT | (native/UI) |
| `sensor.cuisine_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.cuisine_power_status_affichage` | NAT | (native/UI) |
| `sensor.delta_1` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.delta_2` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.delta_5` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.delta_7` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.delta_ademe_recommande` | NAT | (native/UI) |
| `sensor.groupe` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.mode_ete_hiver` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.mode_ete_hiver_etat` | NAT | (native/UI) |
| `sensor.presence` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.radiateur_cuisine_etat` | NAT | (native/UI) |
| `sensor.radiateur_elec_cuisine_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.salon_power_lock` | NAT | (native/UI) |
| `sensor.salon_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.salon_power_status_affichage` | NAT | (native/UI) |
| `sensor.sdb_power_status_affichage` | NAT | (native/UI) |
| `sensor.sdb_seche_serviette_etat` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_seche_serviette_power_status` | NAT | (native/UI) |
| `sensor.sdb_seche_serviette_power_status_affichage` | NAT | (native/UI) |
| `sensor.sdb_soufflant_etat` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_soufflant_power_status` | NAT | (native/UI) |
| `sensor.temperature_cible` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_confort_jour` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_confort_nuit` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_03_automation_message_clim_21h_7h30.yaml |
| `sensor.temperature_corrige_chambre` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.temperature_corrige_bureau` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.temperature_corrige_salon` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.temperature_delta_affichage` | NAT | (native/UI) |
| `sensor.temperature_differentielle` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_eco_ete` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_eco_ete_corrige` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.temperature_eco_hiver` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.temperature_eco_hiver_corrige` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.temperature_hors_gel_hiver` | NAT | (native/UI) |
| `sensor.temperature_moyenne_interieure` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_balcon_nord_temperature` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml |
| `sensor.th_bureau_temperature` | NAT | configuration.yaml |
| `sensor.th_chambre_temperature` | NAT | configuration.yaml |
| `sensor.th_cuisine_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salle_de_bain_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salon_temperature` | NAT | configuration.yaml |
| `switch.clim_bureau_nous` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `switch.clim_chambre_nous` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `switch.clim_salon_nous` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `switch.inter_soufflant_salle_de_bain` | NAT | (native/UI) |
| `switch.prise_soufflant_salle_de_bain_nous` | NAT | (native/UI) |
| `switch.radiateur_elec_cuisine` | NAT | (native/UI) |
| `switch.schedule_clim_de_la_chambre_week` | NAT | (native/UI) |
| `switch.schedule_clim_de_la_chambre_week_end` | NAT | (native/UI) |
| `switch.schedule_clim_du_bureau_week` | NAT | (native/UI) |
| `switch.schedule_clim_du_bureau_week_end` | NAT | (native/UI) |
| `switch.schedule_clim_du_salon_week` | NAT | (native/UI) |
| `switch.schedule_clim_du_salon_week_end` | NAT | (native/UI) |
| `switch.schedule_radiateur_cuisine_week` | NAT | (native/UI) |
| `switch.schedule_radiateur_cuisine_week_end` | NAT | (native/UI) |
| `switch.schedule_soufflant_salle_de_bain_week` | NAT | (native/UI) |
| `switch.schedule_soufflant_salle_de_bain_week_end` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `configuration.yaml` | `H:\configuration.yaml` | identique |
| `sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml` | `H:\sensors\P1_clim_chauffage\P1_DUT\P1_DUT_clim_chauffage.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_ext_temperature_card.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml` | `H:\templates\P0_energie_total_diag\P0_Total_pour_les_7_postes\P0_total_pour_les_7_postes.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_01_clim_logique_system_autom.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_02_automation_message_clim_7h30_21h.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_03_automation_message_clim_21h_7h30.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_03_automation_message_clim_21h_7h30.yaml` | identique |
| `templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml` | `H:\templates\P1_clim_chauffage\P1_UI_DASHBOARD\P1_UI_DASHBOARD.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/Card_calcule_temp_cible.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/Card_prog_clim_bureau.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/Card_prog_clim_chambre.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/Card_prog_clim_salon.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/Card_prog_radiateur_cuisine.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/Card_prog_soufflant_SDB.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/L1C3_CLIM_01_Vignette/L1C3_Vignette_CLIM.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L1C3_CLIM/L1C3_CLIM_02_Page/L1C3_Page_CLIM.yaml`

### L2C1 - ENERGIE_GENERALE

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

> **Source énergie générale (depuis 2026-06-17) : Nodon SEM-4-1-00** (pince ampèremétrique Z2M) - `sensor.general_electric_appart_energy` (kWh) → source des UM P0 - `sensor.general_electric_appart_power` (W) → puissance temps réel **Linky (MyElectricalData)** = J-1 uniquement (HP/HC historique) - source secondaire
> ⚠️ Corrigé le 2026-07-19 : le diagramme référençait un fichier `total_par_poste_7.yaml` qui n'existe pas - les vrais noms sont `P0_diag_conso_{jour,hebdomadaire,mois}_en_cours.yaml` (3 fichiers distincts pour `diag_poste_*`) et `P0_total_pour_les_7_postes.yaml` (pour `total_poste_*_puissance`), vérifiés par grep des `unique_id:` réels.

*199 entites, 237 cartes, 4 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L2C1_ENERGIE_GENERALE`*

### Chaine de dependances

```
MATERIEL (NAT: 89)
  - NAT: (native/UI) (89)
TPL (TPL: 108)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml (7)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml (25)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml (25)
  - TPL: templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml (6)
  - TPL: templates/P0_energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml (3)
  - TPL: templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml (2)
  - TPL: templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml (25)
  - TPL: templates/P2_prise/P2_congelateur/P2_congelateur_compresseur_actif.yaml (1)
  - TPL: templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml (14)
SEN (SEN: 1)
  - SEN: sensors/P0_energie_total_min_maxi_diag/P0_genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_genelec_appart.yaml (1)
UM (UM: 1)
  - UM: utility_meter/P0_energie_total/Genelec_appart/P0_UM_AMHQ.yaml (1)
  -> VIGNETTE L2C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.airfryer_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.airfryer_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.all_standby_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.all_standby_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.all_standby_current` | NAT | (native/UI) |
| `sensor.all_standby_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.all_standby_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.all_standby_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.box_internet_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.box_internet_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.chargeurs_salon_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.chargeurs_salon_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.clim_bureau_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_chambre_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_salon_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.congelateur_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.congelateur_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.diag_max_poste_hebdomadaire_dynamique` | NAT | (native/UI) |
| `sensor.diag_max_poste_mensuel_dynamique` | NAT | (native/UI) |
| `sensor.diag_max_poste_quotidien_dynamique` | NAT | (native/UI) |
| `sensor.diag_poste_autre_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_autre_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_autre_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_chauffage_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_chauffage_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_chauffage_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_cuisine_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_cuisine_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_cuisine_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_eclairage_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_eclairage_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_eclairage_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_froid_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_froid_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_froid_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_hygiene_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_hygiene_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_hygiene_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.diag_poste_multimedia_hebdomadaire` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.diag_poste_multimedia_mensuel` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.diag_poste_multimedia_quotidien` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.eclairage_total_group_puissance_tpl` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.fer_repasser_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.fer_repasser_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.four_et_plaque_de_cuisson_current` | NAT | (native/UI) |
| `sensor.four_et_plaque_de_cuisson_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.four_et_plaque_de_cuisson_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.four_et_plaque_de_cuisson_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.four_mo_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.four_mo_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.frigo_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.frigo_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.genelec_appart_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.genelec_appart_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.genelec_appart_conso_maxi_24h` | NAT | (native/UI) |
| `sensor.genelec_appart_conso_mini_24h` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_hc_hebdomadaire` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_hc_mensuel` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_hc_quotidien` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_hp_hebdomadaire` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_hp_mensuel` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_hp_quotidien` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_total_hebdomadaire` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_total_mensuel` | NAT | (native/UI) |
| `sensor.genelec_appart_cout_total_quotidien` | NAT | (native/UI) |
| `sensor.genelec_appart_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml |
| `sensor.genelec_appart_hphc_hebdomadaire_um_hc` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_hphc_hebdomadaire_um_hp` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_hphc_mensuel_um_hc` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_hphc_mensuel_um_hp` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_hphc_quotidien_um_hc` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_hphc_quotidien_um_hp` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml |
| `sensor.genelec_appart_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml |
| `sensor.genelec_appart_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml |
| `sensor.genelec_appart_ratio_hc_hebdomadaire` | NAT | (native/UI) |
| `sensor.genelec_appart_ratio_hc_mensuel` | NAT | (native/UI) |
| `sensor.genelec_appart_ratio_hc_quotidien` | NAT | (native/UI) |
| `sensor.general_electric_appart_energy` | UM | utility_meter/P0_energie_total/Genelec_appart/P0_UM_AMHQ.yaml |
| `sensor.general_electric_appart_power` | SEN | sensors/P0_energie_total_min_maxi_diag/P0_genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_genelec_appart.yaml |
| `sensor.histo_energie_linky` | NAT | (native/UI) |
| `sensor.histo_energie_nodon` | TPL | templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml |
| `sensor.horloge_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.horloge_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.hue_ambiance_lamp_salon_` | NAT | (native/UI) |
| `sensor.hue_color_candle_chambre_eric_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_color_candle_chambre_gege_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_color_candle_salon_1_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_play_1_pc_bureau_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_play_2_pc_bureau_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_play_3_pc_bureau_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_bureau_1_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_bureau_2_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_chambre_` | NAT | (native/UI) |
| `sensor.hue_white_lamp_couloir_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_cuisine_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_entree_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_salle_de_bain_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.hue_white_lamp_table_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.lave_linge_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.lave_linge_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.lave_vaisselle_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.lave_vaisselle_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.linky_25481620821301_consumption` | TPL | templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml |
| `sensor.linky_jour_0` | NAT | (native/UI) |
| `sensor.linky_jour_1` | NAT | (native/UI) |
| `sensor.linky_jour_2` | NAT | (native/UI) |
| `sensor.linky_jour_3` | NAT | (native/UI) |
| `sensor.linky_jour_4` | NAT | (native/UI) |
| `sensor.linky_jour_5` | NAT | (native/UI) |
| `sensor.linky_jour_6` | NAT | (native/UI) |
| `sensor.linky_jour_7` | NAT | (native/UI) |
| `sensor.pc_bureau_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.pc_bureau_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.pc_gege_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.pc_gege_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.petit_dej_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.petit_dej_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.plaques_cuisson_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.plaques_cuisson_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.prise_airfryer_ninja_nous_current` | NAT | (native/UI) |
| `sensor.prise_airfryer_ninja_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_airfryer_ninja_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_airfryer_ninja_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_box_internet_ikea_current` | NAT | (native/UI) |
| `sensor.prise_box_internet_ikea_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_box_internet_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_box_internet_ikea_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_bureau_fer_a_repasser_nous_current` | NAT | (native/UI) |
| `sensor.prise_bureau_fer_a_repasser_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_bureau_fer_a_repasser_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_bureau_fer_a_repasser_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_bureau_pc_ikea_current` | NAT | (native/UI) |
| `sensor.prise_bureau_pc_ikea_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_bureau_pc_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_bureau_pc_ikea_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_congelateur_cuisine_nous_current` | TPL | templates/P2_prise/P2_congelateur/P2_congelateur_compresseur_actif.yaml |
| `sensor.prise_congelateur_cuisine_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_congelateur_cuisine_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_congelateur_cuisine_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_four_micro_ondes_nous_current` | NAT | (native/UI) |
| `sensor.prise_four_micro_ondes_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_four_micro_ondes_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_four_micro_ondes_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_frigo_cuisine_nous_current` | NAT | (native/UI) |
| `sensor.prise_frigo_cuisine_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_frigo_cuisine_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_frigo_cuisine_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_horloge_ikea_current` | NAT | (native/UI) |
| `sensor.prise_horloge_ikea_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_horloge_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_horloge_ikea_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_lave_linge_nous_current` | NAT | (native/UI) |
| `sensor.prise_lave_linge_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_lave_linge_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_lave_linge_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_lave_vaisselle_nous_current` | NAT | (native/UI) |
| `sensor.prise_lave_vaisselle_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_lave_vaisselle_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_lave_vaisselle_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_pc_s_gege_ikea_current` | NAT | (native/UI) |
| `sensor.prise_pc_s_gege_ikea_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_pc_s_gege_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_pc_s_gege_ikea_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_petit_dejeune_nous_current` | NAT | (native/UI) |
| `sensor.prise_petit_dejeune_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_petit_dejeune_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_petit_dejeune_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_salon_chargeur_nous_current` | NAT | (native/UI) |
| `sensor.prise_salon_chargeur_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_salon_chargeur_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_salon_chargeur_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tete_de_lit_chambre_current` | NAT | (native/UI) |
| `sensor.prise_tete_de_lit_chambre_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_tete_de_lit_chambre_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tete_de_lit_chambre_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_tv_chambre_nous_current` | NAT | (native/UI) |
| `sensor.prise_tv_chambre_nous_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_tv_chambre_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tv_chambre_nous_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.prise_tv_salon_ikea_current` | NAT | (native/UI) |
| `sensor.prise_tv_salon_ikea_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.prise_tv_salon_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tv_salon_ikea_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.radiateur_elec_cuisine_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.relais_lumiere_sdb_sonoff_power` | TPL | templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml |
| `sensor.tetes_lit_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.tetes_lit_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.total_poste_autre_puissance` | NAT | (native/UI) |
| `sensor.total_poste_chauffage_puissance` | NAT | (native/UI) |
| `sensor.total_poste_cuisine_puissance` | NAT | (native/UI) |
| `sensor.total_poste_froid_puissance` | NAT | (native/UI) |
| `sensor.total_poste_hygiene_puissance` | NAT | (native/UI) |
| `sensor.total_poste_multimedia_puissance` | NAT | (native/UI) |
| `sensor.tv_chambre_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.tv_chambre_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.tv_salon_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.tv_salon_avg_watts_quotidien` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `sensors/P0_energie_total_min_maxi_diag/P0_genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_genelec_appart.yaml` | `H:\sensors\P0_energie_total_min_maxi_diag\P0_genelec_appart_mini_maxi\P0_MINI_MAXI_AVG_genelec_appart.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_hebdomadaire_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_jour_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_mois_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml` | `H:\templates\P0_energie_total_diag\P0_Genelec_appart\P0_01_genelec_appart_AMHQ_cost.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml` | `H:\templates\P0_energie_total_diag\P0_Genelec_appart\P0_03_AVG_genelec_appart.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml` | `H:\templates\P0_energie_total_diag\P0_Linky\P0_MyElectricalData.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml` | `H:\templates\P0_energie_total_diag\P0_Total_pour_les_7_postes\P0_total_pour_les_7_postes.yaml` | identique |
| `templates/P2_prise/P2_congelateur/P2_congelateur_compresseur_actif.yaml` | `H:\templates\P2_prise\P2_congelateur\P2_congelateur_compresseur_actif.yaml` | identique |
| `templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml` | `H:\templates\P3_eclairage\P3_POWER_TPL\P3_POWER_3_TOTAL_ZONE.yaml` | identique |
| `utility_meter/P0_energie_total/Genelec_appart/P0_UM_AMHQ.yaml` | `H:\utility_meter\P0_energie_total\Genelec_appart\P0_UM_AMHQ.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L2C1_ENERGIE_GENERALE/L2C1_ENERGIE_GENERALE_01_Vignette/L2C1_Vignette_ENERGIE_GENERALE.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L2C1_ENERGIE_GENERALE/L2C1_ENERGIE_GENERALE_02_Page_temps_reel/L2C1_Page_ENERGIE_GENERALE_temps_reel.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L2C1_ENERGIE_GENERALE/L2C1_ENERGIE_GENERALE_03_Page_principale/L2C1_Page_ENERGIE_GENERALE_principale.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L2C1_ENERGIE_GENERALE/L2C1_ENERGIE_GENERALE_04_Page_mensuel/L2C1_Page_ENERGIE_GENERALE_mensuel.yaml`

### L2C2 - ENERGIE_CLIM

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-13*

*109 entites, 180 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L2C2_ENERGIE_CLIM`*

### Chaine de dependances

```
MATERIEL (NAT: 46)
  - NAT: (native/UI) (40)
  - NAT: configuration.yaml (6)
TPL (TPL: 51)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml (1)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml (6)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml (6)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml (6)
  - TPL: templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml (6)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml (3)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml (1)
  - TPL: templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml (12)
  - TPL: templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml (6)
  - TPL: templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml (4)
SEN (SEN: 6)
  - SEN: sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml (6)
UM (UM: 6)
  - UM: utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml (6)
  -> VIGNETTE L2C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `climate.clim_bureau_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.clim_chambre_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.clim_salon_rm4_mini` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.radiateur_cuisine` | TPL | templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml |
| `climate.soufflant_salle_de_bain` | NAT | (native/UI) |
| `fan.includes` | NAT | (native/UI) |
| `sensor.bureau_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.bureau_power_status_affichage` | NAT | (native/UI) |
| `sensor.chambre_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.chambre_power_status_affichage` | NAT | (native/UI) |
| `sensor.clim_bureau_annuel_um` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml |
| `sensor.clim_bureau_avg_watts_mensuel` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_bureau_avg_watts_quotidien` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_bureau_etat` | NAT | (native/UI) |
| `sensor.clim_bureau_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.clim_bureau_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.clim_bureau_nous_current` | NAT | (native/UI) |
| `sensor.clim_bureau_nous_energy` | UM | utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml |
| `sensor.clim_bureau_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_bureau_nous_voltage` | NAT | (native/UI) |
| `sensor.clim_bureau_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.clim_chambre_annuel_um` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml |
| `sensor.clim_chambre_avg_watts_mensuel` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_chambre_avg_watts_quotidien` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_chambre_etat` | NAT | (native/UI) |
| `sensor.clim_chambre_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.clim_chambre_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.clim_chambre_nous_current` | NAT | (native/UI) |
| `sensor.clim_chambre_nous_energy` | UM | utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml |
| `sensor.clim_chambre_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_chambre_nous_voltage` | NAT | (native/UI) |
| `sensor.clim_chambre_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.clim_rad_total_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.clim_salon_annuel_um` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml |
| `sensor.clim_salon_avg_watts_mensuel` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_salon_avg_watts_quotidien` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.clim_salon_etat` | NAT | (native/UI) |
| `sensor.clim_salon_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.clim_salon_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.clim_salon_nous_current` | NAT | (native/UI) |
| `sensor.clim_salon_nous_energy` | UM | utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml |
| `sensor.clim_salon_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.clim_salon_nous_voltage` | NAT | (native/UI) |
| `sensor.clim_salon_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.conso_clim_rad_total` | NAT | (native/UI) |
| `sensor.conso_clim_rad_total_mensuel` | NAT | (native/UI) |
| `sensor.conso_clim_rad_total_quotidien` | NAT | (native/UI) |
| `sensor.cuisine_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.cuisine_power_status_affichage` | NAT | (native/UI) |
| `sensor.dut_clim_bureau` | NAT | (native/UI) |
| `sensor.dut_clim_chambre` | NAT | (native/UI) |
| `sensor.dut_clim_salon` | NAT | (native/UI) |
| `sensor.dut_radiateur_cuisine` | NAT | (native/UI) |
| `sensor.dut_sdb_total` | NAT | (native/UI) |
| `sensor.ete_hiver` | NAT | (native/UI) |
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | NAT | (native/UI) |
| `sensor.prise_seche_serviette_salle_de_bain_nous_current` | NAT | (native/UI) |
| `sensor.prise_seche_serviette_salle_de_bain_nous_energy` | UM | utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml |
| `sensor.prise_seche_serviette_salle_de_bain_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_seche_serviette_salle_de_bain_nous_voltage` | NAT | (native/UI) |
| `sensor.prise_soufflant_salle_de_bain_nous_current` | NAT | (native/UI) |
| `sensor.prise_soufflant_salle_de_bain_nous_energy` | UM | utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml |
| `sensor.prise_soufflant_salle_de_bain_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_soufflant_salle_de_bain_nous_voltage` | NAT | (native/UI) |
| `sensor.radiateur_cuisine_etat` | NAT | (native/UI) |
| `sensor.radiateur_elec_cuisine_annuel_um` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml |
| `sensor.radiateur_elec_cuisine_avg_watts_mensuel` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.radiateur_elec_cuisine_avg_watts_quotidien` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.radiateur_elec_cuisine_current` | NAT | (native/UI) |
| `sensor.radiateur_elec_cuisine_energy` | UM | utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml |
| `sensor.radiateur_elec_cuisine_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.radiateur_elec_cuisine_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.radiateur_elec_cuisine_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.radiateur_elec_cuisine_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.radiateur_elec_cuisine_voltage` | NAT | (native/UI) |
| `sensor.salon_power_status` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.salon_power_status_affichage` | NAT | (native/UI) |
| `sensor.sdb_power_status_affichage` | NAT | (native/UI) |
| `sensor.sdb_seche_serviette_etat` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_seche_serviette_power_status` | NAT | (native/UI) |
| `sensor.sdb_seche_serviette_power_status_affichage` | NAT | (native/UI) |
| `sensor.sdb_soufflant_etat` | SEN | sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml |
| `sensor.sdb_soufflant_power_status` | NAT | (native/UI) |
| `sensor.seche_serviette_sdb_annuel_um` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml |
| `sensor.seche_serviette_sdb_avg_watts_mensuel` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.seche_serviette_sdb_avg_watts_quotidien` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.seche_serviette_sdb_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.seche_serviette_sdb_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.seche_serviette_sdb_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.soufflant_sdb_annuel_um` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml |
| `sensor.soufflant_sdb_avg_watts_mensuel` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.soufflant_sdb_avg_watts_quotidien` | TPL | templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml |
| `sensor.soufflant_sdb_hebdomadaire_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml |
| `sensor.soufflant_sdb_mensuel_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.soufflant_sdb_quotidien_um` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.temperature_delta_affichage` | NAT | (native/UI) |
| `sensor.temperature_moyenne_interieure` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_balcon_nord_temperature` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml |
| `sensor.th_balcon_nord_temperature_trend` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.th_bureau_humidity` | NAT | configuration.yaml |
| `sensor.th_bureau_temperature` | NAT | configuration.yaml |
| `sensor.th_chambre_humidity` | NAT | configuration.yaml |
| `sensor.th_chambre_temperature` | NAT | configuration.yaml |
| `sensor.th_cuisine_humidity` | NAT | (native/UI) |
| `sensor.th_cuisine_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salle_de_bain_humidity` | NAT | (native/UI) |
| `sensor.th_salle_de_bain_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salon_humidity` | NAT | configuration.yaml |
| `sensor.th_salon_temperature` | NAT | configuration.yaml |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `configuration.yaml` | `H:\configuration.yaml` | identique |
| `sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml` | `H:\sensors\P1_clim_chauffage\P1_DUT\P1_DUT_clim_chauffage.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_ext_temperature_card.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_hebdomadaire_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_jour_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_mois_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml` | `H:\templates\P0_energie_total_diag\P0_Total_pour_les_7_postes\P0_total_pour_les_7_postes.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_01_clim_logique_system_autom.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_02_automation_message_clim_7h30_21h.yaml` | identique |
| `templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml` | `H:\templates\P1_clim_chauffage\P1_AVG\P1_AVG_AMHQ_TOTAL.yaml` | identique |
| `templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml` | `H:\templates\P1_clim_chauffage\P1_AVG\P1_AVG_AMHQ_UNITE.yaml` | identique |
| `templates/P1_clim_chauffage/P1_UI_DASHBOARD/P1_UI_DASHBOARD.yaml` | `H:\templates\P1_clim_chauffage\P1_UI_DASHBOARD\P1_UI_DASHBOARD.yaml` | identique |
| `utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml` | `H:\utility_meter\P1_clim_chauffage\P1_UM_AMHQ.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L2C2_ENERGIE_CLIM/L2C2_ENERGIE_CLIM_01_Vignette/L2C2_Vignette_ENERGIE_CLIM.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L2C2_ENERGIE_CLIM/L2C2_ENERGIE_CLIM_02_Page/L2C2_Page_ENERGIE_CLIM.yaml`

### L2C3 - ENERGIE_ECLAIRAGE

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-04-29 - Migration TPL kWh complète (_um → _um_kwh_tpl) | Dashboard archivé le 2026-05-13 | 2026-06-14 state_class total_increasing → total (× 116 sensors)*

> Somme des 19 `{slug}_power` (PowerCalc). Consommé par `total_pour_les_7_postes.yaml` (Pôle 6) → L2C1.

*85 entites, 79 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L2C3_ENERGIE_ECLAIRAGE`*

### Chaine de dependances

```
MATERIEL (NAT: 37)
  - NAT: (native/UI) (37)
TPL (TPL: 48)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml (1)
  - TPL: templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml (1)
  - TPL: templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml (38)
  - TPL: templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml (8)
  -> VIGNETTE L2C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `light.bureau` | NAT | (native/UI) |
| `light.chambre` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.couloir` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.cuisine` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.entree` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_white_lamp_salle_de_bain` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.lit` | NAT | (native/UI) |
| `light.salon` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.table` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `sensor.eclairage_appart_2_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_appart_2_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_appart_3_annuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_appart_3_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.eclairage_appart_3_hebdomadaire_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_appart_3_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_appart_3_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_bureau_5_annuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_bureau_5_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.eclairage_bureau_5_hebdomadaire_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_chambre_4_annuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_chambre_4_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.eclairage_chambre_4_hebdomadaire_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_salon_5_annuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_salon_5_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.eclairage_salon_5_hebdomadaire_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_salon_5_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_salon_5_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_sdb_2_annuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_sdb_2_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.eclairage_sdb_2_hebdomadaire_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl` | NAT | (native/UI) |
| `sensor.eclairage_total_unit_mensuel_kwh_tpl` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml |
| `sensor.eclairage_total_unit_quotidien_kwh_tpl` | TPL | templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml |
| `sensor.hue_ambiance_lamp_salon_1_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_ambiance_lamp_salon_1_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_ambiance_lamp_salon_2_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_ambiance_lamp_salon_2_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_ambiance_lamp_salon_3_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_ambiance_lamp_salon_3_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_color_candle_chambre_eric_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_color_candle_chambre_eric_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_color_candle_chambre_gege_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_color_candle_chambre_gege_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_color_candle_salon_1_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_color_candle_salon_1_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_play_1_pc_bureau_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_play_1_pc_bureau_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_play_2_pc_bureau_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_play_2_pc_bureau_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_play_3_pc_bureau_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_play_3_pc_bureau_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_bureau_1_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_bureau_1_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_bureau_2_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_bureau_2_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_chambre_1_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_chambre_1_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_chambre_2_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_chambre_2_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_couloir_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_couloir_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_cuisine_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_cuisine_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_entree_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_entree_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_salle_de_bain_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_salle_de_bain_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_table_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.hue_white_lamp_table_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.lumiere_appartement_etat` | NAT | (native/UI) |
| `sensor.lumiere_bureau_etat` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `sensor.lumiere_chambre_etat` | NAT | (native/UI) |
| `sensor.lumiere_cuisine_etat` | NAT | (native/UI) |
| `sensor.lumiere_salle_de_bain_etat` | NAT | (native/UI) |
| `sensor.lumiere_salon_etat` | NAT | (native/UI) |
| `sensor.relais_lumiere_sdb_sonoff_mensuel_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `sensor.relais_lumiere_sdb_sonoff_quotidien_um_kwh_tpl` | TPL | templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml |
| `switch.relais_lumiere_sdb_sonoff` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_jour_en_cours.yaml` | identique |
| `templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml` | `H:\templates\P0_energie_total_diag\P0_Diag\P0_diag_conso_mois_en_cours.yaml` | identique |
| `templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml` | `H:\templates\P3_eclairage\P3_AVG\P3_AVG_AMHQ_1_UNITE.yaml` | identique |
| `templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml` | `H:\templates\P3_eclairage\P3_UI_DASHBOARD\P3_etats_status.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L2C3_ENERGIE_ECLAIRAGE/L2C3_ENERGIE_ECLAIRAGE_01_Vignette/L2C3_Vignette_ENERGIE_ECLAIRAGE.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L2C3_ENERGIE_ECLAIRAGE/L2C3_ENERGIE_ECLAIRAGE_02_Page/L2C3_Page_ENERGIE_ECLAIRAGE.yaml`

### L3C1 - ECLAIRAGE

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-04 | Dashboard archivé le 2026-05-13*

*46 entites, 85 cartes, 3 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L3C1_ECLAIRAGE`*

### Chaine de dependances

```
MATERIEL (NAT: 23)
  - NAT: (native/UI) (20)
  - NAT: configuration.yaml (3)
TPL (TPL: 23)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml (2)
  - TPL: templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml (2)
  - TPL: templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml (17)
  - TPL: templates/Stores/S_01_store.yaml (2)
  -> VIGNETTE L3C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `cover.store_bureau` | TPL | templates/Stores/S_01_store.yaml |
| `cover.store_salon` | TPL | templates/Stores/S_01_store.yaml |
| `light.bureau` | NAT | (native/UI) |
| `light.chambre` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.couloir` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.cuisine` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.entree` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_color_candle_chambre_eric` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_color_candle_chambre_gege` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_play_1_pc_bureau` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_play_2_pc_bureau` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_play_3_pc_bureau` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_white_lamp_bureau_1` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_white_lamp_bureau_2` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.hue_white_lamp_salle_de_bain` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.lit` | NAT | (native/UI) |
| `light.moniteur_pc` | NAT | (native/UI) |
| `light.salon` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.table` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `light.toggle` | NAT | (native/UI) |
| `light.turn_on` | NAT | (native/UI) |
| `light.zone_eric` | NAT | (native/UI) |
| `light.zone_gege` | NAT | (native/UI) |
| `sensor.bureau_etat` | NAT | (native/UI) |
| `sensor.chambre_etat` | NAT | (native/UI) |
| `sensor.chambre_nb_allumes` | NAT | (native/UI) |
| `sensor.lumiere_appartement_etat` | NAT | (native/UI) |
| `sensor.lumiere_bureau_etat` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `sensor.lumiere_chambre_etat` | NAT | (native/UI) |
| `sensor.lumiere_couloir_etat` | NAT | (native/UI) |
| `sensor.lumiere_cuisine_etat` | NAT | (native/UI) |
| `sensor.lumiere_ecran_etat` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `sensor.lumiere_entree_etat` | NAT | (native/UI) |
| `sensor.lumiere_salle_de_bain_etat` | NAT | (native/UI) |
| `sensor.lumiere_salon_etat` | NAT | (native/UI) |
| `sensor.lumiere_table_etat` | NAT | (native/UI) |
| `sensor.lumiere_tete_de_lit_etat` | TPL | templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml |
| `sensor.plug_power` | NAT | (native/UI) |
| `sensor.th_bureau_temperature` | NAT | configuration.yaml |
| `sensor.th_chambre_temperature` | NAT | configuration.yaml |
| `sensor.th_cuisine_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salle_de_bain_temperature` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml |
| `sensor.th_salon_temperature` | NAT | configuration.yaml |
| `switch.ecran_p_c_3_play_hue` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `switch.prise_tete_de_lit_chambre` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `switch.relais_lumiere_sdb_sonoff` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `configuration.yaml` | `H:\configuration.yaml` | identique |
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_01_clim_logique_system_autom.yaml` | identique |
| `templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml` | `H:\templates\P2_prise\P2_eCO_prises\P2_eCO_prises_config.yaml` | identique |
| `templates/P3_eclairage/P3_UI_DASHBOARD/P3_etats_status.yaml` | `H:\templates\P3_eclairage\P3_UI_DASHBOARD\P3_etats_status.yaml` | identique |
| `templates/Stores/S_01_store.yaml` | `H:\templates\Stores\S_01_store.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L3C1_ECLAIRAGE/L3C1_ECLAIRAGE_01_Vignette/L3C1_Vignette_ECLAIRAGE.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L3C1_ECLAIRAGE/L3C1_ECLAIRAGE_02_Page_gauche/L3C1_Page_ECLAIRAGE_gauche.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L3C1_ECLAIRAGE/L3C1_ECLAIRAGE_03_Page_droite/L3C1_Page_ECLAIRAGE_droite.yaml`

### L3C2 - PRISES

*24 entites, 22 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L3C2_PRISES`*

### Chaine de dependances

```
MATERIEL (NAT: 13)
  - NAT: (native/UI) (13)
TPL (TPL: 11)
  - TPL: templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml (6)
  - TPL: templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml (5)
  -> VIGNETTE L3C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `light.hue_smart_eco_pc_bureau` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `light.hue_smart_eco_salon` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `light.hue_smart_eco_tv_chambre` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `sensor.prise_bureau_pc_ikea_current` | NAT | (native/UI) |
| `sensor.prise_bureau_pc_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_bureau_pc_ikea_voltage` | NAT | (native/UI) |
| `sensor.prise_horloge_ikea_current` | NAT | (native/UI) |
| `sensor.prise_horloge_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_horloge_ikea_voltage` | NAT | (native/UI) |
| `sensor.prise_salon_chargeur_nous_current` | NAT | (native/UI) |
| `sensor.prise_salon_chargeur_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_salon_chargeur_nous_voltage` | NAT | (native/UI) |
| `sensor.prise_tete_de_lit_chambre_current` | NAT | (native/UI) |
| `sensor.prise_tete_de_lit_chambre_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tete_de_lit_chambre_voltage` | NAT | (native/UI) |
| `sensor.prise_tv_chambre_nous_current` | NAT | (native/UI) |
| `sensor.prise_tv_chambre_nous_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tv_chambre_nous_voltage` | NAT | (native/UI) |
| `sensor.prise_tv_salon_ikea_current` | NAT | (native/UI) |
| `sensor.prise_tv_salon_ikea_power` | TPL | templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml |
| `sensor.prise_tv_salon_ikea_voltage` | NAT | (native/UI) |
| `switch.prise_horloge_ikea` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `switch.prise_tete_de_lit_chambre` | TPL | templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml |
| `switch.prise_tv_salon_ikea` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `templates/P0_energie_total_diag/P0_Total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml` | `H:\templates\P0_energie_total_diag\P0_Total_pour_les_7_postes\P0_total_pour_les_7_postes.yaml` | identique |
| `templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml` | `H:\templates\P2_prise\P2_eCO_prises\P2_eCO_prises_config.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L3C2_PRISES/L3C2_PRISES_01_Vignette/L3C2_Vignette_PRISES.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L3C2_PRISES/L3C2_PRISES_02_Page/L3C2_Page_PRISES.yaml`

### L3C3 - STORES

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-14*

*18 entites, 53 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L3C3_STORES`*

### Chaine de dependances

```
MATERIEL (NAT: 11)
  - NAT: (native/UI) (9)
  - NAT: groups/GRP_03_batteries_sonoff.yaml (2)
TPL (TPL: 7)
  - TPL: templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml (1)
  - TPL: templates/Stores/S_01_store.yaml (2)
  - TPL: templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml (4)
  -> VIGNETTE L3C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.contact_fenetre_bureau_sonoff_contact` | TPL | templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml |
| `binary_sensor.contact_fenetre_chambre_sonoff_contact` | TPL | templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml |
| `binary_sensor.contact_fenetre_cuisine_sonoff_contact` | TPL | templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml |
| `binary_sensor.contact_fenetre_salon_sonoff_contact` | TPL | templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml |
| `cover.set_cover_position` | NAT | (native/UI) |
| `cover.store_bureau` | TPL | templates/Stores/S_01_store.yaml |
| `cover.store_salon` | TPL | templates/Stores/S_01_store.yaml |
| `light.store_bureau_dnd` | NAT | (native/UI) |
| `light.store_salon_dnd` | NAT | (native/UI) |
| `sensor.contact_fenetre_bureau_sonoff_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.contact_fenetre_salon_sonoff_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.store_bureau_signal_strength` | NAT | (native/UI) |
| `sensor.store_bureau_status` | NAT | (native/UI) |
| `sensor.store_chambre_status` | NAT | (native/UI) |
| `sensor.store_cuisine_status` | NAT | (native/UI) |
| `sensor.store_salon_signal_strength` | NAT | (native/UI) |
| `sensor.store_salon_status` | NAT | (native/UI) |
| `sensor.th_balcon_nord_temperature` | TPL | templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `groups/GRP_03_batteries_sonoff.yaml` | `H:\groups\GRP_03_batteries_sonoff.yaml` | identique |
| `templates/Meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml` | `H:\templates\Meteo\M_04_meteo_tendances\M_04_tendances_th_ext_temperature_card.yaml` | identique |
| `templates/Stores/S_01_store.yaml` | `H:\templates\Stores\S_01_store.yaml` | identique |
| `templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml` | `H:\templates\utilitaires\nb_fenetre_ouvert_ferme_autom.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L3C3_STORES/L3C3_STORES_01_Vignette/L3C3_Vignette_STORES.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L3C3_STORES/L3C3_STORES_02_Page/L3C3_Page_STORES.yaml`

### L4C1 - MINI_PC

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-06-13 (docs entièrement réécrites - +5e section MyElectricalData)*

> Page complète supervision infrastructure Proxmox VE. Vignette : température CPU, CPU %, RAM %, Storage %, PVE Status. Page : **5 sections** (PVE, HA, Z2M, MariaDB, MyElectricalData) × métriques détaillées + apexcharts CPU 1h. Path → `/dashboard-tablette/systeme-proxmox`.
> ⚠️ Pas de `binary_sensor.myelectricaldata_backup_status` (contrairement à PVE). Pas de `sensor.myelectricaldata_utilisation_du_disque` en % - seuils page à exprimer en GiB absolu. Badge : vert `rgb(15,157,88)` - couleur section : `#00bcd4`.

*28 entites, 99 cartes, 3 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L4C1_MINI_PC`*

### Chaine de dependances

```
MATERIEL (NAT: 25)
  - NAT: (native/UI) (25)
TPL (TPL: 2)
  - TPL: templates/P2_prise/P2_AVG/P2_AVG_AMHQ_MINI_PC.yaml (2)
UM (UM: 1)
  - UM: utility_meter/P2_prise/P2_UM_AMHQ_MINI_PC.yaml (1)
  -> VIGNETTE L4C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.cpu_speed` | NAT | (native/UI) |
| `sensor.ip_externe_wan` | NAT | (native/UI) |
| `sensor.local_ip` | NAT | (native/UI) |
| `sensor.mini_pc_avg_watts_mensuel` | NAT | (native/UI) |
| `sensor.mini_pc_avg_watts_quotidien` | NAT | (native/UI) |
| `sensor.prise_mini_pc_ikea_current` | NAT | (native/UI) |
| `sensor.prise_mini_pc_ikea_energy` | UM | utility_meter/P2_prise/P2_UM_AMHQ_MINI_PC.yaml |
| `sensor.prise_mini_pc_ikea_mensuel_um` | TPL | templates/P2_prise/P2_AVG/P2_AVG_AMHQ_MINI_PC.yaml |
| `sensor.prise_mini_pc_ikea_power` | NAT | (native/UI) |
| `sensor.prise_mini_pc_ikea_quotidien_um` | TPL | templates/P2_prise/P2_AVG/P2_AVG_AMHQ_MINI_PC.yaml |
| `sensor.proxmox_carte_mere` | NAT | (native/UI) |
| `sensor.proxmox_core_0` | NAT | (native/UI) |
| `sensor.proxmox_core_1` | NAT | (native/UI) |
| `sensor.proxmox_core_2` | NAT | (native/UI) |
| `sensor.proxmox_core_3` | NAT | (native/UI) |
| `sensor.proxmox_cpu_package` | NAT | (native/UI) |
| `sensor.pve_memory_usage_percentage` | NAT | (native/UI) |
| `sensor.pve_uptime` | NAT | (native/UI) |
| `sensor.pve_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.pve_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.storage_local_storage_usage_percentage` | NAT | (native/UI) |
| `sensor.system_monitor_charge_15m` | NAT | (native/UI) |
| `sensor.system_monitor_charge_1m` | NAT | (native/UI) |
| `sensor.system_monitor_charge_5m` | NAT | (native/UI) |
| `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18` | NAT | (native/UI) |
| `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18` | NAT | (native/UI) |
| `sensor.system_monitor_memoire_libre` | NAT | (native/UI) |
| `sensor.system_monitor_memoire_utilisee` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `templates/P2_prise/P2_AVG/P2_AVG_AMHQ_MINI_PC.yaml` | `H:\templates\P2_prise\P2_AVG\P2_AVG_AMHQ_MINI_PC.yaml` | identique |
| `utility_meter/P2_prise/P2_UM_AMHQ_MINI_PC.yaml` | `H:\utility_meter\P2_prise\P2_UM_AMHQ_MINI_PC.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L4C1_MINI_PC/Card_popup_memory.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C1_MINI_PC/L4C1_MINI_PC_01_Vignette/L4C1_Vignette_MINI_PC.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C1_MINI_PC/L4C1_MINI_PC_02_Page/L4C1_Page_MINI_PC.yaml`

### L4C2 - PROXMOX

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-06-18 - vignette refactorisée : proxmox_cpu_package direct (sans template) | ⚠️ uptime bug non encore corrigé en page*

> ⚠️ **BUG UPTIME CONNU** (non corrigé) : Jinja2 dans la page utilise `| int(0)` + `/ 86400` alors que `sensor.pve_uptime` retourne des **heures** (float), pas des secondes. Résultat : affiche ~0j 0h. Fix à appliquer : ```yaml {% set uptime = states('sensor.pve_uptime') | float(0) %} {% set jours = (uptime / 24) | int(0) %} {% set heures = (uptime % 24) | int(0) %} {% set minutes = ((uptime % 1) * 60) | int(0) %} ```
> ⚠️ Interface réseau : **`enp6s18`** (VirtIO KVM sous Proxmox) - PAS `enp1s0`.

*69 entites, 115 cartes, 3 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L4C2_PROXMOX`*

### Chaine de dependances

```
MATERIEL (NAT: 69)
  - NAT: (native/UI) (69)
  -> VIGNETTE L4C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.pve_backup_status` | NAT | (native/UI) |
| `binary_sensor.pve_status` | NAT | (native/UI) |
| `button.homeassistant_create_snapshot` | NAT | (native/UI) |
| `button.homeassistant_demarrer` | NAT | (native/UI) |
| `button.homeassistant_redemarrer` | NAT | (native/UI) |
| `button.homeassistant_reload` | NAT | (native/UI) |
| `button.homeassistant_restart` | NAT | (native/UI) |
| `button.homeassistant_stopper` | NAT | (native/UI) |
| `button.mariadb_create_snapshot` | NAT | (native/UI) |
| `button.mariadb_demarrer` | NAT | (native/UI) |
| `button.mariadb_redemarrer` | NAT | (native/UI) |
| `button.mariadb_stopper` | NAT | (native/UI) |
| `button.press` | NAT | (native/UI) |
| `button.z2m_create_snapshot` | NAT | (native/UI) |
| `button.z2m_demarrer` | NAT | (native/UI) |
| `button.z2m_redemarrer` | NAT | (native/UI) |
| `button.z2m_stopper` | NAT | (native/UI) |
| `sensor.homeassistant_max_cpu` | NAT | (native/UI) |
| `sensor.homeassistant_memory_usage_percentage` | NAT | (native/UI) |
| `sensor.homeassistant_statut` | NAT | (native/UI) |
| `sensor.homeassistant_uptime` | NAT | (native/UI) |
| `sensor.homeassistant_utilisation_de_la_memoire` | NAT | (native/UI) |
| `sensor.homeassistant_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.homeassistant_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.homeassistant_utilisation_maximale_de_la_memoire` | NAT | (native/UI) |
| `sensor.homeassistant_utilisation_maximale_du_disque` | NAT | (native/UI) |
| `sensor.mariadb_max_cpu` | NAT | (native/UI) |
| `sensor.mariadb_memory_usage_percentage` | NAT | (native/UI) |
| `sensor.mariadb_statut` | NAT | (native/UI) |
| `sensor.mariadb_uptime` | NAT | (native/UI) |
| `sensor.mariadb_utilisation_de_la_memoire` | NAT | (native/UI) |
| `sensor.mariadb_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.mariadb_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.mariadb_utilisation_maximale_de_la_memoire` | NAT | (native/UI) |
| `sensor.mariadb_utilisation_maximale_du_disque` | NAT | (native/UI) |
| `sensor.myelectricaldata_max_cpu` | NAT | (native/UI) |
| `sensor.myelectricaldata_statut` | NAT | (native/UI) |
| `sensor.myelectricaldata_uptime` | NAT | (native/UI) |
| `sensor.myelectricaldata_utilisation_de_la_memoire` | NAT | (native/UI) |
| `sensor.myelectricaldata_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.myelectricaldata_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.myelectricaldata_utilisation_maximale_de_la_memoire` | NAT | (native/UI) |
| `sensor.myelectricaldata_utilisation_maximale_du_disque` | NAT | (native/UI) |
| `sensor.proxmox_cpu_package` | NAT | (native/UI) |
| `sensor.pve_max_cpu` | NAT | (native/UI) |
| `sensor.pve_memory_usage_percentage` | NAT | (native/UI) |
| `sensor.pve_statut` | NAT | (native/UI) |
| `sensor.pve_uptime` | NAT | (native/UI) |
| `sensor.pve_utilisation_de_la_memoire` | NAT | (native/UI) |
| `sensor.pve_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.pve_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.pve_utilisation_maximale_de_la_memoire` | NAT | (native/UI) |
| `sensor.pve_utilisation_maximale_du_disque` | NAT | (native/UI) |
| `sensor.searxng_pourcentage_d_utilisation_de_la_memoire` | NAT | (native/UI) |
| `sensor.searxng_statut` | NAT | (native/UI) |
| `sensor.searxng_temps_de_fonctionnement` | NAT | (native/UI) |
| `sensor.searxng_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.searxng_utilisation_maximale_de_la_memoire` | NAT | (native/UI) |
| `sensor.storage_local_storage_usage_percentage` | NAT | (native/UI) |
| `sensor.system_monitor_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.z2m_max_cpu` | NAT | (native/UI) |
| `sensor.z2m_memory_usage_percentage` | NAT | (native/UI) |
| `sensor.z2m_statut` | NAT | (native/UI) |
| `sensor.z2m_uptime` | NAT | (native/UI) |
| `sensor.z2m_utilisation_de_la_memoire` | NAT | (native/UI) |
| `sensor.z2m_utilisation_du_disque` | NAT | (native/UI) |
| `sensor.z2m_utilisation_du_processeur` | NAT | (native/UI) |
| `sensor.z2m_utilisation_maximale_de_la_memoire` | NAT | (native/UI) |
| `sensor.z2m_utilisation_maximale_du_disque` | NAT | (native/UI) |

### Fichiers YAML deployables

*Aucun fichier de config ne definit les entites de cette vignette (tout est natif).*

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L4C2_PROXMOX/Card_services_ha_Z2M_mariadb.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C2_PROXMOX/L4C2_PROXMOX_01_Vignette/L4C2_Vignette_PROXMOX.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C2_PROXMOX/L4C2_PROXMOX_02_Page/L4C2_Page_PROXMOX.yaml`

### L4C3 - MAJ_HA

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-14*

> ⚠️ Corrigé le 2026-07-19 : `sensor.available_updates` était marqué NAT - c'est en réalité un TPL (`templates/utilitaires/Mise_a_jour_home_assistant.yaml`, absent de cette section jusqu'ici), qui compte les entités `update.*` à l'état "on". Vérifié dans le corps du fichier.

*7 entites, 102 cartes, 4 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L4C3_MAJ_HA`*

### Chaine de dependances

```
MATERIEL (NAT: 7)
  - NAT: (native/UI) (7)
  -> VIGNETTE L4C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.available_updates` | NAT | (native/UI) |
| `update.hacs_update` | NAT | (native/UI) |
| `update.home` | NAT | (native/UI) |
| `update.home_assistant_core_update` | NAT | (native/UI) |
| `update.home_assistant_operating_system_update` | NAT | (native/UI) |
| `update.home_assistant_supervisor_update` | NAT | (native/UI) |
| `update.install` | NAT | (native/UI) |

### Fichiers YAML deployables

*Aucun fichier de config ne definit les entites de cette vignette (tout est natif).*

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L4C3_MAJ_HA/L4C3_MAJ_HA_01_Vignette/L4C3_Vignette_MAJ_HA.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C3_MAJ_HA/L4C3_MAJ_HA_02_Page_gauche/L4C3_Page_MAJ_HA_gauche.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C3_MAJ_HA/L4C3_MAJ_HA_03_Page_droite/L4C3_Page_MAJ_HA_droite.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L4C3_MAJ_HA/page_L4C3_maj_ha.yaml`

### L5C1 - PILES_BATTERIES

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-14 - ⚠️ page partiellement tronquée (3 sections HUE/IKEA/SONOFF à compléter)*

*41 entites, 11 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L5C1_PILES_BATTERIES`*

### Chaine de dependances

```
MATERIEL (NAT: 41)
  - NAT: (native/UI) (9)
  - NAT: groups/GRP_01_batteries_hue.yaml (11)
  - NAT: groups/GRP_02_batteries_ikea.yaml (8)
  - NAT: groups/GRP_03_batteries_sonoff.yaml (13)
  -> VIGNETTE L5C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `group.attributes` | NAT | (native/UI) |
| `group.hue_devices` | NAT | (native/UI) |
| `group.ikea_devices` | NAT | (native/UI) |
| `group.sonoff_devices` | NAT | (native/UI) |
| `sensor.contact_fenetre_bureau_sonoff_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.contact_fenetre_chambre_sonoff_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.contact_fenetre_cuisine_sonoff_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.contact_fenetre_salon_sonoff_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.detecteur_de_fuite_ikea_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.detecteur_ikea_vallhorn_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.gm1901_battery_level` | NAT | (native/UI) |
| `sensor.hue_smart_button_bureau_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_chambre_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_chambre_eric_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_chambre_gege_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_couloir_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_cuisine_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_eco_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_entree_1_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_entree_2_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_salle_de_bain_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.hue_smart_button_table_batterie` | NAT | groups/GRP_01_batteries_hue.yaml |
| `sensor.inter_bureau_rodret_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.inter_reserve_ikea_rodret_battery` | NAT | (native/UI) |
| `sensor.inter_salon_4_ikea_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.inter_somrig_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.inter_soufflant_salle_de_bain_ikea_rodret_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.ne2213_` | NAT | (native/UI) |
| `sensor.porte_congel_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.poussoir_pc_ikea_tradfri_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.poussoir_tv_ikea_tradfri_battery` | NAT | groups/GRP_02_batteries_ikea.yaml |
| `sensor.sm_a530f_battery_level` | NAT | (native/UI) |
| `sensor.tablette_battery_level` | NAT | (native/UI) |
| `sensor.th_balcon_nord_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_bureau_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_cellier_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_chambre_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_cuisine_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_salle_de_bain_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.th_salon_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |
| `sensor.tongel_battery` | NAT | groups/GRP_03_batteries_sonoff.yaml |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `groups/GRP_01_batteries_hue.yaml` | `H:\groups\GRP_01_batteries_hue.yaml` | identique |
| `groups/GRP_02_batteries_ikea.yaml` | `H:\groups\GRP_02_batteries_ikea.yaml` | identique |
| `groups/GRP_03_batteries_sonoff.yaml` | `H:\groups\GRP_03_batteries_sonoff.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_01_Vignette/L5C1_Vignette_PILES_BATTERIES.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C1_PILES_BATTERIES/L5C1_PILES_BATTERIES_02_Page/L5C1_Page_PILES_BATTERIES.yaml`

### L5C2 - BATTERIES_PORTABLES

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-12 - ⚠️ todo: vérifier sensor.ne2213_mamour_battery_health + temperature*

*49 entites, 35 cartes, 3 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L5C2_BATTERIES_PORTABLES`*

### Chaine de dependances

```
MATERIEL (NAT: 45)
  - NAT: (native/UI) (45)
TPL (TPL: 4)
  - TPL: templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml (2)
  - TPL: templates/P4_groupe_presence/P4_groupe_presence.yaml (2)
  -> VIGNETTE L5C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.eric_battery_health` | NAT | (native/UI) |
| `sensor.eric_battery_level` | NAT | (native/UI) |
| `sensor.eric_battery_state` | NAT | (native/UI) |
| `sensor.eric_battery_temperature` | NAT | (native/UI) |
| `sensor.eric_charger_type` | NAT | (native/UI) |
| `sensor.eric_network_type` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.eric_wi_fi_connection` | TPL | templates/P4_groupe_presence/P4_groupe_presence.yaml |
| `sensor.gm1901_battery_health` | NAT | (native/UI) |
| `sensor.gm1901_battery_level` | NAT | (native/UI) |
| `sensor.gm1901_battery_state` | NAT | (native/UI) |
| `sensor.gm1901_battery_temperature` | NAT | (native/UI) |
| `sensor.gm1901_charger_type` | NAT | (native/UI) |
| `sensor.gm1901_network_type` | NAT | (native/UI) |
| `sensor.gm1901_wi_fi_connection` | NAT | (native/UI) |
| `sensor.mamour_battery_health` | NAT | (native/UI) |
| `sensor.mamour_battery_level` | NAT | (native/UI) |
| `sensor.mamour_battery_state` | NAT | (native/UI) |
| `sensor.mamour_battery_temperature` | NAT | (native/UI) |
| `sensor.mamour_charger_type` | NAT | (native/UI) |
| `sensor.mamour_network_type` | TPL | templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml |
| `sensor.mamour_wi_fi_connection` | TPL | templates/P4_groupe_presence/P4_groupe_presence.yaml |
| `sensor.ne2213_eric_battery_health` | NAT | (native/UI) |
| `sensor.ne2213_eric_battery_level` | NAT | (native/UI) |
| `sensor.ne2213_eric_battery_state` | NAT | (native/UI) |
| `sensor.ne2213_eric_battery_temperature` | NAT | (native/UI) |
| `sensor.ne2213_eric_charger_type` | NAT | (native/UI) |
| `sensor.ne2213_eric_network_type` | NAT | (native/UI) |
| `sensor.ne2213_eric_wi_fi_connection` | NAT | (native/UI) |
| `sensor.ne2213_mamour_battery_health` | NAT | (native/UI) |
| `sensor.ne2213_mamour_battery_level` | NAT | (native/UI) |
| `sensor.ne2213_mamour_battery_state` | NAT | (native/UI) |
| `sensor.ne2213_mamour_battery_temperature` | NAT | (native/UI) |
| `sensor.ne2213_mamour_charger_type` | NAT | (native/UI) |
| `sensor.ne2213_mamour_network_type` | NAT | (native/UI) |
| `sensor.ne2213_mamour_wi_fi_connection` | NAT | (native/UI) |
| `sensor.sm_a530f_battery_health` | NAT | (native/UI) |
| `sensor.sm_a530f_battery_level` | NAT | (native/UI) |
| `sensor.sm_a530f_battery_state` | NAT | (native/UI) |
| `sensor.sm_a530f_battery_temperature` | NAT | (native/UI) |
| `sensor.sm_a530f_charger_type` | NAT | (native/UI) |
| `sensor.sm_a530f_network_type` | NAT | (native/UI) |
| `sensor.sm_a530f_wi_fi_connection` | NAT | (native/UI) |
| `sensor.tablette_battery_health` | NAT | (native/UI) |
| `sensor.tablette_battery_level` | NAT | (native/UI) |
| `sensor.tablette_battery_state` | NAT | (native/UI) |
| `sensor.tablette_battery_temperature` | NAT | (native/UI) |
| `sensor.tablette_charger_type` | NAT | (native/UI) |
| `sensor.tablette_network_type` | NAT | (native/UI) |
| `sensor.tablette_wi_fi_connection` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml` | `H:\templates\P1_clim_chauffage\P1_01_MASTER\P1_02_automation_message_clim_7h30_21h.yaml` | identique |
| `templates/P4_groupe_presence/P4_groupe_presence.yaml` | `H:\templates\P4_groupe_presence\P4_groupe_presence.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L5C2_BATTERIES_PORTABLES/L5C2_BATTERIES_PORTABLES_01_Vignette/L5C2_Vignette_BATTERIES_PORTABLES.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C2_BATTERIES_PORTABLES/L5C2_BATTERIES_PORTABLES_02_Page_gauche/L5C2_Page_BATTERIES_PORTABLES_gauche.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C2_BATTERIES_PORTABLES/L5C2_BATTERIES_PORTABLES_03_Page_droite/L5C2_Page_BATTERIES_PORTABLES_droite.yaml`

### L5C3 - MARIADB

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-10*

*13 entites, 48 cartes, 7 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB`*

### Chaine de dependances

```
MATERIEL (NAT: 13)
  - NAT: (native/UI) (13)
  -> VIGNETTE L5C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `automation.db_purge_mariadb_repack` | NAT | (native/UI) |
| `automation.trigger` | NAT | (native/UI) |
| `script.audit_md5` | NAT | (native/UI) |
| `script.audit_md5_md_yaml` | NAT | (native/UI) |
| `script.turn_on` | NAT | (native/UI) |
| `sensor.audit_md5_journal` | NAT | (native/UI) |
| `sensor.audit_md5_md_yaml_journal` | NAT | (native/UI) |
| `sensor.backup_github_journal` | NAT | (native/UI) |
| `sensor.backup_github_status` | NAT | (native/UI) |
| `sensor.git_last_weekly_tag` | NAT | (native/UI) |
| `sensor.github_default_branch` | NAT | (native/UI) |
| `sensor.taille_db_home_assistant` | NAT | (native/UI) |
| `text.split` | NAT | (native/UI) |

### Fichiers YAML deployables

*Aucun fichier de config ne definit les entites de cette vignette (tout est natif).*

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/Card_audit_buttons.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/Card_audit_journal.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/Card_audit_md5.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/Card_audit_recap.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/Card_mariadb.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/L5C3_MARIADB_01_Vignette/L5C3_Vignette_MARIADB.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L5C3_MARIADB/L5C3_MARIADB_02_Page_mariadb/L5C3_Page_MARIADB_mariadb.yaml`

### L6C1 - AIR_QUALITE

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-14*

*15 entites, 30 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L6C1_AIR_QUALITE`*

### Chaine de dependances

```
MATERIEL (NAT: 9)
  - NAT: (native/UI) (9)
SEN (SEN: 6)
  - SEN: sensors/Air_Quality/AQ_01_air_quality.yaml (6)
  -> VIGNETTE L6C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.pm2_5_bureau_moy_24h` | NAT | (native/UI) |
| `sensor.pm2_5_chambre_moy_24h` | NAT | (native/UI) |
| `sensor.pm2_5_salon_moy_24h` | NAT | (native/UI) |
| `sensor.qualite_air_bureau_ikea_pm25` | SEN | sensors/Air_Quality/AQ_01_air_quality.yaml |
| `sensor.qualite_air_bureau_ikea_voc_index` | SEN | sensors/Air_Quality/AQ_01_air_quality.yaml |
| `sensor.qualite_air_chambre_ikea_pm25` | SEN | sensors/Air_Quality/AQ_01_air_quality.yaml |
| `sensor.qualite_air_chambre_ikea_voc_index` | SEN | sensors/Air_Quality/AQ_01_air_quality.yaml |
| `sensor.qualite_air_salon_ikea_pm25` | SEN | sensors/Air_Quality/AQ_01_air_quality.yaml |
| `sensor.qualite_air_salon_ikea_voc_index` | SEN | sensors/Air_Quality/AQ_01_air_quality.yaml |
| `sensor.tcov_bureau_moy_24h` | NAT | (native/UI) |
| `sensor.tcov_bureau_ppb` | NAT | (native/UI) |
| `sensor.tcov_chambre_moy_24h` | NAT | (native/UI) |
| `sensor.tcov_chambre_ppb` | NAT | (native/UI) |
| `sensor.tcov_salon_moy_24h` | NAT | (native/UI) |
| `sensor.tcov_salon_ppb` | NAT | (native/UI) |

### Fichiers YAML deployables

| Fichier de config | Destination prod | Statut |
|:------------------|:-----------------|:-------|
| `sensors/Air_Quality/AQ_01_air_quality.yaml` | `H:\sensors\Air_Quality\AQ_01_air_quality.yaml` | identique |

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L6C1_AIR_QUALITE/L6C1_AIR_QUALITE_01_Vignette/L6C1_Vignette_AIR_QUALITE.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L6C1_AIR_QUALITE/L6C1_AIR_QUALITE_02_Page/L6C1_Page_AIR_QUALITE.yaml`

### L6C2 - POLLUTION_POLLEN

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-14*

*19 entites, 32 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L6C2_POLLUTION_POLLEN`*

### Chaine de dependances

```
MATERIEL (NAT: 19)
  - NAT: (native/UI) (19)
  -> VIGNETTE L6C2
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.concentration_ambroisie_vence` | NAT | (native/UI) |
| `sensor.concentration_armoise_vence` | NAT | (native/UI) |
| `sensor.concentration_aulne_vence` | NAT | (native/UI) |
| `sensor.concentration_bouleau_vence` | NAT | (native/UI) |
| `sensor.concentration_gramine_vence` | NAT | (native/UI) |
| `sensor.concentration_olivier_vence` | NAT | (native/UI) |
| `sensor.dioxyde_d_azote_vence` | NAT | (native/UI) |
| `sensor.dioxyde_de_soufre_vence` | NAT | (native/UI) |
| `sensor.niveau_ambroisie_vence` | NAT | (native/UI) |
| `sensor.niveau_armoise_vence` | NAT | (native/UI) |
| `sensor.niveau_aulne_vence` | NAT | (native/UI) |
| `sensor.niveau_bouleau_vence` | NAT | (native/UI) |
| `sensor.niveau_gramine_vence` | NAT | (native/UI) |
| `sensor.niveau_olivier_vence` | NAT | (native/UI) |
| `sensor.ozone_vence` | NAT | (native/UI) |
| `sensor.pm10_vence` | NAT | (native/UI) |
| `sensor.pm25_vence` | NAT | (native/UI) |
| `sensor.qualite_globale_pollen_vence` | NAT | (native/UI) |
| `sensor.qualite_globale_vence` | NAT | (native/UI) |

### Fichiers YAML deployables

*Aucun fichier de config ne definit les entites de cette vignette (tout est natif).*

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L6C2_POLLUTION_POLLEN/L6C2_POLLUTION_POLLEN_01_Vignette/L6C2_Vignette_POLLUTION_POLLEN.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L6C2_POLLUTION_POLLEN/L6C2_POLLUTION_POLLEN_02_Page/L6C2_Page_POLLUTION_POLLEN.yaml`

### L6C3 - VIGIEAU

*Annotations conservees de la version precedente (extraction du 2026-10-26).*

*Validée le 2026-05-14*

*4 entites, 16 cartes, 2 fichiers YAML - dossier `02_docs_dashboard/02_dashboard_docs_YAML/L6C3_VIGIEAU`*

### Chaine de dependances

```
MATERIEL (NAT: 4)
  - NAT: (native/UI) (4)
  -> VIGNETTE L6C3
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.alert_level_in_vence` | NAT | (native/UI) |
| `sensor.alert_level_in_vence_numeric` | NAT | (native/UI) |
| `sensor.attributes` | NAT | (native/UI) |
| `sensor.state` | NAT | (native/UI) |

### Fichiers YAML deployables

*Aucun fichier de config ne definit les entites de cette vignette (tout est natif).*

### Fichiers de la vignette (dashboard)

- `02_docs_dashboard/02_dashboard_docs_YAML/L6C3_VIGIEAU/L6C3_VIGIEAU_01_Vignette/L6C3_Vignette_VIGIEAU.yaml`
- `02_docs_dashboard/02_dashboard_docs_YAML/L6C3_VIGIEAU/L6C3_VIGIEAU_02_Page/L6C3_Page_VIGIEAU.yaml`

## 2. SCRIPTS .SH

### Audit_md5.sh
*04_docs_scripts/04_docs_scripts_SH/Audit_md5/Audit_md5.sh - 3 entites*

- `input_button.yaml`
- `input_datetime.yaml`
- `input_select.yaml`

### Audit_md5_md_yaml.sh
*04_docs_scripts/04_docs_scripts_SH/Audit_md5_md_yaml/Audit_md5_md_yaml.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### Audit_md5_yaml.sh
*04_docs_scripts/04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh - 3 entites*

- `input_button.yaml`
- `input_datetime.yaml`
- `input_select.yaml`

### Ha_git_backup.sh
*04_docs_scripts/04_docs_scripts_SH/Ha_git_backup/Ha_git_backup.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### Hermes_audit_md5_docs.sh
*04_docs_scripts/04_docs_scripts_SH/Hermes_audit_md5_docs/Hermes_audit_md5_docs.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### Hermes_audit_md5_trigul_3md.sh
*04_docs_scripts/04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

### Mf_vigilance_images.sh
*04_docs_scripts/04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh - 0 entites*

*Aucune entite HA referencee (script systeme/fichiers).*

## 3. AUTOMATIONS (PAR POLE)

### Automations_yaml_original
*1 fichiers YAML, 269 automations, 142 entites*

- Alerte Météo France actualisation des "CARTES
- Vérif si Today est HS
- Vérif si Tomorrow est HS
- Premier essai de mise à jour
- Répéter MAJ Today si toujours indisponible
- Répéter MAJ Tomorrow si toujours indisponible
- Rafraîchir les caméras finales
- [03-Backup] Git weekly (dim 01:30)
- [01-Backup] Git hourly H+10
- [02-Backup] Git daily (03:00)
- [00-Backup] Alerte si KO 15 min
- [04-Backup] Git push manuel
- [05-Backup] Git push weekly manuel
- DB Purge MariaDB + Repack
- Système - Économie Énergie VS Code
- ACTION : STOP (OU TIMEOUT)
- ACTION : KEEP
- [P3-SALON] BOUTON IKEA INTER SALON (4) — ON/OFF LIGHT.SALON
- DÉCLENCHEMENT : BOUTON ON (MQTT)
- DÉCLENCHEMENT : BOUTON OFF (MQTT)
- ACTION : BASCULE LIGHT.SALON
- CAS : BOUTON ON PRESSÉ
- CAS : BOUTON OFF PRESSÉ
- (H) (CLIM DEBUG) Force Mode Correct & Sécurité
- CALCUL DES LISTES D'ERREURS
- NOTIF : INTERDICTION DÉMARRAGE
- ACTION : FORCER OFF
- NOTIF : CORRECTION MODE
- ACTION : FORCER MODE SAISON
- Z - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT
- CHANGEMENT ÉTAT INTERRUPTEUR
- TEMPÉRATURE > 23°C
- TEMPÉRATURE < 22°C
- SÉCURITÉ AUTO-OFF 60 MIN
- ROUTAGE DES ACTIONS PAR TRIGGER
- CAS ALLUMAGE INTER
- DÉMARRAGE 2000W (< 21°C)
- CAS TEMPÉRATURE > 23°C
- CAS TEMPÉRATURE < 22°C
- CAS EXTINCTION (MANUELLE OU AUTO)
- F - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 2h)
- START : DÉTECTION PUISSANCE > 50W
- CHRONO : DÉCOMPTE DE 2 HEURES
- VERIF : EST-IL TOUJOURS ALLUMÉ ?
- ACTION : COUPURE DE SÉCURITÉ
- NOTIF : ARRÊT AUTO
- RESET : ATTENTE 1 MIN
- ACTION : RÉARMEMENT (VEILLE)
- (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)
- SYSTEM : REDÉMARRAGE HOME ASSISTANT
- HORAIRE : DÉMARRAGE 07H30
- RÉSEAU : CHANGEMENT WIFI <-> CELLULAR
- PRISES : CHANGEMENT ÉTAT ON/OFF
- FENÊTRES : OUVERTURE (COUPURE URGENCE)
- FENÊTRES : FERMETURE (RÉTABLISSEMENT)
- ENVIRONNEMENT : MISE À JOUR TEMPÉRATURES OU MODE
- (B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30)
- SYSTEM : REDÉMARRAGE HOME ASSISTANT
- HORAIRE : DÉMARRAGE 21H00
- RÉSEAU : CHANGEMENT WIFI <-> CELLULAR
- PRISES : CHANGEMENT ÉTAT ON/OFF
- FENÊTRES : OUVERTURE (COUPURE URGENCE)
- FENÊTRES : FERMETURE (RÉTABLISSEMENT)
- ENVIRONNEMENT : MISE À JOUR TEMPÉRATURES OU MODE
- Update previous temperature
- Update previous humidity
- Notification de la foudre
- Mettre à jour le temps du dernier impact de foudre
- (C) Notification température Up ou Down de (7h30 -> 21h00)
- DÉCLENCHEUR : CAPTEUR TEMPÉRATURE
- DÉCLENCHEUR : HORAIRE FIXE 07H30
- CONDITION : PÉRIODE DIURNE
- ACTION : PAUSE 2 SECONDES
- LOGIQUE : VÉRIFICATION CAPTEURS
- ACTION : NOTIF ERREUR (MAX 15 CAR)
- ACTION : NOTIF TENDANCE (MAX 15 CAR)
- (D) Notification température Up ou Down de (21h00 -> 7h30)
- DÉCLENCHEUR : CAPTEUR TEMPÉRATURE
- DÉCLENCHEUR : HORAIRE FIXE 21H00
- CONDITION : PÉRIODE NOCTURNE
- ACTION : PAUSE 2 SECONDES
- LOGIQUE : VÉRIFICATION CAPTEURS
- ACTION : NOTIF ERREUR (MAX 15 CAR)
- ACTION : NOTIF TENDANCE (MAX 15 CAR)
- (E) (CLIM) Notification de fermeture des fenêtres
- (F) (CLIM) Automatisation Arrêt Clim Notification
- (G) (CLIM) Notification de changement de mode Été/Fan/Hiver
- (I) Synchro & Notif Clim si Prise Coupée
- (J) (DEBUG) Notifier les changements de message clim (Mobile)
- Détection : CELLULAR
- Détection : MAMOUR
- Détection : ERIC
- Détection : LES DEUX
- Détection : UP (Hausse)
- Détection : DOWN (Baisse)
- Détection : STABLE
- Détection : HEAT
- Détection : COOL
- Détection : FAN
- A - Chauffage Cuisine (entre 4h45 & 7h LMMJ ou 5:45h & 8h VSD avec T° 19,9°
- Présence Eric ou Mamour
- Vérification Plage Horaire et Jour
- ARRÊT FORCE : Fin de période Semaine (07:00)
- ARRÊT FORCE : Fin de période Week-end (08:00)
- ACTION : Allumage (Temp < 19.9)
- ACTION : Extinction (Temp > 20.5)
- B - Chauffage Cuisine Vacances
- ARRÊT FORCÉ : Fin de période (8h30)
- DÉMARRAGE : Mode Chauffage
- Présence Eric ou Mamour
- ARRÊT : Température atteinte
- Présence Eric ou Mamour
- Gestion Optimisée du Store Bureau
- SÉCURITÉ : La fenêtre doit être FERMÉE pour bouger le store
- SCÉNARIO A : Ouverture Travail (Printemps/Automne)
- SCÉNARIO B : Fermeture Chaleur (Été)
- SCÉNARIO C : Fermeture Nuit
- Gestion Simple du Store Salon (Matin/Soir)
- SÉCURITÉ : La fenêtre doit être FERMÉE
- Matin : Ouverture si > 6h30 ET Soleil levé
- Soir : Fermeture au coucher du soleil
- ECO. PRISES DYNAMIQUE -> By-Présence/Groupe
- DÉCLENCHEUR — Changement de groupe
- FILTRE — Ignorer transitions depuis unavailable (boot HA)
- VARIABLES — Groupe actif + liste des prises (source externe)
- ACTION — ON/OFF chaque prise selon groupe
- DÉLAI — Attente mise à jour états avant notification
- ACTION — Notification résumé prises
- Gestion PC Bureau : Scène de Fin + Notif
- ALLUMAGE : Bouton ON
- EXTINCTION : veille confirmée (12 min)
- Gestion TV Chambre : Scène de Fin + Notif
- ALLUMAGE : Bouton ON
- EXTINCTION : veille confirmée (12 min)
- C - SALLE DE BAIN : WATCHDOG SÉCURITÉ SOUFFLANT
- TRIGGER : CHANGEMENT TEMPÉRATURE SDB
- CONDITION : VÉRIFICATION ALIMENTATION PRISE
- CONDITION : VÉRIFICATION ÉTAT INTERNE
- CONDITION : TEMPÉRATURE > 25°C
- CONDITION : DÉRIVE THERMIQUE RAPIDE (+0.4°C)
- ACTION : ATTENTE STABILISATION (1 MIN)
- ACTION : ENVOI COMMANDE IR RESET
- ETAT : PASSAGE DU BOOLEAN SUR OFF (SÉCURITÉ)
- ACTION : ATTENTE AVANT COUPURE (1 MIN) SÉCURITÉ
- MATÉRIEL : COUPURE PHYSIQUE DE LA PRISE
- NOTIFIER : ALERTE MOBILE DÉRIVE THERMIQUE
- P3_ENTREE_ALLUMAGE_LUMIERE
- SURVEILLANCE DU CHANGEMENT DE GROUPE DE PRÉSENCE
- CHOIX DE LA LOGIQUE SELON LA TRANSITION DÉTECTÉE
- CAS 1 : ARRIVÉE INITIALE EN PÉRIODE DIURNE (G1 -> PRÉSENCE)
- VÉRIFICATION : PASSAGE DE ABSENT À PRÉSENT
- VÉRIFICATION : PÉRIODE DIURNE (SOLEIL LEVÉ)
- ACTION : ALLUMAGE DE LA LUMIÈRE ENTRÉE
- CAS 2 : RETOUR DE MAMOUR (TRANSITION G3 VERS G4)
- VÉRIFICATION : PASSAGE DE ERIC SEUL À DUO
- ACTION : ALLUMAGE DE LA LUMIÈRE ENTRÉE
- P3_BUREAU - BOUTON RODRET TOGGLE BLANCHES
- RÉCEPTION MESSAGE MQTT BOUTON RODRET
- DÉCISION SELON LE PAYLOAD MQTT (ON OU OFF)
- BOUTON ON OU OFF PRESSÉ -> LOGIQUE TOGGLE
- VÉRIFICATION ACTION DANS LE JSON
- LOGIQUE DE BASCULEMENT (TOGGLE)
- SI LUMIÈRE PRÉSENTE -> EXTINCTION
- VÉRIFICATION SI UNE LAMPE EST ON
- EXTINCTION DES 2 LAMPES BLANCHES
- SI TOUT EST NOIR -> ALLUMAGE
- VÉRIFICATION SI TOUT EST OFF
- ALLUMAGE DES 2 LAMPES BLANCHES
- FORÇAGE MISE À JOUR DU SENSOR D'ÉTAT
- P3_BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES
- DÉTECTION ALLUMAGE LAMPE BUREAU 1
- DÉTECTION ALLUMAGE LAMPE BUREAU 2
- VÉRIFICATION SI UNE DES DEUX LAMPES RESTE ÉTEINTE
- FORÇAGE ALLUMAGE DES DEUX LAMPES
- MISE À JOUR FORCÉE DE L'ÉTAT DU BUREAU
- P3_BUREAU - Forcer Play ON si PC tourne
- PLAY 1
- PLAY 2
- PLAY 3
- P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO
- DÉCLENCHEMENT : PC BUREAU ALLUMÉ
- DÉCLENCHEMENT : PC BUREAU ÉTEINT
- DÉCLENCHEMENT : PRISE ÉCRAN COUPÉE 7 MIN
- ACTION : SYNCHRONISATION ALIMENTATION ÉCRAN
- CAS : PC ON -> ALLUMER ÉCRAN
- CAS : PRISE COUPÉE ALORS QUE LA SYNCHRO TOURNE -> ALLUMER ÉCRAN
- Système - Watchdog Piles (HUE/IKEA/SONOFF)
- Z2M last_seen
- [P3-SALON] BOUTON IKEA SOMRIG — TOUT MESSAGE = ON/OFF
- DÉCLENCHEMENT : BOUTON 1 (CLIC SIMPLE)
- DÉCLENCHEMENT : BOUTON 1 (DOUBLE CLIC)
- DÉCLENCHEMENT : BOUTON 1 (APPUI LONG)
- DÉCLENCHEMENT : BOUTON 2 (CLIC SIMPLE)
- DÉCLENCHEMENT : BOUTON 2 (DOUBLE CLIC)
- DÉCLENCHEMENT : BOUTON 2 (APPUI LONG)
- ACTION : ALLUMER OU ÉTEINDRE
- CAS : N''IMPORTE QUEL APPUI BOUTON 1 -> ALLUMER
- CAS : N''IMPORTE QUEL APPUI BOUTON 2 -> ÉTEINDRE
- AUTO. ENERGIE. Basculement Tarif HC/HP — Genelec Appart
- DÉCLENCHEUR : HC DÉBUT 01H00
- DÉCLENCHEUR : HP DÉBUT 07H30
- DÉCLENCHEUR : HC DÉBUT 13H00
- DÉCLENCHEUR : HP DÉBUT 14H30
- ACTION : PASSAGE EN HEURES CREUSES
- ACTION : PASSAGE EN HEURES PLEINES
- VEILLE GITHUB — Nouvelle release détectée
- DÉCLENCHEUR — Nouvelle entrée Feedreader
- VARIABLES — Extraire titre + lien + source
- ACTION — Notif standard (toutes releases)
- CONDITION — Breaking change détecté ?
- ACTION — Notif alerte breaking change
- Log Écart Linky vs Nodon
- P3_SDB - SYNC MIROIR LAMPE ET RELAIS SDB
- CHANGEMENT D'ÉTAT DE LA LAMPE SDB
- SYNCHRONISATION DU RELAIS SUR LA LAMPE
- S'ASSURER QUE LES DEUX SOIENT BIEN ALLUMÉS (SÉCURITÉ ON)
- SI LA LAMPE EST ON -> FORCE LE RELAIS ET LA LAMPE
- DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)
- DÉCLENCHEUR : TOUTES LES 15 MINUTES
- ACTION : ENREGISTREMENT DANS LE FICHIER
- [06-Backup] Git au démarrage HA
- DÉLAI : Attente stabilisation HA
- ACTION : Push Git
- LOG : Confirmation démarrage
- [P4] Eric — Log Zones
- CHANGEMENT ZONE ERIC
- ÉCRITURE LOG ZONE
- [P0] Histo Linky quotidien + Ecart J-1
- HORAIRE : EXECUTION 23H59
- [P0] Histo Nodon quotidien
- HORAIRE : EXECUTION 23H59
- [P0] Rattrapage Linky J-2 + Ecart
- HORAIRE : EXECUTION 23H59
- [P0] Rattrapage Linky MANQUANT + Ecart
- HORAIRE : EXECUTION 01H00
- P2 - ALARME Congélateur : Porte mal fermée (probable)
- P2 - ALARME Congélateur : Panne probable (pas de courant)
- P2 - ALARME Congélateur : Perte de supervision capteur Tongel
- B - SDB - SOUFFLANT - ROUTAGE (interrupteur vers sequences)
- Interrupteur SDB sur ON
- Interrupteur SDB sur OFF
- A - SDB - SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)
- Appui bouton I (marche)
- Appui bouton O (arret)
- D - SDB - SOUFFLANT - DECOMPTE 60 MIN (timer)
- Mise en marche reelle (arret vers marche)
- Interrupteur SDB sur arret
- Fin d'un des deux timers (60 min ou 10 min)
- Marche : lancer le timer 60 min
- Arret : annuler les deux timers
- Fin de timer : couper l''interrupteur s''il est encore en marche
- E - SDB - SOUFFLANT - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)
- Home Assistant demarre
- Laisser aux timers le temps d'etre restaures
- Lever le verrou, le script de demarrage qui le tenait ne tourne plus
- Soufflant en marche sans timer actif : lancer le rattrapage 10 min
- G - SDB - SECHE-SERVIETTES - DECOMPTE 2 H (timer)
- Chauffe detectee : puissance superieure a 50 W
- Prise sur arret
- Fin d'un des deux timers (2 h ou 10 min)
- Chauffe : lancer le 2 h s''il n''est pas deja actif, et annuler le rattrapage
- Prise sur arret : annuler les deux timers
- Fin de timer : coupure de securite, notification, puis rearmement (veille)
- Attente 1 minute
- Rearmement (veille)
- H - SDB - SECHE-SERVIETTES - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)
- Home Assistant demarre
- Laisser aux timers le temps d'etre restaures
- Prise en marche sans timer actif : lancer le rattrapage 10 min

### Backup_ha_GitHub
*7 fichiers YAML, 10 automations, 5 entites*

- [00-Backup] Alerte si KO 15 min
- [01-Backup] Git hourly H+10
- [02-Backup] Git daily (03:00)
- [03-Backup] Git weekly (dim 01:30)
- [04-Backup] Git push manuel
- [05-Backup] Git push weekly manuel
- [06-Backup] Git au démarrage HA
- DÉLAI : Attente stabilisation HA
- ACTION : Push Git
- LOG : Confirmation démarrage

### Bouton_virtuel
*2 fichiers YAML, 16 automations, 3 entites*

- [P3-SALON] BOUTON IKEA INTER SALON (4) — ON/OFF LIGHT.SALON
- DÉCLENCHEMENT : BOUTON ON (MQTT)
- DÉCLENCHEMENT : BOUTON OFF (MQTT)
- ACTION : BASCULE LIGHT.SALON
- CAS : BOUTON ON PRESSÉ
- CAS : BOUTON OFF PRESSÉ
- [P3-SALON] BOUTON IKEA SOMRIG — TOUT MESSAGE = ON/OFF
- DÉCLENCHEMENT : BOUTON 1 (CLIC SIMPLE)
- DÉCLENCHEMENT : BOUTON 1 (DOUBLE CLIC)
- DÉCLENCHEMENT : BOUTON 1 (APPUI LONG)
- DÉCLENCHEMENT : BOUTON 2 (CLIC SIMPLE)
- DÉCLENCHEMENT : BOUTON 2 (DOUBLE CLIC)
- DÉCLENCHEMENT : BOUTON 2 (APPUI LONG)
- ACTION : ALLUMER OU ÉTEINDRE
- CAS : N''IMPORTE QUEL APPUI BOUTON 1 -> ALLUMER
- CAS : N''IMPORTE QUEL APPUI BOUTON 2 -> ÉTEINDRE

### Controle_entity_Z2M
*1 fichiers YAML, 1 automations, 1 entites*

- Z2M last_seen

### Gestion_des_stores
*2 fichiers YAML, 9 automations, 8 entites*

- Gestion Optimisée du Store Bureau
- SÉCURITÉ : La fenêtre doit être FERMÉE pour bouger le store
- SCÉNARIO A : Ouverture Travail (Printemps/Automne)
- SCÉNARIO B : Fermeture Chaleur (Été)
- SCÉNARIO C : Fermeture Nuit
- Gestion Simple du Store Salon (Matin/Soir)
- SÉCURITÉ : La fenêtre doit être FERMÉE
- Matin : Ouverture si > 6h30 ET Soleil levé
- Soir : Fermeture au coucher du soleil

### Mariadb_et_vscode_optimisation
*2 fichiers YAML, 4 automations, 4 entites*

- DB Purge MariaDB + Repack
- Système - Économie Énergie VS Code
- ACTION : STOP (OU TIMEOUT)
- ACTION : KEEP

### Meteo
*5 fichiers YAML, 11 automations, 16 entites*

- Alerte Météo France actualisation des "CARTES
- Vérif si Today est HS
- Vérif si Tomorrow est HS
- Premier essai de mise à jour
- Répéter MAJ Today si toujours indisponible
- Répéter MAJ Tomorrow si toujours indisponible
- Rafraîchir les caméras finales
- Mettre à jour le temps du dernier impact de foudre
- Notification de la foudre
- Update previous humidity
- Update previous temperature

### P0_Energie
*7 fichiers YAML, 14 automations, 29 entites*

- DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)
- DÉCLENCHEUR : TOUTES LES 15 MINUTES
- ACTION : ENREGISTREMENT DANS LE FICHIER
- A - [P0] Histo Linky quotidien + Ecart J-1
- HORAIRE : EXECUTION 23H59
- E - [P0] Histo Nodon complet quotidien (Total HP HC Cout)
- HORAIRE : EXECUTION 23H59M10S
- B - [P0] Histo Nodon quotidien
- HORAIRE : EXECUTION 23H59
- Log Écart Linky vs Nodon
- D - [P0] Rattrapage Linky MANQUANT + Ecart
- HORAIRE : EXECUTION 01H00
- C - [P0] Rattrapage Linky J-2 + Ecart
- HORAIRE : EXECUTION 23H59

### P1_01_Clim_chauffage
*10 fichiers YAML, 53 automations, 30 entites*

- (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)
- SYSTEM : REDÉMARRAGE HOME ASSISTANT
- HORAIRE : DÉMARRAGE 07H30
- RÉSEAU : CHANGEMENT WIFI <-> CELLULAR
- PRISES : CHANGEMENT ÉTAT ON/OFF
- FENÊTRES : OUVERTURE (COUPURE URGENCE)
- FENÊTRES : FERMETURE (RÉTABLISSEMENT)
- ENVIRONNEMENT : MISE À JOUR TEMPÉRATURES OU MODE
- (B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30)
- SYSTEM : REDÉMARRAGE HOME ASSISTANT
- HORAIRE : DÉMARRAGE 21H00
- RÉSEAU : CHANGEMENT WIFI <-> CELLULAR
- PRISES : CHANGEMENT ÉTAT ON/OFF
- FENÊTRES : OUVERTURE (COUPURE URGENCE)
- FENÊTRES : FERMETURE (RÉTABLISSEMENT)
- ENVIRONNEMENT : MISE À JOUR TEMPÉRATURES OU MODE
- (C) Notification température Up ou Down de (7h30 -> 21h00)
- DÉCLENCHEUR : CAPTEUR TEMPÉRATURE
- DÉCLENCHEUR : HORAIRE FIXE 07H30
- CONDITION : PÉRIODE DIURNE
- ACTION : PAUSE 2 SECONDES
- LOGIQUE : VÉRIFICATION CAPTEURS
- ACTION : NOTIF ERREUR (MAX 15 CAR)
- ACTION : NOTIF TENDANCE (MAX 15 CAR)
- (D) Notification température Up ou Down de (21h00 -> 7h30)
- DÉCLENCHEUR : CAPTEUR TEMPÉRATURE
- DÉCLENCHEUR : HORAIRE FIXE 21H00
- CONDITION : PÉRIODE NOCTURNE
- ACTION : PAUSE 2 SECONDES
- LOGIQUE : VÉRIFICATION CAPTEURS
- ACTION : NOTIF ERREUR (MAX 15 CAR)
- ACTION : NOTIF TENDANCE (MAX 15 CAR)
- (E) (CLIM) Notification de fermeture des fenêtres
- (F) (CLIM) Automatisation Arrêt Clim Notification
- (G) (CLIM) Notification de changement de mode Été/Fan/Hiver
- (H) (CLIM DEBUG) Force Mode Correct & Sécurité
- CALCUL DES LISTES D'ERREURS
- NOTIF : INTERDICTION DÉMARRAGE
- ACTION : FORCER OFF
- NOTIF : CORRECTION MODE
- ACTION : FORCER MODE SAISON
- (I) Synchro & Notif Clim si Prise Coupée
- (J) (DEBUG) Notifier les changements de message clim (Mobile)
- Détection : CELLULAR
- Détection : MAMOUR
- Détection : ERIC
- Détection : LES DEUX
- Détection : UP (Hausse)
- Détection : DOWN (Baisse)
- Détection : STABLE
- Détection : HEAT
- Détection : COOL
- Détection : FAN

### P1_02_Cuisine
*2 fichiers YAML, 13 automations, 7 entites*

- A - Chauffage Cuisine (entre 4h45 & 7h LMMJ ou 5:45h & 8h VSD avec T° 19,9°
- Présence Eric ou Mamour
- Vérification Plage Horaire et Jour
- ARRÊT FORCE : Fin de période Semaine (07:00)
- ARRÊT FORCE : Fin de période Week-end (08:00)
- ACTION : Allumage (Temp < 19.9)
- ACTION : Extinction (Temp > 20.5)
- B - Chauffage Cuisine Vacances
- ARRÊT FORCÉ : Fin de période (8h30)
- DÉMARRAGE : Mode Chauffage
- Présence Eric ou Mamour
- ARRÊT : Température atteinte
- Présence Eric ou Mamour

### P1_03_Chauffage_salle_de_bain
*9 fichiers YAML, 62 automations, 27 entites*

- A - SDB - SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)
- Appui bouton I (marche)
- Appui bouton O (arret)
- B - SDB - SOUFFLANT - ROUTAGE (interrupteur vers sequences)
- Interrupteur SDB sur ON
- Interrupteur SDB sur OFF
- C - SALLE DE BAIN : WATCHDOG SÉCURITÉ SOUFFLANT
- TRIGGER : CHANGEMENT TEMPÉRATURE SDB
- CONDITION : VÉRIFICATION ALIMENTATION PRISE
- CONDITION : VÉRIFICATION ÉTAT INTERNE
- CONDITION : TEMPÉRATURE > 25°C
- CONDITION : DÉRIVE THERMIQUE RAPIDE (+0.4°C)
- ACTION : ATTENTE STABILISATION (1 MIN)
- ACTION : ENVOI COMMANDE IR RESET
- ETAT : PASSAGE DU BOOLEAN SUR OFF (SÉCURITÉ)
- ACTION : ATTENTE AVANT COUPURE (1 MIN) SÉCURITÉ
- MATÉRIEL : COUPURE PHYSIQUE DE LA PRISE
- NOTIFIER : ALERTE MOBILE DÉRIVE THERMIQUE
- D - SDB - SOUFFLANT - DECOMPTE 60 MIN (timer)
- Mise en marche reelle (arret vers marche)
- Interrupteur SDB sur arret
- Fin d'un des deux timers (60 min ou 10 min)
- Marche : lancer le timer 60 min
- Arret : annuler les deux timers
- Fin de timer : couper l''interrupteur s''il est encore en marche
- E - SDB - SOUFFLANT - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)
- Home Assistant demarre
- Laisser aux timers le temps d'etre restaures
- Lever le verrou, le script de demarrage qui le tenait ne tourne plus
- Soufflant en marche sans timer actif : lancer le rattrapage 10 min
- F - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 2h)
- START : DÉTECTION PUISSANCE > 50W
- CHRONO : DÉCOMPTE DE 2 HEURES
- VERIF : EST-IL TOUJOURS ALLUMÉ ?
- ACTION : COUPURE DE SÉCURITÉ
- NOTIF : ARRÊT AUTO
- RESET : ATTENTE 1 MIN
- ACTION : RÉARMEMENT (VEILLE)
- G - SDB - SECHE-SERVIETTES - DECOMPTE 2 H (timer)
- Chauffe detectee : puissance superieure a 50 W
- Prise sur arret
- Fin d'un des deux timers (2 h ou 10 min)
- Chauffe : lancer le 2 h s''il n''est pas deja actif, et annuler le rattrapage
- Prise sur arret : annuler les deux timers
- Fin de timer : coupure de securite, notification, puis rearmement (veille)
- Attente 1 minute
- Rearmement (veille)
- H - SDB - SECHE-SERVIETTES - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)
- Home Assistant demarre
- Laisser aux timers le temps d'etre restaures
- Prise en marche sans timer actif : lancer le rattrapage 10 min
- Z - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT
- CHANGEMENT ÉTAT INTERRUPTEUR
- TEMPÉRATURE > 23°C
- TEMPÉRATURE < 22°C
- SÉCURITÉ AUTO-OFF 60 MIN
- ROUTAGE DES ACTIONS PAR TRIGGER
- CAS ALLUMAGE INTER
- DÉMARRAGE 2000W (< 21°C)
- CAS TEMPÉRATURE > 23°C
- CAS TEMPÉRATURE < 22°C
- CAS EXTINCTION (MANUELLE OU AUTO)

### P1_SDB
*2 fichiers YAML, 6 automations, 6 entites*

- SDB - SOUFFLANT - ROUTAGE (interrupteur vers sequences)
- Interrupteur SDB sur ON
- Interrupteur SDB sur OFF
- SDB - SOUFFLANT - BOUTON IKEA RODRET (MQTT vers interrupteur)
- Appui bouton I (marche)
- Appui bouton O (arret)

### P2_Alarme_congelateur
*3 fichiers YAML, 3 automations, 4 entites*

- P2 - ALARME Congélateur : Perte de supervision capteur Tongel
- P2 - ALARME Congélateur : Panne probable (pas de courant)
- P2 - ALARME Congélateur : Porte mal fermée (probable)

### P2_eCO_prises
*3 fichiers YAML, 13 automations, 11 entites*

- Gestion PC Bureau : Scène de Fin + Notif
- ALLUMAGE : Bouton ON
- EXTINCTION : veille confirmée (12 min)
- Gestion TV Chambre : Scène de Fin + Notif
- ALLUMAGE : Bouton ON
- EXTINCTION : veille confirmée (12 min)
- ECO. PRISES DYNAMIQUE -> By-Présence/Groupe
- DÉCLENCHEUR — Changement de groupe
- FILTRE — Ignorer transitions depuis unavailable (boot HA)
- VARIABLES — Groupe actif + liste des prises (source externe)
- ACTION — ON/OFF chaque prise selon groupe
- DÉLAI — Attente mise à jour états avant notification
- ACTION — Notification résumé prises

### P3_Eclairage
*6 fichiers YAML, 45 automations, 17 entites*

- P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO
- DÉCLENCHEMENT : PC BUREAU ALLUMÉ
- DÉCLENCHEMENT : PC BUREAU ÉTEINT
- DÉCLENCHEMENT : PRISE ÉCRAN COUPÉE 7 MIN
- ACTION : SYNCHRONISATION ALIMENTATION ÉCRAN
- CAS : PC ON -> ALLUMER ÉCRAN
- CAS : PRISE COUPÉE ALORS QUE LA SYNCHRO TOURNE -> ALLUMER ÉCRAN
- P3_BUREAU - BOUTON RODRET TOGGLE BLANCHES
- RÉCEPTION MESSAGE MQTT BOUTON RODRET
- DÉCISION SELON LE PAYLOAD MQTT (ON OU OFF)
- BOUTON ON OU OFF PRESSÉ -> LOGIQUE TOGGLE
- VÉRIFICATION ACTION DANS LE JSON
- LOGIQUE DE BASCULEMENT (TOGGLE)
- SI LUMIÈRE PRÉSENTE -> EXTINCTION
- VÉRIFICATION SI UNE LAMPE EST ON
- EXTINCTION DES 2 LAMPES BLANCHES
- SI TOUT EST NOIR -> ALLUMAGE
- VÉRIFICATION SI TOUT EST OFF
- ALLUMAGE DES 2 LAMPES BLANCHES
- FORÇAGE MISE À JOUR DU SENSOR D'ÉTAT
- P3_BUREAU - Forcer Play ON si PC tourne
- PLAY 1
- PLAY 2
- PLAY 3
- P3_BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES
- DÉTECTION ALLUMAGE LAMPE BUREAU 1
- DÉTECTION ALLUMAGE LAMPE BUREAU 2
- VÉRIFICATION SI UNE DES DEUX LAMPES RESTE ÉTEINTE
- FORÇAGE ALLUMAGE DES DEUX LAMPES
- MISE À JOUR FORCÉE DE L'ÉTAT DU BUREAU
- P3_ENTREE_ALLUMAGE_LUMIERE
- SURVEILLANCE DU CHANGEMENT DE GROUPE DE PRÉSENCE
- CHOIX DE LA LOGIQUE SELON LA TRANSITION DÉTECTÉE
- CAS 1 : ARRIVÉE INITIALE EN PÉRIODE DIURNE (G1 -> PRÉSENCE)
- VÉRIFICATION : PASSAGE DE ABSENT À PRÉSENT
- VÉRIFICATION : PÉRIODE DIURNE (SOLEIL LEVÉ)
- ACTION : ALLUMAGE DE LA LUMIÈRE ENTRÉE
- CAS 2 : RETOUR DE MAMOUR (TRANSITION G3 VERS G4)
- VÉRIFICATION : PASSAGE DE ERIC SEUL À DUO
- ACTION : ALLUMAGE DE LA LUMIÈRE ENTRÉE
- P3_SDB - SYNC MIROIR LAMPE ET RELAIS SDB
- CHANGEMENT D'ÉTAT DE LA LAMPE SDB
- SYNCHRONISATION DU RELAIS SUR LA LAMPE
- S'ASSURER QUE LES DEUX SOIENT BIEN ALLUMÉS (SÉCURITÉ ON)
- SI LA LAMPE EST ON -> FORCE LE RELAIS ET LA LAMPE

### Tarif_hc_hp
*1 fichiers YAML, 7 automations, 5 entites*

- AUTO. ENERGIE. Basculement Tarif HC/HP — Genelec Appart
- DÉCLENCHEUR : HC DÉBUT 01H00
- DÉCLENCHEUR : HP DÉBUT 07H30
- DÉCLENCHEUR : HC DÉBUT 13H00
- DÉCLENCHEUR : HP DÉBUT 14H30
- ACTION : PASSAGE EN HEURES CREUSES
- ACTION : PASSAGE EN HEURES PLEINES

### Watchdog_piles_hue_ikea_sonoff
*1 fichiers YAML, 1 automations, 4 entites*

- Système - Watchdog Piles (HUE/IKEA/SONOFF)

### _Sans_categorie
*2 fichiers YAML, 9 automations, 5 entites*

- [P4] Eric — Log Zones
- CHANGEMENT ZONE ERIC
- ÉCRITURE LOG ZONE
- VEILLE GITHUB — Nouvelle release détectée
- DÉCLENCHEUR — Nouvelle entrée Feedreader
- VARIABLES — Extraire titre + lien + source
- ACTION — Notif standard (toutes releases)
- CONDITION — Breaking change détecté ?
- ACTION — Notif alerte breaking change

## 4. SCRIPTS NON-SH

- `04_docs_scripts/04_docs_scripts_SH/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.py` - 5 entites
- `04_docs_scripts/04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py` - 0 entites
- `04_docs_scripts/04_docs_scripts_SH/Check_sous_context_ia/Check_sous_context_ia.py` - 3 entites
- `04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py` - 1 entites
- `04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.py` - 2 entites
- `04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.py` - 1 entites
- `04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py` - 0 entites
- `04_docs_scripts/04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_unitaire.py` - 0 entites
- `04_docs_scripts/04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py` - 2 entites
- `04_docs_scripts/04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/trigul_run.py` - 2 entites
- `04_docs_scripts/04_docs_scripts_SH/Verif_emplacements/Verif_emplacements.py` - 0 entites
- `04_docs_scripts/04_docs_scripts_SH/Verif_headers_yaml/Verif_headers_yaml.py` - 0 entites
- `04_docs_scripts/04_docs_scripts_SH/Verif_integrations_file/Verif_integrations_file.py` - 0 entites
- `04_docs_scripts/04_docs_scripts_SH/histo_html/histo_html.py` - 1 entites
- `04_docs_scripts/04_docs_scripts_SH/histo_trace/histo_trace.py` - 1 entites

## 5. ENTITES ORPHELINES (NI DASHBOARD, NI AUTOMATIONS, NI SCRIPTS)

223 entites definies dans la config et utilisees nulle part.

- `input_boolean.turn_on` (TPL, templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_SDB.yaml)
- `input_boolean.voyant_thermostat_soufflant_salle_de_bain` (TPL, templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_SDB.yaml)
- `light.hue_smart_eco_tv_salon` (TPL, templates/P2_prise/P2_eCO_prises/P2_eCO_prises_config.yaml)
- `sensor.127_0_0_1` (NAT, configuration.yaml)
- `sensor.all_standby_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml)
- `sensor.all_standby_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml)
- `sensor.all_standby_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.clim_bureau_avg_watts_annuel` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.clim_bureau_avg_watts_hebdomadaire` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.clim_chambre_avg_watts_annuel` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.clim_chambre_avg_watts_hebdomadaire` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.clim_salon_avg_watts_annuel` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.clim_salon_avg_watts_hebdomadaire` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.condition_eric_wifi` (TPL, templates/P4_groupe_presence/P4_wifi_detection.yaml)
- `sensor.condition_mamour_wifi` (TPL, templates/P4_groupe_presence/P4_wifi_detection.yaml)
- `sensor.date` (NAT, configuration.yaml)
- `sensor.dut_sdb_seche_serviettes` (TPL, templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml)
- `sensor.dut_sdb_soufflant` (TPL, templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml)
- `sensor.eclairage_total_unit_hebdomadaire_kwh_tpl` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.four_et_plaque_de_cuisson_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.four_et_plaque_de_cuisson_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.four_et_plaque_de_cuisson_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.genelec_appart_annuel_um` (TPL, templates/P0_energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml)
- `sensor.genelec_appart_hphc_annuel_um_hc` (TPL, templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml)
- `sensor.genelec_appart_hphc_annuel_um_hp` (TPL, templates/P0_energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml)
- `sensor.histo_energie_nodon_complet` (TPL, templates/P0_energie_total_diag/P0_Linky/P0_MyElectricalData.yaml)
- `sensor.hue_ambiance_lamp_salon_1_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_power` (TPL, templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml)
- `sensor.hue_ambiance_lamp_salon_1_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_power` (TPL, templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml)
- `sensor.hue_ambiance_lamp_salon_2_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_power` (TPL, templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml)
- `sensor.hue_ambiance_lamp_salon_3_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_eric_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_chambre_gege_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_color_candle_salon_1_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_1_pc_bureau_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_2_pc_bureau_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_play_3_pc_bureau_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_1_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_bureau_2_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_1_power` (TPL, templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml)
- `sensor.hue_white_lamp_chambre_1_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_chambre_2_power` (TPL, templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml)
- `sensor.hue_white_lamp_chambre_2_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_couloir_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_cuisine_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_entree_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_salle_de_bain_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.hue_white_lamp_table_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.prise_airfryer_ninja_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_airfryer_ninja_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_airfryer_ninja_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_box_internet_ikea_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_box_internet_ikea_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_box_internet_ikea_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_bureau_fer_a_repasser_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_bureau_fer_a_repasser_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_bureau_fer_a_repasser_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_bureau_pc_ikea_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_bureau_pc_ikea_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_bureau_pc_ikea_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_congelateur_cuisine_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_congelateur_cuisine_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_congelateur_cuisine_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_four_micro_ondes_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_four_micro_ondes_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_four_micro_ondes_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_frigo_cuisine_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_frigo_cuisine_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_frigo_cuisine_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_horloge_ikea_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_horloge_ikea_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_horloge_ikea_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_lave_linge_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_lave_linge_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_lave_linge_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_lave_vaisselle_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_lave_vaisselle_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_lave_vaisselle_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_mini_pc_ikea_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_MINI_PC.yaml)
- `sensor.prise_mini_pc_ikea_hebdomadaire_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_MINI_PC.yaml)
- `sensor.prise_pc_s_gege_ikea_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_pc_s_gege_ikea_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_pc_s_gege_ikea_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_petit_dejeune_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_petit_dejeune_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_petit_dejeune_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_salon_chargeur_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_salon_chargeur_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_salon_chargeur_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_tete_de_lit_chambre_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_tete_de_lit_chambre_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_tete_de_lit_chambre_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_tv_chambre_nous_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_tv_chambre_nous_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_tv_chambre_nous_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.prise_tv_salon_ikea_annuel_um` (TPL, templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
- `sensor.prise_tv_salon_ikea_energy` (UM, utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml)
- `sensor.prise_tv_salon_ikea_hebdomadaire_um` (TPL, templates/P0_energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml)
- `sensor.radiateur_elec_cuisine_avg_watts_annuel` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.radiateur_elec_cuisine_avg_watts_hebdomadaire` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.relais_lumiere_sdb_sonoff_annuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.relais_lumiere_sdb_sonoff_annuel_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.relais_lumiere_sdb_sonoff_energy` (UM, utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
- `sensor.relais_lumiere_sdb_sonoff_hebdomadaire_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.relais_lumiere_sdb_sonoff_hebdomadaire_um_kwh_tpl` (TPL, templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml)
- `sensor.relais_lumiere_sdb_sonoff_mensuel_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.relais_lumiere_sdb_sonoff_quotidien_um` (TPL, templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml)
- `sensor.seche_serviette_sdb_avg_watts_annuel` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.seche_serviette_sdb_avg_watts_hebdomadaire` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.seuil_non_chauffage` (TPL, templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml)
- `sensor.seuil_non_clim` (TPL, templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml)
- `sensor.soufflant_sdb_avg_watts_annuel` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.soufflant_sdb_avg_watts_hebdomadaire` (TPL, templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml)
- `sensor.time` (NAT, configuration.yaml)

## STATISTIQUES

| Mesure | Valeur |
|:-------|-------:|
| Vignettes | 19 |
| Entites definies dans la config | 564 |
| Entites referencees quelque part | 871 |
| Entites orphelines | 223 |
| Scripts .sh | 7 |
| Scripts non-sh | 15 |
| Poles d'automations | 18 |
| Cartes au total | 1611 |

