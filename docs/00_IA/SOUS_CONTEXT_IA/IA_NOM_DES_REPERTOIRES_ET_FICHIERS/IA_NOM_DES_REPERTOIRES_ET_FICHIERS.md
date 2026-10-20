```text
┌─────────────────────────────────────┐
│ IA_NOM_DES_REPERTOIRES_ET_FICHIERS  │
└─────────────────────────────────────┘
```

# IA_NOM_DES_REPERTOIRES_ET_FICHIERS

Règles de nommage des répertoires et des fichiers du dossier `docs`.
- Statut : brouillon à valider par Eric. Mise à jour du 2026-10-17. Le renommage local du 2026-10-16 est fait. Le 2026-10-17, les règles de mots (accents, SDB, eCO, Z2M, RASPI, GitHub, GLOBAL_INDEX, AQ_, MPC_, UI_DASHBOARD) ont été appliquées en local : 156 renommages, rapport `historique\RENOMMAGE_2026-10-17_rapport.tsv`. Les listes d'écarts des paragraphes 6.3 et 6.6 à 6.14, les comptes de la section 7 et la grille de la section 8 donnent les noms AVANT ce renommage. Restent à faire : la restructuration LxCx, les points ouverts, la prod et le repo.
- Périmètre : `docs` uniquement. Le dossier `docs` lui-même reste en minuscules.
- Ordre de déploiement : local, puis prod (`H:\docs`), puis repo GitHub via le backup HA. Chaque étape attend un go séparé d'Eric.
- Légende : un "écart" est un nom actuel qui ne suit pas la règle. Il est listé avec le nom attendu, mais pas renommé.

## 1. Règle de base
- Pôle : `P` majuscule suivi du numéro. Exemple : `P3_Eclairage`.
- Sans pôle : première lettre en majuscule.
- Premier mot : première lettre en majuscule, tout le reste en minuscules, mots suivants compris.
- Les préfixes numériques (`01_`, `02_`) sont conservés tels quels et ne comptent pas comme premier mot.
- Les fichiers `.bak_...` suivent le nom du fichier qu'ils sauvegardent.
- Le renommage du 2026-10-16 n'a changé que la casse : jamais de lettre, d'accent, d'espace ni d'extension.
- Aucun accent dans les noms (règle du 2026-10-17, paragraphe 6.3).
- Le numéro du dossier racine `0x_` descend devant le nom des dossiers de type de fichiers qu'il contient (règle du 2026-10-17, paragraphe 6.15).

## 2. Exemples
- `p3_salon_bouton_ikea_inter_salon` devient `P3_Salon_bouton_ikea_inter_salon`.
- `dashboard_docs_MD` devient `Dashboard_docs_md`.
- `PAGE_HOME.md` devient `Page_Home.md`.
- `vignette_L1C1_meteo.yaml` devient `Vignette_L1C1_meteo.yaml`.
- Dossier yaml `L1C1_01_Meteo` devient `L1C1_01_METEO` (LxCx_{NOM} en majuscules).
- Dossier `02_Page` de L1C1 devient `02_L1C1_Page`, avec le fichier `Page_L1C1_meteo.yaml` (et la même chose côté md).
- `Tuto_images_alertes_meteo_france.md` devient `TUTO_L1C1_images_alertes_meteo_france.md`.
- `Couleurs_eclairage_par_piece.md` devient `COULEURS_ECLAIRAGE_PAR_PIECE.md`.

## 3. Pôles
Liste donnée par Eric. Dans un nom, le pôle s'écrit `P` suivi du numéro (`P0` à `P4`).
- P0 : énergie globale (Linky, Nodon)
- P1 : chauffage et clim
- P2 : prises connectées
- P3 : éclairage
- P4 : présence (Wi-Fi, mobile)

Préfixes hors-pôle (fichiers sans pôle énergie). Source : CLAUDE.md, section 3 "Répertoires HA & préfixes hors-pôles", sauf `AQ_` et `MPC_` décidés par Eric le 2026-10-17. Format d'un fichier : `{PREFIXE}_{index}_{description}.yaml`.
- `M_` : Météo
- `AQ_` : Air Quality (remplace `A_`, décision du 2026-10-17 ; CLAUDE.md et ses deux copies mis à jour le 2026-10-17)
- `S_` : Stores (repris de CLAUDE.md, non rediscuté)
- `MPC_` : Mini-PC (remplace `MP_`, décision du 2026-10-17 ; CLAUDE.md et ses deux copies mis à jour le 2026-10-17)
- À ne pas confondre avec l'ordre établi : dans les automations (`03_Docs_automations`), les lettres `A_`, `B_`, `C_`, `D_`... placées devant le nom (exemples : `A_chauffage_cuisine`, `C_notif_temp_jour`, `D_notif_temp_nuit`) servent à les mettre dans un ordre défini. Ce ne sont pas des préfixes hors-pôle et elles ne sont pas concernées par `AQ_` (précisé par Eric le 2026-10-17).

## 4. Abréviations
Liste donnée par Eric, avec l'orthographe corrigée. Elles servent aux noms des fichiers YAML modulaires (convention du fichier CLAUDE.md, section RÈGLES YAML - CONVENTIONS). Les sigles restent en majuscules (paragraphe 5).

Répertoires système :
- SNS : répertoires système `sensors/`
- UM : répertoires système `utility_meter/`
- TPL : répertoires système `templates/`

