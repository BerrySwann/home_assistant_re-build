# 🗂️ INDEX GLOBAL - HA ReBuild

*Index unique de navigation - YAML, docs, entités, scripts*
*Dernière mise à jour : 2026-10-13 (soir, /histo S1) - entrées ajoutées pour les index générés GLOBAL_INDEX_IA, GLOBAL_INDEX_VIGNETTES_PAGES, GLOBAL_INDEX_AUTOMATIONS, GLOBAL_INDEX_SCRIPTS_SH et GLOBAL_INDEX_SCRIPTS_YAML et pour 6 scripts python d'index (docs_scripts_SH), tous locaux et non poussés en prod ; compteurs existants non modifiés*
*Dernière mise à jour : 2026-10-12 (soir, /histo S1) - 6 scripts HA (audit_md5, audit_md5_md_yaml, j_1_1, j_1_2, j_1_3, j_2_0) et 2 scripts shell (audit_md5_yaml.sh, mf_vigilance_images.sh) copiés de la prod en local, sans fiche Doc ; liens des scripts YAML corriges apres le regroupement en sous-dossiers Climatisation et Soufflant SDB (20h12) ; compteurs scripts recomptés (SH 5, YAML 9) ; description de l'automation G corrigée en prod*
*Dernière mise à jour : 2026-10-11 (soir, /histo S3) - lettres des automations SDB alignees en prod (H:\automations.yaml, A B C D E F G H Z, entity_id inchanges), dossier L0C0_PAGE_Home (PAGE_Home (L0C0) renomme), skills histo-final et ha-push-docs modifies ; les fiches CARD_*_HOME de la page Home ne sont pas indexees ici (la section 02 ne liste que les 18 vignettes)*
*Dernière mise à jour : 2026-10-11 (après-midi) - dashboard_docs_MD et dashboard_docs_YAML : un sous-dossier 01_vignette et 02_page (02_page_nom si plusieurs pages) par dossier LxCy, PAGE_Home et PAGE_RASPI ; 148 fichiers deplaces, 42 liens corriges*
*Dernière mise à jour : 2026-10-11 - lettres des automations SDB decalees (D->C, E->D, F->E, G->F, H->G, I->H), fiches et YAML renommes en local (prod pas encore modifiee)*
*Dernière mise à jour : 2026-10-11 (matin) - section 05 SKILLS : entrées ajoutées pour ha-resync-tree, journal-modifs et update-arbo (13 skills du projet) ; chemins docs_scripts et un dossier par automation corrigés à 06h42 et 07h13*
*Dernière mise à jour : 2026-10-10 (nuit) - automations : fichiers rangés par catégorie HA (YAML et MD), dossier _old_avant_staging supprimé, 6 fiches créées pour P1_03 (A, B, E, F, H, I), YAML a_, b_, g_ renommés selon l'alias HA ; 88+ liens de la section 03 remis sur les emplacements actuels*
*Dernière mise à jour : 2026-10-08 - nouveau dossier docs/05_docs_skills (10 skills du projet), TODO.txt renommé TODO.md, journaux histo en .md*
*Dernière mise à jour : 2026-10-07 (nuit) - timers de durée SDB : domaine timer (timers/P1_timers/, 4 helpers), automations E et F (soufflant), H et I (sèche-serviettes), G = ancienne E (minuterie sèche-serviettes) ; non testé en conditions réelles*
*Dernière mise à jour : 2026-10-07 (soir) - soufflant SDB : thermostat devenu voyant (heater = switch.voyant_thermostat_soufflant_salle_de_bain, switch template neutre + input_boolean.voyant_thermostat_soufflant_salle_de_bain), garde de démarrage 25 degrés remplacée par une garde de saison (sensor.mode_ete_hiver = cool), automation D : dérive +0,4 degré, verrou de démarrage 2 min -> 30 s*
*Dernière mise à jour : 2026-09-29 (soir) - soufflant SDB : garde 25 degrés en première ligne du script de démarrage, affichage du climate en heat à l'allumage et off à l'arrêt, arrêt forcé après 60 minutes de marche dans le script ; watchdog radiateur réactivé mais inopérant (condition de dérive infaisable avec un capteur à pas de 0,2, jamais déclenché) ; prise de la salle de bain réarmée, la puissance remonte de nouveau (1645 W relevés) ; thermostat passé de 21 à 32 degrés de consigne ; copies de doc des scripts et copie config_system_YAML resynchronisées avec la production ; fiches P1_SDB complétées*
*Dernière mise à jour : 2026-09-28 (soir) - soufflant SDB version finale 2026/2027 : 2 automations (routage + bouton Rodret MQTT), 2 scripts (demarrage 2000 W avec verrou 2 min, arret resistances + ventilateur 1 min 30 + prise), verrou input_boolean, exports YAML et fiche de specification ; correction de 3 liens morts (dossier energie devenu P0_energie, faute « dinamique »), entité du bouton salle de bain renommée, renvoi vers la carte des dépendances à jour*
*Dernière mise à jour : 2026-09-24 - HOME PAGE + L1C2 + L5C1 : carte Congélateur (contact porte, seuils 26/48/235), batterie porte_congel (groupe SONOFF à 13)*
*Dernière mise à jour : 2026-09-23 - section P2 Prises (correctif eco + refonte PC/TV + spies)*
*Dernière mise à jour : 2026-07-19 - correction section L1C1 Météo (entités reelles verifiees, voir historique)*
*Dernière mise à jour : 2026-07-16*

---

## 🧠 00 - IA & CONTEXTE

*Fichiers de référence IA - à lire à la demande selon le contexte de la tâche*

---

<details>
<summary><b>IA_CONTEXT_BASE.md</b> &nbsp;|&nbsp; Base de contexte expert HA (résumé principal)</summary>
<blockquote>
📄 <a href="docs/00_IA/IA_CONTEXT_BASE/IA_CONTEXT_BASE.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>GLOBAL_INDEX_IA.md</b> &nbsp;|&nbsp; Index généré des fichiers de docs/00_IA (qui s'en sert, but, quand les lire, MD5 prod) - local, non poussé en prod</summary>
<blockquote>
📄 <a href="docs/00_IA/GLOBAL_INDEX_IA.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_ia/gen_global_index_ia.py">Générateur</a> (régénéré à chaque /histo, ne pas modifier à la main)
</blockquote>
</details>

<details>
<summary><b>IA_ARBO_DETAIL.md</b> &nbsp;|&nbsp; Arborescence complète prod + local, URLs GitHub raw</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_ARBO_DETAIL/IA_ARBO_DETAIL.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_AUTOMATIONS_NOTIFS.md</b> &nbsp;|&nbsp; Création/modif automations, messages notify, scripts HA</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_AUTOMATIONS_NOTIFS/IA_AUTOMATIONS_NOTIFS.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_CMD_TERMINAL_HA.md</b> &nbsp;|&nbsp; Commandes tree prod, audit MD5, git backup, chemins /homeassistant/, logs HA</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_CMD_TERMINAL_HA/IA_CMD_TERMINAL_HA.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INDEX_AUTOMATIONS.md</b> &nbsp;|&nbsp; Régénération INDEX_AUTOMATIONS, mapping alias → docs/03, anomalies</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_INDEX_AUTOMATIONS/IA_INDEX_AUTOMATIONS.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INDEX_NAVIGATION.md</b> &nbsp;|&nbsp; Régénération INDEX_GLOBAL, ajout vignette/page, mapping entités → fichiers sources</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_INDEX_NAVIGATION/IA_INDEX_NAVIGATION.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INTEGRATIONS_CARTES.md</b> &nbsp;|&nbsp; YAML dashboard, custom:*, intégrations manquantes, palette couleurs</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_INTEGRATIONS_CARTES/IA_INTEGRATIONS_CARTES.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_P4_PRESENCE.md</b> &nbsp;|&nbsp; sensor.presence, format notif avec présence, logique groupe Wi-Fi</summary>
<blockquote>
📄 <a href="docs/00_IA/sous_context_ia/IA_P4_PRESENCE/IA_P4_PRESENCE.md">Doc</a>
</blockquote>
</details>

---

## ⚙️ 01 - CONFIGURATION SYSTÈME

*Fichiers YAML config HA - auto-documentés via headers inline. Seule la doc de configuration générale est ici.*

---

<details>
<summary><b>configuration.md</b> &nbsp;|&nbsp; Structure configuration.yaml, includes, pôles actifs</summary>
<blockquote>
📄 <a href="docs/01_docs_config_system/config_system_MD/configuration.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>timers/P1_timers/</b> &nbsp;|&nbsp; Helpers timer SDB (soufflant 60 mn / 10 mn, sèche-serviettes 2 h / 10 mn)</summary>
<blockquote>
⚙️ <a href="docs/01_docs_config_system/config_system_YAML/timers/P1_timers/P1_timer_60mn_soufflant_sdb.yaml">P1_timer_60mn_soufflant_sdb.yaml</a><br>
⚙️ <a href="docs/01_docs_config_system/config_system_YAML/timers/P1_timers/P1_timer_10mn_soufflant_sdb.yaml">P1_timer_10mn_soufflant_sdb.yaml</a><br>
⚙️ <a href="docs/01_docs_config_system/config_system_YAML/timers/P1_timers/P1_timer_2h_seche_serviettes_sdb.yaml">P1_timer_2h_seche_serviettes_sdb.yaml</a><br>
⚙️ <a href="docs/01_docs_config_system/config_system_YAML/timers/P1_timers/P1_timer_10mn_seche_serviettes_sdb.yaml">P1_timer_10mn_seche_serviettes_sdb.yaml</a><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES/TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES.md">Documentation timers SDB</a>
</blockquote>
</details>


---

## 📊 02 - DASHBOARD (18 vignettes)

*Chemins relatifs depuis la racine du repo GitHub `home_assistant_re-build`*

---

<details>
<summary><b>GLOBAL_INDEX_VIGNETTES_PAGES.md</b> &nbsp;|&nbsp; Index généré des vignettes et des pages du dashboard - local, non poussé en prod</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_vignettes_pages/gen_global_index_vignettes_pages.py">Générateur</a> (régénéré à chaque /histo, ne pas modifier à la main)
</blockquote>
</details>

