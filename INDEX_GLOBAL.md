# 🗂️ INDEX GLOBAL — HA ReBuild

*Index unique de navigation — YAML, docs, entités, scripts*
*Dernière mise à jour : 2026-07-16*

---

## 🧠 00 — IA & CONTEXTE

*Fichiers de référence IA — à lire à la demande selon le contexte de la tâche*

---

<details>
<summary><b>IA_CONTEXT_BASE.md</b> &nbsp;|&nbsp; Base de contexte expert HA (résumé principal)</summary>
<blockquote>
📄 <a href="DOCS/00_IA/IA_CONTEXT_BASE.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_ARBO_DETAIL.md</b> &nbsp;|&nbsp; Arborescence complète prod + local, URLs GitHub raw</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_ARBO_DETAIL.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_AUTOMATIONS_NOTIFS.md</b> &nbsp;|&nbsp; Création/modif automations, messages notify, scripts HA</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_AUTOMATIONS_NOTIFS.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_CMD_TERMINAL_HA.md</b> &nbsp;|&nbsp; Commandes tree prod, audit MD5, git backup, chemins /homeassistant/, logs HA</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_CMD_TERMINAL_HA.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INDEX_AUTOMATIONS.md</b> &nbsp;|&nbsp; Régénération INDEX_AUTOMATIONS, mapping alias → DOCS/03, anomalies</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_INDEX_AUTOMATIONS.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INDEX_NAVIGATION.md</b> &nbsp;|&nbsp; Régénération INDEX_GLOBAL, ajout vignette/page, mapping entités → fichiers sources</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_INDEX_NAVIGATION.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_INTEGRATIONS_CARTES.md</b> &nbsp;|&nbsp; YAML dashboard, custom:*, intégrations manquantes, palette couleurs</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_INTEGRATIONS_CARTES.md">Doc</a>
</blockquote>
</details>

<details>
<summary><b>IA_P4_PRESENCE.md</b> &nbsp;|&nbsp; sensor.presence, format notif avec présence, logique groupe Wi-Fi</summary>
<blockquote>
📄 <a href="DOCS/00_IA/sous_md/IA_P4_PRESENCE.md">Doc</a>
</blockquote>
</details>

---

## ⚙️ 01 — CONFIGURATION SYSTÈME

*Fichiers YAML config HA — auto-documentés via headers inline. Seule la doc de configuration générale est ici.*

---

<details>
<summary><b>configuration.md</b> &nbsp;|&nbsp; Structure configuration.yaml, includes, pôles actifs</summary>
<blockquote>
📄 <a href="DOCS/01_docs_config_system/config_system_MD/configuration.md">Doc</a>
</blockquote>
</details>

---

## 📊 02 — DASHBOARD (18 vignettes)

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
<summary>💬 Pop-up <code>#foudre</code> — 11 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.dernier_impact_temps_reel</code></li>
<li><code>sensor.eclairs_annuel</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_hebdomadaire</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_horaire</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_mensuel</code> — <i>Natif HA</i></li>
<li><code>sensor.eclairs_quotidien</code> — <i>Natif HA</i></li>
<li><code>sensor.lightning_bearing</code></li>
<li><code>sensor.lightning_direction_label</code></li>
<li><code>sensor.lightning_distance_km</code></li>
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
<summary>💬 Pop-up <code>#sun</code> — 6 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.duree_du_jour</code></li>
<li><code>sensor.moon_phase</code> — <i>Natif HA</i></li>
<li><code>sensor.season</code> — <i>Natif HA</i></li>
<li><code>sensor.tendance_duree_jour</code></li>
<li><code>sensor.variation_quotidienne</code></li>
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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 10 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C2_TEMPERATURES/PAGE_TEMPERATURES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L1C2_02_Temperatures/page_L1C2_temperatures_2026-05-12.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tendances</code> — 0 entité(s)</summary>
<blockquote><ul>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#exterieur</code> — 2 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_temperature</code></li>
<li><code>weather.vence</code></li>
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
<li><code>sensor.th_balcon_nord_temperature</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#hcourbe</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.th_balcon_nord_humidity</code></li>
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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 1 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L1C3_CLIM/PAGE_CLIM.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L1C3_03_Commandes_Clim/page_L1C3_clim_2026-05-13.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page Principale</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_principale_2026-05-12.yaml">YAML Page</a>


