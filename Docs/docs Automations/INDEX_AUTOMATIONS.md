# 📋 INDEX GLOBAL DES AUTOMATIONS
> Dernière mise à jour : 2026-04-06
> Source de vérité : `automations_corrige/` (41 fichiers)

---

## 🟥 P1 — CLIM & CHAUFFAGE

### P1_clim_chauffage/ (13 fichiers)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `A0_clim_jour_2026-01-11.yaml` | (A-0) CLIM JOUR 07H30↔21H00 | [→ Doc](P1_CLIM_CHAUFFAGE/A0_CLIM_JOUR.md) |
| ~~`A0_clim_jour_2026-01-01.yaml`~~ | ❌ OBSOLÈTE | — |
| `B0_clim_nuit_2026-01-11.yaml` | (B-0) CLIM NUIT 21H00↔07H30 | [→ Doc](P1_CLIM_CHAUFFAGE/B0_CLIM_NUIT.md) |
| ~~`B0_clim_nuit_2026-01-02.yaml`~~ | ❌ OBSOLÈTE | — |
| `C_gardien_eco.yaml` | (C) Gardien Éco Delta T | [→ Doc](P1_CLIM_CHAUFFAGE/C_GARDIEN_ECO.md) |
| `D_notif_temp_jour.yaml` | (D) Notif T° Jour | [→ Doc](P1_CLIM_CHAUFFAGE/D_NOTIF_TEMP_JOUR.md) |
| `E_notif_temp_nuit.yaml` | (E) Notif T° Nuit | [→ Doc](P1_CLIM_CHAUFFAGE/E_NOTIF_TEMP_NUIT.md) |
| `F_notif_fermeture_fenetres.yaml` | (F) Notif Fermeture Fenêtres | [→ Doc](P1_CLIM_CHAUFFAGE/F_NOTIF_FERMETURE_FENETRES.md) |
| `G_arret_clim_notif.yaml` | (G) Arrêt Clim Notif | [→ Doc](P1_CLIM_CHAUFFAGE/G_ARRET_CLIM_NOTIF.md) |
| `H_notif_mode_changement.yaml` | (H) Notif Changement Mode | [→ Doc](P1_CLIM_CHAUFFAGE/H_NOTIF_MODE_CHANGEMENT.md) |
| `I_debug_force_mode.yaml` | (I) Watchdog Force Mode | [→ Doc](P1_CLIM_CHAUFFAGE/I_DEBUG_FORCE_MODE.md) |
| `J_synchro_notif_prise_coupee.yaml` | (J) Synchro Prise Coupée | [→ Doc](P1_CLIM_CHAUFFAGE/J_SYNCHRO_NOTIF_PRISE_COUPEE.md) |
| `L_debug_notif_message_clim.yaml` | (L) Debug Notif Message Clim | [→ Doc](P1_CLIM_CHAUFFAGE/L_DEBUG_NOTIF_MESSAGE_CLIM.md) |

### P1_cuisine/ (2 fichiers)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `A_chauffage_cuisine.yaml` | Chauffage Cuisine LMMJ/VSD | [→ Doc](P1_CUISINE/A_CHAUFFAGE_CUISINE.md) |
| `B_chauffage_cuisine_vacances.yaml` | Chauffage Cuisine Vacances | [→ Doc](P1_CUISINE/B_CHAUFFAGE_CUISINE_VACANCES.md) |

### P1_sdb/ (1 fichier)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `E_minuterie_seche_serviettes.yaml` | Minuterie Sèche-Serviettes 2h | [→ Doc](P1_SDB/E_MINUTERIE_SECHE_SERVIETTES.md) |

---

## 🟦 P2 — PRISES

| Fichier | Alias | Doc |
|:---|:---|:---|
| `P2_prises/bureau_allumage_pc.yaml` | Allumage Manu PC (MQTT Poussoir) | [→ Doc](P2_PRISES/BUREAU_ALLUMAGE_PC.md) |
| `P2_prises/eco_prises.yaml` | Automation éCO Prises | [→ Doc](P2_PRISES/ECO_PRISES.md) |
| `P2_prises/gestion_pc_bureau.yaml` | Gestion PC Bureau Scène Fin | [→ Doc](P2_PRISES/GESTION_PC_BUREAU.md) |
| `P2_prises/gestion_tv_chambre.yaml` | Gestion TV Chambre Scène Fin | [→ Doc](P2_PRISES/GESTION_TV_CHAMBRE.md) |
| `P2_prises/rodret_soufflant_sdb.yaml` | RODRET Soufflant SDB | [→ Doc](P2_PRISES/RODRET_SOUFFLANT_SDB.md) |
| `P2_prises/rodret_tv_chambre.yaml` | RODRET TV Chambre | [→ Doc](P2_PRISES/RODRET_TV_CHAMBRE.md) |
| `P2_bouton_rodret_soufflant_sdb.yaml` | ⚠️ DOUBLON RODRET SDB | [→ Doc](P2_PRISES/RODRET_SOUFFLANT_SDB.md) |

