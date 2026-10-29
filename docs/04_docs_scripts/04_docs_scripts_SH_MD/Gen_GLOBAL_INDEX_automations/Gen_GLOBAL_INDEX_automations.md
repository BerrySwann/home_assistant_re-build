# Gen_GLOBAL_INDEX_automations.py - genere GLOBAL_INDEX_AUTOMATIONS.md

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Gen_GLOBAL_INDEX_automations/Gen_GLOBAL_INDEX_automations.py` |
| Langage | Python 3 (module `yaml` requis) |
| Lance par | /histo (etape 2, point 8) ou a la main. Ne fait pas tourner Home Assistant |
| Ecrit | `docs/03_docs_automations/GLOBAL_INDEX_AUTOMATIONS.md` (et rien d'autre) |

## Role

Genere l'index global des automatisations. Source de verite : `H:\automations.yaml` (prod) et le registre Home Assistant (`H:\.storage\core.entity_registry` et `core.category_registry` : entity_id et categorie). Il croise ces donnees avec les YAML locaux (`03_docs_automations_YAML`) et les fiches (`03_docs_automations_MD`). Lecture seule sur la prod. Le dossier `AUTOMATIONS_YAML_ORIGINAL` est ignore.

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Gen_GLOBAL_INDEX_automations.py [--dry]
```

- `--dry` : n'ecrit rien, affiche seulement le resume des ecarts.
- Avant d'ecraser la sortie, le script en fait une copie `.bak_AAAA_MM_JJ_HHhMMmSSs` a cote, uniquement si le contenu change.
- Sortie console : `liens=N casses=M`, puis `ecrit : <fichier> (N lignes, K ecarts)`. `casses` doit valoir 0.
- Si la prod n'est pas lisible, le script s'arrete avec le code 2 (le skill /histo demande de le noter sans bloquer).

## A savoir

- Ne jamais modifier `GLOBAL_INDEX_AUTOMATIONS.md` a la main : il est regenere.
- Un ecart nouveau (automation sans YAML, sans fiche, sans entite, id different, erreur YAML) se signale a Eric, il ne se corrige pas sans demande.
- Le skill /histo cite encore l'ancien chemin en minuscules (`gen_global_index_automations/gen_global_index_automations.py`) alors que le fichier s'appelle `Gen_GLOBAL_INDEX_automations.py`.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source (en-tete et sorties). Rien n'a ete execute pour l'ecrire.
