# Check_GLOBAL_INDEX.py - controle des index globaux (lecture seule)

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Check_GLOBAL_INDEX/Check_GLOBAL_INDEX.py` |
| Langage | Python 3 |
| Lance par | /histo (etape 6, point 8). Ne fait pas tourner Home Assistant |
| Ecrit | rien : il signale, il ne corrige pas |

## Role

Controle tous les index globaux. Pour chaque index : existence, liens casses (Markdown et href), equilibre `<details>` / `<blockquote>` (pour GLOBAL_INDEX_REPO), presence et MD5 en prod (`H:\`, lecture seule ; regle des 2 emplacements pour GLOBAL_INDEX_REPO), entites citees absentes de `core.entity_registry`, `core.restore_state` et des groupes YAML (index REPO et ENTITES). Les faux positifs connus sont ecartes par les listes `ENTITES_SYSTEME`, `ENTITES_NOTES` et `TYPES_NON_ENTITES`.

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Check_GLOBAL_INDEX.py
```

- Sortie : une ligne par index (`<nom>: liens=N casses=M prod=...`), puis la derniere ligne `controle global_index: index=N liens=N casses=N ecarts=N`.
- Si `H:` est inaccessible, le script le dit et ne controle ni la prod ni les entites.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture de l'en-tete et des sorties du fichier source.
