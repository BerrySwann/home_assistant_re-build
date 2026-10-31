# Sync_98_sauvegarde.py - copie des dossiers hors docs vers la prod

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

*Cree le 2026-10-31 sur ordre d'Eric : Infra_Proxmox, TODO et historique doivent etre sous GitHub, dans un dossier sous docs qui commence par 98.*

## Role
Copie `Infra_Proxmox`, `TODO` et `historique` (qui sont a la racine de ReBuild, hors `docs`) vers `docs\98_sauvegarde_hors_docs\`. Le push general (5C) les envoie ensuite en prod, puis GitHub par le backup HA. Les originaux restent a la racine, la copie est a refaire (mode `exec`) avant chaque 5C.

## Emplacement
- Script : `docs\04_docs_scripts\04_docs_scripts_SH\Sync_98_sauvegarde\Sync_98_sauvegarde.py`
- Destination : `docs\98_sauvegarde_hors_docs\Infra_Proxmox`, `\TODO`, `\historique`

## Lancement
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Sync_98_sauvegarde\Sync_98_sauvegarde.py" plan` (lecture seule) puis `exec`.

## Ce qui n'est pas copie
- `.bak`, `.avant_*`, `.racine_avant_*`, `__pycache__`, `#...#`, `secrets.yaml`.
- `Infra_Proxmox\docs\sonoff\SONOFF_STATUS_2026-05-23.md` : contient un mot de passe en clair (decision de Claude le 2026-10-31, a valider par Eric).
- Dans la copie, les jetons GitHub `ghp_...` (debuts de jetons cites dans les journaux) sont remplaces par `ghp_***`. Les originaux ne sont pas modifies.

## Regles liees
- Le dossier 98_ est ignore par `Check_badges_fiches`, `gen_moc_docs` et `gen_moc_dashboard` (copies de sauvegarde, pas des fiches).
- Il part en prod avec le 5C (il n'est pas XX_ ni 99_).
- Ne jamais corriger un fichier dans la copie 98 : on corrige l'original puis on relance le script.
