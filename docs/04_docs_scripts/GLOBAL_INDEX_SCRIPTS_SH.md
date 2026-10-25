# GLOBAL_INDEX_SCRIPTS_SH.md - index des scripts shell et python

Fichier GENERE le 2026-10-25 21:20 par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications.

## Difference entre l'index SH et l'index YAML

- Scripts SH (index GLOBAL_INDEX_SCRIPTS_SH.md, dossier 04_docs_scripts_SH) : programmes bash ou python, executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\.scripts) et HA les lance par une commande shell_command (dossier H:\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.
- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier 04_docs_scripts_YAML) : scripts Home Assistant definis dans H:\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.
- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\shell_command) -> script SH (/config/.scripts).
- Verification par /histo : les deux index sont regeneres par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.

## Controle

- Scripts SH indexes : 23
- Scripts sans fiche dans 04_docs_scripts_SH_MD : 9 (Check_GLOBAL_INDEX.py, Check_sous_context_ia.py, Gen_GLOBAL_INDEX_automations.py, Gen_GLOBAL_INDEX_ia.py, Gen_GLOBAL_INDEX_scripts.py, Gen_GLOBAL_INDEX_vignettes_pages.py, Mf_vigilance_images.sh, histo_html.py, histo_trace.py)
- Scripts presents dans H:\.scripts avec un contenu different du local : 1 (Audit_md5_md_yaml.sh)
- Les scripts 'absent de H:\.scripts' tournent sur le PC ou ne sont pas deployes : a lire avec la colonne Skill.

## Scripts SH

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [Audit_md5.sh](04_docs_scripts_SH/Audit_md5/Audit_md5.sh) | bash | absent de H:\.scripts | - | - | - | [Audit_md5.md](04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md) | Audit_md5 |
| [Audit_md5_md_yaml.sh](04_docs_scripts_SH/Audit_md5_md_yaml/Audit_md5_md_yaml.sh) | bash | DIFFERENT | - | - | - | [Audit_md5.md](04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md) | Audit_md5_md_yaml |
| [Audit_md5_yaml.sh](04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh) | bash | identique | - | - | - | [Audit_md5.md](04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md) | Audit_md5_yaml |
| [Check_GLOBAL_INDEX.py](04_docs_scripts_SH/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.py) | python | absent de H:\.scripts | - | - | - | aucune | Check_GLOBAL_INDEX |
| [Check_XX_presents.py](04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py) | python | absent de H:\.scripts | - | - | ha-push-docs, ha-push-md, ha-push-yaml | [Check_XX_presents.md](04_docs_scripts_SH_MD/Check_XX_presents/Check_XX_presents.md) | Check_XX_presents |
| [XX_manifest.json](04_docs_scripts_SH/Check_XX_presents/XX_manifest.json) | autre | absent de H:\.scripts | - | - | ha-push-docs, ha-push-md, ha-push-yaml | [Check_XX_presents.md](04_docs_scripts_SH_MD/Check_XX_presents/Check_XX_presents.md) | Check_XX_presents |
| [Check_sous_context_ia.py](04_docs_scripts_SH/Check_sous_context_ia/Check_sous_context_ia.py) | python | absent de H:\.scripts | - | - | - | aucune | Check_sous_context_ia |
| [Gen_GLOBAL_INDEX_automations.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py) | python | absent de H:\.scripts | - | - | - | aucune | Gen_GLOBAL_INDEX_automations |
| [Gen_GLOBAL_INDEX_ia.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.py) | python | absent de H:\.scripts | - | - | - | aucune | Gen_GLOBAL_INDEX_ia |
| [Gen_GLOBAL_INDEX_scripts.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.py) | python | absent de H:\.scripts | - | - | - | aucune | Gen_GLOBAL_INDEX_scripts |
| [Gen_GLOBAL_INDEX_vignettes_pages.py](04_docs_scripts_SH/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py) | python | absent de H:\.scripts | - | - | - | aucune | Gen_GLOBAL_INDEX_vignettes_pages |
| [Ha_git_backup.sh](04_docs_scripts_SH/Ha_git_backup/Ha_git_backup.sh) | bash | identique | - | - | ha-trigul | [Ha_git_backup.md](04_docs_scripts_SH_MD/Ha_git_backup/Ha_git_backup.md) | Ha_git_backup |
| [Hermes_audit_md5_docs.sh](04_docs_scripts_SH/Hermes_audit_md5_docs/Hermes_audit_md5_docs.sh) | bash | absent de H:\.scripts | - | - | - | [Audit_md5_docs.md](04_docs_scripts_SH_MD/Audit_md5_docs/Audit_md5_docs.md) | Hermes_audit_md5_docs |
| [Hermes_audit_md5_trigul_3md.sh](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh) | bash | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_trigul_unitaire.md](04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_unitaire/Hermes_audit_md5_trigul_unitaire.md) | Hermes_audit_md5_trigul_3md |
| [Hermes_audit_md5_trigul_unitaire.py](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_unitaire.py) | python | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_trigul_unitaire.md](04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_unitaire/Hermes_audit_md5_trigul_unitaire.md) | Hermes_audit_md5_trigul_3md |
| [hermes_audit_trigul_arbres.py](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/hermes_audit_trigul_arbres.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Hermes_audit_trigul_arbres.md](04_docs_scripts_SH_MD/Hermes_audit_trigul_arbres/Hermes_audit_trigul_arbres.md) | Hermes_audit_md5_trigul_3md |
| [trigul_run.py](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/trigul_run.py) | python | absent de H:\.scripts | - | - | ha-trigul | [Trigul_run.md](04_docs_scripts_SH_MD/Trigul_run/Trigul_run.md) | Hermes_audit_md5_trigul_3md |
| [Mf_vigilance_images.sh](04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh) | bash | absent de H:\.scripts | - | - | - | aucune | Mf_vigilance_images |
| [Verif_emplacements.py](04_docs_scripts_SH/Verif_emplacements/Verif_emplacements.py) | python | absent de H:\.scripts | - | - | fix-file, ha-new-yaml, ha-push-docs, ha-push-yaml, ha-resync-tree, ha-trigul, ha-update-check-cli, ha-verif-headers, histo, histo-final, sync-index, update-arbo | [Verif_emplacements.md](04_docs_scripts_SH_MD/Verif_emplacements/Verif_emplacements.md) | Verif_emplacements |
| [Verif_headers_yaml.py](04_docs_scripts_SH/Verif_headers_yaml/Verif_headers_yaml.py) | python | absent de H:\.scripts | - | - | ha-verif-headers | [Verif_headers_yaml.md](04_docs_scripts_SH_MD/Verif_headers_yaml/Verif_headers_yaml.md) | Verif_headers_yaml |
| [Verif_integrations_file.py](04_docs_scripts_SH/Verif_integrations_file/Verif_integrations_file.py) | python | absent de H:\.scripts | - | - | histo | [Verif_integrations_file.md](04_docs_scripts_SH_MD/Verif_integrations_file/Verif_integrations_file.md) | Verif_integrations_file |
| [histo_html.py](04_docs_scripts_SH/histo_html/histo_html.py) | python | absent de H:\.scripts | - | - | histo, histo-final | aucune | histo_html |
| [histo_trace.py](04_docs_scripts_SH/histo_trace/histo_trace.py) | python | absent de H:\.scripts | - | - | histo, histo-final | aucune | histo_trace |
