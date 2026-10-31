# Gen_GLOBAL_INDEX_scripts.py - genere GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_scripts/Gen_GLOBAL_INDEX_scripts.py` |
| Langage | Python 3 (module `yaml` requis) |
| Lance par | /histo (etape 2, point 10) ou a la main. Ne fait pas tourner Home Assistant |
| Ecrit | `GLOBAL_INDEX_SCRIPTS_SH.md` et `GLOBAL_INDEX_SCRIPTS_YAML.md`, a la racine de `docs/04_docs_scripts` |

## Role

Index des scripts SH (programmes bash et python) et des scripts YAML (scripts Home Assistant). Sources : l'arbre local `04_docs_scripts_SH`, `04_docs_scripts_YAML` et leurs dossiers `_MD`, plus la prod en lecture seule : `H:\scripts.yaml`, `H:\automations.yaml`, `H:\shell_command`, `H:\.scripts` et le registre Home Assistant (entity_registry).

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Gen_GLOBAL_INDEX_scripts.py [--dry]
```

- Sortie console : une ligne `<index> : liens=N casses=M` puis `<index> : ecrit` pour chacun des deux fichiers. `casses` doit valoir 0.
- Copie `.bak_AAAA_MM_JJ_HHhMMmSSs.md` avant ecrasement si le contenu change.
- Le script ne pousse rien en prod. Un script de `H:\.scripts` ne se pousse jamais sans ordre d'Eric.

## A savoir

- Ne jamais modifier les deux index a la main.
- Il ne remplace pas `MOC_SCRIPTS.md` : celui-ci est genere par `gen_moc_docs.py` (regle 1 source = 1 fiche).

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source. Rien n'a ete execute pour l'ecrire.
