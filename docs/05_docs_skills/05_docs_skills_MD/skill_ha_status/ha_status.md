# Skill ha-status - Avancement du projet en 3 points

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--31-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Skill-ffeb3b?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Skill | `ha-status` |
| Appel | /status (ou "ou en est le projet") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_status/ha_status.md` |
| Skill installe | `.claude/skills/ha-status/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Resume ultra-compact de l'etat du projet : ce qui est fait, ce qui est en cours, ce qui suit, plus les blocages. Zero discours, pour economiser des tokens.

## Les etapes

1. Lire l'historique de la conversation, puis `docs\00_IA\`, puis les fichiers recents de `01_config_system_SH_PY_YAML`.
2. Repondre au format fixe : `[1] FAIT`, `[2] EN COURS`, `[3] SUIVANT`, puis `Blocages`.

## Regles cles

- Maximum 2 lignes par point.
- Utiliser les IDs de la matrice (L1C1, P2...) et des noms de fichiers courts.
- Ne jamais repeter du YAML deja poste.
- Rien de fait : `[1] FAIT : aucune modification validee dans cette session`.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
