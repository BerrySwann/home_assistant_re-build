# 🔑 RÉFÉRENCE IDs AUTOMATIONS — ReBuild ↔ PROD
> Utilité : retrouver instantanément une automation dans HA UI ou dans les templates
> Colonne "ID PROD" = à remplir manuellement depuis HA → Paramètres → Automatisations → ⚙️ → Modifier YAML

---

## 📌 LÉGENDE

| Colonne | Description |
|:--------|:------------|
| **ID ReBuild** | Valeur du champ `id:` dans le YAML ReBuild (slug court — sert dans les triggers `id:`) |
| **Entity_id HA** | Identifiant HA déduit de l'alias — utilisable dans les templates `{{ states('automation.xxx') }}` |
| **ID PROD** | UUID interne HA — visible dans l'URL de l'automation dans HA UI (à remplir) |

---

## 🟥 CLIM — P1_clim_chauffage/ (13)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 01 | ~~(A-0) 2026-01-01 Automatisation CLIM (07h30 <-> 21h00)~~ | `force_run` | `automation.a_0_2026_01_01_...` | ❌ À SUPPRIMER |
| 02 | (A-0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00) | `ha_restart` | `automation.a_0_2026_01_11_automatisation_clim_jour_07h30_21h00` | |
| 03 | ~~(B-0) 2026-01-02 Automatisation CLIM NUIT (21h00 <-> 07h30)~~ | `force_run` | `automation.b_0_2026_01_02_...` | ❌ À SUPPRIMER |
| 04 | (B-0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30) | `ha_restart` | `automation.b_0_2026_01_11_automatisation_clim_nuit_21h00_07h30` | |
| 05 | (C) (CLIM OFF) Gardien Éco (Delta T < -1 et T°Ext > Seuil Non-Chauffage) | — | `automation.c_clim_off_gardien_eco_delta_t_1_et_t_ext_seuil_non_chauffage` | |
| 06 | (D) Notification température Up ou Down de (7h30 -> 21h00) | — | `automation.d_notification_temperature_up_ou_down_de_7h30_21h00` | |
| 07 | (E) Notification température Up ou Down de (21h00 -> 7h30) | — | `automation.e_notification_temperature_up_ou_down_de_21h00_7h30` | |
| 08 | (F) (CLIM) Notification de fermeture des fenêtres | — | `automation.f_clim_notification_de_fermeture_des_fenetres` | |
| 09 | (G) (CLIM) Automatisation Arrêt Clim Notification | — | `automation.g_clim_automatisation_arret_clim_notification` | |
| 10 | (H) (CLIM) Notification de changement de mode Été/Fan/Hiver | — | `automation.h_clim_notification_de_changement_de_mode_ete_fan_hiver` | |
| 11 | (I) (CLIM DEBUG) Force Mode Correct & Sécurité | — | `automation.i_clim_debug_force_mode_correct_securite` | |
| 12 | (J) Synchro & Notif Clim si Prise Coupée | — | `automation.j_synchro_notif_clim_si_prise_coupee` | |
| 13 | (K) (DEBUG) Notifier les changements de message clim (Mobile) | — | `automation.k_debug_notifier_les_changements_de_message_clim_mobile` | |

---

## 🟧 CUISINE — P1_cuisine/ (2)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 14 | A - Chauffage Cuisine (4h45-7h LMMJ / 5h45-8h VSD) | — | `automation.a_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9_20_5` | |
| 15 | B - Chauffage Cuisine Vacances | — | `automation.b_chauffage_cuisine_vacances` | |

---

## 🟨 SDB — P1_sdb/ (6)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 16 | A - SALLE DE BAIN - DÉMARRAGE ET INITIALISATION DU SOUFFLANT | — | `automation.a_salle_de_bain_demarrage_et_initialisation_du_soufflant` | |
| 17 | A - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT | `inter_change` | `automation.a_2026_02_01_salle_de_bain_gestion_intelligente_soufflant` | |
| 18 | A - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT | `inter_change` | `automation.a_salle_de_bain_gestion_intelligente_soufflant` | |
| 19 | B - SALLE DE BAIN - GESTION RÉSISTANCES DU SOUFFLANT | `temp_23` | `automation.b_salle_de_bain_gestion_resistances_du_soufflant` | |
| 20 | C - SALLE DE BAIN - GESTION ARRÊT SÉCURISÉ DU SOUFFLANT | — | `automation.c_salle_de_bain_gestion_arret_securise_du_soufflant` | |
| 21 | D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR | — | `automation.d_salle_de_bain_watchdog_securite_radiateur` | |
| 22 | E - Minuterie Sèche Serviettes Salle de Bain (Timer Absolu **2h**) | — | `automation.e_minuterie_seche_serviettes_salle_de_bain_timer_absolu_1h` | |

> ⚠️ #22 : entity_id HA garde "1h" (issu de l'ancien alias) — sera mis à jour si tu renommes dans HA

---