</blockquote>
</details>

<details>
<summary>📄 <b>Page Mensuel</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE_MENSUEL.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_mensuel_2026-05-12.yaml">YAML Page</a>


</blockquote>
</details>

<details>
<summary>📄 <b>Page Temps Réel</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C1_ENERGIE/PAGE_ENERGIE_TEMPS_REEL.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C1_04_Energie_Generale/page_L2C1_energie_temps_reel_2026-05-12.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 1 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C2_ENERGIE_CLIM/PAGE_ENERGIE_CLIM.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C2_05_Energie_Clim/page_L2C2_energie_clim_2026-05-13.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L2C3_ENERGIE_ECLAIRAGE/PAGE_ENERGIE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L2C3_06_Energie_Eclairage/page_L2C3_energie_eclairage_2026-05-13.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_gauche_2026-05-13.yaml">YAML Page</a>


</blockquote>
</details>

<details>
<summary>📄 <b>Page Droite</b> — 3 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C1_ECLAIRAGE/PAGE_ECLAIRAGE.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C1_07_Commandes_Eclairage/page_L3C1_eclairage_droite_2026-05-13.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#tete_de_lit</code> — 2 entité(s)</summary>
<blockquote><ul>
<li><code>light.hue_color_candle_chambre_eric</code></li>
<li><code>light.hue_color_candle_chambre_gege</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bureau</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>light.bureau</code></li>
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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C2_PRISES/PAGE_PRISES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C2_08_Commandes_Prises/page_L3C2_prises_2026-05-14.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L3C3_STORES/PAGE_STORES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L3C3_09_Stores_Fenetres/page_L3C3_stores_2026-05-14.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b> — 5 pop-up(s)</summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C2_MINI_PC/PAGE_MINI_PC.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L4C2_11_Mini_PC/page_L4C2_mini_pc_2026-05-14.yaml">YAML Page</a>


<details>
<summary>💬 Pop-up <code>#speed</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.system_monitor_utilisation_du_processeur</code> — <i>Natif HA</i></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#temp</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.temperature_cpu_package</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#conso</code> — 7 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.mini_pc_avg_watts_mensuel</code></li>
<li><code>sensor.mini_pc_avg_watts_quotidien</code></li>
<li><code>sensor.prise_mini_pc_ikea_current</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_energy</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_mensuel_um</code></li>
<li><code>sensor.prise_mini_pc_ikea_power</code> — <i>Natif HA</i></li>
<li><code>sensor.prise_mini_pc_ikea_quotidien_um</code></li>
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


</blockquote>
</details>

<details>
<summary>📄 <b>Page Gauche</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C3_MAJ_HA/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_gauche_2026-05-14.yaml">YAML Page</a>


</blockquote>
</details>

<details>
<summary>📄 <b>Page Droite</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L4C3_MAJ_HA/PAGE_MAJ.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L4C3_12_MAJ_HA/page_L4C3_maj_ha_droite_2026-05-14.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C1_PILES_BATTERIES/PAGE_BATTERIES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C1_13_Batteries_Piles/page_L5C1_batteries_piles_2026-05-14.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page Droite</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C2_BATTERIES_PORTABLES/PAGE_BATTERIES_PORTABLES.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C2_14_Batteries_Portables/page_L5C2_batteries_portables_droite_2026-05-12.yaml">YAML Page</a>


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


</blockquote>
</details>

<details>
<summary>📄 <b>Page</b></summary>
<blockquote>
📄 <a href="Docs/docs_dashboard/docs/L5C3_MARIADB/PAGE_SYSTEME.md">Doc Page</a><br>
⚙️ <a href="Docs/Dashboard/L5C3_15_MariaDB/page_L5C3_mariadb_2026-05-10.yaml">YAML Page</a>


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
<summary>💬 Pop-up <code>#spm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_salon_moy_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#scov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_bureau_ikea_pm25</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_bureau_ppb</code></li>
<li><code>sensor.tcov_salon_moy_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bpm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_bureau_moy_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#bcov</code> — 3 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.qualite_air_chambre_ikea_pm25</code> — <i>Natif HA</i></li>
<li><code>sensor.tcov_bureau_moy_24h</code></li>
<li><code>sensor.tcov_chambre_ppb</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#cpm25</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.pm2_5_chambre_moy_24h</code></li>
</ul></blockquote>
</details>

