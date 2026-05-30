# 📇 INDEX NAVIGATION — Dashboard HA

*Navigation complète des 18 vignettes — Accès direct aux docs, YAML, entités et pop-ups*
*Chemins relatifs depuis la racine du repo GitHub `home_assistant_re-build`*

---

## L1C1 — MÉTÉO

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L1C1_METEO/L1C1_VIGNETTE_METEO.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L1C1_01_Meteo/vignette_L1C1_meteo_2026-05-16.yaml)

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L1C1_METEO/PAGE_METEO.md)
- [⚙️ YAML Page](Docs/Dashboard/L1C1_01_Meteo/page_L1C1_meteo_2026-05-09.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`M_01_meteo_alertes_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml)
  - `sensor.alerte_avalanches`
  - `sensor.alerte_canicule`
  - `sensor.alerte_grand_froid`
  - `sensor.alerte_inondation`
  - `sensor.alerte_meteo`
  - `sensor.alerte_neige_verglas`
  - `sensor.alerte_orages`
  - `sensor.alerte_pluie_inondation`
  - `sensor.alerte_vagues_submersion`
  - `sensor.alerte_vent_violent`
- [`M_02_meteo_vent_vence_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml)
  - `sensor.vence_wind_speed`
  - `weather.vence`
- [`M_03_meteo_blitzortung.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml)
  - `sensor.dernier_impact_temps_reel`
  - `sensor.lightning_bearing`
  - `sensor.lightning_direction_label`
  - `sensor.lightning_distance_km`
- [`M_04_tendances_th_ext_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml)
  - `sensor.th_balcon_nord_temperature`
- [`M_05_cycle_solaire.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_05_cycle_solaire.yaml)
  - `sensor.duree_du_jour`
  - `sensor.tendance_duree_jour`
  - `sensor.variation_quotidienne`
- *Entités natives HA / intégrations externes :*
  - `camera.mf_alerte_today`
  - `camera.mf_alerte_tomorrow`
  - `sensor.06_weather_alert`
  - `sensor.direction_du_vent_vence`
  - `sensor.direction_du_vent_vence_label`
  - `sensor.eclairs_annuel`
  - `sensor.eclairs_hebdomadaire`
  - `sensor.eclairs_horaire`
  - `sensor.eclairs_mensuel`
  - `sensor.eclairs_quotidien`
  - `sensor.maison_lightning_counter`
  - `sensor.maison_lightning_distance`
  - `sensor.moon_phase`
  - `sensor.season`
  - `sensor.vence_daily_precipitation`
  - `sensor.vence_pressure`
  - `sensor.vence_uv`
  - `sensor.vence_wind_gust`
  - `sensor.vitesse_du_vent_vence`
  - `sun.sun`

#### Pop-up `#foudre`
- `sensor.dernier_impact_temps_reel`
- `sensor.eclairs_annuel`
- `sensor.eclairs_hebdomadaire`
- `sensor.eclairs_horaire`
- `sensor.eclairs_mensuel`
- `sensor.eclairs_quotidien`
- `sensor.lightning_bearing`
- `sensor.lightning_direction_label`
- `sensor.lightning_distance_km`
- `sensor.maison_lightning_counter`
- `sensor.maison_lightning_distance`

#### Pop-up `#alert`
- `camera.mf_alerte_today`
- `camera.mf_alerte_tomorrow`
- `sensor.06_weather_alert`
- `sensor.alerte_avalanches`
- `sensor.alerte_canicule`
- `sensor.alerte_grand_froid`
- `sensor.alerte_inondation`
- `sensor.alerte_meteo`
- `sensor.alerte_neige_verglas`
- `sensor.alerte_orages`
- `sensor.alerte_pluie_inondation`
- `sensor.alerte_vagues_submersion`
- `sensor.alerte_vent_violent`

#### Pop-up `#sun`
- `sensor.duree_du_jour`
- `sensor.moon_phase`
- `sensor.season`
- `sensor.tendance_duree_jour`
- `sensor.variation_quotidienne`
- `sun.sun`

- [📄 TUTO IMAGES ALERTES METEO FRANCE](Docs/docs_dashboard/docs/L1C1_METEO/TUTO_IMAGES_ALERTES_METEO_FRANCE.md)

- [⚙️ Card Durée du Jour](Docs/Dashboard/L1C1_01_Meteo/card_duree_du_jour_2026-05-03.yaml)

---

## L1C2 — TEMPÉRATURES

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L1C2_TEMPERATURES/L1C2_VIGNETTE_TEMPERATURES.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L1C2_02_Temperatures/vignette_L1C2_temperatures_2026-05-12.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`M_04_tendances_th_ext_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml)
  - `sensor.th_balcon_nord_humidity`
  - `sensor.th_balcon_nord_temperature`
- *Entités natives HA / intégrations externes :*
  - `sensor.th_bureau_humidity`
  - `sensor.th_bureau_temperature`
  - `sensor.th_cellier_humidity`
  - `sensor.th_cellier_temperature`
  - `sensor.th_chambre_humidity`
  - `sensor.th_chambre_temperature`
  - `sensor.th_cuisine_humidity`
  - `sensor.th_cuisine_temperature`
  - `sensor.th_salle_de_bain_humidity`
  - `sensor.th_salle_de_bain_temperature`
  - `sensor.th_salon_humidity`
  - `sensor.th_salon_temperature`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L1C2_TEMPERATURES/PAGE_TEMPERATURES.md)
- [⚙️ YAML Page](Docs/Dashboard/L1C2_02_Temperatures/page_L1C2_temperatures_2026-05-12.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_01_clim_logique_system_autom.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml)
  - `sensor.temperature_delta_affichage`
  - `sensor.temperature_moyenne_interieure`
- [`P1_AVG_TOTAL_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml)
  - `sensor.clim_rad_total_avg_watts_quotidien`
- [`P1_TOTAL_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml)
  - `sensor.conso_clim_rad_total`
  - `sensor.conso_clim_rad_total_mensuel`
  - `sensor.conso_clim_rad_total_quotidien`
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `climate.radiateur_cuisine`
  - `sensor.bureau_power_status`
  - `sensor.chambre_power_status`
  - `sensor.cuisine_power_status`
  - `sensor.salon_power_status`
  - `sensor.sdb_seche_serviette_power_status`
  - `sensor.sdb_soufflant_power_status`
- [`M_02_meteo_vent_vence_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml)
  - `weather.vence`
- [`M_04_tendances_th_ext_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml)
  - `sensor.th_balcon_nord_humidity`
  - `sensor.th_balcon_nord_temperature`
- [`P1_UM_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml)
  - `switch.radiateur_elec_cuisine`
- *Entités natives HA / intégrations externes :*
  - `climate.clim_bureau_rm4_mini`
  - `climate.clim_chambre_rm4_mini`
  - `climate.clim_du_bureau`
  - `climate.clim_salon_rm4_mini`
  - `sensor.th_balcon_nord_battery`
  - `sensor.th_bureau_battery`
  - `sensor.th_bureau_humidity`
  - `sensor.th_bureau_temperature`
  - `sensor.th_cellier_battery`
  - `sensor.th_cellier_humidity`
  - `sensor.th_cellier_temperature`
  - `sensor.th_chambre_battery`
  - `sensor.th_chambre_humidity`
  - `sensor.th_chambre_temperature`
  - `sensor.th_cuisine_battery`
  - `sensor.th_cuisine_humidity`
  - `sensor.th_cuisine_temperature`
  - `sensor.th_salle_de_bain_battery`
  - `sensor.th_salle_de_bain_humidity`
  - `sensor.th_salle_de_bain_temperature`
  - `sensor.th_salon_battery`
  - `sensor.th_salon_humidity`
  - `sensor.th_salon_temperature`
  - `sensor.vence_temperature`

#### Pop-up `#tendances`
- *(aucune entité détectée)*

#### Pop-up `#exterieur`
- `sensor.th_balcon_nord_temperature`
- `weather.vence`

