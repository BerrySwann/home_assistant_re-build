# Skill hermes-aligne - Alignement d'Hermes sur Claude (lecture seule)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Skill-ffeb3b?style=flat-square)](.)

| Champ | Valeur |
|:------|:-------|
| Skill | `hermes-aligne` |
| Appel | Eric dit "aligne-toi", "t'aligner", "alignement" a Hermes |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_hermes_aligne/hermes_aligne.md` (en francais, c'est le texte que lit Hermes) |
| Skill installe | `.claude/skills/hermes-aligne/SKILL.md` |
| Langue de la copie | francais |

## A quoi ca sert

Hermes lit les regles et les modifications de Claude, les assimile et se comporte ensuite comme lui. Il n'ecrit rien : ni fichier, ni dossier, ni git, ni script qui ecrit. Origine : l'incident du 2026-10-17 (suppression de `00_IA\sous_context_ia` pris pour un doublon sur un disque insensible a la casse).

## Les etapes

1. Hermes annonce "ALIGNEMENT en lecture seule".
2. Il lit, dans l'ordre : CLAUDE.md, IA_CONTEXT_BASE.md (deux fichiers distincts), l'index IA et les sous-contextes, les journaux MODIFS et les messages de Claude dans `C:\Users\Berry Swann\AppData\Local\hermes\Discussion_Claude_Hermes`, les skills de Claude (copies PURE, fiches, MOC_SKILLS).
3. Il retient les regles avec leurs exceptions (XX_, 99_, 98_, TEMPO et Groupe_A/B/C, manifeste, .bak, 8 badges, index par type).
4. Il rend un rapport court : sources lues, regles retenues, ecarts constates, sans rien corriger.

## Regles cles

- Zero ecriture pendant l'alignement. Seule exception (Eric, 2026-11-01) : un message PROPOSITION dans sa propre boite d'echanges pour donner une idee d'amelioration.
- Une regle se recopie avec son exception, sa date et son decideur, jamais en resume.
- En cas de doute : une question courte a Eric.

## Decisions datees

- 2026-10-17 : incident a l'origine du skill.
- 2026-10-18 : "s'aligner" = lire, jamais ecrire.
- 2026-11-01 : skill reecrit (chemins actuels, boite d'echanges, regles XX_/99_/98_, TEMPO) et exception PROPOSITION ajoutee.

## Points a verifier avec Eric

- Hermes a sa propre version du skill dans `C:\Users\Berry Swann\AppData\Local\hermes\skills\autonomous-ai-agents\hermes-aligne`, que le curateur de skills d'Hermes peut modifier sans nous ; elle n'est pas forcement identique a celle-ci.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour.

<!-- annotations_log: -->
<!-- [2026-11-01] Fiche creee : le skill n'en avait pas -->
<!-- annotations_log: [2026-11-04] chemins D: alignes sur AppData\Local\hermes -->