<details>
<summary><b>L1C1 - MÉTÉO</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~31 entités produites (+17 natives, corrigé 2026-07-19)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/01_vignette/L1C1_VIGNETTE_METEO.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/01_vignette/vignette_L1C1_meteo.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources</b> <i>- ajouté 2026-07-19, icône/texte dynamiques</i></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (3)</i></summary>
<blockquote><ul>
<li><code>weather.vence</code> - pilote l'icône météo (chemin <code>/local/images/meteocons/{state}.svg</code>, ex: "ciel clair"/"ciel couvert")</li>
<li><code>sensor.vence_original_condition</code> - texte condition affiché sous l'icône</li>
<li><code>sensor.th_balcon_nord_temperature</code> - température affichée (SONOFF Z2M)</li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> - 3 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/02_page/PAGE_METEO.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/02_page/page_L1C1_meteo.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#foudre</code> - 14 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.blitzortung_lightning_localisation</code> - <a href="sensors/meteo/M_meteo_sensors_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.timer_foudre</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml">voir fichier</a></li>
<li><code>sensor.eclair_annuel</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_hebdomadaire</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_horaire</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_mensuel</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_quotidien</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.direction_foudre_deg</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml">voir fichier</a></li>
<li><code>sensor.direction_foudre_label</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_direction_foudre_label_card.yaml">voir fichier</a></li>
<li><code>sensor.distance_foudre_km</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_distance_foudre_km_card.yaml">voir fichier</a></li>
<li><code>sensor.dernier_impact_foudre</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_dernier_impact_foudre_card.yaml">voir fichier</a></li>
<li><code>sensor.maison_lightning_azimuth</code> - <i>Natif HA (Blitzortung)</i></li>
<li><code>sensor.maison_lightning_counter</code> - <i>Natif HA (Blitzortung)</i></li>
<li><code>sensor.maison_lightning_distance</code> - <i>Natif HA (Blitzortung)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#alert</code> - 14 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.06_weather_alert</code> - <i>Natif HA</i></li>
<li><code>binary_sensor.meteoalarm</code> - <i>Natif HA (fallback)</i></li>
<li><code>sensor.meteo_france_alertes_image_today</code> - <a href="command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
<li><code>sensor.meteo_france_alertes_image_tomorrow</code> - <a href="command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
<li><code>sensor.alerte_avalanches</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_canicule</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_grand_froid</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_inondation</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_meteo</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_neige_verglas</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_orages</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_pluie_inondation</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vagues_submersion</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vent_violent</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#sun</code> - 6 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code> - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_duree_du_jour_card.yaml">voir fichier</a></li>
<li><code>sensor.moon_phase</code> - <i>Natif HA</i></li>
<li><code>sensor.season</code> - <i>Natif HA</i></li>
<li><code>sensor.tendance_duree_jour</code> - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_tendance_duree_jour_card.yaml">voir fichier</a></li>
<li><code>sensor.variation_quotidienne</code> - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_variation_quotidienne_card.yaml">voir fichier</a></li>
<li><code>sun.sun</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>M_01_meteo_alertes_card.yaml</code> - 10 entité(s) - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.alerte_avalanches</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_canicule</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_grand_froid</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_inondation</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_meteo</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_neige_verglas</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_orages</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_pluie_inondation</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vagues_submersion</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
<li><code>sensor.alerte_vent_violent</code> - <a href="templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_direction_vent_vence_deg_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.direction_vent_vence_deg</code> - <a href="templates/meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_deg_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_direction_vent_vence_label_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_label_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.direction_vent_vence_label</code> - <a href="templates/meteo/M_02_meteo_vent/M_02_meteo_direction_vent_vence_label_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_02_meteo_vitesse_vent_vence_kmh_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_02_meteo_vent/M_02_meteo_vitesse_vent_vence_kmh_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.vitesse_vent_vence_kmh</code> - <a href="templates/meteo/M_02_meteo_vent/M_02_meteo_vitesse_vent_vence_kmh_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_direction_foudre_label_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_direction_foudre_label_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.direction_foudre_label</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_direction_foudre_label_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_distance_foudre_km_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_distance_foudre_km_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.distance_foudre_km</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_distance_foudre_km_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_direction_foudre_deg_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.direction_foudre_deg</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_direction_foudre_deg_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_timer_foudre_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.timer_foudre</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_timer_foudre_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_dernier_impact_foudre_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_dernier_impact_foudre_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dernier_impact_foudre</code> - <a href="templates/meteo/M_03_Meteo_orage_eclaires/M_03_meteo_dernier_impact_foudre_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_sensors_blitzortung.yaml</code> - 1 entité(s) - <a href="sensors/meteo/M_meteo_sensors_blitzortung.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.blitzortung_lightning_localisation</code> - <a href="sensors/meteo/M_meteo_sensors_blitzortung.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_03_meteo_UM_blitzortung.yaml</code> - 5 entité(s) - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclair_annuel</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_hebdomadaire</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_horaire</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_mensuel</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
<li><code>sensor.eclair_quotidien</code> - <a href="utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_05_meteo_duree_du_jour_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_duree_du_jour_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code> - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_duree_du_jour_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_05_meteo_tendance_duree_jour_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_tendance_duree_jour_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.tendance_duree_jour</code> - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_tendance_duree_jour_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_05_meteo_variation_quotidienne_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_variation_quotidienne_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.variation_quotidienne</code> - <a href="templates/meteo/M_05_meteo_cycle_solaire/M_05_meteo_variation_quotidienne_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>carte_meteo_france.yaml</code> - 2 entité(s) - <a href="command_line/meteo/carte_meteo_france.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.meteo_france_alertes_image_today</code> - <a href="command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
<li><code>sensor.meteo_france_alertes_image_tomorrow</code> - <a href="command_line/meteo/carte_meteo_france.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><i>Entités natives HA / intégrations externes (17)</i></summary>
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
<li><code>sensor.vence_original_condition</code> - texte condition (ex: "ciel clair"), utilisé par la Vignette</li>
<li><code>sun.sun</code></li>
<li><code>weather.vence</code></li>
<li><code>zone.home</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : cette section listait des entités obsolètes/inexistantes
(<code>camera.mf_alerte_today/_tomorrow</code> - n'existent pas, <code>camera:</code> désactivé ;
<code>sensor.eclairs_*</code> au pluriel - le vrai nom est <code>sensor.eclair_*</code> singulier ;
<code>sensor.vence_wind_speed</code> - inexistant, vrai nom <code>vence_wind_speed_kmh</code> ;
<code>sensor.direction_du_vent_vence</code>, <code>sensor.vitesse_du_vent_vence</code> - noms
obsolètes sans correspondance réelle, retirés).
Fichiers <code>M_03_meteo_sensors_blitzortung.yaml</code>, <code>M_03_meteo_UM_blitzortung.yaml</code>
et <code>carte_meteo_france.yaml</code> étaient absents de "Fichiers sources" - ajoutés.
<code>M_04_tendances_th_ext_card.yaml</code> était classé à tort ici - son entête déclare
lui-même <code>AVAL : L1C2 Températures</code>, pas L1C1. Déplacé vers la section L1C2.
Vérifié directement dans le corps de chaque fichier yaml, en cohérence avec
DEPENDANCES_GLOBALES_HERMES_V1.md (carte vivante ; l'ancien DEPENDANCES_GLOBALES.md a été archivé le 2026-09-28).
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📎 Fichiers complémentaires</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C1_METEO/TUTO_IMAGES_ALERTES_METEO_FRANCE.md">Tuto Images Alertes Météo France</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C1_01_Meteo/card_duree_du_jour.yaml">Card Durée du Jour</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L1C2 - TEMPÉRATURES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~42 entités (corrigé 2026-07-19)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C2_TEMPERATURES/01_vignette/L1C2_VIGNETTE_TEMPERATURES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/01_vignette/vignette_L1C2_temperatures.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>M_04_tendances_th_est_humidity_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity_trend</code> - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_temperature_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature_trend</code> - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml">voir fichier</a></li>
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
<summary>📄 <b>Page</b> - 10 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C2_TEMPERATURES/02_page/PAGE_TEMPERATURES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C2_02_Temperatures/02_page/page_L1C2_temperatures.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tendances</code> - 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#exterieur</code> - 4 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> - <i>Natif HA (SONOFF Z2M)</i></li>
<li><code>sensor.th_balcon_nord_humidity</code> - <i>Natif HA (SONOFF Z2M)</i></li>
<li><code>sensor.th_balcon_nord_temperature_trend</code> - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml">voir fichier</a></li>
<li><code>weather.vence</code> - <i>HACS - MeteoFrance weather card (pas Natif HA core)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#salon</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_salon_temperature</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#cellier</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_cellier_temperature</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#cuisine</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_cuisine_temperature</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bureau</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_bureau_temperature</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#salle_de_bain</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_salle_de_bain_temperature</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#chambre</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_chambre_temperature</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#tcourbe</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> - <i>Natif HA (SONOFF Z2M - historique graphe)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#hcourbe</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity</code> - <i>Natif HA (SONOFF Z2M - historique graphe)</i></li>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> - 3 entité(s) - <a href="configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> - 2 entité(s) - <a href="templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG_TOTAL_AMHQ.yaml</code> - 1 entité(s) - <a href="templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_rad_total_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> - 3 entité(s) - <a href="templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> - 6 entité(s) - <a href="templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
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
<summary><code>M_02_meteo_vent_vence_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_02_meteo_vent_vence_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>weather.vence</code> - <i>HACS - MeteoFrance weather card (pas Natif HA core)</i></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_est_humidity_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity_trend</code> - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_est_humidity_card.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>M_04_tendances_th_ext_temperature_card.yaml</code> - 1 entité(s) - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature_trend</code> - <a href="templates/meteo/M_04_meteo_tendances/M_04_tendances_th_ext_temperature_card.yaml">voir fichier</a></li>
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
comme ses propres entités produites - en réalité ce fichier ne produit que les 2 sensors
<code>*_trend</code>, vérifié dans son corps. Les pop-up <code>#tcourbe</code>/<code>#hcourbe</code>
(historique/graphe) reclassés en Natif HA (un graphe historique n'a pas besoin d'un TPL).
<code>P1_ui_dashboard.yaml</code> listait à tort <code>climate.radiateur_cuisine</code> comme
produit par ce fichier - c'est une entité native Meross consommée en source, pas produite
(déplacée vers natives). Bloc <code>P1_UM_AMHQ.yaml - switch.radiateur_elec_cuisine</code>
retiré entièrement - ce fichier utility_meter ne produit que des <code>sensor.*_um</code>
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
<summary><b>L1C3 - COMMANDES CLIM</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~61 entités (corrigé 2026-07-19)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C3_CLIM/01_vignette/L1C3_VIGNETTE_CLIM.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/01_vignette/vignette_L1C3_clim.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> - 3 entité(s) - <a href="configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> - 2 entité(s) - <a href="templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.delta_ademe_recommande</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> - 13 entité(s) - <a href="templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
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
<summary>📄 <b>Page</b> - 1 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L1C3_CLIM/02_page/PAGE_CLIM.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L1C3_03_Commandes_Clim/02_page/page_L1C3_clim.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#calcul</code> - 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> - 3 entité(s) - <a href="configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_BV_01_SW_inter_souflant_sdb.yaml</code> - 2 entité(s) - <a href="templates/Inter_BP_Virtuel/P1/P1_BV_IB_SW_inter_souflant_sdb.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
<li><code>switch.voyant_thermostat_soufflant_salle_de_bain</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> - 1 entité(s) - <a href="templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> - 1 entité(s) - <a href="templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> - 11 entité(s) - <a href="templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
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
⚠️ <b>Corrigé le 2026-07-19</b> : <code>climate.soufflant_salle_de_bain</code> retiré partout -
entité inexistante (le soufflant SDB n'a pas d'entité climate, vérifié : aucune occurrence
dans tout <code>config_system_YAML/</code>). <code>climate.radiateur_cuisine</code> déplacé de
"produit par P1_ui_dashboard.yaml" vers natif (c'est une entité Meross consommée, pas produite).
Mise à jour 2026-10-07 : <code>climate.soufflant_salle_de_bain</code> existe en live (helper UI generic_thermostat, devenu voyant, heater = <code>switch.voyant_thermostat_soufflant_salle_de_bain</code>) ; la correction du 2026-07-19 ci-dessus est obsolète.
Bloc <code>P1_UM_AMHQ.yaml - remote.clim_*/switch.radiateur_elec_cuisine</code> retiré
entièrement - un fichier utility_meter ne produit que des <code>sensor.*_um</code> (vérifié :
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
<summary><b>L2C1 - ÉNERGIE GÉNÉRALE</b> &nbsp;|&nbsp; 3 page(s) &nbsp;|&nbsp; ~197 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/01_vignette/L2C1_VIGNETTE_ENERGIE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/01_vignette/vignette_L2C1_energie.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P0_MINI_MAXI_AVG_Genelec_appart.yaml</code> - 2 entité(s) - <a href="sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_conso_maxi_24h</code></li>
<li><code>sensor.genelec_appart_conso_mini_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P0_01_genelec_appart_AMHQ_cost.yaml</code> - 3 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/03_page_principale/PAGE_ENERGIE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/03_page_principale/page_L2C1_energie_principale.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P0_MINI_MAXI_AVG_Genelec_appart.yaml</code> - 2 entité(s) - <a href="sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_conso_maxi_24h</code></li>
<li><code>sensor.genelec_appart_conso_mini_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P0_diag_conso_hebdomadaire_en_cours.yaml</code> - 7 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_hebdomadaire_en_cours.yaml">voir fichier</a></summary>
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
<summary><code>P0_diag_conso_jour_en_cours.yaml</code> - 7 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_jour_en_cours.yaml">voir fichier</a></summary>
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
<summary><code>P0_diag_conso_mois_en_cours.yaml</code> - 7 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Diag/P0_diag_conso_mois_en_cours.yaml">voir fichier</a></summary>
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
<summary><code>P0_01_genelec_appart_AMHQ_cost.yaml</code> - 9 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Genelec_appart/P0_01_genelec_appart_AMHQ_cost.yaml">voir fichier</a></summary>
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
<summary><code>P0_02_ratio_hp_hc.yaml</code> - 3 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Genelec_appart/P0_02_ratio_hp_hc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_ratio_hc_hebdomadaire</code></li>
<li><code>sensor.genelec_appart_ratio_hc_mensuel</code></li>
<li><code>sensor.genelec_appart_ratio_hc_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P0_03_AVG_genelec_appart.yaml</code> - 2 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Genelec_appart/P0_03_AVG_genelec_appart.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_avg_watts_mensuel</code></li>
<li><code>sensor.genelec_appart_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P0_MyElectricalData.yaml</code> - 8 entité(s) - <a href="templates/P0_Energie_total_diag/P0_Linky/P0_MyElectricalData.yaml">voir fichier</a></summary>
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
<summary><code>01_UM_AMHQ.yaml</code> - 3 entité(s) - <a href="utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.genelec_appart_hebdomadaire_um</code></li>
<li><code>sensor.genelec_appart_mensuel_um</code></li>
<li><code>sensor.genelec_appart_quotidien_um</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>02_UM_genelec_appart_HPHC_AMHQ.yaml</code> - 6 entité(s) - <a href="utility_meter/P0_Energie_total/Genelec_appart/P0_UM_AMHQ_HPHC.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/04_page_mensuel/PAGE_ENERGIE_MENSUEL.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/04_page_mensuel/page_L2C1_energie_mensuel.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P2_AVG_AMHQ_prises.yaml</code> - 17 entité(s) - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_AVG_AMHQ_veilles.yaml</code> - 1 entité(s) - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> - 17 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_UM_AMHQ_veilles.yaml</code> - 1 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C1_ENERGIE/02_page_temps_reel/PAGE_ENERGIE_TEMPS_REEL.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C1_04_Energie_Generale/02_page_temps_reel/page_L2C1_energie_temps_reel.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P0_total_pour_les_7_postes.yaml</code> - 6 entité(s) - <a href="templates/P0_Energie_total_diag/P0_total_pour_les_7_postes/P0_total_pour_les_7_postes.yaml">voir fichier</a></summary>
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
<summary><code>P2_AVG_AMHQ_prises.yaml</code> - 17 entité(s) - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_AVG_AMHQ_veilles.yaml</code> - 1 entité(s) - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_current_all_standby.yaml</code> - 1 entité(s) - <a href="templates/P2_prise/P2_I_all_standby_power/P2_current_all_standby.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.all_standby_current</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_POWER_3_TOTAL_ZONE.yaml</code> - 1 entité(s) - <a href="templates/P3_eclairage/P3_POWER_TPL/P3_POWER_3_TOTAL_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_total_group_puissance_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> - 17 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><code>P2_UM_AMHQ_veilles.yaml</code> - 1 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml">voir fichier</a></summary>
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
<summary><b>L2C2 - ÉNERGIE CLIM</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~97 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C2_ENERGIE_CLIM/01_vignette/L2C2_VIGNETTE_ENERGIE_CLIM.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/01_vignette/vignette_L2C2_energie_clim.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> - 3 entité(s) - <a href="configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> - 2 entité(s) - <a href="templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> - 6 entité(s) - <a href="templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
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
<summary><code>P1_UM_AMHQ.yaml</code> - 12 entité(s) - <a href="utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
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
<summary>📄 <b>Page</b> - 1 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C2_ENERGIE_CLIM/02_page/PAGE_ENERGIE_CLIM.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C2_05_Energie_Clim/02_page/page_L2C2_energie_clim.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tendances</code> - 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>configuration.yaml</code> - 3 entité(s) - <a href="configuration.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_DUT_clim_chauffage.yaml</code> - 4 entité(s) - <a href="sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dut_clim_bureau</code></li>
<li><code>sensor.dut_clim_chambre</code></li>
<li><code>sensor.dut_clim_salon</code></li>
<li><code>sensor.dut_radiateur_cuisine</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_01_clim_logique_system_autom.yaml</code> - 2 entité(s) - <a href="templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_affichage</code></li>
<li><code>sensor.temperature_moyenne_interieure</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_AVG.yaml</code> - 12 entité(s) - <a href="templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_UNITE.yaml">voir fichier</a></summary>
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
<summary><code>P1_AVG_TOTAL_AMHQ.yaml</code> - 1 entité(s) - <a href="templates/P1_clim_chauffage/P1_AVG/P1_AVG_AMHQ_TOTAL.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.clim_rad_total_avg_watts_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_DUT_TOTAL_SDB.yaml</code> - 1 entité(s) - <a href="templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.dut_sdb_total</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_TOTAL_AMHQ.yaml</code> - 3 entité(s) - <a href="templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.conso_clim_rad_total</code></li>
<li><code>sensor.conso_clim_rad_total_mensuel</code></li>
<li><code>sensor.conso_clim_rad_total_quotidien</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P1_ui_dashboard.yaml</code> - 11 entité(s) - <a href="templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml">voir fichier</a></summary>
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
<summary><code>P1_UM_AMHQ.yaml</code> - 24 entité(s) - <a href="utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml">voir fichier</a></summary>
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
<summary><b>L2C3 - ÉNERGIE ÉCLAIRAGE</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~85 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/01_vignette/L2C3_VIGNETTE_ECLAIRAGE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/01_vignette/vignette_L2C3_energie_eclairage.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P3_TPL_AMHQ_2_ZONE.yaml</code> - 12 entité(s) - <a href="templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
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
<summary><code>P3_TPL_AMHQ_3_TOTAL.yaml</code> - 2 entité(s) - <a href="templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_3_TOTAL.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_total_unit_mensuel_kwh_tpl</code></li>
<li><code>sensor.eclairage_total_unit_quotidien_kwh_tpl</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>etats_status.yaml</code> - 6 entité(s) - <a href="templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L2C3_ENERGIE_ECLAIRAGE/02_page/PAGE_ENERGIE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L2C3_06_Energie_Eclairage/02_page/page_L2C3_energie_eclairage.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P3_AVG_AMHQ_2_ZONE.yaml</code> - 5 entité(s) - <a href="templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.eclairage_appart_3_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_bureau_5_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_chambre_4_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_salon_5_avg_watts_mensuel</code></li>
<li><code>sensor.eclairage_sdb_2_avg_watts_mensuel</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P3_TPL_AMHQ_1_UNITE.yaml</code> - 38 entité(s) - <a href="templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_1_UNITE.yaml">voir fichier</a></summary>
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
<summary><code>P3_TPL_AMHQ_2_ZONE.yaml</code> - 20 entité(s) - <a href="templates/P3_eclairage/P3_ENERGIE_TPL/P3_TPL_AMHQ_2_ZONE.yaml">voir fichier</a></summary>
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
attribués à tort à <code>P1_ui_dashboard.yaml</code> (fichier Pôle 1 clim - vérifié dans
son corps, aucune entité <code>light.*</code> nulle part dedans). <code>light.hue_white_lamp_salle_de_bain</code>
et <code>switch.relais_lumiere_sdb_sonoff</code> étaient attribués à tort à
<code>P3_UM_AMHQ_1_UNITE.yaml</code> (fichier utility_meter - vérifié, ne produit que des
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
<summary><b>L3C1 - COMMANDES ÉCLAIRAGE</b> &nbsp;|&nbsp; 2 page(s) &nbsp;|&nbsp; ~43 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/01_vignette/L3C1_VIGNETTE_ECLAIRAGE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/01_vignette/vignette_L3C1_eclairage.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>etats_status.yaml</code> - 7 entité(s) - <a href="templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml">voir fichier</a></summary>
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
<summary><code>P2_UM_AMHQ_prises.yaml</code> - 1 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
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
(fichier utility_meter) - vérifié dans les deux corps, aucun des deux ne produit d'entité
<code>light.*</code>. Ce sont toutes des entités natives Hue Bridge, regroupées en natives.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/02_page/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/02_page_gauche/page_L3C1_eclairage_gauche.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>etats_status.yaml</code> - 5 entité(s) - <a href="templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.lumiere_couloir_etat</code></li>
<li><code>sensor.lumiere_cuisine_etat</code></li>
<li><code>sensor.lumiere_entree_etat</code></li>
<li><code>sensor.lumiere_salon_etat</code></li>
<li><code>sensor.lumiere_table_etat</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>S_01_STORES.yaml</code> - 1 entité(s) - <a href="templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
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
<summary>📄 <b>Page Droite</b> - 3 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C1_ECLAIRAGE/02_page/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C1_07_Commandes_Eclairage/03_page_droite/page_L3C1_eclairage_droite.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tete_de_lit</code> - 2 entité(s)</summary>
<blockquote><ul>
<li><code>light.hue_color_candle_chambre_eric</code> - <i>Natif HA (Hue)</i></li>
<li><code>light.hue_color_candle_chambre_gege</code> - <i>Natif HA (Hue)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bureau</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.bureau</code> - <i>Natif HA (Hue)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ecranpc</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.moniteur_pc</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>etats_status.yaml</code> - 6 entité(s) - <a href="templates/P3_eclairage/P3_ui_dashboard/P3_etats_status.yaml">voir fichier</a></summary>
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
<summary><code>S_01_STORES.yaml</code> - 1 entité(s) - <a href="templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>cover.store_bureau</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_prises.yaml</code> - 1 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml">voir fichier</a></summary>
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
<summary><b>L3C2 - COMMANDES PRISES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~6 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C2_PRISES/01_vignette/L3C2_VIGNETTE_PRISES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/01_vignette/vignette_L3C2_prises.yaml">YAML Vignette</a>



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
<code>P2_UM_AMHQ_prises.yaml</code> (fichier utility_meter - ne produit que des
<code>sensor.*_um</code>, vérifié). Ce sont des switches natifs Z2M IKEA, déplacés vers natives.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C2_PRISES/02_page/PAGE_PRISES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C2_08_Commandes_Prises/02_page/page_L3C2_prises.yaml">YAML Page</a>



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
<code>P2_UM_AMHQ_prises.yaml</code> (fichier utility_meter - ne produit que des
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
<summary><b>L3C3 - STORES & FENÊTRES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~15 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C3_STORES/01_vignette/L3C3_VIGNETTE_STORES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/01_vignette/vignette_L3C3_stores.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>S_01_STORES.yaml</code> - 2 entité(s) - <a href="templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L3C3_STORES/02_page/PAGE_STORES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L3C3_09_Stores_Fenetres/02_page/page_L3C3_stores.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>S_01_STORES.yaml</code> - 2 entité(s) - <a href="templates/Stores/S_01_STORES.yaml">voir fichier</a></summary>
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
des entités produites - vérifié dans le corps du fichier (il ne produit que les 2
<code>*_status</code>). <code>sensor.th_balcon_nord_temperature</code> était attribué à
<code>M_04_tendances_th_ext_card.yaml</code> qui ne produit que le sensor <code>*_trend</code> -
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
<summary><b>L4C2 - PROXMOX (PVE)</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~5 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C2_PROXMOX/01_vignette/L4C2_VIGNETTE_PROXMOX.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Proxmox/01_vignette/vignette_L4C2_proxmox.yaml">YAML Vignette</a>



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
<li><code>sensor.proxmox_cpu_package</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : <code>sensor.proxmox_cpu_package</code> n'existe dans
aucun fichier <code>config_system_YAML/</code> (vérifié) - publié par le script externe
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C2_PROXMOX/02_page/PAGE_PROXMOX.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C2_11_Proxmox/02_page/page_L4C2_proxmox.yaml">YAML Page</a>


</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L4C1 - MINI PC (NUC)</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~25 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C1_MINI_PC/01_vignette/L4C1_VIGNETTE_MINI_PC.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Mini_PC/01_vignette/vignette_L4C1_mini_pc.yaml">YAML Vignette</a>



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
<li><code>sensor.proxmox_cpu_package</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> - 5 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C1_MINI_PC/02_page_mini_pc/PAGE_MINI_PC.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C1_10_Mini_PC/02_page/page_L4C1_mini_pc.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#speed</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_utilisation_du_processeur</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#temp</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.proxmox_cpu_package</code> - <i>Natif HA (MQTT Discovery - MP_01_monitor_temp.sh)</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#conso</code> - 7 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code> - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code> - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_current</code> - <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_energy</code> - <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code> - <a href="utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_power</code> - <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code> - <a href="utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#disk</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_espace_utilise</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#memory</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_memoire_utilisee</code> - <i>Natif HA</i></li>
</ul></blockquote>
</details>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>P2_AVG_AMHQ_mini_pc.yaml</code> - 2 entité(s) - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code> - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code> - <a href="templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>P2_UM_AMHQ_mini_pc.yaml</code> - 2 entité(s) - <a href="utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code> - <a href="utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code> - <a href="utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml">voir fichier</a></li>
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
<li><code>sensor.proxmox_carte_mere</code></li>
<li><code>sensor.proxmox_core_0</code></li>
<li><code>sensor.proxmox_core_1</code></li>
<li><code>sensor.proxmox_core_2</code></li>
<li><code>sensor.proxmox_core_3</code></li>
<li><code>sensor.proxmox_cpu_package</code></li>
</ul></blockquote>
</details>

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : les 6 <code>sensor.proxmox_*</code> (carte_mere, core_0-3,
cpu_package) n'existent dans aucun fichier <code>config_system_YAML/</code> - publiés par
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C1_MINI_PC/03_page_raspi/PAGE_RASPI.md">Page RPi (transitoire)</a><br>
</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>L4C3 - MISES À JOUR HA</b> &nbsp;|&nbsp; 2 page(s) &nbsp;|&nbsp; ~9 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/01_vignette/L4C3_VIGNETTE_MAJ.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/01_vignette/vignette_L4C3_maj_ha.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>Mise_a_jour_home_assistant.yaml</code> - 1 entité(s) - <a href="templates/utilitaires/Mise_a_jour_home_assistant.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/02_page/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/02_page_gauche/page_L4C3_maj_ha_gauche.yaml">YAML Page</a>



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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L4C3_MAJ_HA/02_page/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L4C3_12_MAJ_HA/03_page_droite/page_L4C3_maj_ha_droite.yaml">YAML Page</a>



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
<summary><b>L5C1 - PILES & BATTERIES</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~35 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C1_PILES_BATTERIES/01_vignette/L5C1_VIGNETTE_BATTERIES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/01_vignette/vignette_L5C1_batteries_piles.yaml">YAML Vignette</a>



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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C1_PILES_BATTERIES/02_page/PAGE_BATTERIES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C1_13_Batteries_Piles/02_page/page_L5C1_batteries_piles.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (32)</i></summary>
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
<li><code>sensor.inter_soufflant_salle_de_bain_ikea_rodret_battery</code></li>
<li><code>sensor.inter_salon_4_ikea_battery</code></li>
<li><code>sensor.inter_somrig_battery</code></li>
<li><code>sensor.inter_tv_chambre_ikea_rodret_battery</code></li>
<li><code>sensor.porte_congel_battery</code></li>
<li><code>sensor.poussoir_ikea_tradfri_battery</code></li>
<li><code>sensor.th_balcon_nord_battery</code></li>
<li><code>sensor.th_bureau_battery</code></li>
<li><code>sensor.th_cellier_battery</code></li>
<li><code>sensor.th_chambre_battery</code></li>
<li><code>sensor.th_cuisine_battery</code></li>
<li><code>sensor.th_salle_de_bain_battery</code></li>
<li><code>sensor.th_salon_battery</code></li>
<li><code>sensor.tongel_battery</code></li>
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
<summary><b>L5C2 - BATTERIES PORTABLES</b> &nbsp;|&nbsp; 2 page(s) &nbsp;|&nbsp; ~49 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/01_vignette/L5C2_VIGNETTE_BATTERIES_PORTABLES.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/01_vignette/vignette_L5C2_batteries_portables.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources</b> <i>- ajouté 2026-07-19, remontée résumé batterie/état</i></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (14)</i></summary>
<blockquote><ul>
<li><code>sensor.eric_battery_level</code></li>
<li><code>sensor.eric_battery_state</code></li>
<li><code>sensor.mamour_battery_level</code></li>
<li><code>sensor.mamour_battery_state</code></li>
<li><code>sensor.ne2213_eric_battery_level</code></li>
<li><code>sensor.ne2213_eric_battery_state</code></li>
<li><code>sensor.ne2213_mamour_battery_level</code></li>
<li><code>sensor.ne2213_mamour_battery_state</code></li>
<li><code>sensor.gm1901_battery_level</code></li>
<li><code>sensor.gm1901_battery_state</code></li>
<li><code>sensor.sm_a530f_battery_level</code></li>
<li><code>sensor.sm_a530f_battery_state</code></li>
<li><code>sensor.tablette_battery_level</code></li>
<li><code>sensor.tablette_battery_state</code></li>
</ul></blockquote>
</details>

<blockquote>
ℹ️ Ces 14 entités (battery_level + battery_state des 7 appareils) sont un sous-ensemble
des entités déjà détaillées dans Page Gauche (eric/ne2213_eric/sm_a530f/tablette) et
Page Droite (gm1901/mamour/ne2213_mamour) - pas de nouvelles entités, pas d'impact sur
le total ~49.
</blockquote>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/02_page/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/02_page_gauche/page_L5C2_batteries_portables_gauche.yaml">YAML Page</a>



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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C2_BATTERIES_PORTABLES/02_page/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C2_14_Batteries_Portables/03_page_droite/page_L5C2_batteries_portables_droite.yaml">YAML Page</a>



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
<summary><b>L5C3 - MARIADB</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~5 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/01_vignette/L5C3_VIGNETTE_MARIADB.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/01_vignette/vignette_L5C3_mariadb.yaml">YAML Vignette</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>sql.yaml</code> - 1 entité(s) - <a href="sql.yaml">voir fichier</a></summary>
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
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L5C3_MARIADB/02_page_principale/PAGE_SYSTEME.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L5C3_15_MariaDB/02_page_mariadb/page_L5C3_mariadb.yaml">YAML Page</a>



<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>github_maintenance.yaml</code> - 3 entité(s) - <a href="command_line/github_maintenance/github_maintenance.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.backup_github_status</code></li>
<li><code>sensor.git_last_weekly_tag</code></li>
<li><code>sensor.github_default_branch</code></li>
</ul></blockquote>
</details>

<details>
<summary><code>sql.yaml</code> - 1 entité(s) - <a href="sql.yaml">voir fichier</a></summary>
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
<summary><b>L6C1 - QUALITÉ AIR (APPART)</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~15 entités (corrigé 2026-07-19)</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C1_AIR_QUALITE/01_vignette/L6C1_VIGNETTE_AIR_QUALITE.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/01_vignette/vignette_L6C1_air_qualite.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources</b> <i>- ajouté 2026-07-19, grille PM2.5+tCOV par pièce</i></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (6)</i></summary>
<blockquote><ul>
<li><code>sensor.qualite_air_salon_ikea_pm25</code> - déjà listé dans "Fichiers sources" de la Page</li>
<li><code>sensor.qualite_air_bureau_ikea_pm25</code> - déjà listé dans "Fichiers sources" de la Page</li>
<li><code>sensor.qualite_air_chambre_ikea_pm25</code> - déjà listé dans "Fichiers sources" de la Page</li>
<li><code>sensor.qualite_air_salon_ikea_voc_index</code> - nouveau, non consolidé ailleurs (visible en pop-up #scov)</li>
<li><code>sensor.qualite_air_bureau_ikea_voc_index</code> - nouveau, non consolidé ailleurs (visible en pop-up #bcov)</li>
<li><code>sensor.qualite_air_chambre_ikea_voc_index</code> - nouveau, non consolidé ailleurs (visible en pop-up #ccov)</li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> - 6 pop-up(s)</summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C1_AIR_QUALITE/02_page/PAGE_AIR_QUALITE.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C1_16_Air_Qualite/02_page/page_L6C1_air_qualite.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#spm25</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_salon_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#scov</code> - 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_salon_ikea_voc_index</code> - <i>Natif HA</i></li>
<li><code>sensor.tcov_salon_ppb</code> - <a href="templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_salon_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>
<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : ce pop-up "Salon COV" contenait à tort une entité PM2.5
Bureau et un tCOV Bureau - incohérent avec son propre nom et la logique du dashboard
(un pop-up COV d'une pièce ne montre pas le PM2.5 d'une autre pièce). Recomposé avec les
3 entités COV/tCOV réelles du Salon (native + TPL + SEN), vérifiées dans les fichiers sources.
</blockquote>

<details>
<summary>💬 Pop-up <code>#bpm25</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bcov</code> - 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_bureau_ikea_voc_index</code> - <i>Natif HA</i></li>
<li><code>sensor.tcov_bureau_ppb</code> - <a href="templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_bureau_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>
<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : ce pop-up "Bureau COV" contenait à tort une entité PM2.5
Chambre et un tCOV Chambre - même erreur de croisement qu'au pop-up #scov. Recomposé avec
les 3 entités COV/tCOV réelles du Bureau.
</blockquote>

<details>
<summary>💬 Pop-up <code>#cpm25</code> - 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_chambre_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ccov</code> - 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_chambre_ikea_voc_index</code> - <i>Natif HA</i></li>
<li><code>sensor.tcov_chambre_ppb</code> - <a href="templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>
<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : ce pop-up "Chambre COV" n'avait qu'1 entité alors que les
pop-up COV des autres pièces en ont 3 (native + TPL + SEN) - complété par cohérence avec
#scov/#bcov, en s'appuyant sur les mêmes 3 fichiers sources déjà vérifiés.
</blockquote>


<details>
<summary><b>📂 Fichiers sources</b></summary>
<blockquote>

<details>
<summary><code>A_01_AIR_QUALITY.yaml</code> - 6 entité(s) - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.pm2_5_chambre_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.pm2_5_salon_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_bureau_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_salon_moy_24h</code> - <a href="sensors/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
</ul></blockquote>
</details>

<details>
<summary><code>A_01_AIR_QUALITY.yaml</code> - 3 entité(s) - <a href="templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></summary>
<blockquote><ul>
<li><code>sensor.tcov_bureau_ppb</code> - <a href="templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
<li><code>sensor.tcov_chambre_ppb</code> - <a href="templates/Air_quality/A_01_AIR_QUALITY.yaml">voir fichier</a></li>
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
<summary><b>L6C2 - POLLUTION & POLLEN</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~19 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C2_POLLUTION_POLLEN/01_vignette/L6C2_VIGNETTE_POLLUTION_POLLEN.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/01_vignette/vignette_L6C2_pollution_pollen.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources</b> <i>- ajouté 2026-07-19, résumé Air/Pollen coloré</i></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (2)</i></summary>
<blockquote><ul>
<li><code>sensor.qualite_globale_vence</code> - déjà listé dans "Fichiers sources" de la Page</li>
<li><code>sensor.qualite_globale_pollen_vence</code> - déjà listé dans "Fichiers sources" de la Page</li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C2_POLLUTION_POLLEN/02_page/PAGE_POLLUTION_POLLEN.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C2_17_Pollution_Pollen/02_page/page_L6C2_pollution_pollen.yaml">YAML Page</a>



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
<summary><b>L6C3 - VIGILANCE EAU</b> &nbsp;|&nbsp; 1 page(s) &nbsp;|&nbsp; ~3 entités</summary>
<blockquote>

<details>
<summary>🖼️ <b>Vignette</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C3_VIGIEAU/01_vignette/L6C3_VIGNETTE_VIGIEAU.md">Doc Vignette</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/01_vignette/vignette_L6C3_vigieau.yaml">YAML Vignette</a>

<details>
<summary><b>📂 Fichiers sources</b> <i>- ajouté 2026-07-19, icône/texte niveau alerte</i></summary>
<blockquote>

<details>
<summary><i>Entités natives HA / intégrations externes (1)</i></summary>
<blockquote><ul>
<li><code>sensor.alert_level_in_vence</code> - déjà listé dans "Fichiers sources" de la Page</li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="docs/02_docs_dashboard/dashboard_docs_MD/L6C3_VIGIEAU/02_page/PAGE_VIGIEAU.md">Doc Page</a><br>
⚙️ <a href="docs/02_docs_dashboard/dashboard_docs_YAML/L6C3_18_VigiEau/02_page/page_L6C3_vigieau.yaml">YAML Page</a>



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

## ⚙️ 03 - AUTOMATIONS (54 automations)

*Chemins relatifs depuis `docs_automations/`*

<details>
<summary><b>GLOBAL_INDEX_AUTOMATIONS.md</b> &nbsp;|&nbsp; Index généré des automations (alias, id prod, id local, entity HA, fiche, YAML) - local, non poussé en prod</summary>
<blockquote>
📄 <a href="docs/03_docs_automations/GLOBAL_INDEX_AUTOMATIONS.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_automations/gen_global_index_automations.py">Générateur</a> (régénéré à chaque /histo, ne pas modifier à la main)
</blockquote>
</details>

**11 catégories · 52 automations · 53 entrées dans l'index**

<details>
<summary>📋 <b>Table des matières</b></summary>
<blockquote>
<b>🔧 Backup Git</b> (7 automations)<br>
<b>🌤️ Météo</b> (5 automations)<br>
<b>🌡️ P1 - Clim & Chauffage</b> (10 automations)<br>
<b>🍳 P1 - Cuisine</b> (2 automations)<br>
<b>🚿 P1 - Salle de Bain</b> (9 automations)<br>
<b>🔌 P2 - Prises</b> (3 automations)<br>
<b>💡 P3 - Éclairage</b> (7 automations)<br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_ALERTE_KO/GIT_ALERTE_KO.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/00_backup_alerte_si_ko_15_min/00_backup_alerte_si_ko_15_min.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_HOURLY/GIT_HOURLY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/01_backup_git_hourly_h_10/01_backup_git_hourly_h_10.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[02-Backup] Git daily (03:00)</b></summary>
<blockquote>
<i>Backup natif HA + push Git quotidien à 03h00</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_DAILY/GIT_DAILY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/02_backup_git_daily_03_00/02_backup_git_daily_03_00.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[03-Backup] Git weekly (dim 01:30)</b></summary>
<blockquote>
<i>Backup natif HA + push + tag weekly chaque dimanche à 01:30</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_WEEKLY/GIT_WEEKLY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/03_backup_git_weekly_dim_01_30/03_backup_git_weekly_dim_01_30.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[04-Backup] Git push manuel</b></summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_PUSH_MANUEL/GIT_PUSH_MANUEL.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/04_backup_git_push_manuel/04_backup_git_push_manuel.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_PUSH_WEEKLY_MANUEL/GIT_PUSH_WEEKLY_MANUEL.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/05_backup_git_push_weekly_manuel/05_backup_git_push_weekly_manuel.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Backup%20HA%20-%20GitHub/GIT_AU_DEMARRAGE/GIT_AU_DEMARRAGE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Backup%20HA%20-%20GitHub/git_push_au_demarrage_ha/git_push_au_demarrage_ha.yaml">YAML source</a><br>

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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Météo/ALERTE_METEO_CARTES/ALERTE_METEO_CARTES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Météo/alerte_meteo_france_actualisation_des_cartes/alerte_meteo_france_actualisation_des_cartes.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Météo/UPDATE_PREV_TEMPERATURE/UPDATE_PREV_TEMPERATURE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Météo/update_previous_temperature/update_previous_temperature.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Météo/UPDATE_PREV_HUMIDITY/UPDATE_PREV_HUMIDITY.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Météo/update_previous_humidity/update_previous_humidity.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Météo/NOTIF_FOUDRE/NOTIF_FOUDRE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Météo/notification_de_la_foudre/notification_de_la_foudre.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Météo/MAJ_TEMPS_FOUDRE/MAJ_TEMPS_FOUDRE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Météo/mettre_a_jour_le_temps_du_dernier_impact_de_foudre/mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml">YAML source</a><br>
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
<summary><b>🌡️ P1 - Clim & Chauffage</b> &nbsp;|&nbsp; 10 automation(s) &nbsp;|&nbsp; <i>Logique de climatisation, notifications, gardien éco</i></summary>
<blockquote>

<details>
<summary>✅ <b>(A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)</b></summary>
<blockquote>
<i>Pilotage clims jour avec boucle de relance et notification ciblée fenêtres</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/A0_CLIM_JOUR/A0_CLIM_JOUR.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00/a_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · 🔄`state`<br>
<br><details>
<summary>🔌 Entités (14) <i>- corrigé 2026-07-19, triggers réels du fichier</i></summary>
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
<a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/p1_master_gestion_clim/p1_master_gestion_clim.yaml">script p1_master_gestion_clim.yaml</a> -
ces entités ne sont pas dans l'automation elle-même, retirées de la liste ci-dessus.
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30)</b></summary>
<blockquote>
<i>Pilotage clims nuit avec boucle de relance et notification ciblée fenêtres</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/B0_CLIM_NUIT/B0_CLIM_NUIT.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30/b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · 🔄`state`<br>
<br><details>
<summary>🔌 Entités (14) <i>- corrigé 2026-07-19, triggers réels du fichier</i></summary>
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
<a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/p1_master_gestion_clim/p1_master_gestion_clim.yaml">script p1_master_gestion_clim.yaml</a> -
ces entités ne sont pas dans l'automation elle-même, retirées de la liste ci-dessus.
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(D) Notification température Up ou Down de (7h30 -> 21h00)</b></summary>
<blockquote>
<i>Envoie le message personnalisé de clim si le texte change, OU au réveil</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/C_NOTIF_TEMP_JOUR/C_NOTIF_TEMP_JOUR.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/c_notification_temperature_up_ou_down_7h30_21h00/c_notification_temperature_up_ou_down_7h30_21h00.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> - <i>Natif HA (SONOFF/Z2M, corrigé 2026-07-19 - pas produit par M_04, qui ne produit que les *_trend)</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(E) Notification température Up ou Down de (21h00 -> 7h30)</b></summary>
<blockquote>
<i>Envoie le message personnalisé de clim si le texte change, OU au début</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/D_NOTIF_TEMP_NUIT/D_NOTIF_TEMP_NUIT.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/d_notification_temperature_up_ou_down_21h00_7h30/d_notification_temperature_up_ou_down_21h00_7h30.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> - <i>Natif HA (SONOFF/Z2M, corrigé 2026-07-19 - pas produit par M_04, qui ne produit que les *_trend)</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(F) (CLIM) Notification de fermeture des fenêtres</b></summary>
<blockquote>
<i>Envoie une notification lorsqu'une fenêtre est fermée.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/E_NOTIF_FERMETURE_FENETRES/E_NOTIF_FERMETURE_FENETRES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/e_clim_notification_de_fermeture_des_fenetres/e_clim_notification_de_fermeture_des_fenetres.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(G) (CLIM) Automatisation Arrêt Clim Notification</b></summary>
<blockquote>
<i>Notification quand une clim est coupée manuellement, seulement si</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/F_ARRET_CLIM_NOTIF/F_ARRET_CLIM_NOTIF.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/f_clim_automatisation_arret_clim_notification/f_clim_automatisation_arret_clim_notification.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/G_NOTIF_MODE_CHANGEMENT/G_NOTIF_MODE_CHANGEMENT.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/g_clim_notification_de_changement_de_mode_ete_fan_hiver/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/H_DEBUG_FORCE_MODE/H_DEBUG_FORCE_MODE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/h_clim_debug_force_mode_correct_securite/h_clim_debug_force_mode_correct_securite.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/I_SYNCHRO_NOTIF_PRISE_COUPEE/I_SYNCHRO_NOTIF_PRISE_COUPEE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/i_synchro_notif_clim_si_prise_coupee/i_synchro_notif_clim_si_prise_coupee.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(K) (DEBUG) Notifier les changements de message clim (Mobile)</b></summary>
<blockquote>
<i>Surveille et notifie les changements d'état du message personnalisé.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_01_CLIM_CHAUFFAGE/J_DEBUG_NOTIF_MESSAGE_CLIM/J_DEBUG_NOTIF_MESSAGE_CLIM.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/j_debug_notifier_les_changements_de_message_clim_mobile/j_debug_notifier_les_changements_de_message_clim_mobile.yaml">YAML source</a><br>
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
<summary><b>🍳 P1 - Cuisine</b> &nbsp;|&nbsp; 2 automation(s) &nbsp;|&nbsp; <i>Chauffage bain d'huile cuisine (plannings semaine/vacances)</i></summary>
<blockquote>

<details>
<summary>✅ <b>A - Chauffage Cuisine (entre 4h45 & 7h LMMJ ou 5:45h & 8h VSD avec T° 19,9°</b></summary>
<blockquote>
<i>Allume ou éteint le chauffage selon la température (19,9° <-> 20.5°)  aux</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_02_Cuisine/A_CHAUFFAGE_CUISINE/A_CHAUFFAGE_CUISINE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_02_Cuisine/a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9/a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_02_Cuisine/B_CHAUFFAGE_CUISINE_VACANCES/B_CHAUFFAGE_CUISINE_VACANCES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_02_Cuisine/b_chauffage_cuisine_vacances/b_chauffage_cuisine_vacances.yaml">YAML source</a><br>
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
<summary><b>🚿 P1 - Salle de Bain</b> &nbsp;|&nbsp; 9 automation(s) &nbsp;|&nbsp; <i>Soufflant SDB version finale 2026/2027 (routage + bouton Rodret) + gestion intelligente + watchdog soufflant + minuterie sèche-serviettes</i></summary>
<blockquote>

<details>
<summary>✅ <b>A - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT</b></summary>
<blockquote>
<i>Cycle complet : Démarrage, Régulation, et Auto-off 60 min avec refroidissement</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/Z_SOUFFLANT_SDB_GESTION_INTELLIGENTE/Z_SOUFFLANT_SDB_GESTION_INTELLIGENTE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant/z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml">YAML source</a><br>
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
<summary>✅ <b>C - SALLE DE BAIN : WATCHDOG SÉCURITÉ SOUFFLANT</b></summary>
<blockquote>
<i>Reset physique si T > 25°C, uniquement si la prise est alimentée</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/C_WATCHDOG_SOUFFLANT_SDB/C_WATCHDOG_SOUFFLANT_SDB.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/c_salle_de_bain_watchdog_securite_soufflant/c_salle_de_bain_watchdog_securite_soufflant.yaml">YAML source</a><br>
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
<summary>✅ <b>F - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu 2h)</b> (ex E puis G)</summary>
<blockquote>
<i>Timer de 2h après détection de chauffe. Sécurité anti-redémarrage incluse.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/F_MINUTERIE_SECHE_SERVIETTES/F_MINUTERIE_SECHE_SERVIETTES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/f_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h/f_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_power</code></li>
<li><code>switch.prise_seche_serviette_salle_de_bain_nous</code></li>
</ul></blockquote>
</details>

<details>
<summary>✅ <b>B - 2026/09/28 - SDB SOUFFLANT : ROUTAGE (INTERRUPTEUR VERS SEQUENCES)</b></summary>
<blockquote>
<i>Entree unique du soufflant SDB : l'interrupteur virtuel declenche le demarrage ou l'arret. Verrou de 30 s tenu par les scripts.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/B_SOUFFLANT_SDB_ROUTAGE/B_SOUFFLANT_SDB_ROUTAGE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/b_soufflant_sdb_routage/b_soufflant_sdb_routage.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
<li><code>script.sdb_soufflant_demarrer</code></li>
<li><code>script.sdb_soufflant_arreter</code></li>
</ul></blockquote>
</details>

<details>
<summary>✅ <b>D - SDB - SOUFFLANT - DECOMPTE 60 MIN (timer)</b></summary>
<blockquote>
<i>Lance le timer 60 mn à la mise en marche réelle, l'annule à l'arrêt, coupe l'interrupteur à la fin d'un timer (non testé).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/D_SDB_SOUFFLANT_DECOMPTE_60MIN/D_SDB_SOUFFLANT_DECOMPTE_60MIN.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/d_sdb_soufflant_decompte_60min_timer/d_sdb_soufflant_decompte_60min_timer.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`, ⏱`timer.finished`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
<li><code>timer.soufflant_sdb_60mn</code></li>
<li><code>timer.soufflant_sdb_10mn</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>E - SDB - SOUFFLANT - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)</b></summary>
<blockquote>
<i>30 s après le démarrage de HA : lève le verrou, lance le 10 mn si soufflant en marche sans timer actif (non testé).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/E_SDB_SOUFFLANT_RATTRAPAGE_DEMARRAGE_HA/E_SDB_SOUFFLANT_RATTRAPAGE_DEMARRAGE_HA.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/e_sdb_soufflant_rattrapage_demarrage_ha_timer/e_sdb_soufflant_rattrapage_demarrage_ha_timer.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant`<br>
<br><details>
<summary>🔌 Entités (4)</summary>
<blockquote><ul>
<li><code>input_boolean.verrou_soufflant_salle_de_bain</code></li>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
<li><code>timer.soufflant_sdb_60mn</code></li>
<li><code>timer.soufflant_sdb_10mn</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>G - SDB - SECHE-SERVIETTES - DECOMPTE 2 H (timer)</b></summary>
<blockquote>
<i>Puissance > 50 W lance le timer 2 h ; fin de timer : coupure, notification, veille. Doublon temporaire avec G (non testé).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/G_SDB_SECHE_SERVIETTES_DECOMPTE_2H/G_SDB_SECHE_SERVIETTES_DECOMPTE_2H.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/g_sdb_seche_serviettes_decompte_2h_timer/g_sdb_seche_serviettes_decompte_2h_timer.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📊`numeric_state`, 🔄`state`, ⏱`timer.finished`<br>
<br><details>
<summary>🔌 Entités (4)</summary>
<blockquote><ul>
<li><code>sensor.prise_seche_serviette_salle_de_bain_nous_power</code></li>
<li><code>switch.prise_seche_serviette_salle_de_bain_nous</code></li>
<li><code>timer.seche_serviettes_sdb_2h</code></li>
<li><code>timer.seche_serviettes_sdb_10mn</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>H - SDB - SECHE-SERVIETTES - RATTRAPAGE AU DEMARRAGE DE HA (timer 10 min)</b></summary>
<blockquote>
<i>30 s après le démarrage de HA : lance le 10 mn si la prise est en marche sans timer actif (non testé).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/H_SDB_SECHE_SERVIETTES_RATTRAPAGE_DEMARRAGE_HA/H_SDB_SECHE_SERVIETTES_RATTRAPAGE_DEMARRAGE_HA.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/h_sdb_seche_serviettes_rattrapage_demarrage_ha_timer/h_sdb_seche_serviettes_rattrapage_demarrage_ha_timer.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>switch.prise_seche_serviette_salle_de_bain_nous</code></li>
<li><code>timer.seche_serviettes_sdb_2h</code></li>
<li><code>timer.seche_serviettes_sdb_10mn</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>A - 2026/09/28 - SDB SOUFFLANT : BOUTON IKEA RODRET (MQTT)</b></summary>
<blockquote>
<i>Le bouton IKEA Rodret SDB pilote l'interrupteur virtuel. Topic : zigbee2mqtt2/Inter Soufflant Salle de Bain (IKEA RODRET)/action</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/A_SOUFFLANT_SDB_BOUTON_RODRET/A_SOUFFLANT_SDB_BOUTON_RODRET.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P1_03_Chauffage%20Salle%20de%20Bain/a_soufflant_sdb_bouton_rodret/a_soufflant_sdb_bouton_rodret.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt`<br>
<br><details>
<summary>🔌 Entités (2)</summary>
<blockquote><ul>
<li><code>switch.inter_soufflant_salle_de_bain</code></li>
<li><code>input_boolean.inter_soufflant_salle_de_bain</code></li>
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
<summary><b>🔌 P2 - Prises</b> &nbsp;|&nbsp; 3 automation(s) &nbsp;|&nbsp; <i>Gestion PC bureau, TV chambre, éco prises dynamique</i></summary>
<blockquote>

<details>
<summary>✅ <b>Eco. PRISES DINAMIQUE -> By-Présence/Groupe</b></summary>
<blockquote>
<i>Pilotage des 7 prises en fonction du groupe de présence (G1 à G4).</i><br>
<i>Correctif + spy 2026-09-23 : liste lue via | from_json ; sensor.eco_prises_spy (groupe + états + écarts).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P2_éCO.%20Prises/ECO_PRISES_DYNAMIQUE/ECO_PRISES_DYNAMIQUE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P2_éCO.%20Prises/eco_prises_dynamique_by_presence_groupe/eco_prises_dynamique_by_presence_groupe.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (8) <i>- corrigé 2026-07-19, liste réelle depuis P2_eco_prises_config.yaml</i></summary>
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
<code>switch.prise_tv_salon_ikea</code> (mauvais domaine/nom - c'est <code>light.hue_smart_eco_tv_salon</code>).
Ajouté : <code>light.hue_smart_eco_tv_chambre</code> (absent de la liste précédente).
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Gestion PC bureau : Scène de Fin + Notif</b></summary>
<blockquote>
<i>Veille confirmée (< 70W, 12 min + filet 15 min) : coupe l'éclairage éco PC et notifie. Prise ON pour le suivi conso.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P2_éCO.%20Prises/GESTION_PC_BUREAU/GESTION_PC_BUREAU.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P2_éCO.%20Prises/gestion_pc_bureau_scene_de_fin_notif/gestion_pc_bureau_scene_de_fin_notif.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt` · 🔄`state` · ⏰`time_pattern`<br>
<br><details>
<summary>🔌 Entités (4)</summary>
<blockquote><ul>
<li><code>sensor.prise_bureau_pc_ikea_power</code></li>
<li><code>binary_sensor.veille_pc_bureau</code></li>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>sensor.eco_prises_spy_pc_tv</code> <i>(spy contrôle)</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Gestion TV Chambre : Scène de Fin + Notif</b></summary>
<blockquote>
<i>Veille confirmée (< 40W, 12 min + filet 15 min) : coupe l'éclairage éco TV et notifie. Prise de mesure ON pour le suivi conso.</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P2_éCO.%20Prises/GESTION_TV_CHAMBRE/GESTION_TV_CHAMBRE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P2_éCO.%20Prises/gestion_tv_chambre_scene_de_fin_notif/gestion_tv_chambre_scene_de_fin_notif.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 📡`mqtt` · 🔄`state` · ⏰`time_pattern`<br>
<br><details>
<summary>🔌 Entités (5)</summary>
<blockquote><ul>
<li><code>sensor.prise_tv_chambre_nous_power</code></li>
<li><code>binary_sensor.veille_tv_chambre</code></li>
<li><code>light.hue_smart_eco_tv_chambre</code></li>
<li><code>switch.prise_tv_chambre_nous</code></li>
<li><code>sensor.eco_prises_spy_pc_tv</code> <i>(spy contrôle)</i></li>
</ul></blockquote>
</details>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>💡 P3 - Éclairage</b> &nbsp;|&nbsp; 7 automation(s) &nbsp;|&nbsp; <i>Boutons IKEA salon, bureau (Rodret/Somrig), watchdogs lampes</i></summary>
<blockquote>

<details>
<summary>✅ <b>P3_Allumage Lumière Entrée</b></summary>
<blockquote>
<i>Gestion de l''éclairage de l''entrée basée sur les transitions des</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/ALLUMAGE_LUMIERE_ENTREE/ALLUMAGE_LUMIERE_ENTREE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_entree_allumage_lumiere/p3_entree_allumage_lumiere.yaml">YAML source</a><br>
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
<summary>✅ <b>[P3-SALON] BOUTON IKEA INTER SALON (4) - ON/OFF LIGHT.SALON</b></summary>
<blockquote>
<i>Pilotage de light.salon via le bouton IKEA 4 touches Salon. Topic</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Bouton%20Virtuel/BOUTON_INTER_IKEA_4/BOUTON_INTER_IKEA_4.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Bouton%20Virtuel/p3_salon_bouton_ikea_inter_salon/p3_salon_bouton_ikea_inter_salon.yaml">YAML source</a><br>
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
<summary>✅ <b>[P3-SALON] BOUTON IKEA SOMRIG - TOUT MESSAGE = ON/OFF</b></summary>
<blockquote>
<i>Pilotage simplifié : n''importe quel appui sur le bouton 1 (simple,</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Bouton%20Virtuel/BOUTON_INTER_SOMRIG/BOUTON_INTER_SOMRIG.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Bouton%20Virtuel/p3_salon_bouton_ikea_somrig/p3_salon_bouton_ikea_somrig.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_RODRET_TOGGLE_BLANCHES/BUREAU_RODRET_TOGGLE_BLANCHES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_bouton_rodret_toggle_blanches/p3_bureau_bouton_rodret_toggle_blanches.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_WATCHDOG_SYNCHRO_LAMPES/BUREAU_WATCHDOG_SYNCHRO_LAMPES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_watchdog_synchronisation_lampes_blanches/p3_bureau_watchdog_synchronisation_lampes_blanches.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_FORCER_PLAY_ON/BUREAU_FORCER_PLAY_ON.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_forcer_play_on_si_pc_tourne/p3_bureau_forcer_play_on_si_pc_tourne.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/P3_ECLAIRAGE/BUREAU_ACTIVATION_ECRAN_SYNCHRO/BUREAU_ACTIVATION_ECRAN_SYNCHRO.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P3_eclairage/p3_bureau_activation_ecran_synchro/p3_bureau_activation_ecran_synchro.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Gestion%20des%20Stores/GESTION_STORE_SALON/GESTION_STORE_SALON.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Gestion%20des%20Stores/gestion_simple_du_store_salon_matin_soir/gestion_simple_du_store_salon_matin_soir.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/Gestion%20des%20Stores/GESTION_STORE_BUREAU/GESTION_STORE_BUREAU.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Gestion%20des%20Stores/gestion_optimisee_du_store_bureau/gestion_optimisee_du_store_bureau.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · 🔄`state` · ☀️`sun`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code> - <i>Natif HA (SONOFF/Z2M, corrigé 2026-07-19 - pas produit par M_04, qui ne produit que les *_trend)</i></li>
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
<summary>✅ <b>AUTO. ENERGIE. Basculement Tarif HC/HP - Genelec Appart</b></summary>
<blockquote>
<i>Bascule le tarif des 4 UM Genelec Appart HP/HC aux heures de transition</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Tarif%20HC-HP/BASCULEMENT_TARIF_HPHC/BASCULEMENT_TARIF_HPHC.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Tarif%20HC-HP/auto_energie_basculement_tarif_hc_hp_genelec_appart/auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Log Écart Linky vs Nodon</b></summary>
<blockquote>
<i>Enregistre l'écart à 23:59 pile</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P0_ENRIGE/LOG_ECART_LINKY_NODON/LOG_ECART_LINKY_NODON.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P0_ENRIGE/log_ecart_linky_vs_nodon/log_ecart_linky_vs_nodon.yaml">YAML source</a><br>
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
📄 <a href="docs/03_docs_automations/docs_automations_MD/MariaDB%20%26%20VSCode%20Optimisation/DB_PURGE_MARIADB/DB_PURGE_MARIADB.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/MariaDB%20%26%20VSCode%20Optimisation/db_purge_mariadb_repack/db_purge_mariadb_repack.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Économie Énergie VS Code</b></summary>
<blockquote>
<i>Coupe VS Code si son CPU dépasse 10% ou s'il est inactif, avec confirmation</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/MariaDB%20%26%20VSCode%20Optimisation/ECONOMIE_ENERGIE_VSCODE/ECONOMIE_ENERGIE_VSCODE.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/MariaDB%20%26%20VSCode%20Optimisation/systeme_economie_energie_vs_code/systeme_economie_energie_vs_code.yaml">YAML source</a><br>
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
<summary>✅ <b>VEILLE GITHUB - Nouvelle release détectée</b></summary>
<blockquote>
<i>Surveille les flux Feedreader GitHub (HA core + HACS + cartes HACS).</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/_SANS_CATEGORIE/VEILLE_GITHUB_RELEASES/VEILLE_GITHUB_RELEASES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/_SANS_CATEGORIE/veille_github_nouvelle_release_detectee/veille_github_nouvelle_release_detectee.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⚡`event`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Watchdog Piles (HUE/IKEA/SONOFF)</b></summary>
<blockquote>
<i>Vérification 3x/jour basée sur les groupes de la vue synthétique (seuil</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Watchdog%20Piles%20(HUE-IKEA-SONOFF)/WATCHDOG_PILES/WATCHDOG_PILES.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Watchdog%20Piles%20(HUE-IKEA-SONOFF)/systeme_watchdog_piles_hue_ikea_sonoff/systeme_watchdog_piles_hue_ikea_sonoff.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Z2M last_seen</b></summary>
<blockquote>
<i>Surveillance des capteurs Zigbee injoignables (plus de 8h ou indisponibles)</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/Contrôle%20Entity%20z2m/Z2M_LAST_SEEN/Z2M_LAST_SEEN.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/Contrôle%20Entity%20z2m/z2m_last_seen/z2m_last_seen.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)</b></summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P0_ENRIGE/DIAG_ENREGISTREMENT_JOURNALIER/DIAG_ENREGISTREMENT_JOURNALIER.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/P0_ENRIGE/diag_enregistrement_journalier/diag_enregistrement_journalier.yaml">YAML source</a><br>

</blockquote>
</details>

</blockquote>
</details>

---

<details>
<summary><b>🍓 Raspberry Pi4 (archivé)</b> &nbsp;|&nbsp; 1 automation(s) &nbsp;|&nbsp; <i>Gestion ventilateur CPU - archivé depuis migration NUC</i></summary>
<blockquote>

<details>
<summary>✅ <b>Raspberry CPU Fan PWM 6 States</b></summary>
<blockquote>
<i>Règle la vitesse du ventilateur du Raspberry en fonction de la température</i><br><br>
📄 <a href="docs/03_docs_automations/docs_automations_MD/RASPI/RPi4_FAN_PWM/RPi4_FAN_PWM.md">Documentation</a><br>
⚙️ <a href="docs/03_docs_automations/docs_automations_YAML/RASPI/A_rpi_fan_pwm_6_states/A_rpi_fan_pwm_6_states.yaml">YAML source</a><br>
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

## 🔧 04 - SCRIPTS

*Scripts bash maintenance système + scripts HA YAML (clim)*

---

<details>
<summary><b>🐚 SCRIPTS BASH</b> &nbsp;|&nbsp; 5 scripts (3 actifs ; 2 ajoutés le 2026-10-12, activité non vérifiée) &nbsp;|&nbsp; Prod : <code>/homeassistant/.scripts/</code> &nbsp;|&nbsp; Local : <code>docs_scripts_SH/</code></summary>
<blockquote>

<details>
<summary><code>audit_md5.sh</code> &nbsp;|&nbsp; Audit MD5 GitHub ↔ prod (YAML config HA)</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_SH_MD/AUDIT_MD5/AUDIT_MD5.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/audit_md5/audit_md5.sh">Script source</a><br>
Sortie : <code>/homeassistant/.logs/audit_md5.log</code>
</blockquote>
</details>

<details>
<summary><code>ha_git_backup.sh</code> &nbsp;|&nbsp; Backup git automatique HA → GitHub</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_SH_MD/HA_GIT_BACKUP/HA_GIT_BACKUP.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/ha_git_backup/ha_git_backup.sh">Script source</a><br>
Sortie : repo GitHub <code>home_assistant_re-build</code>
</blockquote>
</details>

<details>
<summary><code>audit_md5_yaml.sh</code> &nbsp;|&nbsp; Audit MD5 YAML GitHub ↔ prod (ajouté le 2026-10-12, activité non vérifiée)</summary>
<blockquote>
Script source : <a href="docs/04_docs_scripts/docs_scripts_SH/audit_md5_yaml/audit_md5_yaml.sh">audit_md5_yaml.sh</a> (copie de <code>/homeassistant/.scripts/</code>)<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>mf_vigilance_images.sh</code> &nbsp;|&nbsp; Cartes de vigilance Météo-France J0/J1 (ajouté le 2026-10-12, activité non vérifiée)</summary>
<blockquote>
Script source : <a href="docs/04_docs_scripts/docs_scripts_SH/mf_vigilance_images/mf_vigilance_images.sh">mf_vigilance_images.sh</a> (copie de <code>/homeassistant/scripts/</code>)<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>#MP_01_monitor_temp.sh.#</code> &nbsp;|&nbsp; Actif - Raspberry Pi</summary>
<blockquote>
Script de monitoring température (Raspberry Pi) - publie <code>sensor.proxmox_cpu_package</code>,
<code>_carte_mere</code>, <code>_core_0-3</code> (utilisés en L4C1/L4C2) via MQTT Discovery.<br>
Pas de doc associée.<br><br>
✅ <b>Confirmé par Eric (2026-07-19)</b> : "ça remonte la T° du CPU et d'autres choses" -
device et fonction confirmés (Raspberry Pi, cf. TODO.md U-2). Corrige l'ancienne mention
"désactivé/archivé" de cette entrée, qui contredisait TODO.md ("actif - NE PAS TOUCHER").
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><b>🐍 SCRIPTS PYTHON D'INDEX</b> &nbsp;|&nbsp; 6 scripts (ajoutés le 2026-10-13, lecture seule de la prod) &nbsp;|&nbsp; Local : <code>docs_scripts_SH/</code> &nbsp;|&nbsp; Non poussés en prod</summary>
<blockquote>

<details>
<summary><code>gen_global_index_automations.py</code> &nbsp;|&nbsp; Génère GLOBAL_INDEX_AUTOMATIONS.md (automations de H:\automations.yaml + registre HA)</summary>
<blockquote>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_automations/gen_global_index_automations.py">Script source</a><br>
Sortie : <a href="docs/03_docs_automations/GLOBAL_INDEX_AUTOMATIONS.md">GLOBAL_INDEX_AUTOMATIONS.md</a> (régénéré à chaque /histo)<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>gen_global_index_vignettes_pages.py</code> &nbsp;|&nbsp; Génère GLOBAL_INDEX_VIGNETTES_PAGES.md (vignettes et pages, arbre local docs/02_docs_dashboard)</summary>
<blockquote>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_vignettes_pages/gen_global_index_vignettes_pages.py">Script source</a><br>
Sortie : <a href="docs/02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md">GLOBAL_INDEX_VIGNETTES_PAGES.md</a> (régénéré à chaque /histo)<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>gen_global_index_scripts.py</code> &nbsp;|&nbsp; Génère GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md</summary>
<blockquote>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py">Script source</a><br>
Sorties : <a href="docs/04_docs_scripts/GLOBAL_INDEX_SCRIPTS_SH.md">GLOBAL_INDEX_SCRIPTS_SH.md</a> · <a href="docs/04_docs_scripts/GLOBAL_INDEX_SCRIPTS_YAML.md">GLOBAL_INDEX_SCRIPTS_YAML.md</a> (régénérés à chaque /histo)<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>gen_global_index_ia.py</code> &nbsp;|&nbsp; Génère GLOBAL_INDEX_IA.md (fichiers de docs/00_IA)</summary>
<blockquote>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/gen_global_index_ia/gen_global_index_ia.py">Script source</a><br>
Sortie : <a href="docs/00_IA/GLOBAL_INDEX_IA.md">GLOBAL_INDEX_IA.md</a> (régénéré à chaque /histo)<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>check_sous_context_ia.py</code> &nbsp;|&nbsp; Contrôle en lecture seule des 9 fichiers de docs/00_IA/sous_context_ia</summary>
<blockquote>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/check_sous_context_ia/check_sous_context_ia.py">Script source</a><br>
Lancé par /histo (étape 6, point 7) ; ne corrige rien.<br>
Pas de doc associée.
</blockquote>
</details>

<details>
<summary><code>check_global_index.py</code> &nbsp;|&nbsp; Contrôle en lecture seule des 7 index globaux</summary>
<blockquote>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_SH/check_global_index/check_global_index.py">Script source</a><br>
Lancé par /histo (étape 6, point 8) ; ne corrige rien.<br>
Pas de doc associée.
</blockquote>
</details>

</blockquote>
</details>

<details>
<summary><b>⚙️ SCRIPTS HA YAML</b> &nbsp;|&nbsp; 3 fichiers sources &nbsp;|&nbsp; Géré via UI HA &nbsp;|&nbsp; Local : <code>docs_scripts_YAML/</code></summary>
<blockquote>

<details>
<summary><code>p1_master_gestion_clim.yaml</code> &nbsp;|&nbsp; Script unique - pilotage clim jour/nuit (param <code>periode</code>)</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_YAML_MD/P1_MASTER_GESTION_CLIM/P1_MASTER_GESTION_CLIM.md">Doc master</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/p1_master_gestion_clim/p1_master_gestion_clim.yaml">YAML source</a><br>
Appelé par les automations (A-0) et (B-0) - voir section 03.

<blockquote>
⚠️ <b>Corrigé le 2026-07-19</b> : le fichier réel <code>p1_master_gestion_clim.yaml</code> est un
script unique (pas 4 sous-scripts). Le doc master lui-même
(<code>P1_MASTER_GESTION_CLIM.md</code>) précise "Créé par Refactoring LLM local - 2026-06"
et qu'il "remplace le code inline dupliqué dans A0/B0". Les 2 sous-entrées ci-dessous
(J 1-1/1-2/1-3 et J 2-0) décrivent une architecture pré-refactor (scripts
<code>j_1_1_salon_clim_on_off_intelligent</code> etc.) dont le yaml n'existe plus dans
<code>docs_scripts_YAML/</code> - conservées ici à titre historique uniquement.
Mise à jour 2026-10-12 : ces 4 scripts existent toujours dans la prod (scripts.yaml, aucune automation ne les appelle) et leurs YAML ont été extraits en local le 2026-10-12. Leur statut obsolète n'est pas confirmé (usage éventuel dans le dashboard non vérifié).
</blockquote>

<details>
<summary>🗄️ ARCHIVÉ (pré-refactor 2026-06) - J 1-1 / J 1-2 / J 1-3 &nbsp;|&nbsp; Routeurs CLIM ON/OFF INTELLIGENT (Salon / Bureau / Chambre)</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_YAML_MD/SCRIPTS_CLIM_ON_OFF/SCRIPTS_CLIM_ON_OFF.md">Doc</a><br>
Scripts (obsolètes, non présents dans docs_scripts_YAML/) : <code>j_1_1_salon_clim_on_off_intelligent</code> · <code>j_1_2_bureau_clim_on_off_intelligent</code> · <code>j_1_3_chambre_clim_on_off_intelligent</code>
YAML sources (extraits de la prod le 2026-10-12) : <a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/j_1_1_salon_clim_on_off_intelligent/j_1_1_salon_clim_on_off_intelligent.yaml">j_1_1</a> · <a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/j_1_2_bureau_clim_on_off_intelligent/j_1_2_bureau_clim_on_off_intelligent.yaml">j_1_2</a> · <a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/j_1_3_chambre_clim_on_off_intelligent/j_1_3_chambre_clim_on_off_intelligent.yaml">j_1_3</a>. Les 3 scripts existent toujours dans la prod ; aucune automation ne les appelle.<br>
</blockquote>
</details>

<details>
<summary>🗄️ ARCHIVÉ (pré-refactor 2026-06) - J 2-0 &nbsp;|&nbsp; SECU - ARRÊT CLIM PROTÉGÉ</summary>
<blockquote>
📄 <a href="docs/04_docs_scripts/docs_scripts_YAML_MD/SCRIPT_J2_0_SECU_ARRET_CLIM/SCRIPT_J2_0_SECU_ARRET_CLIM.md">Doc</a><br>
Script (obsolète, non présent dans docs_scripts_YAML/) : <code>j_2_0_secu_arret_clim_protege</code>
YAML source (extrait de la prod le 2026-10-12) : <a href="docs/04_docs_scripts/docs_scripts_YAML/Climatisation/j_2_0_secu_arret_clim_protege/j_2_0_secu_arret_clim_protege.yaml">j_2_0_secu_arret_clim_protege.yaml</a>. Le script existe toujours dans la prod ; aucune automation ne l'appelle.<br>

<details>
<summary><code>sdb_soufflant_demarrer.yaml</code> &nbsp;|&nbsp; Soufflant SDB : demarrage 2000 W + verrou 30 s</summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/SDB_SOUFFLANT_SPECIFICATION_2026/SDB_SOUFFLANT_SPECIFICATION_2026.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_YAML/Soufflant%20SDB/sdb_soufflant_demarrer/sdb_soufflant_demarrer.yaml">YAML source</a><br>
Appelé par l'automation H (section 03). Refuse de démarrer en mode cool (sensor.mode_ete_hiver, depuis le 2026-10-07 ; remplace la garde 25 degrés) (première ligne, avant le verrou). Pose le verrou, alimente la prise, 2 impulsions 1000 W,
passe le climate en heat, et éteint l'interrupteur si l'appareil tourne encore après 60 minutes.
</blockquote>
</details>

<details>
<summary><code>sdb_soufflant_arreter.yaml</code> &nbsp;|&nbsp; Soufflant SDB : resistances, ventilateur 1 min 30, prise</summary>
<blockquote>
📄 <a href="docs/03_docs_automations/docs_automations_MD/P1_03_Chauffage%20Salle%20de%20Bain/SDB_SOUFFLANT_SPECIFICATION_2026/SDB_SOUFFLANT_SPECIFICATION_2026.md">Doc</a><br>
⚙️ <a href="docs/04_docs_scripts/docs_scripts_YAML/Soufflant%20SDB/sdb_soufflant_arreter/sdb_soufflant_arreter.yaml">YAML source</a><br>
Appelé par l'automation H (section 03). Refusé pendant le verrou de démarrage. Remet le climate
sur off à la fin, après la coupure de la prise.
</blockquote>
</details>

<details>
<summary><code>audit_md5.yaml</code> &nbsp;|&nbsp; Script HA : lance <code>shell_command.audit_md5</code> (audit MD5 GitHub)</summary>
<blockquote>
<a href="docs/04_docs_scripts/docs_scripts_YAML/audit_md5/audit_md5.yaml">YAML source</a> (extrait de la prod le 2026-10-12)<br>
Pas de doc associée. Aucune automation de la prod ne l'appelle (vérifié le 2026-10-12).
</blockquote>
</details>

<details>
<summary><code>audit_md5_md_yaml.yaml</code> &nbsp;|&nbsp; Script HA : lance <code>shell_command.audit_md5_md_yaml</code> (audit MD5 docs)</summary>
<blockquote>
<a href="docs/04_docs_scripts/docs_scripts_YAML/audit_md5_md_yaml/audit_md5_md_yaml.yaml">YAML source</a> (extrait de la prod le 2026-10-12)<br>
Pas de doc associée. Aucune automation de la prod ne l'appelle (vérifié le 2026-10-12).
</blockquote>
</details>

</blockquote>
</details>
</blockquote>
</details>

</blockquote>
</details>

---

## 📋 05 - SYSTÈME MD

*Documents transversaux : index entités, MOC, templates, workflow ReBuild*

---

<details>
<summary><b>ENTITES_GLOBAL_INDEX.md</b> &nbsp;|&nbsp; Index global des entités HA (unique_id → fichier source)</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/ENTITES_GLOBAL_INDEX/ENTITES_GLOBAL_INDEX.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>MOC_DEPENDANCES.md</b> &nbsp;|&nbsp; Map of Content - dépendances inter-fichiers YAML <i>(dossier MOC/ local, hors docs/ - non poussé)</i></summary>
<blockquote>
📄 <a href="MOC/MOC_DEPENDANCES/MOC_DEPENDANCES.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>MOC_DASHBOARD.md</b> &nbsp;|&nbsp; Map of Content - vignettes & pages dashboard (Obsidian) <i>(dossier MOC/ local, hors docs/ - non poussé)</i></summary>
<blockquote>
📄 <a href="MOC/MOC_DASHBOARD/MOC_DASHBOARD.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>MOC_PRESENCE.md</b> &nbsp;|&nbsp; Map of Content - pôle 4 présence (groupe_1 à groupe_4, statuts réseau) <i>(dossier MOC/ local, hors docs/ - non poussé)</i></summary>
<blockquote>
<a href="MOC/MOC_PRESENCE/MOC_PRESENCE.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>_TEMPLATE_DOC.md</b> &nbsp;|&nbsp; Template officiel pour créer une doc vignette/automation/script</summary>
<blockquote>
📄 <a href="docs/05_docs_MD_system/matrisse_template_doc/_TEMPLATE_DOC.md">Doc</a>
</blockquote>
</details>


---

## 05 - SKILLS

*Copies des SKILL.md du projet (source : .claude/skills/), poussées vers H:\docs\05_docs_skills. Les 14 skills du projet ont leur copie dans docs/05_docs_skills/skill_<nom>/ (histo et histo-final compris).*

---

<details>
<summary><b>fix-file.md</b> &nbsp;|&nbsp; analyse une erreur Home Assistant et retourne le bloc YAML corrigé</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_fix-file/fix-file.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-new-yaml.md</b> &nbsp;|&nbsp; génère un squelette YAML conforme aux conventions du projet</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-new-yaml/ha-new-yaml.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-push-docs.md</b> &nbsp;|&nbsp; synchronise les docs locales (*.md + yaml dashboard) vers H:\Docs</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-push-docs/ha-push-docs.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-push-md.md</b> &nbsp;|&nbsp; pousse uniquement les *.md de documentation vers H:\Docs</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-push-md/ha-push-md.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-push-yaml.md</b> &nbsp;|&nbsp; pousse un YAML config vers la prod, sauvegarde locale avant modification</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-push-yaml/ha-push-yaml.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-resync-docs.md</b> &nbsp;|&nbsp; compare et resynchronise les YAML locaux depuis GitHub</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-resync-docs/ha-resync-docs.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-resync-tree.md</b> &nbsp;|&nbsp; resynchronise les YAML locaux depuis le repo GitHub (source de vérité n°2)</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-resync-tree/ha-resync-tree.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-status.md</b> &nbsp;|&nbsp; résumé ultra-compact de l'avancement du projet en 3 points</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-status/ha-status.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>ha-trigul.md</b> &nbsp;|&nbsp; triangulation MD5 des docs local / prod / GitHub, rapports dans historique/MD5</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_ha-trigul/ha-trigul.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>histo.md</b> &nbsp;|&nbsp; journal de bord, sync_index, journal fusionné, Obsidian, ménage des .bak, tree</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_histo/histo.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>histo-final.md</b> &nbsp;|&nbsp; histo complet, puis extinction de l'écran (switch.ecran_p_c_3_play_hue) et arrêt du PC après 5 minutes</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_histo-final/histo-final.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>journal-modifs.md</b> &nbsp;|&nbsp; note au fil de l'eau chaque modification de fichier dans un journal par auteur (claude, eric, hermes)</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_journal-modifs/journal-modifs.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>sync-index.md</b> &nbsp;|&nbsp; met à jour DEPENDANCES_GLOBALES.md et l'index après validation d'un YAML</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_sync-index/sync-index.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>update-arbo.md</b> &nbsp;|&nbsp; met à jour IA_ARBO_DETAIL.md (comptages local, prod, GitHub)</summary>
<blockquote>
<a href="docs/05_docs_skills/skill_update-arbo/update-arbo.md">Doc</a>
</blockquote>
</details>