#### Pop-up `#salon`
- `sensor.th_salon_temperature`

#### Pop-up `#cellier`
- `sensor.th_cellier_temperature`

#### Pop-up `#cuisine`
- `sensor.th_cuisine_temperature`

#### Pop-up `#bureau`
- `sensor.th_bureau_temperature`

#### Pop-up `#salle_de_bain`
- `sensor.th_salle_de_bain_temperature`

#### Pop-up `#chambre`
- `sensor.th_chambre_temperature`

#### Pop-up `#tcourbe`
- `sensor.th_balcon_nord_temperature`

#### Pop-up `#hcourbe`
- `sensor.th_balcon_nord_humidity`

---

## L1C3 — COMMANDES CLIM

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L1C3_CLIM/L1C3_VIGNETTE_CLIM.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_01_clim_logique_system_autom.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml)
  - `sensor.delta_ademe_recommande`
  - `sensor.temperature_moyenne_interieure`
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `climate.radiateur_cuisine`
  - `sensor.bureau_power_status`
  - `sensor.chambre_power_status`
  - `sensor.clim_bureau_etat`
  - `sensor.clim_chambre_etat`
  - `sensor.clim_salon_etat`
  - `sensor.cuisine_power_status`
  - `sensor.mode_ete_hiver_etat`
  - `sensor.radiateur_cuisine_etat`
  - `sensor.salon_power_status`
  - `sensor.sdb_seche_serviette_etat`
  - `sensor.sdb_seche_serviette_power_status`
  - `sensor.sdb_soufflant_etat`
  - `sensor.sdb_soufflant_power_status`
- *Entités natives HA / intégrations externes :*
  - `climate.clim_bureau_rm4_mini`
  - `climate.clim_chambre_rm4_mini`
  - `climate.clim_salon_rm4_mini`
  - `climate.soufflant_salle_de_bain`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L1C3_CLIM/PAGE_CLIM.md)
- [⚙️ YAML Page](Docs/Dashboard/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_BV_01_SW_inter_souflant_sdb.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/Inter_BP_Virtuel/P1/P1_BV_01_SW_inter_souflant_sdb.yaml)
  - `switch.inter_soufflant_salle_de_bain`
- [`P1_01_clim_logique_system_autom.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml)
  - `sensor.temperature_delta_affichage`
- [`P1_TOTAL_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml)
  - `sensor.conso_clim_rad_total`
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `climate.radiateur_cuisine`
  - `sensor.bureau_power_status`
  - `sensor.bureau_power_status_affichage`
  - `sensor.chambre_power_status`
  - `sensor.chambre_power_status_affichage`
  - `sensor.cuisine_power_status`
  - `sensor.cuisine_power_status_affichage`
  - `sensor.salon_power_status`
  - `sensor.salon_power_status_affichage`
  - `sensor.sdb_power_status_affichage`
  - `sensor.sdb_seche_serviette_power_status`
  - `sensor.sdb_soufflant_power_status`
- [`P1_UM_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml)
  - `remote.clim_bureau`
  - `remote.clim_chambre`
  - `remote.clim_salon`
  - `remote.soufflant_sdb`
  - `switch.radiateur_elec_cuisine`
- *Entités natives HA / intégrations externes :*
  - `climate.clim_bureau_rm4_mini`
  - `climate.clim_chambre_rm4_mini`
  - `climate.clim_salon_rm4_mini`
  - `climate.soufflant_salle_de_bain`
  - `input_boolean.clim_bureau_arret_securise_en_cours`
  - `input_boolean.clim_chambre_arret_securise_en_cours`
  - `input_boolean.clim_salon_arret_securise_en_cours`
  - `input_select.etat_resistance_soufflant_sdb`
  - `sensor.bureau_power_lock`
  - `sensor.chambre_power_lock`
  - `sensor.clim_bureau_nous_power`
  - `sensor.clim_chambre_nous_power`
  - `sensor.clim_salon_nous_power`
  - `sensor.prise_soufflant_salle_de_bain_nous_power`
  - `sensor.radiateur_elec_cuisine_power`
  - `sensor.salon_power_lock`
  - `sensor.sdb_seche_serviette_status_affichage`
  - `sensor.th_salle_de_bain_temperature`
  - `switch.clim_bureau_nous`
  - `switch.clim_chambre_nous`
  - `switch.clim_salon_nous`
  - `switch.prise_soufflant_salle_de_bain_nous`
  - `switch.schedule_clim_de_la_chambre_week`
  - `switch.schedule_clim_de_la_chambre_week_end`
  - `switch.schedule_clim_du_bureau_week`
  - `switch.schedule_clim_du_bureau_week_end`
  - `switch.schedule_clim_du_salon_week`
  - `switch.schedule_clim_du_salon_week_end`
  - `switch.schedule_radiateur_cuisine_week`
  - `switch.schedule_radiateur_cuisine_week_end`
  - `switch.schedule_soufflant_salle_de_bain_week`
  - `switch.schedule_soufflant_salle_de_bain_week_end`

#### Pop-up `#calcul`
- *(aucune entité détectée)*

---

## L2C1 — ÉNERGIE GÉNÉRALE

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L2C1_04_Energie_Generale/vignette_L2C1_energie_2026-05-12.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P0_MINI_MAXI_AVG_Genelec_appart.yaml`](Docs/docs_dashboard/TREE_CORRIGE/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml)
  - `sensor.genelec_appart_conso_maxi_24h`
  - `sensor.genelec_appart_conso_mini_24h`
- [`01_genelec_appart_AMHQ_cost.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml)
  - `sensor.genelec_appart_cout_hc_quotidien`
  - `sensor.genelec_appart_cout_hp_quotidien`
  - `sensor.genelec_appart_cout_total_quotidien`
- *Entités natives HA / intégrations externes :*
  - `sensor.general_electric_appart_power`

### Pages (3)

#### Page Principale

