# Check_yaml_forme.py - controle de forme des YAML de configuration (version rangee dans 04_docs_scripts_YAML)

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
| Source | `docs/04_docs_scripts/04_docs_scripts_YAML/Check_yaml_forme/Check_yaml_forme.py` (85 lignes) |
| Langage | Python 3 |
| Lance par | a la main. Ne fait pas tourner Home Assistant |
| Ecrit | rien : une ligne par anomalie sur la sortie standard |

## Role

Controle de forme des YAML de configuration Home Assistant (recupere le 2026-09-29 depuis l'ancien WORKFLOW_REBUILD.md, dossier passe en argument). Trois controles :

1. en-tete secondaire colle (`#|`, `#+` au lieu de `# |`, `# +`) : anomalie `ENTETE_COLLE` ;
2. boites ASCII dont le haut, le titre et le bas n'ont pas la meme largeur : `BOITE_DECALEE` ;
3. reference obsolete `P3_01_somme_par_piece` (renommee `P3_POWER_2_TOTAL_MULTI_ZONE`), hors journal `# annotations_log:` : `REF_OBSOLETE`.

Un fichier illisible est signale `ILLISIBLE`.

## Utilisation

```
python check_yaml_forme.py [dossier]
```

Defaut : `docs/01_docs_config_system/01_config_system_SH_PY_YAML` du dossier ReBuild. Derniere ligne `RESULTAT : <dossier> - aucune anomalie` (code 0) ou `RESULTAT : <dossier> - N anomalie(s)` (code 1) ; code 2 si le dossier est introuvable.

## A savoir

- C'est un `.py` range dans l'arbre des scripts YAML (ecart de rangement, a decider avec Eric).
- Il existe une autre version, plus longue (96 lignes, MD5 `65ee52a4` au 2026-10-28), dans `01_docs_config_system/01_config_system_SH_PY_YAML/.scripts/02_scripts.py/` et en prod ; sa fiche est `01_docs_config_system/01_config_system_MD/.scripts/02_scripts.py_md/Check_yaml_forme.md`. La version de cette fiche n'a pas les controles supplementaires (en-tete secondaire et DATE_NOM, d'apres la difference de taille ; non relu ligne a ligne).

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du fichier source.
