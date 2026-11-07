# GLOBAL_INDEX_SCRIPTS_SH.md - index des scripts shell et python

Fichier GENERE le 2026-11-07 17:14 par docs/04_docs_scripts/04_docs_scripts_sh/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications.

## Difference entre l'index SH et l'index YAML

- Scripts SH (index GLOBAL_INDEX_SCRIPTS_SH.md, dossier 04_docs_scripts_sh) : programmes bash ou python, executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\.scripts) et HA les lance par une commande shell_command (dossier H:\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.
- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier 04_docs_scripts_yaml) : scripts Home Assistant definis dans H:\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.
- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\shell_command) -> script SH (/config/.scripts).
- Verification par /histo : les deux index sont regeneres par docs/04_docs_scripts/04_docs_scripts_sh/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.

## Controle

- Scripts SH indexes : 40
- Scripts sans fiche dans 04_docs_scripts_sh_md : 0
- Scripts presents dans H:\.scripts avec un contenu different du local : 0
- Les scripts 'absent de H:\.scripts' tournent sur le PC ou ne sont pas deployes : a lire avec la colonne Skill.

## Scripts SH

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [Audit_md5.sh](04_docs_scripts_sh/Audit_md5/Audit_md5.sh) | bash | absent de H:\.scripts | - | - | - | [Audit_md5.md](04_docs_scripts_sh_md/Audit_md5/Audit_md5.md) | Audit_md5 |
| [Audit_md5_docs_local.sh](04_docs_scripts_sh/Audit_md5_docs_local/Audit_md5_docs_local.sh) | bash | absent de H:\.scripts | - | - | - | [Audit_md5_docs_local.md](04_docs_scripts_sh_md/Audit_md5_docs_local/Audit_md5_docs_local.md) | Audit_md5_docs_local |
| [Audit_md5_yaml.sh](04_docs_scripts_sh/Audit_md5_yaml/Audit_md5_yaml.sh) | bash | identique | - | - | - | [Audit_md5_yaml.md](04_docs_scripts_sh_md/Audit_md5_yaml/Audit_md5_yaml.md) | Audit_md5_yaml |
| [Check_DEPENDANCES.py](04_docs_scripts_sh/Check_DEPENDANCES/Check_DEPENDANCES.py) | python | absent de H:\.scripts | - | - | histo-final | [Check_DEPENDANCES.md](04_docs_scripts_sh_md/Check_DEPENDANCES/Check_DEPENDANCES.md) | Check_DEPENDANCES |
| [Check_GLOBAL_INDEX.py](04_docs_scripts_sh/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.py) | python | absent de H:\.scripts | - | - | - | [Check_GLOBAL_INDEX.md](04_docs_scripts_sh_md/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.md) | Check_GLOBAL_INDEX |
| [Check_XX_presents.py](04_docs_scripts_sh/Check_XX_presents/Check_XX_presents.py) | python | absent de H:\.scripts | - | - | ha-push-docs, ha-push-md, ha-push-yaml, hermes-aligne, histo | [Check_XX_presents.md](04_docs_scripts_sh_md/Check_XX_presents/Check_XX_presents.md) | Check_XX_presents |
| [Check_badges_fiches.py](04_docs_scripts_sh/Check_badges_fiches/Check_badges_fiches.py) | python | absent de H:\.scripts | - | - | - | [Check_badges_fiches.md](04_docs_scripts_sh_md/Check_badges_fiches/Check_badges_fiches.md) | Check_badges_fiches |
| [Check_prod_fonctionnelle.py](04_docs_scripts_sh/Check_prod_fonctionnelle/Check_prod_fonctionnelle.py) | python | absent de H:\.scripts | - | - | histo-final | [Check_prod_fonctionnelle.md](04_docs_scripts_sh_md/Check_prod_fonctionnelle/Check_prod_fonctionnelle.md) | Check_prod_fonctionnelle |
| [Check_sous_context_ia.py](04_docs_scripts_sh/Check_sous_context_ia/Check_sous_context_ia.py) | python | absent de H:\.scripts | - | - | - | [Check_sous_context_ia.md](04_docs_scripts_sh_md/Check_sous_context_ia/Check_sous_context_ia.md) | Check_sous_context_ia |
| [Copie_reference.py](04_docs_scripts_sh/Copie_reference/Copie_reference.py) | python | absent de H:\.scripts | - | - | histo | [Copie_reference.md](04_docs_scripts_sh_md/Copie_reference/Copie_reference.md) | Copie_reference |
| [Gen_GLOBAL_INDEX_automations.py](04_docs_scripts_sh/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_automations.md](04_docs_scripts_sh_md/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.md) | Gen_GLOBAL_INDEX_automations |
| [Gen_GLOBAL_INDEX_ia.py](04_docs_scripts_sh/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_ia.md](04_docs_scripts_sh_md/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.md) | Gen_GLOBAL_INDEX_ia |
| [Gen_GLOBAL_INDEX_scripts.py](04_docs_scripts_sh/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_scripts.md](04_docs_scripts_sh_md/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.md) | Gen_GLOBAL_INDEX_scripts |
| [Gen_GLOBAL_INDEX_vignettes_pages.py](04_docs_scripts_sh/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_vignettes_pages.md](04_docs_scripts_sh_md/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.md) | Gen_GLOBAL_INDEX_vignettes_pages |
| [Ha_git_backup.sh](04_docs_scripts_sh/Ha_git_backup/Ha_git_backup.sh) | bash | identique | - | - | ha-trigul | [Ha_git_backup.md](04_docs_scripts_sh_md/Ha_git_backup/Ha_git_backup.md) | Ha_git_backup |
| [Hermes_audit_md5_docs.sh](04_docs_scripts_sh/Hermes_audit_md5_docs/Hermes_audit_md5_docs.sh) | bash | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_docs.md](04_docs_scripts_sh_md/Hermes_audit_md5_docs/Hermes_audit_md5_docs.md) | Hermes_audit_md5_docs |
| [Hermes_audit_md5_trigul_3md.sh](04_docs_scripts_sh/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh) | bash | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_trigul_3md.md](04_docs_scripts_sh_md/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.md) | Hermes_audit_md5_trigul_3md |
| [Hermes_audit_md5_trigul_unitaire.py](04_docs_scripts_sh/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_unitaire.py) | python | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_trigul_unitaire.md](04_docs_scripts_sh_md/Hermes_audit_md5_trigul_unitaire/Hermes_audit_md5_trigul_unitaire.md) | Hermes_audit_md5_trigul_3md |
| [hermes_audit_trigul_arbres.py](04_docs_scripts_sh/Hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Hermes_audit_trigul_arbres.md](04_docs_scripts_sh_md/Hermes_audit_trigul_arbres/Hermes_audit_trigul_arbres.md) | Hermes_audit_md5_trigul_3md |
| [trigul_run.py](04_docs_scripts_sh/Hermes_audit_md5_trigul_3md/trigul_run.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Trigul_run.md](04_docs_scripts_sh_md/Trigul_run/Trigul_run.md) | Hermes_audit_md5_trigul_3md |
| [Mf_vigilance_images.sh](04_docs_scripts_sh/Mf_vigilance_images/Mf_vigilance_images.sh) | bash | absent de H:\.scripts | - | - | - | [Mf_vigilance_images.md](04_docs_scripts_sh_md/Mf_vigilance_images/Mf_vigilance_images.md) | Mf_vigilance_images |
| [Push_5C.py](04_docs_scripts_sh/Push_5C/Push_5C.py) | python | absent de H:\.scripts | - | - | histo | [Push_5C.md](04_docs_scripts_sh_md/Push_5C/Push_5C.md) | Push_5C |
| [Recap_index.py](04_docs_scripts_sh/Recap_index/Recap_index.py) | python | absent de H:\.scripts | - | - | histo | [Recap_index.md](04_docs_scripts_sh_md/Recap_index/Recap_index.md) | Recap_index |
| [Sync_98_sauvegarde.py](04_docs_scripts_sh/Sync_98_sauvegarde/Sync_98_sauvegarde.py) | python | absent de H:\.scripts | - | - | hermes-aligne | [Sync_98_sauvegarde.md](04_docs_scripts_sh_md/Sync_98_sauvegarde/Sync_98_sauvegarde.md) | Sync_98_sauvegarde |
| [Verif_emplacements.py](04_docs_scripts_sh/Verif_emplacements/Verif_emplacements.py) | python | absent de H:\.scripts | - | - | fix-file, ha-new-yaml, ha-push-docs, ha-push-yaml, ha-resync-tree, ha-trigul, ha-update-check-cli, ha-verif-headers, histo, histo-final, sync-index, update-arbo | [Verif_emplacements.md](04_docs_scripts_sh_md/Verif_emplacements/Verif_emplacements.md) | Verif_emplacements |
| [Verif_headers_yaml.py](04_docs_scripts_sh/Verif_headers_yaml/Verif_headers_yaml.py) | python | absent de H:\.scripts | - | - | ha-verif-headers | [Verif_headers_yaml.md](04_docs_scripts_sh_md/Verif_headers_yaml/Verif_headers_yaml.md) | Verif_headers_yaml |
| [Verif_integrations_file.py](04_docs_scripts_sh/Verif_integrations_file/Verif_integrations_file.py) | python | absent de H:\.scripts | - | - | - | [Verif_integrations_file.md](04_docs_scripts_sh_md/Verif_integrations_file/Verif_integrations_file.md) | Verif_integrations_file |
| [MPC_01_monitor_temp.sh](04_docs_scripts_sh/XX_MPC_01_monitor_temp_sh_RASPI%20%28a%20ne%20pas%20jeter%29/MPC_01_monitor_temp.sh) | bash | absent de H:\.scripts | - | - | - | [MPC_01_monitor_temp.md](04_docs_scripts_sh_md/XX_MPC_01_monitor_temp_sh_RASPI%20%28a%20ne%20pas%20jeter%29/MPC_01_monitor_temp.md) | XX_MPC_01_monitor_temp_sh_RASPI (a ne pas jeter) |
| [audit_carte_docs_hermes.py](04_docs_scripts_sh/audit_carte_docs_hermes/audit_carte_docs_hermes.py) | python | absent de H:\.scripts | - | - | - | [audit_carte_docs_hermes.md](04_docs_scripts_sh_md/audit_carte_docs_hermes/audit_carte_docs_hermes.md) | audit_carte_docs_hermes |
| [audit_huissier_hermes.py](04_docs_scripts_sh/audit_huissier_hermes/audit_huissier_hermes.py) | python | absent de H:\.scripts | - | - | - | [audit_huissier_hermes.md](04_docs_scripts_sh_md/audit_huissier_hermes/audit_huissier_hermes.md) | audit_huissier_hermes |
| [boite_claude_watch_hermes.py](04_docs_scripts_sh/boite_claude_watch_hermes/boite_claude_watch_hermes.py) | python | absent de H:\.scripts | - | - | - | [boite_claude_watch_hermes.md](04_docs_scripts_sh_md/boite_claude_watch_hermes/boite_claude_watch_hermes.md) | boite_claude_watch_hermes |
| [check_xx_repertoires_hermes.py](04_docs_scripts_sh/check_xx_repertoires_hermes/check_xx_repertoires_hermes.py) | python | absent de H:\.scripts | - | - | - | [check_xx_repertoires_hermes.md](04_docs_scripts_sh_md/check_xx_repertoires_hermes/check_xx_repertoires_hermes.md) | check_xx_repertoires_hermes |
| [edition_tracee_hermes.py](04_docs_scripts_sh/edition_tracee_hermes/edition_tracee_hermes.py) | python | absent de H:\.scripts | - | - | - | [edition_tracee_hermes.md](04_docs_scripts_sh_md/edition_tracee_hermes/edition_tracee_hermes.md) | edition_tracee_hermes |
| [gen_moc_dashboard.py](04_docs_scripts_sh/gen_moc_dashboard/gen_moc_dashboard.py) | python | absent de H:\.scripts | - | - | - | [gen_moc_dashboard.md](04_docs_scripts_sh_md/gen_moc_dashboard/gen_moc_dashboard.md) | gen_moc_dashboard |
| [gen_moc_docs.py](04_docs_scripts_sh/gen_moc_docs/gen_moc_docs.py) | python | absent de H:\.scripts | - | - | - | [gen_moc_docs.md](04_docs_scripts_sh_md/gen_moc_docs/gen_moc_docs.md) | gen_moc_docs |
| [hermes_gen_dependances.py](04_docs_scripts_sh/hermes_gen_dependances/hermes_gen_dependances.py) | python | absent de H:\.scripts | - | - | - | [hermes_gen_dependances.md](04_docs_scripts_sh_md/hermes_gen_dependances/hermes_gen_dependances.md) | hermes_gen_dependances |
| [histo_html.py](04_docs_scripts_sh/histo_html/histo_html.py) | python | absent de H:\.scripts | - | - | histo, histo-final | [histo_html.md](04_docs_scripts_sh_md/histo_html/histo_html.md) | histo_html |
| [histo_trace.py](04_docs_scripts_sh/histo_trace/histo_trace.py) | python | absent de H:\.scripts | - | - | histo, histo-final | [histo_trace.md](04_docs_scripts_sh_md/histo_trace/histo_trace.md) | histo_trace |
| [renomme_chemins_trace_hermes.py](04_docs_scripts_sh/renomme_chemins_trace_hermes/renomme_chemins_trace_hermes.py) | python | absent de H:\.scripts | - | - | - | [renomme_chemins_trace_hermes.md](04_docs_scripts_sh_md/renomme_chemins_trace_hermes/renomme_chemins_trace_hermes.md) | renomme_chemins_trace_hermes |
| [verif_ecriture_hermes.py](04_docs_scripts_sh/verif_ecriture_hermes/verif_ecriture_hermes.py) | python | absent de H:\.scripts | - | - | - | [verif_ecriture_hermes.md](04_docs_scripts_sh_md/verif_ecriture_hermes/verif_ecriture_hermes.md) | verif_ecriture_hermes |

