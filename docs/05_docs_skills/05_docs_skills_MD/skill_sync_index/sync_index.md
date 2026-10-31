# Skill sync-index - Mise a jour des index et des dependances

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
| Skill | `sync-index` |
| Appel | /sync_index |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_sync_index/sync_index.md` |
| Skill installe | `.claude/skills/sync-index/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Apres validation d'un fichier YAML (config, automation ou script), le skill met a jour la documentation de dependances pour garder le projet coherent : `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` et la fiche `.md` de l'automation ou du script.

## Les etapes

1. Identifier le type (config, automation, script), le `unique_id` ou alias, le fichier source et les vignettes concernees.
2. Mettre a jour `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` (statuts, colonnes vides, date en tete) si une config ou une vignette est impactee.
3. Verifier ou mettre a jour la fiche `.md` de l'automation ou du script ; signaler une fiche absente.
4. Repondre au format `SYNC_INDEX - [date]` avec la liste des mises a jour.

## Regles cles

- Ne reecrire que les lignes concernees, jamais le fichier complet.
- Aucune dependance impactee : repondre "Index deja a jour - aucune action".
- Les chemins cites doivent avoir la casse exacte du disque (GitHub distingue la casse).

## Decisions datees

- 2026-10-18 : regle de la casse des chemins (resync).

## Points a verifier avec Eric

- Corrige le 2026-10-31 dans la copie anglaise : le fichier d'index est `docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\DEPENDANCES_GLOBALES_CLAUDE_memoire.md`.
- Aucun autre point ouvert.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
