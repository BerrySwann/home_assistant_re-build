# ⚙️ INDEX AUTOMATIONS — Home Assistant ReBuild

*Navigation complète des 48 automations — par catégorie, avec docs, YAML, triggers et entités*<br>
*Chemins relatifs depuis `docs_automations/`*

**11 catégories · 48 automations · 49 entrées dans l'index**

<details>
<summary>📋 <b>Table des matières</b></summary>
<blockquote>
<b>🔧 Backup Git</b> (7 automations)<br>
<b>🌤️ Météo</b> (5 automations)<br>
<b>🌡️ P1 — Clim & Chauffage</b> (11 automations)<br>
<b>🍳 P1 — Cuisine</b> (2 automations)<br>
<b>🚿 P1 — Salle de Bain</b> (3 automations)<br>
<b>🔌 P2 — Prises</b> (3 automations)<br>
<b>💡 P3 — Éclairage</b> (8 automations)<br>
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
📄 <a href="docs_automations/docs/BACKUP/GIT_ALERTE_KO.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/backup/git_alerte_ko.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/BACKUP/GIT_HOURLY.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/backup/git_hourly.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>⚠️ <b>[02-Backup] Git daily (03:00)</b></summary>
<blockquote>
<i>Backup natif HA + push Git quotidien à 03h00</i><br><br>
📄 <a href="docs_automations/docs/BACKUP/GIT_DAILY.md">Documentation</a><br>
⚙️ <i>Pas de fichier TREE_CORRIGE</i><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[03-Backup] Git weekly (dim 01:30)</b></summary>
<blockquote>
<i>Backup natif HA + push + tag weekly chaque dimanche à 01:30</i><br><br>
📄 <a href="docs_automations/docs/BACKUP/GIT_WEEKLY.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/backup/git_weekly.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[04-Backup] Git push manuel</b></summary>
<blockquote>
📄 <a href="docs_automations/docs/BACKUP/GIT_PUSH_MANUEL.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/backup/git_push_manuel.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/BACKUP/GIT_PUSH_WEEKLY_MANUEL.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/backup/git_push_weekly_manuel.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/BACKUP/GIT_AU_DEMARRAGE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/backup/git_au_demarrage.yaml">YAML source</a><br>

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
📄 <a href="docs_automations/docs/METEO/ALERTE_METEO_CARTES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/meteo/alerte_meteo_cartes.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/METEO/UPDATE_PREV_TEMPERATURE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/meteo/update_prev_temperature.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/METEO/UPDATE_PREV_HUMIDITY.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/meteo/update_prev_humidity.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/METEO/NOTIF_FOUDRE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/meteo/notif_foudre.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/METEO/MAJ_TEMPS_FOUDRE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/meteo/maj_temps_foudre.yaml">YAML source</a><br>
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
<summary><b>🌡️ P1 — Clim & Chauffage</b> &nbsp;|&nbsp; 11 automation(s) &nbsp;|&nbsp; <i>Logique de climatisation, notifications, gardien éco</i></summary>
<blockquote>

