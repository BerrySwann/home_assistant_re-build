# Recap_index.py - recapitulatif des entites en fin des index globaux

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

*Cree le 2026-11-04 sur ordre d'Eric (aligner les skills histo de Claude sur ceux d'Hermes) : copie de `recap_index.py` d'Hermes, rangee dans docs pour etre sous GitHub.*

## Role
Pose a la fin de 7 index globaux un bloc delimite (`<!-- RECAP-ENTITES:DEBUT -->` ... `<!-- RECAP-ENTITES:FIN -->`) qui compte les entites citees par `GLOBAL_INDEX_REPO.md` et donne l'origine de chacune : NAT (coeur de Home Assistant), HACS (dossier `H:\custom_components`), CREE (YAML du depot, famille = dossier qui declare l'objet), RASPI-PI4-4GO, SUPPRIMEE, ARTEFACT-TEMPLATE. Regle d'Eric du 2026-11-03.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\Recap_index\Recap_index.py`
- Original d'Hermes : `C:\Users\Berry Swann\AppData\Local\hermes\scripts\histo\recap_index.py`

## Lancement
- Essai sans ecriture : `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Recap_index\Recap_index.py" --dry`
- Ecriture : meme commande sans `--dry`.

## Ordre
A lancer APRES les generateurs `Gen_GLOBAL_INDEX_*` : un generateur reecrit son index en entier et efface le bloc. Le bloc est remplace a chaque passage, jamais edite a la main.

## Ce qu'il lit et ecrit
- Lit (lecture seule) : `H:\.storage\core.entity_registry`, `H:\.storage\core.config_entries`, `H:\custom_components`, les YAML de `01_config_system_SH_PY_YAML`.
- Ecrit : les 7 index, seulement si le bloc change, apres une sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.md` a cote (ajout de Claude, l'original d'Hermes ecrit sans sauvegarde) (GLOBAL_INDEX_REPO, ENTITES_GLOBAL_INDEX, GLOBAL_INDEX_AUTOMATIONS, GLOBAL_INDEX_VIGNETTES_PAGES, GLOBAL_INDEX_SCRIPTS_SH, GLOBAL_INDEX_SCRIPTS_YAML, IA_GLOBAL_INDEX_memoire). Rien sur H:.

## Qui l'utilise
L'etape 2 (sync_index) du skill `histo`, apres les generateurs.

## Historique
- 2026-11-04 : ajout d'une sauvegarde avant ecriture et d'aucune ecriture si le bloc est identique. Premier passage reel : 2 index modifies (SCRIPTS_SH et SCRIPTS_YAML, deja sauves par leur generateur), 5 identiques.
- 2026-11-04 : copie dans docs (md5 du fichier d'Hermes ecrit dans l'en-tete du script). Essai `--dry` du jour : 685 entites retenues, les 7 index trouves.