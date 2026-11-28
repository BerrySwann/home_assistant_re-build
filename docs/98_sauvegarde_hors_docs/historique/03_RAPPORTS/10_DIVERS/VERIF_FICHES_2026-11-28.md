# Verification des fiches MD, des MOC et des GLOBAL - 2026-11-28

Lecture seule. Aucun fichier de docs, de prod ou de config n'a ete modifie par cette verification.
Outils : TEMPO\verif_docs_2026-11-28\verif_fiches.py, ghost_ctx.py, verif_moc_global.py (sorties : fiches_verif.txt/json, ghosts_ctx.txt, moc_global.txt).
Sources de reference (etabli) : H:\.storage\core.entity_registry (3310 entites, 211 supprimees), core.restore_state, etat live HA (ha_get_state), fichiers prod de H:\ (269 yaml hors docs/backups/.ha_mcp).

## 1. Prod d'abord : aucune casse trouvee

Les entites fantomes citees par les fiches et les index ont ete recherchees mot entier dans la prod (automations.yaml, scripts.yaml, templates, sensors, utility_meter, dashboards .storage\lovelace*, hors .ha_mcp\backups et docs).

- 37 entites citees par Automations.md et les fiches energie/meteo : 0 usage actif en prod. Les occurrences prod sont des commentaires d'en-tete (P1_DUT_clim_chauffage.yaml l.22-24, M_01, M_03, P0_*, P2_UM_AMHQ_MINI_PC, P1_UM_AMHQ) ou des anciennes sauvegardes .ha_mcp\backups.
- 33 entites citees par GLOBAL_INDEX_REPO et DEPENDANCES_GLOBALES : 0 usage actif, sauf sensor.plug_power dans le dashboard tablette (lovelace.dashboard_tablette l.13334 et 13404). C'est un reglage inactif d'un modele card_mod (use_number = false) : sans effet.
- Les 3 group.hue_devices / ikea_devices / sonoff_devices existent en live (etat unknown), ce ne sont pas des fantomes.

Conclusion : les ecarts sont des retards de documentation, pas des bugs de prod.

## 2. Fiches MD contre leur YAML (297 MD examines)

Compte des constats (lignes) : HAUT 27, MOYEN 147, BAS 203, INFO 160. 162 fiches ont au moins un constat.

HAUT (27) :
- 17 : entites citees inconnues de HA et des YAML (apres triage : surtout des noms renommes ou supprimes, pas des bugs de prod).
- 6 : YAML cite introuvable (docs et prod).
- 4 : YAML cite present en prod seulement (H:\automations.yaml, scripts.yaml, a documenter comme "prod racine").

MOYEN, principaux types : valeurs du YAML absentes de la fiche (41), chemin YAML d'en-tete obsolete (24), chemin cite different du reel (15), entites citees supprimees du registre (13), YAML modifie apres la date de la fiche (nombreux, ecarts de 2 a 185 jours), unique_id du YAML absents de la fiche (6).

Exemples verifies a la main :
- Automations.md : 14 entites inconnues (binary_sensor.bureau_pc_status, sensor.groupe_clim, sensor.conso_multi_nuit_2h_5h, light.hue_smart_salon -> hue_smart_eco_salon, sensor.blitzortung_lightning_counter -> maison_lightning_counter...). YAML modifie le 2026-11-23, fiche du 2026-10-31.
- Page_Home.md : cite sensor.luna_lunar_* absents de HA ; YAML modifie le 2026-11-28, fiche du 2026-10-15.
- L2C1_Page_ENERGIE_GENERALE_principale.md : sensor.genelec_appart_conso_moyenne_1h inconnu ; chemin d'en-tete obsolete ; YAML plus recent de 185 jours.
- 3 fiches citent des fichiers deplaces ou renommes (templates\P1_clim_chauffage\...\P1_01_clim_logique_system_autom.yaml est maintenant dans un dossier du meme nom).

Faux positifs identifies et exclus : phrases "l'ancien nom n'existe plus", notations abregees (clim_salon/bureau/chambre_nous, cout_total/hp/hc_quotidien), bruit Jinja et services (sun.sun, zone.home, timer.finished, text.split, fan.includes, remote.send_command...).

Limite : le comptage "valeurs du YAML absentes" est un indice (heuristique), pas une preuve de fiche fausse.

## 3. MOC

