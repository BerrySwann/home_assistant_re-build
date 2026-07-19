# 🗂️ INDEX GLOBAL — HA ReBuild

*Index unique de navigation — YAML, docs, entités, scripts*
*Dernière mise à jour : 2026-07-19 — correction section L1C1 Météo (entités reelles verifiees, voir historique)*
*Dernière mise à jour : 2026-07-16*

---

## 🧠 00 — IA & CONTEXTE

*Fichiers de référence IA — à lire à la demande selon le contexte de la tâche*

---

<details>
<summary><b>IA_CONTEXT_BASE.md</b> &nbsp;|&nbsp; Base de contexte expert HA (résumé principal)</summary>
<blockquote>
📄 <a href="docs/00_IA/IA_CONTEXT_BASE.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_ARBO_DETAIL.md</b> &nbsp;|&nbsp; Arborescence complète prod + local, URLs GitHub raw</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_ARBO_DETAIL.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_AUTOMATIONS_NOTIFS.md</b> &nbsp;|&nbsp; Création/modif automations, messages notify, scripts HA</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_AUTOMATIONS_NOTIFS.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_CMD_TERMINAL_HA.md</b> &nbsp;|&nbsp; Commandes tree prod, audit MD5, git backup, chemins /homeassistant/, logs HA</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_CMD_TERMINAL_HA.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INDEX_AUTOMATIONS.md</b> &nbsp;|&nbsp; Régénération INDEX_AUTOMATIONS, mapping alias → DOCS/03, anomalies</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_INDEX_AUTOMATIONS.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INDEX_NAVIGATION.md</b> &nbsp;|&nbsp; Régénération INDEX_GLOBAL, ajout vignette/page, mapping entités → fichiers sources</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_INDEX_NAVIGATION.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INTEGRATIONS_CARTES.md</b> &nbsp;|&nbsp; YAML dashboard, custom:*, intégrations manquantes, palette couleurs</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_INTEGRATIONS_CARTES.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_P4_PRESENCE.md</b> &nbsp;|&nbsp; sensor.presence, format notif avec présence, logique groupe Wi-Fi</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_P4_PRESENCE.md">Doc</a>
</blockquote>
</details>

---

## ⚙️ 01 — CONFIGURATION SYSTÈME

*Fichiers YAML config HA — auto-documentés via headers inline. Seule la doc de configuration générale est ici.*

---

<details>
<summary><b>configuration.md</b> &nbsp;|&nbsp; Structure configuration.yaml, includes, pôles actifs</summary>
<blockquote>
📄 <a href="docs/01_docs_config_system/config_system_MD/configuration.md">Doc</a>
</blockquote>
</details>

---

## 📊 02 — DASHBOARD (18 vignettes)

*Chemins relatifs depuis la racine du repo GitHub `home_assistant_re-build`*

---