<details>
<summary>✅ <b>(A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00)</b></summary>
<blockquote>
<i>Pilotage clims jour avec boucle de relance et notification ciblée fenêtres</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/A0_CLIM_JOUR.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/A0_clim_jour_2026-01-11.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · 🔄`state`<br>
<br><details>
<summary>🔌 Entités (8)</summary>
<blockquote><ul>
<li><code>switch.clim_salon_nous</code></li>
<li><code>input_boolean.clim_salon_arret_securise_en_cours</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
<li><code>switch.clim_bureau_nous</code></li>
<li><code>input_boolean.clim_bureau_arret_securise_en_cours</code></li>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>switch.clim_chambre_nous</code></li>
<li><code>input_boolean.clim_chambre_arret_securise_en_cours</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30)</b></summary>
<blockquote>
<i>Pilotage clims nuit avec boucle de relance et notification ciblée fenêtres</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/B0_CLIM_NUIT.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/B0_clim_nuit_2026-01-11.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🏠`homeassistant` · ⏰`time` · 🔄`state`<br>
<br><details>
<summary>🔌 Entités (8)</summary>
<blockquote><ul>
<li><code>switch.clim_salon_nous</code></li>
<li><code>input_boolean.clim_salon_arret_securise_en_cours</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
<li><code>switch.clim_bureau_nous</code></li>
<li><code>input_boolean.clim_bureau_arret_securise_en_cours</code></li>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>switch.clim_chambre_nous</code></li>
<li><code>input_boolean.clim_chambre_arret_securise_en_cours</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(C) (CLIM OFF) Gardien Éco (Delta T < -1 et T°Ext > Seuil Non-Chauffage)</b></summary>
<blockquote>
<i>Module de sécurité ÉCO. Coupe les climatiseurs si l''air extérieur</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/C_GARDIEN_ECO.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/C_gardien_eco.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (5)</summary>
<blockquote><ul>
<li><code>sensor.temperature_delta_valeur</code></li>
<li><code>sensor.th_balcon_nord_temperature</code></li>
<li><code>climate.clim_salon_rm4_mini</code></li>
<li><code>climate.clim_bureau_rm4_mini</code></li>
<li><code>climate.clim_chambre_rm4_mini</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(D) Notification température Up ou Down de (7h30 -> 21h00)</b></summary>
<blockquote>
<i>Envoie le message personnalisé de clim si le texte change, OU au réveil</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/D_NOTIF_TEMP_JOUR.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/D_notif_temp_jour.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(E) Notification température Up ou Down de (21h00 -> 7h30)</b></summary>
<blockquote>
<i>Envoie le message personnalisé de clim si le texte change, OU au début</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/E_NOTIF_TEMP_NUIT.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/E_notif_temp_nuit.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · ⏰`time`<br>
<br><details>
<summary>🔌 Entités (1)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>(F) (CLIM) Notification de fermeture des fenêtres</b></summary>
<blockquote>
<i>Envoie une notification lorsqu'une fenêtre est fermée.</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/F_NOTIF_FERMETURE_FENETRES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/F_notif_fermeture_fenetres.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(G) (CLIM) Automatisation Arrêt Clim Notification</b></summary>
<blockquote>
<i>Notification quand une clim est coupée manuellement, seulement si</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/G_ARRET_CLIM_NOTIF.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/G_arret_clim_notif.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/H_NOTIF_MODE_CHANGEMENT.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/H_notif_mode_changement.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/I_DEBUG_FORCE_MODE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/I_debug_force_mode.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/J_SYNCHRO_NOTIF_PRISE_COUPEE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/J_synchro_notif_prise_coupee.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(K) (DEBUG) Notifier les changements de message clim (Mobile)</b></summary>
<blockquote>
<i>Surveille et notifie les changements d'état du message personnalisé.</i><br><br>
📄 <a href="docs_automations/docs/P1_CLIM_CHAUFFAGE/L_DEBUG_NOTIF_MESSAGE_CLIM.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_clim_chauffage/L_debug_notif_message_clim.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_CUISINE/A_CHAUFFAGE_CUISINE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_cuisine/A_chauffage_cuisine.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_CUISINE/B_CHAUFFAGE_CUISINE_VACANCES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_cuisine/B_chauffage_cuisine_vacances.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_SDB/A_SOUFFLANT_SDB.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_sdb/A_soufflant_sdb_gestion_intelligente.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_SDB/D_WATCHDOG_RADIATEUR_SDB.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_sdb/D_sdb_watchdog_radiateur.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P1_SDB/E_MINUTERIE_SECHE_SERVIETTES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P1_sdb/E_minuterie_seche_serviettes.yaml">YAML source</a><br>
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
<i>Pilotage des 6 prises en fonction du groupe de présence (G1 à G4).</i><br><br>
📄 <a href="docs_automations/docs/P2_PRISES/ECO_PRISES_DYNAMIQUE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P2_prises/P2_eco_prises_dynamique.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state` · 📊`numeric_state`<br>
<br><details>
<summary>🔌 Entités (8)</summary>
<blockquote><ul>
<li><code>sensor.groupe</code></li>
<li><code>sensor.prise_bureau_pc_ikea_power</code></li>
<li><code>switch.prise_tv_salon_ikea</code></li>
<li><code>light.hue_smart_eco_salon</code></li>
<li><code>switch.prise_horloge_ikea</code></li>
<li><code>switch.ecran_p_c_3_play_hue</code></li>
<li><code>light.hue_smart_eco_pc_bureau</code></li>
<li><code>switch.prise_tete_de_lit_chambre</code></li>
</ul></blockquote>
</details>

</blockquote>
</details>

<details>
<summary>✅ <b>Gestion PC bureau : Scène de Fin + Notif</b></summary>
<blockquote>
<i>Éteint la prise du PC et notifie, mais laisse la prise ON pour le</i><br><br>
📄 <a href="docs_automations/docs/P2_PRISES/GESTION_PC_BUREAU.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P2_prises/gestion_pc_bureau.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P2_PRISES/GESTION_TV_CHAMBRE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P2_prises/gestion_tv_chambre.yaml">YAML source</a><br>
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
<summary><b>💡 P3 — Éclairage</b> &nbsp;|&nbsp; 8 automation(s) &nbsp;|&nbsp; <i>Boutons IKEA salon, bureau (Rodret/Somrig), watchdogs lampes</i></summary>
<blockquote>