Suffixes et types :
- `_AMHQ` : Annuel, Mensuel, Hebdomadaire, Quotidien
- AVG : moyenne (average)
- TOTAL : totaux
- kWh : unité kilowattheure
- DUT : durée d'utilisation totale
- DIAG : diagnostics
- POWER : puissance
- BV : bouton virtuel
- IB : input boolean
- SW : switch
- MINI_ : minimum d'une unité, le point le plus bas
- MAXI_ : maximum d'une unité, le point le plus haut
- MINI_MAXI_AVG : agglomération de MINI_, MAXI_ et AVG. À l'avenir, MINI_ ou MAXI_ peuvent aussi s'utiliser seuls (précisé par Eric le 2026-10-17).
- UI_DASHBOARD : spécification de fichiers propre à un pôle, qui change un état en signal ou autre chose (formulation d'Eric, 2026-10-17). Écrit `P*_UI_DASHBOARD`, `*` désignant tous les pôles (P0 à P4) (règle au paragraphe 6.9).

Pièces :
- SDB : salle de bain (décidé le 2026-10-17, règle au paragraphe 6.8)

Graphie fixe :
- eCO : s'écrit toujours ainsi (e minuscule, CO majuscules), pour que ce soit visuel (décidé le 2026-10-17, règle au paragraphe 6.10). Sa signification n'est pas donnée.
- Z2M : Zigbee2MQTT, s'écrit toujours ainsi (décidé le 2026-10-17, règle au paragraphe 6.11).
- RASPI : Raspberry Pi, s'écrit toujours ainsi, y compris pour `rpi` (décidé le 2026-10-17, règle au paragraphe 6.12).
- GitHub : s'écrit toujours ainsi, G et H majuscules (décidé le 2026-10-17, règle au paragraphe 6.13).
- GLOBAL_INDEX : s'écrit toujours en majuscules, sauvegardes comprises (décidé le 2026-10-17, règle au paragraphe 6.14).

Niveaux (repris de CLAUDE.md, section P3, ajoutés le 2026-10-17). Ce sont des suffixes de niveau : l'extension du fichier reste `.yaml`.
- UNITE : niveau 1, une lampe individuelle. Exemple `P3_AVG_AMHQ_1_UNITE.yaml`. P1 n'a pas de numéro : `P1_AVG_AMHQ_UNITE.yaml`.
- ZONE : niveau 2, agrégat par pièce. Exemple `P3_AVG_AMHQ_2_ZONE.yaml`.
- TOTAL : niveau 3, appartement entier (voir plus haut). Exemple `P3_POWER_3_TOTAL_ZONE.yaml`.
- UNITE et ZONE s'écrivent en majuscules et sans accent (CLAUDE.md écrit UNITÉ dans un titre ; les noms de fichiers n'ont pas d'accent).
- Règle : tout nom qui se termine par `_UNITE`, `_ZONE` ou `_TOTAL`, avec ou sans numéro de niveau devant (`_1_UNITE`, `_2_ZONE`, `_3_TOTAL`), garde ces suffixes en majuscules et n'est pas renommé à cause d'eux.
- Exemples présents aujourd'hui, état du jour (7 fichiers de `01_docs_config_system\config_system_SH_PY_YAML`, zone dont la casse reste inchangée) :
- `templates\P1_clim_chauffage\P1_AVG\P1_AVG_AMHQ_UNITE.yaml`
- `templates\P3_eclairage\P3_AVG\P3_AVG_AMHQ_1_UNITE.yaml`
- `templates\P3_eclairage\P3_AVG\P3_AVG_AMHQ_2_ZONE.yaml`
- `templates\P3_eclairage\P3_ENERGIE_TPL\P3_TPL_AMHQ_1_UNITE.yaml`
- `templates\P3_eclairage\P3_ENERGIE_TPL\P3_TPL_AMHQ_2_ZONE.yaml`
- `templates\P3_eclairage\P3_POWER_TPL\P3_POWER_3_TOTAL_ZONE.yaml`
- `utility_meter\P3_eclairage\P3_UM_AMHQ_1_UNITE.yaml`

## 5. Noms laissés intacts
- `README`. Les entrées cachées (nom commençant par un point) sont aussi laissées telles quelles : choix de mise en oeuvre, non demandé explicitement par Eric.
- `GLOBAL_INDEX_*` et `DEPENDANCES_GLOBALES` : toujours en majuscules.
- `IA_*` : toujours en majuscules. Les fichiers dont le nom contient "couleur" : tout en majuscules (exemple `COULEURS_PRISES_PAR_PIECE.md`).
- `00_IA` : ne pas renommer (consigne du 2026-10-16). La règle de majuscules de 00_IA est documentée en 6.1.
- `05_docs_MD_system` : reste tel quel.
- `Dashboard_COMPLET` : reste tel quel, contenu compris.
- `L0C0_PAGE_Home` : tout son contenu reste où il est (décision du 2026-10-17).
- Les motifs `GRP_0X` et `LXCX` (exemple `L1C1`) dans un nom.
- Les noms de modules HACS et d'applications, écrits comme le module (paragraphe 6.7).
- Les suffixes de niveau `_UNITE`, `_ZONE` et `_TOTAL`, avec ou sans numéro, toujours en majuscules (paragraphe 4).
- Les sigles `AVG`, `AMHQ` (donc `P1_UM_AMHQ`), `TPL`, `TOTAL`, `DUT`, `BV`, `IB`, `MINI`, `MAXI`, `SDB`, `Z2M`, `RASPI`, `GitHub`, `GLOBAL_INDEX`, `UI_DASHBOARD`.
- Tout `01_docs_config_system` (système, image de `H:\`) reste tel quel pour la casse, sauf les exceptions des paragraphes 6.5 à 6.14.

## 6. Règles par zone

### 6.1 Dossier 00_IA (décidé le 2026-10-17)
- Tous les dossiers et fichiers de `00_IA` sont en majuscules, extension en minuscules (exemple `GLOBAL_INDEX_IA.md`).
- Documentation seulement : `00_IA` reste intact, il n'y a pas de dossier yaml dans `00_IA`.
- Écart relevé :
- `00_IA\IA_CONTEXT_BASE\IA_CONTEXT_BASE_2026-07-19_15h46.md` (attendu : `IA_CONTEXT_BASE_2026-07-19_15H46.md`)

### 6.2 Dossiers LxCx de 02_Docs_dashboard (décidé le 2026-10-17)
- Les sous-dossiers directs de `Dashboard_docs_md` et de `Dashboard_docs_yaml` s'écrivent `LxCx_{NOM}` en majuscules. Les sous-sous-dossiers ne sont pas concernés. Le numéro fait partie du {NOM} (déduit, non confirmé) : `L2C1_04_Energie_Generale` devient `L2C1_04_ENERGIE_GENERALE`.
- Chaque dossier LxCx contient un dossier vignette `01_LxCx_Vignette[_suffixe]` et un ou plusieurs dossiers page `0N_LxCx_Page[_suffixe]` (`02_`, `03_`, `04_`...), avec LxCx remplacé par l'identifiant réel. Exemples : `01_L2C1_Vignette`, `02_L2C1_Page_temps_reel`.
- Les fichiers du dossier vignette s'appellent `Vignette_LxCx[_suffixe]` et ceux du dossier page `Page_LxCx[_suffixe]`, en `.yaml` côté yaml et en `.md` côté md. Exemple d'Eric : `Dashboard_docs_yaml\L1C1_01_Meteo\02_L1C1_Page` avec `Page_L1C1_meteo.yaml`, et la même chose côté md.
- Fichiers à part posés à la racine d'un dossier LxCx : première lettre en majuscule (`Card_*.yaml`). Fichiers dont le nom contient "couleur" : tout en majuscules. Tutos : `TUTO_LxCx[_suffixe].md` (TUTO et LxCx en majuscules, suffixe en minuscules), pour les tutos existants comme pour les futurs.
- `L0C0_PAGE_Home` : tout ce qu'il contient reste où il est (spécifique à cette page), noms compris. Son propre nom reste à trancher (paragraphe 9).

### 6.3 Aucun accent dans les noms (décidé le 2026-10-17)
- Aucun accent dans les noms de dossiers et de fichiers. Un accent est remplacé par la lettre sans accent (é devient e, É devient E) ; la lettre n'est pas supprimée. La règle vise les noms, pas le contenu des fichiers.
- Écarts relevés (le renommage attend un go séparé) :
- `02_Docs_dashboard\Dashboard_docs_md\L0C0_PAGE_Home\03_Carte météo` (attendu : `03_Carte meteo`)
- `02_Docs_dashboard\Dashboard_docs_md\L0C0_PAGE_Home\03_Carte météo\Carte météo vence.md` (attendu : `Carte meteo vence.md`)
- `02_Docs_dashboard\Dashboard_docs_md\L0C0_PAGE_Home\08_Congélateur` (attendu : `08_Congelateur`)
- `02_Docs_dashboard\Dashboard_docs_md\L0C0_PAGE_Home\09_Détecteur de fuite` (attendu : `09_Detecteur de fuite`)
- `02_Docs_dashboard\Dashboard_docs_md\L0C0_PAGE_Home\11_Carte présence` (attendu : `11_Carte presence`)
- `02_Docs_dashboard\Dashboard_docs_yaml\L0C0_PAGE_Home\03_Carte météo` (attendu : `03_Carte meteo`)
- `02_Docs_dashboard\Dashboard_docs_yaml\L0C0_PAGE_Home\08_Congélateur` (attendu : `08_Congelateur`)
- `02_Docs_dashboard\Dashboard_docs_yaml\L0C0_PAGE_Home\09_Détecteur de fuite` (attendu : `09_Detecteur de fuite`)
- `02_Docs_dashboard\Dashboard_docs_yaml\L0C0_PAGE_Home\11_Carte présence` (attendu : `11_Carte presence`)
- `03_Docs_automations\Docs_automations_md\Contrôle entity z2m` (attendu : `Controle entity z2m`)
- `03_Docs_automations\Docs_automations_md\Météo` (attendu : `Meteo`)
- `03_Docs_automations\Docs_automations_md\P2_Alarme_congélateur` (attendu : `P2_Alarme_congelateur`)
- `03_Docs_automations\Docs_automations_md\P2_Éco. prises` (attendu : `P2_eCO. prises`, avec la règle eCO du paragraphe 6.10)
- `03_Docs_automations\Docs_automations_yaml\Contrôle entity z2m` (attendu : `Controle entity z2m`)
- `03_Docs_automations\Docs_automations_yaml\Météo` (attendu : `Meteo`)
- `03_Docs_automations\Docs_automations_yaml\P2_Alarme_congélateur` (attendu : `P2_Alarme_congelateur`)
- `03_Docs_automations\Docs_automations_yaml\P2_Éco. prises` (attendu : `P2_eCO. prises`, avec la règle eCO du paragraphe 6.10)

### 6.4 Dashboard_docs_specifique (décidé le 2026-10-17, pas encore créé)
- Un dossier `Dashboard_docs_specifique` dans `Dashboard_docs_md` et un dans `Dashboard_docs_yaml`.
- Il reçoit les fichiers spécifiques posés aujourd'hui à la racine d'un dossier LxCx : les tutos et les fichiers couleur.
- Mêmes fichiers des deux côtés. Toute modification d'un côté est reproduite de l'autre.
- Fichiers concernés aujourd'hui : `Tuto_images_alertes_meteo_france.md` (L1C1), `COULEURS_PRISES_PAR_PIECE.md` et sa sauvegarde `.bak_2026_09_20.md` (L2C1), `Couleurs_eclairage_par_piece.md` (L2C3).
- Organisation à plat, sans sous-dossier par LxCx (déduit de la demande de mettre le LxCx à l'intérieur des fichiers couleur, non confirmé). Les fichiers couleur portent la mention de leur LxCx (L2C1, L2C3) dans leur contenu : modification à faire sur go.
- Création du dossier et déplacements : sur go séparé, après contrôle des liens.

### 6.5 Cas particuliers décidés le 2026-10-16
- `PAGE_HOME` devient `Page_Home` (dossier et fichier `.md`).
- Un nom qui commence par `vignette_`, `page_` ou `PAGE_` prend `Vignette_` ou `Page_` (première lettre seulement). Ce cas est repris par les règles du paragraphe 6.2.
- Dans `01_docs_config_system\config_system_SH_PY_YAML\command_line`, les sous-dossiers prennent une majuscule en première lettre : `Audit`, `Energie`, `Github_maintenance`, `Ip_externe`, `Meteo`. Exception décidé le 2026-10-17 : `Github_maintenance` s'écrit `GitHub_maintenance` (règle GitHub, paragraphe 6.13).
- Sous `00_IA`, plus aucun renommage automatique.

### 6.6 Air_Quality, préfixes AQ_ et MPC_ (décidé le 2026-10-17)
- Le préfixe des fichiers Air Quality devient `AQ_` (au lieu de `A_`) : `A_01_air_quality.yaml` devient `AQ_01_air_quality.yaml`.
- Le dossier `Air_quality/` s'écrit `Air_Quality/` : exception à la règle du premier mot (paragraphe 1), chaque mot garde sa majuscule, comme les lettres de `AQ`. Je l'applique à ce seul nom ; elle ne devient pas une règle générale (déduit de la demande, à confirmer).
- Concerne, dans `01_docs_config_system\config_system_SH_PY_YAML` (image de `H:\`) : `sensors\Air_quality` et `templates\Air_quality`, avec leur fichier `A_01_air_quality.yaml` dans chacun. Écarts relevés : 4 entrées.
- Le préfixe Mini-PC devient `MPC_` (au lieu de `MP_`) : `MP_01_monitor_temp.sh` devient `MPC_01_monitor_temp.sh`.
- Écarts relevés pour `MPC_` : 2 entrées dans `04_Docs_scripts\Docs_scripts_sh`, le dossier `Mp_01_monitor_temp.sh - save pour raspi` (attendu : `MPC_01_monitor_temp.sh - save pour raspi`) et son fichier `#Mp_01_monitor_temp.sh.#` (attendu : `#MPC_01_monitor_temp.sh.#`). Établi : les noms actuels commencent par `Mp_`. Déduit : l'original était `MP_` (le fichier de la prod s'appelle `#MP_01_monitor_temp.sh.#`, vu dans l'arbre de `H:\.scripts`), passé en `Mp_` par la règle du premier mot.
- Renommage : sur go séparé (local, puis prod, puis repo). Avant la prod, vérifier que ni `configuration.yaml` (includes) ni une carte ne dépendent de ces chemins : non vérifié à ce jour.
- CLAUDE.md (section 3 et exemple de la convention YAML) et ses deux copies identiques, `IA_CONTEXT_BASE.md` en local et `D:\docs\00_IA\IA_CONTEXT_BASE.md`, ont été mis à jour le 2026-10-17 : `AQ_` et `MPC_`, et `{PREFIXE}` à la place de `{LETTRE}`. La copie de la prod (`H:\docs\00_IA`) n'est pas poussée : go séparé. La section 9 de CLAUDE.md a été complétée le même jour (UI_DASHBOARD, MINI_/MAXI_, SDB, eCO, noms de modules, accents).

### 6.7 Noms de modules HACS et d'applications (décidé le 2026-10-17)
- Quand un nom contient le nom d'un module HACS ou d'une application, il s'écrit comme ce module ou cette application, majuscules comprises. Cette règle passe avant la règle du premier mot (paragraphe 1). Exemple d'Eric : `P0_MyElectricalData`, fichier `01_docs_config_system\config_system_SH_PY_YAML\templates\P0_energie_total_diag\P0_Linky\P0_MyElectricalData.yaml`, déjà conforme.
- Orthographe exacte : seule celle de `MyElectricalData` est donnée. Pour les autres modules, l'orthographe est à fournir par Eric ; aucune n'est déduite.
- `MyElectricalData` est une application (pas un module HACS), déportée dans une VM (précisé par Eric le 2026-10-17). Constat du même jour : elle ne figure pas dans la liste HACS lue dans Home Assistant (56 modules installés).
- Noms de `docs` qui contiennent un module HACS installé, orthographe à confirmer : Blitzortung (`M_meteo_sensors_blitzortung.yaml` et `M_03_meteo_UM_blitzortung.yaml`, écrits en minuscules ; module "Blitzortung.org Lightning Detector"), Vigieau (dossier `L6C3_VIGIEAU` côté md, `L6C3_18_VigiEau` côté yaml, fichiers en `vigieau`), MeteoCSS (`Meteocss_card_modif.md`, dans `L0C0_PAGE_Home` : reste en place).
- Aucun écart n'est compté pour cette règle tant que les orthographes ne sont pas confirmées.

### 6.8 SDB, abréviation de salle de bain (décidé le 2026-10-17)
- SDB est l'abréviation de Salle De Bain. Elle s'écrit SDB, en majuscules, dans les noms de dossiers et de fichiers.
- Lecture retenue (précisée par Eric le 2026-10-17) : toute variante d'écriture de l'abréviation (`sdb`, `Sdb`, `sdB`, `sDb`...) devient `SDB`. Les noms écrits en toutes lettres (`salle_de_bain`, `salle de bain`) ne sont pas touchés. Exemple : `A_soufflant_sdb_bouton_rodret` devient `A_soufflant_SDB_bouton_rodret` ; `P1_03_Chauffage salle de bain` reste tel quel.
- Écarts relevés (51 entrées, noms actuels ; le renommage attend un go séparé) :
- `01_docs_config_system\config_system_SH_PY_YAML\input_booleans\P1\P1_BV_IB_inter_soufflant_sdb.yaml` (attendu : `P1_BV_IB_inter_soufflant_SDB.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\templates\Inter_BP_Virtuel\P1\P1_BV_IB_SW_inter_souflant_sdb.yaml` (attendu : `P1_BV_IB_SW_inter_souflant_SDB.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\timers\P1_timers\P1_Timer_10mn\P1_timer_10mn_seche_serviettes_sdb.yaml` (attendu : `P1_timer_10mn_seche_serviettes_SDB.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\timers\P1_timers\P1_Timer_10mn\P1_timer_10mn_soufflant_sdb.yaml` (attendu : `P1_timer_10mn_soufflant_SDB.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\timers\P1_timers\P1_Timer_2h\P1_timer_2h_seche_serviettes_sdb.yaml` (attendu : `P1_timer_2h_seche_serviettes_SDB.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\timers\P1_timers\P1_Timer_60mn\P1_timer_60mn_soufflant_sdb.yaml` (attendu : `P1_timer_60mn_soufflant_SDB.yaml`)
- `02_Docs_dashboard\Dashboard_docs_yaml\L1C3_03_Commandes_Clim\Card_prog_soufflant_sdb.yaml` (attendu : `Card_prog_soufflant_SDB.yaml`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\A_soufflant_sdb_bouton_rodret` (attendu : `A_soufflant_SDB_bouton_rodret`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\A_soufflant_sdb_bouton_rodret\A_soufflant_sdb_bouton_rodret.md` (attendu : `A_soufflant_SDB_bouton_rodret.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\B_soufflant_sdb_routage` (attendu : `B_soufflant_SDB_routage`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\B_soufflant_sdb_routage\B_soufflant_sdb_routage.md` (attendu : `B_soufflant_SDB_routage.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\C_watchdog_soufflant_sdb` (attendu : `C_watchdog_soufflant_SDB`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\C_watchdog_soufflant_sdb\C_watchdog_soufflant_sdb.md` (attendu : `C_watchdog_soufflant_SDB.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\D_sdb_soufflant_decompte_60min` (attendu : `D_SDB_soufflant_decompte_60min`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\D_sdb_soufflant_decompte_60min\D_sdb_soufflant_decompte_60min.md` (attendu : `D_SDB_soufflant_decompte_60min.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\E_sdb_soufflant_rattrapage_demarrage_ha` (attendu : `E_SDB_soufflant_rattrapage_demarrage_ha`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\E_sdb_soufflant_rattrapage_demarrage_ha\E_sdb_soufflant_rattrapage_demarrage_ha.md` (attendu : `E_SDB_soufflant_rattrapage_demarrage_ha.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\G_sdb_seche_serviettes_decompte_2h` (attendu : `G_SDB_seche_serviettes_decompte_2h`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\G_sdb_seche_serviettes_decompte_2h\G_sdb_seche_serviettes_decompte_2h.md` (attendu : `G_SDB_seche_serviettes_decompte_2h.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\H_sdb_seche_serviettes_rattrapage_demarrage_ha` (attendu : `H_SDB_seche_serviettes_rattrapage_demarrage_ha`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\H_sdb_seche_serviettes_rattrapage_demarrage_ha\H_sdb_seche_serviettes_rattrapage_demarrage_ha.md` (attendu : `H_SDB_seche_serviettes_rattrapage_demarrage_ha.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Rodret_soufflant_sdb` (attendu : `Rodret_soufflant_SDB`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Sdb_soufflant_specification_2026` (attendu : `SDB_soufflant_specification_2026`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Sdb_soufflant_specification_2026\Sdb_soufflant_specification_2026.md` (attendu : `SDB_soufflant_specification_2026.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Timers_sdb_soufflant_et_seche_serviettes` (attendu : `Timers_SDB_soufflant_et_seche_serviettes`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Timers_sdb_soufflant_et_seche_serviettes\Timers_sdb_soufflant_et_seche_serviettes.md` (attendu : `Timers_SDB_soufflant_et_seche_serviettes.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Z_soufflant_sdb_gestion_intelligente` (attendu : `Z_soufflant_SDB_gestion_intelligente`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Z_soufflant_sdb_gestion_intelligente\Z_soufflant_sdb_gestion_intelligente.md` (attendu : `Z_soufflant_SDB_gestion_intelligente.md`)
- `03_Docs_automations\Docs_automations_md\P1_03_Chauffage salle de bain\Z_soufflant_sdb_old_2024-2025` (attendu : `Z_soufflant_SDB_old_2024-2025`)
- `03_Docs_automations\Docs_automations_md\P3_Eclairage\Sdb_sync_miroir_lampe_et_relais_sdb` (attendu : `SDB_sync_miroir_lampe_et_relais_SDB`)
- `03_Docs_automations\Docs_automations_md\P3_Eclairage\Sdb_sync_miroir_lampe_et_relais_sdb\Sdb_sync_miroir_lampe_et_relais_sdb.md` (attendu : `SDB_sync_miroir_lampe_et_relais_SDB.md`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\A_soufflant_sdb_bouton_rodret` (attendu : `A_soufflant_SDB_bouton_rodret`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\A_soufflant_sdb_bouton_rodret\A_soufflant_sdb_bouton_rodret.yaml` (attendu : `A_soufflant_SDB_bouton_rodret.yaml`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\B_soufflant_sdb_routage` (attendu : `B_soufflant_SDB_routage`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\B_soufflant_sdb_routage\B_soufflant_sdb_routage.yaml` (attendu : `B_soufflant_SDB_routage.yaml`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\D_sdb_soufflant_decompte_60min_timer` (attendu : `D_SDB_soufflant_decompte_60min_timer`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\D_sdb_soufflant_decompte_60min_timer\D_sdb_soufflant_decompte_60min_timer.yaml` (attendu : `D_SDB_soufflant_decompte_60min_timer.yaml`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\E_sdb_soufflant_rattrapage_demarrage_ha_timer` (attendu : `E_SDB_soufflant_rattrapage_demarrage_ha_timer`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\E_sdb_soufflant_rattrapage_demarrage_ha_timer\E_sdb_soufflant_rattrapage_demarrage_ha_timer.yaml` (attendu : `E_SDB_soufflant_rattrapage_demarrage_ha_timer.yaml`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\G_sdb_seche_serviettes_decompte_2h_timer` (attendu : `G_SDB_seche_serviettes_decompte_2h_timer`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\G_sdb_seche_serviettes_decompte_2h_timer\G_sdb_seche_serviettes_decompte_2h_timer.yaml` (attendu : `G_SDB_seche_serviettes_decompte_2h_timer.yaml`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer` (attendu : `H_SDB_seche_serviettes_rattrapage_demarrage_ha_timer`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer\H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer.yaml` (attendu : `H_SDB_seche_serviettes_rattrapage_demarrage_ha_timer.yaml`)
- `03_Docs_automations\Docs_automations_yaml\P1_03_Chauffage salle de bain\Rodret_soufflant_sdb` (attendu : `Rodret_soufflant_SDB`)
- `03_Docs_automations\Docs_automations_yaml\P3_Eclairage\P3_Sdb_sync_miroir_lampe_et_relais_sdb` (attendu : `P3_SDB_sync_miroir_lampe_et_relais_SDB`)
- `03_Docs_automations\Docs_automations_yaml\P3_Eclairage\P3_Sdb_sync_miroir_lampe_et_relais_sdb\P3_Sdb_sync_miroir_lampe_et_relais_sdb.yaml` (attendu : `P3_SDB_sync_miroir_lampe_et_relais_SDB.yaml`)
- `04_Docs_scripts\Docs_scripts_yaml\Soufflant sdb` (attendu : `Soufflant SDB`)
- `04_Docs_scripts\Docs_scripts_yaml\Soufflant sdb\Sdb_soufflant_arreter` (attendu : `SDB_soufflant_arreter`)
- `04_Docs_scripts\Docs_scripts_yaml\Soufflant sdb\Sdb_soufflant_arreter\Sdb_soufflant_arreter.yaml` (attendu : `SDB_soufflant_arreter.yaml`)
- `04_Docs_scripts\Docs_scripts_yaml\Soufflant sdb\Sdb_soufflant_demarrer` (attendu : `SDB_soufflant_demarrer`)
- `04_Docs_scripts\Docs_scripts_yaml\Soufflant sdb\Sdb_soufflant_demarrer\Sdb_soufflant_demarrer.yaml` (attendu : `SDB_soufflant_demarrer.yaml`)
- Avant tout renommage, non vérifié à ce jour : les fichiers de `01_docs_config_system` sont l'image de `H:\` et peuvent être cités par un `include` ; les dossiers d'automations sont croisés avec `H:\automations.yaml` par le générateur de `GLOBAL_INDEX_AUTOMATIONS` ; les chemins sont cités dans des index, des fiches et des skills.

### 6.9 UI_DASHBOARD (décidé le 2026-10-17)
- `UI_DASHBOARD` est une spécification de fichiers qui change un état en signal ou autre chose (formulation d'Eric). Elle est propre à un pôle et s'écrit `P*_UI_DASHBOARD`, `*` désignant tous les pôles (P0 à P4) (`P1_UI_DASHBOARD`, `P3_UI_DASHBOARD`).
- Elle passe en majuscules comme un sigle (paragraphe 5) : `P1_ui_dashboard` devient `P1_UI_DASHBOARD`.
- Orthographe : Eric a écrit `Px_UI_DASBOARD` ; je lis `DASHBOARD`, comme dans le nom actuel `ui_dashboard`. À confirmer.
- Écarts relevés (3 entrées, noms actuels ; le renommage attend un go séparé) :
- `01_docs_config_system\config_system_SH_PY_YAML\templates\P1_clim_chauffage\P1_ui_dashboard` (attendu : `P1_UI_DASHBOARD`)
- `01_docs_config_system\config_system_SH_PY_YAML\templates\P1_clim_chauffage\P1_ui_dashboard\P1_ui_dashboard.yaml` (attendu : `P1_UI_DASHBOARD.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\templates\P3_eclairage\P3_ui_dashboard` (attendu : `P3_UI_DASHBOARD`)
- Le fichier `P3_etats_status.yaml` du dossier `P3_ui_dashboard` n'est pas concerné (son nom ne contient pas `ui_dashboard`).
- Avant tout renommage, non vérifié à ce jour : ces fichiers sont dans l'image de `H:\` et peuvent être cités par un `include`. CLAUDE.md et ses copies ont été alignés le 2026-10-17 (section 9, nommage des fichiers YAML).

### 6.10 eCO, graphie fixe (décidé le 2026-10-17)
- `eCO` s'écrit toujours `eCO` (e minuscule, CO majuscules) dans les noms de dossiers et de fichiers, pour que ce soit visuel. Exemple d'Eric : `P2_eCO_prises`, déjà conforme.
- Lecture retenue, déduite de l'exemple et à confirmer : toute variante du mot isolé (`eco`, `Eco`, `ECO`, `éco`, `Éco`) devient `eCO`. Les mots qui contiennent seulement ces lettres (`economie`, `ecoute`) ne sont pas touchés.
- Conflit avec la règle de base : un nom sans pôle qui commence par `eCO` commence par une minuscule (exemple : `eCO_prises_dynamique`), alors que le paragraphe 1 demande une majuscule en première lettre. Je propose que `eCO` l'emporte (déduit, à confirmer).
- Écarts relevés (7 entrées, noms actuels ; le renommage attend un go séparé) :
- `01_docs_config_system\config_system_SH_PY_YAML\templates\P2_prise\P2_eCO_prises\P2_eco_prises_config.yaml` (attendu : `P2_eCO_prises_config.yaml`)
- `03_Docs_automations\Docs_automations_md\P2_Éco. prises` (attendu : `P2_eCO. prises`)
- `03_Docs_automations\Docs_automations_md\P2_Éco. prises\Eco_prises_dynamique` (attendu : `eCO_prises_dynamique`)
- `03_Docs_automations\Docs_automations_md\P2_Éco. prises\Eco_prises_dynamique\Eco_prises_dynamique.md` (attendu : `eCO_prises_dynamique.md`)
- `03_Docs_automations\Docs_automations_yaml\P2_Éco. prises` (attendu : `P2_eCO. prises`)
- `03_Docs_automations\Docs_automations_yaml\P2_Éco. prises\Eco_prises_dynamique_by_presence_groupe` (attendu : `eCO_prises_dynamique_by_presence_groupe`)
- `03_Docs_automations\Docs_automations_yaml\P2_Éco. prises\Eco_prises_dynamique_by_presence_groupe\Eco_prises_dynamique_by_presence_groupe.yaml` (attendu : `eCO_prises_dynamique_by_presence_groupe.yaml`)
- Avant tout renommage, non vérifié à ce jour : les dossiers d'automations sont croisés avec `H:\automations.yaml` par le générateur de `GLOBAL_INDEX_AUTOMATIONS` ; le fichier de `01_docs_config_system` est dans l'image de `H:\` et peut être cité par un `include` ; les chemins sont cités dans des index, des fiches et des skills.

### 6.11 Z2M, abréviation de Zigbee2MQTT (décidé le 2026-10-17)
- `Z2M` est l'abréviation de Zigbee2MQTT. Elle s'écrit `Z2M`, en majuscules, dans les noms de dossiers et de fichiers de `docs`.
- Lecture retenue, à confirmer : Eric a écrit "de partout" ; je limite la règle aux noms de dossiers et de fichiers de `docs`, comme pour SDB et eCO. Toute variante d'écriture de l'abréviation (`z2m`, `Z2m`, `z2M`) devient `Z2M`. Le nom écrit en toutes lettres (`zigbee2mqtt`) n'est pas touché. Les identifiants d'entités Home Assistant restent en minuscules (obligation de Home Assistant, non vérifiée ici).
- Écarts relevés (7 entrées, noms actuels ; le renommage attend un go séparé ; les 2 sauvegardes `.bak_...` suivent leur fichier ; l'accent de `Contrôle` reléve du paragraphe 6.3) :
- `02_Docs_dashboard\Dashboard_docs_yaml\L4C2_11_Proxmox\Card_services_ha_z2m_mariadb.yaml` (attendu : `Card_services_ha_Z2M_mariadb.yaml`)
- `03_Docs_automations\Docs_automations_md\Contrôle entity z2m` (attendu : `Contrôle entity Z2M`)
- `03_Docs_automations\Docs_automations_md\Contrôle entity z2m\Z2m_last_seen` (attendu : `Z2M_last_seen`)
- `03_Docs_automations\Docs_automations_md\Contrôle entity z2m\Z2m_last_seen\Z2m_last_seen.md` (attendu : `Z2M_last_seen.md`)
- `03_Docs_automations\Docs_automations_yaml\Contrôle entity z2m` (attendu : `Contrôle entity Z2M`)
- `03_Docs_automations\Docs_automations_yaml\Contrôle entity z2m\Z2m_last_seen` (attendu : `Z2M_last_seen`)
- `03_Docs_automations\Docs_automations_yaml\Contrôle entity z2m\Z2m_last_seen\Z2m_last_seen.yaml` (attendu : `Z2M_last_seen.yaml`)
- Avant tout renommage, non vérifié à ce jour : les dossiers d'automations sont croisés avec `H:\automations.yaml` par le générateur de `GLOBAL_INDEX_AUTOMATIONS`, et `Card_services_ha_z2m_mariadb.yaml` est cité dans CLAUDE.md.

### 6.12 RASPI, abréviation de Raspberry Pi (décidé le 2026-10-17)
- `RASPI` est l'abréviation de Raspberry Pi. Elle s'écrit `RASPI`, en majuscules, dans les noms de dossiers et de fichiers de `docs`. Eric a demandé `RASPI` à la place de `rpi` : les deux écritures deviennent `RASPI`.
- Lecture retenue, à confirmer : toute variante de `raspi` (`Raspi`, `RasPi`) et de `rpi` (`Rpi`, `RPI`), prise comme mot isolé entre séparateurs, devient `RASPI`. Le nom écrit en toutes lettres (`raspberry`) et les mots qui contiennent seulement ces lettres (`scorpion`) ne sont pas touchés. Déjà conformes : `03_Page_RASPI` et `Page_RASPI`. Eric a précisé le 2026-10-17 que `Rpi4` devient aussi `RASPI` : le numéro de modèle disparaît.
- Écarts relevés (9 entrées, noms actuels ; le renommage attend un go séparé ; la sauvegarde `Page_raspi.bak_...` suit son fichier) :
- `02_Docs_dashboard\Dashboard_docs_md\L4C1_MINI_PC\03_Page_RASPI\Page_raspi.md` (attendu : `Page_RASPI.md`)
- `02_Docs_dashboard\Dashboard_docs_yaml\Page_RASPI\02_Page\Page_raspi.yaml` (attendu : `Page_RASPI.yaml`)
- `03_Docs_automations\Docs_automations_md\Raspi` (attendu : `RASPI`)
- `03_Docs_automations\Docs_automations_yaml\Raspi` (attendu : `RASPI`)
- `03_Docs_automations\Docs_automations_yaml\Raspi\A_rpi_fan_pwm_6_states` (attendu : `A_RASPI_fan_pwm_6_states`)
- `03_Docs_automations\Docs_automations_yaml\Raspi\A_rpi_fan_pwm_6_states\A_rpi_fan_pwm_6_states.yaml` (attendu : `A_RASPI_fan_pwm_6_states.yaml`)
- `04_Docs_scripts\Docs_scripts_sh\Mp_01_monitor_temp.sh - save pour raspi` (attendu : `Mp_01_monitor_temp.sh - save pour RASPI` ; le préfixe `Mp_` reléve du paragraphe 6.6)
- `03_Docs_automations\Docs_automations_md\Raspi\Rpi4_fan_pwm` (attendu : `RASPI_fan_pwm`, le 4 disparaît)
- `03_Docs_automations\Docs_automations_md\Raspi\Rpi4_fan_pwm\Rpi4_fan_pwm.md` (attendu : `RASPI_fan_pwm.md`)
- Avant tout renommage, non vérifié à ce jour : le dossier `A_rpi_fan_pwm_6_states` est croisé avec `H:\automations.yaml` par le générateur de `GLOBAL_INDEX_AUTOMATIONS`.

### 6.13 GitHub, graphie fixe (décidé le 2026-10-17)
- `GitHub` s'écrit toujours `GitHub` (G et H majuscules) dans les noms de dossiers et de fichiers de `docs`.
- Lecture retenue, à confirmer : toute autre écriture du mot isolé (`github`, `Github`, `GITHUB`) devient `GitHub`. Eric a tranché le 2026-10-17 que cette règle l'emporte sur la règle de la première lettre en majuscule du paragraphe 6.5 : `Github_maintenance` devient `GitHub_maintenance`. Le dossier `Github` à la racine du projet (hors `docs`) n'est pas concerné.
- Écarts relevés (10 entrées, noms actuels ; le renommage attend un go séparé) :
- `01_docs_config_system\config_system_SH_PY_YAML\command_line\Github_maintenance` (attendu : `GitHub_maintenance`)
- `01_docs_config_system\config_system_SH_PY_YAML\command_line\Github_maintenance\github_maintenance.yaml` (attendu : `GitHub_maintenance.yaml`)
- `01_docs_config_system\config_system_SH_PY_YAML\shell_command\GITHUB` (attendu : `GitHub`)
- `01_docs_config_system\config_system_SH_PY_YAML\shell_command\GITHUB\GITHUB_backup_github.yaml` (attendu : `GitHub_backup_GitHub.yaml`)
- `03_Docs_automations\Docs_automations_md\Backup ha - github` (attendu : `Backup ha - GitHub`)
- `03_Docs_automations\Docs_automations_md\_Sans_categorie\Veille_github_releases` (attendu : `Veille_GitHub_releases`)
- `03_Docs_automations\Docs_automations_md\_Sans_categorie\Veille_github_releases\Veille_github_releases.md` (attendu : `Veille_GitHub_releases.md`)
- `03_Docs_automations\Docs_automations_yaml\Backup ha - github` (attendu : `Backup ha - GitHub`)
- `03_Docs_automations\Docs_automations_yaml\_Sans_categorie\Veille_github_nouvelle_release_detectee` (attendu : `Veille_GitHub_nouvelle_release_detectee`)
- `03_Docs_automations\Docs_automations_yaml\_Sans_categorie\Veille_github_nouvelle_release_detectee\Veille_github_nouvelle_release_detectee.yaml` (attendu : `Veille_GitHub_nouvelle_release_detectee.yaml`)
- Avant tout renommage, non vérifié à ce jour : les 4 noms de `01_docs_config_system` sont dans l'image de `H:\` et peuvent être cités par un `include` ou un `shell_command` ; les dossiers d'automations sont croisés avec `H:\automations.yaml`.

### 6.14 GLOBAL_INDEX, graphie fixe (décidé le 2026-10-17)
- `GLOBAL_INDEX` s'écrit toujours en majuscules dans les noms de dossiers et de fichiers de `docs`, y compris dans leurs sauvegardes `.bak_...`.
- Lecture retenue, à confirmer : seul le mot `GLOBAL_INDEX` est mis en majuscules (`Gen_global_index_ia.py` devient `Gen_GLOBAL_INDEX_ia.py`). Le reste du nom ne change pas, extension et suffixe `.bak` compris. Les noms qui l'ont déjà en majuscules (`GLOBAL_INDEX_REPO.md`, `ENTITES_GLOBAL_INDEX.md`) ne bougent pas.
- Appliqué en local le 2026-10-17 (10 entrées, noms avant ; la sauvegarde `Check_global_index.py.bak_2026_10_14` a suivi son fichier) :
- `04_Docs_scripts\Docs_scripts_sh\Check_global_index` (attendu : `Check_GLOBAL_INDEX`)
- `04_Docs_scripts\Docs_scripts_sh\Check_global_index\Check_global_index.py` (attendu : `Check_GLOBAL_INDEX.py`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_automations` (attendu : `Gen_GLOBAL_INDEX_automations`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_automations\Gen_global_index_automations.py` (attendu : `Gen_GLOBAL_INDEX_automations.py`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_ia` (attendu : `Gen_GLOBAL_INDEX_ia`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_ia\Gen_global_index_ia.py` (attendu : `Gen_GLOBAL_INDEX_ia.py`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_scripts` (attendu : `Gen_GLOBAL_INDEX_scripts`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_scripts\Gen_global_index_scripts.py` (attendu : `Gen_GLOBAL_INDEX_scripts.py`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_vignettes_pages` (attendu : `Gen_GLOBAL_INDEX_vignettes_pages`)
- `04_Docs_scripts\Docs_scripts_sh\Gen_global_index_vignettes_pages\Gen_global_index_vignettes_pages.py` (attendu : `Gen_GLOBAL_INDEX_vignettes_pages.py`)
- Sous Windows la casse est ignorée : les skills qui citent `gen_global_index_*` en minuscules trouvent encore les scripts. Sur `H:` et GitHub la casse compte : à refaire en prod puis dans le repo. Le script `Check_GLOBAL_INDEX.py` n'a pas été relancé après le renommage.
### 6.15 Dossiers de type de fichiers : le numéro du dossier racine descend (décidé le 2026-10-17)
- Un dossier de type de fichiers (md, yaml, sh...), enfant direct d'un dossier racine `0x_` de `docs`, reprend le numéro de ce dossier racine devant son nom : `03_Docs_automations_md` plutôt que `Docs_automations_md`, `03_Docs_automations_yaml` plutôt que `Docs_automations_yaml` (exemples d'Eric).
- Logique déjà utilisée pour les dossiers LxCx : le code du dossier au-dessus descend dans le nom de l'enfant (`02_L1C1_Page` et `Page_L1C1_meteo`).
- Lecture retenue, à confirmer : "tous les pôles" = les dossiers de type de fichiers de `01_` à `04_`. Non concernés : `00_IA` (6.1), les dossiers nommés d'après un document (`05_docs_MD_system\DEPENDANCES_GLOBALES`...) ou un skill (`05_Docs_skills\Skill_histo`...), et `06_Docs_technique\01_Pont_hue_hacking` (déjà numéroté).
- Le reste du nom ne change pas, hors majuscule au premier mot (règle de base, paragraphe 1) : `Docs_scripts_sh` devient `04_Docs_scripts_sh`. Les enfants de ces dossiers ne changent pas.
- Exception d'Eric (2026-10-18) : dans `01_docs_config_system`, `config_system_MD` et `config_system_SH_PY_YAML` gardent le nom qu'il a créé, sans numéro. Ils sortent de la liste ci-dessous. `config_system_SH_PY_YAML` remplace `config_system_SH_PY_YAML` (nouvelle organisation : `.scripts\01_scripts.sh`, `.scripts\02_scripts.py`, `sql.yaml`, `notifs`, sans `blueprints`). Les arbres plus bas dans ce document (tableau des chemins) ne sont pas régénérés : ils décrivent encore l'ancienne organisation.
- Écarts relevés en local (9 dossiers, aucun renommé) :
- `02_Docs_dashboard\Dashboard_docs_md` (attendu : `02_Docs_dashboard\02_Dashboard_docs_md`)
- `02_Docs_dashboard\Dashboard_docs_yaml` (attendu : `02_Docs_dashboard\02_Dashboard_docs_yaml`)
- `03_Docs_automations\Docs_automations_md` (attendu : `03_Docs_automations\03_Docs_automations_md`)
- `03_Docs_automations\Docs_automations_yaml` (attendu : `03_Docs_automations\03_Docs_automations_yaml`)
- `04_Docs_scripts\Docs_script_original` (attendu : `04_Docs_scripts\04_Docs_script_original`)
- `04_Docs_scripts\Docs_scripts_sh` (attendu : `04_Docs_scripts\04_Docs_scripts_sh`)
- `04_Docs_scripts\Docs_scripts_sh_md` (attendu : `04_Docs_scripts\04_Docs_scripts_sh_md`)
- `04_Docs_scripts\Docs_scripts_yaml` (attendu : `04_Docs_scripts\04_Docs_scripts_yaml`)
- `04_Docs_scripts\Docs_scripts_yaml_md` (attendu : `04_Docs_scripts\04_Docs_scripts_yaml_md`)
- La prod (`H:\docs`) porte les mémes noms (mémes écarts). Tous les chemins cités vers ces dossiers (fiches, index, skills, générateurs, `CLAUDE.md`, `IA_CONTEXT_BASE.md`) sont à corriger dans la méme opération ; aucun renommage sans go séparé d'Eric.

### 6.16 Dossiers à la racine de la prod : pas de convention de nommage (décidé le 2026-10-18)
- Les dossiers placés à la racine de la prod, juste après `/config/` (racine de `H:`), gardent le nom qu'ils ont en prod et ne suivent pas la convention de nommage : `command_line`, `sensors`, `templates`, `utility_meter`, `shell_command`, `groups`, `input_booleans`, `input_number`, `timers`, `notifs`, `themes`, `.scripts`. Les dossiers de `docs` qui sont à cet endroit (`01_docs_config_system\config_system_SH_PY_YAML`) suivent la prod.
- La convention commence au niveau d'en dessous : `command_line\Audit`, `command_line\Energie`, `command_line\IP_externe`, `command_line\Meteo`, `sensors\Meteo`, `templates\Meteo`, `utility_meter\Meteo`, `utility_meter\P0_energie_total`.
- Contexte (option B choisie par Eric le 2026-10-18) : le local garde la convention, la prod est renommée pour la suivre. 15 renommages de casse faits en prod le 2026-10-18 (2 fichiers, 13 dossiers). Liste dans `TEMPO\renommages_casse_config_system_2026-10-18.txt` (colonne de gauche = nom de la convention).
- Point non tranché : la ligne du paragraphe 1 sur `command_line` écrit `Ip_externe`, l'arborescence écrit `IP_externe`. Le nom appliqué en prod est `IP_externe`.
## 7. Écarts relevés
Liste de tous les dossiers (482) et fichiers (474) de `docs`, hors fichiers `.bak_...` (366, qui suivent le nom de leur fichier). Nombre d'entrées en écart par règle (une entrée peut cumuler plusieurs écarts) :
- 00_IA (noms pas tout en majuscules) : 1
- dossiers LxCx_{NOM} pas en majuscules : 17
- dossiers vignette à renommer en 0N_LxCx_Vignette : 35
- dossiers page à renommer en 0N_LxCx_Page : 48
- fichiers vignette à renommer en Vignette_LxCx : 18
- fichiers page à renommer en Page_LxCx : 25
- tuto à renommer en TUTO_LxCx : 1
- fichier couleur pas en majuscules : 1
- noms avec accent : 17
- Air_Quality, préfixes AQ_ et MPC_ (paragraphe 6.6) : 6
- SDB (paragraphe 6.8) : 51
- UI_DASHBOARD (paragraphe 6.9) : 3
- eCO (paragraphe 6.10) : 7
- Z2M (paragraphe 6.11) : 7
- RASPI (paragraphe 6.12) : 9
- GitHub (paragraphe 6.13) : 10
- GLOBAL_INDEX (paragraphe 6.14) : 10 (appliqué en local le 2026-10-17)
- dossiers à classer : 2

## 8. Arborescence complète (état réel du 2026-10-17)
La colonne de droite donne la règle appliquée à l'entrée, ou l'écart avec le nom attendu. Cellule vide : la règle de base s'applique. État relevé sur le PC en local, noms modifiés à la main compris.

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┬─────────────────────────────────────────────────────────────────────────────────────────────┐
│ ARBORESCENCE                                                                                │ RÈGLE APPLIQUÉE                                                                             │
├─────────────────────────────────────────────────────────────────────────────────────────────┼─────────────────────────────────────────────────────────────────────────────────────────────┤
│ docs/                                                                                       │                                                                                             │
│ │                                                                                           │                                                                                             │
│ ├── 00_IA/                                                                                  │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │                                                                                       │                                                                                             │
│ │   ├── IA_CONTEXT_BASE/                                                                    │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_CONTEXT_BASE.md                                                              │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── IA_CONTEXT_BASE_2026-07-19_15h46.md                                             │ écart 00_IA (attendu : IA_CONTEXT_BASE_2026-07-19_15H46.md ; 00_IA reste intact)            │
│ │   │                                                                                       │                                                                                             │
│ │   ├── SOUS_CONTEXT_IA/                                                                    │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_ARBO_DETAIL/                                                                 │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_ARBO_DETAIL.md                                                           │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/                                              │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md                                        │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_AUTOMATIONS_NOTIFS/                                                          │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_AUTOMATIONS_NOTIFS.md                                                    │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_CMD_TERMINAL_HA/                                                             │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_CMD_TERMINAL_HA.md                                                       │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_INDEX_AUTOMATIONS/                                                           │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_INDEX_AUTOMATIONS.md                                                     │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_INDEX_NAVIGATION/                                                            │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_INDEX_NAVIGATION.md                                                      │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_INTEGRATIONS_CARTES/                                                         │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_INTEGRATIONS_CARTES.md                                                   │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_NOM_DES_REPERTOIRES_ET_FICHIERS/                                             │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md                                       │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── IA_P4_PRESENCE/                                                                 │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── IA_P4_PRESENCE.md                                                           │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── IA_SKILLS_INVENTAIRE/                                                           │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── IA_SKILLS_INVENTAIRE.md                                                     │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │   │                                                                                       │                                                                                             │
│ │   └── GLOBAL_INDEX_IA.md                                                                  │ 00_IA : majuscules, conforme (00_IA intact)                                                 │
│ │                                                                                           │                                                                                             │
│ ├── 01_docs_config_system/                                                                  │ système : casse inchangée, image de H:\                                                     │
│ │   │                                                                                       │                                                                                             │
│ │   ├── config_system_MD/                                                                   │ système                                                                                     │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── configuration.md                                                                │ système                                                                                     │
│ │   │                                                                                       │                                                                                             │
│ │   └── config_system_SH_PY_YAML/                                                                 │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── blueprints/                                                                     │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── template/                                                                   │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── homeassistant/                                                          │ système                                                                                     │
│ │       │           │                                                                       │                                                                                             │
│ │       │           └── inverted_binary_sensor.yaml                                         │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── command_line/                                                                   │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Audit/                                                                      │ exception : 1re lettre en majuscule                                                         │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── audit_md5_md_yaml.yaml                                                  │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── audit_md5_yaml.yaml                                                     │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Energie/                                                                    │ exception : 1re lettre en majuscule                                                         │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── histo_energie.yaml                                                      │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Github_maintenance/                                                         │ exception : 1re lettre en majuscule ; écart GitHub (paragraphe 6.13)                        │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── github_maintenance.yaml                                                 │ système ; écart GitHub (paragraphe 6.13)                                                    │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── IP_externe/                                                                 │ exception : 1re lettre en majuscule                                                         │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── IP_externe.yaml                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── Meteo/                                                                      │ exception : 1re lettre en majuscule                                                         │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── carte_meteo_france.yaml                                                 │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── groups/                                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── GRP_01_batteries_hue.yaml                                                   │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── GRP_02_batteries_ikea.yaml                                                  │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── GRP_03_batteries_sonoff.yaml                                                │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── input_booleans/                                                                 │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P1/                                                                         │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P1_ACS_IB_01_arret_clim_securises.yaml                                  │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P1_BV_IB_inter_soufflant_sdb.yaml                                       │ système ; écart SDB (paragraphe 6.8)                                                        │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── P4/                                                                         │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── P4_presence_wifi.yaml                                                   │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── input_number/                                                                   │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── input_number.yaml                                                           │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── notifs/                                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── diag_conso_elec.txt                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── ecart_liky_vs_nodon.txt                                                     │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── sensors/                                                                        │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Air_quality/                                                                │ écart (attendu : Air_Quality ; paragraphe 6.6)                                              │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── A_01_air_quality.yaml                                                   │ écart préfixe (attendu : AQ_01_air_quality.yaml ; paragraphe 6.6)                           │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Meteo/                                                                      │ mis à la main par Eric                                                                      │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── M_meteo_sensors_blitzortung.yaml                                        │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P0_energie_total_min_maxi_diag/                                             │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P0_genelec_appart_mini_maxi/                                            │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P0_MINI_MAXI_AVG_genelec_appart.yaml                                │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── P1_clim_chauffage/                                                          │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── P1_DUT/                                                                 │ système                                                                                     │
│ │       │           │                                                                       │                                                                                             │
│ │       │           └── P1_DUT_clim_chauffage.yaml                                          │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── shell_command/                                                                  │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── GITHUB/                                                                     │ mis à la main ? à confirmer ; écart GitHub (paragraphe 6.13)                                │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── GITHUB_backup_github.yaml                                               │ système ; écart GitHub (paragraphe 6.13)                                                    │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P0/                                                                         │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P0_correct_linky.yaml                                                   │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── P4/                                                                         │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── P4_log_eric_zone.yaml                                                   │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── templates/                                                                      │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Air_quality/                                                                │ écart (attendu : Air_Quality ; paragraphe 6.6)                                              │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── A_01_air_quality.yaml                                                   │ écart préfixe (attendu : AQ_01_air_quality.yaml ; paragraphe 6.6)                           │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Inter_BP_Virtuel/                                                           │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P1/                                                                     │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P1_BV_IB_SW_inter_souflant_sdb.yaml                                 │ système ; écart SDB (paragraphe 6.8)                                                        │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Meteo/                                                                      │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── M_01_meteo_alerte/                                                      │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── M_01_meteo_alertes_card.yaml                                        │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── M_02_meteo_vent/                                                        │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_02_meteo_direction_vent_vence_deg_card.yaml                       │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_02_meteo_direction_vent_vence_label_card.yaml                     │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── M_02_meteo_vitesse_vent_vence_kmh_card.yaml                         │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── M_03_meteo_orage_eclaires/                                              │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_03_meteo_dernier_impact_foudre_card.yaml                          │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_03_meteo_direction_foudre_deg_card.yaml                           │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_03_meteo_direction_foudre_label_card.yaml                         │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_03_meteo_distance_foudre_km_card.yaml                             │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── M_03_meteo_timer_foudre_card.yaml                                   │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── M_04_meteo_tendances/                                                   │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── M_04_tendances_th_est_humidity_card.yaml                            │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── M_04_tendances_th_ext_temperature_card.yaml                         │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── M_05_meteo_cycle_solaire/                                               │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       ├── M_05_meteo_duree_du_jour_card.yaml                                  │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       ├── M_05_meteo_tendance_duree_jour_card.yaml                            │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── M_05_meteo_variation_quotidienne_card.yaml                          │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P0_energie_total_diag/                                                      │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P0_Diag/                                                                │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P0_diag_conso_hebdomadaire_en_cours.yaml                            │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P0_diag_conso_jour_en_cours.yaml                                    │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P0_diag_conso_mois_en_cours.yaml                                    │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P0_Genelec_appart/                                                      │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P0_01_genelec_appart_AMHQ_cost.yaml                                 │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P0_02_ratio_hp_hc.yaml                                              │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P0_03_AVG_genelec_appart.yaml                                       │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P0_Linky/                                                               │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P0_MyElectricalData.yaml                                            │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P0_Total_pour_les_7_postes/                                             │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P0_total_pour_les_7_postes.yaml                                     │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P1_clim_chauffage/                                                          │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P1_01_MASTER/                                                           │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P1_01_clim_logique_system_autom.yaml                                │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P1_02_automation_message_clim_7h30_21h.yaml                         │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P1_03_automation_message_clim_21h_7h30.yaml                         │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P1_AVG/                                                                 │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P1_AVG_AMHQ_TOTAL.yaml                                              │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P1_AVG_AMHQ_UNITE.yaml                                              │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P1_DUT_TOTAL/                                                           │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P1_DUT_TOTAL_SDB.yaml                                               │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P1_TOTAL/                                                               │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P1_TOTAL_AMHQ.yaml                                                  │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P1_ui_dashboard/                                                        │ écart UI_DASHBOARD (attendu : P1_UI_DASHBOARD ; paragraphe 6.9)                             │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P1_ui_dashboard.yaml                                                │ écart UI_DASHBOARD (attendu : P1_UI_DASHBOARD.yaml ; paragraphe 6.9)                        │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P2_prise/                                                                   │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P2_AVG/                                                                 │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P2_AVG_AMHQ_mini_pc.yaml                                            │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P2_AVG_AMHQ_prises.yaml                                             │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P2_AVG_AMHQ_veilles.yaml                                            │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P2_congelateur/                                                         │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P2_congelateur_compresseur_actif.yaml                               │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P2_eCO_prises/                                                          │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P2_eco_prises_config.yaml                                           │ écart eCO (paragraphe 6.10)                                                                 │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P2_I_all_standby_power/                                                 │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P2_current_all_standby.yaml                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P3_eclairage/                                                               │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P3_AVG/                                                                 │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P3_AVG_AMHQ_1_UNITE.yaml                                            │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P3_AVG_AMHQ_2_ZONE.yaml                                             │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P3_AVG_AMHQ_3_TOTAL.yaml                                            │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P3_ENERGIE_TPL/                                                         │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P3_TPL_AMHQ_1_UNITE.yaml                                            │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   ├── P3_TPL_AMHQ_2_ZONE.yaml                                             │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P3_TPL_AMHQ_3_TOTAL.yaml                                            │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P3_POWER_TPL/                                                           │ système                                                                                     │
│ │       │   │   │   │                                                                       │                                                                                             │
│ │       │   │   │   └── P3_POWER_3_TOTAL_ZONE.yaml                                          │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P3_ui_dashboard/                                                        │ écart UI_DASHBOARD (attendu : P3_UI_DASHBOARD ; paragraphe 6.9)                             │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P3_etats_status.yaml                                                │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P4_groupe_presence/                                                         │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P4_groupe_presence.yaml                                                 │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P4_wifi_detection.yaml                                                  │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Stores/                                                                     │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── S_01_store.yaml                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── utilitaires/                                                                │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── jour_nuit.yaml                                                          │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── Mise_a_jour_home_assistant.yaml                                         │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── nb_fenetre_ouvert_ferme_autom.yaml                                      │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── themes/                                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Frosted Glass/                                                              │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── Frosted Glass Dark Lite.yaml                                            │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── Frosted Glass Dark.yaml                                                 │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── Frosted Glass Light Lite.yaml                                           │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── Frosted Glass Light.yaml                                                │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── Frosted Glass Lite.yaml                                                 │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── Frosted Glass.yaml                                                      │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── ios-dark-mode/                                                              │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── ios-dark-mode.yaml                                                      │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── visionos/                                                                   │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── Liquid Glass Tinted.yaml                                                │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── Liquid Glass.yaml                                                       │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── System 7.yaml                                                           │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── visionos.yaml                                                           │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── timers/                                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── P1_timers/                                                                  │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── P1_Timer_10mn/                                                          │ système                                                                                     │
│ │       │       │   │                                                                       │                                                                                             │
│ │       │       │   ├── P1_timer_10mn_seche_serviettes_sdb.yaml                             │ système ; écart SDB (paragraphe 6.8)                                                        │
│ │       │       │   │                                                                       │                                                                                             │
│ │       │       │   └── P1_timer_10mn_soufflant_sdb.yaml                                    │ système ; écart SDB (paragraphe 6.8)                                                        │
│ │       │       │                                                                           │                                                                                             │
│ │       │       ├── P1_Timer_2h/                                                            │ système                                                                                     │
│ │       │       │   │                                                                       │                                                                                             │
│ │       │       │   └── P1_timer_2h_seche_serviettes_sdb.yaml                               │ système ; écart SDB (paragraphe 6.8)                                                        │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── P1_Timer_60mn/                                                          │ système                                                                                     │
│ │       │           │                                                                       │                                                                                             │
│ │       │           └── P1_timer_60mn_soufflant_sdb.yaml                                    │ système ; écart SDB (paragraphe 6.8)                                                        │
│ │       │                                                                                   │                                                                                             │
│ │       ├── utility_meter/                                                                  │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── Meteo/                                                                      │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── M_03_meteo_UM_blitzortung.yaml                                          │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P0_energie_total/                                                           │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── Genelec_appart/                                                         │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       ├── P0_UM_AMHQ.yaml                                                     │ système                                                                                     │
│ │       │   │       │                                                                       │                                                                                             │
│ │       │   │       └── P0_UM_AMHQ_HPHC.yaml                                                │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P1_clim_chauffage/                                                          │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P1_UM_AMHQ.yaml                                                         │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   ├── P2_prise/                                                                   │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P2_UM_AMHQ_mini_pc.yaml                                                 │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   ├── P2_UM_AMHQ_prises.yaml                                                  │ système                                                                                     │
│ │       │   │   │                                                                           │                                                                                             │
│ │       │   │   └── P2_UM_AMHQ_veilles.yaml                                                 │ système                                                                                     │
│ │       │   │                                                                               │                                                                                             │
│ │       │   └── P3_eclairage/                                                               │ système                                                                                     │
│ │       │       │                                                                           │                                                                                             │
│ │       │       └── P3_UM_AMHQ_1_UNITE.yaml                                                 │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── configuration.yaml                                                              │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── input_button.yaml                                                               │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       ├── input_datetime.yaml                                                             │ système                                                                                     │
│ │       │                                                                                   │                                                                                             │
│ │       └── input_select.yaml                                                               │ système                                                                                     │
│ │                                                                                           │                                                                                             │
│ ├── 02_Docs_dashboard/                                                                      │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Dashboard_docs_md/                                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L0C0_PAGE_Home/                                                                 │ L0C0 intact (décision Eric 2026-10-17) : nom du dossier à trancher                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_Home.md                                                            │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 03_Carte météo/                                                             │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 03_Carte meteo)            │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   ├── www_meteocons/                                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   └── Meteocons_install.md                                                │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   ├── Carte météo vence.md                                                    │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : Carte meteo vence.md)      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Meteocss_card_modif.md                                                  │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 04_Studio code server/                                                      │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_vscode_home.md                                                     │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 05_Impacte de foudre/                                                       │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_foudre_home.md                                                     │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 06_Lave linge/                                                              │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_lave_linge_home.md                                                 │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 07_Lave vaisselle/                                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_lave_vaisselle_home.md                                             │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 08_Congélateur/                                                             │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 08_Congelateur)            │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_congelateur_home.md                                                │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 09_Détecteur de fuite/                                                      │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 09_Detecteur de fuite)     │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_detecteur_fuite_home.md                                            │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 10_Carte meteoalarm/                                                        │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_meteoalarm_home.md                                                 │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 11_Carte présence/                                                          │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 11_Carte presence)         │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Card_presence_home.md                                                   │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L1C1_METEO/                                                                     │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L1C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L1C1_VIGNETTE_METEO.md                                                  │ écart fichier vignette (attendu : Vignette_L1C1_meteo.md)                                   │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ écart dossier page (attendu : 02_L1C1_Page)                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_meteo.md                                                           │ écart fichier page (attendu : Page_L1C1_meteo.md)                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Tuto_images_alertes_meteo_france.md                                         │ écart tuto (attendu : TUTO_L1C1_images_alertes_meteo_france.md)                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L1C2_TEMPERATURES/                                                              │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L1C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L1C2_VIGNETTE_TEMPERATURES.md                                           │ écart fichier vignette (attendu : Vignette_L1C2_temperatures.md)                            │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L1C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_temperatures.md                                                    │ écart fichier page (attendu : Page_L1C2_temperatures.md)                                    │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L1C3_CLIM/                                                                      │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L1C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L1C3_VIGNETTE_CLIM.md                                                   │ écart fichier vignette (attendu : Vignette_L1C3_clim.md)                                    │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L1C3_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_clim.md                                                            │ écart fichier page (attendu : Page_L1C3_clim.md)                                            │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L2C1_ENERGIE/                                                                   │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L2C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L2C1_VIGNETTE_ENERGIE.md                                                │ écart fichier vignette (attendu : Vignette_L2C1_energie.md)                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_temps_reel/                                                         │ écart dossier page (attendu : 02_L2C1_Page_temps_reel)                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_energie_temps_reel.md                                              │ écart fichier page (attendu : Page_L2C1_energie_temps_reel.md)                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 03_Page_principale/                                                         │ écart dossier page (attendu : 03_L2C1_Page_principale)                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_energie.md                                                         │ écart fichier page (attendu : Page_L2C1_energie.md)                                         │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 04_Page_mensuel/                                                            │ écart dossier page (attendu : 04_L2C1_Page_mensuel)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_energie_mensuel.md                                                 │ écart fichier page (attendu : Page_L2C1_energie_mensuel.md)                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── COULEURS_PRISES_PAR_PIECE.md                                                │ couleur en majuscules : conforme                                                            │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L2C2_ENERGIE_CLIM/                                                              │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L2C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L2C2_VIGNETTE_ENERGIE_CLIM.md                                           │ écart fichier vignette (attendu : Vignette_L2C2_energie_clim.md)                            │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L2C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_energie_clim.md                                                    │ écart fichier page (attendu : Page_L2C2_energie_clim.md)                                    │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L2C3_ENERGIE_ECLAIRAGE/                                                         │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L2C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L2C3_VIGNETTE_ECLAIRAGE.md                                              │ écart fichier vignette (attendu : Vignette_L2C3_eclairage.md)                               │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ écart dossier page (attendu : 02_L2C3_Page)                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_energie_eclairage.md                                               │ écart fichier page (attendu : Page_L2C3_energie_eclairage.md)                               │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Couleurs_eclairage_par_piece.md                                             │ écart couleur (attendu : COULEURS_ECLAIRAGE_PAR_PIECE.md)                                   │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L3C1_ECLAIRAGE/                                                                 │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L3C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L3C1_VIGNETTE_ECLAIRAGE.md                                              │ écart fichier vignette (attendu : Vignette_L3C1_eclairage.md)                               │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_gauche/                                                             │ écart dossier page (attendu : 02_L3C1_Page_gauche)                                          │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_eclairage_gauche.md                                                │ écart fichier page (attendu : Page_L3C1_eclairage_gauche.md)                                │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_droite/                                                             │ écart dossier page (attendu : 03_L3C1_Page_droite)                                          │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_eclairage_droite.md                                                │ écart fichier page (attendu : Page_L3C1_eclairage_droite.md)                                │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L3C2_PRISES/                                                                    │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L3C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L3C2_VIGNETTE_PRISES.md                                                 │ écart fichier vignette (attendu : Vignette_L3C2_prises.md)                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L3C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_prises.md                                                          │ écart fichier page (attendu : Page_L3C2_prises.md)                                          │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L3C3_STORES/                                                                    │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L3C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L3C3_VIGNETTE_STORES.md                                                 │ écart fichier vignette (attendu : Vignette_L3C3_stores.md)                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L3C3_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_stores.md                                                          │ écart fichier page (attendu : Page_L3C3_stores.md)                                          │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L4C1_MINI_PC/                                                                   │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L4C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L4C1_VIGNETTE_MINI_PC.md                                                │ écart fichier vignette (attendu : Vignette_L4C1_mini_pc.md)                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_MINI_PC/                                                            │ écart dossier page (attendu : 02_L4C1_Page_MINI_PC)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_MINI_PC.md                                                         │ écart fichier page (attendu : Page_L4C1_mini_pc.md)                                         │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_RASPI/                                                              │ écart dossier page (attendu : 03_L4C1_Page_RASPI)                                           │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_raspi.md                                                           │ écart fichier page (attendu : Page_L4C1_raspi.md) ; écart RASPI (paragraphe 6.12)           │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L4C2_PROXMOX/                                                                   │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L4C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L4C2_VIGNETTE_PROXMOX.md                                                │ écart fichier vignette (attendu : Vignette_L4C2_proxmox.md)                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L4C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_proxmox.md                                                         │ écart fichier page (attendu : Page_L4C2_proxmox.md)                                         │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L4C3_MAJ_HA/                                                                    │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L4C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L4C3_VIGNETTE_MAJ.md                                                    │ écart fichier vignette (attendu : Vignette_L4C3_maj.md)                                     │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_gauche/                                                             │ écart dossier page (attendu : 02_L4C3_Page_gauche)                                          │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_maj_gauche.md                                                      │ écart fichier page (attendu : Page_L4C3_maj_gauche.md)                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_droite/                                                             │ écart dossier page (attendu : 03_L4C3_Page_droite)                                          │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_maj_droite.md                                                      │ écart fichier page (attendu : Page_L4C3_maj_droite.md)                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L5C1_PILES_BATTERIES/                                                           │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L5C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L5C1_VIGNETTE_BATTERIES.md                                              │ écart fichier vignette (attendu : Vignette_L5C1_batteries.md)                               │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L5C1_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_batteries.md                                                       │ écart fichier page (attendu : Page_L5C1_batteries.md)                                       │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L5C2_BATTERIES_PORTABLES/                                                       │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L5C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L5C2_VIGNETTE_BATTERIES_PORTABLES.md                                    │ écart fichier vignette (attendu : Vignette_L5C2_batteries_portables.md)                     │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_gauche/                                                             │ écart dossier page (attendu : 02_L5C2_Page_gauche)                                          │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_batteries_portables_gauche.md                                      │ écart fichier page (attendu : Page_L5C2_batteries_portables_gauche.md)                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_droite/                                                             │ écart dossier page (attendu : 03_L5C2_Page_droite)                                          │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_batteries_portables_droite.md                                      │ écart fichier page (attendu : Page_L5C2_batteries_portables_droite.md)                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L5C3_MARIADB/                                                                   │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L5C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L5C3_VIGNETTE_MARIADB.md                                                │ écart fichier vignette (attendu : Vignette_L5C3_mariadb.md)                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_principale/                                                         │ écart dossier page (attendu : 02_L5C3_Page_principale)                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_systeme.md                                                         │ écart fichier page (attendu : Page_L5C3_systeme.md)                                         │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_reserve/                                                            │ écart dossier page (attendu : 03_L5C3_Page_reserve)                                         │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L5C3_SYSTEME_RESERVE.md                                            │ écart fichier page (attendu : Page_L5C3_systeme_reserve.md)                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L6C1_AIR_QUALITE/                                                               │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L6C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L6C1_VIGNETTE_AIR_QUALITE.md                                            │ écart fichier vignette (attendu : Vignette_L6C1_air_qualite.md)                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L6C1_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_air_qualite.md                                                     │ écart fichier page (attendu : Page_L6C1_air_qualite.md)                                     │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L6C2_POLLUTION_POLLEN/                                                          │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L6C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── L6C2_VIGNETTE_POLLUTION_POLLEN.md                                       │ écart fichier vignette (attendu : Vignette_L6C2_pollution_pollen.md)                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L6C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_pollution_pollen.md                                                │ écart fichier page (attendu : Page_L6C2_pollution_pollen.md)                                │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── L6C3_VIGIEAU/                                                                   │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │       │                                                                               │                                                                                             │
│ │   │       ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L6C3_Vignette)                                         │
│ │   │       │   │                                                                           │                                                                                             │
│ │   │       │   └── L6C3_VIGNETTE_VIGIEAU.md                                                │ écart fichier vignette (attendu : Vignette_L6C3_vigieau.md)                                 │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L6C3_Page)                                                 │
│ │   │           │                                                                           │                                                                                             │
│ │   │           └── Page_vigieau.md                                                         │ écart fichier page (attendu : Page_L6C3_vigieau.md)                                         │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Dashboard_docs_yaml/                                                                │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Dashboard_COMPLET/                                                              │ intact : Dashboard_COMPLET                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_03_16.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_03_20.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_03_22.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_03_25.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_03_29.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_04_01.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_04_15.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_04_19.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_04_25.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_05_03.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_05_24.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_06_13.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_06_18.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_07_14.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_07_18.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_08_01.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_08_02.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_08_09.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_09_20.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_09_24.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_10_04.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Dashboard_2026_10_11.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Dashboard_2026_10_14.yaml                                                   │ intact (sous Dashboard_COMPLET)                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L0C0_PAGE_Home/                                                                 │ L0C0 intact (décision Eric 2026-10-17) : nom du dossier à trancher                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_Home.yaml                                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 03_Carte météo/                                                             │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 03_Carte meteo)            │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   ├── Www_meteocons/                                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Clear-night.svg                                                     │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Cloudy.svg                                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Exceptional.svg                                                     │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Fog.svg                                                             │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Hail.svg                                                            │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Lightning-rainy.svg                                                 │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Lightning.svg                                                       │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Partlycloudy-night.svg                                              │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Partlycloudy.svg                                                    │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Pouring.svg                                                         │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Rainy.svg                                                           │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Snowy-rainy.svg                                                     │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Snowy.svg                                                           │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Sunny.svg                                                           │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   ├── Windy-variant.svg                                                   │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │   │                                                                       │                                                                                             │
│ │   │   │   │   │   └── Windy.svg                                                           │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   ├── Card_meteocss_home.yaml                                                 │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Meteocss-card.js                                                        │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 04_Studio code server/                                                      │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_vscode_home.yaml                                                   │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 05_Impacte de foudre/                                                       │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_foudre_home.yaml                                                   │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 06_Lave linge/                                                              │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_lave_linge_home.yaml                                               │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 07_Lave vaisselle/                                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_lave_vaisselle_home.yaml                                           │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 08_Congélateur/                                                             │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 08_Congelateur)            │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_congelateur_home.yaml                                              │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 09_Détecteur de fuite/                                                      │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 09_Detecteur de fuite)     │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_detecteur_fuite_home.yaml                                          │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 10_Carte meteoalarm/                                                        │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Card_meteoalarm_home.yaml                                               │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 11_Carte présence/                                                          │ L0C0 intact (décision Eric 2026-10-17) ; écart accent (attendu : 11_Carte presence)         │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Card_presence_home.yaml                                                 │ L0C0 intact (décision Eric 2026-10-17)                                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L1C1_01_Meteo/                                                                  │ écart LxCx_NOM (attendu : L1C1_01_METEO)                                                    │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_L1C1_Vignette/                                                           │ 0N_LxCx_Vignette[_suffixe] : conforme                                                       │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L1C1_meteo.yaml                                                │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_L1C1_Page/                                                               │ 0N_LxCx_Page[_suffixe] : conforme                                                           │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L1C1_meteo.yaml                                                    │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Card_duree_du_jour.yaml                                                     │ fichier à part Card_* : reste en place                                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L1C2_02_Temperatures/                                                           │ écart LxCx_NOM (attendu : L1C2_02_TEMPERATURES)                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L1C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L1C2_temperatures.yaml                                         │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L1C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L1C2_temperatures.yaml                                             │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L1C3_03_Commandes_Clim/                                                         │ écart LxCx_NOM (attendu : L1C3_03_COMMANDES_CLIM)                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L1C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L1C3_clim.yaml                                                 │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ écart dossier page (attendu : 02_L1C3_Page)                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L1C3_clim.yaml                                                     │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_calcule_temp_cible.yaml                                                │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_prog_clim_bureau.yaml                                                  │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_prog_clim_chambre.yaml                                                 │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_prog_clim_salon.yaml                                                   │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_prog_radiateur_cuisine.yaml                                            │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Card_prog_soufflant_sdb.yaml                                                │ fichier à part Card_* : reste en place ; écart SDB (paragraphe 6.8)                         │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L2C1_04_Energie_Generale/                                                       │ écart LxCx_NOM (attendu : L2C1_04_ENERGIE_GENERALE)                                         │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L2C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L2C1_energie.yaml                                              │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_temps_reel/                                                         │ écart dossier page (attendu : 02_L2C1_Page_temps_reel)                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L2C1_energie_temps_reel.yaml                                       │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 03_Page_principale/                                                         │ écart dossier page (attendu : 03_L2C1_Page_principale)                                      │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L2C1_energie_principale.yaml                                       │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 04_Page_mensuel/                                                            │ écart dossier page (attendu : 04_L2C1_Page_mensuel)                                         │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L2C1_energie_mensuel.yaml                                          │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L2C2_05_Energie_Clim/                                                           │ écart LxCx_NOM (attendu : L2C2_05_ENERGIE_CLIM)                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L2C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L2C2_energie_clim.yaml                                         │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L2C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L2C2_energie_clim.yaml                                             │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L2C3_06_Energie_Eclairage/                                                      │ écart LxCx_NOM (attendu : L2C3_06_ENERGIE_ECLAIRAGE)                                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L2C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L2C3_energie_eclairage.yaml                                    │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L2C3_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L2C3_energie_eclairage.yaml                                        │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L3C1_07_Commandes_Eclairage/                                                    │ écart LxCx_NOM (attendu : L3C1_07_COMMANDES_ECLAIRAGE)                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L3C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L3C1_eclairage.yaml                                            │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_gauche/                                                             │ écart dossier page (attendu : 02_L3C1_Page_gauche)                                          │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L3C1_eclairage_gauche.yaml                                         │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_droite/                                                             │ écart dossier page (attendu : 03_L3C1_Page_droite)                                          │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L3C1_eclairage_droite.yaml                                         │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L3C2_08_Commandes_Prises/                                                       │ écart LxCx_NOM (attendu : L3C2_08_COMMANDES_PRISES)                                         │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L3C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L3C2_prises.yaml                                               │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L3C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L3C2_prises.yaml                                                   │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L3C3_09_Stores_Fenetres/                                                        │ écart LxCx_NOM (attendu : L3C3_09_STORES_FENETRES)                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L3C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L3C3_stores.yaml                                               │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L3C3_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L3C3_stores.yaml                                                   │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L4C1_10_Mini_PC/                                                                │ écart LxCx_NOM (attendu : L4C1_10_MINI_PC)                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L4C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L4C1_mini_pc.yaml                                              │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ écart dossier page (attendu : 02_L4C1_Page)                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L4C1_mini_pc.yaml                                                  │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Card_popup_memory.yaml                                                      │ fichier à part Card_* : reste en place                                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L4C2_11_Proxmox/                                                                │ écart LxCx_NOM (attendu : L4C2_11_PROXMOX)                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L4C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L4C2_proxmox.yaml                                              │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page/                                                                    │ écart dossier page (attendu : 02_L4C2_Page)                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L4C2_proxmox.yaml                                                  │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Card_services_ha_z2m_mariadb.yaml                                           │ fichier à part Card_* : reste en place ; écart Z2M (paragraphe 6.11)                        │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L4C3_12_MAJ_HA/                                                                 │ LxCx_NOM en majuscules : conforme                                                           │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L4C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L4C3_maj_ha.yaml                                               │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_gauche/                                                             │ écart dossier page (attendu : 02_L4C3_Page_gauche)                                          │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L4C3_maj_ha_gauche.yaml                                            │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_droite/                                                             │ écart dossier page (attendu : 03_L4C3_Page_droite)                                          │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L4C3_maj_ha_droite.yaml                                            │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L5C1_13_Batteries_Piles/                                                        │ écart LxCx_NOM (attendu : L5C1_13_BATTERIES_PILES)                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L5C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L5C1_batteries_piles.yaml                                      │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L5C1_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L5C1_batteries_piles.yaml                                          │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L5C2_14_Batteries_Portables/                                                    │ écart LxCx_NOM (attendu : L5C2_14_BATTERIES_PORTABLES)                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L5C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L5C2_batteries_portables.yaml                                  │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_gauche/                                                             │ écart dossier page (attendu : 02_L5C2_Page_gauche)                                          │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L5C2_batteries_portables_gauche.yaml                               │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 03_Page_droite/                                                             │ écart dossier page (attendu : 03_L5C2_Page_droite)                                          │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L5C2_batteries_portables_droite.yaml                               │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L5C3_15_MariaDB/                                                                │ écart LxCx_NOM (attendu : L5C3_15_MARIADB)                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L5C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L5C3_mariadb.yaml                                              │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Page_mariadb/                                                            │ écart dossier page (attendu : 02_L5C3_Page_mariadb)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L5C3_mariadb.yaml                                                  │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 03_Page_systeme_reserve/                                                    │ écart dossier page (attendu : 03_L5C3_Page_systeme_reserve)                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Page_L5C3_systeme_reserve.yaml                                          │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Script sh/                                                                  │ dossier à classer (ni Vignette ni Page)                                                     │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Audit_md5.sh                                                            │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_audit_buttons.yaml                                                     │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_audit_journal.yaml                                                     │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_audit_md5.yaml                                                         │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Card_audit_recap.yaml                                                       │ fichier à part Card_* : reste en place                                                      │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Card_mariadb.yaml                                                           │ fichier à part Card_* : reste en place                                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L6C1_16_Air_Qualite/                                                            │ écart LxCx_NOM (attendu : L6C1_16_AIR_QUALITE)                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L6C1_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L6C1_air_qualite.yaml                                          │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L6C1_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L6C1_air_qualite.yaml                                              │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L6C2_17_Pollution_Pollen/                                                       │ écart LxCx_NOM (attendu : L6C2_17_POLLUTION_POLLEN)                                         │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L6C2_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L6C2_pollution_pollen.yaml                                     │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L6C2_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L6C2_pollution_pollen.yaml                                         │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── L6C3_18_VigiEau/                                                                │ écart LxCx_NOM (attendu : L6C3_18_VIGIEAU)                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Vignette/                                                                │ écart dossier vignette (attendu : 01_L6C3_Vignette)                                         │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Vignette_L6C3_vigieau.yaml                                              │ Vignette_LxCx[_suffixe] : conforme                                                          │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── 02_Page/                                                                    │ écart dossier page (attendu : 02_L6C3_Page)                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Page_L6C3_vigieau.yaml                                                  │ Page_LxCx[_suffixe] : conforme                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Page_RASPI/                                                                     │ dossier au niveau LxCx sans LxCx dans le nom, RASPI mis en majuscules à la main : à classer │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── 02_Page/                                                                    │                                                                                             │
│ │   │           │                                                                           │                                                                                             │
│ │   │           └── Page_raspi.yaml                                                         │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │                                                                                       │                                                                                             │
│ │   └── GLOBAL_INDEX_VIGNETTES_PAGES.md                                                     │ intact : GLOBAL_INDEX                                                                       │
│ │                                                                                           │                                                                                             │
│ ├── 03_Docs_automations/                                                                    │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_automations_md/                                                                │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── _Sans_categorie/                                                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P4_Log_zones_eric/                                                          │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P4_Log_zones_eric.md                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Veille_github_releases/                                                     │ écart GitHub (paragraphe 6.13)                                                              │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Veille_github_releases.md                                               │ écart GitHub (paragraphe 6.13)                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Automations.yalm original/                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Automations.md                                                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Backup ha - github/                                                             │ écart GitHub (paragraphe 6.13)                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Git_alerte_ko/                                                              │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Git_alerte_ko.md                                                        │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Git_au_demarrage/                                                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Git_au_demarrage.md                                                     │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Git_daily/                                                                  │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Git_daily.md                                                            │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Git_hourly/                                                                 │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Git_hourly.md                                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Git_push_manuel/                                                            │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Git_push_manuel.md                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Git_push_weekly_manuel/                                                     │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Git_push_weekly_manuel.md                                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Git_weekly/                                                                 │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Git_weekly.md                                                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Bouton virtuel/                                                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Bouton_inter_ikea_4/                                                        │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Bouton_inter_ikea_4.md                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Bouton_inter_somrig/                                                        │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Bouton_inter_somrig.md                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Contrôle entity z2m/                                                            │ écart accent (attendu : Controle entity z2m) ; écart Z2M (paragraphe 6.11)                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Z2m_last_seen/                                                              │ écart Z2M (paragraphe 6.11)                                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Z2m_last_seen.md                                                        │ écart Z2M (paragraphe 6.11)                                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Gestion des stores/                                                             │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Gestion_store_bureau/                                                       │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Gestion_store_bureau.md                                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gestion_store_salon/                                                        │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Gestion_store_salon.md                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Mariadb & vscode optimisation/                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Db_purge_mariadb/                                                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Db_purge_mariadb.md                                                     │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Economie_energie_vscode/                                                    │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Economie_energie_vscode.md                                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Météo/                                                                          │ écart accent (attendu : Meteo)                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Alerte_meteo_cartes/                                                        │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Alerte_meteo_cartes.md                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Maj_temps_foudre/                                                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Maj_temps_foudre.md                                                     │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Notif_foudre/                                                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Notif_foudre.md                                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Update_prev_humidity/                                                       │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Update_prev_humidity.md                                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Update_prev_temperature/                                                    │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Update_prev_temperature.md                                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P0_Enrige/                                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Diag_enregistrement_journalier/                                             │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Diag_enregistrement_journalier.md                                       │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Histo_linky_quotidien/                                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Histo_linky_quotidien.md                                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Histo_nodon_quotidien/                                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Histo_nodon_quotidien.md                                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Log_ecart_linky_nodon/                                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Log_ecart_linky_nodon.md                                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Rattrapage_linky_ecart/                                                     │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Rattrapage_linky_ecart.md                                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Rattrapage_linky_j2/                                                        │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Rattrapage_linky_j2.md                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_01_Clim_chauffage/                                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A0_clim_jour/                                                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── A0_clim_jour.md                                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── B0_clim_nuit/                                                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── B0_clim_nuit.md                                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── C_notif_temp_jour/                                                          │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── C_notif_temp_jour.md                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── D_notif_temp_nuit/                                                          │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── D_notif_temp_nuit.md                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── E_notif_fermeture_fenetres/                                                 │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── E_notif_fermeture_fenetres.md                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── F_arret_clim_notif/                                                         │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── F_arret_clim_notif.md                                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── G_notif_mode_changement/                                                    │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── G_notif_mode_changement.md                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── H_debug_force_mode/                                                         │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── H_debug_force_mode.md                                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── I_synchro_notif_prise_coupee/                                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── I_synchro_notif_prise_coupee.md                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── J_debug_notif_message_clim/                                                 │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── J_debug_notif_message_clim.md                                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_02_Cuisine/                                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A_chauffage_cuisine/                                                        │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── A_chauffage_cuisine.md                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── B_chauffage_cuisine_vacances/                                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── B_chauffage_cuisine_vacances.md                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Fiche_op_relais_cuisine_maj_shelly/                                         │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Fiche_op_relais_cuisine_maj_shelly.md                                   │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_03_Chauffage salle de bain/                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A_soufflant_sdb_bouton_rodret/                                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── A_soufflant_sdb_bouton_rodret.md                                        │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── B_soufflant_sdb_routage/                                                    │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── B_soufflant_sdb_routage.md                                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── C_watchdog_soufflant_sdb/                                                   │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── C_watchdog_soufflant_sdb.md                                             │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── D_sdb_soufflant_decompte_60min/                                             │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── D_sdb_soufflant_decompte_60min.md                                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── E_sdb_soufflant_rattrapage_demarrage_ha/                                    │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── E_sdb_soufflant_rattrapage_demarrage_ha.md                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── F_minuterie_seche_serviettes/                                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── F_minuterie_seche_serviettes.md                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── G_sdb_seche_serviettes_decompte_2h/                                         │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── G_sdb_seche_serviettes_decompte_2h.md                                   │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── H_sdb_seche_serviettes_rattrapage_demarrage_ha/                             │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── H_sdb_seche_serviettes_rattrapage_demarrage_ha.md                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Rodret_soufflant_sdb/                                                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Sdb_soufflant_specification_2026/                                           │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Sdb_soufflant_specification_2026.md                                     │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Timers_sdb_soufflant_et_seche_serviettes/                                   │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Timers_sdb_soufflant_et_seche_serviettes.md                             │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Z_soufflant_sdb_gestion_intelligente/                                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Z_soufflant_sdb_gestion_intelligente.md                                 │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Z_soufflant_sdb_old_2024-2025/                                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P2_Alarme_congélateur/                                                          │ écart accent (attendu : P2_Alarme_congelateur)                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Congelateur_alarme_capteur/                                                 │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Congelateur_alarme_capteur.md                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Congelateur_alarme_panne/                                                   │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Congelateur_alarme_panne.md                                             │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Congelateur_alarme_porte/                                                   │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Congelateur_alarme_porte.md                                             │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P2_Prises/                                                                      │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P2_Éco. prises/                                                                 │ écart accent (attendu : P2_Eco. prises) ; écart eCO (paragraphe 6.10)                       │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Eco_prises_dynamique/                                                       │ écart eCO (paragraphe 6.10)                                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Eco_prises_dynamique.md                                                 │ écart eCO (paragraphe 6.10)                                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Gestion_pc_bureau/                                                          │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Gestion_pc_bureau.md                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gestion_tv_chambre/                                                         │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Gestion_tv_chambre.md                                                   │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P3_Eclairage/                                                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Allumage_lumiere_entree/                                                    │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Allumage_lumiere_entree.md                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Bureau_activation_ecran_synchro/                                            │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Bureau_activation_ecran_synchro.md                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Bureau_forcer_play_on/                                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Bureau_forcer_play_on.md                                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Bureau_rodret_toggle_blanches/                                              │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Bureau_rodret_toggle_blanches.md                                        │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Bureau_watchdog_synchro_lampes/                                             │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Bureau_watchdog_synchro_lampes.md                                       │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Sdb_sync_miroir_lampe_et_relais_sdb/                                        │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Sdb_sync_miroir_lampe_et_relais_sdb.md                                  │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Raspi/                                                                          │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Rpi4_fan_pwm/                                                               │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Rpi4_fan_pwm.md                                                         │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Tarif hc-hp/                                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Basculement_tarif_hphc/                                                     │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Basculement_tarif_hphc.md                                               │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Watchdog piles (hue-ikea-sonoff)/                                               │                                                                                             │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── Watchdog_piles/                                                             │                                                                                             │
│ │   │           │                                                                           │                                                                                             │
│ │   │           └── Watchdog_piles.md                                                       │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_automations_yaml/                                                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── _Sans_categorie/                                                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P4_Log_zones_eric/                                                          │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P4_Log_zones_eric.yaml                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Veille_github_nouvelle_release_detectee/                                    │ écart GitHub (paragraphe 6.13)                                                              │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Veille_github_nouvelle_release_detectee.yaml                            │ écart GitHub (paragraphe 6.13)                                                              │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Automations.yalm original/                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Automations.yaml                                                            │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Backup ha - github/                                                             │ écart GitHub (paragraphe 6.13)                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 00_Backup_alerte_si_ko_15_min/                                              │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── 00_Backup_alerte_si_ko_15_min.yaml                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 01_Backup_git_hourly_h_10/                                                  │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── 01_Backup_git_hourly_h_10.yaml                                          │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 02_Backup_git_daily_03_00/                                                  │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── 02_Backup_git_daily_03_00.yaml                                          │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 03_Backup_git_weekly_dim_01_30/                                             │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── 03_Backup_git_weekly_dim_01_30.yaml                                     │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 04_Backup_git_push_manuel/                                                  │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── 04_Backup_git_push_manuel.yaml                                          │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── 05_Backup_git_push_weekly_manuel/                                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── 05_Backup_git_push_weekly_manuel.yaml                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Git_push_au_demarrage_ha/                                                   │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Git_push_au_demarrage_ha.yaml                                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Bouton virtuel/                                                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P3_Salon_bouton_ikea_inter_salon/                                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P3_Salon_bouton_ikea_inter_salon.yaml                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── P3_Salon_bouton_ikea_somrig/                                                │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── P3_Salon_bouton_ikea_somrig.yaml                                        │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Contrôle entity z2m/                                                            │ écart accent (attendu : Controle entity z2m) ; écart Z2M (paragraphe 6.11)                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Z2m_last_seen/                                                              │ écart Z2M (paragraphe 6.11)                                                                 │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Z2m_last_seen.yaml                                                      │ écart Z2M (paragraphe 6.11)                                                                 │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Gestion des stores/                                                             │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Gestion_optimisee_du_store_bureau/                                          │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Gestion_optimisee_du_store_bureau.yaml                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gestion_simple_du_store_salon_matin_soir/                                   │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Gestion_simple_du_store_salon_matin_soir.yaml                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Mariadb & vscode optimisation/                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Db_purge_mariadb_repack/                                                    │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Db_purge_mariadb_repack.yaml                                            │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Systeme_economie_energie_vs_code/                                           │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Systeme_economie_energie_vs_code.yaml                                   │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Météo/                                                                          │ écart accent (attendu : Meteo)                                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Alerte_meteo_france_actualisation_des_cartes/                               │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Alerte_meteo_france_actualisation_des_cartes.yaml                       │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Mettre_a_jour_le_temps_du_dernier_impact_de_foudre/                         │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Mettre_a_jour_le_temps_du_dernier_impact_de_foudre.yaml                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Notification_de_la_foudre/                                                  │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Notification_de_la_foudre.yaml                                          │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Update_previous_humidity/                                                   │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Update_previous_humidity.yaml                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Update_previous_temperature/                                                │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Update_previous_temperature.yaml                                        │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P0_Enrige/                                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Diag_enregistrement_journalier/                                             │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Diag_enregistrement_journalier.yaml                                     │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Histo_linky_quotidien/                                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Histo_linky_quotidien.yaml                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Histo_nodon_quotidien/                                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Histo_nodon_quotidien.yaml                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Log_ecart_linky_vs_nodon/                                                   │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Log_ecart_linky_vs_nodon.yaml                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Rattrapage_linky_ecart/                                                     │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Rattrapage_linky_ecart.yaml                                             │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Rattrapage_linky_j2_ecart/                                                  │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Rattrapage_linky_j2_ecart.yaml                                          │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_01_Clim_chauffage/                                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A0_clim_jour/                                                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A_0_2026_01_11_automatisation_clim_jour_07h30_21h00/                        │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── A_0_2026_01_11_automatisation_clim_jour_07h30_21h00.yaml                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── B0_clim_nuit/                                                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── B_0_2026_01_11_automatisation_clim_nuit_21h00_07h30/                        │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── B_0_2026_01_11_automatisation_clim_nuit_21h00_07h30.yaml                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── C_notification_temperature_up_ou_down_7h30_21h00/                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── C_notification_temperature_up_ou_down_7h30_21h00.yaml                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── D_notification_temperature_up_ou_down_21h00_7h30/                           │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── D_notification_temperature_up_ou_down_21h00_7h30.yaml                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── E_clim_notification_de_fermeture_des_fenetres/                              │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── E_clim_notification_de_fermeture_des_fenetres.yaml                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── F_clim_automatisation_arret_clim_notification/                              │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── F_clim_automatisation_arret_clim_notification.yaml                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── G_clim_notification_de_changement_de_mode_ete_fan_hiver/                    │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── G_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml            │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── H_clim_debug_force_mode_correct_securite/                                   │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── H_clim_debug_force_mode_correct_securite.yaml                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── I_synchro_notif_clim_si_prise_coupee/                                       │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── I_synchro_notif_clim_si_prise_coupee.yaml                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── J_debug_notifier_les_changements_de_message_clim_mobile/                    │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── J_debug_notifier_les_changements_de_message_clim_mobile.yaml            │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_02_Cuisine/                                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9/         │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── A_chauffage_cuisine_entre_4h45_7h_lmmj_ou_5_45h_8h_vsd_avec_t_19_9.yaml │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── B_chauffage_cuisine_vacances/                                               │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── B_chauffage_cuisine_vacances.yaml                                       │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_03_Chauffage salle de bain/                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── A_soufflant_sdb_bouton_rodret/                                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── A_soufflant_sdb_bouton_rodret.yaml                                      │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── B_soufflant_sdb_routage/                                                    │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── B_soufflant_sdb_routage.yaml                                            │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── C_salle_de_bain_watchdog_securite_soufflant/                                │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── C_salle_de_bain_watchdog_securite_soufflant.yaml                        │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── D_sdb_soufflant_decompte_60min_timer/                                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── D_sdb_soufflant_decompte_60min_timer.yaml                               │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── E_sdb_soufflant_rattrapage_demarrage_ha_timer/                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── E_sdb_soufflant_rattrapage_demarrage_ha_timer.yaml                      │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── F_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h/                 │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── F_minuterie_seche_serviettes_salle_de_bain_timer_absolu_2h.yaml         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── G_sdb_seche_serviettes_decompte_2h_timer/                                   │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── G_sdb_seche_serviettes_decompte_2h_timer.yaml                           │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer/                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── H_sdb_seche_serviettes_rattrapage_demarrage_ha_timer.yaml               │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Rodret_soufflant_sdb/                                                       │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant/                  │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Z_2026_02_01_salle_de_bain_gestion_intelligente_soufflant.yaml          │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P2_Alarme_congélateur/                                                          │ écart accent (attendu : P2_Alarme_congelateur)                                              │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Congelateur_alarme_capteur/                                                 │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Congelateur_alarme_capteur.yaml                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Congelateur_alarme_panne/                                                   │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Congelateur_alarme_panne.yaml                                           │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Congelateur_alarme_porte/                                                   │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Congelateur_alarme_porte.yaml                                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P2_Éco. prises/                                                                 │ écart accent (attendu : P2_Eco. prises) ; écart eCO (paragraphe 6.10)                       │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Eco_prises_dynamique_by_presence_groupe/                                    │ écart eCO (paragraphe 6.10)                                                                 │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Eco_prises_dynamique_by_presence_groupe.yaml                            │ écart eCO (paragraphe 6.10)                                                                 │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Gestion_pc_bureau_scene_de_fin_notif/                                       │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Gestion_pc_bureau_scene_de_fin_notif.yaml                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gestion_tv_chambre_scene_de_fin_notif/                                      │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Gestion_tv_chambre_scene_de_fin_notif.yaml                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P3_Eclairage/                                                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P3_Bureau_activation_ecran_synchro/                                         │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P3_Bureau_activation_ecran_synchro.yaml                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P3_Bureau_bouton_rodret_toggle_blanches/                                    │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P3_Bureau_bouton_rodret_toggle_blanches.yaml                            │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P3_Bureau_forcer_play_on_si_pc_tourne/                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P3_Bureau_forcer_play_on_si_pc_tourne.yaml                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P3_Bureau_watchdog_synchronisation_lampes_blanches/                         │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P3_Bureau_watchdog_synchronisation_lampes_blanches.yaml                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── P3_Entree_allumage_lumiere/                                                 │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── P3_Entree_allumage_lumiere.yaml                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── P3_Sdb_sync_miroir_lampe_et_relais_sdb/                                     │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── P3_Sdb_sync_miroir_lampe_et_relais_sdb.yaml                             │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Raspi/                                                                          │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── A_rpi_fan_pwm_6_states/                                                     │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── A_rpi_fan_pwm_6_states.yaml                                             │ écart RASPI (paragraphe 6.12)                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Tarif hc-hp/                                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Auto_energie_basculement_tarif_hc_hp_genelec_appart/                        │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── Auto_energie_basculement_tarif_hc_hp_genelec_appart.yaml                │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Watchdog piles (hue-ikea-sonoff)/                                               │                                                                                             │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── Systeme_watchdog_piles_hue_ikea_sonoff/                                     │                                                                                             │
│ │   │           │                                                                           │                                                                                             │
│ │   │           └── Systeme_watchdog_piles_hue_ikea_sonoff.yaml                             │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   └── GLOBAL_INDEX_AUTOMATIONS.md                                                         │ intact : GLOBAL_INDEX                                                                       │
│ │                                                                                           │                                                                                             │
│ ├── 04_Docs_scripts/                                                                        │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_script_original/                                                               │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_scripts_sh/                                                                    │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5/                                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5.sh                                                                │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5_md_yaml/                                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5_md_yaml.sh                                                        │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5_yaml/                                                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5_yaml.sh                                                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Check_global_index/                                                             │ écart GLOBAL_INDEX (paragraphe 6.14)                                                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Check_global_index.py                                                       │ écart GLOBAL_INDEX (paragraphe 6.14)                                                        │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Check_sous_context_ia/                                                          │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── __Pycache__/                                                                │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── Check_sous_context_ia.cpython-314.pyc                                   │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Check_sous_context_ia.py                                                    │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Gen_global_index_automations/                                                   │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gen_global_index_automations.py                                             │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Gen_global_index_ia/                                                            │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gen_global_index_ia.py                                                      │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Gen_global_index_scripts/                                                       │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gen_global_index_scripts.py                                                 │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Gen_global_index_vignettes_pages/                                               │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Gen_global_index_vignettes_pages.py                                         │ renommé, à confirmer par Eric ; écart GLOBAL_INDEX (paragraphe 6.14)                        │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Ha_git_backup/                                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Ha_git_backup.sh                                                            │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Hermes_audit_md5_docs/                                                          │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Hermes_audit_md5_docs.sh                                                    │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Hermes_audit_md5_trigul_3md/                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── Hermes_audit_md5_trigul_3md.sh                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Hermes_audit_md5_trigul_unitaire.py                                         │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Mf_vigilance_images/                                                            │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Mf_vigilance_images.sh                                                      │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Mp_01_monitor_temp.sh - save pour raspi/                                        │ écart préfixe (attendu : MPC_01_monitor_temp.sh - save pour RASPI ; 6.6 et 6.12)            │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── #Mp_01_monitor_temp.sh.#                                                    │ écart préfixe (attendu : #MPC_01_monitor_temp.sh.# ; paragraphe 6.6)                        │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_scripts_sh_md/                                                                 │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5/                                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5.md                                                                │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5_docs/                                                                 │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5_docs.md                                                           │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha_git_backup/                                                                  │                                                                                             │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── Ha_git_backup.md                                                            │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_scripts_yaml/                                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5/                                                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5.yaml                                                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Audit_md5_md_yaml/                                                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Audit_md5_md_yaml.yaml                                                      │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Check_yaml_forme/                                                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Check_yaml_forme.py                                                         │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Climatisation/                                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── J_1_1_salon_clim_on_off_intelligent/                                        │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── J_1_1_salon_clim_on_off_intelligent.yaml                                │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── J_1_2_bureau_clim_on_off_intelligent/                                       │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── J_1_2_bureau_clim_on_off_intelligent.yaml                               │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── J_1_3_chambre_clim_on_off_intelligent/                                      │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── J_1_3_chambre_clim_on_off_intelligent.yaml                              │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   ├── J_2_0_secu_arret_clim_protege/                                              │                                                                                             │
│ │   │   │   │   │                                                                           │                                                                                             │
│ │   │   │   │   └── J_2_0_secu_arret_clim_protege.yaml                                      │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── P1_Master_gestion_clim/                                                     │                                                                                             │
│ │   │   │       │                                                                           │                                                                                             │
│ │   │   │       └── P1_Master_gestion_clim.yaml                                             │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Correct_linky/                                                                  │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Correct_linky.py                                                            │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Soufflant sdb/                                                                  │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │       │                                                                               │                                                                                             │
│ │   │       ├── Sdb_soufflant_arreter/                                                      │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │       │   │                                                                           │                                                                                             │
│ │   │       │   └── Sdb_soufflant_arreter.yaml                                              │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── Sdb_soufflant_demarrer/                                                     │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │           │                                                                           │                                                                                             │
│ │   │           └── Sdb_soufflant_demarrer.yaml                                             │ écart SDB (paragraphe 6.8)                                                                  │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Docs_scripts_yaml_md/                                                               │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── P1_Master_gestion_clim/                                                         │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── P1_Master_gestion_clim.md                                                   │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── Script_j2_0_secu_arret_clim/                                                    │                                                                                             │
│ │   │   │   │                                                                               │                                                                                             │
│ │   │   │   └── Script_j2_0_secu_arret_clim.md                                              │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Scripts_clim_on_off/                                                            │                                                                                             │
│ │   │       │                                                                               │                                                                                             │
│ │   │       └── Scripts_clim_on_off.md                                                      │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── GLOBAL_INDEX_SCRIPTS_SH.md                                                          │ intact : GLOBAL_INDEX                                                                       │
│ │   │                                                                                       │                                                                                             │
│ │   └── GLOBAL_INDEX_SCRIPTS_YAML.md                                                        │ intact : GLOBAL_INDEX                                                                       │
│ │                                                                                           │                                                                                             │
│ ├── 05_docs_MD_system/                                                                      │ intact : 05_docs_MD_system                                                                  │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Config_root/                                                                        │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Config_root.md                                                                  │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── DEPENDANCES_GLOBALES/                                                               │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── DEPENDANCES_GLOBALES.md                                                         │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── DEPENDANCES_GLOBALES_archive_2026-09-28.md                                      │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   ├── DEPENDANCES_GLOBALES_archive_2026-10-07_18h13.md                                │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── DEPENDANCES_GLOBALES_archive_2026-10-07_19h20.md                                │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │                                                                                       │                                                                                             │
│ │   ├── DEPENDANCES_GLOBALES_HERMES/                                                        │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── DEPENDANCES_GLOBALES_HERMES_V1.md                                               │ intact : DEPENDANCES_GLOBALES                                                               │
│ │   │                                                                                       │                                                                                             │
│ │   ├── ENTITES_GLOBAL_INDEX/                                                               │ intact : GLOBAL_INDEX                                                                       │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── ENTITES_GLOBAL_INDEX.md                                                         │ intact : GLOBAL_INDEX                                                                       │
│ │   │                                                                                       │                                                                                             │
│ │   ├── GLOBAL_INDEX_REPO/                                                                  │ intact : GLOBAL_INDEX                                                                       │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── GLOBAL_INDEX_REPO.md                                                            │ intact : GLOBAL_INDEX                                                                       │
│ │   │                                                                                       │                                                                                             │
│ │   └── Matrisse_template_doc/                                                              │                                                                                             │
│ │       │                                                                                   │                                                                                             │
│ │       └── _Template_doc.md                                                                │                                                                                             │
│ │                                                                                           │                                                                                             │
│ ├── 05_Docs_skills/                                                                         │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_fix-file/                                                                     │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Fix-file.md                                                                     │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-new-yaml/                                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-new-yaml.md                                                                  │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-push-docs/                                                                 │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-push-docs.md                                                                 │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-push-md/                                                                   │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-push-md.md                                                                   │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-push-yaml/                                                                 │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-push-yaml.md                                                                 │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-resync-tree/                                                               │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-resync-tree.md                                                               │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-status/                                                                    │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-status.md                                                                    │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-trigul/                                                                    │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-trigul.md                                                                    │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_ha-verif-headers/                                                                    │                                                                                      │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Ha-verif-headers.md                                                                    │                                                                                      │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_histo/                                                                        │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Histo.md                                                                        │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_histo-final/                                                                  │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Histo-final.md                                                                  │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_journal-modifs/                                                               │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Journal-modifs.md                                                               │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   ├── Skill_sync-index/                                                                   │                                                                                             │
│ │   │   │                                                                                   │                                                                                             │
│ │   │   └── Sync-index.md                                                                   │                                                                                             │
│ │   │                                                                                       │                                                                                             │
│ │   └── Skill_update-arbo/                                                                  │                                                                                             │
│ │       │                                                                                   │                                                                                             │
│ │       └── Update-arbo.md                                                                  │                                                                                             │
│ │                                                                                           │                                                                                             │
│ └── 06_Docs_technique/                                                                      │                                                                                             │
│     │                                                                                       │                                                                                             │
│     └── 01_Pont_hue_hacking/                                                                │                                                                                             │
│         │                                                                                   │                                                                                             │
│         └── 01_Pont_hue_hacking.md                                                          │                                                                                             │
└─────────────────────────────────────────────────────────────────────────────────────────────┴─────────────────────────────────────────────────────────────────────────────────────────────┘
```

## 9. Points ouverts
- Suffixe `[_suffixe]` : les exemples d'Eric sont en minuscules (`Page_L1C1_meteo`) mais la casse du suffixe n'est pas écrite. Le relevé attend du minuscule quand le suffixe actuel est entièrement en majuscules.
- `UI_DASHBOARD` (6.9) : orthographe `DASHBOARD` (Eric a écrit `DASBOARD`).
- `Dashboard_docs_specifique` : organisation à plat non confirmée. Les 14 `Card_*.yaml` hors `L0C0_PAGE_Home` (L1C1 : 1, L1C3 : 6, L4C1 : 1, L4C2 : 1, L5C3 : 5) restent en place selon ma proposition, non confirmée. Des noms de `Card_*` sont cités dans `GLOBAL_INDEX_VIGNETTES_PAGES.md`, `DEPENDANCES_GLOBALES.md`, `GLOBAL_INDEX_REPO.md` et `IA_CONTEXT_BASE.md`. Qu'aucune page ni aucun index ne cite les fichiers couleur est le constat d'Eric, je ne l'ai pas vérifié.
- `L0C0_PAGE_Home` : le nom du dossier reste-t-il `L0C0_PAGE_Home` (exception) ou devient-il `L0C0_PAGE_HOME` ? Neuf noms avec accent y figurent, signalés mais intacts.
- Dossiers hors schéma LxCx, à classer. Page_RASPI : RASPI mis en majuscules à la main depuis le relevé de 21:30, non journalisé. Script sh : dossier avec espace dans L5C3_15_MariaDB, déjà présent au relevé de 21:30 :
- `02_Docs_dashboard\Dashboard_docs_yaml\L5C3_15_MariaDB\Script sh`
- `02_Docs_dashboard\Dashboard_docs_yaml\Page_RASPI`
- 50 noms contiennent des espaces (exemple `04_Studio code server`) : aucune règle n'existe.
- `00_IA\SOUS_CONTEXT_IA` : orthographe tranché par Eric le 2026-10-17 (SOUS_CONTEXT_IA, avec X). L'ancien nom local `SOUS_CONTEST_IA` (saisi à la main) et l'ancien nom prod `sous_context_ia` sont renommés en `SOUS_CONTEXT_IA`. Chemins de `CLAUDE.md` et de ses cousins corrigés ; scripts, skills et fiches : en cours.
- `01_docs_config_system\config_system_SH_PY_YAML\sensors\Meteo` et `shell_command\GITHUB` : majuscules mises à la main par Eric. Elles contredisent la règle "système en minuscules" : à trancher. Pour `shell_command\GITHUB`, tranché le 2026-10-17 : `GitHub` (paragraphe 6.13).
- `Gen_global_index_*` (4 dossiers) : renommés d'après le tree validé, sans réponse explicite d'Eric.
- `Docs_scripts_sh\Check_sous_context_ia\__Pycache__` : mon renommage a changé la casse d'un dossier de cache généré, à remettre en `__pycache__`. Demande sans réponse.
- `05_docs_YAML_system` n'existe pas, identité à préciser.
- Où inscrire ces règles dans `CLAUDE.md` et ses fichiers apparentés : non décidé (`CLAUDE.md` et `IA_CONTEXT_BASE.md` sont à ne pas toucher).
- Des modifications faites à la main par Eric ne sont pas journalisées (liste dans le journal du jour).
- `AQ_` et `MPC_` : `S_` est repris de CLAUDE.md sans être rediscuté. `Air_Quality` est appliqué à ce seul dossier : à confirmer.
- Modules HACS (6.7) : orthographe exacte de Blitzortung, Vigieau et MeteoCSS ; conflit entre `L6C3_VIGIEAU` (majuscules imposées par 6.2 pour les dossiers LxCx) et l'orthographe du module.
- SDB (6.8) : impact du renommage sur les noms d'automations (à vérifier avant le go).
- eCO (6.10) : lecture de la règle (toutes les variantes de `eco` en mot isolé) et nom commençant par une minuscule.
- Z2M (6.11) : lecture de la règle (toutes les variantes de `z2m`) et impact du renommage sur l'automation `Z2m_last_seen` (non vérifié).
- RASPI (6.12) : `rpi` devient `RASPI`, y compris dans `A_rpi_fan_pwm_6_states` : impact sur le nom d'automation dans `H:\automations.yaml` (non vérifié).
- GitHub (6.13) : `command_line\Github_maintenance` et `shell_command\GITHUB` (mis à la main) passent à `GitHub` ; impact sur les `include` et les `shell_command` non vérifié.
- Dossiers de type de fichiers (6.15) : portée "tous les pôles" lue comme les dossiers md, yaml et sh de `01_` à `04_` ; dossiers nommés d'après un document ou un skill non concernés : à confirmer.
- Racines `01_docs_config_system` et `05_docs_MD_system` : `docs` en minuscules au début, alors que `02_Docs_dashboard`, `03_Docs_automations`, `04_Docs_scripts`, `05_Docs_skills` et `06_Docs_technique` ont une majuscule : à trancher (règle du premier mot, paragraphe 1).

## 10. Mise en oeuvre et précautions
- Les changements du 2026-10-16 sont des changements de casse seule. Sous Windows, le renommage se fait en deux temps (nom temporaire, puis nom final).
- GitHub distingue la casse. IA_ARBO_DETAIL (RÈGLES DE CASSE) indique que le local et `H:` ne la distinguent pas. Je n'ai pas testé `H:`. Pousser un dossier renommé sans renommer la prod peut créer un doublon à côté de l'ancien nom. Pour `command_line` et `sensors`, `configuration.yaml` charge le dossier entier : un doublon serait lu deux fois.
- Avant tout push en prod : renommer d'abord la prod à l'identique, puis supprimer les anciens noms avec un go explicite d'Eric (pas de corbeille sur `H:`).
- Après renommage : corriger les chemins cités dans les skills, les générateurs, les fiches à liens relatifs, `Github\README.md` et les MOC, puis régénérer les index.
- Les renommages de cette mise à jour (dossiers `0N_LxCx_...`, `LxCx_{NOM}`, accents, `TUTO_`, `COULEURS_`) touchent les liens des index : ils se font en une seule opération avec les corrections de chemins.
