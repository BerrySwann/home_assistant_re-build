# GLOBAL_INDEX_SCRIPTS_PY.md - index des scripts python

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--09-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-4fc3f7?style=flat-square)](.)

</div>

Fichier GENERE le 2026-11-09 20:43 par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications.

## Difference entre les index SH, PY et YAML

- Scripts SH et PY (index GLOBAL_INDEX_SCRIPTS_SH.md pour les .sh bash, GLOBAL_INDEX_SCRIPTS_PY.md pour les .py python, dossier 04_docs_scripts_SH) : programmes executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\.scripts) et HA les lance par une commande shell_command (dossier H:\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.
- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier 04_docs_scripts_YAML) : scripts Home Assistant definis dans H:\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.
- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\shell_command) -> script SH (/config/.scripts).
- Verification par /histo : les trois index sont regeneres par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.

## Controle

- Scripts PY indexes : 34
- Scripts sans fiche dans 04_docs_scripts_SH_MD : 0
- Scripts presents dans H:\.scripts avec un contenu different du local : 0
- Les scripts 'absent de H:\.scripts' tournent sur le PC ou ne sont pas deployes : a lire avec la colonne Skill.
- Fichiers du dossier 04_docs_scripts_SH ni shell ni python, hors index : aucun
- Autre type de script : voir GLOBAL_INDEX_SCRIPTS_SH.md (dossier 04_docs_scripts_SH, classement identique).

## SCRIPTS HOME ASSISTANT, ILS TOURNENT DANS HOME ASSISTANT

- aucun script de ce type ne tourne dans Home Assistant

## SCRIPTS HOME ASSISTANT, ILS NE TOURNENT PAS DANS HOME ASSISTANT (audit, verification, generation, historique et sauvegarde : la maison fonctionnerait sans eux)

### SCRIPTS DE L'IA CLAUDE

