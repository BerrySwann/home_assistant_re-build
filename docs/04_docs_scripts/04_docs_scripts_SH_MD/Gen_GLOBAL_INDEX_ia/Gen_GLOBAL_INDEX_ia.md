# Gen_GLOBAL_INDEX_ia.py - genere GLOBAL_INDEX_IA.md

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_ia/Gen_GLOBAL_INDEX_ia.py` |
| Langage | Python 3 |
| Lance par | /histo (etape 2, point 11) ou a la main. Ne fait pas tourner Home Assistant |
| Ecrit | `docs/00_IA/GLOBAL_INDEX_IA.md` (et rien d'autre) |

## Role

Liste tous les fichiers de `docs/00_IA` (`00_IA_CONTEXT_BASE/` et `00_SOUS_CONTEXT_IA/*/`) : qui s'en sert, a quoi ils servent, quand les lire, avec les liens, le MD5 en prod et un resume des `.bak` par dossier. Lecture seule sur la prod (`H:\docs\00_IA`) et sur `CLAUDE.md`.

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Gen_GLOBAL_INDEX_ia.py [--dry]
```

- Les descriptions (qui / but / quand) sont dans le dictionnaire `DESC` du script. Un fichier sans description est signale : il faut le lire, ajouter son entree dans `DESC` (apres sauvegarde du script) puis relancer. Ne jamais inventer une description.
- `IA_SKILLS_INVENTAIRE` est dans `NON_POUSSES` (pas en prod tant qu'Eric ne le demande pas).
- Sortie console : `liens=N casses=M sans_description=K`. `casses` et `sans_description` doivent valoir 0.
- Copie `.bak_AAAA_MM_JJ_HHhMMmSSs.md` avant ecrasement si le contenu change.

## A savoir

- Ne jamais modifier `GLOBAL_INDEX_IA.md` a la main.
- Le skill /histo cite encore l'ancien chemin en minuscules (`gen_global_index_ia/gen_global_index_ia.py`).

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source. Rien n'a ete execute pour l'ecrire.
