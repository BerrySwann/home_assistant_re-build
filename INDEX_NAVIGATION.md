# 📇 INDEX NAVIGATION — Dashboard HA

*Navigation complète des 18 vignettes — Accès direct aux docs, YAML, entités et pop-ups*<br>
*Chemins relatifs depuis la racine du repo GitHub `home_assistant_re-build`*

---

<details>
<summary><b>L1C1 — MÉTÉO</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~40 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C1_METEO/L1C1_VIGNETTE_METEO.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L1C1_01_Meteo/vignette_L1C1_meteo_2026-05-16.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 3 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C1_METEO/PAGE_METEO.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L1C1_01_Meteo/page_L1C1_meteo_2026-05-09.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>M_01_meteo_alertes_card.yaml</code> — 10 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.alerte_avalanches</code></li>
<li><code>sensor.alerte_canicule</code></li>
<li><code>sensor.alerte_grand_froid</code></li>
<li><code>sensor.alerte_inondation</code></li>
<li><code>sensor.alerte_meteo</code></li>
<li><code>sensor.alerte_neige_verglas</code></li>
<li><code>sensor.alerte_orages</code></li>
<li><code>sensor.alerte_pluie_inondation</code></li>
<li><code>sensor.alerte_vagues_submersion</code></li>
<li><code>sensor.alerte_vent_violent</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_vent_vence_card.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.vence_wind_speed</code></li>
<li><code>weather.vence</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_blitzortung.yaml</code> — 4 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dernier_impact_temps_reel</code></li>
<li><code>sensor.lightning_bearing</code></li>
<li><code>sensor.lightning_direction_label</code></li>
<li><code>sensor.lightning_distance_km</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_05_cycle_solaire.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code></li>
<li><code>sensor.tendance_duree_jour</code></li>
<li><code>sensor.variation_quotidienne</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (20)</i></summary>
<blockquote><ul>
<li><code>camera.mf_alerte_today</code></li>
<li><code>camera.mf_alerte_tomorrow</code></li>
<li><code>sensor.06_weather_alert</code></li>
<li><code>sensor.direction_du_vent_vence</code></li>
<li><code>sensor.direction_du_vent_vence_label</code></li>
<li><code>sensor.eclairs_annuel</code></li>
<li><code>sensor.eclairs_hebdomadaire</code></li>
<li><code>sensor.eclairs_horaire</code></li>
<li><code>sensor.eclairs_mensuel</code></li>
<li><code>sensor.eclairs_quotidien</code></li>
<li><code>sensor.maison_lightning_counter</code></li>
<li><code>sensor.maison_lightning_distance</code></li>
<li><code>sensor.moon_phase</code></li>
<li><code>sensor.season</code></li>
<li><code>sensor.vence_daily_precipitation</code></li>
<li><code>sensor.vence_pressure</code></li>
<li><code>sensor.vence_uv</code></li>
<li><code>sensor.vence_wind_gust</code></li>
<li><code>sensor.vitesse_du_vent_vence</code></li>
<li><code>sun.sun</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#foudre</code> — 11 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.dernier_impact_temps_reel</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclairs_annuel</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_hebdomadaire</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_horaire</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_mensuel</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_quotidien</code> — <i>Natif HA</i></li>
<li><code>sensor.lightning_bearing</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_direction_label</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_distance_km</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.maison_lightning_counter</code> — <i>Natif HA</i></li>
<li><code>sensor.maison_lightning_distance</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#alert</code> — 13 entité(s)</summary>
<blockquote><ul>
<li><code>camera.mf_alerte_today</code> — <i>Natif HA</i></li>
<li><code>camera.mf_alerte_tomorrow</code> — <i>Natif HA</i></li>
<li><code>sensor.06_weather_alert</code> — <i>Natif HA</i></li>
<li><code>sensor.alerte_avalanches</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_canicule</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_grand_froid</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_inondation</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_meteo</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_neige_verglas</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_orages</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_pluie_inondation</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vagues_submersion</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vent_violent</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#sun</code> — 6 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sensor.moon_phase</code> — <i>Natif HA</i></li>
<li><code>sensor.season</code> — <i>Natif HA</i></li>
<li><code>sensor.tendance_duree_jour</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sensor.variation_quotidienne</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sun.sun</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C1_METEO/TUTO_IMAGES_ALERTES_METEO_FRANCE.md">Tuto Images Alertes Météo France</a><br>
⚙️ <a href="Docs/Dashboard/L1C1_01_Meteo/card_duree_du_jour_2026-05-03.yaml">Card Durée du Jour</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L1C2 — TEMPÉRATURES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~41 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C2_TEMPERATURES/L1C2_VIGNETTE_TEMPERATURES.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L1C2_02_Temperatures/vignette_L1C2_temperatures_2026-05-12.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (12)</i></summary>
<blockquote><ul>
<li><code>sensor.th_bureau_humidity</code></li>
<li><code>sensor.th_bureau_temperature</code></li>
<li><code>sensor.th_cellier_humidity</code></li>
<li><code>sensor.th_cellier_temperature</code></li>
<li><code>sensor.th_chambre_humidity</code></li>
<li><code>sensor.th_chambre_temperature</code></li>
<li><code>sensor.th_cuisine_humidity</code></li>
<li><code>sensor.th_cuisine_temperature</code></li>
<li><code>sensor.th_salle_de_bain_humidity</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>sensor.th_salon_humidity</code></li>
<li><code>sensor.th_salon_temperature</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 10 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C2_TEMPERATURES/PAGE_TEMPERATURES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L1C2_02_Temperatures/page_L1C2_temperatures_2026-05-12.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG_TOTAL_AMHQ.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_rad_total_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 7 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.sdb_seche_serviette_power_status</code></li>
<li><code>sensor.sdb_soufflant_power_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_vent_vence_card.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>weather.vence</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_UM_AMHQ.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.radiateur_elec_cuisine</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (21)</i></summary>
<blockquote><ul>
<li><code>climate.clim_du_bureau</code></li>
<li><code>sensor.th_balcon_nord_battery</code></li>
<li><code>sensor.th_bureau_battery</code></li>
<li><code>sensor.th_bureau_humidity</code></li>
<li><code>sensor.th_bureau_temperature</code></li>
<li><code>sensor.th_cellier_battery</code></li>
<li><code>sensor.th_cellier_humidity</code></li>
<li><code>sensor.th_cellier_temperature</code></li>
<li><code>sensor.th_chambre_battery</code></li>
<li><code>sensor.th_chambre_humidity</code></li>
<li><code>sensor.th_chambre_temperature</code></li>
<li><code>sensor.th_cuisine_battery</code></li>
<li><code>sensor.th_cuisine_humidity</code></li>
<li><code>sensor.th_cuisine_temperature</code></li>
<li><code>sensor.th_salle_de_bain_battery</code></li>
<li><code>sensor.th_salle_de_bain_humidity</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>sensor.th_salon_battery</code></li>
<li><code>sensor.th_salon_humidity</code></li>
<li><code>sensor.th_salon_temperature</code></li>
<li><code>sensor.vence_temperature</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#tendances</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#exterieur</code> — 2 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
<li><code>weather.vence</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#salon</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_salon_temperature</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#cellier</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_cellier_temperature</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#cuisine</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_cuisine_temperature</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bureau</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_bureau_temperature</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#salle_de_bain</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_salle_de_bain_temperature</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#chambre</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_chambre_temperature</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#tcourbe</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#hcourbe</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L1C3 — COMMANDES CLIM</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~61 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C3_CLIM/L1C3_VIGNETTE_CLIM.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-05-13.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.delta_ademe_recommande</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 14 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.clim_bureau_etat</code></li>
<li><code>sensor.clim_chambre_etat</code></li>
<li><code>sensor.clim_salon_etat</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.mode_ete_hiver_etat</code></li>
<li><code>sensor.radiateur_cuisine_etat</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.sdb_seche_serviette_etat</code></li>
<li><code>sensor.sdb_seche_serviette_power_status</code></li>
<li><code>sensor.sdb_soufflant_etat</code></li>
<li><code>sensor.sdb_soufflant_power_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (1)</i></summary>
<blockquote><ul>
<li><code>climate.soufflant_salle_de_bain</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 1 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C3_CLIM/PAGE_CLIM.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-05-13.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_BV_01_SW_inter_souflant_sdb.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Inter_BP_Virtuel/P1/P1_BV_01_SW_inter_souflant_sdb.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 12 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.bureau_power_status_affichage</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.chambre_power_status_affichage</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.cuisine_power_status_affichage</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.salon_power_status_affichage</code></li>
<li><code>sensor.sdb_power_status_affichage</code></li>
<li><code>sensor.sdb_seche_serviette_power_status</code></li>
<li><code>sensor.sdb_soufflant_power_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_UM_AMHQ.yaml</code> — 5 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>remote.clim_bureau</code></li>
<li><code>remote.clim_chambre</code></li>
<li><code>remote.clim_salon</code></li>
<li><code>remote.soufflant_sdb</code></li>
<li><code>switch.radiateur_elec_cuisine</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (29)</i></summary>
<blockquote><ul>
<li><code>climate.soufflant_salle_de_bain</code></li>
<li><code>input_boolean.clim_bureau_arret_securise_en_cours</code></li>
<li><code>input_boolean.clim_chambre_arret_securise_en_cours</code></li>
<li><code>input_boolean.clim_salon_arret_securise_en_cours</code></li>
<li><code>input_select.etat_resistance_soufflant_sdb</code></li>
<li><code>sensor.bureau_power_lock</code></li>
<li><code>sensor.chambre_power_lock</code></li>
<li><code>sensor.clim_bureau_nous_power</code></li>
<li><code>sensor.clim_chambre_nous_power</code></li>
<li><code>sensor.clim_salon_nous_power</code></li>
<li><code>sensor.prise_soufflant_salle_de_bain_nous_power</code></li>
<li><code>sensor.radiateur_elec_cuisine_power</code></li>
<li><code>sensor.salon_power_lock</code></li>
<li><code>sensor.sdb_seche_serviette_status_affichage</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>switch.clim_bureau_nous</code></li>
<li><code>switch.clim_chambre_nous</code></li>
<li><code>switch.clim_salon_nous</code></li>
<li><code>switch.prise_soufflant_salle_de_bain_nous</code></li>
<li><code>switch.schedule_clim_de_la_chambre_week</code></li>
<li><code>switch.schedule_clim_de_la_chambre_week_end</code></li>
<li><code>switch.schedule_clim_du_bureau_week</code></li>
<li><code>switch.schedule_clim_du_bureau_week_end</code></li>
<li><code>switch.schedule_clim_du_salon_week</code></li>
<li><code>switch.schedule_clim_du_salon_week_end</code></li>
<li><code>switch.schedule_radiateur_cuisine_week</code></li>
<li><code>switch.schedule_radiateur_cuisine_week_end</code></li>
<li><code>switch.schedule_soufflant_salle_de_bain_week</code></li>
<li><code>switch.schedule_soufflant_salle_de_bain_week_end</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#calcul</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L2C1 — ÉNERGIE GÉNÉRALE</b> &nbsp;|&nbsp; 3 page(s) &nbsp;|&nbsp; ~197 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/vignette_L2C1_energie_2026-05-12.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P0_MINI_MAXI_AVG_Genelec_appart.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_conso_maxi_24h</code></li>
<li><code>sensor.genelec_appart_conso_mini_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>01_genelec_appart_AMHQ_cost.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_cout_hc_quotidien</code></li>
<li><code>sensor.genelec_appart_cout_hp_quotidien</code></li>
<li><code>sensor.genelec_appart_cout_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (1)</i></summary>
<blockquote><ul>
<li><code>sensor.general_electric_appart_power</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Principale</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-05-12.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P0_kWh_genelec_appart.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart/P0_kWh_genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_totale_kwh</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P0_MINI_MAXI_AVG_Genelec_appart.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_conso_maxi_24h</code></li>
<li><code>sensor.genelec_appart_conso_mini_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>diag_conso_hebdomadaire_en_cours.yaml</code> — 7 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/diag_conso_hebdomadaire_en_cours.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.diag_poste_autre_hebdomadaire</code></li>
<li><code>sensor.diag_poste_chauffage_hebdomadaire</code></li>
<li><code>sensor.diag_poste_cuisine_hebdomadaire</code></li>
<li><code>sensor.diag_poste_eclairage_hebdomadaire</code></li>
<li><code>sensor.diag_poste_froid_hebdomadaire</code></li>
<li><code>sensor.diag_poste_hygiene_hebdomadaire</code></li>
<li><code>sensor.diag_poste_multimedia_hebdomadaire</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>diag_conso_jour_en_cours.yaml</code> — 7 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.diag_poste_autre_quotidien</code></li>
<li><code>sensor.diag_poste_chauffage_quotidien</code></li>
<li><code>sensor.diag_poste_cuisine_quotidien</code></li>
<li><code>sensor.diag_poste_eclairage_quotidien</code></li>
<li><code>sensor.diag_poste_froid_quotidien</code></li>
<li><code>sensor.diag_poste_hygiene_quotidien</code></li>
<li><code>sensor.diag_poste_multimedia_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>diag_conso_mois_en_cours.yaml</code> — 7 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.diag_poste_autre_mensuel</code></li>
<li><code>sensor.diag_poste_chauffage_mensuel</code></li>
<li><code>sensor.diag_poste_cuisine_mensuel</code></li>
<li><code>sensor.diag_poste_eclairage_mensuel</code></li>
<li><code>sensor.diag_poste_froid_mensuel</code></li>
<li><code>sensor.diag_poste_hygiene_mensuel</code></li>
<li><code>sensor.diag_poste_multimedia_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>01_genelec_appart_AMHQ_cost.yaml</code> — 9 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_cout_hc_hebdomadaire</code></li>
<li><code>sensor.genelec_appart_cout_hc_mensuel</code></li>
<li><code>sensor.genelec_appart_cout_hc_quotidien</code></li>
<li><code>sensor.genelec_appart_cout_hp_hebdomadaire</code></li>
<li><code>sensor.genelec_appart_cout_hp_mensuel</code></li>
<li><code>sensor.genelec_appart_cout_hp_quotidien</code></li>
<li><code>sensor.genelec_appart_cout_total_hebdomadaire</code></li>
<li><code>sensor.genelec_appart_cout_total_mensuel</code></li>
<li><code>sensor.genelec_appart_cout_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>02_ratio_hp_hc.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_ratio_hc_hebdomadaire</code></li>
<li><code>sensor.genelec_appart_ratio_hc_mensuel</code></li>
<li><code>sensor.genelec_appart_ratio_hc_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>03_AVG_genelec_appart.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Genelec_appart/03_AVG_genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_avg_watts_mensuel</code></li>
<li><code>sensor.genelec_appart_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>MyElectricalData.yaml</code> — 8 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.linky_jour_0</code></li>
<li><code>sensor.linky_jour_1</code></li>
<li><code>sensor.linky_jour_2</code></li>
<li><code>sensor.linky_jour_3</code></li>
<li><code>sensor.linky_jour_4</code></li>
<li><code>sensor.linky_jour_5</code></li>
<li><code>sensor.linky_jour_6</code></li>
<li><code>sensor.linky_jour_7</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>01_kWh_UM_AMHQ.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P0_Energie_total/Genelec_appart/01_kWh_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_quotidien_kwh_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>02_UM_AMHQ.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P0_Energie_total/Genelec_appart/02_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_hebdomadaire_um</code></li>
<li><code>sensor.genelec_appart_mensuel_um</code></li>
<li><code>sensor.genelec_appart_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>03_UM_genelec_appart_HPHC_AMHQ.yaml</code> — 6 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P0_Energie_total/Genelec_appart/03_UM_genelec_appart_HPHC_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_hphc_hebdomadaire_um_hc</code></li>
<li><code>sensor.genelec_appart_hphc_hebdomadaire_um_hp</code></li>
<li><code>sensor.genelec_appart_hphc_mensuel_um_hc</code></li>
<li><code>sensor.genelec_appart_hphc_mensuel_um_hp</code></li>
<li><code>sensor.genelec_appart_hphc_quotidien_um_hc</code></li>
<li><code>sensor.genelec_appart_hphc_quotidien_um_hp</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (4)</i></summary>
<blockquote><ul>
<li><code>sensor.general_electric_appart_energy</code></li>
<li><code>sensor.general_electric_appart_power</code></li>
<li><code>sensor.linky_25481620821301_consumption</code></li>
<li><code>sensor.linky_25481620821301_consumption_history</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Mensuel</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE_MENSUEL.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_mensuel_2026-05-12.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P2_AVG_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.airfryer_avg_watts_mensuel</code></li>
<li><code>sensor.box_internet_avg_watts_mensuel</code></li>
<li><code>sensor.chargeurs_salon_avg_watts_mensuel</code></li>
<li><code>sensor.congelateur_avg_watts_mensuel</code></li>
<li><code>sensor.fer_repasser_avg_watts_mensuel</code></li>
<li><code>sensor.four_mo_avg_watts_mensuel</code></li>
<li><code>sensor.frigo_avg_watts_mensuel</code></li>
<li><code>sensor.horloge_avg_watts_mensuel</code></li>
<li><code>sensor.lave_linge_avg_watts_mensuel</code></li>
<li><code>sensor.lave_vaisselle_avg_watts_mensuel</code></li>
<li><code>sensor.pc_bureau_avg_watts_mensuel</code></li>
<li><code>sensor.pc_gege_avg_watts_mensuel</code></li>
<li><code>sensor.petit_dej_avg_watts_mensuel</code></li>
<li><code>sensor.plaques_cuisson_avg_watts_mensuel</code></li>
<li><code>sensor.tetes_lit_avg_watts_mensuel</code></li>
<li><code>sensor.tv_chambre_avg_watts_mensuel</code></li>
<li><code>sensor.tv_salon_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_AVG_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.four_et_plaque_de_cuisson_mensuel_um</code></li>
<li><code>sensor.prise_airfryer_ninja_nous_mensuel_um</code></li>
<li><code>sensor.prise_box_internet_ikea_mensuel_um</code></li>
<li><code>sensor.prise_bureau_fer_a_repasser_nous_mensuel_um</code></li>
<li><code>sensor.prise_bureau_pc_ikea_mensuel_um</code></li>
<li><code>sensor.prise_congelateur_cuisine_nous_mensuel_um</code></li>
<li><code>sensor.prise_four_micro_ondes_nous_mensuel_um</code></li>
<li><code>sensor.prise_frigo_cuisine_nous_mensuel_um</code></li>
<li><code>sensor.prise_horloge_ikea_mensuel_um</code></li>
<li><code>sensor.prise_lave_linge_nous_mensuel_um</code></li>
<li><code>sensor.prise_lave_vaisselle_nous_mensuel_um</code></li>
<li><code>sensor.prise_pc_s_gege_ikea_mensuel_um</code></li>
<li><code>sensor.prise_petit_dejeune_nous_mensuel_um</code></li>
<li><code>sensor.prise_salon_chargeur_nous_mensuel_um</code></li>
<li><code>sensor.prise_tete_de_lit_chambre_mensuel_um</code></li>
<li><code>sensor.prise_tv_chambre_nous_mensuel_um</code></li>
<li><code>sensor.prise_tv_salon_ikea_mensuel_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_mensuel_um</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Temps Réel</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE_TEMPS_REEL.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_temps_reel_2026-05-12.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>total_pour_les_7_postes.yaml</code> — 6 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P0_Energie_total_diag/total_pour_les_7_postes/total_pour_les_7_postes.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.total_poste_autre_puissance</code></li>
<li><code>sensor.total_poste_chauffage_puissance</code></li>
<li><code>sensor.total_poste_cuisine_puissance</code></li>
<li><code>sensor.total_poste_froid_puissance</code></li>
<li><code>sensor.total_poste_hygiene_puissance</code></li>
<li><code>sensor.total_poste_multimedia_puissance</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_AVG_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.airfryer_avg_watts_quotidien</code></li>
<li><code>sensor.box_internet_avg_watts_quotidien</code></li>
<li><code>sensor.chargeurs_salon_avg_watts_quotidien</code></li>
<li><code>sensor.congelateur_avg_watts_quotidien</code></li>
<li><code>sensor.fer_repasser_avg_watts_quotidien</code></li>
<li><code>sensor.four_mo_avg_watts_quotidien</code></li>
<li><code>sensor.frigo_avg_watts_quotidien</code></li>
<li><code>sensor.horloge_avg_watts_quotidien</code></li>
<li><code>sensor.lave_linge_avg_watts_quotidien</code></li>
<li><code>sensor.lave_vaisselle_avg_watts_quotidien</code></li>
<li><code>sensor.pc_bureau_avg_watts_quotidien</code></li>
<li><code>sensor.pc_gege_avg_watts_quotidien</code></li>
<li><code>sensor.petit_dej_avg_watts_quotidien</code></li>
<li><code>sensor.plaques_cuisson_avg_watts_quotidien</code></li>
<li><code>sensor.tetes_lit_avg_watts_quotidien</code></li>
<li><code>sensor.tv_chambre_avg_watts_quotidien</code></li>
<li><code>sensor.tv_salon_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_AVG_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_current_all_standby.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_I_all_standby_power/P2_current_all_standby.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_current</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_POWER_3_TOTAL_ZONE.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_total_group_puissance_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.four_et_plaque_de_cuisson_quotidien_um</code></li>
<li><code>sensor.prise_airfryer_ninja_nous_quotidien_um</code></li>
<li><code>sensor.prise_box_internet_ikea_quotidien_um</code></li>
<li><code>sensor.prise_bureau_fer_a_repasser_nous_quotidien_um</code></li>
<li><code>sensor.prise_bureau_pc_ikea_quotidien_um</code></li>
<li><code>sensor.prise_congelateur_cuisine_nous_quotidien_um</code></li>
<li><code>sensor.prise_four_micro_ondes_nous_quotidien_um</code></li>
<li><code>sensor.prise_frigo_cuisine_nous_quotidien_um</code></li>
<li><code>sensor.prise_horloge_ikea_quotidien_um</code></li>
<li><code>sensor.prise_lave_linge_nous_quotidien_um</code></li>
<li><code>sensor.prise_lave_vaisselle_nous_quotidien_um</code></li>
<li><code>sensor.prise_pc_s_gege_ikea_quotidien_um</code></li>
<li><code>sensor.prise_petit_dejeune_nous_quotidien_um</code></li>
<li><code>sensor.prise_salon_chargeur_nous_quotidien_um</code></li>
<li><code>sensor.prise_tete_de_lit_chambre_quotidien_um</code></li>
<li><code>sensor.prise_tv_chambre_nous_quotidien_um</code></li>
<li><code>sensor.prise_tv_salon_ikea_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (58)</i></summary>
<blockquote><ul>
<li><code>sensor.all_standby_power</code></li>
<li><code>sensor.clim_bureau_nous_power</code></li>
<li><code>sensor.clim_chambre_nous_power</code></li>
<li><code>sensor.clim_salon_nous_power</code></li>
<li><code>sensor.four_et_plaque_de_cuisson_current</code></li>
<li><code>sensor.four_et_plaque_de_cuisson_power</code></li>
<li><code>sensor.general_electric_appart_power</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_</code></li>
<li><code>sensor.hue_color_candle_chambre_eric_power</code></li>
<li><code>sensor.hue_color_candle_chambre_gege_power</code></li>
<li><code>sensor.hue_color_candle_salon_1_power</code></li>
<li><code>sensor.hue_play_1_pc_bureau_power</code></li>
<li><code>sensor.hue_play_2_pc_bureau_power</code></li>
<li><code>sensor.hue_play_3_pc_bureau_power</code></li>
<li><code>sensor.hue_white_lamp_bureau_1_power</code></li>
<li><code>sensor.hue_white_lamp_bureau_2_power</code></li>
<li><code>sensor.hue_white_lamp_chambre_</code></li>
<li><code>sensor.hue_white_lamp_couloir_power</code></li>
<li><code>sensor.hue_white_lamp_cuisine_power</code></li>
<li><code>sensor.hue_white_lamp_entree_power</code></li>
<li><code>sensor.hue_white_lamp_table_power</code></li>
<li><code>sensor.lampe_salle_de_bain_hue_power</code></li>
<li><code>sensor.prise_airfryer_ninja_nous_current</code></li>
<li><code>sensor.prise_airfryer_ninja_nous_power</code></li>
<li><code>sensor.prise_box_internet_ikea_current</code></li>
<li><code>sensor.prise_box_internet_ikea_power</code></li>
<li><code>sensor.prise_bureau_fer_a_repasser_nous_current</code></li>
<li><code>sensor.prise_bureau_fer_a_repasser_nous_power</code></li>
<li><code>sensor.prise_bureau_pc_ikea_current</code></li>
<li><code>sensor.prise_bureau_pc_ikea_power</code></li>
<li><code>sensor.prise_congelateur_cuisine_nous_current</code></li>
<li><code>sensor.prise_congelateur_cuisine_nous_power</code></li>
<li><code>sensor.prise_four_micro_ondes_nous_current</code></li>
<li><code>sensor.prise_four_micro_ondes_nous_power</code></li>
<li><code>sensor.prise_frigo_cuisine_nous_current</code></li>
<li><code>sensor.prise_frigo_cuisine_nous_power</code></li>
<li><code>sensor.prise_horloge_ikea_current</code></li>
<li><code>sensor.prise_horloge_ikea_power</code></li>
<li><code>sensor.prise_lave_linge_nous_current</code></li>
<li><code>sensor.prise_lave_linge_nous_power</code></li>
<li><code>sensor.prise_lave_vaisselle_nous_current</code></li>
<li><code>sensor.prise_lave_vaisselle_nous_power</code></li>
<li><code>sensor.prise_pc_s_gege_ikea_current</code></li>
<li><code>sensor.prise_pc_s_gege_ikea_power</code></li>
<li><code>sensor.prise_petit_dejeune_nous_current</code></li>
<li><code>sensor.prise_petit_dejeune_nous_power</code></li>
<li><code>sensor.prise_salon_chargeur_nous_current</code></li>
<li><code>sensor.prise_salon_chargeur_nous_power</code></li>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_power</code></li>
<li><code>sensor.prise_soufflant_salle_de_bain_nous_power</code></li>
<li><code>sensor.prise_tete_de_lit_chambre_current</code></li>
<li><code>sensor.prise_tete_de_lit_chambre_power</code></li>
<li><code>sensor.prise_tv_chambre_nous_current</code></li>
<li><code>sensor.prise_tv_chambre_nous_power</code></li>
<li><code>sensor.prise_tv_salon_ikea_current</code></li>
<li><code>sensor.prise_tv_salon_ikea_power</code></li>
<li><code>sensor.radiateur_elec_cuisine_power</code></li>
<li><code>sensor.relais_lumiere_sdb_sonoff_power</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/COULEURS_PRISES_PAR_PIECE.md">Couleurs Prises par Pièce</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L2C2 — ÉNERGIE CLIM</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~97 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C2_ENERGIE_CLIM/L2C2_VIGNETTE_ENERGIE_CLIM.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L2C2_05_Energie_Clim/vignette_L2C2_energie_clim_2026-05-13.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 7 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.sdb_seche_serviette_etat</code></li>
<li><code>sensor.sdb_soufflant_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_UM_AMHQ.yaml</code> — 12 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_bureau_mensuel_um</code></li>
<li><code>sensor.clim_bureau_quotidien_um</code></li>
<li><code>sensor.clim_chambre_mensuel_um</code></li>
<li><code>sensor.clim_chambre_quotidien_um</code></li>
<li><code>sensor.clim_salon_mensuel_um</code></li>
<li><code>sensor.clim_salon_quotidien_um</code></li>
<li><code>sensor.radiateur_elec_cuisine_mensuel_um</code></li>
<li><code>sensor.radiateur_elec_cuisine_quotidien_um</code></li>
<li><code>sensor.seche_serviette_sdb_mensuel_um</code></li>
<li><code>sensor.seche_serviette_sdb_quotidien_um</code></li>
<li><code>sensor.soufflant_sdb_mensuel_um</code></li>
<li><code>sensor.soufflant_sdb_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (1)</i></summary>
<blockquote><ul>
<li><code>climate.soufflant_salle_de_bain</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 1 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C2_ENERGIE_CLIM/PAGE_ENERGIE_CLIM.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-05-13.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_DUT_clim_chauffage.yaml</code> — 4 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dut_clim_bureau</code></li>
<li><code>sensor.dut_clim_chambre</code></li>
<li><code>sensor.dut_clim_salon</code></li>
<li><code>sensor.dut_radiateur_cuisine</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG.yaml</code> — 12 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_AVG/P1_AVG.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_bureau_avg_watts_mensuel</code></li>
<li><code>sensor.clim_bureau_avg_watts_quotidien</code></li>
<li><code>sensor.clim_chambre_avg_watts_mensuel</code></li>
<li><code>sensor.clim_chambre_avg_watts_quotidien</code></li>
<li><code>sensor.clim_salon_avg_watts_mensuel</code></li>
<li><code>sensor.clim_salon_avg_watts_quotidien</code></li>
<li><code>sensor.radiateur_elec_cuisine_avg_watts_mensuel</code></li>
<li><code>sensor.radiateur_elec_cuisine_avg_watts_quotidien</code></li>
<li><code>sensor.seche_serviette_sdb_avg_watts_mensuel</code></li>
<li><code>sensor.seche_serviette_sdb_avg_watts_quotidien</code></li>
<li><code>sensor.soufflant_sdb_avg_watts_mensuel</code></li>
<li><code>sensor.soufflant_sdb_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG_TOTAL_AMHQ.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_rad_total_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_DUT_TOTAL_SDB.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dut_sdb_total</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 12 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.bureau_power_status_affichage</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.chambre_power_status_affichage</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.cuisine_power_status_affichage</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.salon_power_status_affichage</code></li>
<li><code>sensor.sdb_power_status_affichage</code></li>
<li><code>sensor.sdb_seche_serviette_power_status</code></li>
<li><code>sensor.sdb_soufflant_power_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_UM_AMHQ.yaml</code> — 24 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_bureau_annuel_um</code></li>
<li><code>sensor.clim_bureau_hebdomadaire_um</code></li>
<li><code>sensor.clim_bureau_mensuel_um</code></li>
<li><code>sensor.clim_bureau_quotidien_um</code></li>
<li><code>sensor.clim_chambre_annuel_um</code></li>
<li><code>sensor.clim_chambre_hebdomadaire_um</code></li>
<li><code>sensor.clim_chambre_mensuel_um</code></li>
<li><code>sensor.clim_chambre_quotidien_um</code></li>
<li><code>sensor.clim_salon_annuel_um</code></li>
<li><code>sensor.clim_salon_hebdomadaire_um</code></li>
<li><code>sensor.clim_salon_mensuel_um</code></li>
<li><code>sensor.clim_salon_quotidien_um</code></li>
<li><code>sensor.radiateur_elec_cuisine_annuel_um</code></li>
<li><code>sensor.radiateur_elec_cuisine_hebdomadaire_um</code></li>
<li><code>sensor.radiateur_elec_cuisine_mensuel_um</code></li>
<li><code>sensor.radiateur_elec_cuisine_quotidien_um</code></li>
<li><code>sensor.seche_serviette_sdb_annuel_um</code></li>
<li><code>sensor.seche_serviette_sdb_hebdomadaire_um</code></li>
<li><code>sensor.seche_serviette_sdb_mensuel_um</code></li>
<li><code>sensor.seche_serviette_sdb_quotidien_um</code></li>
<li><code>sensor.soufflant_sdb_annuel_um</code></li>
<li><code>sensor.soufflant_sdb_hebdomadaire_um</code></li>
<li><code>sensor.soufflant_sdb_mensuel_um</code></li>
<li><code>sensor.soufflant_sdb_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (32)</i></summary>
<blockquote><ul>
<li><code>climate.soufflant_salle_de_bain</code></li>
<li><code>sensor.clim_bureau_nous_current</code></li>
<li><code>sensor.clim_bureau_nous_energy</code></li>
<li><code>sensor.clim_bureau_nous_power</code></li>
<li><code>sensor.clim_bureau_nous_voltage</code></li>
<li><code>sensor.clim_chambre_nous_current</code></li>
<li><code>sensor.clim_chambre_nous_energy</code></li>
<li><code>sensor.clim_chambre_nous_power</code></li>
<li><code>sensor.clim_chambre_nous_voltage</code></li>
<li><code>sensor.clim_salon_nous_current</code></li>
<li><code>sensor.clim_salon_nous_energy</code></li>
<li><code>sensor.clim_salon_nous_power</code></li>
<li><code>sensor.clim_salon_nous_voltage</code></li>
<li><code>sensor.prise_radiateur_salle_de_bain_inspelning_ikea_power</code></li>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_current</code></li>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_energy</code></li>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_power</code></li>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_voltage</code></li>
<li><code>sensor.prise_soufflant_salle_de_bain_nous_current</code></li>
<li><code>sensor.prise_soufflant_salle_de_bain_nous_energy</code></li>
<li><code>sensor.prise_soufflant_salle_de_bain_nous_power</code></li>
<li><code>sensor.prise_soufflant_salle_de_bain_nous_voltage</code></li>
<li><code>sensor.radiateur_elec_cuisine_current</code></li>
<li><code>sensor.radiateur_elec_cuisine_energy</code></li>
<li><code>sensor.radiateur_elec_cuisine_power</code></li>
<li><code>sensor.radiateur_elec_cuisine_voltage</code></li>
<li><code>sensor.sdb_seche_serviettes_power_status_affichage</code></li>
<li><code>sensor.th_bureau_temperature</code></li>
<li><code>sensor.th_chambre_temperature</code></li>
<li><code>sensor.th_cuisine_temperature</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>sensor.th_salon_temperature</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#tendances</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L2C3 — ÉNERGIE ÉCLAIRAGE</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~85 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/L2C3_VIGNETTE_ECLAIRAGE.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L2C3_06_Energie_Eclairage/vignette_L2C3_energie_eclairage_2026-05-13.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P3_TPL_AMHQ_2_ZONE.yaml</code> — 12 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_appart_2_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_appart_2_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_bureau_5_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_bureau_5_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_chambre_4_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_chambre_4_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_cuisine_1_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_cuisine_1_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_salon_5_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_salon_5_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_sdb_2_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_sdb_2_quotidien_um_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_TPL_AMHQ_3_TOTAL.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_3_TOTAL.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_total_unit_mensuel_kwh_tpl</code></li>
<li><code>sensor.eclairage_total_unit_quotidien_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>etats_status.yaml</code> — 6 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.lumiere_appartement_etat</code></li>
<li><code>sensor.lumiere_bureau_etat</code></li>
<li><code>sensor.lumiere_chambre_etat</code></li>
<li><code>sensor.lumiere_cuisine_etat</code></li>
<li><code>sensor.lumiere_salle_de_bain_etat</code></li>
<li><code>sensor.lumiere_salon_etat</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/PAGE_ENERGIE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C3_06_Energie_Eclairage/page_L2C3_energie_eclairage_2026-05-13.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 4 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.bureau</code></li>
<li><code>light.chambre</code></li>
<li><code>light.cuisine</code></li>
<li><code>light.salon</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_AVG_AMHQ_2_ZONE.yaml</code> — 5 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_appart_3_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_bureau_5_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_chambre_4_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_salon_5_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_sdb_2_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_TPL_AMHQ_1_UNITE.yaml</code> — 38 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_1_UNITE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.hue_ambiance_lamp_salon_1_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_1_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_2_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_2_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_3_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_3_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_color_candle_chambre_eric_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_color_candle_chambre_eric_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_color_candle_chambre_gege_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_color_candle_chambre_gege_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_color_candle_salon_1_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_color_candle_salon_1_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_play_1_pc_bureau_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_play_1_pc_bureau_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_play_2_pc_bureau_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_play_2_pc_bureau_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_play_3_pc_bureau_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_play_3_pc_bureau_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_bureau_1_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_bureau_1_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_bureau_2_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_bureau_2_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_chambre_1_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_chambre_1_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_chambre_2_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_chambre_2_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_couloir_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_couloir_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_cuisine_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_cuisine_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_entree_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_entree_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_table_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_table_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.lampe_salle_de_bain_hue_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.lampe_salle_de_bain_hue_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.relais_lumiere_sdb_sonoff_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.relais_lumiere_sdb_sonoff_quotidien_um_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_TPL_AMHQ_2_ZONE.yaml</code> — 20 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/P3_ENERGIE_TLP/P3_TPL_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_appart_3_annuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_appart_3_hebdomadaire_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_appart_3_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_appart_3_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_bureau_5_annuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_bureau_5_hebdomadaire_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_bureau_5_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_bureau_5_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_chambre_4_annuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_chambre_4_hebdomadaire_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_chambre_4_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_chambre_4_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_salon_5_annuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_salon_5_hebdomadaire_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_salon_5_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_salon_5_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_sdb_2_annuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_sdb_2_hebdomadaire_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_sdb_2_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.eclairage_sdb_2_quotidien_um_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_UM_AMHQ_1_UNITE.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.lampe_salle_de_bain_hue</code></li>
<li><code>switch.relais_lumiere_sdb_sonoff</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (4)</i></summary>
<blockquote><ul>
<li><code>light.couloir</code></li>
<li><code>light.entree</code></li>
<li><code>light.lit</code></li>
<li><code>light.table</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/COULEURS_ECLAIRAGE_PAR_PIECE.md">Couleurs Éclairage par Pièce</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L3C1 — COMMANDES ÉCLAIRAGE</b> &nbsp;|&nbsp; 2 page(s) &nbsp;|&nbsp; ~43 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/L3C1_VIGNETTE_ECLAIRAGE.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L3C1_07_Commandes_Eclairage/vignette_L3C1_eclairage_2026-05-13.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.chambre</code></li>
<li><code>light.cuisine</code></li>
<li><code>light.salon</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>etats_status.yaml</code> — 7 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.bureau_etat</code></li>
<li><code>sensor.chambre_etat</code></li>
<li><code>sensor.lumiere_appartement_etat</code></li>
<li><code>sensor.lumiere_cuisine_etat</code></li>
<li><code>sensor.lumiere_ecran_etat</code></li>
<li><code>sensor.lumiere_salle_de_bain_etat</code></li>
<li><code>sensor.lumiere_salon_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_UM_AMHQ_1_UNITE.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.hue_color_candle_chambre_eric</code></li>
<li><code>light.hue_color_candle_chambre_gege</code></li>
<li><code>light.lampe_salle_de_bain_hue</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>light.couloir</code></li>
<li><code>light.entree</code></li>
<li><code>light.table</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_gauche_2026-05-13.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.cuisine</code></li>
<li><code>light.salon</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>etats_status.yaml</code> — 5 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.lumiere_couloir_etat</code></li>
<li><code>sensor.lumiere_cuisine_etat</code></li>
<li><code>sensor.lumiere_entree_etat</code></li>
<li><code>sensor.lumiere_salon_etat</code></li>
<li><code>sensor.lumiere_table_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>S_01_STORES.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>cover.store_salon</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (5)</i></summary>
<blockquote><ul>
<li><code>light.couloir</code></li>
<li><code>light.entree</code></li>
<li><code>light.table</code></li>
<li><code>sensor.th_cuisine_temperature</code></li>
<li><code>sensor.th_salon_temperature</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Droite</b> — 3 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-13.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.bureau</code></li>
<li><code>light.chambre</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>etats_status.yaml</code> — 6 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.chambre_nb_allumes</code></li>
<li><code>sensor.lumiere_bureau_etat</code></li>
<li><code>sensor.lumiere_chambre_etat</code></li>
<li><code>sensor.lumiere_ecran_etat</code></li>
<li><code>sensor.lumiere_salle_de_bain_etat</code></li>
<li><code>sensor.lumiere_tete_de_lit_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>S_01_STORES.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>cover.store_bureau</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_UM_AMHQ_1_UNITE.yaml</code> — 9 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>light.hue_color_candle_chambre_eric</code></li>
<li><code>light.hue_color_candle_chambre_gege</code></li>
<li><code>light.hue_play_1_pc_bureau</code></li>
<li><code>light.hue_play_2_pc_bureau</code></li>
<li><code>light.hue_play_3_pc_bureau</code></li>
<li><code>light.hue_white_lamp_bureau_1</code></li>
<li><code>light.hue_white_lamp_bureau_2</code></li>
<li><code>light.lampe_salle_de_bain_hue</code></li>
<li><code>switch.relais_lumiere_sdb_sonoff</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (8)</i></summary>
<blockquote><ul>
<li><code>light.lit</code></li>
<li><code>light.moniteur_pc</code></li>
<li><code>light.zone_eric</code></li>
<li><code>light.zone_gege</code></li>
<li><code>sensor.th_bureau_temperature</code></li>
<li><code>sensor.th_chambre_temperature</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>switch.ecran_p_c_3_play_hue</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#tete_de_lit</code> — 2 entité(s)</summary>
<blockquote><ul>
<li><code>light.hue_color_candle_chambre_eric</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml">voir fichier</a></li>
<li><code>light.hue_color_candle_chambre_gege</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bureau</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.bureau</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ecranpc</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.moniteur_pc</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L3C2 — COMMANDES PRISES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~6 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C2_PRISES/L3C2_VIGNETTE_PRISES.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L3C2_08_Commandes_Prises/vignette_L3C2_prises_2026-05-14.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.prise_horloge_ikea</code></li>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
<li><code>switch.prise_tv_salon_ikea</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>light.hue_smart_eco_salon</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C2_PRISES/PAGE_PRISES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C2_08_Commandes_Prises/page_L3C2_prises_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.prise_horloge_ikea</code></li>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
<li><code>switch.prise_tv_salon_ikea</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>light.hue_smart_eco_salon</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L3C3 — STORES & FENÊTRES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~15 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C3_STORES/L3C3_VIGNETTE_STORES.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L3C3_09_Stores_Fenetres/vignette_L3C3_stores_2026-05-14.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>S_01_STORES.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.store_bureau_status</code></li>
<li><code>sensor.store_salon_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (4)</i></summary>
<blockquote><ul>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_chambre_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_cuisine_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C3_STORES/PAGE_STORES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>S_01_STORES.yaml</code> — 4 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>cover.store_bureau</code></li>
<li><code>cover.store_salon</code></li>
<li><code>sensor.store_bureau_status</code></li>
<li><code>sensor.store_salon_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (8)</i></summary>
<blockquote><ul>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
<li><code>light.store_bureau_dnd</code></li>
<li><code>light.store_salon_dnd</code></li>
<li><code>sensor.contact_fenetre_bureau_sonoff_battery</code></li>
<li><code>sensor.contact_fenetre_salon_sonoff_battery</code></li>
<li><code>sensor.store_bureau_signal_strength</code></li>
<li><code>sensor.store_salon_signal_strength</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L4C1 — PROXMOX (PVE)</b> ⚠️ &nbsp;|&nbsp; 0 page(s) &nbsp;|&nbsp; ~5 entités</summary>
<blockquote>