## 🟦 PRISES — P2_prises/ (5)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 23 | Bureau : Allumage Manu PC (MQTT) Poussoir (IKEA TRADFRI) | — | `automation.bureau_allumage_manu_pc_mqtt_poussoir_ikea_tradfri` | |
| 24 | Automation éCO. Prises | — | `automation.automation_eco_prises` | |
| 25 | Gestion PC bureau : Scène de Fin + Notif | — | `automation.gestion_pc_bureau_scene_de_fin_notif` | |
| 26 | Gestion TV Chambre : Scène de Fin + Notif | — | `automation.gestion_tv_chambre_scene_de_fin_notif` | |
| 27 | Bouton IKEA RODRET - Soufflant SdB Gestion ON/OFF (JSON) | — | `automation.bouton_ikea_rodret_soufflant_sdb_gestion_on_off_json` | |
| 28 | Bouton IKEA RODRET - TV Chambre (JSON) | — | `automation.bouton_ikea_rodret_tv_chambre_json` | |

---

## 🟩 ÉCLAIRAGE — P3_eclairage/ (5)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 29 | Allumage Lumière Entrée | — | `automation.allumage_lumiere_entree` | |
| 30 | BUREAU_ACTIVATION_ECRAN_SYNCHRO | `pc_on` | `automation.bureau_activation_ecran_synchro` | |
| 31 | BUREAU - BOUTON RODRET TOGGLE BLANCHES | — | `automation.bureau_bouton_rodret_toggle_blanches` | |
| 32 | Bureau - Forcer Play ON si PC tourne | — | `automation.bureau_forcer_play_on_si_pc_tourne` | |
| 33 | BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES | — | `automation.bureau_watchdog_synchronisation_lampes_blanches` | |

---

## 💾 BACKUP — backup/ (4)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 34 | [Backup] Alerte si KO 15 min | — | `automation.backup_alerte_si_ko_15_min` | |
| 35 | [Backup] Git au démarrage HA | — | `automation.backup_git_au_demarrage_ha` | |
| 36 | [Backup] Git hourly H+10 | — | `automation.backup_git_hourly_h_10` | |
| 37 | [Backup] Git weekly (dim 01:30) | — | `automation.backup_git_weekly_dim_01_30` | |

---

## 🌡️ STORES — stores/ (2)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 38 | Gestion Optimisée du Store Bureau | — | `automation.gestion_optimisee_du_store_bureau` | |
| 39 | Gestion Optimisée du Store Salon (Avec Mode Anti-Reflet PC) | — | `automation.gestion_optimisee_du_store_salon_avec_mode_anti_reflet_pc` | |

---

## 🌦️ MÉTÉO — meteo/ (6 dont 2 capteurs)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 40 | Alerte Météo France actualisation des "CARTES" | `Start` | `automation.alerte_meteo_france_actualisation_des_cartes` | |
| 41 | Mettre à jour le temps du dernier impact de foudre | — | `automation.mettre_a_jour_le_temps_du_dernier_impact_de_foudre` | |
| 42 | Notification de la foudre | — | `automation.notification_de_la_foudre` | |
| 43 | Update previous humidity | — | `automation.update_previous_humidity` | |
| 44 | Update previous temperature | — | `automation.update_previous_temperature` | |
| 48 | Mettre à jour le texte du temps écoulé | — | `automation.mettre_a_jour_le_texte_du_temps_ecoule` | |

---

## ⚙️ SYSTÈME — systeme/ (4)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 45 | DB Purge MariaDB + Repack | — | `automation.db_purge_mariadb_repack` | |
| 46 | DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT) | — | `automation.diag_enregistrement_journalier_6_postes_dut` | |
| 47 | Système - Économie Énergie VS Code | — | `automation.systeme_economie_energie_vs_code` | |
| 49 | Système - Watchdog Piles (HUE/IKEA/SONOFF) | — | `automation.systeme_watchdog_piles_hue_ikea_sonoff` | |

---

## ⚡ ÉNERGIE & DIVERS — energie/ (2) + ❓ INCERTAIN (1)

| # | ALIAS | ID ReBuild | Entity_id HA | ID PROD |
|:--|:------|:-----------|:-------------|:--------|
| 50 | Z2M last_seen | — | `automation.z2m_last_seen` | |
| 51 | ~~NOTIF - Gardien Énergétique (Anomalies)~~ | `radiateur_cuisine` | `automation.notif_gardien_energetique_anomalies` | ❓ À CONFIRMER suppr. |
| 52 | ÉNERGIE - SURVEILLANCE GROS ÉLECTRO EN HP | — | `automation.energie_surveillance_gros_electro_en_hp` | |

---

## 📋 COMMENT TROUVER L'ID PROD (UUID)

```
HA → Paramètres → Automatisations → [clic sur l'automation]
→ URL du navigateur = /config/automation/edit/[UUID]
→ Copier l'UUID et le coller dans la colonne "ID PROD" ci-dessus
```

Ou depuis l'éditeur YAML HA → l'`id:` en haut du bloc = UUID PROD

---

*Généré le 2026-04-05 — Source : ReBuild GitHub (52 automations)*
*Colonne "ID PROD" = à remplir depuis HA UI*