<!-- RECAP-ENTITES:DEBUT -->

## Recapitulatif des entites citees par cet index

Total : **684 entites**. Origine de chacune : type, puis le nom de l integration telle qu elle apparait dans Appareils et services.

| origine | nombre | explication |
|:---|---:|:---|
| CREE template | 248 | creee par un YAML du depot, dossier `template`, sans aucune integration dans Appareils et services |
| NAT mqtt | 128 | chaine a trois maillons, verifiee le 2026-11-03 : Zigbee2MQTT (conteneur 200, Proxmox 10.32.154.244) publie vers le broker `core-mosquitto` (add-on Mosquitto, port 1883), que consomme l integration `mqtt` d Appareils et services. Si un des trois manque, les entites tombent |
| CREE utility_meter | 76 | creee par un YAML du depot, dossier `utility_meter`, sans aucune integration dans Appareils et services |
| NAT mobile_app | 49 | integration `mobile_app` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT hue | 35 | integration `hue` du coeur de Home Assistant, installee et visible dans Appareils et services |
| HACS atmofrance | 19 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Atmo France - Vence` |
| HACS powercalc | 19 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services en 38 entrees (premiere : `Hue ambiance lamp salon 1`) |
| NAT systemmonitor | 11 | integration `systemmonitor` du coeur de Home Assistant, installee et visible dans Appareils et services |
| HACS scheduler | 9 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Scheduler` |
| CREE statistics | 8 | creee par un YAML du depot, dossier `statistics`, sans aucune integration dans Appareils et services |
| CREE input_booleans | 7 | creee par un YAML du depot, dossier `input_booleans`, sans aucune integration dans Appareils et services |
| HACS meross_lan | 6 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services en 2 entrees (premiere : `Store SALON`) |
| CREE command_line | 5 | creee par un YAML du depot, dossier `command_line`, sans aucune integration dans Appareils et services |
| NAT hassio | 5 | integration `hassio` du coeur de Home Assistant, installee et visible dans Appareils et services |
| CREE history_stats | 4 | creee par un YAML du depot, dossier `history_stats`, sans aucune integration dans Appareils et services |
| CREE timers | 4 | creee par un YAML du depot, dossier `timers`, sans aucune integration dans Appareils et services |
| NAT broadlink | 4 | integration `broadlink` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT meteo_france | 4 | integration `meteo_france` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT proxmoxve | 4 | integration `proxmoxve` du coeur de Home Assistant, installee et visible dans Appareils et services |
| CREE groups | 3 | creee par un YAML du depot, dossier `groups`, sans aucune integration dans Appareils et services |
| CREE smartir | 3 | creee par un YAML du depot, dossier `smartir`, sans aucune integration dans Appareils et services |
| HACS blitzortung | 3 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Maison` |
| NAT template | 3 | integration `template` du coeur de Home Assistant, installee et visible dans Appareils et services |
| RASPI-PI4-4GO | 3 | entites du Raspberry Pi 4 4 Go : elles existent, le materiel est hors tension (pour Raspberry Pi4 4Go) |
| CREE input_button | 2 | creee par un YAML du depot, dossier `input_button`, sans aucune integration dans Appareils et services |
| CREE input_number | 2 | creee par un YAML du depot, dossier `input_number`, sans aucune integration dans Appareils et services |
| CREE person | 2 | creee par un YAML du depot, dossier `person`, sans aucune integration dans Appareils et services |
| CREE script | 2 | creee par un YAML du depot, dossier `script`, sans aucune integration dans Appareils et services |
| HACS vigieau | 2 | deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans Appareils et services sous le nom `Vigieau AEP` |
| NAT generic_thermostat | 2 | integration `generic_thermostat` du coeur de Home Assistant, installee et visible dans Appareils et services |
| ARTEFACT-TEMPLATE | 1 | mot-cle de template, pas une entite |
| CREE automation | 1 | creee par un YAML du depot, dossier `automation`, sans aucune integration dans Appareils et services |
| CREE input_datetime | 1 | creee par un YAML du depot, dossier `input_datetime`, sans aucune integration dans Appareils et services |
| CREE input_select | 1 | creee par un YAML du depot, dossier `input_select`, sans aucune integration dans Appareils et services |
| CREE powercalc | 1 | creee par un YAML du depot, dossier `powercalc`, sans aucune integration dans Appareils et services |
| CREE rest | 1 | creee par un YAML du depot, dossier `rest`, sans aucune integration dans Appareils et services |
| CREE sql | 1 | creee par un YAML du depot, dossier `sql`, sans aucune integration dans Appareils et services |
| HACS hacs | 1 | installee via HACS (qui va etre renomme marketplace) ; son entree dans Appareils et services n a pas de nom affiche |
| NAT cpuspeed | 1 | integration `cpuspeed` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT moon | 1 | integration `moon` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT season | 1 | integration `season` du coeur de Home Assistant, installee et visible dans Appareils et services |
| NAT-SANS-REGISTRE | 1 | fournie par Home Assistant sans entree au registre (zone.home) |

> **Chaine la plus fragile** : les `NAT mqtt` ne dependent pas que de Home Assistant. Mesure du 2026-11-03 : l integration `mqtt` pointe le broker add-on `core-mosquitto` (1883), et les mesures viennent de Zigbee2MQTT, conteneur 200 sur 10.32.154.244. Conteneur arrete, broker en vrac ou integration retiree : les entites tombent, sans que rien ne le signale dans l interface. A la meme date, 114 des 128 entites citees avaient remonte dans les 2 heures.

*Bloc ecrit par `recap_index.py`, encadre par deux marqueurs : il est remplace a chaque passage, jamais edite a la main. Classification : NAT <integration> si l entree de registre a un config entry ; NAT <integration> pour le coeur de Home Assistant, HACS <integration> pour ce qui vient de HACS ou d un depot (dossier custom_components) ; CREE <famille> sinon, famille = dossier du YAML qui declare l objet ; RASPI-PI4-4GO pour les trois entites du Pi 4 4 Go (materiel hors tension, entites existantes) ; SUPPRIMEE pour les noms remplaces ; ARTEFACT-TEMPLATE pour les mots-cles qui ne sont pas des entites.*

<!-- RECAP-ENTITES:FIN -->