#### .py

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [Check_badges_fiches.py](04_docs_scripts_SH/Check_badges_fiches/Check_badges_fiches.py) | python | absent de H:\.scripts | - | - | - | [Check_badges_fiches.md](04_docs_scripts_SH_MD/Check_badges_fiches/Check_badges_fiches.md) | Check_badges_fiches |
| [Check_DEPENDANCES.py](04_docs_scripts_SH/Check_DEPENDANCES/Check_DEPENDANCES.py) | python | absent de H:\.scripts | - | - | histo-final | [Check_DEPENDANCES.md](04_docs_scripts_SH_MD/Check_DEPENDANCES/Check_DEPENDANCES.md) | Check_DEPENDANCES |
| [Check_GLOBAL_INDEX.py](04_docs_scripts_SH/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.py) | python | absent de H:\.scripts | - | - | - | [Check_GLOBAL_INDEX.md](04_docs_scripts_SH_MD/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.md) | Check_GLOBAL_INDEX |
| [Check_prod_fonctionnelle.py](04_docs_scripts_SH/Check_prod_fonctionnelle/Check_prod_fonctionnelle.py) | python | absent de H:\.scripts | - | - | histo-final | [Check_prod_fonctionnelle.md](04_docs_scripts_SH_MD/Check_prod_fonctionnelle/Check_prod_fonctionnelle.md) | Check_prod_fonctionnelle |
| [Check_qualite_docs.py](04_docs_scripts_SH/Check_qualite_docs/Check_qualite_docs.py) | python | absent de H:\.scripts | - | - | histo, histo-final | [Check_qualite_docs.md](04_docs_scripts_SH_MD/Check_qualite_docs/Check_qualite_docs.md) | Check_qualite_docs |
| [Check_sous_context_ia.py](04_docs_scripts_SH/Check_sous_context_ia/Check_sous_context_ia.py) | python | absent de H:\.scripts | - | - | - | [Check_sous_context_ia.md](04_docs_scripts_SH_MD/Check_sous_context_ia/Check_sous_context_ia.md) | Check_sous_context_ia |
| [Check_XX_presents.py](04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py) | python | absent de H:\.scripts | - | - | ha-push-docs, ha-push-md, ha-push-yaml, hermes-aligne, histo | [Check_XX_presents.md](04_docs_scripts_SH_MD/Check_XX_presents/Check_XX_presents.md) | Check_XX_presents |
| [Copie_reference.py](04_docs_scripts_SH/Copie_reference/Copie_reference.py) | python | absent de H:\.scripts | - | - | histo | [Copie_reference.md](04_docs_scripts_SH_MD/Copie_reference/Copie_reference.md) | Copie_reference |
| [Gen_GLOBAL_INDEX_automations.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_automations.md](04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.md) | Gen_GLOBAL_INDEX_automations |
| [Gen_GLOBAL_INDEX_ia.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_ia.md](04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.md) | Gen_GLOBAL_INDEX_ia |
| [Gen_GLOBAL_INDEX_scripts.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_scripts.md](04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.md) | Gen_GLOBAL_INDEX_scripts |
| [Gen_GLOBAL_INDEX_vignettes_pages.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py) | python | absent de H:\.scripts | - | - | - | [Gen_GLOBAL_INDEX_vignettes_pages.md](04_docs_scripts_SH_MD/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.md) | Gen_GLOBAL_INDEX_vignettes_pages |
| [gen_moc_dashboard.py](04_docs_scripts_SH/gen_moc_dashboard/gen_moc_dashboard.py) | python | absent de H:\.scripts | - | - | - | [gen_moc_dashboard.md](04_docs_scripts_SH_MD/gen_moc_dashboard/gen_moc_dashboard.md) | gen_moc_dashboard |
| [gen_moc_docs.py](04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py) | python | absent de H:\.scripts | - | - | - | [gen_moc_docs.md](04_docs_scripts_SH_MD/gen_moc_docs/gen_moc_docs.md) | gen_moc_docs |
| [histo_html.py](04_docs_scripts_SH/histo_html/histo_html.py) | python | absent de H:\.scripts | - | - | histo, histo-final | [histo_html.md](04_docs_scripts_SH_MD/histo_html/histo_html.md) | histo_html |
| [histo_trace.py](04_docs_scripts_SH/histo_trace/histo_trace.py) | python | absent de H:\.scripts | - | - | histo, histo-final | [histo_trace.md](04_docs_scripts_SH_MD/histo_trace/histo_trace.md) | histo_trace |
| [Menage_bak.py](04_docs_scripts_SH/Menage_bak/Menage_bak.py) | python | absent de H:\.scripts | - | - | - | [Menage_bak.md](04_docs_scripts_SH_MD/Menage_bak/Menage_bak.md) | Menage_bak |
| [Push_5C.py](04_docs_scripts_SH/Push_5C/Push_5C.py) | python | absent de H:\.scripts | - | - | histo | [Push_5C.md](04_docs_scripts_SH_MD/Push_5C/Push_5C.md) | Push_5C |
| [Recap_index.py](04_docs_scripts_SH/Recap_index/Recap_index.py) | python | absent de H:\.scripts | - | - | histo | [Recap_index.md](04_docs_scripts_SH_MD/Recap_index/Recap_index.md) | Recap_index |
| [Sync_98_sauvegarde.py](04_docs_scripts_SH/Sync_98_sauvegarde/Sync_98_sauvegarde.py) | python | absent de H:\.scripts | - | - | hermes-aligne | [Sync_98_sauvegarde.md](04_docs_scripts_SH_MD/Sync_98_sauvegarde/Sync_98_sauvegarde.md) | Sync_98_sauvegarde |
| [trigul_run.py](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/trigul_run.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Trigul_run.md](04_docs_scripts_SH_MD/Trigul_run/Trigul_run.md) | Hermes_audit_md5_trigul_3md |
| [Verif_emplacements.py](04_docs_scripts_SH/Verif_emplacements/Verif_emplacements.py) | python | absent de H:\.scripts | - | - | fix-file, ha-new-yaml, ha-push-docs, ha-push-yaml, ha-resync-tree, ha-trigul, ha-update-check-cli, ha-verif-headers, histo, histo-final, sync-index, update-arbo | [Verif_emplacements.md](04_docs_scripts_SH_MD/Verif_emplacements/Verif_emplacements.md) | Verif_emplacements |
| [Verif_headers_yaml.py](04_docs_scripts_SH/Verif_headers_yaml/Verif_headers_yaml.py) | python | absent de H:\.scripts | - | - | ha-verif-headers | [Verif_headers_yaml.md](04_docs_scripts_SH_MD/Verif_headers_yaml/Verif_headers_yaml.md) | Verif_headers_yaml |
| [Verif_integrations_file.py](04_docs_scripts_SH/Verif_integrations_file/Verif_integrations_file.py) | python | absent de H:\.scripts | - | - | - | [Verif_integrations_file.md](04_docs_scripts_SH_MD/Verif_integrations_file/Verif_integrations_file.md) | Verif_integrations_file |