- MOC_AUTOMATIONS (2026-11-08) : l.77 pointe vers J_debug_notifier_..._clim_mobile sans le prefixe XX_ (dossier renomme XX_J_debug_notifier_...). Lien casse (yaml et md).
- MOC_SCRIPTS (2026-11-04) : bloc "Controle des fiches" perime. Il annonce 39 sources SH, 9 YAML, "2 scripts bash, 0 python, 9 YAML, 5 verif bash, 32 verif python". Realite : 8 .sh + 34 .py = 42 sources, 12 yaml (13 fiches YAML_MD). La ligne "Hermes_audit_md5_trigul_unitaire.py" est ecrite avec une casse differente du fichier reel.
- MOC_DASHBOARD (docs) (2026-11-08) : liens corrects une fois decodes (URL-encodes). Regle "1 YAML = 1 fiche" : exceptions reelles = page_L4C3_maj_ha.yaml sans fiche ; card_meteocss_home.yaml dont la fiche s'appelle meteocss_card_modif.md ; 28 snapshots Dashboard_2026_* sans fiche (archives, hors regle).
- MOC_SKILLS (2026-11-08) : conforme (SKILL.md et skill_NOM\NOM.md sont des exemples de modele). Verifier qu'ha-verif-headers et hermes_aligne y figurent (fiches presentes dans docs\05_docs_skills).
- MOC\MOC_DEPENDANCES (2026-10-29) : 3 fichiers cites n'existent ni en local ni en prod (templates\Air_Quality\A_01_AIR_QUALITY.yaml, sensors\Air_Quality\A_01_AIR_QUALITY.yaml, templates\Stores\S_01_STORES.yaml) ; P2_UM_AMHQ_mini_pc.yaml (reel : P2_UM_AMHQ_MINI_PC.yaml, casse).
- MOC\MOC_PRESENCE (2026-10-11) : templates\P4_groupe_presence\02_logique_wifi_cellular.yaml introuvable.
- MOC\MOC_DASHBOARD (2026-10-25) : liens non verifiables par nom (1 seul nom de fichier cite) ; annonce 18 vignettes (coherent avec les index).

## 4. GLOBAL

- GLOBAL_INDEX_REPO (2026-11-23) : 26 noms introuvables, 16 casses differentes. Renommages probables : M_03_meteo_sensors_blitzortung -> M_meteo_sensors_blitzortung.yaml ; M_04_tendances_th_ext_card -> M_04_tendances_th_ext_temperature_card.yaml ; P1_AVG_TOTAL_AMHQ -> P1_AVG_AMHQ_TOTAL.yaml ; P1_BV_01_SW_inter_souflant_sdb -> P1_BV_IB_SW_inter_souflant_SDB.yaml ; 01_UM_AMHQ / 02_UM_genelec_appart_HPHC_AMHQ -> P0_UM_AMHQ.yaml (a confirmer) ; etats_status -> P3_etats_status.yaml ; TODO.md -> TODO\TODO.html. Sans correspondance trouvee : P1_AVG.yaml, S_01_STORES.yaml, A_01_AIR_QUALITY.yaml. Les 15 fiches de skills sont citees avec des noms a tirets (ha-push-docs.md...) alors que les fiches reelles sont skill_ha_push_docs\ha_push_docs.md (underscores). Casses : gen_global_index_*.py, check_global_index.py, audit_md5.sh en minuscules alors que les fichiers sont en majuscules (sans effet sous Windows, cassant sous Linux/GitHub).
- GLOBAL_INDEX_AUTOMATIONS (2026-11-23) : TIMERS_SDB_SOUFFLANT_ET_SECHE_SERVIETTES.md -> reel P1_XX_Timers_SDB_soufflant_et_seche_serviettes.md ; recap_index.py casse differente.
- GLOBAL_INDEX_VIGNETTES_PAGES, GLOBAL_INDEX_SCRIPTS_PY/SH/YAML (2026-11-23 / 11-09) : liens corrects une fois decodes ; seule casse de recap_index.py (reel Recap_index.py).
- IA_GLOBAL_INDEX_memoire (2026-11-23) : 6 casses de noms de scripts .py ; 1 chemin ancien (historique\IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md).
- DEPENDANCES_GLOBALES_CLAUDE_memoire (modifie le 2026-11-28) : 89 noms introuvables et 50 entites inconnues, en grande majorite dans des lignes d'historique (anciens noms de fichiers datees, ex. page_L1C2_temperatures_2026-09-02.yaml) et du bruit Jinja/service. A trier avant toute correction : seule la partie "etat courant" compte. Entites reellement obsoletes citees : sensor.temperature_cible, consigne_de_base, temperature_differentielle (supprimees du registre), sensor.temperature_corrige_eric/mamour, sun_left/top/opacity, moon_*, ete_hiver, store_*_status.
- DEPENDANCES_GLOBALES_HERMES_V1 (2026-11-03, non touche depuis 25 jours) : 8 noms introuvables, 35 entites inconnues (meme profil), chemins P1_01_MASTER anciens.
- ENTITES_GLOBAL_INDEX (2026-11-21) : seule la casse de recap_index.py. Le total "684 entites" et "128 NAT mqtt" (mesure du 2026-11-03) n'ont pas ete recomptes.

## 5. Non verifie

- Lecture cote a cote fiche / YAML des 162 fiches avec constat : le passage automatique couvre toutes les fiches, mais la lecture manuelle complete n'est pas faite (seulement les exemples ci-dessus et le triage des entites). Elle se fait par lots, dans l'ordre de gravite.
- Fiches de 01_docs_config_system qui portent un YAML : traitees par le script (perimetre _MD), pas relues une a une.
- Valeurs en dur (offset_salon/bureau/chambre "0.3" dans P1_01) : pas comparees a HA.
- Chiffres "684 entites", "128 NAT mqtt", "18 vignettes", "39 sources" : seuls 39 et 9 ont ete recomptes (faux).