- [📄 Doc Page](Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE.md)
- [⚙️ YAML Page](Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-05-12.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- [`P0_kWh_genelec_appart.yaml`](Docs/docs_dashboard/TREE_CORRIGE/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart/P0_kWh_genelec_appart.yaml)
  - `sensor.genelec_appart_totale_kwh`
- [`P0_MINI_MAXI_AVG_Genelec_appart.yaml`](Docs/docs_dashboard/TREE_CORRIGE/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml)
  - `sensor.genelec_appart_conso_maxi_24h`
  - `sensor.genelec_appart_conso_mini_24h`
- [`diag_conso_hebdomadaire_en_cours.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/diag_conso_hebdomadaire_en_cours.yaml)
  - `sensor.diag_poste_autre_hebdomadaire`
  - `sensor.diag_poste_chauffage_hebdomadaire`
  - `sensor.diag_poste_cuisine_hebdomadaire`
  - `sensor.diag_poste_eclairage_hebdomadaire`
  - `sensor.diag_poste_froid_hebdomadaire`
  - `sensor.diag_poste_hygiene_hebdomadaire`
  - `sensor.diag_poste_multimedia_hebdomadaire`
- [`diag_conso_jour_en_cours.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml)
  - `sensor.diag_poste_autre_quotidien`
  - `sensor.diag_poste_chauffage_quotidien`
  - `sensor.diag_poste_cuisine_quotidien`
  - `sensor.diag_poste_eclairage_quotidien`
  - `sensor.diag_poste_froid_quotidien`
  - `sensor.diag_poste_hygiene_quotidien`
  - `sensor.diag_poste_multimedia_quotidien`
- [`diag_conso_mois_en_cours.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml)
  - `sensor.diag_poste_autre_mensuel`
  - `sensor.diag_poste_chauffage_mensuel`
  - `sensor.diag_poste_cuisine_mensuel`
  - `sensor.diag_poste_eclairage_mensuel`
  - `sensor.diag_poste_froid_mensuel`
  - `sensor.diag_poste_hygiene_mensuel`
  - `sensor.diag_poste_multimedia_mensuel`
- [`01_genelec_appart_AMHQ_cost.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml)
  - `sensor.genelec_appart_cout_hc_hebdomadaire`
  - `sensor.genelec_appart_cout_hc_mensuel`
  - `sensor.genelec_appart_cout_hc_quotidien`
  - `sensor.genelec_appart_cout_hp_hebdomadaire`
  - `sensor.genelec_appart_cout_hp_mensuel`
  - `sensor.genelec_appart_cout_hp_quotidien`
  - `sensor.genelec_appart_cout_total_hebdomadaire`
  - `sensor.genelec_appart_cout_total_mensuel`
  - `sensor.genelec_appart_cout_total_quotidien`
- [`02_ratio_hp_hc.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml)
  - `sensor.genelec_appart_ratio_hc_hebdomadaire`
  - `sensor.genelec_appart_ratio_hc_mensuel`
  - `sensor.genelec_appart_ratio_hc_quotidien`
- [`03_AVG_genelec_appart.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/03_AVG_genelec_appart.yaml)
  - `sensor.genelec_appart_avg_watts_mensuel`
  - `sensor.genelec_appart_avg_watts_quotidien`
- [`MyElectricalData.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml)
  - `sensor.linky_jour_0`
  - `sensor.linky_jour_1`
  - `sensor.linky_jour_2`
  - `sensor.linky_jour_3`
  - `sensor.linky_jour_4`
  - `sensor.linky_jour_5`
  - `sensor.linky_jour_6`
  - `sensor.linky_jour_7`
- *Entités natives HA / intégrations externes :*
  - `sensor.genelec_appart_hebdomadaire_um`
  - `sensor.genelec_appart_hphc_hebdomadaire_um_hc`
  - `sensor.genelec_appart_hphc_hebdomadaire_um_hp`
  - `sensor.genelec_appart_hphc_mensuel_um_hc`
  - `sensor.genelec_appart_hphc_mensuel_um_hp`
  - `sensor.genelec_appart_hphc_quotidien_um_hc`
  - `sensor.genelec_appart_hphc_quotidien_um_hp`
  - `sensor.genelec_appart_mensuel_um`
  - `sensor.genelec_appart_quotidien_kwh_um`
  - `sensor.genelec_appart_quotidien_um`
  - `sensor.general_electric_appart_energy`
  - `sensor.general_electric_appart_power`
  - `sensor.linky_25481620821301_consumption`
  - `sensor.linky_25481620821301_consumption_history`

#### Page Mensuel

- [📄 Doc Page](Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE_MENSUEL.md)
- [⚙️ YAML Page](Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_mensuel_2026-05-12.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- [`P2_AVG_AMHQ_prises.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
  - `sensor.airfryer_avg_watts_mensuel`
  - `sensor.box_internet_avg_watts_mensuel`
  - `sensor.chargeurs_salon_avg_watts_mensuel`
  - `sensor.congelateur_avg_watts_mensuel`
  - `sensor.fer_repasser_avg_watts_mensuel`
  - `sensor.four_mo_avg_watts_mensuel`
  - `sensor.frigo_avg_watts_mensuel`
  - `sensor.horloge_avg_watts_mensuel`
  - `sensor.lave_linge_avg_watts_mensuel`
  - `sensor.lave_vaisselle_avg_watts_mensuel`
  - `sensor.pc_bureau_avg_watts_mensuel`
  - `sensor.pc_gege_avg_watts_mensuel`
  - `sensor.petit_dej_avg_watts_mensuel`
  - `sensor.plaques_cuisson_avg_watts_mensuel`
  - `sensor.tetes_lit_avg_watts_mensuel`
  - `sensor.tv_chambre_avg_watts_mensuel`
  - `sensor.tv_salon_avg_watts_mensuel`
- [`P2_AVG_AMHQ_veilles.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml)
  - `sensor.all_standby_avg_watts_mensuel`
- *Entités natives HA / intégrations externes :*
  - `sensor.all_standby_mensuel_um`
  - `sensor.four_et_plaque_de_cuisson_mensuel_um`
  - `sensor.prise_airfryer_ninja_nous_mensuel_um`
  - `sensor.prise_box_internet_ikea_mensuel_um`
  - `sensor.prise_bureau_fer_a_repasser_nous_mensuel_um`
  - `sensor.prise_bureau_pc_ikea_mensuel_um`
  - `sensor.prise_congelateur_cuisine_nous_mensuel_um`
  - `sensor.prise_four_micro_ondes_nous_mensuel_um`
  - `sensor.prise_frigo_cuisine_nous_mensuel_um`
  - `sensor.prise_horloge_ikea_mensuel_um`
  - `sensor.prise_lave_linge_nous_mensuel_um`
  - `sensor.prise_lave_vaisselle_nous_mensuel_um`
  - `sensor.prise_pc_s_gege_ikea_mensuel_um`
  - `sensor.prise_petit_dejeune_nous_mensuel_um`
  - `sensor.prise_salon_chargeur_nous_mensuel_um`
  - `sensor.prise_tete_de_lit_chambre_mensuel_um`
  - `sensor.prise_tv_chambre_nous_mensuel_um`
  - `sensor.prise_tv_salon_ikea_mensuel_um`

#### Page Temps Réel

- [📄 Doc Page](Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE_TEMPS_REEL.md)
- [⚙️ YAML Page](Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_temps_reel_2026-05-12.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- [`P2_AVG_AMHQ_prises.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml)
  - `sensor.airfryer_avg_watts_quotidien`
  - `sensor.box_internet_avg_watts_quotidien`
  - `sensor.chargeurs_salon_avg_watts_quotidien`
  - `sensor.congelateur_avg_watts_quotidien`
  - `sensor.fer_repasser_avg_watts_quotidien`
  - `sensor.four_mo_avg_watts_quotidien`
  - `sensor.frigo_avg_watts_quotidien`
  - `sensor.horloge_avg_watts_quotidien`
  - `sensor.lave_linge_avg_watts_quotidien`
  - `sensor.lave_vaisselle_avg_watts_quotidien`
  - `sensor.pc_bureau_avg_watts_quotidien`
  - `sensor.pc_gege_avg_watts_quotidien`
  - `sensor.petit_dej_avg_watts_quotidien`
  - `sensor.plaques_cuisson_avg_watts_quotidien`
  - `sensor.tetes_lit_avg_watts_quotidien`
  - `sensor.tv_chambre_avg_watts_quotidien`
  - `sensor.tv_salon_avg_watts_quotidien`
- [`P2_AVG_AMHQ_veilles.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml)
  - `sensor.all_standby_avg_watts_quotidien`
- [`P2_current_all_standby.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_I_all_standby_power/P2_current_all_standby.yaml)
  - `sensor.all_standby_current`
- *Entités natives HA / intégrations externes :*
  - `sensor.all_standby_power`
  - `sensor.all_standby_quotidien_um`
  - `sensor.clim_bureau_nous_power`
  - `sensor.clim_chambre_nous_power`
  - `sensor.clim_salon_nous_power`
  - `sensor.eclairage_total_group_puissance_tpl`
  - `sensor.four_et_plaque_de_cuisson_current`
  - `sensor.four_et_plaque_de_cuisson_power`
  - `sensor.four_et_plaque_de_cuisson_quotidien_um`
  - `sensor.general_electric_appart_power`
  - `sensor.hue_ambiance_lamp_salon_`
  - `sensor.hue_color_candle_chambre_eric_power`
  - `sensor.hue_color_candle_chambre_gege_power`
  - `sensor.hue_color_candle_salon_1_power`
  - `sensor.hue_play_1_pc_bureau_power`
  - `sensor.hue_play_2_pc_bureau_power`
  - `sensor.hue_play_3_pc_bureau_power`
  - `sensor.hue_white_lamp_bureau_1_power`
  - `sensor.hue_white_lamp_bureau_2_power`
  - `sensor.hue_white_lamp_chambre_`
  - `sensor.hue_white_lamp_couloir_power`
  - `sensor.hue_white_lamp_cuisine_power`
  - `sensor.hue_white_lamp_entree_power`
  - `sensor.hue_white_lamp_table_power`
  - `sensor.lampe_salle_de_bain_hue_power`
  - `sensor.prise_airfryer_ninja_nous_current`
  - `sensor.prise_airfryer_ninja_nous_power`
  - `sensor.prise_airfryer_ninja_nous_quotidien_um`
  - `sensor.prise_box_internet_ikea_current`
  - `sensor.prise_box_internet_ikea_power`
  - `sensor.prise_box_internet_ikea_quotidien_um`
  - `sensor.prise_bureau_fer_a_repasser_nous_current`
  - `sensor.prise_bureau_fer_a_repasser_nous_power`
  - `sensor.prise_bureau_fer_a_repasser_nous_quotidien_um`
  - `sensor.prise_bureau_pc_ikea_current`
  - `sensor.prise_bureau_pc_ikea_power`
  - `sensor.prise_bureau_pc_ikea_quotidien_um`
  - `sensor.prise_congelateur_cuisine_nous_current`
  - `sensor.prise_congelateur_cuisine_nous_power`
  - `sensor.prise_congelateur_cuisine_nous_quotidien_um`
  - `sensor.prise_four_micro_ondes_nous_current`
  - `sensor.prise_four_micro_ondes_nous_power`
  - `sensor.prise_four_micro_ondes_nous_quotidien_um`
  - `sensor.prise_frigo_cuisine_nous_current`
  - `sensor.prise_frigo_cuisine_nous_power`
  - `sensor.prise_frigo_cuisine_nous_quotidien_um`
  - `sensor.prise_horloge_ikea_current`
  - `sensor.prise_horloge_ikea_power`
  - `sensor.prise_horloge_ikea_quotidien_um`
  - `sensor.prise_lave_linge_nous_current`
  - `sensor.prise_lave_linge_nous_power`
  - `sensor.prise_lave_linge_nous_quotidien_um`
  - `sensor.prise_lave_vaisselle_nous_current`
  - `sensor.prise_lave_vaisselle_nous_power`
  - `sensor.prise_lave_vaisselle_nous_quotidien_um`
  - `sensor.prise_pc_s_gege_ikea_current`
  - `sensor.prise_pc_s_gege_ikea_power`
  - `sensor.prise_pc_s_gege_ikea_quotidien_um`
  - `sensor.prise_petit_dejeune_nous_current`
  - `sensor.prise_petit_dejeune_nous_power`
  - `sensor.prise_petit_dejeune_nous_quotidien_um`
  - `sensor.prise_salon_chargeur_nous_current`
  - `sensor.prise_salon_chargeur_nous_power`
  - `sensor.prise_salon_chargeur_nous_quotidien_um`
  - `sensor.prise_seche_serviette_salle_de_bain_nous_power`
  - `sensor.prise_soufflant_salle_de_bain_nous_power`
  - `sensor.prise_tete_de_lit_chambre_current`
  - `sensor.prise_tete_de_lit_chambre_power`
  - `sensor.prise_tete_de_lit_chambre_quotidien_um`
  - `sensor.prise_tv_chambre_nous_current`
  - `sensor.prise_tv_chambre_nous_power`
  - `sensor.prise_tv_chambre_nous_quotidien_um`
  - `sensor.prise_tv_salon_ikea_current`
  - `sensor.prise_tv_salon_ikea_power`
  - `sensor.prise_tv_salon_ikea_quotidien_um`
  - `sensor.radiateur_elec_cuisine_power`
  - `sensor.relais_lumiere_sdb_sonoff_power`
  - `sensor.total_poste_autre_puissance`
  - `sensor.total_poste_chauffage_puissance`
  - `sensor.total_poste_cuisine_puissance`
  - `sensor.total_poste_froid_puissance`
  - `sensor.total_poste_hygiene_puissance`
  - `sensor.total_poste_multimedia_puissance`

- [📄 COULEURS PRISES PAR PIECE](Docs/docs_dashboard/docs/L2C1_ENERGIE/COULEURS_PRISES_PAR_PIECE.md)

---

## L2C2 — ÉNERGIE CLIM

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L2C2_ENERGIE_CLIM/L2C2_VIGNETTE_ENERGIE_CLIM.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L2C2_05_Energie_Clim/vignette_L2C2_energie_clim_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_TOTAL_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml)
  - `sensor.conso_clim_rad_total_mensuel`
  - `sensor.conso_clim_rad_total_quotidien`
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `climate.radiateur_cuisine`
  - `sensor.bureau_power_status`
  - `sensor.chambre_power_status`
  - `sensor.cuisine_power_status`
  - `sensor.salon_power_status`
  - `sensor.sdb_seche_serviette_etat`
  - `sensor.sdb_soufflant_etat`
- [`P1_UM_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml)
  - `sensor.clim_bureau_mensuel_um`
  - `sensor.clim_bureau_quotidien_um`
  - `sensor.clim_chambre_mensuel_um`
  - `sensor.clim_chambre_quotidien_um`
  - `sensor.clim_salon_mensuel_um`
  - `sensor.clim_salon_quotidien_um`
  - `sensor.radiateur_elec_cuisine_mensuel_um`
  - `sensor.radiateur_elec_cuisine_quotidien_um`
  - `sensor.seche_serviette_sdb_mensuel_um`
  - `sensor.seche_serviette_sdb_quotidien_um`
  - `sensor.soufflant_sdb_mensuel_um`
  - `sensor.soufflant_sdb_quotidien_um`
- *Entités natives HA / intégrations externes :*
  - `climate.clim_bureau_rm4_mini`
  - `climate.clim_chambre_rm4_mini`
  - `climate.clim_salon_rm4_mini`
  - `climate.soufflant_salle_de_bain`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L2C2_ENERGIE_CLIM/PAGE_ENERGIE_CLIM.md)
- [⚙️ YAML Page](Docs/Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_DUT_clim_chauffage.yaml`](Docs/docs_dashboard/TREE_CORRIGE/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml)
  - `sensor.dut_clim_bureau`
  - `sensor.dut_clim_chambre`
  - `sensor.dut_clim_salon`
  - `sensor.dut_radiateur_cuisine`
- [`P1_01_clim_logique_system_autom.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml)
  - `sensor.temperature_delta_affichage`
  - `sensor.temperature_moyenne_interieure`
- [`P1_AVG.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_AVG/P1_AVG.yaml)
  - `sensor.clim_bureau_avg_watts_mensuel`
  - `sensor.clim_bureau_avg_watts_quotidien`
  - `sensor.clim_chambre_avg_watts_mensuel`
  - `sensor.clim_chambre_avg_watts_quotidien`
  - `sensor.clim_salon_avg_watts_mensuel`
  - `sensor.clim_salon_avg_watts_quotidien`
  - `sensor.radiateur_elec_cuisine_avg_watts_mensuel`
  - `sensor.radiateur_elec_cuisine_avg_watts_quotidien`
  - `sensor.seche_serviette_sdb_avg_watts_mensuel`
  - `sensor.seche_serviette_sdb_avg_watts_quotidien`
  - `sensor.soufflant_sdb_avg_watts_mensuel`
  - `sensor.soufflant_sdb_avg_watts_quotidien`
- [`P1_AVG_TOTAL_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml)
  - `sensor.clim_rad_total_avg_watts_quotidien`
- [`P1_DUT_TOTAL_SDB.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml)
  - `sensor.dut_sdb_total`
- [`P1_TOTAL_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml)
  - `sensor.conso_clim_rad_total`
  - `sensor.conso_clim_rad_total_mensuel`
  - `sensor.conso_clim_rad_total_quotidien`
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `climate.radiateur_cuisine`
  - `sensor.bureau_power_status`
  - `sensor.bureau_power_status_affichage`
  - `sensor.chambre_power_status`
  - `sensor.chambre_power_status_affichage`
  - `sensor.cuisine_power_status`
  - `sensor.cuisine_power_status_affichage`
  - `sensor.salon_power_status`
  - `sensor.salon_power_status_affichage`
  - `sensor.sdb_power_status_affichage`
  - `sensor.sdb_seche_serviette_power_status`
  - `sensor.sdb_soufflant_power_status`
- [`M_04_tendances_th_ext_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml)
  - `sensor.th_balcon_nord_temperature`
- [`P1_UM_AMHQ.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml)
  - `sensor.clim_bureau_annuel_um`
  - `sensor.clim_bureau_hebdomadaire_um`
  - `sensor.clim_bureau_mensuel_um`
  - `sensor.clim_bureau_quotidien_um`
  - `sensor.clim_chambre_annuel_um`
  - `sensor.clim_chambre_hebdomadaire_um`
  - `sensor.clim_chambre_mensuel_um`
  - `sensor.clim_chambre_quotidien_um`
  - `sensor.clim_salon_annuel_um`
  - `sensor.clim_salon_hebdomadaire_um`
  - `sensor.clim_salon_mensuel_um`
  - `sensor.clim_salon_quotidien_um`
  - `sensor.radiateur_elec_cuisine_annuel_um`
  - `sensor.radiateur_elec_cuisine_hebdomadaire_um`
  - `sensor.radiateur_elec_cuisine_mensuel_um`
  - `sensor.radiateur_elec_cuisine_quotidien_um`
  - `sensor.seche_serviette_sdb_annuel_um`
  - `sensor.seche_serviette_sdb_hebdomadaire_um`
  - `sensor.seche_serviette_sdb_mensuel_um`
  - `sensor.seche_serviette_sdb_quotidien_um`
  - `sensor.soufflant_sdb_annuel_um`
  - `sensor.soufflant_sdb_hebdomadaire_um`
  - `sensor.soufflant_sdb_mensuel_um`
  - `sensor.soufflant_sdb_quotidien_um`
- *Entités natives HA / intégrations externes :*
  - `climate.clim_bureau_rm4_mini`
  - `climate.clim_chambre_rm4_mini`
  - `climate.clim_salon_rm4_mini`
  - `climate.soufflant_salle_de_bain`
  - `sensor.clim_bureau_nous_current`
  - `sensor.clim_bureau_nous_energy`
  - `sensor.clim_bureau_nous_power`
  - `sensor.clim_bureau_nous_voltage`
  - `sensor.clim_chambre_nous_current`
  - `sensor.clim_chambre_nous_energy`
  - `sensor.clim_chambre_nous_power`
  - `sensor.clim_chambre_nous_voltage`
  - `sensor.clim_salon_nous_current`
  - `sensor.clim_salon_nous_energy`
  - `sensor.clim_salon_nous_power`
  - `sensor.clim_salon_nous_voltage`
  - `sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power`
  - `sensor.prise_seche_serviette_salle_de_bain_nous_current`
  - `sensor.prise_seche_serviette_salle_de_bain_nous_energy`
  - `sensor.prise_seche_serviette_salle_de_bain_nous_power`
  - `sensor.prise_seche_serviette_salle_de_bain_nous_voltage`
  - `sensor.prise_soufflant_salle_de_bain_nous_current`
  - `sensor.prise_soufflant_salle_de_bain_nous_energy`
  - `sensor.prise_soufflant_salle_de_bain_nous_power`
  - `sensor.prise_soufflant_salle_de_bain_nous_voltage`
  - `sensor.radiateur_elec_cuisine_current`
  - `sensor.radiateur_elec_cuisine_energy`
  - `sensor.radiateur_elec_cuisine_power`
  - `sensor.radiateur_elec_cuisine_voltage`
  - `sensor.sdb_seche_serviettes_power_status_affichage`
  - `sensor.th_bureau_temperature`
  - `sensor.th_chambre_temperature`
  - `sensor.th_cuisine_temperature`
  - `sensor.th_salle_de_bain_temperature`
  - `sensor.th_salon_temperature`

#### Pop-up `#tendances`
- *(aucune entité détectée)*

---

## L2C3 — ÉNERGIE ÉCLAIRAGE

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/L2C3_VIGNETTE_ECLAIRAGE.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L2C3_06_Energie_Eclairage/vignette_L2C3_energie_eclairage_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`etats_status.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml)
  - `sensor.lumiere_appartement_etat`
  - `sensor.lumiere_bureau_etat`
  - `sensor.lumiere_chambre_etat`
  - `sensor.lumiere_cuisine_etat`
  - `sensor.lumiere_salle_de_bain_etat`
  - `sensor.lumiere_salon_etat`
- *Entités natives HA / intégrations externes :*
  - `sensor.eclairage_appart_2_mensuel_um_kwh_tpl`
  - `sensor.eclairage_appart_2_quotidien_um_kwh_tpl`
  - `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl`
  - `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl`
  - `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl`
  - `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl`
  - `sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl`
  - `sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl`
  - `sensor.eclairage_salon_5_mensuel_um_kwh_tpl`
  - `sensor.eclairage_salon_5_quotidien_um_kwh_tpl`
  - `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl`
  - `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl`
  - `sensor.eclairage_total_unit_mensuel_kwh_tpl`
  - `sensor.eclairage_total_unit_quotidien_kwh_tpl`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/PAGE_ENERGIE_ECLAIRAGE.md)
- [⚙️ YAML Page](Docs/Dashboard/L2C3_06_Energie_Eclairage/page_L2C3_energie_eclairage_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `light.bureau`
  - `light.chambre`
  - `light.cuisine`
  - `light.salon`
- [`P3_AVG_AMHQ_2_ZONE.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml)
  - `sensor.eclairage_appart_3_avg_watts_mensuel`
  - `sensor.eclairage_bureau_5_avg_watts_mensuel`
  - `sensor.eclairage_chambre_4_avg_watts_mensuel`
  - `sensor.eclairage_salon_5_avg_watts_mensuel`
  - `sensor.eclairage_sdb_2_avg_watts_mensuel`
- [`P3_UM_AMHQ_1_UNITE.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
  - `light.lampe_salle_de_bain_hue`
  - `sensor.hue_ambiance_lamp_salon_1_mensuel_um_kwh_tpl`
  - `sensor.hue_ambiance_lamp_salon_1_quotidien_um_kwh_tpl`
  - `sensor.hue_ambiance_lamp_salon_2_mensuel_um_kwh_tpl`
  - `sensor.hue_ambiance_lamp_salon_2_quotidien_um_kwh_tpl`
  - `sensor.hue_ambiance_lamp_salon_3_mensuel_um_kwh_tpl`
  - `sensor.hue_ambiance_lamp_salon_3_quotidien_um_kwh_tpl`
  - `sensor.hue_color_candle_chambre_eric_mensuel_um_kwh_tpl`
  - `sensor.hue_color_candle_chambre_eric_quotidien_um_kwh_tpl`
  - `sensor.hue_color_candle_chambre_gege_mensuel_um_kwh_tpl`
  - `sensor.hue_color_candle_chambre_gege_quotidien_um_kwh_tpl`
  - `sensor.hue_color_candle_salon_1_mensuel_um_kwh_tpl`
  - `sensor.hue_color_candle_salon_1_quotidien_um_kwh_tpl`
  - `sensor.hue_play_1_pc_bureau_mensuel_um_kwh_tpl`
  - `sensor.hue_play_1_pc_bureau_quotidien_um_kwh_tpl`
  - `sensor.hue_play_2_pc_bureau_mensuel_um_kwh_tpl`
  - `sensor.hue_play_2_pc_bureau_quotidien_um_kwh_tpl`
  - `sensor.hue_play_3_pc_bureau_mensuel_um_kwh_tpl`
  - `sensor.hue_play_3_pc_bureau_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_bureau_1_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_bureau_1_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_bureau_2_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_bureau_2_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_chambre_1_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_chambre_1_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_chambre_2_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_chambre_2_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_couloir_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_couloir_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_cuisine_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_cuisine_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_entree_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_entree_quotidien_um_kwh_tpl`
  - `sensor.hue_white_lamp_table_mensuel_um_kwh_tpl`
  - `sensor.hue_white_lamp_table_quotidien_um_kwh_tpl`
  - `sensor.lampe_salle_de_bain_hue_mensuel_um_kwh_tpl`
  - `sensor.lampe_salle_de_bain_hue_quotidien_um_kwh_tpl`
  - `sensor.relais_lumiere_sdb_sonoff_mensuel_um_kwh_tpl`
  - `sensor.relais_lumiere_sdb_sonoff_quotidien_um_kwh_tpl`
  - `switch.relais_lumiere_sdb_sonoff`
- *Entités natives HA / intégrations externes :*
  - `light.couloir`
  - `light.entree`
  - `light.lit`
  - `light.table`
  - `sensor.eclairage_appart_3_annuel_um_kwh_tpl`
  - `sensor.eclairage_appart_3_hebdomadaire_um_kwh_tpl`
  - `sensor.eclairage_appart_3_mensuel_um_kwh_tpl`
  - `sensor.eclairage_appart_3_quotidien_um_kwh_tpl`
  - `sensor.eclairage_bureau_5_annuel_um_kwh_tpl`
  - `sensor.eclairage_bureau_5_hebdomadaire_um_kwh_tpl`
  - `sensor.eclairage_bureau_5_mensuel_um_kwh_tpl`
  - `sensor.eclairage_bureau_5_quotidien_um_kwh_tpl`
  - `sensor.eclairage_chambre_4_annuel_um_kwh_tpl`
  - `sensor.eclairage_chambre_4_hebdomadaire_um_kwh_tpl`
  - `sensor.eclairage_chambre_4_mensuel_um_kwh_tpl`
  - `sensor.eclairage_chambre_4_quotidien_um_kwh_tpl`
  - `sensor.eclairage_salon_5_annuel_um_kwh_tpl`
  - `sensor.eclairage_salon_5_hebdomadaire_um_kwh_tpl`
  - `sensor.eclairage_salon_5_mensuel_um_kwh_tpl`
  - `sensor.eclairage_salon_5_quotidien_um_kwh_tpl`
  - `sensor.eclairage_sdb_2_annuel_um_kwh_tpl`
  - `sensor.eclairage_sdb_2_hebdomadaire_um_kwh_tpl`
  - `sensor.eclairage_sdb_2_mensuel_um_kwh_tpl`
  - `sensor.eclairage_sdb_2_quotidien_um_kwh_tpl`

- [📄 COULEURS ECLAIRAGE PAR PIECE](Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/COULEURS_ECLAIRAGE_PAR_PIECE.md)

---

## L3C1 — COMMANDES ÉCLAIRAGE

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/L3C1_VIGNETTE_ECLAIRAGE.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L3C1_07_Commandes_Eclairage/vignette_L3C1_eclairage_2026-05-13.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `light.chambre`
  - `light.cuisine`
  - `light.salon`
- [`etats_status.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml)
  - `sensor.bureau_etat`
  - `sensor.chambre_etat`
  - `sensor.lumiere_appartement_etat`
  - `sensor.lumiere_cuisine_etat`
  - `sensor.lumiere_ecran_etat`
  - `sensor.lumiere_salle_de_bain_etat`
  - `sensor.lumiere_salon_etat`
- [`P3_UM_AMHQ_1_UNITE.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
  - `light.hue_color_candle_chambre_eric`
  - `light.hue_color_candle_chambre_gege`
  - `light.lampe_salle_de_bain_hue`
- *Entités natives HA / intégrations externes :*
  - `light.couloir`
  - `light.entree`
  - `light.table`
  - `switch.prise_tete_de_lit_chambre`

### Pages (2)

#### Page Gauche

- [📄 Doc Page](Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md)
- [⚙️ YAML Page](Docs/Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_gauche_2026-05-13.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `light.cuisine`
  - `light.salon`
- [`etats_status.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml)
  - `sensor.lumiere_couloir_etat`
  - `sensor.lumiere_cuisine_etat`
  - `sensor.lumiere_entree_etat`
  - `sensor.lumiere_salon_etat`
  - `sensor.lumiere_table_etat`
- [`S_01_STORES.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml)
  - `cover.store_salon`
- *Entités natives HA / intégrations externes :*
  - `light.couloir`
  - `light.entree`
  - `light.table`
  - `sensor.th_cuisine_temperature`
  - `sensor.th_salon_temperature`

#### Page Droite

- [📄 Doc Page](Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md)
- [⚙️ YAML Page](Docs/Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-13.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- [`P1_ui_dashboard.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml)
  - `light.bureau`
  - `light.chambre`
- [`etats_status.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml)
  - `sensor.chambre_nb_allumes`
  - `sensor.lumiere_bureau_etat`
  - `sensor.lumiere_chambre_etat`
  - `sensor.lumiere_ecran_etat`
  - `sensor.lumiere_salle_de_bain_etat`
  - `sensor.lumiere_tete_de_lit_etat`
- [`S_01_STORES.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml)
  - `cover.store_bureau`
- [`P3_UM_AMHQ_1_UNITE.yaml`](Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml)
  - `light.hue_color_candle_chambre_eric`
  - `light.hue_color_candle_chambre_gege`
  - `light.hue_play_1_pc_bureau`
  - `light.hue_play_2_pc_bureau`
  - `light.hue_play_3_pc_bureau`
  - `light.hue_white_lamp_bureau_1`
  - `light.hue_white_lamp_bureau_2`
  - `light.lampe_salle_de_bain_hue`
  - `switch.relais_lumiere_sdb_sonoff`
- *Entités natives HA / intégrations externes :*
  - `light.lit`
  - `light.moniteur_pc`
  - `light.zone_eric`
  - `light.zone_gege`
  - `sensor.th_bureau_temperature`
  - `sensor.th_chambre_temperature`
  - `sensor.th_salle_de_bain_temperature`
  - `switch.ecran_p_c_3_play_hue`
  - `switch.prise_tete_de_lit_chambre`

##### Pop-up `#tete_de_lit`
- `light.hue_color_candle_chambre_eric`
- `light.hue_color_candle_chambre_gege`

##### Pop-up `#bureau`
- `light.bureau`

##### Pop-up `#ecranpc`
- `light.moniteur_pc`

---

## L3C2 — COMMANDES PRISES

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L3C2_PRISES/L3C2_VIGNETTE_PRISES.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L3C2_08_Commandes_Prises/vignette_L3C2_prises_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `light.hue_smart_eco_pc_bureau`
  - `light.hue_smart_eco_salon`
  - `light.hue_smart_eco_tv_chambre`
  - `switch.prise_horloge_ikea`
  - `switch.prise_tete_de_lit_chambre`
  - `switch.prise_tv_salon_ikea`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L3C2_PRISES/PAGE_PRISES.md)