<details>
<summary><b>L1C1 — MÉTÉO</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~31 entités produites (+16 natives)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/L1C1_VIGNETTE_METEO.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/vignette_L1C1_meteo_2026-05-16.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 3 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/PAGE_METEO.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/page_L1C1_meteo_2026-06-13.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#foudre</code> — 14 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.blitzortung_lightning_localisation</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/meteo/M_03_meteo_sensors_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.dernier_impact_temps_reel</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_annuel</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_hebdomadaire</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_horaire</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_mensuel</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_quotidien</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_bearing</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_direction_label</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_distance_km</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.temps_depuis_le_dernier_impact_de_foudre</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.maison_lightning_azimuth</code> — <i>Natif HA (Blitzortung)</i></li>
<li><code>sensor.maison_lightning_counter</code> — <i>Natif HA (Blitzortung)</i></li>
<li><code>sensor.maison_lightning_distance</code> — <i>Natif HA (Blitzortung)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#alert</code> — 14 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.06_weather_alert</code> — <i>Natif HA</i></li>
<li><code>binary_sensor.meteoalarm</code> — <i>Natif HA (fallback)</i></li>
<li><code>sensor.meteo_france_alertes_image_today</code> — <a href="docs/01_docs_config_system/config_system_YAML/command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
<li><code>sensor.meteo_france_alertes_image_tomorrow</code> — <a href="docs/01_docs_config_system/config_system_YAML/command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
<li><code>sensor.alerte_avalanches</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_canicule</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_grand_froid</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_inondation</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_meteo</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_neige_verglas</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_orages</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_pluie_inondation</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vagues_submersion</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vent_violent</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#sun</code> — 6 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sensor.moon_phase</code> — <i>Natif HA</i></li>
<li><code>sensor.season</code> — <i>Natif HA</i></li>
<li><code>sensor.tendance_duree_jour</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sensor.variation_quotidienne</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sun.sun</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>M_01_meteo_alertes_card.yaml</code> — 10 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.alerte_avalanches</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_canicule</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_grand_froid</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_inondation</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_meteo</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_neige_verglas</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_orages</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_pluie_inondation</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vagues_submersion</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vent_violent</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_vent_vence_card.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.vence_wind_bearing</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></li>
<li><code>sensor.vence_wind_direction_label</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></li>
<li><code>sensor.vence_wind_speed_kmh</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_blitzortung.yaml</code> — 5 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dernier_impact_temps_reel</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_bearing</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_direction_label</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.lightning_distance_km</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.temps_depuis_le_dernier_impact_de_foudre</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_03_meteo_blitzortung.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_sensors_blitzortung.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sensors/meteo/M_03_meteo_sensors_blitzortung.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.blitzortung_lightning_localisation</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/meteo/M_03_meteo_sensors_blitzortung.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_UM_blitzortung.yaml</code> — 5 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclair_annuel</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_hebdomadaire</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_horaire</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_mensuel</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_quotidien</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_05_cycle_solaire.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sensor.tendance_duree_jour</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
<li><code>sensor.variation_quotidienne</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_05_cycle_solaire.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>carte_meteo_france.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/command_line/meteo/carte_meteo_france.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.meteo_france_alertes_image_today</code> — <a href="docs/01_docs_config_system/config_system_YAML/command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
<li><code>sensor.meteo_france_alertes_image_tomorrow</code> — <a href="docs/01_docs_config_system/config_system_YAML/command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (16)</i></summary>
<blockquote><ul>
<li><code>binary_sensor.meteoalarm</code></li>
<li><code>input_datetime.dernier_eclair</code></li>
<li><code>input_number.th_balcon_nord_humidity_previous</code></li>
<li><code>input_number.th_balcon_nord_temperature_previous</code></li>
<li><code>sensor.06_weather_alert</code></li>
<li><code>sensor.blitzortung_lightning_last_impact_time</code></li>
<li><code>sensor.maison_lightning_azimuth</code></li>
<li><code>sensor.maison_lightning_counter</code></li>
<li><code>sensor.maison_lightning_distance</code></li>
<li><code>sensor.moon_phase</code></li>
<li><code>sensor.season</code></li>
<li><code>sensor.th_balcon_nord_humidity</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
<li><code>sun.sun</code></li>
<li><code>weather.vence</code></li>
<li><code>zone.home</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : cette section listait des entités obsolètes/inexistantes
(<code>camera.mf_alerte_today/_tomorrow</code> — n'existent pas, <code>camera:</code> désactivé ;
<code>sensor.eclairs_*</code> au pluriel — le vrai nom est <code>sensor.eclair_*</code> singulier ;
<code>sensor.vence_wind_speed</code> — inexistant, vrai nom <code>vence_wind_speed_kmh</code> ;
<code>sensor.direction_du_vent_vence</code>, <code>sensor.vitesse_du_vent_vence</code> — noms
obsolètes sans correspondance réelle, retirés).
Fichiers <code>M_03_meteo_sensors_blitzortung.yaml</code>, <code>M_03_meteo_UM_blitzortung.yaml</code>
et <code>carte_meteo_france.yaml</code> étaient absents de "Fichiers sources" — ajoutés.
<code>M_04_tendances_th_ext_card.yaml</code> était classé à tort ici — son entête déclare
lui-même <code>AVAL : L1C2 Températures</code>, pas L1C1. Déplacé vers la section L1C2.
Vérifié directement dans le corps de chaque fichier yaml, en cohérence avec
DEPENDANCES_GLOBALES.md (section L1C1, corrigée le même jour).
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/TUTO_IMAGES_ALERTES_METEO_FRANCE.md">Tuto Images Alertes Météo France</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/card_duree_du_jour_2026-05-23.yaml">Card Durée du Jour</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L1C2 — TEMPÉRATURES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~42 entités (corrigé 2026-07-19)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C2_TEMPERATURES/L1C2_VIGNETTE_TEMPERATURES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/vignette_L1C2_temperatures_2026-05-12.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity_trend</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
<li><code>sensor.th_balcon_nord_temperature_trend</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C2_TEMPERATURES/PAGE_TEMPERATURES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/page_L1C2_temperatures_2026-07-14.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tendances</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#exterieur</code> — 4 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> — <i>Natif HA (SONOFF Z2M)</i></li>
<li><code>sensor.th_balcon_nord_humidity</code> — <i>Natif HA (SONOFF Z2M)</i></li>
<li><code>sensor.th_balcon_nord_temperature_trend</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
<li><code>weather.vence</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></li>
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
<li><code>sensor.th_balcon_nord_temperature</code> — <i>Natif HA (SONOFF Z2M — historique graphe)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#hcourbe</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity</code> — <i>Natif HA (SONOFF Z2M — historique graphe)</i></li>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG_TOTAL_AMHQ.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_rad_total_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.sdb_seche_serviette_power_status</code></li>
<li><code>sensor.sdb_soufflant_power_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_vent_vence_card.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>weather.vence</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_card.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity_trend</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
<li><code>sensor.th_balcon_nord_temperature_trend</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/meteo/M_04_tendances_th_ext_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (23)</i></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.th_balcon_nord_battery</code></li>
<li><code>sensor.th_balcon_nord_humidity</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
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

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>M_04_tendances_th_ext_card.yaml</code> listait à tort
<code>sensor.th_balcon_nord_temperature</code> / <code>_humidity</code> (valeurs natives brutes)
comme ses propres entités produites — en réalité ce fichier ne produit que les 2 sensors
<code>*_trend</code>, vérifié dans son corps. Les pop-up <code>#tcourbe</code>/<code>#hcourbe</code>
(historique/graphe) reclassés en Natif HA (un graphe historique n'a pas besoin d'un TPL).
<code>P1_ui_dashboard.yaml</code> listait à tort <code>climate.radiateur_cuisine</code> comme
produit par ce fichier — c'est une entité native Meross consommée en source, pas produite
(déplacée vers natives). Bloc <code>P1_UM_AMHQ.yaml — switch.radiateur_elec_cuisine</code>
retiré entièrement — ce fichier utility_meter ne produit que des <code>sensor.*_um</code>
(24 compteurs kWh), aucun <code>switch.*</code>, vérifié dans son corps. Entrée native
<code>climate.clim_du_bureau</code> retirée (nom inexistant, probable coquille de
<code>climate.clim_bureau_rm4_mini</code> déjà listé ailleurs).
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L1C3 — COMMANDES CLIM</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~61 entités (corrigé 2026-07-19)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C3_CLIM/L1C3_VIGNETTE_CLIM.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/vignette_L1C3_clim_2026-07-18.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.delta_ademe_recommande</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 13 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
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
<li><code>climate.radiateur_cuisine</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 1 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C3_CLIM/PAGE_CLIM.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-07-18.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#calcul</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_BV_01_SW_inter_souflant_sdb.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/Inter_BP_Virtuel/P1/P1_BV_01_SW_inter_souflant_sdb.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 11 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
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
<summary><i>Entités natives HA / intégrations externes (34)</i></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>remote.clim_bureau</code></li>
<li><code>remote.clim_chambre</code></li>
<li><code>remote.clim_salon</code></li>
<li><code>remote.soufflant_sdb</code></li>
<li><code>switch.radiateur_elec_cuisine</code></li>
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

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>climate.soufflant_salle_de_bain</code> retiré partout —
entité inexistante (le soufflant SDB n'a pas d'entité climate, vérifié : aucune occurrence
dans tout <code>config_system_YAML/</code>). <code>climate.radiateur_cuisine</code> déplacé de
"produit par P1_ui_dashboard.yaml" vers natif (c'est une entité Meross consommée, pas produite).
Bloc <code>P1_UM_AMHQ.yaml — remote.clim_*/switch.radiateur_elec_cuisine</code> retiré
entièrement — un fichier utility_meter ne produit que des <code>sensor.*_um</code> (vérifié :
24 entrées kWh dans son corps, aucun <code>remote.*</code>/<code>switch.*</code>) ; ces 5 entités
déplacées vers natives.
</blockquote>

</blockquote>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/L2C1_VIGNETTE_ENERGIE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/vignette_L2C1_energie_2026-06-18.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P0_MINI_MAXI_AVG_Genelec_appart.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_conso_maxi_24h</code></li>
<li><code>sensor.genelec_appart_conso_mini_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>01_genelec_appart_AMHQ_cost.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/PAGE_ENERGIE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-06-18.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P0_MINI_MAXI_AVG_Genelec_appart.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_conso_maxi_24h</code></li>
<li><code>sensor.genelec_appart_conso_mini_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>diag_conso_hebdomadaire_en_cours.yaml</code> — 7 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml">voir fichier</a></summary>
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
<summary><code>diag_conso_jour_en_cours.yaml</code> — 7 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml">voir fichier</a></summary>
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
<summary><code>diag_conso_mois_en_cours.yaml</code> — 7 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml">voir fichier</a></summary>
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
<summary><code>01_genelec_appart_AMHQ_cost.yaml</code> — 9 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml">voir fichier</a></summary>
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
<summary><code>02_ratio_hp_hc.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_ratio_hc_hebdomadaire</code></li>
<li><code>sensor.genelec_appart_ratio_hc_mensuel</code></li>
<li><code>sensor.genelec_appart_ratio_hc_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>03_AVG_genelec_appart.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_avg_watts_mensuel</code></li>
<li><code>sensor.genelec_appart_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>MyElectricalData.yaml</code> — 8 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml">voir fichier</a></summary>
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
<summary><code>01_UM_AMHQ.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_hebdomadaire_um</code></li>
<li><code>sensor.genelec_appart_mensuel_um</code></li>
<li><code>sensor.genelec_appart_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>02_UM_genelec_appart_HPHC_AMHQ.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P0_Energie_total/Genelec_appart/02_UM_genelec_appart_HPHC_AMHQ.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/PAGE_ENERGIE_MENSUEL.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_mensuel_2026-06-18.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P2_AVG_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_AVG_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_UM_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/PAGE_ENERGIE_TEMPS_REEL.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/page_L2C1_energie_temps_reel_2026-06-18.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>total_pour_les_7_postes.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P0_Energie_total_diag/P0_total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml">voir fichier</a></summary>
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
<summary><code>P2_AVG_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_AVG_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_current_all_standby.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_I_all_standby_power/P2_current_all_standby.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_current</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_POWER_3_TOTAL_ZONE.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_total_group_puissance_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 17 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_UM_AMHQ_veilles.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (61)</i></summary>
<blockquote><ul>
<li><code>sensor.all_standby_power</code></li>
<li><code>sensor.clim_bureau_nous_power</code></li>
<li><code>sensor.clim_chambre_nous_power</code></li>
<li><code>sensor.clim_salon_nous_power</code></li>
<li><code>sensor.four_et_plaque_de_cuisson_current</code></li>
<li><code>sensor.four_et_plaque_de_cuisson_power</code></li>
<li><code>sensor.general_electric_appart_power</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_1_power</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_2_power</code></li>
<li><code>sensor.hue_ambiance_lamp_salon_3_power</code></li>
<li><code>sensor.hue_color_candle_chambre_eric_power</code></li>
<li><code>sensor.hue_color_candle_chambre_gege_power</code></li>
<li><code>sensor.hue_color_candle_salon_1_power</code></li>
<li><code>sensor.hue_play_1_pc_bureau_power</code></li>
<li><code>sensor.hue_play_2_pc_bureau_power</code></li>
<li><code>sensor.hue_play_3_pc_bureau_power</code></li>
<li><code>sensor.hue_white_lamp_bureau_1_power</code></li>
<li><code>sensor.hue_white_lamp_bureau_2_power</code></li>
<li><code>sensor.hue_white_lamp_chambre_1_power</code></li>
<li><code>sensor.hue_white_lamp_chambre_2_power</code></li>
<li><code>sensor.hue_white_lamp_couloir_power</code></li>
<li><code>sensor.hue_white_lamp_cuisine_power</code></li>
<li><code>sensor.hue_white_lamp_entree_power</code></li>
<li><code>sensor.hue_white_lamp_table_power</code></li>
<li><code>sensor.hue_white_lamp_salle_de_bain_power</code></li>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/COULEURS_PRISES_PAR_PIECE.md">Couleurs Prises par Pièce</a><br>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C2_ENERGIE_CLIM/L2C2_VIGNETTE_ENERGIE_CLIM.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/vignette_L2C2_energie_clim_2026-05-13.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.bureau_power_status</code></li>
<li><code>sensor.chambre_power_status</code></li>
<li><code>sensor.cuisine_power_status</code></li>
<li><code>sensor.salon_power_status</code></li>
<li><code>sensor.sdb_seche_serviette_etat</code></li>
<li><code>sensor.sdb_soufflant_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_UM_AMHQ.yaml</code> — 12 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
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
<li><code>climate.radiateur_cuisine</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 1 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C2_ENERGIE_CLIM/PAGE_ENERGIE_CLIM.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-07-14.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tendances</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_DUT_clim_chauffage.yaml</code> — 4 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dut_clim_bureau</code></li>
<li><code>sensor.dut_clim_chambre</code></li>
<li><code>sensor.dut_clim_salon</code></li>
<li><code>sensor.dut_radiateur_cuisine</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG.yaml</code> — 12 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG.yaml">voir fichier</a></summary>
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
<summary><code>P1_AVG_TOTAL_AMHQ.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_rad_total_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_DUT_TOTAL_SDB.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dut_sdb_total</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> — 11 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
<blockquote><ul>
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
<summary><code>P1_UM_AMHQ.yaml</code> — 24 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
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
<summary><i>Entités natives HA / intégrations externes (33)</i></summary>
<blockquote><ul>
<li><code>climate.radiateur_cuisine</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/L2C3_VIGNETTE_ECLAIRAGE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/vignette_L2C3_energie_eclairage_2026-05-13.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P3_TPL_AMHQ_2_ZONE.yaml</code> — 12 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
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
<summary><code>P3_TPL_AMHQ_3_TOTAL.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_total_unit_mensuel_kwh_tpl</code></li>
<li><code>sensor.eclairage_total_unit_quotidien_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>etats_status.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/PAGE_ENERGIE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/page_L2C3_energie_eclairage_2026-05-13.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P3_AVG_AMHQ_2_ZONE.yaml</code> — 5 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_appart_3_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_bureau_5_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_chambre_4_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_salon_5_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_sdb_2_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_TPL_AMHQ_1_UNITE.yaml</code> — 38 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml">voir fichier</a></summary>
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
<li><code>sensor.hue_white_lamp_salle_de_bain_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.hue_white_lamp_salle_de_bain_quotidien_um_kwh_tpl</code></li>
<li><code>sensor.relais_lumiere_sdb_sonoff_mensuel_um_kwh_tpl</code></li>
<li><code>sensor.relais_lumiere_sdb_sonoff_quotidien_um_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_TPL_AMHQ_2_ZONE.yaml</code> — 20 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
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
<summary><i>Entités natives HA / intégrations externes (10)</i></summary>
<blockquote><ul>
<li><code>light.bureau</code></li>
<li><code>light.chambre</code></li>
<li><code>light.couloir</code></li>
<li><code>light.cuisine</code></li>
<li><code>light.entree</code></li>
<li><code>light.lit</code></li>
<li><code>light.salon</code></li>
<li><code>light.table</code></li>
<li><code>light.hue_white_lamp_salle_de_bain</code></li>
<li><code>switch.relais_lumiere_sdb_sonoff</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>light.bureau/chambre/cuisine/salon</code> étaient
attribués à tort à <code>P1_ui_dashboard.yaml</code> (fichier Pôle 1 clim — vérifié dans
son corps, aucune entité <code>light.*</code> nulle part dedans). <code>light.hue_white_lamp_salle_de_bain</code>
et <code>switch.relais_lumiere_sdb_sonoff</code> étaient attribués à tort à
<code>P3_UM_AMHQ_1_UNITE.yaml</code> (fichier utility_meter — vérifié, ne produit que des
<code>sensor.*_um</code>, jamais de <code>light.*</code>/<code>switch.*</code>). Les 6 regroupés en natives.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/COULEURS_ECLAIRAGE_PAR_PIECE.md">Couleurs Éclairage par Pièce</a><br>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/L3C1_VIGNETTE_ECLAIRAGE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/vignette_L3C1_eclairage_2026-05-13.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>etats_status.yaml</code> — 7 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
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
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (9)</i></summary>
<blockquote><ul>
<li><code>light.chambre</code></li>
<li><code>light.couloir</code></li>
<li><code>light.cuisine</code></li>
<li><code>light.entree</code></li>
<li><code>light.hue_color_candle_chambre_eric</code></li>
<li><code>light.hue_color_candle_chambre_gege</code></li>
<li><code>light.hue_white_lamp_salle_de_bain</code></li>
<li><code>light.salon</code></li>
<li><code>light.table</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : tous les <code>light.*</code> ci-dessus étaient attribués
à tort à <code>P1_ui_dashboard.yaml</code> (fichier Pôle 1 clim) ou <code>P3_UM_AMHQ_1_UNITE.yaml</code>
(fichier utility_meter) — vérifié dans les deux corps, aucun des deux ne produit d'entité
<code>light.*</code>. Ce sont toutes des entités natives Hue Bridge, regroupées en natives.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_gauche_2026-05-13.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>etats_status.yaml</code> — 5 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.lumiere_couloir_etat</code></li>
<li><code>sensor.lumiere_cuisine_etat</code></li>
<li><code>sensor.lumiere_entree_etat</code></li>
<li><code>sensor.lumiere_salon_etat</code></li>
<li><code>sensor.lumiere_table_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>S_01_STORES.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>cover.store_salon</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (7)</i></summary>
<blockquote><ul>
<li><code>light.couloir</code></li>
<li><code>light.cuisine</code></li>
<li><code>light.entree</code></li>
<li><code>light.salon</code></li>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-22.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tete_de_lit</code> — 2 entité(s)</summary>
<blockquote><ul>
<li><code>light.hue_color_candle_chambre_eric</code> — <i>Natif HA (Hue)</i></li>
<li><code>light.hue_color_candle_chambre_gege</code> — <i>Natif HA (Hue)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bureau</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.bureau</code> — <i>Natif HA (Hue)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ecranpc</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.moniteur_pc</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>etats_status.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P3_eclairage/ui_dashboard/etats_status.yaml">voir fichier</a></summary>
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
<summary><code>S_01_STORES.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>cover.store_bureau</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (19)</i></summary>
<blockquote><ul>
<li><code>light.bureau</code></li>
<li><code>light.chambre</code></li>
<li><code>light.hue_color_candle_chambre_eric</code></li>
<li><code>light.hue_color_candle_chambre_gege</code></li>
<li><code>light.hue_play_1_pc_bureau</code></li>
<li><code>light.hue_play_2_pc_bureau</code></li>
<li><code>light.hue_play_3_pc_bureau</code></li>
<li><code>light.hue_white_lamp_bureau_1</code></li>
<li><code>light.hue_white_lamp_bureau_2</code></li>
<li><code>light.hue_white_lamp_salle_de_bain</code></li>
<li><code>light.lit</code></li>
<li><code>light.moniteur_pc</code></li>
<li><code>light.zone_eric</code></li>
<li><code>light.zone_gege</code></li>
<li><code>sensor.th_bureau_temperature</code></li>
<li><code>sensor.th_chambre_temperature</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>switch.ecran_p_c_3_play_hue</code></li>
<li><code>switch.relais_lumiere_sdb_sonoff</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>light.bureau/chambre</code> (attribués à tort à
<code>P1_ui_dashboard.yaml</code>) et les 9 <code>light.*</code>/<code>switch.*</code>
(attribués à tort à <code>P3_UM_AMHQ_1_UNITE.yaml</code>, fichier utility_meter qui ne
produit que des <code>sensor.*_um</code>) déplacés vers natives.
</blockquote>

</blockquote>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C2_PRISES/L3C2_VIGNETTE_PRISES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/vignette_L3C2_prises_2026-05-14.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (6)</i></summary>
<blockquote><ul>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>light.hue_smart_eco_salon</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
<li><code>switch.prise_horloge_ikea</code></li>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
<li><code>switch.prise_tv_salon_ikea</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : les 3 <code>switch.*</code> étaient attribués à tort à
<code>P2_UM_AMHQ_prises.yaml</code> (fichier utility_meter — ne produit que des
<code>sensor.*_um</code>, vérifié). Ce sont des switches natifs Z2M IKEA, déplacés vers natives.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C2_PRISES/PAGE_PRISES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/page_L3C2_prises_2026-05-14.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (6)</i></summary>
<blockquote><ul>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>light.hue_smart_eco_salon</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
<li><code>switch.prise_horloge_ikea</code></li>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
<li><code>switch.prise_tv_salon_ikea</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : les 3 <code>switch.*</code> étaient attribués à tort à
<code>P2_UM_AMHQ_prises.yaml</code> (fichier utility_meter — ne produit que des
<code>sensor.*_um</code>, vérifié). Ce sont des switches natifs Z2M IKEA, déplacés vers natives.
</blockquote>

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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C3_STORES/L3C3_VIGNETTE_STORES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/vignette_L3C3_stores_2026-05-14.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>S_01_STORES.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C3_STORES/PAGE_STORES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-06-02.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>S_01_STORES.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.store_bureau_status</code></li>
<li><code>sensor.store_salon_status</code></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (11)</i></summary>
<blockquote><ul>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
<li><code>cover.store_bureau</code></li>
<li><code>cover.store_salon</code></li>
<li><code>light.store_bureau_dnd</code></li>
<li><code>light.store_salon_dnd</code></li>
<li><code>sensor.contact_fenetre_bureau_sonoff_battery</code></li>
<li><code>sensor.contact_fenetre_salon_sonoff_battery</code></li>
<li><code>sensor.store_bureau_signal_strength</code></li>
<li><code>sensor.store_salon_signal_strength</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>cover.store_bureau/salon</code> sont des sources
consommées par <code>S_01_STORES.yaml</code> (attributs <code>current_position</code>), pas
des entités produites — vérifié dans le corps du fichier (il ne produit que les 2
<code>*_status</code>). <code>sensor.th_balcon_nord_temperature</code> était attribué à
<code>M_04_tendances_th_ext_card.yaml</code> qui ne produit que le sensor <code>*_trend</code> —
la valeur brute est native. Tout déplacé vers natives.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L4C1 — PROXMOX (PVE)</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~5 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C1_PROXMOX/L4C1_VIGNETTE_PROXMOX.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/vignette_L4C1_proxmox_2026-06-18.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (5)</i></summary>
<blockquote><ul>
<li><code>binary_sensor.pve_status</code></li>
<li><code>sensor.pve_memory_usage_percentage</code></li>
<li><code>sensor.pve_utilisation_du_processeur</code></li>
<li><code>sensor.storage_local_storage_usage_percentage</code></li>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>sensor.temperature_cpu_package</code> n'existe dans
aucun fichier <code>config_system_YAML/</code> (vérifié) — publié par le script externe
<code>MP_01_monitor_temp.sh</code> tournant sur le <b>Raspberry Pi</b> (confirmé par Eric
2026-07-19 : "ça remonte la T° du CPU et d'autres choses"), remonté dans HA
via MQTT Discovery. Reclassé natif plutôt que "fichier réorganisé" (ambigu).
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Proxmox</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C1_PROXMOX/PAGE_PROXMOX.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Proxmox/page_L4C1_proxmox_2026-06-18.yaml">YAML Page</a>


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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/vignette_L4C2_mini_pc_2026-06-18.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (5)</i></summary>
<blockquote><ul>
<li><code>sensor.prise_mini_pc_ikea_power</code></li>
<li><code>sensor.system_monitor_utilisation_de_la_memoire</code></li>
<li><code>sensor.system_monitor_utilisation_du_disque</code></li>
<li><code>sensor.system_monitor_utilisation_du_processeur</code></li>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 5 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C2_MINI_PC/PAGE_MINI_PC.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-06-18.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#speed</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_utilisation_du_processeur</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#temp</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.temperature_cpu_package</code> — <i>Natif HA (MQTT Discovery — MP_01_monitor_temp.sh)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#conso</code> — 7 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_current</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_energy</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_power</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
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


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P2_AVG_AMHQ_mini_pc.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_mini_pc.yaml</code> — 2 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code> — <a href="docs/01_docs_config_system/config_system_YAML/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (21)</i></summary>
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
<li><code>sensor.temperature_carte_mere</code></li>
<li><code>sensor.temperature_core_0</code></li>
<li><code>sensor.temperature_core_1</code></li>
<li><code>sensor.temperature_core_2</code></li>
<li><code>sensor.temperature_core_3</code></li>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : les 6 <code>sensor.temperature_*</code> (carte_mere, core_0-3,
cpu_package) n'existent dans aucun fichier <code>config_system_YAML/</code> — publiés par
<code>MP_01_monitor_temp.sh</code> tournant sur le <b>Raspberry Pi</b> (confirmé par Eric
2026-07-19) via MQTT Discovery. Reclassés natifs.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C2_MINI_PC/PAGE_RASPI.md">Page RPi (transitoire)</a><br>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/L4C3_VIGNETTE_MAJ.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/vignette_L4C3_maj_ha_2026-05-14.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>Mise_a_jour_home_assistant.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/utilitaires/Mise_a_jour_home_assistant.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/page_L4C3_maj_ha_gauche_2026-05-14.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/page_L4C3_maj_ha_droite_2026-05-14.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C1_PILES_BATTERIES/L5C1_VIGNETTE_BATTERIES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/vignette_L5C1_batteries_piles_2026-05-14.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C1_PILES_BATTERIES/PAGE_BATTERIES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/page_L5C1_batteries_piles_2026-05-14.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/L5C2_VIGNETTE_BATTERIES_PORTABLES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/vignette_L5C2_batteries_portables_2026-05-12.yaml">YAML Vignette</a>


</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_gauche_2026-05-12.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_droite_2026-05-12.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/L5C3_VIGNETTE_MARIADB.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/vignette_L5C3_mariadb_2026-05-10.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>sql.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sql.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/PAGE_SYSTEME.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/page_L5C3_mariadb_2026-06-15.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>github_maintenance.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/command_line/github_maintenance/github_maintenance.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.backup_github_status</code></li>
<li><code>sensor.git_last_weekly_tag</code></li>
<li><code>sensor.github_default_branch</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>sql.yaml</code> — 1 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sql.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C1_AIR_QUALITE/L6C1_VIGNETTE_AIR_QUALITE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/vignette_L6C1_air_qualite_2026-05-14.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 6 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C1_AIR_QUALITE/PAGE_AIR_QUALITE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/page_L6C1_air_qualite_2026-05-23.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#spm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_salon_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#scov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_salon_ikea_voc_index</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_salon_ppb</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_salon_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>
<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : ce pop-up "Salon COV" contenait à tort une entité PM2.5
Bureau et un tCOV Bureau — incohérent avec son propre nom et la logique du dashboard
(un pop-up COV d'une pièce ne montre pas le PM2.5 d'une autre pièce). Recomposé avec les
3 entités COV/tCOV réelles du Salon (native + TPL + SEN), vérifiées dans les fichiers sources.
</blockquote>

<details>
<summary>💬 Pop-up <code>#bpm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bcov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_bureau_ikea_voc_index</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_bureau_ppb</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_bureau_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>
<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : ce pop-up "Bureau COV" contenait à tort une entité PM2.5
Chambre et un tCOV Chambre — même erreur de croisement qu'au pop-up #scov. Recomposé avec
les 3 entités COV/tCOV réelles du Bureau.
</blockquote>

<details>
<summary>💬 Pop-up <code>#cpm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_chambre_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ccov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_chambre_ikea_voc_index</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_chambre_ppb</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>
<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : ce pop-up "Chambre COV" n'avait qu'1 entité alors que les
pop-up COV des autres pièces en ont 3 (native + TPL + SEN) — complété par cohérence avec
#scov/#bcov, en s'appuyant sur les mêmes 3 fichiers sources déjà vérifiés.
</blockquote>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>A_01_AIR_QUALITY.yaml</code> — 6 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.pm2_5_chambre_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.pm2_5_salon_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_bureau_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_salon_moy_24h</code> — <a href="docs/01_docs_config_system/config_system_YAML/sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>A_01_AIR_QUALITY.yaml</code> — 3 entité(s) — <a href="docs/01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.tcov_bureau_ppb</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_ppb</code> — <a href="docs/01_docs_config_system/config_system_YAML/templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C2_POLLUTION_POLLEN/L6C2_VIGNETTE_POLLUTION_POLLEN.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/vignette_L6C2_pollution_pollen_2026-05-14.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C2_POLLUTION_POLLEN/PAGE_POLLUTION_POLLEN.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/page_L6C2_pollution_pollen_2026-06-13.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C3_VIGIEAU/L6C3_VIGNETTE_VIGIEAU.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/vignette_L6C3_vigieau_2026-05-14.yaml">YAML Vignette</a>
</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C3_VIGIEAU/PAGE_VIGIEAU.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/page_L6C3_vigieau_2026-05-14.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
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

*Dernière mise à jour : 2026-07-19 (audit entites L1C1-L6C3, voir historique en tete de fichier)*
---

## ⚙️ 03 — AUTOMATIONS (48 automations)

*Chemins relatifs depuis `docs_automations/`*

**11 catégories · 48 automations · 49 entrées dans l'index**

<details>
<summary>📋 <b>Table des matières</b></summary>
<blockquote>
<b>🔧 Backup Git</b> (7 automations)<br>
<b>🌤️ Météo</b> (5 automations)<br>
<b>🌡️ P1 — Clim & Chauffage</b> (10 automations)<br>
<b>🍳 P1 — Cuisine</b> (2 automations)<br>
<b>🚿 P1 — Salle de Bain</b> (3 automations)<br>
<b>🔌 P2 — Prises</b> (3 automations)<br>
<b>💡 P3 — Éclairage</b> (7 automations)<br>
<b>🏠 Stores</b> (2 automations)<br>
<b>⚡ Énergie</b> (2 automations)<br>
<b>🖥️ Système</b> (6 automations)<br>
<b>🍓 Raspberry Pi4 (archivé)</b> (1 automations)<br>
</blockquote>
</details>

---

<details>
<summary><b>🔧 Backup Git</b> &nbsp;|&nbsp; 7 automation(s) &nbsp;|&nbsp; <i>Sauvegardes automatiques de la config vers GitHub</i></summary>
<blockquote>

<details>
<summary>✅ <b>[00-Backup] Alerte si KO 15 min</b></summary>
<blockquote>
<i>Notification si le backup reste en KO pendant 15 minutes</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_ALERTE_KO.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/00_backup_alerte_si_ko_15_min.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.backup_github_status</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>[01-Backup] Git hourly H+10</b></summary>
<blockquote>
<i>Push Git + backup natif HA toutes les heures à H+10</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_HOURLY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/01_backup_git_hourly_h_10.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[02-Backup] Git daily (03:00)</b></summary>
<blockquote>
<i>Backup natif HA + push Git quotidien à 03h00</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_DAILY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/02_backup_git_daily_03_00.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[03-Backup] Git weekly (dim 01:30)</b></summary>
<blockquote>
<i>Backup natif HA + push + tag weekly chaque dimanche à 01:30</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_WEEKLY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/03_backup_git_weekly_dim_01_30.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[04-Backup] Git push manuel</b></summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_PUSH_MANUEL.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/04_backup_git_push_manuel.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>input_button.git_push_manuel</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>[05-Backup] Git push weekly manuel</b></summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_PUSH_WEEKLY_MANUEL.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/05_backup_git_push_weekly_manuel.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>input_button.git_push_weekly_manuel</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Git au démarrage</b></summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/BACKUP/GIT_AU_DEMARRAGE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/github_backup/git_push_au_demarrage_ha.yaml">YAML source</a><br>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🌤️ Météo</b> &nbsp;|&nbsp; 5 automation(s) &nbsp;|&nbsp; <i>Alertes Météo France, foudre, tendances thermiques</i></summary>
<blockquote>

<details>
<summary>✅ <b>Alerte Météo France actualisation des "CARTES</b></summary>
<blockquote>
<i>Force la mise à jour des images d''alerte Météo France au démarrage,  aux</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/METEO/ALERTE_METEO_CARTES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/meteo/alerte_meteo_france_actualisation_des_cartes.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · ⏰`time_pattern`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.meteo_france_alertes_image_today</code></li>
<li><code>sensor.meteo_france_alertes_image_tomorrow</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Update previous temperature</b></summary>
<blockquote>
<i>Enregistre la température toutes les 30 minutes pour calculer la tendance.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/METEO/UPDATE_PREV_TEMPERATURE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/meteo/update_previous_temperature.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time_pattern`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>input_number.th_balcon_nord_temperature_previous</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Update previous humidity</b></summary>
<blockquote>
<i>Enregistre l'humidité toutes les 30 minutes pour calculer la tendance.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/METEO/UPDATE_PREV_HUMIDITY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/meteo/update_previous_humidity.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time_pattern`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>input_number.th_balcon_nord_humidity_previous</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Notification de la foudre</b></summary>
<blockquote>
<i>Alerte sur Poco X7 Pro avec distance, ville ou direction et décompte</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/METEO/NOTIF_FOUDRE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/meteo/notification_de_la_foudre.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.maison_lightning_counter</code></li>
<li><code>sensor.blitzortung_lightning_localisation</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Mettre à jour le temps du dernier impact de foudre</b></summary>
<blockquote>
<i>Met à jour le temps du dernier impact de foudre lorsque le capteur</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/METEO/MAJ_TEMPS_FOUDRE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/meteo/mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.maison_lightning_counter</code></li>
<li><code>input_datetime.dernier_eclair</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🌡️ P1 — Clim & Chauffage</b> &nbsp;|&nbsp; 10 automation(s) &nbsp;|&nbsp; <i>Logique de climatisation, notifications, gardien éco</i></summary>
<blockquote>

<details>
<summary>✅ <b>(A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)</b></summary>
<blockquote>
<i>Pilotage clims jour avec boucle de relance et notification ciblée fenêtres</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/A0_CLIM_JOUR.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · 🔄`state`<br>
<br><details>
<summary>🔌 Entités (14) <i>— corrigé 2026-07-19, triggers réels du fichier</i></summary>
<blockquote><ul>
<li><code>sensor.mamour_network_type</code></li>
<li><code>sensor.eric_network_type</code></li>
<li><code>switch.clim_salon_nous</code></li>
<li><code>switch.clim_bureau_nous</code></li>
<li><code>switch.clim_chambre_nous</code></li>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_cuisine_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_chambre_sonoff_contact</code></li>
<li><code>sensor.groupe</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
<li><code>sensor.temperature_cible</code></li>
<li><code>sensor.mode_ete_hiver</code></li>
<li><code>sensor.temperature_confort_jour</code></li>
</ul></blockquote>
<blockquote>
⚙️ Logique clim (climate.*, input_boolean.*_arret_securise_en_cours) déléguée au
<a href="docs/04_docs_scripts/docs_scripts_YAML/p1_master_gestion_clim.yaml">script p1_master_gestion_clim.yaml</a> —
ces entités ne sont pas dans l'automation elle-même, retirées de la liste ci-dessus.
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30)</b></summary>
<blockquote>
<i>Pilotage clims nuit avec boucle de relance et notification ciblée fenêtres</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/B0_CLIM_NUIT.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · 🔄`state`<br>
<br><details>
<summary>🔌 Entités (14) <i>— corrigé 2026-07-19, triggers réels du fichier</i></summary>
<blockquote><ul>
<li><code>sensor.mamour_network_type</code></li>
<li><code>sensor.eric_network_type</code></li>
<li><code>switch.clim_salon_nous</code></li>
<li><code>switch.clim_bureau_nous</code></li>
<li><code>switch.clim_chambre_nous</code></li>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_cuisine_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_chambre_sonoff_contact</code></li>
<li><code>sensor.groupe</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
<li><code>sensor.temperature_cible</code></li>
<li><code>sensor.mode_ete_hiver</code></li>
<li><code>sensor.temperature_confort_nuit</code></li>
</ul></blockquote>
<blockquote>
⚙️ Logique clim (climate.*, input_boolean.*_arret_securise_en_cours) déléguée au
<a href="docs/04_docs_scripts/docs_scripts_YAML/p1_master_gestion_clim.yaml">script p1_master_gestion_clim.yaml</a> —
ces entités ne sont pas dans l'automation elle-même, retirées de la liste ci-dessus.
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(D) Notification température Up ou Down de (7h30 -> 21h00)</b></summary>
<blockquote>
<i>Envoie le message personnalisé de clim si le texte change, OU au réveil</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/C_NOTIF_TEMP_JOUR.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/c_notification_temperature_up_ou_down_7h30_21h00.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> — <i>Natif HA (SONOFF/Z2M, corrigé 2026-07-19 — pas produit par M_04, qui ne produit que les *_trend)</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(E) Notification température Up ou Down de (21h00 -> 7h30)</b></summary>
<blockquote>
<i>Envoie le message personnalisé de clim si le texte change, OU au début</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/D_NOTIF_TEMP_NUIT.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/d_notification_temperature_up_ou_down_21h00_7h30.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> — <i>Natif HA (SONOFF/Z2M, corrigé 2026-07-19 — pas produit par M_04, qui ne produit que les *_trend)</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(F) (CLIM) Notification de fermeture des fenêtres</b></summary>
<blockquote>
<i>Envoie une notification lorsqu'une fenêtre est fermée.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/E_NOTIF_FERMETURE_FENETRES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/e_clim_notification_de_fermeture_des_fenetres.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(G) (CLIM) Automatisation Arrêt Clim Notification</b></summary>
<blockquote>
<i>Notification quand une clim est coupée manuellement, seulement si</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/F_ARRET_CLIM_NOTIF.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/f_clim_automatisation_arret_clim_notification.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (7)</summary>
<blockquote><ul>
<li><code>switch.clim_salon_nous</code></li>
<li><code>switch.clim_bureau_nous</code></li>
<li><code>switch.clim_chambre_nous</code></li>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_cuisine_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>binary_sensor.contact_fenetre_chambre_sonoff_contact</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(H) (CLIM) Notification de changement de mode Été/Fan/Hiver</b></summary>
<blockquote>
<i>Notification lorsque le mode change entre Été, Ventilateur ou Hiver</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/G_NOTIF_MODE_CHANGEMENT.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.mode_ete_hiver</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(I) (CLIM DEBUG) Force Mode Correct & Sécurité</b></summary>
<blockquote>
<i>WATCHDOG :   1. FORCE OFF si tentative d''allumage alors que Prise</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/H_DEBUG_FORCE_MODE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/h_clim_debug_force_mode_correct_securite.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.mode_ete_hiver</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(J) Synchro & Notif Clim si Prise Coupée</b></summary>
<blockquote>
<i>Met à jour l''état du thermostat et notifie proprement si la prise</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/I_SYNCHRO_NOTIF_PRISE_COUPEE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/i_synchro_notif_clim_si_prise_coupee.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(K) (DEBUG) Notifier les changements de message clim (Mobile)</b></summary>
<blockquote>
<i>Surveille et notifie les changements d'état du message personnalisé.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CLIM_CHAUFFAGE/J_DEBUG_NOTIF_MESSAGE_CLIM.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/j_debug_notifier_les_changements_de_message_clim_mobile.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.message_clim_personnalise_7h30_21h00</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🍳 P1 — Cuisine</b> &nbsp;|&nbsp; 2 automation(s) &nbsp;|&nbsp; <i>Chauffage bain d'huile cuisine (plannings semaine/vacances)</i></summary>
<blockquote>

