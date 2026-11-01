# XX_manifest.json - manifeste des dossiers et fichiers XX_ (local seul)

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

## Rôle

Liste de référence des dossiers `XX_*` de `docs` et des fichiers qu'ils contiennent (hors `.bak`). `Check_XX_presents.py` compare le disque à cette liste avant chaque push (ha-push-docs, ha-push-md, ha-push-yaml) : un dossier ou un fichier manquant = ALERTE, rien n'est poussé.

## Emplacement

- Fichier source : `docs\04_docs_scripts\04_docs_scripts_JSON\Check_XX_presents\XX_manifest.json`
- Déplacé le 2026-11-01 (ordre d'Eric) depuis `04_docs_scripts_SH\Check_XX_presents\`. Il reste dans ce dossier JSON : ne pas le déplacer, le renommer ni le régénérer.
- Contenu au 2026-11-01 : 8 dossiers XX_, 13 fichiers.
- Nom conservé `XX_manifest.json` : ce n'est pas un dossier XX_, il part en prod avec `docs` (étape 5C).

## Propriétaire et règles

- Propriété de Claude. Hermes ne le modifie pas.
- Mise à jour (`--maj` de `Check_XX_presents.py`) uniquement sur ordre d'Eric.
- Utilisé par : [Check_XX_presents.py](../../04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py) (constante `MANIFEST`), fiche : [Check_XX_presents.md](../../04_docs_scripts_SH_MD/Check_XX_presents/Check_XX_presents.md).

*Fin de la fiche*