---

## 🟩 P3 — ÉCLAIRAGE

| Fichier | Alias | Doc |
|:---|:---|:---|
| `P3_eclairage/allumage_lumiere_entree.yaml` | Allumage Lumière Entrée | [→ Doc](P3_ECLAIRAGE/ALLUMAGE_LUMIERE_ENTREE.md) |
| `P3_salon_bouton_inter_ikea_4.yaml` | Inter IKEA 4 Touches Salon | [→ Doc](P3_ECLAIRAGE/BOUTON_INTER_IKEA_4.md) |
| `P3_salon_bouton_inter_somrig.yaml` | Inter IKEA SOMRIG Salon | [→ Doc](P3_ECLAIRAGE/BOUTON_INTER_SOMRIG.md) |

---

## 🗂️ BACKUP (4 fichiers)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `backup/git_au_demarrage.yaml` | Git Push au Démarrage | [→ Doc](BACKUP/GIT_AU_DEMARRAGE.md) |
| `backup/git_hourly.yaml` | Git Push Horaire H+10 | [→ Doc](BACKUP/GIT_HOURLY.md) |
| `backup/git_weekly.yaml` | Git Push Hebdo + Tag | [→ Doc](BACKUP/GIT_WEEKLY.md) |
| `backup/git_alerte_ko.yaml` | Alerte Git KO 15 min | [→ Doc](BACKUP/GIT_ALERTE_KO.md) |

---

## ⚡ ÉNERGIE (1 fichier)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `energie/surveillance_gros_electro_hp.yaml` | Surveillance Gros Électro HP | [→ Doc](ENERGIE/SURVEILLANCE_GROS_ELECTRO_HP.md) |

---

## 🌩️ MÉTÉO (5 fichiers)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `meteo/alerte_meteo_cartes.yaml` | Alerte MF Actualisation Cartes | [→ Doc](METEO/ALERTE_METEO_CARTES.md) |
| `meteo/maj_temps_foudre.yaml` | MAJ Temps Dernier Impact | [→ Doc](METEO/MAJ_TEMPS_FOUDRE.md) |
| `meteo/notif_foudre.yaml` | Notification Foudre | [→ Doc](METEO/NOTIF_FOUDRE.md) |
| `meteo/update_prev_temperature.yaml` | Snapshot T° Ext (30 min) | [→ Doc](METEO/UPDATE_PREV_TEMPERATURE.md) |
| `meteo/update_prev_humidity.yaml` | Snapshot Humidité Ext (30 min) | [→ Doc](METEO/UPDATE_PREV_HUMIDITY.md) |

---

## 🪟 STORES (2 fichiers)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `stores/gestion_store_bureau.yaml` | Store Bureau (3 scénarios) | [→ Doc](STORES/GESTION_STORE_BUREAU.md) |
| `stores/gestion_store_salon.yaml` | Store Salon Anti-Reflet PC | [→ Doc](STORES/GESTION_STORE_SALON.md) |

---

## 🖥️ SYSTÈME (5 fichiers)

| Fichier | Alias | Doc |
|:---|:---|:---|
| `systeme/db_purge_mariadb.yaml` | Purge MariaDB 00:30 | [→ Doc](SYSTEME/DB_PURGE_MARIADB.md) |
| `systeme/diag_enregistrement_journalier.yaml` | Diag Log 15 min (7 postes) | [→ Doc](SYSTEME/DIAG_ENREGISTREMENT_JOURNALIER.md) |
| `systeme/economie_energie_vscode.yaml` | Économie Énergie VS Code | [→ Doc](SYSTEME/ECONOMIE_ENERGIE_VSCODE.md) |
| `systeme/watchdog_piles.yaml` | Watchdog Piles 3×/jour | [→ Doc](SYSTEME/WATCHDOG_PILES.md) |
| `systeme/z2m_last_seen.yaml` | Z2M Last Seen Zigbee | [→ Doc](SYSTEME/Z2M_LAST_SEEN.md) |

---

## ⚠️ Points d'attention globaux

| # | Problème | Fichier |
|:---|:---|:---|
| 1 | **Doublon obsolète** A0 `2026-01-01` → à supprimer | `P1_clim_chauffage/` |
| 2 | **Doublon obsolète** B0 `2026-01-02` → à supprimer | `P1_clim_chauffage/` |
| 3 | **Doublon exact** RODRET SDB dans `P2_prises/` ET à la racine | `P2_bouton_rodret_soufflant_sdb.yaml` |
| 4 | **Bug** : trigger lave-vaisselle pointe sur lave-linge | `energie/surveillance_gros_electro_hp.yaml` |
