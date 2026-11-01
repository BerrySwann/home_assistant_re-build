# GLOBAL_INDEX_SCRIPTS_SH.md - index des scripts shell (bash)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-4fc3f7?style=flat-square)](.)

</div>

Fichier GENERE le 2026-11-01 12:46 par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications.

## Difference entre les index SH, PY et YAML

- Scripts SH et PY (index GLOBAL_INDEX_SCRIPTS_SH.md pour les .sh bash, GLOBAL_INDEX_SCRIPTS_PY.md pour les .py python, dossier 04_docs_scripts_SH) : programmes executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\.scripts) et HA les lance par une commande shell_command (dossier H:\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.
- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier 04_docs_scripts_YAML) : scripts Home Assistant definis dans H:\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.
- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\shell_command) -> script SH (/config/.scripts).
- Verification par /histo : les trois index sont regeneres par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.

## Controle

- Scripts SH indexes : 7
- Scripts sans fiche dans 04_docs_scripts_SH_MD : 0
- Scripts presents dans H:\.scripts avec un contenu different du local : 0
- Les scripts 'absent de H:\.scripts' tournent sur le PC ou ne sont pas deployes : a lire avec la colonne Skill.
- Fichiers du dossier 04_docs_scripts_SH ni shell ni python, hors index : aucun
- Autre type de script : voir GLOBAL_INDEX_SCRIPTS_PY.md (dossier 04_docs_scripts_SH, classement identique).

## SCRIPTS HOME ASSISTANT, ILS TOURNENT DANS HOME ASSISTANT

#### .sh

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [Ha_git_backup.sh](04_docs_scripts_SH/Ha_git_backup/Ha_git_backup.sh) | bash | identique | shell_command.git_backup_push, shell_command.git_backup_push_manual, shell_command.git_backup_push_weekly | automation [01-Backup] Git hourly H+10, automation [02-Backup] Git daily (03:00), automation [06-Backup] Git au démarrage HA, automation [04-Backup] Git push manuel, automation [03-Backup] Git weekly (dim 01:30), automation [05-Backup] Git push weekly manuel | ha-trigul | [Ha_git_backup.md](04_docs_scripts_SH_MD/Ha_git_backup/Ha_git_backup.md) | Ha_git_backup |
| [Mf_vigilance_images.sh](04_docs_scripts_SH/Mf_vigilance_images/Mf_vigilance_images.sh) | bash | absent de H:\.scripts | - | - | - | [Mf_vigilance_images.md](04_docs_scripts_SH_MD/Mf_vigilance_images/Mf_vigilance_images.md) | Mf_vigilance_images |

## SCRIPTS HOME ASSISTANT, ILS NE TOURNENT PAS DANS HOME ASSISTANT (audit, verification, generation, historique et sauvegarde : la maison fonctionnerait sans eux)

### SCRIPTS DE L'IA CLAUDE

#### .sh

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [Audit_md5.sh](04_docs_scripts_SH/Audit_md5/Audit_md5.sh) | bash | absent de H:\.scripts | - | - | - | [Audit_md5.md](04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md) | Audit_md5 |
| [Audit_md5_docs_local.sh](04_docs_scripts_SH/Audit_md5_docs_local/Audit_md5_docs_local.sh) | bash | absent de H:\.scripts | - | - | - | [Audit_md5_docs_local.md](04_docs_scripts_SH_MD/Audit_md5_docs_local/Audit_md5_docs_local.md) | Audit_md5_docs_local |
| [Audit_md5_yaml.sh](04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh) | bash | identique | shell_command.audit_md5 | script audit_md5 | - | [Audit_md5_yaml.md](04_docs_scripts_SH_MD/Audit_md5_yaml/Audit_md5_yaml.md) | Audit_md5_yaml |

---

### SCRIPTS DE L'IA HERMES

#### .sh

| Script | Type | Copie dans H:\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |
|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|
| [Hermes_audit_md5_docs.sh](04_docs_scripts_SH/Hermes_audit_md5_docs/Hermes_audit_md5_docs.sh) | bash | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_docs.md](04_docs_scripts_SH_MD/Hermes_audit_md5_docs/Hermes_audit_md5_docs.md) | Hermes_audit_md5_docs |
| [Hermes_audit_md5_trigul_3md.sh](04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh) | bash | absent de H:\.scripts | - | - | - | [Hermes_audit_md5_trigul_3md.md](04_docs_scripts_SH_MD/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.md) | Hermes_audit_md5_trigul_3md |

---
