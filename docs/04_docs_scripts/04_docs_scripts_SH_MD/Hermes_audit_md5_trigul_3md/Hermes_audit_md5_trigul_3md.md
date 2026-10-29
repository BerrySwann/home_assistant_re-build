# Hermes_audit_md5_trigul_3md.sh - ancien trigul .md en bash (local / prod / GitHub)

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Hermes_audit_md5_trigul_3md/Hermes_audit_md5_trigul_3md.sh` |
| Langage | bash (git-bash sur le PC Windows) |
| Lance par | personne aujourd'hui (voir "A savoir"). Ne fait pas tourner Home Assistant |
| Ecrit | `historique/hermes_md5_audit_md_AAAA-MM-JJ.txt` |

## Role

Triangulation des fichiers `.md` entre trois niveaux : LOCAL (ReBuild, source de verite), PROD (`H:`) et GITHUB (curl sur les URL raw). Complement du script de la prod (qui compare prod et GitHub) : il s'execute sur le PC, car le maillon local n'est visible que depuis le PC.

Format lisible : `L<->P | P<->R | L<->R | DETAIL | FICHIER`. Un ecart L<->P veut dire prod en retard, P<->R depot en retard, L<->R local et depot divergents. Resume final avec les compteurs par paire. README et GLOBAL_INDEX_REPO sont mis en correspondance local, racine prod et depot.

## A savoir

- Selon le skill ha-trigul, ce script est redondant avec `hermes_audit_trigul_arbres.py` depuis le 2026-10-18 (le trigul .md ne voyait que les `.md` et partait de la liste locale). Il ne faut plus le lancer ; le fichier reste en place et ne se supprime pas sans demande d'Eric.
- Pieges documentes dans l'en-tete : curl Windows n'ecrit pas dans `/tmp` (chemin Windows explicite via `cygpath`), fins de ligne CRLF (MD5 normalise), chemins a espaces et accents (encodage URL), ne pas toucher aux archives `historique/JOURNAL*` et `CLAUDE_backup*`.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture de l'en-tete du fichier source et du skill ha-trigul. Le statut "Actif" du badge est celui par defaut : a corriger si Eric classe ce script comme obsolete.
