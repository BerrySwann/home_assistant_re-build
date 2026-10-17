# DEPENDANCES GLOBALES HERMES - TABLEAU DE BORD HA
*Version Hermes - architecture par CARTE : vignettes dashboard (L0C0-L6C3) + scripts sh + automations par pole + scripts + complement + orphelines. Types auto-detectes, annotations Claude conservees. Genere automatiquement.*
*Derniere mise a jour : 2026-10-13 21h51 (Hermes - regeneration complete apres audit huissier + corrections skills)*

## LEGENDE

| Symbole | Signification |
|:-------:|:-------------|
| [type] | Type de carte |
| (TPL) | Entite definie dans un template (templates/) |
| (SEN) | Entite definie dans sensors/ |
| (UM) | Entite definie dans utility_meter/ |
| (NAT) | Entite native/UI ou autre fichier |
| ORPHELINE | Entite dans aucun dashboard, automation ni script |

## MATRICE DES VIGNETTES

| ID | Vignette | Entites | Cartes |
|:---|:---------|:-------:|:------:|
| **L0C0** | PAGE_Home | 20 | 13 |
| **L1C1** | Meteo | 46 | 120 |
| **L1C2** | Temperatures | 50 | 93 |
| **L1C3** | Commandes_Clim | 87 | 207 |
| **L2C1** | Energie_Generale | 181 | 153 |
| **L2C2** | Energie_Clim | 104 | 180 |
| **L2C3** | Energie_Eclairage | 85 | 79 |
| **L3C1** | Commandes_Eclairage | 44 | 85 |
| **L3C2** | Commandes_Prises | 24 | 22 |
| **L3C3** | Stores_Fenetres | 17 | 53 |
| **L4C1** | Proxmox | 63 | 100 |
| **L4C2** | Mini_PC | 28 | 99 |
| **L4C3** | MAJ_HA | 10 | 110 |
| **L5C1** | Batteries_Piles | 37 | 11 |
| **L5C2** | Batteries_Portables | 49 | 35 |
| **L5C3** | MariaDB | 25 | 73 |
| **L6C1** | Air_Qualite | 15 | 30 |
| **L6C2** | Pollution_Pollen | 19 | 32 |
| **L6C3** | VigiEau | 2 | 16 |

## SOMMAIRE

- Vignettes dashboard : 19 sections (L0C0 a L6C3), cartes detaillees
- Scripts .sh : 8
- Automations : 63 (par pole, 17 poles)
- Scripts non-sh : 2
- Complement : fichiers racine et repertoires hors dashboard
- Entites orphelines : 183 (139 vivantes + 44 mortes)

## 1. VIGNETTES DASHBOARD (L0C0 -> L6C3) - PAR CARTE

### L0C0 - PAGE_Home

*Validée le 2026-06-13*

> Les 18 vignettes de la grille sont documentées dans leurs sections respectives (L1C1–L6C3). Cette section couvre **uniquement les cartes permanentes en haut de la HOME page** qui n'appartiennent à aucune vignette. Ces fichiers font partie intégrante de la config HA et sont audités par `audit_md5.sh`. Ils n'alimentent pas directement d'entités dashboard - référencés ici pour inventaire complet. *Ajouté le 2026-06-15* Configurée via : Paramètres → Appareils & Services → Ajouter → File Génère des services `notify.file_*` utilisés par les automations. ✅ **Note 2026-08-08** : ligne ci-dessus confirmée par Eric (2026-08-08). La phrase tronquée (coupure sur "docs_da") a été complétée par hypothèse le 2026-07-19 ; hypothèse validée - `docs_dashboard/` est bien l'ancien répertoire supprimé le 2026-07-14 tel que documenté dans CLAUDE.md.

*20 entites, 13 cartes, 7 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 17)
  └─→ TPL: M_01_meteo_alertes_card.yaml (1)
  └─→ TPL: M_03_meteo_dernier_impact_foudre_card.yaml (1)
  └─→ TPL: P4_wifi_detection.yaml (1)
        └─→ VIGNETTE L0C0
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | NAT | (native/UI) |
| `device_tracker.mamour` | NAT | idem |
| `device_tracker.poco` | NAT | idem |
| `person.eric` | NAT | idem |
| `person.mamour` | NAT | idem |
| `sensor.maison_lightning_azimuth` | NAT | idem |
| `sensor.maison_lightning_counter` | NAT | idem |
| `sensor.maison_lightning_distance` | NAT | idem |
| `sensor.maison_lightning_localisation` | NAT | idem |
| `sensor.prise_lave_linge_nous_power` | NAT | idem |
| `sensor.prise_lave_vaisselle_nous_power` | NAT | idem |
| `sensor.studio_code_server_pourcentage_du_processeur` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.vence_original_condition` | NAT | idem |
| `sun.sun` | NAT | idem |
| `switch.plug_6_local` | NAT | idem |
| `weather.vence` | NAT | idem |
| `sensor.alerte_meteo` | TPL | M_01_meteo_alertes_card.yaml |
| `sensor.dernier_impact_foudre` | TPL | M_03_meteo_dernier_impact_foudre_card.yaml |
| `sensor.etat_wifi_maison` | TPL | P4_wifi_detection.yaml |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_detecteur_fuite_home_2026-06-13.yaml` | ✅ |
| `card_foudre_home_2026-06-13.yaml` | ✅ |
| `card_lave_linge_home_2026-06-13.yaml` | ✅ |
| `card_lave_vaisselle_home_2026-06-13.yaml` | ✅ |
| `card_meteocss_home_2026-06-28.yaml` | ✅ |
| `card_presence_home_2026-06-13.yaml` | ✅ |
| `card_vscode_home_2026-06-13.yaml` | ✅ |