## 6. Corrections possibles (aucune faite, en attente d'un go)

1. MOC_AUTOMATIONS l.77 (prefixe XX_) et bloc "Controle des fiches" de MOC_SCRIPTS (42 sources, 12 yaml).
2. GLOBAL_INDEX_REPO : noms renommes (liste section 4), noms de fiches de skills, casses.
3. Fiches : chemins d'en-tete obsoletes (24) et entites renommees (17 fiches), apres lecture cote a cote.
4. MOC_DEPENDANCES / MOC_PRESENCE : retirer ou remplacer les 4 fichiers inexistants.

---

## Corrections appliquees le 2026-11-28 (local seulement, rien poussé en prod)

Résultat de la re-vérification après les lots 1 à 4 (297 fiches MD, 159 avec YAML en en-tête) : HAUT 27 -> 19, MOYEN 147 -> 81, BAS 203 -> 151, INFO 160 -> 152. Fiches avec au moins un constat : 147.

62 fiches distinctes corrigées, chacune avec son .bak (format nom.bak_AAAA_MM_JJ_HHhMMmSSs.ext), MD5 avant/après et ligne dans MODIFS_2026-11-28_claude.md.

- Lot 1 (11 fiches) : entités fantômes remplacées par les entités réelles (énergie générale, éclairage, MAJ HA, Home, E_clim_notification, Rattrapage_linky_j2, Git_au_demarrage, COULEURS_PRISES, Carte météo) et note de vérification en tête d'Automations.md.
- Lot 2 (36 fiches) : chemins YAML obsolètes ou différents du réel remplacés par le chemin docs réel (35 en correction automatique, fiches dashboard et fiches automations, plus une édition à la main sur Rattrapage_linky_ecart).
- Lot 3 (16 fiches) : casse des chemins (A_0, B_0, Card_foudre_home, Db_purge), noms renommés le 2026-11-03 (L1C2 page), switch -> light pour la prise PC bureau (2 fiches PRISES), condition pas groupe_1 ajoutée aux fiches J, K, L, et 5 vignettes dont le code intégré est resynchronisé avec le YAML (L1C1, L1C2, L1C3, L6C2, L6C3).
- Lot 4 (2 fiches) : chemins d'exports corrigés (C_watchdog_soufflant_SDB, spécification soufflant SDB).

Laissé tel quel, faux positifs ou historique : configuration.md, integrations_file.md, h_soufflant_SDB_routage, i_soufflant_SDB_bouton_rodret, Bureau_espace_de_loisirs_actif, Economie_energie_vscode, Bouton_inter_ikea_4/somrig, I_synchro_notif_clim_si_prise_coupee, Bureau_forcer_play_on, L4C1_Page_MINI_PC_RASPI, Card_duree_du_jour, L2C1_Vignette_ENERGIE_GENERALE, L3C1_Page_ECLAIRAGE_droite. Pour L3C2_Vignette_PRISES, seul le switch -> light est corrigé, il reste des écarts de formatage.

A décider :

- Automations.md : l'en-tête dit de ne jamais documenter depuis la prod et de prendre GitHub comme source unique, ce qui contredit la règle actuelle (le local fait foi).
- Card_calcule_temp_cible : son YAML cite 3 entités supprimées de HA (consigne_de_base, temperature_cible, temperature_differentielle) et aucun dashboard de la prod ne les cite. Refaire ou retirer la carte.
- L6C3_Vignette_VIGIEAU : l'ancien code de la fiche (break ajoutés, niveaux crise et alerte) n'est pas en prod, il est conservé comme piste de correction.
- P1_XX_D_WATCHDOG_RADIATEUR_SDB : statut Actif, mais aucune automation avec cet alias dans automations.yaml et aucun YAML dans docs. Fiche à archiver ou à relier à un YAML.
- 27 fiches citent encore dans leur texte d'anciens chemins introuvables (templates/P3_eclairage/ui_dashboard/etats_status.yaml, utility_meter/P0_Energie_total/..., TREE_CORRIGE/...). Lot 2b possible.
- Fiches de pages non comparées ligne à ligne (entités seulement) : L1C1_Page_METEO, L1C3_Page_CLIM, L2C2_Page_ENERGIE_CLIM, L6C2_Page_POLLUTION_POLLEN, L6C3_Page_VIGIEAU, TUTO_L1C1, Card_prog_clim_chambre.
- Poussée en prod (ha-push-md vers H:\docs), GLOBAL_INDEX_REPO et IA_GLOBAL_INDEX_memoire : en attente de ton go ; Check_GLOBAL_INDEX signale 2 écarts prod, attendus tant que ces poussées ne sont pas faites (liens: 1038, cassés: 0).
<!-- annotations_log: [2026-11-28] VERIF_FICHES_2026-11-28 : rapport verif fiches: ajout de la section corrections des lots 1 a 4 (local seulement) -->