- [⚙️ YAML Page](Docs/Dashboard/L3C2_08_Commandes_Prises/page_L3C2_prises_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `light.hue_smart_eco_pc_bureau`
  - `light.hue_smart_eco_salon`
  - `light.hue_smart_eco_tv_chambre`
  - `switch.prise_horloge_ikea`
  - `switch.prise_tete_de_lit_chambre`
  - `switch.prise_tv_salon_ikea`

---

## L3C3 — STORES & FENÊTRES

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L3C3_STORES/L3C3_VIGNETTE_STORES.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L3C3_09_Stores_Fenetres/vignette_L3C3_stores_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`S_01_STORES.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml)
  - `sensor.store_bureau_status`
  - `sensor.store_salon_status`
- *Entités natives HA / intégrations externes :*
  - `binary_sensor.contact_fenetre_bureau_sonoff_contact`
  - `binary_sensor.contact_fenetre_chambre_sonoff_contact`
  - `binary_sensor.contact_fenetre_cuisine_sonoff_contact`
  - `binary_sensor.contact_fenetre_salon_sonoff_contact`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L3C3_STORES/PAGE_STORES.md)
- [⚙️ YAML Page](Docs/Dashboard/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`S_01_STORES.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml)
  - `cover.store_bureau`
  - `cover.store_salon`
  - `sensor.store_bureau_status`
  - `sensor.store_salon_status`