### Detail par carte (complement Hermes)

#### card_detecteur_fuite_home_2026-06-13.yaml (1 cartes, 1 entites)

- [custom:mushroom-entity-card] Détecteur de fuite sous évier cuisine: binary_sensor.detecteur_de_fuite_ikea_water_leak (NAT)

#### card_foudre_home_2026-06-13.yaml (1 cartes, 5 entites)

- [custom:button-card] [[[
  const distRaw = states['sensor.maison_lightning_distan: sensor.dernier_impact_foudre (TPL), sensor.maison_lightning_azimuth (NAT), sensor.maison_lightning_counter (NAT), sensor.maison_lightning_distance (NAT), sensor.maison_lightning_localisation (NAT)

#### card_lave_linge_home_2026-06-13.yaml (1 cartes, 2 entites)

- [custom:mushroom-entity-card] Lave-linge: sensor.prise_lave_linge_nous_power (NAT), switch.plug_6_local (NAT)

#### card_lave_vaisselle_home_2026-06-13.yaml (1 cartes, 2 entites)

- [custom:mushroom-entity-card] Lave-vaisselle: sensor.prise_lave_vaisselle_nous_power (NAT), switch.plug_7_local (NAT)

#### card_meteocss_home_2026-06-28.yaml (1 cartes, 1 entites)

- [custom:meteocss-card] Météo CSS Home: weather.vence (NAT)

#### card_presence_home_2026-06-13.yaml (1 cartes, 4 entites)

- [custom:button-card] Présence: person.eric (NAT), person.mamour (NAT), device_tracker.poco (NAT), device_tracker.mamour (NAT)

#### card_vscode_home_2026-06-13.yaml (1 cartes, 1 entites)

- [custom:mushroom-template-card] VSCode: sensor.studio_code_server_pourcentage_du_processeur (NAT)

### L1C1 - Meteo

*46 entites, 120 cartes, 12 fichiers*

### Chaine de dependances

```
MATERIEL (NAT: 29)
  └─→ TPL: M_01_meteo_alertes_card.yaml (10)
  └─→ TPL: M_03_meteo_dernier_impact_foudre_card.yaml (1)
  └─→ TPL: M_03_meteo_direction_foudre_deg_card.yaml (1)
  └─→ TPL: M_03_meteo_direction_foudre_label_card.yaml (1)
  └─→ TPL: M_03_meteo_distance_foudre_km_card.yaml (1)
  └─→ TPL: M_03_meteo_timer_foudre_card.yaml (1)
  └─→ TPL: M_05_cycle_solaire.yaml (3)
  └─→ SEN: M_meteo_sensors_blitzortung.yaml (1)
        └─→ VIGNETTE L1C1
```

### Entites consommees par la vignette

| Entite | Type | Fichier source |
|:-------|:----:|:--------------|
| `sensor.06_weather_alert` | NAT | (native/UI) |
| `sensor.direction_du_vent_vence` | NAT | idem |
| `sensor.direction_du_vent_vence_label` | NAT | idem |
| `sensor.duree_du_jour_brut` | NAT | idem |
| `sensor.eclairs_annuel` | NAT | idem |
| `sensor.eclairs_hebdomadaire` | NAT | idem |
| `sensor.eclairs_horaire` | NAT | idem |
| `sensor.eclairs_mensuel` | NAT | idem |
| `sensor.eclairs_quotidien` | NAT | idem |
| `sensor.maison_lightning_azimuth` | NAT | idem |
| `sensor.maison_lightning_counter` | NAT | idem |
| `sensor.maison_lightning_distance` | NAT | idem |
| `sensor.maison_lightning_localisation` | NAT | idem |
| `sensor.moon_phase` | NAT | idem |
| `sensor.season` | NAT | idem |
| `sensor.sun_next_rising` | NAT | idem |
| `sensor.sun_next_setting` | NAT | idem |
| `sensor.th_balcon_nord_humidity` | NAT | idem |
| `sensor.th_balcon_nord_temperature` | NAT | idem |
| `sensor.vence_daily_precipitation` | NAT | idem |
| `sensor.vence_original_condition` | NAT | idem |
| `sensor.vence_pressure` | NAT | idem |
| `sensor.vence_uv` | NAT | idem |
| `sensor.vence_wind_gust` | NAT | idem |
| `sensor.vence_wind_speed` | NAT | idem |
| `sensor.vitesse_du_vent_vence` | NAT | idem |
| `sun.sun` | NAT | idem |
| `weather.vence` | NAT | idem |
| `zone.home` | NAT | idem |
| `sensor.alerte_avalanches` | TPL | M_01_meteo_alertes_card.yaml |
| `sensor.alerte_canicule` | TPL | idem |
| `sensor.alerte_grand_froid` | TPL | idem |
| `sensor.alerte_inondation` | TPL | idem |
| `sensor.alerte_meteo` | TPL | idem |
| `sensor.alerte_neige_verglas` | TPL | idem |
| `sensor.alerte_orages` | TPL | idem |
| `sensor.alerte_pluie_inondation` | TPL | idem |
| `sensor.alerte_vagues_submersion` | TPL | idem |
| `sensor.alerte_vent_violent` | TPL | idem |
| `sensor.dernier_impact_foudre` | TPL | M_03_meteo_dernier_impact_foudre_card.yaml |
| `sensor.direction_foudre_deg` | TPL | M_03_meteo_direction_foudre_deg_card.yaml |
| `sensor.direction_foudre_label` | TPL | M_03_meteo_direction_foudre_label_card.yaml |
| `sensor.distance_foudre_km` | TPL | M_03_meteo_distance_foudre_km_card.yaml |
| `sensor.timer_foudre` | TPL | M_03_meteo_timer_foudre_card.yaml |
| `sensor.duree_du_jour` | TPL | M_05_cycle_solaire.yaml |
| `sensor.tendance_duree_jour` | TPL | idem |
| `sensor.variation_quotidienne` | TPL | idem |
| `sensor.blitzortung_lightning_localisation` | SEN | M_meteo_sensors_blitzortung.yaml |

### Fichiers YAML deployables

| Fichier | Statut |
|:--------|:------:|
| `card_duree_du_jour_2026-05-23.yaml` | ✅ |
| `page_L1C1_meteo_2026-06-13.yaml` | ✅ |
| `vignette_L1C1_meteo_2026-05-16.yaml` | ✅ |
| `M_meteo_sensors_blitzortung.yaml` | ✅ |
| `M_01_meteo_alertes_card.yaml` | ✅ |
| `M_03_meteo_dernier_impact_foudre_card.yaml` | ✅ |
| `M_03_meteo_direction_foudre_deg_card.yaml` | ✅ |
| `M_03_meteo_direction_foudre_label_card.yaml` | ✅ |
| `M_03_meteo_distance_foudre_km_card.yaml` | ✅ |
| `M_03_meteo_timer_foudre_card.yaml` | ✅ |
| `M_05_cycle_solaire.yaml` | ✅ |

### Correction 2026-10-14 - sensor.blitzortung_lightning_last_impact_time

> **ENTITE SUPPRIMEE DU REGISTRE** : `sensor.blitzortung_lightning_last_impact_time` n'existe pas dans l'integration Blitzortung 1.7.3 (H:\custom_components\blitzortung) qui ne definit que azimuth, counter, distance. Verifie le 2026-10-14 par Claude (MODIFS_2026-10-14_claude.md) : 0 ligne dans states (jamais de valeur), pas dans states_meta (registre), 0 evenement state_changed.
>
> **Remplacement** : `input_datetime.dernier_eclair` (helper UI, ecrit par l'automation "Mettre a jour le temps du dernier impact de foudre" a chaque changement de `sensor.maison_lightning_counter > 0`).
>
> **Fichiers corriges** : `M_03_meteo_timer_foudre_card.yaml` (state -> states('input_datetime.dernier_eclair'), note datee dans PIEGES). Le template affichait toujours "Calme" avec l'ancienne entite.
>
> **Reste a faire** : `template.reload` dans HA (le capteur garde l'ancien code jusqu'au rechargement ou redemarrage). Non fait le 2026-10-14.
>
> **Anciennes references encore presentes** (a nettoyer) : TODO.md L637, TODO_2026-10-04_20h39.txt L104 (citent l'ancien nom comme entite meteo).

## 2. SCRIPTS .SH

*8 scripts actifs (dedup racine/sous-dossier), 0 entite HA referencee (scripts systeme/fichiers)*

### audit_md5.sh
*docs\04_docs_scripts\docs_scripts_SH\audit_md5\audit_md5.sh*

### audit_md5_md_yaml.sh
*docs\04_docs_scripts\docs_scripts_SH\audit_md5_md_yaml\audit_md5_md_yaml.sh*

### ha_git_backup.sh
*docs\04_docs_scripts\docs_scripts_SH\ha_git_backup\ha_git_backup.sh*

### hermes_audit_md5_docs.sh
*docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_docs\hermes_audit_md5_docs.sh*

### hermes_audit_md5_trigul_3md.sh
*docs\04_docs_scripts\docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_3md.sh*

### mf_vigilance_images.sh
*scripts\mf_vigilance_images.sh (racine H:) + local docs_scripts_SH\mf_vigilance_images\*

### setup_z2m.sh
*Infra_Proxmox\scripts\setup_z2m.sh*

### snapshot_rolling.sh
*Infra_Proxmox\scripts\snapshot_rolling.sh*

## 3. AUTOMATIONS (PAR POLE)

*63 automations reparties en 17 poles (fichiers YAML actifs, hors .bak et hors AUTOMATIONS.YALM ORIGINAL)*

### Pole P1_01_CLIM_CHAUFFAGE (10 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P1_01_CLIM_CHAUFFAGE\*

### Pole P1_03_Chauffage Salle de Bain (9 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P1_03_Chauffage Salle de Bain\*

### Pole P0_ENRIGE (6 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P0_ENRIGE\*

### Pole P3_Eclairage (6 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P3_Eclairage\*

### Pole Météo (5 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\Météo\*

### Pole Backup HA - GitHub (7 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\Backup HA - GitHub\*

### Pole P2_Alarme_Congélateur (3 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P2_Alarme_Congélateur\*

### Pole P2_éCO. Prises (3 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P2_éCO. Prises\*

### Pole P1_02_Cuisine (2 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\P1_02_Cuisine\*

### Pole Gestion des Stores (2 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\Gestion des Stores\*

### Pole Bouton Virtuel (2 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\Bouton Virtuel\*

### Pole MariaDB & VSCode Optimisation (2 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\MariaDB & VSCode Optimisation\*

### Pole _SANS_CATEGORIE (2 automations)

*Source : docs\03_docs_automations\docs_automations_YAML\_SANS_CATEGORIE\*

### Pole Contrôle Entity z2m (1 automation)

*Source : docs\03_docs_automations\docs_automations_YAML\Contrôle Entity z2m\*

### Pole RASPI (1 automation)

*Source : docs\03_docs_automations\docs_automations_YAML\RASPI\*

### Pole Tarif HC-HP (1 automation)

*Source : docs\03_docs_automations\docs_automations_YAML\Tarif HC-HP\*

### Pole Watchdog Piles (HUE-IKEA-SONOFF) (1 automation)

*Source : docs\03_docs_automations\docs_automations_YAML\Watchdog Piles (HUE-IKEA-SONOFF)\*

## 4. SCRIPTS NON-SH

### p1_master_gestion_clim.yaml
*04_docs_scripts\docs_scripts_YAML\p1_master_gestion_clim\p1_master_gestion_clim.yaml - 27 entites*

```
binary_sensor.contact_fenetre_bureau_sonoff_contact
binary_sensor.contact_fenetre_chambre_sonoff_contact
binary_sensor.contact_fenetre_cuisine_sonoff_contact
binary_sensor.contact_fenetre_salon_sonoff_contact
climate.clim_bureau_rm4_mini
climate.clim_chambre_rm4_mini
climate.clim_salon_rm4_mini
input_boolean.clim_bureau_arret_securise_en_cours
input_boolean.clim_chambre_arret_securise_en_cours
input_boolean.clim_salon_arret_securise_en_cours
notify.mobile_app_eric
sensor.consigne_de_base
sensor.mode_ete_hiver
sensor.nombre_de_fenetres_ouvertes
sensor.presence
sensor.temperature_cible
sensor.temperature_confort_nuit
sensor.temperature_corrige_chambre
sensor.temperature_corrige_eric
sensor.temperature_corrige_mamour
sensor.temperature_eco_ete
sensor.temperature_eco_ete_corrige
sensor.temperature_eco_hiver
sensor.temperature_eco_hiver_corrige
switch.clim_bureau_nous
switch.clim_chambre_nous
switch.clim_salon_nous
```

### scripts.yaml
*scripts.yaml - 51 entites referencees*

*Contient les scripts HA : j_1_1_salon_clim_on_off_intelligent, j_1_2_bureau_clim_on_off_intelligent, j_1_3_chambre_clim_on_off_intelligent, j_2_0_secu_arret_clim_protege, audit_md5, audit_md5_md_yaml, p1_master_gestion_clim, sdb_soufflant_demarrer, sdb_soufflant_arreter*

## 5. COMPLEMENT - FICHIERS CONFIG RACINE & REPERTOIRES HORS DASHBOARD

> Ces fichiers font partie integrante de la config HA et sont audites par `audit_md5.sh`.
> Ils n'alimentent pas directement d'entites dashboard - references ici pour inventaire complet.

### Fichiers racine /config/

| Fichier | Role | Audite |
|:--------|:-----|:------:|
| `automations.yaml` | Toutes les automations HA (gere via UI) - 62 automations | ✅ |
| `scripts.yaml` | Scripts HA (J-1-x, J-2-0, audit_md5) - 9 scripts | ✅ |
| `shell_command/` (repertoire) | Commandes shell (git backup, audit MD5, zone log P4) - `!include_dir_merge_named` | ✅ |
| `configuration.yaml` | Point d'entree HA - includes, integrations | ✅ |
| `sql.yaml` | Capteurs SQL (taille MariaDB) → L5C3 | ✅ |
| `input_button.yaml` | Boutons virtuels (declencheurs UI) | ✅ |
| `input_datetime.yaml` | Helpers date/heure (dont `dernier_eclair` pour le timer foudre) | ✅ |
| `input_select.yaml` | Helpers liste (mode soufflant SDB, etc.) | ✅ |
| `input_number/` | Helpers numeriques | ✅ |
| `scenes.yaml` | Scenes HA | ❌ hors scope |
| `secrets.yaml` | Identifiants - NE PAS auditer / synchroniser | ⛔ |

### Repertoires audites (DIRS)

| Repertoire | Contenu | Audite |
|:-----------|:--------|:------:|
| `sensors/` | Integrations kWh, stats min/max, qualite air, meteo blitzortung | ✅ |
| `templates/` | Calculs, AVG, UI, meteo, presence, stores | ✅ |
| `utility_meter/` | Compteurs AMHQ (P0→P3, meteo) | ✅ |
| `command_line/` | Meteo France, GitHub maintenance, audit MD5, IP externe | ✅ |
| `groups/` | Groupes batteries HUE/IKEA/SONOFF → L5C1 | ✅ |
| `input_booleans/` | Helpers booleens (verrous clim, presence…) | ✅ |
| `input_number/` | Helpers numeriques | ✅ |
| `packages/` | Packages CSS meteo (cssmeteo.yaml, demometeo.yaml) - Moon API | ✅ |
| `shell_command/` | Commandes shell (backup Git, audit MD5, zone log P4) | ✅ |

### Integration FILE (UI uniquement - notify.file interdit en YAML)

> Configuree via : Parametres → Appareils & Services → Ajouter → File
> Genere des services `notify.file_*` utilises par les automations.

| Service genere | Fichier destination | Utilise par |
|:---------------|:--------------------|:------------|
| `notify.file_zone_eric_txt` | `/config/.logs/zone_eric.txt` | `shell_command/P4/P4_log_eric_zone.yaml` → automation P4 presence |
| `notify.file_diag_conso_elec_txt` | `/config/notifs/diag_conso_elec.txt` | automation `energie/diag_enregistrement_journalier.yaml` |
| `notify.file_ecart_liky_vs_nodon_txt` | `/config/notifs/ecart_liky_vs_nodon.txt` | automation `energie/log_ecart_linky_vs_nodon.yaml` |

### Repertoires hors scope audit

| Repertoire | Raison |
|:-----------|:-------|
| `.scripts/` | Scripts shell - pas des entites HA |
| `notifs/` | Fichiers .txt - hors perimetre YAML |
| `blueprints/` | Blueprints HA - non modifies manuellement |
| `custom_components/` | Integrations HACS - non versionnees ici |
| `www/` | Ressources frontend - hors config HA |
| `docs_dashboard/` | Ancien repertoire, supprime le 2026-07-14, remplace par `docs/02_docs_dashboard/` |

## 6. ENTITES ORPHELINES (NI DASHBOARD, NI AUTOMATIONS, NI SCRIPTS)

*183 reelles (potentiellement mortes) + intermediaires de calcul + 52 familles (prefixes)*

*Recalcule le 2026-10-13 par Hermes : 521 entites definies dans les YAML modulaires, 1121 referencees (union dashboard + automations + scripts + templates + sensors + utility_meter + groups + command_line + shell_command + input_booleans). 183 definies mais jamais referencees.*

### 6.1 Vivantes (dans le registre HA) - 139

*Definies dans un YAML modulaire, jamais referencees, mais presentes dans le registre HA (etat connu). Candidates a verification ou reintegration.*

```
sensor.airfryer_avg_watts_annuel
sensor.airfryer_avg_watts_hebdomadaire
sensor.box_internet_avg_watts_annuel
sensor.box_internet_avg_watts_hebdomadaire
sensor.chargeurs_salon_avg_watts_annuel
sensor.chargeurs_salon_avg_watts_hebdomadaire
sensor.congelateur_avg_watts_annuel
sensor.congelateur_avg_watts_hebdomadaire
sensor.eclairage_appart_2_avg_watts_annuel
sensor.eclairage_appart_2_avg_watts_hebdomadaire
sensor.eclairage_appart_2_avg_watts_mensuel
sensor.eclairage_appart_2_avg_watts_quotidien
sensor.eclairage_appart_3_avg_watts_annuel
sensor.eclairage_appart_3_avg_watts_hebdomadaire
sensor.eclairage_appart_3_avg_watts_quotidien
sensor.eclairage_bureau_5_avg_watts_annuel
sensor.eclairage_bureau_5_avg_watts_hebdomadaire
sensor.eclairage_bureau_5_avg_watts_quotidien
sensor.eclairage_chambre_4_avg_watts_annuel
sensor.eclairage_chambre_4_avg_watts_hebdomadaire
sensor.eclairage_chambre_4_avg_watts_quotidien
sensor.eclairage_couloir_1_avg_watts_annuel
sensor.eclairage_couloir_1_avg_watts_hebdomadaire
sensor.eclairage_couloir_1_avg_watts_mensuel
sensor.eclairage_couloir_1_avg_watts_quotidien
sensor.eclairage_cuisine_1_avg_watts_annuel
sensor.eclairage_cuisine_1_avg_watts_hebdomadaire
sensor.eclairage_cuisine_1_avg_watts_mensuel
sensor.eclairage_cuisine_1_avg_watts_quotidien
sensor.eclairage_entree_1_avg_watts_annuel
sensor.eclairage_entree_1_avg_watts_hebdomadaire
sensor.eclairage_entree_1_avg_watts_mensuel
sensor.eclairage_entree_1_avg_watts_quotidien
sensor.eclairage_salon_5_avg_watts_annuel
sensor.eclairage_salon_5_avg_watts_hebdomadaire
sensor.eclairage_salon_5_avg_watts_mensuel
sensor.eclairage_salon_5_avg_watts_quotidien
sensor.eclairage_sdb_2_avg_watts_annuel
sensor.eclairage_sdb_2_avg_watts_hebdomadaire
sensor.eclairage_sdb_2_avg_watts_mensuel
sensor.eclairage_sdb_2_avg_watts_quotidien
sensor.hue_ambiance_lamp_salon_1_avg_watts_annuel
sensor.hue_ambiance_lamp_salon_1_avg_watts_hebdomadaire
sensor.hue_ambiance_lamp_salon_1_avg_watts_mensuel
sensor.hue_ambiance_lamp_salon_1_avg_watts_quotidien
sensor.hue_ambiance_lamp_salon_2_avg_watts_annuel
sensor.hue_ambiance_lamp_salon_2_avg_watts_hebdomadaire
sensor.hue_ambiance_lamp_salon_2_avg_watts_mensuel
sensor.hue_ambiance_lamp_salon_2_avg_watts_quotidien
sensor.hue_ambiance_lamp_salon_3_avg_watts_annuel
sensor.hue_ambiance_lamp_salon_3_avg_watts_hebdomadaire
sensor.hue_ambiance_lamp_salon_3_avg_watts_mensuel
sensor.hue_ambiance_lamp_salon_3_avg_watts_quotidien
sensor.hue_color_candle_chambre_eric_avg_watts_annuel
sensor.hue_color_candle_chambre_eric_avg_watts_hebdomadaire
sensor.hue_color_candle_chambre_eric_avg_watts_mensuel
sensor.hue_color_candle_chambre_eric_avg_watts_quotidien
sensor.hue_color_candle_chambre_gege_avg_watts_annuel
sensor.hue_color_candle_chambre_gege_avg_watts_hebdomadaire
sensor.hue_color_candle_chambre_gege_avg_watts_mensuel
sensor.hue_color_candle_chambre_gege_avg_watts_quotidien
sensor.hue_color_candle_salon_1_avg_watts_annuel
sensor.hue_color_candle_salon_1_avg_watts_hebdomadaire
sensor.hue_color_candle_salon_1_avg_watts_mensuel
sensor.hue_color_candle_salon_1_avg_watts_quotidien
sensor.hue_play_1_pc_bureau_avg_watts_annuel
sensor.hue_play_1_pc_bureau_avg_watts_hebdomadaire
sensor.hue_play_1_pc_bureau_avg_watts_mensuel
sensor.hue_play_1_pc_bureau_avg_watts_quotidien
sensor.hue_play_2_pc_bureau_avg_watts_annuel
sensor.hue_play_2_pc_bureau_avg_watts_hebdomadaire
sensor.hue_play_2_pc_bureau_avg_watts_mensuel
sensor.hue_play_2_pc_bureau_avg_watts_quotidien
sensor.hue_play_3_pc_bureau_avg_watts_annuel
sensor.hue_play_3_pc_bureau_avg_watts_hebdomadaire
sensor.hue_play_3_pc_bureau_avg_watts_mensuel
sensor.hue_play_3_pc_bureau_avg_watts_quotidien
sensor.hue_white_lamp_bureau_1_avg_watts_annuel
sensor.hue_white_lamp_bureau_1_avg_watts_hebdomadaire
sensor.hue_white_lamp_bureau_1_avg_watts_mensuel
sensor.hue_white_lamp_bureau_1_avg_watts_quotidien
sensor.hue_white_lamp_bureau_2_avg_watts_annuel
sensor.hue_white_lamp_bureau_2_avg_watts_hebdomadaire
sensor.hue_white_lamp_bureau_2_avg_watts_mensuel
sensor.hue_white_lamp_bureau_2_avg_watts_quotidien
sensor.hue_white_lamp_chambre_1_avg_watts_annuel
sensor.hue_white_lamp_chambre_1_avg_watts_hebdomadaire
sensor.hue_white_lamp_chambre_1_avg_watts_mensuel
sensor.hue_white_lamp_chambre_1_avg_watts_quotidien
sensor.hue_white_lamp_chambre_2_avg_watts_annuel
sensor.hue_white_lamp_chambre_2_avg_watts_hebdomadaire
sensor.hue_white_lamp_chambre_2_avg_watts_mensuel
sensor.hue_white_lamp_chambre_2_avg_watts_quotidien
sensor.hue_white_lamp_couloir_avg_watts_annuel
sensor.hue_white_lamp_couloir_avg_watts_hebdomadaire
sensor.hue_white_lamp_couloir_avg_watts_mensuel
sensor.hue_white_lamp_couloir_avg_watts_quotidien
sensor.hue_white_lamp_cuisine_avg_watts_annuel
sensor.hue_white_lamp_cuisine_avg_watts_hebdomadaire
sensor.hue_white_lamp_cuisine_avg_watts_mensuel
sensor.hue_white_lamp_cuisine_avg_watts_quotidien
sensor.hue_white_lamp_entree_avg_watts_annuel
sensor.hue_white_lamp_entree_avg_watts_hebdomadaire
sensor.hue_white_lamp_entree_avg_watts_mensuel
sensor.hue_white_lamp_entree_avg_watts_quotidien
sensor.hue_white_lamp_salle_de_bain_avg_watts_annuel
sensor.hue_white_lamp_salle_de_bain_avg_watts_hebdomadaire
sensor.hue_white_lamp_salle_de_bain_avg_watts_mensuel
sensor.hue_white_lamp_salle_de_bain_avg_watts_quotidien
sensor.hue_white_lamp_table_avg_watts_annuel
sensor.hue_white_lamp_table_avg_watts_hebdomadaire
sensor.hue_white_lamp_table_avg_watts_mensuel
sensor.hue_white_lamp_table_avg_watts_quotidien
sensor.lave_linge_avg_watts_annuel
sensor.lave_linge_avg_watts_hebdomadaire
sensor.lave_linge_avg_watts_mensuel
sensor.lave_linge_avg_watts_quotidien
sensor.lave_vaisselle_avg_watts_annuel
sensor.lave_vaisselle_avg_watts_hebdomadaire
sensor.lave_vaisselle_avg_watts_mensuel
sensor.lave_vaisselle_avg_watts_quotidien
sensor.mini_pc_avg_watts_annuel
sensor.mini_pc_avg_watts_hebdomadaire
sensor.mini_pc_avg_watts_mensuel
sensor.mini_pc_avg_watts_quotidien
sensor.pc_bureau_avg_watts_annuel
sensor.pc_bureau_avg_watts_hebdomadaire
sensor.pc_bureau_avg_watts_mensuel
sensor.pc_bureau_avg_watts_quotidien
sensor.pc_gege_avg_watts_annuel
sensor.pc_gege_avg_watts_hebdomadaire
sensor.pc_gege_avg_watts_mensuel
sensor.pc_gege_avg_watts_quotidien
sensor.petit_dej_avg_watts_annuel
sensor.petit_dej_avg_watts_hebdomadaire
sensor.petit_dej_avg_watts_mensuel
sensor.petit_dej_avg_watts_quotidien
sensor.plaques_cuisson_avg_watts_annuel
sensor.plaques_cuisson_avg_watts_hebdomadaire
sensor.plaques_cuisson_avg_watts_mensuel
sensor.plaques_cuisson_avg_watts_quotidien
sensor.tetes_lit_avg_watts_annuel
sensor.tetes_lit_avg_watts_hebdomadaire
sensor.tetes_lit_avg_watts_mensuel
sensor.tetes_lit_avg_watts_quotidien
sensor.tv_chambre_avg_watts_annuel
sensor.tv_chambre_avg_watts_hebdomadaire
sensor.tv_chambre_avg_watts_mensuel
sensor.tv_chambre_avg_watts_quotidien
sensor.tv_salon_avg_watts_annuel
sensor.tv_salon_avg_watts_hebdomadaire
sensor.tv_salon_avg_watts_mensuel
sensor.tv_salon_avg_watts_quotidien
```

### 6.2 Mortes (pas dans le registre HA) - 44

*Definies dans un YAML modulaire, jamais referencees, et ABSENTES du registre HA. Candidates a suppression du YAML ou du registre (entites fantomes).*

```
binary_sensor.est_jour_7h30_21h
binary_sensor.est_nuit_21h_7h30
sensor.all_standby_current
sensor.audit_md5_journal
sensor.audit_md5_md_yaml_journal
sensor.backup_github_journal
sensor.bureau_power_locks
sensor.bureau_power_status_affichage
sensor.chambre_etat
sensor.chambre_nb_allumes
sensor.chambre_power_locks
sensor.chambre_power_status_affichage
sensor.clim_bureau_etat
sensor.clim_chambre_etat
sensor.clim_rad_total_avg_watts_annuel
sensor.clim_rad_total_avg_watts_hebdomadaire
sensor.clim_rad_total_avg_watts_mensuel
sensor.cuisine_power_status_affichage
sensor.delta_3
sensor.delta_ademe_recommande
sensor.diag_max_poste_hebdomadaire_dynamique
sensor.diag_max_poste_mensuel_dynamique
sensor.diag_max_poste_quotidien_dynamique
sensor.diag_total_identifie_hebdomadaire
sensor.diag_total_identifie_mensuel
sensor.diag_total_identifie_quotidien
sensor.git_last_weekly_tag
sensor.github_default_branch
sensor.histo_energie_linky
sensor.histo_energie_nodon
sensor.ip_externe_wan
sensor.lumiere_chambre_etat
sensor.lumiere_couloir_etat
sensor.lumiere_cuisine_etat
sensor.lumiere_entree_etat
sensor.lumiere_salle_de_bain_etat
sensor.lumiere_salon_etat
sensor.lumiere_table_etat
sensor.salon_power_locks
sensor.salon_power_status_affichage
sensor.sdb_power_status_affichage
sensor.sdb_seche_serviette_power_status
sensor.sdb_seche_serviette_power_status_affichage
sensor.sdb_soufflant_power_status
sensor.store_bureau_status
sensor.store_salon_status
switch.voyant_thermostat_soufflant_salle_de_bain
```

### 6.3 Familles (52 prefixes avec >1 membre orpheline)

*Groupes d'entites orphelines partageant un prefixe commun (ex: `eclairage_bureau_5_*` = 4 membres). Utile pour identifier des familles entieres a nettoyer.*

```
eclairage_appart_2_* (4), eclairage_appart_3_* (4), eclairage_bureau_5_* (4),
eclairage_chambre_4_* (4), eclairage_couloir_1_* (4), eclairage_cuisine_1_* (4),
eclairage_entree_1_* (4), eclairage_salon_5_* (4), eclairage_sdb_2_* (4),
hue_ambiance_lamp_salon_1_* (4), hue_ambiance_lamp_salon_2_* (4), hue_ambiance_lamp_salon_3_* (4),
hue_color_candle_chambre_eric_* (4), hue_color_candle_chambre_gege_* (4),
hue_color_candle_salon_1_* (4), hue_play_1_pc_bureau_* (4), hue_play_2_pc_bureau_* (4),
hue_play_3_pc_bureau_* (4), hue_white_lamp_bureau_1_* (4), hue_white_lamp_bureau_2_* (4),
hue_white_lamp_chambre_1_* (4), hue_white_lamp_chambre_2_* (4), hue_white_lamp_couloir_* (4),
hue_white_lamp_cuisine_* (4), hue_white_lamp_entree_* (4), hue_white_lamp_salle_de_bain_* (4),
hue_white_lamp_table_* (4), airfryer_avg_watts_* (2), box_internet_avg_watts_* (2),
chargeurs_salon_avg_watts_* (2), congelateur_avg_watts_* (2), lave_linge_avg_watts_* (4),
lave_vaisselle_avg_watts_* (4), mini_pc_avg_watts_* (4), pc_bureau_avg_watts_* (4),
pc_gege_avg_watts_* (4), petit_dej_avg_watts_* (4), plaques_cuisson_avg_watts_* (4),
tetes_lit_avg_watts_* (4), tv_chambre_avg_watts_* (4), tv_salon_avg_watts_* (4)
```

## STATISTIQUES

- Fichiers YAML modulaires actifs : 58
- Total entites definies (unique_id) : 521 (sensor=516, binary_sensor=3, switch=2)
- Entites referencees (union dashboard + automations + scripts + templates + sensors + utility_meter + groups + command_line + shell_command + input_booleans) : 1121
- Scripts .sh actifs : 8
- Automations (fichiers YAML actifs) : 63 (17 poles)
- Scripts non-sh (scripts.yaml) : 9 scripts
- Entites orphelines (definies, non referencees) : 183 (139 vivantes + 44 mortes)
- Familles orphelines (>1 membre) : 52
- Dashboard actif : Dashboard_2026_10_14.yaml (1.7 Mo)
- Genere le : 2026-10-13 21h51 (Hermes)