<blockquote>⚠️ ⚠️ En cours : page non pushée. Doc vignette à créer.</blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <em>Doc Vignette — à créer</em><br>
⚙️ <a href="Docs/Dashboard/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-05-17.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>MP_02_sonde_température_mini-pc.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Mini-PC/MP_02_sonde_température_mini-pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (4)</i></summary>
<blockquote><ul>
<li><code>binary_sensor.pve_status</code></li>
<li><code>sensor.pve_memory_usage_percentage</code></li>
<li><code>sensor.pve_utilisation_du_processeur</code></li>
<li><code>sensor.storage_local_storage_usage_percentage</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L4C2 — MINI PC (NUC)</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~25 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-05-10.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>MP_02_sonde_température_mini-pc.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Mini-PC/MP_02_sonde_température_mini-pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (4)</i></summary>
<blockquote><ul>
<li><code>sensor.prise_mini_pc_ikea_power</code></li>
<li><code>sensor.system_monitor_utilisation_de_la_memoire</code></li>
<li><code>sensor.system_monitor_utilisation_du_disque</code></li>
<li><code>sensor.system_monitor_utilisation_du_processeur</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 5 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C2_MINI_PC/PAGE_MINI_PC.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>MP_02_sonde_température_mini-pc.yaml</code> — 6 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Mini-PC/MP_02_sonde_température_mini-pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_carte_mere</code></li>
<li><code>sensor.temperature_core_0</code></li>
<li><code>sensor.temperature_core_1</code></li>
<li><code>sensor.temperature_core_2</code></li>
<li><code>sensor.temperature_core_3</code></li>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_AVG_AMHQ_mini_pc.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_mini_pc.yaml</code> — 2 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (15)</i></summary>
<blockquote><ul>
<li><code>sensor.cpu_speed</code></li>
<li><code>sensor.prise_mini_pc_ikea_current</code></li>
<li><code>sensor.prise_mini_pc_ikea_energy</code></li>
<li><code>sensor.prise_mini_pc_ikea_power</code></li>
<li><code>sensor.system_monitor_charge_15m</code></li>
<li><code>sensor.system_monitor_charge_1m</code></li>
<li><code>sensor.system_monitor_charge_5m</code></li>
<li><code>sensor.system_monitor_debit_du_reseau_entrant_via_enp6s18</code></li>
<li><code>sensor.system_monitor_debit_du_reseau_sortant_via_enp6s18</code></li>
<li><code>sensor.system_monitor_espace_utilise</code></li>
<li><code>sensor.system_monitor_memoire_libre</code></li>
<li><code>sensor.system_monitor_memoire_utilisee</code></li>
<li><code>sensor.system_monitor_utilisation_de_la_memoire</code></li>
<li><code>sensor.system_monitor_utilisation_du_disque</code></li>
<li><code>sensor.system_monitor_utilisation_du_processeur</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#speed</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_utilisation_du_processeur</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#temp</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.temperature_cpu_package</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Mini-PC/MP_02_sonde_température_mini-pc.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#conso</code> — 7 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_current</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_energy</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_power</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#disk</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_espace_utilise</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#memory</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_memoire_utilisee</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C2_MINI_PC/PAGE_RASPI.md">Page RPi (transitoire)</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L4C3 — MISES À JOUR HA</b> &nbsp;|&nbsp; 2 page(s) &nbsp;|&nbsp; ~9 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C3_MAJ_HA/L4C3_VIGNETTE_MAJ.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L4C3_12_MAJ_HA/vignette_L4C3_maj_ha_2026-05-14.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>Mise_a_jour_home_assistant.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/utilitaires/Mise_a_jour_home_assistant.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.available_updates</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C3_MAJ_HA/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_gauche_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (4)</i></summary>
<blockquote><ul>
<li><code>update.hacs_update</code></li>
<li><code>update.home_assistant_core_update</code></li>
<li><code>update.home_assistant_operating_system_update</code></li>
<li><code>update.home_assistant_supervisor_update</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Droite</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C3_MAJ_HA/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_droite_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (7)</i></summary>
<blockquote><ul>
<li><code>sensor.home_assistant_core_cpu_percent</code></li>
<li><code>sensor.home_assistant_core_memory_percent</code></li>
<li><code>sensor.home_assistant_supervisor_cpu_percent</code></li>
<li><code>sensor.home_assistant_supervisor_memory_percent</code></li>
<li><code>update.hacs_update</code></li>
<li><code>update.home_assistant_core_update</code></li>
<li><code>update.home_assistant_supervisor_update</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L5C1 — PILES & BATTERIES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~33 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C1_PILES_BATTERIES/L5C1_VIGNETTE_BATTERIES.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L5C1_13_Batteries_Piles/vignette_L5C1_batteries_piles_2026-05-14.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>group.hue_devices</code></li>
<li><code>group.ikea_devices</code></li>
<li><code>group.sonoff_devices</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C1_PILES_BATTERIES/PAGE_BATTERIES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C1_13_Batteries_Piles/page_L5C1_batteries_piles_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (30)</i></summary>
<blockquote><ul>
<li><code>sensor.boutton_salle_de_bain_hue_battery</code></li>
<li><code>sensor.contact_fenetre_bureau_sonoff_battery</code></li>
<li><code>sensor.contact_fenetre_chambre_sonoff_battery</code></li>
<li><code>sensor.contact_fenetre_cuisine_sonoff_battery</code></li>
<li><code>sensor.contact_fenetre_salon_sonoff_battery</code></li>
<li><code>sensor.detecteur_de_fuite_ikea_battery</code></li>
<li><code>sensor.detecteur_vallhorn_battery</code></li>
<li><code>sensor.hue_smart_button_bureau_batterie</code></li>
<li><code>sensor.hue_smart_button_chambre_batterie</code></li>
<li><code>sensor.hue_smart_button_chambre_eric_batterie</code></li>
<li><code>sensor.hue_smart_button_chambre_gege_batterie</code></li>
<li><code>sensor.hue_smart_button_couloir_batterie</code></li>
<li><code>sensor.hue_smart_button_cuisine_batterie</code></li>
<li><code>sensor.hue_smart_button_eco_batterie</code></li>
<li><code>sensor.hue_smart_button_entee_1_batterie</code></li>
<li><code>sensor.hue_smart_button_entee_2_batterie</code></li>
<li><code>sensor.hue_smart_button_table_batterie</code></li>
<li><code>sensor.inter_bureau_rodret_battery</code></li>
<li><code>sensor.inter_radiateur_salle_de_bain_ikea_rodret_battery</code></li>
<li><code>sensor.inter_salon_4_ikea_battery</code></li>
<li><code>sensor.inter_somrig_battery</code></li>
<li><code>sensor.inter_tv_chambre_ikea_rodret_battery</code></li>
<li><code>sensor.poussoir_ikea_tradfri_battery</code></li>
<li><code>sensor.th_balcon_nord_battery</code></li>
<li><code>sensor.th_bureau_battery</code></li>
<li><code>sensor.th_cellier_battery</code></li>
<li><code>sensor.th_chambre_battery</code></li>
<li><code>sensor.th_cuisine_battery</code></li>
<li><code>sensor.th_salle_de_bain_battery</code></li>
<li><code>sensor.th_salon_battery</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L5C2 — BATTERIES PORTABLES</b> &nbsp;|&nbsp; 2 page(s) &nbsp;|&nbsp; ~49 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/L5C2_VIGNETTE_BATTERIES_PORTABLES.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L5C2_14_Batteries_Portables/vignette_L5C2_batteries_portables_2026-05-12.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_gauche_2026-05-12.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (28)</i></summary>
<blockquote><ul>
<li><code>sensor.eric_battery_health</code></li>
<li><code>sensor.eric_battery_level</code></li>
<li><code>sensor.eric_battery_state</code></li>
<li><code>sensor.eric_battery_temperature</code></li>
<li><code>sensor.eric_charger_type</code></li>
<li><code>sensor.eric_network_type</code></li>
<li><code>sensor.eric_wi_fi_connection</code></li>
<li><code>sensor.ne2213_eric_battery_health</code></li>
<li><code>sensor.ne2213_eric_battery_level</code></li>
<li><code>sensor.ne2213_eric_battery_state</code></li>
<li><code>sensor.ne2213_eric_battery_temperature</code></li>
<li><code>sensor.ne2213_eric_charger_type</code></li>
<li><code>sensor.ne2213_eric_network_type</code></li>
<li><code>sensor.ne2213_eric_wi_fi_connection</code></li>
<li><code>sensor.sm_a530f_battery_health</code></li>
<li><code>sensor.sm_a530f_battery_level</code></li>
<li><code>sensor.sm_a530f_battery_state</code></li>
<li><code>sensor.sm_a530f_battery_temperature</code></li>
<li><code>sensor.sm_a530f_charger_type</code></li>
<li><code>sensor.sm_a530f_network_type</code></li>
<li><code>sensor.sm_a530f_wi_fi_connection</code></li>
<li><code>sensor.tablette_battery_health</code></li>
<li><code>sensor.tablette_battery_level</code></li>
<li><code>sensor.tablette_battery_state</code></li>
<li><code>sensor.tablette_battery_temperature</code></li>
<li><code>sensor.tablette_charger_type</code></li>
<li><code>sensor.tablette_network_type</code></li>
<li><code>sensor.tablette_wi_fi_connection</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Droite</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_droite_2026-05-12.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (21)</i></summary>
<blockquote><ul>
<li><code>sensor.gm1901_battery_health</code></li>
<li><code>sensor.gm1901_battery_level</code></li>
<li><code>sensor.gm1901_battery_state</code></li>
<li><code>sensor.gm1901_battery_temperature</code></li>
<li><code>sensor.gm1901_charger_type</code></li>
<li><code>sensor.gm1901_network_type</code></li>
<li><code>sensor.gm1901_wi_fi_connection</code></li>
<li><code>sensor.mamour_battery_health</code></li>
<li><code>sensor.mamour_battery_level</code></li>
<li><code>sensor.mamour_battery_state</code></li>
<li><code>sensor.mamour_battery_temperature</code></li>
<li><code>sensor.mamour_charger_type</code></li>
<li><code>sensor.mamour_network_type</code></li>
<li><code>sensor.mamour_wi_fi_connection</code></li>
<li><code>sensor.ne2213_mamour_battery_health</code></li>
<li><code>sensor.ne2213_mamour_battery_level</code></li>
<li><code>sensor.ne2213_mamour_battery_state</code></li>
<li><code>sensor.ne2213_mamour_battery_temperature</code></li>
<li><code>sensor.ne2213_mamour_charger_type</code></li>
<li><code>sensor.ne2213_mamour_network_type</code></li>
<li><code>sensor.ne2213_mamour_wi_fi_connection</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L5C3 — MARIADB</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~5 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C3_MARIADB/L5C3_VIGNETTE_MARIADB.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L5C3_15_MariaDB/vignette_L5C3_mariadb_2026-05-10.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>sql.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sql.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.taille_db_home_assistant</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C3_MARIADB/PAGE_SYSTEME.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C3_15_MariaDB/page_L5C3_mariadb_2026-05-10.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>github_maintenance.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/command_line/github_maintenance/github_maintenance.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.backup_github_status</code></li>
<li><code>sensor.git_last_weekly_tag</code></li>
<li><code>sensor.github_default_branch</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>sql.yaml</code> — 1 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sql.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.taille_db_home_assistant</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (1)</i></summary>
<blockquote><ul>
<li><code>automation.db_purge_mariadb_repack</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L6C1 — QUALITÉ AIR (APPART)</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~12 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L6C1_AIR_QUALITE/L6C1_VIGNETTE_AIR_QUALITE.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L6C1_16_Air_Qualite/vignette_L6C1_air_qualite_2026-05-14.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 6 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L6C1_AIR_QUALITE/PAGE_AIR_QUALITE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L6C1_16_Air_Qualite/page_L6C1_air_qualite_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><code>A_01_AIR_QUALITY.yaml</code> — 6 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code></li>
<li><code>sensor.pm2_5_chambre_moy_24h</code></li>
<li><code>sensor.pm2_5_salon_moy_24h</code></li>
<li><code>sensor.tcov_bureau_moy_24h</code></li>
<li><code>sensor.tcov_chambre_moy_24h</code></li>
<li><code>sensor.tcov_salon_moy_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>A_01_AIR_QUALITY.yaml</code> — 3 entité(s) — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.tcov_bureau_ppb</code></li>
<li><code>sensor.tcov_chambre_ppb</code></li>
<li><code>sensor.tcov_salon_ppb</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>sensor.qualite_air_bureau_ikea_pm25</code></li>
<li><code>sensor.qualite_air_chambre_ikea_pm25</code></li>
<li><code>sensor.qualite_air_salon_ikea_pm25</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#spm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_salon_moy_24h</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#scov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_bureau_ikea_pm25</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_bureau_ppb</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_salon_moy_24h</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bpm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bcov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_chambre_ikea_pm25</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_bureau_moy_24h</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_ppb</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#cpm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_chambre_moy_24h</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ccov</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.tcov_chambre_moy_24h</code> — <a href="Docs/docs_dashboard/TREE_CORRIGE/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L6C2 — POLLUTION & POLLEN</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~19 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L6C2_POLLUTION_POLLEN/L6C2_VIGNETTE_POLLUTION_POLLEN.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L6C2_17_Pollution_Pollen/vignette_L6C2_pollution_pollen_2026-05-14.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L6C2_POLLUTION_POLLEN/PAGE_POLLUTION_POLLEN.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L6C2_17_Pollution_Pollen/page_L6C2_pollution_pollen_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (19)</i></summary>
<blockquote><ul>
<li><code>sensor.concentration_ambroisie_vence</code></li>
<li><code>sensor.concentration_armoise_vence</code></li>
<li><code>sensor.concentration_aulne_vence</code></li>
<li><code>sensor.concentration_bouleau_vence</code></li>
<li><code>sensor.concentration_gramine_vence</code></li>
<li><code>sensor.concentration_olivier_vence</code></li>
<li><code>sensor.dioxyde_d_azote_vence</code></li>
<li><code>sensor.dioxyde_de_soufre_vence</code></li>
<li><code>sensor.niveau_ambroisie_vence</code></li>
<li><code>sensor.niveau_armoise_vence</code></li>
<li><code>sensor.niveau_aulne_vence</code></li>
<li><code>sensor.niveau_bouleau_vence</code></li>
<li><code>sensor.niveau_gramine_vence</code></li>
<li><code>sensor.niveau_olivier_vence</code></li>
<li><code>sensor.ozone_vence</code></li>
<li><code>sensor.pm10_vence</code></li>
<li><code>sensor.pm25_vence</code></li>
<li><code>sensor.qualite_globale_pollen_vence</code></li>
<li><code>sensor.qualite_globale_vence</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L6C3 — VIGILANCE EAU</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~3 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L6C3_VIGIEAU/L6C3_VIGNETTE_VIGIEAU.md">Doc Vignette</a><br>
⚙️ <a href="Docs/Dashboard/L6C3_18_VigiEau/vignette_L6C3_vigieau_2026-05-14.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L6C3_VIGIEAU/PAGE_VIGIEAU.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L6C3_18_VigiEau/page_L6C3_vigieau_2026-05-14.yaml">YAML Page</a>

<details>
<summary><b>📂 Fichiers sources (TREE_CORRIGE)</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>sensor.alert_level_in_vence</code></li>
<li><code>sensor.alert_level_in_vence_numeric</code></li>
<li><code>this.entity_id</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

*Dernière mise à jour : 2026-05-30*