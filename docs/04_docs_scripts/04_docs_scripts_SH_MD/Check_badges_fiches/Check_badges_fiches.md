# Check_badges_fiches.py - controle des badges des fiches .md

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-En%20cours-0f9d58?style=flat-square)](.)&nbsp;
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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Check_badges_fiches/Check_badges_fiches.py` |
| Langage | Python 3 |
| Lance par | a la main, puis par /histo et /histo-final (pas encore branche : en attente de la validation d'Eric) |
| Ecrit | rien par defaut ; avec `--fix`, ajoute les badges manquants aux fiches (copie `.bak` a cote) |

## Role

Controle la regle des 8 badges de CLAUDE.md sur toutes les fiches `.md` de `docs/` (ordre : Statut, MàJ, HA, IA Partner, Source, Modifs, Expert, Type). Signale : fiche sans banniere, badge manquant, valeur hors liste, gabarit non rempli. Exemptes : `.bak`, `XX_*`, `*_ORIGINAL`, `*_archive*`, `MOC_*`, `GLOBAL_INDEX_*`, `docs/00_IA`, `docs/05_docs_skills`.

## Utilisation

```
python -I -X utf8 Check_badges_fiches.py [--chemin SOUS_DOSSIER] [--fix] [--limite N]
```

- Sans `--fix` : lecture seule. Derniere ligne `controle badges: fiches=N conformes=N a_corriger=N a_decider=N corrigees=N` ; code 1 s'il reste des fiches a corriger.
- `--fix` : cree les badges manquants, jamais de modification d'un badge existant. Valeurs automatiques : HA lu en live dans `H:\.HA_VERSION`, MàJ = date du jour, IA Partner `Claude_Sonnet_5.5`, Source `Interne`, Modifs `Autorisees`, Expert `HAOS_Proxmox`, Type `Scripts` pour les fiches de `04_docs_scripts`.
- Statut, et Type hors `04_docs_scripts`, ne sont jamais devines : la fiche est listee `a_decider`.
- Une fiche dont les badges sont hors d'un bloc `<div align="center">` n'est pas corrigee (forme a revoir a la main).

## Etat

- Cree le 2026-10-28. Premier controle en lecture seule sur `04_docs_scripts` : 30 fiches, 17 conformes, 13 a corriger. `--fix` pas encore essaye.

## Origine de cette fiche

Creee le 2026-10-28 par Claude (ordre d'Eric 21:03).