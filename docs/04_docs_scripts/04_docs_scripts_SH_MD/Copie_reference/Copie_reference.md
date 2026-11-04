# Copie_reference.py - copies de reference de automations.yaml, scripts.yaml et configuration.yaml

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Opus_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

*Cree le 2026-11-04 sur ordre d'Eric (aligner les skills histo de Claude sur ceux d'Hermes) : copie de `copie_reference.py` d'Hermes, rangee dans docs pour etre sous GitHub.*

## Role
Regle d'Eric du 2026-11-02 : avant le push 5C, garder en local une copie de reference des trois fichiers maitres de la prod.
- `H:\automations.yaml` -> copie datee `automations.bak_<horodatage>.yaml` dans `03_docs_automations\03_docs_automations_YAML\Automations_yaml_original\`
- `H:\scripts.yaml` -> copie datee `scripts.bak_<horodatage>.yaml` dans `04_docs_scripts\04_docs_script_ORIGINAL\`
- `H:\configuration.yaml` -> fichier de travail stable `01_config_system_SH_PY_YAML\configuration.yaml`, l'ancien est d'abord sauve avec sa vraie date.

Un fichier non date de ces dossiers est renomme avec sa VRAIE date de modification, jamais la date du jour. Copie deja identique : rien n'est ecrit.

## Le MD5 est une barriere
MD5 different apres copie : la copie est retiree, le script s'arrete (code 1) et ecrit `ALERTE A ENVOYER PAR CLAUDE`. Claude envoie alors lui-meme la notification au telephone (`notify.mobile_app_eric`) et dans HA (`persistent_notification.create`).

## Difference avec l'original d'Hermes
L'original lit le jeton HA dans le `.env` d'Hermes pour envoyer l'alerte. Cette copie ne lit aucun jeton : elle ecrit la ligne d'alerte, et c'est Claude qui notifie.

## Emplacement et lancement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\Copie_reference\Copie_reference.py`
- `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Copie_reference\Copie_reference.py"`
- Aucune ecriture sur H: : c'est le push 5C qui porte les copies vers `H:\docs`.

## Qui l'utilise
L'etape 5C du skill `histo`, juste avant `Push_5C.py`.

## Historique
- 2026-11-04 : copie dans docs, alerte remplacee par une ligne lue par Claude. Pas encore lance par Claude.