- [`M_04_tendances_th_ext_card.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml)
  - `sensor.th_balcon_nord_temperature`
- *Entités natives HA / intégrations externes :*
  - `binary_sensor.contact_fenetre_bureau_sonoff_contact`
  - `binary_sensor.contact_fenetre_salon_sonoff_contact`
  - `light.store_bureau_dnd`
  - `light.store_salon_dnd`
  - `sensor.contact_fenetre_bureau_sonoff_battery`
  - `sensor.contact_fenetre_salon_sonoff_battery`
  - `sensor.store_bureau_signal_strength`
  - `sensor.store_salon_signal_strength`

---

## L4C1 — PROXMOX (PVE)

> ⚠️ En cours : page non pushée. Doc vignette à créer.

### Vignette

- *(📄 Doc Vignette — à créer)*
- [⚙️ YAML Vignette](Docs/Dashboard/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-05-17.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `binary_sensor.pve_status`
  - `sensor.pve_memory_usage_percentage`
  - `sensor.pve_utilisation_du_processeur`
  - `sensor.storage_local_storage_usage_percentage`
  - `sensor.temperature_cpu_package`

---

## L4C2 — MINI PC (NUC)

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-05-10.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.prise_mini_pc_ikea_power`
  - `sensor.system_monitor_utilisation_de_la_memoire`
  - `sensor.system_monitor_utilisation_du_disque`
  - `sensor.system_monitor_utilisation_du_processeur`
  - `sensor.temperature_cpu_package`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L4C2_MINI_PC/PAGE_MINI_PC.md)
