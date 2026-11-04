# Push_5C.py - push general de l'etape 5C de /histo

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
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
Regle des garde-fous d'Eric du 2026-11-03 : un garde-fou protege une donnee, il ne doit jamais empecher sa propre reparation.
- Avant chaque ecrasement, l'ancienne version de prod est copiee dans `TEMPO\push_5C_L_vers_P_<AAAA-MM-JJ_HHhMMmSSs>\` (meme chemin relatif), MD5 verifie contre la prod d'origine. Copie non conforme : le fichier n'est PAS ecrase et il est signale.
- Prod differente qui ne correspond a aucun `.bak` local connu (prod modifiee hors circuit) : PROD INCONNUE, poussee quand meme avec un avertissement (avant le 2026-11-04 : non poussee). La copie TEMPO garde l'ancienne prod.
- Fichiers seuls en prod (SEUL_EN_PROD) : signales, jamais supprimes sans ordre d'Eric, et ils n'arretent plus le push (avant le 2026-11-04 : arret du mode `exec`, code 3).
- Purge (validee par Eric le 2026-11-04 a 19h57, alignement sur Hermes) : en mode `exec`, les dossiers `TEMPO\push_5C_L_vers_P_*` de plus de 7 jours (date lue dans le nom) partent a la corbeille Windows, jamais supprimes definitivement. Le mode `plan` les liste. Le reste de TEMPO reste vide par Eric seul.
- Code de retour 1 si un MD5 differe apres push ou si une copie de securite n'est pas conforme.

## Copie 98 automatique
En mode `exec`, le script lance d'abord `Sync_98_sauvegarde.py exec` : la copie de `Infra_Proxmox`, `TODO` et `historique` dans `docs\98_sauvegarde_hors_docs` est donc toujours a jour avant le push (ajoute le 2026-10-31).

## Qui l'utilise
L'etape 5C du skill `histo` (decide par Eric le 2026-10-30).

## Historique
- 2026-11-04 : regle des garde-fous du 2026-11-03 appliquee (copie TEMPO avant ecrasement, PROD INCONNUE poussee avec avertissement, SEUL_EN_PROD ne bloque plus), ordre d'Eric.
- 2026-10-31 : rangé dans le projet. Differences avec la version temporaire : date du dossier TEMPO automatique, liste des suppressions attendues remplacee par un arret si SEUL_EN_PROD non vide.

<!-- annotations_log: [2026-11-04] garde-fous alignes sur la regle d'Eric du 2026-11-03 (script et fiche) -->
<!-- annotations_log: [2026-11-04] purge TEMPO push_5C de plus de 7 jours vers la corbeille, validee par Eric -->
