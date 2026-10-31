# Push_5C.py - push general de l'etape 5C de /histo

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

*Cree le 2026-10-31 sur ordre d'Eric : tout ce qui sert doit etre sous GitHub. Avant, ce script n'existait que dans le dossier temporaire du PC.*

## Role
Compare `docs` (local, source de verite) a `H:\docs` (prod) et pousse ce qui manque ou a change, avec MD5 avant et apres. GitHub suit par le backup HA.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\Push_5C\Push_5C.py`

## Lancement
- Plan (lecture seule, defaut) : `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Push_5C\Push_5C.py" plan`
- Execution : meme commande avec `exec`. Lancer `Check_XX_presents.py` avant et apres.

## Ce qui n'est jamais pousse
Dossiers `XX_`, `99_docs_MD_system` (sauf `ENTITES_GLOBAL_INDEX\ENTITES_GLOBAL_INDEX.md`), `.bak`, `secrets.yaml`, `*.pyc`, `#...#`, `__pycache__`, `Dashboard_COMPLET`, dossiers `_archive_` / `ARCHIVE`.

## Garde-fous
- Un fichier different en prod n'est ecrase que si la prod (badges retires) est identique a un ancien `.bak` local connu. Sinon : PROD DIFFERENTE INCONNUE, non pousse, signale.
- Fichiers seuls en prod (SEUL_EN_PROD) : le mode `exec` s'arrete (code 3), aucune suppression sans ordre d'Eric. Pour les supprimer : copie dans `TEMPO\miroir_5C_AAAA-MM-JJ` + MD5, puis suppression, a faire a part.

## Qui l'utilise
L'etape 5C du skill `histo` (decide par Eric le 2026-10-30).

## Historique
- 2026-10-31 : rangé dans le projet. Differences avec la version temporaire : date du dossier TEMPO automatique, liste des suppressions attendues remplacee par un arret si SEUL_EN_PROD non vide.
