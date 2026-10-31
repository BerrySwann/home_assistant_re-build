# Gen_GLOBAL_INDEX_vignettes_pages.py - genere GLOBAL_INDEX_VIGNETTES_PAGES.md

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_vignettes_pages/Gen_GLOBAL_INDEX_vignettes_pages.py` |
| Langage | Python 3 |
| Lance par | /histo (etape 2, point 9) ou a la main. Ne fait pas tourner Home Assistant |
| Ecrit | `docs/02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md` (et rien d'autre) |

## Role

Index des vignettes (LxCy) et des pages du dashboard, construit depuis l'arbre local `docs/02_docs_dashboard` (`02_dashboard_docs_MD` et `02_dashboard_docs_YAML`) et `DEPENDANCES_GLOBALES_CLAUDE_memoire.md`. Lecture seule sur tout sauf la sortie. `Dashboard_COMPLET` n'est jamais lu ni modifie.

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Gen_GLOBAL_INDEX_vignettes_pages.py [--dry]
```

- `--dry` : n'ecrit rien.
- Sortie console : `liens=N casses=M` (casses doit valoir 0), puis `ecrit : <fichier> (N lignes)`.
- Copie `.bak_AAAA_MM_JJ_HHhMMmSSs.md` avant ecrasement si le contenu change.

## A savoir

- Ne jamais modifier `GLOBAL_INDEX_VIGNETTES_PAGES.md` a la main.
- Vignettes sans fiche ou sans YAML, dossiers presents d'un seul cote et vignettes sans dependances sont a signaler dans le rapport de /histo.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source. Rien n'a ete execute pour l'ecrire.
