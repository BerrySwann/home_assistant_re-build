# Check_DEPENDANCES.py - controle de fraicheur de DEPENDANCES_GLOBALES_CLAUDE_memoire.md et IA_GLOBAL_INDEX_memoire.md (lecture seule)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--29-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Scripts-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/Check_DEPENDANCES/Check_DEPENDANCES.py` |
| Langage | Python 3 (bibliotheque standard seule) |
| Lance par | /histo (etape 6, point 12) et donc /histo-final. Ne fait pas tourner Home Assistant |
| Ecrit | rien : il rapporte les ecarts (code retour 0 = rien a signaler, 1 = ecarts) |

## Role

Demande d'Eric le 2026-10-29 : les deux fichiers memoire de Claude, qui servent a retrouver vite "le petit" en cas de souci, doivent etre IMPERATIVEMENT a jour. Le script controle, sans rien corriger :

1. `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` :
   - chaque automation de `H:\automations.yaml` doit avoir une section (recherche par nom d'alias, accents et prefixes ignores ; un nom different est signale "A VERIFIER", ce n'est pas une preuve d'absence) ;
   - les YAML de `docs/` (automations, scripts, dashboard, config) modifies apres la date de la ligne "Derniere mise a jour" en tete ;
   - `automations.yaml` modifie apres cette date ;
   - chemins `docs/...` cites entre accents graves qui n'existent plus (les lignes marquees retire, absent, introuvable ou supprime sont ignorees) ;
2. `IA_GLOBAL_INDEX_memoire.md` : fichier `.md` de `docs/00_IA` absent de l'index, ou modifie apres l'index (regenerer avec `Gen_GLOBAL_INDEX_ia.py`, jamais a la main).

Limites : les entites ne sont pas controlees en live (il faut HA, a faire par Claude via les outils HA) ; le contenu d'une section n'est pas compare a son YAML.

## Utilisation

```
$env:PYTHONIOENCODING='utf-8'; python -I Check_DEPENDANCES.py
```

Derniere ligne : `== RESULTAT : ecarts=N | OK` ou `| A TRAITER`.

## Quoi faire d'un ecart

DEPENDANCES : mettre a jour la section ou la ligne concernee (sauvegarde `.bak` avant, date en tete, ligne au journal des modifs), fichier local seul. Index : relancer `Gen_GLOBAL_INDEX_ia.py`.

## Origine de cette fiche

Creee le 2026-10-29 par Claude avec le script. Premier lancement : ecarts=0 apres regeneration de l'index.