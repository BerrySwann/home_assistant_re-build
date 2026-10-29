# Audit_md5.yaml - script.audit_md5 (Audit MD5 GitHub)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_YAML/Audit_md5/Audit_md5.yaml` |
| Entite | `script.audit_md5` (alias "Audit MD5 GitHub", icone `mdi:shield-search`, mode `single`) |
| Prod | `H:\scripts.yaml` (bloc `audit_md5`) |
| Action | `shell_command.audit_md5` |

## Role

Un seul pas, "RUN AUDIT MD5" : appelle `shell_command.audit_md5`. Cette commande est definie dans `shell_command/GitHub/GitHub_backup_GitHub.yaml` et lance `bash /config/.scripts/audit_md5_yaml.sh`, avec ajout de la sortie dans `/config/.logs/md5_audit_yaml_AAAA-MM-JJ.txt`.

Le script bash compare les YAML de la prod a GitHub (voir la fiche de `Audit_md5_yaml.sh` dans `01_docs_config_system/01_config_system_MD/.scripts/01_scripts.sh_md/`).

## Etat

- Extrait le 2026-10-12 de la prod (`scripts.yaml`, fichier du 2026-10-07 20:20:29). Aucune copie locale n'existait. Contenu repris tel quel, non modifie. Pas de description dans la prod.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du YAML local, de `H:\scripts.yaml` et du shell_command.