- [⚙️ YAML Page](Docs/Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`P2_AVG_AMHQ_mini_pc.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml)
  - `sensor.mini_pc_avg_watts_mensuel`
  - `sensor.mini_pc_avg_watts_quotidien`
- *Entités natives HA / intégrations externes :*
  - `sensor.cpu_speed`
  - `sensor.prise_mini_pc_ikea_current`
  - `sensor.prise_mini_pc_ikea_energy`
  - `sensor.prise_mini_pc_ikea_mensuel_um`
  - `sensor.prise_mini_pc_ikea_power`
  - `sensor.prise_mini_pc_ikea_quotidien_um`
  - `sensor.system_monitor_charge_15m`
  - `sensor.system_monitor_charge_1m`
  - `sensor.system_monitor_charge_5m`
  - `sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18`
  - `sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18`
  - `sensor.system_monitor_espace_utilise`
  - `sensor.system_monitor_memoire_libre`
  - `sensor.system_monitor_memoire_utilisee`
  - `sensor.system_monitor_utilisation_de_la_memoire`
  - `sensor.system_monitor_utilisation_du_disque`
  - `sensor.system_monitor_utilisation_du_processeur`
  - `sensor.temperature_carte_mere`
  - `sensor.temperature_core_0`
  - `sensor.temperature_core_1`
  - `sensor.temperature_core_2`
  - `sensor.temperature_core_3`
  - `sensor.temperature_cpu_package`

#### Pop-up `#speed`
- `sensor.system_monitor_utilisation_du_processeur`

#### Pop-up `#temp`
- `sensor.temperature_cpu_package`

#### Pop-up `#conso`
- `sensor.mini_pc_avg_watts_mensuel`
- `sensor.mini_pc_avg_watts_quotidien`
- `sensor.prise_mini_pc_ikea_current`
- `sensor.prise_mini_pc_ikea_energy`
- `sensor.prise_mini_pc_ikea_mensuel_um`
- `sensor.prise_mini_pc_ikea_power`
- `sensor.prise_mini_pc_ikea_quotidien_um`

#### Pop-up `#disk`
- `sensor.system_monitor_espace_utilise`

#### Pop-up `#memory`
- `sensor.system_monitor_memoire_utilisee`

- [📄 PAGE RASPI](Docs/docs_dashboard/docs/L4C2_MINI_PC/PAGE_RASPI.md)

---

## L4C3 — MISES À JOUR HA

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L4C3_MAJ_HA/L4C3_VIGNETTE_MAJ.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L4C3_12_MAJ_HA/vignette_L4C3_maj_ha_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`Mise_a_jour_home_assistant.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/utilitaires/Mise_a_jour_home_assistant.yaml)
  - `sensor.available_updates`

### Pages (2)

#### Page Gauche

- [📄 Doc Page](Docs/docs_dashboard/docs/L4C3_MAJ_HA/PAGE_MAJ.md)
- [⚙️ YAML Page](Docs/Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_gauche_2026-05-14.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `update.hacs_update`
  - `update.home_assistant_core_update`
  - `update.home_assistant_operating_system_update`
  - `update.home_assistant_supervisor_update`

#### Page Droite

- [📄 Doc Page](Docs/docs_dashboard/docs/L4C3_MAJ_HA/PAGE_MAJ.md)
- [⚙️ YAML Page](Docs/Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_droite_2026-05-14.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.home_assistant_core_cpu_percent`
  - `sensor.home_assistant_core_memory_percent`
  - `sensor.home_assistant_supervisor_cpu_percent`
  - `sensor.home_assistant_supervisor_memory_percent`
  - `update.hacs_update`
  - `update.home_assistant_core_update`
  - `update.home_assistant_supervisor_update`

---

## L5C1 — PILES & BATTERIES

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L5C1_PILES_BATTERIES/L5C1_VIGNETTE_BATTERIES.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L5C1_13_Batteries_Piles/vignette_L5C1_batteries_piles_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `group.hue_devices`
  - `group.ikea_devices`
  - `group.sonoff_devices`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L5C1_PILES_BATTERIES/PAGE_BATTERIES.md)