---

### SCRIPTS DE L'IA HERMES

#### .py

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [audit_carte_docs_hermes.py](04_docs_scripts_SH/audit_carte_docs_hermes/audit_carte_docs_hermes.py) | python | absent de H:\.scripts | - | - | - | [audit_carte_docs_hermes.md](04_docs_scripts_SH_MD/audit_carte_docs_hermes/audit_carte_docs_hermes.md) | audit_carte_docs_hermes |
| [audit_huissier_hermes.py](04_docs_scripts_SH/audit_huissier_hermes/audit_huissier_hermes.py) | python | absent de H:\.scripts | - | - | - | [audit_huissier_hermes.md](04_docs_scripts_SH_MD/audit_huissier_hermes/audit_huissier_hermes.md) | audit_huissier_hermes |
| [boite_claude_watch_hermes.py](04_docs_scripts_SH/boite_claude_watch_hermes/boite_claude_watch_hermes.py) | python | absent de H:\.scripts | - | - | - | [boite_claude_watch_hermes.md](04_docs_scripts_SH_MD/boite_claude_watch_hermes/boite_claude_watch_hermes.md) | boite_claude_watch_hermes |
| [check_xx_repertoires_hermes.py](04_docs_scripts_SH/check_xx_repertoires_hermes/check_xx_repertoires_hermes.py) | python | absent de H:\.scripts | - | - | - | [check_xx_repertoires_hermes.md](04_docs_scripts_SH_MD/check_xx_repertoires_hermes/check_xx_repertoires_hermes.md) | check_xx_repertoires_hermes |
| [edition_tracee_hermes.py](04_docs_scripts_SH/edition_tracee_hermes/edition_tracee_hermes.py) | python | absent de H:\.scripts | - | - | - | [edition_tracee_hermes.md](04_docs_scripts_SH_MD/edition_tracee_hermes/edition_tracee_hermes.md) | edition_tracee_hermes |
| [hermes_audit_md5_trigul_unitaire.py](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/hermes_audit_md5_trigul_unitaire.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Hermes_audit_md5_trigul_unitaire.md](04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_unitaire/Hermes_audit_md5_trigul_unitaire.md) | Hermes_audit_md5_trigul_3md |
| [hermes_audit_trigul_arbres.py](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Hermes_audit_trigul_arbres.md](04_docs_scripts_SH_MD/Hermes_audit_trigul_arbres/Hermes_audit_trigul_arbres.md) | Hermes_audit_md5_trigul_3md |
| [hermes_gen_dependances.py](04_docs_scripts_SH/hermes_gen_dependances/hermes_gen_dependances.py) | python | absent de H:\.scripts | - | - | - | [hermes_gen_dependances.md](04_docs_scripts_SH_MD/hermes_gen_dependances/hermes_gen_dependances.md) | hermes_gen_dependances |
| [renomme_chemins_trace_hermes.py](04_docs_scripts_SH/renomme_chemins_trace_hermes/renomme_chemins_trace_hermes.py) | python | absent de H:\.scripts | - | - | - | [renomme_chemins_trace_hermes.md](04_docs_scripts_SH_MD/renomme_chemins_trace_hermes/renomme_chemins_trace_hermes.md) | renomme_chemins_trace_hermes |
| [verif_ecriture_hermes.py](04_docs_scripts_SH/verif_ecriture_hermes/verif_ecriture_hermes.py) | python | absent de H:\.scripts | - | - | - | [verif_ecriture_hermes.md](04_docs_scripts_SH_MD/verif_ecriture_hermes/verif_ecriture_hermes.md) | verif_ecriture_hermes |

---
