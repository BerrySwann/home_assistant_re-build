# gen_moc_dashboard.py - genere MOC_DASHBOARD.md

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_dashboard/gen_moc_dashboard.py` |
| Langage | Python 3 |
| Lance par | a la main (regle d'Eric du 2026-10-28 : 1 YAML = 1 fiche .md). Ne fait pas tourner Home Assistant |
| Ecrit | `docs/02_docs_dashboard/MOC_DASHBOARD.md` (et rien d'autre) |

## Role

Pour chaque YAML de `docs/02_docs_dashboard/02_dashboard_docs_YAML` (.yaml et .yml), cherche sa fiche .md dans `02_dashboard_docs_MD` : meme nom (insensible a la casse et aux separateurs), sinon fiche de la meme cellule (puis de tout l'arbre) qui cite le nom du fichier YAML. Le resultat est la carte `MOC_DASHBOARD.md`.

Sont ignores : les sauvegardes `.bak`, les dossiers `XX_*`, `Dashboard_COMPLET`, `*_ORIGINAL` et `*_archive*`.

## Utilisation

```
python -I -X utf8 gen_moc_dashboard.py [--dry]
```

- `--dry` : n'ecrit rien.
- Sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.md` si le contenu change ; rien n'est ecrit si le contenu est identique.
- Lecture seule sur les sources.

## A savoir

- Le MOC n'est pas aligne sur le nouveau format de `MOC_SCRIPTS.md` (tableaux HTML, groupes). Aucun MOC n'est pousse en prod.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source. Rien n'a ete execute pour l'ecrire.