<details>
<summary>✅ <b>A - Chauffage Cuisine (entre 4h45 & 7h LMMJ ou 5:45h & 8h VSD avec T° 19,9°</b></summary>
<blockquote>
<i>Allume ou éteint le chauffage selon la température (19,9° <-> 20.5°)  aux</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CUISINE/A_CHAUFFAGE_CUISINE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_cuisine/a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (4)</summary>
<blockquote><ul>
<li><code>sensor.th_cuisine_temperature</code></li>
<li><code>person.eric</code></li>
<li><code>person.mamour</code></li>
<li><code>climate.radiateur_cuisine</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>B - Chauffage Cuisine Vacances</b></summary>
<blockquote>
<i>Allume ou éteint le chauffage selon la température entre 6h00 et 8h30  pendant</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_CUISINE/B_CHAUFFAGE_CUISINE_VACANCES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_cuisine/b_chauffage_cuisine_vacances.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (4)</summary>
<blockquote><ul>
<li><code>sensor.th_cuisine_temperature</code></li>
<li><code>person.mamour</code></li>
<li><code>person.eric</code></li>
<li><code>climate.radiateur_cuisine</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🚿 P1 — Salle de Bain</b> &nbsp;|&nbsp; 3 automation(s) &nbsp;|&nbsp; <i>Soufflant SDB gestion intelligente + watchdog radiateur + minuterie sèche-serviettes</i></summary>
<blockquote>

<details>
<summary>✅ <b>A - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT</b></summary>
<blockquote>
<i>Cycle complet : Démarrage, Régulation, et Auto-off 60 min avec refroidissement</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_SDB/A_SOUFFLANT_SDB.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_sdb/a_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (6)</summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>switch.prise_soufflant_salle_de_bain_nous</code></li>
<li><code>remote.soufflant_sdb</code></li>
<li><code>input_select.etat_resistance_soufflant_sdb</code></li>
<li><code>climate.soufflant_salle_de_bain</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR</b></summary>
<blockquote>
<i>Reset physique si T > 25°C, uniquement si la prise est alimentée</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_SDB/D_WATCHDOG_RADIATEUR_SDB.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_sdb/d_salle_de_bain_watchdog_securite_radiateur.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (4)</summary>
<blockquote><ul>
<li><code>sensor.th_salle_de_bain_temperature</code></li>
<li><code>switch.prise_soufflant_salle_de_bain_nous</code></li>
<li><code>input_boolean.inter_soufflant_salle_de_bain</code></li>
<li><code>remote.soufflant_sdb</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>E - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 2h)</b></summary>
<blockquote>
<i>Timer de 2h après détection de chauffe. Sécurité anti-redémarrage incluse.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_SDB/E_MINUTERIE_SECHE_SERVIETTES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_sdb/e_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_power</code></li>
<li><code>switch.prise_seche_serviette_salle_de_bain_nous</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🔌 P2 — Prises</b> &nbsp;|&nbsp; 3 automation(s) &nbsp;|&nbsp; <i>Gestion PC bureau, TV chambre, éco prises dynamique</i></summary>
<blockquote>

