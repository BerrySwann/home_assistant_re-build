# Audit_md5_md_yaml.sh - audit MD5 des docs, version locale (local / prod / GitHub)

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Audit_md5_md_yaml/Audit_md5_md_yaml.sh` |
| Langage | bash (git-bash sur le PC Windows) |
| Lance par | Eric ou Claude sur le PC. Ne fait pas tourner Home Assistant |
| Ecrit | `historique/md5_audit_md_yaml_AAAA-MM-JJ.txt` et sa copie `md5_audit_md_yaml_latest.txt` (compatibilite avec la carte du dashboard) |

## Role

Compare tous les fichiers de `docs/` (`.md`, `.yaml`, `.sh`) entre LOCAL (ReBuild, source de verite), PROD (`H:`) et GITHUB (curl sur les URL raw). MD5 brut et MD5 normalise (CRLF vers LF) pour classer : SYNC, CRLF (meme contenu, fins de ligne), DIFF, ABSENT. Un ecart local vers prod veut dire que la prod est en retard.

Variables surchargeables : `LOCAL_ROOT`, `PROD_ROOT` (par defaut `/h`), `GH_BASE`, `LOG_DIR`.

## A savoir

- Cette version s'execute localement. La version qui tourne dans Home Assistant (`/config/.scripts/audit_md5_md_yaml.sh`, appelee par `shell_command.audit_md5_md_yaml`) est une autre version : compare faite le 2026-10-28, MD5 differents (local 10084 octets, prod 6686 octets) et fiche existante de la prod dans `01_docs_config_system/01_config_system_MD/.scripts/01_scripts.sh_md/Audit_md5_md_yaml.md`.
- La carte L5C3 Systeme du dashboard lit le meme log.
- Pieges documentes dans l'en-tete : curl Windows n'ecrit pas dans `/tmp`, fichiers locaux en CRLF, chemins a espaces et accents.
- Selon le skill ha-trigul, le trigul actuel est fait par `hermes_audit_trigul_arbres.py` ; cet audit reste un outil separe.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture de l'en-tete du fichier source et de la comparaison des MD5 avec la version de la prod.