- [⚙️ YAML Page](Docs/Dashboard/L5C1_13_Batteries_Piles/page_L5C1_batteries_piles_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.boutton_salle_de_bain_hue_battery`
  - `sensor.contact_fenetre_bureau_sonoff_battery`
  - `sensor.contact_fenetre_chambre_sonoff_battery`
  - `sensor.contact_fenetre_cuisine_sonoff_battery`
  - `sensor.contact_fenetre_salon_sonoff_battery`
  - `sensor.detecteur_de_fuite_ikea_battery`
  - `sensor.detecteur_vallhorn_battery`
  - `sensor.hue_smart_button_bureau_batterie`
  - `sensor.hue_smart_button_chambre_batterie`
  - `sensor.hue_smart_button_chambre_eric_batterie`
  - `sensor.hue_smart_button_chambre_gege_batterie`
  - `sensor.hue_smart_button_couloir_batterie`
  - `sensor.hue_smart_button_cuisine_batterie`
  - `sensor.hue_smart_button_eco_batterie`
  - `sensor.hue_smart_button_entee_1_batterie`
  - `sensor.hue_smart_button_entee_2_batterie`
  - `sensor.hue_smart_button_table_batterie`
  - `sensor.inter_bureau_rodret_battery`
  - `sensor.inter_radiateur_salle_de_bain_ikea_rodret_battery`
  - `sensor.inter_salon_4_ikea_battery`
  - `sensor.inter_somrig_battery`
  - `sensor.inter_tv_chambre_ikea_rodret_battery`
  - `sensor.poussoir_ikea_tradfri_battery`
  - `sensor.th_balcon_nord_battery`
  - `sensor.th_bureau_battery`
  - `sensor.th_cellier_battery`
  - `sensor.th_chambre_battery`
  - `sensor.th_cuisine_battery`
  - `sensor.th_salle_de_bain_battery`
  - `sensor.th_salon_battery`

---

## L5C2 — BATTERIES PORTABLES

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/L5C2_VIGNETTE_BATTERIES_PORTABLES.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L5C2_14_Batteries_Portables/vignette_L5C2_batteries_portables_2026-05-12.yaml)

### Pages (2)

#### Page Gauche

- [📄 Doc Page](Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md)
- [⚙️ YAML Page](Docs/Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_gauche_2026-05-12.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.eric_battery_health`
  - `sensor.eric_battery_level`
  - `sensor.eric_battery_state`
  - `sensor.eric_battery_temperature`
  - `sensor.eric_charger_type`
  - `sensor.eric_network_type`
  - `sensor.eric_wi_fi_connection`
  - `sensor.ne2213_eric_battery_health`
  - `sensor.ne2213_eric_battery_level`
  - `sensor.ne2213_eric_battery_state`
  - `sensor.ne2213_eric_battery_temperature`
  - `sensor.ne2213_eric_charger_type`
  - `sensor.ne2213_eric_network_type`
  - `sensor.ne2213_eric_wi_fi_connection`
  - `sensor.sm_a530f_battery_health`
  - `sensor.sm_a530f_battery_level`
  - `sensor.sm_a530f_battery_state`
  - `sensor.sm_a530f_battery_temperature`
  - `sensor.sm_a530f_charger_type`
  - `sensor.sm_a530f_network_type`
  - `sensor.sm_a530f_wi_fi_connection`
  - `sensor.tablette_battery_health`
  - `sensor.tablette_battery_level`
  - `sensor.tablette_battery_state`
  - `sensor.tablette_battery_temperature`
  - `sensor.tablette_charger_type`
  - `sensor.tablette_network_type`
  - `sensor.tablette_wi_fi_connection`

#### Page Droite

- [📄 Doc Page](Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md)
- [⚙️ YAML Page](Docs/Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_droite_2026-05-12.yaml)

#####  Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.gm1901_battery_health`
  - `sensor.gm1901_battery_level`
  - `sensor.gm1901_battery_state`
  - `sensor.gm1901_battery_temperature`
  - `sensor.gm1901_charger_type`
  - `sensor.gm1901_network_type`
  - `sensor.gm1901_wi_fi_connection`
  - `sensor.mamour_battery_health`
  - `sensor.mamour_battery_level`
  - `sensor.mamour_battery_state`
  - `sensor.mamour_battery_temperature`
  - `sensor.mamour_charger_type`
  - `sensor.mamour_network_type`
  - `sensor.mamour_wi_fi_connection`
  - `sensor.ne2213_mamour_battery_health`
  - `sensor.ne2213_mamour_battery_level`
  - `sensor.ne2213_mamour_battery_state`
  - `sensor.ne2213_mamour_battery_temperature`
  - `sensor.ne2213_mamour_charger_type`
  - `sensor.ne2213_mamour_network_type`
  - `sensor.ne2213_mamour_wi_fi_connection`

---

## L5C3 — MARIADB

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L5C3_MARIADB/L5C3_VIGNETTE_MARIADB.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L5C3_15_MariaDB/vignette_L5C3_mariadb_2026-05-10.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.taille_db_home_assistant`

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L5C3_MARIADB/PAGE_SYSTEME.md)
- [⚙️ YAML Page](Docs/Dashboard/L5C3_15_MariaDB/page_L5C3_mariadb_2026-05-10.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `automation.db_purge_mariadb_repack`
  - `sensor.backup_github_status`
  - `sensor.git_last_weekly_tag`
  - `sensor.github_default_branch`
  - `sensor.taille_db_home_assistant`

---

## L6C1 — QUALITÉ AIR (APPART)

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L6C1_AIR_QUALITE/L6C1_VIGNETTE_AIR_QUALITE.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L6C1_16_Air_Qualite/vignette_L6C1_air_qualite_2026-05-14.yaml)

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L6C1_AIR_QUALITE/PAGE_AIR_QUALITE.md)
- [⚙️ YAML Page](Docs/Dashboard/L6C1_16_Air_Qualite/page_L6C1_air_qualite_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- [`A_01_AIR_QUALITY.yaml`](Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml)
  - `sensor.pm2_5_bureau_moy_24h`
  - `sensor.pm2_5_chambre_moy_24h`
  - `sensor.pm2_5_salon_moy_24h`
  - `sensor.tcov_bureau_moy_24h`
  - `sensor.tcov_chambre_moy_24h`
  - `sensor.tcov_salon_moy_24h`
- [`A_01_AIR_QUALITY.yaml`](Docs/docs_dashboard/TREE_CORRIGE/templates/Air_quality/A_01_AIR_QUALITY.yaml)
  - `sensor.tcov_bureau_ppb`
  - `sensor.tcov_chambre_ppb`
  - `sensor.tcov_salon_ppb`
- *Entités natives HA / intégrations externes :*
  - `sensor.qualite_air_bureau_ikea_pm25`
  - `sensor.qualite_air_chambre_ikea_pm25`
  - `sensor.qualite_air_salon_ikea_pm25`

#### Pop-up `#spm25`
- `sensor.pm2_5_salon_moy_24h`

#### Pop-up `#scov`
- `sensor.qualite_air_bureau_ikea_pm25`
- `sensor.tcov_bureau_ppb`
- `sensor.tcov_salon_moy_24h`

#### Pop-up `#bpm25`
- `sensor.pm2_5_bureau_moy_24h`

#### Pop-up `#bcov`
- `sensor.qualite_air_chambre_ikea_pm25`
- `sensor.tcov_bureau_moy_24h`
- `sensor.tcov_chambre_ppb`

#### Pop-up `#cpm25`
- `sensor.pm2_5_chambre_moy_24h`

#### Pop-up `#ccov`
- `sensor.tcov_chambre_moy_24h`

---

## L6C2 — POLLUTION & POLLEN

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L6C2_POLLUTION_POLLEN/L6C2_VIGNETTE_POLLUTION_POLLEN.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L6C2_17_Pollution_Pollen/vignette_L6C2_pollution_pollen_2026-05-14.yaml)

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L6C2_POLLUTION_POLLEN/PAGE_POLLUTION_POLLEN.md)
- [⚙️ YAML Page](Docs/Dashboard/L6C2_17_Pollution_Pollen/page_L6C2_pollution_pollen_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.concentration_ambroisie_vence`
  - `sensor.concentration_armoise_vence`
  - `sensor.concentration_aulne_vence`
  - `sensor.concentration_bouleau_vence`
  - `sensor.concentration_gramine_vence`
  - `sensor.concentration_olivier_vence`
  - `sensor.dioxyde_d_azote_vence`
  - `sensor.dioxyde_de_soufre_vence`
  - `sensor.niveau_ambroisie_vence`
  - `sensor.niveau_armoise_vence`
  - `sensor.niveau_aulne_vence`
  - `sensor.niveau_bouleau_vence`
  - `sensor.niveau_gramine_vence`
  - `sensor.niveau_olivier_vence`
  - `sensor.ozone_vence`
  - `sensor.pm10_vence`
  - `sensor.pm25_vence`
  - `sensor.qualite_globale_pollen_vence`
  - `sensor.qualite_globale_vence`

---

## L6C3 — VIGILANCE EAU

### Vignette

- [📄 Doc Vignette](Docs/docs_dashboard/docs/L6C3_VIGIEAU/L6C3_VIGNETTE_VIGIEAU.md)
- [⚙️ YAML Vignette](Docs/Dashboard/L6C3_18_VigiEau/vignette_L6C3_vigieau_2026-05-14.yaml)

### Page

- [📄 Doc Page](Docs/docs_dashboard/docs/L6C3_VIGIEAU/PAGE_VIGIEAU.md)
- [⚙️ YAML Page](Docs/Dashboard/L6C3_18_VigiEau/page_L6C3_vigieau_2026-05-14.yaml)

#### Fichiers sources (TREE_CORRIGE)
- *Entités natives HA / intégrations externes :*
  - `sensor.alert_level_in_vence`
  - `sensor.alert_level_in_vence_numeric`
  - `this.entity_id`

---

*Dernière mise à jour : 2026-05-30*