<details>
<summary>✅ <b>Eco. PRISES DINAMIQUE -> By-Présence/Groupe</b></summary>
<blockquote>
<i>Pilotage des 7 prises en fonction du groupe de présence (G1 à G4).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P2_PRISES/ECO_PRISES_DYNAMIQUE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P2_prises/eco_prises_dinamique_by_presence_groupe.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (8) <i>— corrigé 2026-07-19, liste réelle depuis P2_eco_prises_config.yaml</i></summary>
<blockquote><ul>
<li><code>sensor.groupe</code></li>
<li><code>switch.prise_horloge_ikea</code></li>
<li><code>light.hue_smart_eco_salon</code></li>
<li><code>light.hue_smart_eco_tv_salon</code></li>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>switch.ecran_p_c_3_play_hue</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
</ul></blockquote>
<blockquote>
⚠️ Retiré : <code>sensor.prise_bureau_pc_ikea_power</code> (fictif, absent de la config) et
<code>switch.prise_tv_salon_ikea</code> (mauvais domaine/nom — c'est <code>light.hue_smart_eco_tv_salon</code>).
Ajouté : <code>light.hue_smart_eco_tv_chambre</code> (absent de la liste précédente).
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Gestion PC bureau : Scène de Fin + Notif</b></summary>
<blockquote>
<i>Éteint la prise du PC et notifie, mais laisse la prise ON pour le</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P2_PRISES/GESTION_PC_BUREAU.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P2_prises/gestion_pc_bureau_scene_de_fin_notif.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.prise_bureau_pc_ikea_power</code></li>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Gestion TV Chambre : Scène de Fin + Notif</b></summary>
<blockquote>
<i>Éteint les lumières et notifie, mais laisse la prise ON pour le suivi</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P2_PRISES/GESTION_TV_CHAMBRE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P2_prises/gestion_tv_chambre_scene_de_fin_notif.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt` · ⏰`time` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>sensor.prise_tv_chambre_nous_power</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
<li><code>switch.prise_tv_chambre_nous</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>💡 P3 — Éclairage</b> &nbsp;|&nbsp; 7 automation(s) &nbsp;|&nbsp; <i>Boutons IKEA salon, bureau (Rodret/Somrig), watchdogs lampes</i></summary>
<blockquote>

<details>
<summary>✅ <b>P3_Allumage Lumière Entrée</b></summary>
<blockquote>
<i>Gestion de l''éclairage de l''entrée basée sur les transitions des</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/ALLUMAGE_LUMIERE_ENTREE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_entree_allumage_lumiere.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>sensor.groupe</code></li>
<li><code>sun.sun</code></li>
<li><code>light.entree</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>[P3-SALON] BOUTON IKEA INTER SALON (4) — ON/OFF LIGHT.SALON</b></summary>
<blockquote>
<i>Pilotage de light.salon via le bouton IKEA 4 touches Salon. Topic</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BOUTON_INTER_IKEA_4.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_salon_bouton_ikea_inter_salon.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>light.salon</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>[P3-SALON] BOUTON IKEA SOMRIG — TOUT MESSAGE = ON/OFF</b></summary>
<blockquote>
<i>Pilotage simplifié : n''importe quel appui sur le bouton 1 (simple,</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BOUTON_INTER_SOMRIG.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_salon_bouton_ikea_somrig.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>light.salon</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>P3_BUREAU - BOUTON RODRET TOGGLE BLANCHES</b></summary>
<blockquote>
<i>Alterne l'allumage des 2 lampes blanches via MQTT (Mode Fainéant)</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_RODRET_TOGGLE_BLANCHES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_bouton_rodret_toggle_blanches.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>light.hue_white_lamp_bureau_1</code></li>
<li><code>light.hue_white_lamp_bureau_2</code></li>
<li><code>sensor.bureau_etat</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES</b></summary>
<blockquote>
<i>Assure que les deux lampes de bureau (1 et 2) sont synchronisées si</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_WATCHDOG_SYNCHRO_LAMPES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_watchdog_synchronisation_lampes_blanches.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>light.hue_white_lamp_bureau_1</code></li>
<li><code>light.hue_white_lamp_bureau_2</code></li>
<li><code>sensor.bureau_etat</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Bureau - Forcer Play ON si PC tourne</b></summary>
<blockquote>
<i>Rallume les Hue Play si elles sont éteintes manuellement alors que</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_FORCER_PLAY_ON.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_forcer_play_on_si_pc_tourne.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>binary_sensor.moniteur_pc</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>BUREAU_ACTIVATION_ECRAN_SYNCHRO</b></summary>
<blockquote>
<i>Synchronise l'état de l'écran avec l'activité du PC bureau.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_ACTIVATION_ECRAN_SYNCHRO.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_activation_ecran_synchro.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>binary_sensor.moniteur_pc</code></li>
<li><code>switch.ecran_p_c_3_play_hue</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🏠 Stores</b> &nbsp;|&nbsp; 2 automation(s) &nbsp;|&nbsp; <i>Volets motorisés salon et bureau (automatiques)</i></summary>
<blockquote>

<details>
<summary>✅ <b>Gestion Simple du Store Salon (Matin/Soir)</b></summary>
<blockquote>
<i>Ouvre le store au lever du soleil (pas avant 6h30) et le ferme au coucher.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/STORES/GESTION_STORE_SALON.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/stores/gestion_simple_du_store_salon_matin_soir.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · ☀️`sun`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>binary_sensor.contact_fenetre_salon_sonoff_contact</code></li>
<li><code>sun.sun</code></li>
<li><code>cover.store_salon</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Gestion Optimisée du Store Bureau</b></summary>
<blockquote>
<i>Priorité Sommeil et Anti-Reflet. Sécurité : Bloque tout mouvement</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/STORES/GESTION_STORE_BUREAU.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/stores/gestion_optimisee_du_store_bureau.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · 🔄`state` · ☀️`sun`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> — <i>Natif HA (SONOFF/Z2M, corrigé 2026-07-19 — pas produit par M_04, qui ne produit que les *_trend)</i></li>
<li><code>binary_sensor.contact_fenetre_bureau_sonoff_contact</code></li>
<li><code>cover.store_bureau</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>⚡ Énergie</b> &nbsp;|&nbsp; 2 automation(s) &nbsp;|&nbsp; <i>Basculement HP/HC, surveillance gros électro, écarts Linky</i></summary>
<blockquote>

<details>
<summary>✅ <b>AUTO. ENERGIE. Basculement Tarif HC/HP — Genelec Appart</b></summary>
<blockquote>
<i>Bascule le tarif des 4 UM Genelec Appart HP/HC aux heures de transition</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/ENERGIE/BASCULEMENT_TARIF_HPHC.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/energie/auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Log Écart Linky vs Nodon</b></summary>
<blockquote>
<i>Enregistre l'écart à 23:59 pile</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/ENERGIE/LOG_ECART_LINKY_NODON.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/energie/log_ecart_linky_vs_nodon.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>notify.log_ecart_energie</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🖥️ Système</b> &nbsp;|&nbsp; 6 automation(s) &nbsp;|&nbsp; <i>DB MariaDB, VS Code éco, GitHub releases, piles, Z2M, DIAG</i></summary>
<blockquote>

<details>
<summary>✅ <b>DB Purge MariaDB + Repack</b></summary>
<blockquote>
<i>Ménage nocturne pour réduire la taille de la base de données (7 jours</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/SYSTEME/DB_PURGE_MARIADB.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/systeme/db_purge_mariadb_repack.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Économie Énergie VS Code</b></summary>
<blockquote>
<i>Coupe VS Code si son CPU dépasse 10% ou s'il est inactif, avec confirmation</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/SYSTEME/ECONOMIE_ENERGIE_VSCODE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/systeme/systeme_economie_energie_vs_code.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📊`numeric_state` · ⚡`event`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.studio_code_server_pourcentage_du_processeur</code></li>
<li><code>binary_sensor.studio_code_server_en_cours_d_execution</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>VEILLE GITHUB — Nouvelle release détectée</b></summary>
<blockquote>
<i>Surveille les flux Feedreader GitHub (HA core + HACS + cartes HACS).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/SYSTEME/VEILLE_GITHUB_RELEASES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/systeme/veille_github_nouvelle_release_detectee.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⚡`event`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Watchdog Piles (HUE/IKEA/SONOFF)</b></summary>
<blockquote>
<i>Vérification 3x/jour basée sur les groupes de la vue synthétique (seuil</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/SYSTEME/WATCHDOG_PILES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/systeme/systeme_watchdog_piles_hue_ikea_sonoff.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Z2M last_seen</b></summary>
<blockquote>
<i>Surveillance des capteurs Zigbee injoignables (plus de 8h ou indisponibles)</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/SYSTEME/Z2M_LAST_SEEN.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/systeme/z2m_last_seen.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)</b></summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/SYSTEME/DIAG_ENREGISTREMENT_JOURNALIER.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/systeme/diag_enregistrement_journalier.yaml">YAML source</a><br>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🍓 Raspberry Pi4 (archivé)</b> &nbsp;|&nbsp; 1 automation(s) &nbsp;|&nbsp; <i>Gestion ventilateur CPU — archivé depuis migration NUC</i></summary>
<blockquote>

<details>
<summary>✅ <b>Raspberry CPU Fan PWM 6 States</b></summary>
<blockquote>
<i>Règle la vitesse du ventilateur du Raspberry en fonction de la température</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/RASPI/RPi4_FAN_PWM.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/_old_avant_staging/raspi/A_rpi_fan_pwm_6_states.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_temperature_du_processeur</code></li>
<li><code>fan.rpi_cooling_fan</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

## ⚠️ Anomalies détectées


---

*Dernière mise à jour : 2026-07-19 | 48 automations (audit entités + comptages catégories corrigés)*
---

## 🔧 04 — SCRIPTS

*Scripts bash maintenance système + scripts HA YAML (clim)*

---

<details>
<summary><b>🐚 SCRIPTS BASH</b> &nbsp;|&nbsp; 3 actifs &nbsp;|&nbsp; Prod : <code>/homeassistant/.scripts/</code> &nbsp;|&nbsp; Local : <code>docs_scripts_SH/</code></summary>
<blockquote>

<details>
<summary><code>audit_md5.sh</code> &nbsp;|&nbsp; Audit MD5 GitHub ↔ prod (YAML config HA)</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_SH_MD/AUDIT_MD5.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/audit_md5.sh">Script source</a><br>
Sortie : <code>/homeassistant/.logs/audit_md5.log</code>
</blockquote>
</details>

<details>
<summary><code>ha_git_backup.sh</code> &nbsp;|&nbsp; Backup git automatique HA → GitHub</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_SH_MD/HA_GIT_BACKUP.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/ha_git_backup.sh">Script source</a><br>
Sortie : repo GitHub <code>home_assistant_re-build</code>
</blockquote>
</details>

<details>
<summary><code>#MP_01_monitor_temp.sh.#</code> &nbsp;|&nbsp; Actif — Raspberry Pi</summary>
<blockquote>
Script de monitoring température (Raspberry Pi) — publie <code>sensor.temperature_cpu_package</code>,
<code>_carte_mere</code>, <code>_core_0-3</code> (utilisés en L4C1/L4C2) via MQTT Discovery.<br>
Pas de doc associée.<br><br>
✅ <b>Confirmé par Eric (2026-07-19)</b> : "ça remonte la T° du CPU et d'autres choses" —
device et fonction confirmés (Raspberry Pi, cf. TODO.txt U-2). Corrige l'ancienne mention
"désactivé/archivé" de cette entrée, qui contredisait TODO.txt ("actif — NE PAS TOUCHER").
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><b>⚙️ SCRIPTS HA YAML</b> &nbsp;|&nbsp; 1 fichier source &nbsp;|&nbsp; Géré via UI HA &nbsp;|&nbsp; Local : <code>docs_scripts_YAML/</code></summary>
<blockquote>

<details>
<summary><code>p1_master_gestion_clim.yaml</code> &nbsp;|&nbsp; Script unique — pilotage clim jour/nuit (param <code>periode</code>)</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_YAML_MD/P1_MASTER_GESTION_CLIM.md">Doc master</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_YAML/p1_master_gestion_clim.yaml">YAML source</a><br>
Appelé par les automations (A-0) et (B-0) — voir section 03.

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : le fichier réel <code>p1_master_gestion_clim.yaml</code> est un
script unique (pas 4 sous-scripts). Le doc master lui-même
(<code>P1_MASTER_GESTION_CLIM.md</code>) précise "Créé par Refactoring LLM local - 2026-06"
et qu'il "remplace le code inline dupliqué dans A0/B0". Les 2 sous-entrées ci-dessous
(J 1-1/1-2/1-3 et J 2-0) décrivent une architecture pré-refactor (scripts
<code>j_1_1_salon_clim_on_off_intelligent</code> etc.) dont le yaml n'existe plus dans
<code>docs_scripts_YAML/</code> — conservées ici à titre historique uniquement.
</blockquote>

<details>
<summary>🗄️ ARCHIVÉ (pré-refactor 2026-06) — J 1-1 / J 1-2 / J 1-3 &nbsp;|&nbsp; Routeurs CLIM ON/OFF INTELLIGENT (Salon / Bureau / Chambre)</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_YAML_MD/SCRIPTS_CLIM_ON_OFF.md">Doc</a><br>
Scripts (obsolètes, non présents dans docs_scripts_YAML/) : <code>j_1_1_salon_clim_on_off_intelligent</code> · <code>j_1_2_bureau_clim_on_off_intelligent</code> · <code>j_1_3_chambre_clim_on_off_intelligent</code>
</blockquote>
</details>

<details>
<summary>🗄️ ARCHIVÉ (pré-refactor 2026-06) — J 2-0 &nbsp;|&nbsp; SECU — ARRÊT CLIM PROTÉGÉ</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_YAML_MD/SCRIPT_J2_0_SECU_ARRET_CLIM.md">Doc</a><br>
Script (obsolète, non présent dans docs_scripts_YAML/) : <code>j_2_0_secu_arret_clim_protege</code>
</blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

## 📋 05 — SYSTÈME MD

*Documents transversaux : index entités, MOC, templates, workflow ReBuild*

---

<details>
<summary><b>ENTITES_INDEX.md</b> &nbsp;|&nbsp; Index global des entités HA (unique_id → fichier source)</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/ENTITES_INDEX.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>MOC_DEPENDANCES.md</b> &nbsp;|&nbsp; Map of Content — dépendances inter-fichiers YAML</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/MOC_DEPENDANCES.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>MOC_DASHBOARD.md</b> &nbsp;|&nbsp; Map of Content — vignettes & pages dashboard (Obsidian)</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/map_of_content_obsidian/MOC_DASHBOARD.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>_TEMPLATE_DOC.md</b> &nbsp;|&nbsp; Template officiel pour créer une doc vignette/automation/script</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/matrisse_template_doc/_TEMPLATE_DOC.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>WORKFLOW_REBUILD.md</b> &nbsp;|&nbsp; Workflow complet du projet ReBuild (étapes, conventions, Git)</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/workflow/WORKFLOW_REBUILD.md">Doc</a>
</blockquote>
</details>
