# gen_moc_docs.py - genere MOC_AUTOMATIONS.md, MOC_SCRIPTS.md et MOC_SKILLS.md

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py` |
| Langage | Python 3 |
| Lance par | a la main (regle d'Eric du 2026-10-28 : 1 source = 1 fiche .md). Ne fait pas tourner Home Assistant |
| Ecrit | `docs/03_docs_automations/MOC_AUTOMATIONS.md`, `docs/04_docs_scripts/MOC_SCRIPTS.md`, `docs/05_docs_skills/MOC_SKILLS.md` |

## Role

Verifie, source par source, qu'une fiche .md existe, et ecrit les trois cartes. Lecture seule sur les sources.

Rapprochement source / fiche : nom normalise identique, sinon fiche qui cite le nom du fichier, sinon table `FORCE` (rattachement manuel valide par Eric), sinon fiche "candidate" (nom proche, `difflib` >= 0.5) proposee a validation et jamais comptee comme fiche OK.

Ignores : `.bak`, `XX_*`, `*_ORIGINAL`, `*_archive*`, `__pycache__`, `.pyc`.

## Particularites

- `MOC_AUTOMATIONS.md` : section "Documents annexes" pour les fiches dont le nom contient `P1_XX_` (references sans YAML, non comptees orphelines).
- `MOC_SCRIPTS.md` : deux groupes, "Home Assistant" (.sh, puis .py, puis .yaml) et "Audit interne" (scripts dont le nom commence par Audit, Check, Verif, Hermes_audit ou trigul_run ; ils ne font pas tourner Home Assistant). Tableaux HTML a colonnes de largeur fixe. Colonne "Appele par Home Assistant" = recherche du nom du fichier (ou de l'id du script) dans les YAML de la prod. Statut "Documente dans l'en-tete du fichier" quand l'en-tete a au moins 3 sections.
- `FORCE` : les trois routeurs clim `J_1_1`, `J_1_2`, `J_1_3` pointent vers la fiche `Scripts_clim_on_off`.

## Utilisation

```
python -I -X utf8 gen_moc_docs.py [--dry]
```

- `--dry` : n'ecrit rien.
- Sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.md` si le contenu change ; rien n'est ecrit si seule la ligne "Genere le" change.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source.
