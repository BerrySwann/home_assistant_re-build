# Check_XX_presents.py - controle de presence des dossiers XX_

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-ff9800?style=flat-square)](.)

</div>

*Cree le 2026-10-25 21:21 sur ordre d'Eric (21:19) : les dossiers XX_ n'existent qu'en local et ne doivent jamais se perdre.*

## Role
Compare les dossiers `XX_` de `docs` (et les fichiers qu'ils contiennent, hors `.bak`) au manifeste `XX_manifest.json` rangé à côté du script. Lecture seule.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py`
- Manifeste : `docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\XX_manifest.json` (7 dossiers XX_, 20 fichiers au 2026-10-25)
- Copie de sécurité : `TEMPO\XX_sauvegarde_2026-10-25` (78 fichiers, md5 vérifiés, `.bak` compris)

## Lancement
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"`

- Code 0 et `RESULTAT : OK` : tout est là.
- Code 1 : ALERTE, dossier ou fichier manquant. Ne rien pousser, prévenir Eric, restaurer depuis TEMPO sur son ordre.
- `INFO nouveau ...` : un dossier ou fichier XX_ n'est pas encore au manifeste (pas bloquant).
- `--maj` : réécrit le manifeste, seulement sur ordre d'Eric.

## Qui l'utilise
Les skills `ha-push-docs`, `ha-push-md` et `ha-push-yaml` (étape "Avant tout push") et les skills équivalents de Hermes. La règle est dans CLAUDE.md (règle XX_, contrôle de présence).
## Version fusionnee (2026-10-25, Claude + Hermes, directive d Eric 21:29)

- Outil unique : decouverte recursive des dossiers XX_ (un XX_ imbrique dans un autre compte separement), manifeste fichier par fichier, .bak exclus, INFO sur un nouveau XX_ ou un nouveau fichier.
- Ajoute par Hermes : alerte si un dossier XX_ existe en prod (H:\docs), controle a lancer AVANT et APRES chaque push, option --quiet (une ligne), option --json.
- Codes de retour : 0 = OK, 1 = ALERTE (ne rien pousser, prevenir Eric), 2 = manifeste absent.
- Manifeste XX_manifest.json (meme dossier) : propriete de Claude ; --maj uniquement sur ordre d Eric.
- Copie maitre : ce dossier. Les skills de Claude et de Hermes appellent ce chemin.