<details>
<summary>💬 Pop-up <code>#ccov</code> — 1 entité(s)</summary>
<blockquote><ul>
<li><code>sensor.tcov_chambre_moy_24h</code></li>
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


</blockquote>
</details>

</blockquote>
</details>

---

*Dernière mise à jour : 2026-05-30*
---

## ⚙️ 03 — AUTOMATIONS (48 automations)

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
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_ALERTE_KO.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/github_backup/git_alerte_ko.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_HOURLY.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/github_backup/git_hourly.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>⚠️ <b>[02-Backup] Git daily (03:00)</b></summary>
<blockquote>
<i>Backup natif HA + push Git quotidien à 03h00</i><br><br>
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_DAILY.md">Documentation</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[03-Backup] Git weekly (dim 01:30)</b></summary>
<blockquote>
<i>Backup natif HA + push + tag weekly chaque dimanche à 01:30</i><br><br>
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_WEEKLY.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/github_backup/git_weekly.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>[04-Backup] Git push manuel</b></summary>
<blockquote>
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_PUSH_MANUEL.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/github_backup/git_push_manuel.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_PUSH_WEEKLY_MANUEL.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/github_backup/git_push_weekly_manuel.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/BACKUP/GIT_AU_DEMARRAGE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/github_backup/git_au_demarrage.yaml">YAML source</a><br>

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
📄 <a href="Docs/docs_automations/docs/METEO/ALERTE_METEO_CARTES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/meteo/alerte_meteo_cartes.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/METEO/UPDATE_PREV_TEMPERATURE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/meteo/update_prev_temperature.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/METEO/UPDATE_PREV_HUMIDITY.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/meteo/update_prev_humidity.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/METEO/NOTIF_FOUDRE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/meteo/notif_foudre.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/METEO/MAJ_TEMPS_FOUDRE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/meteo/maj_temps_foudre.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/A0_CLIM_JOUR.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/A0_clim_jour_2026-01-11.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/B0_CLIM_NUIT.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/B0_clim_nuit_2026-01-11.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/C_GARDIEN_ECO.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/C_gardien_eco.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/D_NOTIF_TEMP_JOUR.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/D_notif_temp_jour.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/E_NOTIF_TEMP_NUIT.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/E_notif_temp_nuit.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/F_NOTIF_FERMETURE_FENETRES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/F_notif_fermeture_fenetres.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(G) (CLIM) Automatisation Arrêt Clim Notification</b></summary>
<blockquote>
<i>Notification quand une clim est coupée manuellement, seulement si</i><br><br>
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/G_ARRET_CLIM_NOTIF.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/G_arret_clim_notif.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/H_NOTIF_MODE_CHANGEMENT.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/H_notif_mode_changement.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/I_DEBUG_FORCE_MODE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/I_debug_force_mode.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/J_SYNCHRO_NOTIF_PRISE_COUPEE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/J_synchro_notif_prise_coupee.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> 🔄`state`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>(K) (DEBUG) Notifier les changements de message clim (Mobile)</b></summary>
<blockquote>
<i>Surveille et notifie les changements d'état du message personnalisé.</i><br><br>
📄 <a href="Docs/docs_automations/docs/P1_CLIM_CHAUFFAGE/L_DEBUG_NOTIF_MESSAGE_CLIM.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_clim_chauffage/L_debug_notif_message_clim.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CUISINE/A_CHAUFFAGE_CUISINE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_cuisine/A_chauffage_cuisine.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_CUISINE/B_CHAUFFAGE_CUISINE_VACANCES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_cuisine/B_chauffage_cuisine_vacances.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_SDB/A_SOUFFLANT_SDB.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_sdb/A_soufflant_sdb_gestion_intelligente.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_SDB/D_WATCHDOG_RADIATEUR_SDB.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_sdb/D_sdb_watchdog_radiateur.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P1_SDB/E_MINUTERIE_SECHE_SERVIETTES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P1_sdb/E_minuterie_seche_serviettes.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P2_PRISES/ECO_PRISES_DYNAMIQUE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P2_prises/P2_eco_prises_dynamique.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P2_PRISES/GESTION_PC_BUREAU.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P2_prises/gestion_pc_bureau.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P2_PRISES/GESTION_TV_CHAMBRE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P2_prises/gestion_tv_chambre.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/ALLUMAGE_LUMIERE_ENTREE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_eclairage/allumage_lumiere_entree.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BOUTON_INTER_IKEA_4.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_salon_bouton_inter_ikea_4.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BOUTON_INTER_IKEA_4.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_salon_bouton_inter_ikea_4.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BOUTON_INTER_SOMRIG.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_salon_bouton_inter_somrig.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BUREAU_RODRET_TOGGLE_BLANCHES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_eclairage/P3_bureau_bouton_rodret_toggle_blanches.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BUREAU_WATCHDOG_SYNCHRO_LAMPES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_eclairage/bureau_watchdog_synchro_lampes.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BUREAU_FORCER_PLAY_ON.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_eclairage/bureau_forcer_play_on_si_pc.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/P3_ECLAIRAGE/BUREAU_ACTIVATION_ECRAN_SYNCHRO.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/P3_eclairage/bureau_activation_ecran_synchro.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/STORES/GESTION_STORE_SALON.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/stores/gestion_store_salon.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/STORES/GESTION_STORE_BUREAU.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/stores/gestion_store_bureau.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/ENERGIE/BASCULEMENT_TARIF_HPHC.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/energie/basculement_tarif_hphc.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Log Écart Linky vs Nodon</b></summary>
<blockquote>
<i>Enregistre l'écart à 23:59 pile</i><br><br>
📄 <a href="Docs/docs_automations/docs/ENERGIE/LOG_ECART_LINKY_NODON.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/energie/log_ecart_linky_nodon.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/SYSTEME/DB_PURGE_MARIADB.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/systeme/db_purge_mariadb.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Économie Énergie VS Code</b></summary>
<blockquote>
<i>Coupe VS Code si son CPU dépasse 10% ou s'il est inactif, avec confirmation</i><br><br>
📄 <a href="Docs/docs_automations/docs/SYSTEME/ECONOMIE_ENERGIE_VSCODE.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/systeme/economie_energie_vscode.yaml">YAML source</a><br>
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
📄 <a href="Docs/docs_automations/docs/SYSTEME/VEILLE_GITHUB_RELEASES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/systeme/veille_github_releases.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⚡`event`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Système - Watchdog Piles (HUE/IKEA/SONOFF)</b></summary>
<blockquote>
<i>Vérification 3x/jour basée sur les groupes de la vue synthétique (seuil</i><br><br>
📄 <a href="Docs/docs_automations/docs/SYSTEME/WATCHDOG_PILES.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/systeme/watchdog_piles.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>Z2M last_seen</b></summary>
<blockquote>
<i>Surveillance des capteurs Zigbee injoignables (plus de 8h ou indisponibles)</i><br><br>
📄 <a href="Docs/docs_automations/docs/SYSTEME/Z2M_LAST_SEEN.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/systeme/z2m_last_seen.yaml">YAML source</a><br>
<br><b>Déclencheurs :</b> ⏰`time` · ⏰`time_pattern`<br>

</blockquote>
</details>

<details>
<summary>✅ <b>DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)</b></summary>
<blockquote>
📄 <a href="Docs/docs_automations/docs/SYSTEME/DIAG_ENREGISTREMENT_JOURNALIER.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/systeme/diag_enregistrement_journalier.yaml">YAML source</a><br>

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
📄 <a href="Docs/docs_automations/docs/RASPI/RPi4_FAN_PWM.md">Documentation</a><br>
⚙️ <a href="DOCS/03_docs_automations/docs_automations_YAML/raspi/A_rpi_fan_pwm_6_states.yaml">YAML source</a><br>
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

*Dernière mise à jour : 2026-05-30 | 48 automations*
---

## 🔧 04 — SCRIPTS

*Scripts ba