<details>
<summary>✅ <b>P3_Allumage Lumière Entrée</b></summary>
<blockquote>
<i>Gestion de l''éclairage de l''entrée basée sur les transitions des</i><br><br>
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/ALLUMAGE_LUMIERE_ENTREE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_eclairage/allumage_lumiere_entree.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BOUTON_INTER_IKEA_4.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_salon_bouton_inter_ikea_4.yaml">YAML source</a><br>
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
<summary>✅ <b>[P3-Salon] Bouton IKEA Inter Salon (4) — ON/OFF light.salon</b></summary>
<blockquote>
<i>Pilotage de light.salon via le bouton IKEA 4 touches Salon. Topic</i><br><br>
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BOUTON_INTER_IKEA_4.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_salon_bouton_inter_ikea_4.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BOUTON_INTER_SOMRIG.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_salon_bouton_inter_somrig.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BUREAU_RODRET_TOGGLE_BLANCHES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_eclairage/P3_bureau_bouton_rodret_toggle_blanches.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BUREAU_WATCHDOG_SYNCHRO_LAMPES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_eclairage/bureau_watchdog_synchro_lampes.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BUREAU_FORCER_PLAY_ON.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_eclairage/bureau_forcer_play_on_si_pc.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/P3_ECLAIRAGE/BUREAU_ACTIVATION_ECRAN_SYNCHRO.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/P3_eclairage/bureau_activation_ecran_synchro.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/STORES/GESTION_STORE_SALON.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/stores/gestion_store_salon.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/STORES/GESTION_STORE_BUREAU.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/stores/gestion_store_bureau.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · 🔄`state` · ☀️`sun`<br>
<br><details>
<summary>🔌 Entités (3)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
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
📄 <a href="docs_automations/docs/ENERGIE/BASCULEMENT_TARIF_HPHC.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/energie/basculement_tarif_hphc.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Log Écart Linky vs Nodon</b></summary>
<blockquote>
<i>Enregistre l'écart à 23:59 pile</i><br><br>
📄 <a href="docs_automations/docs/ENERGIE/LOG_ECART_LINKY_NODON.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/energie/log_ecart_linky_nodon.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/SYSTEME/DB_PURGE_MARIADB.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/systeme/db_purge_mariadb.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Économie Énergie VS Code</b></summary>
<blockquote>
<i>Coupe VS Code si son CPU dépasse 10% ou s'il est inactif, avec confirmation</i><br><br>
📄 <a href="docs_automations/docs/SYSTEME/ECONOMIE_ENERGIE_VSCODE.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/systeme/economie_energie_vscode.yaml">YAML source</a><br>
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
📄 <a href="docs_automations/docs/SYSTEME/VEILLE_GITHUB_RELEASES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/systeme/veille_github_releases.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⚡`event`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Watchdog Piles (HUE/IKEA/SONOFF)</b></summary>
<blockquote>
<i>Vérification 3x/jour basée sur les groupes de la vue synthétique (seuil</i><br><br>
📄 <a href="docs_automations/docs/SYSTEME/WATCHDOG_PILES.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/systeme/watchdog_piles.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Z2M last_seen</b></summary>
<blockquote>
<i>Surveillance des capteurs Zigbee injoignables (plus de 8h ou indisponibles)</i><br><br>
📄 <a href="docs_automations/docs/SYSTEME/Z2M_LAST_SEEN.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/systeme/z2m_last_seen.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)</b></summary>
<blockquote>
📄 <a href="docs_automations/docs/SYSTEME/DIAG_ENREGISTREMENT_JOURNALIER.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/systeme/diag_enregistrement_journalier.yaml">YAML source</a><br>

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
📄 <a href="docs_automations/docs/RASPI/RPi4_FAN_PWM.md">Documentation</a><br>
⚙️ <a href="docs_automations/TREE_CORRIGE/raspi/A_rpi_fan_pwm_6_states.yaml">YAML source</a><br>
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

<details>
<summary>Fichiers TREE_CORRIGE absents de GitHub (à vérifier)</summary>
<blockquote>
<b>`P2_prises/eco_prises.yaml`</b> — Ancienne version de 'Eco. PRISES DINAMIQUE' — **à archiver dans `old/`**<br>
<b>`P2_prises/bureau_allumage_pc.yaml`</b> — Automation supprimée de HA — **à archiver dans `old/`**<br>
<b>`P2_prises/rodret_soufflant_sdb.yaml`</b> — Automation supprimée de HA — **à archiver dans `old/`**<br>
<b>`P2_prises/rodret_tv_chambre.yaml`</b> — Automation supprimée de HA — **à archiver dans `old/`**<br>
<b>`P2_bouton_rodret_soufflant_sdb.yaml`</b> — Fichier mal placé à la racine — doublon probable<br>
<b>`systeme/diag_enregistrement_journalier.yaml`</b> — NON présent dans GitHub — **vérifier si active dans HA live**<br>
</blockquote>
</details>

---

*Dernière mise à jour : 2026-05-30 | 48 automations GitHub | 46 fichiers TREE_CORRIGE*