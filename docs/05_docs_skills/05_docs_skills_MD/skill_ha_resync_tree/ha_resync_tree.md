# Skill ha-resync-tree - Comparaison local / prod / GitHub en lecture seule

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
| Skill | `ha-resync-tree` |
| Appel | /ha-resync-tree (pas sur "resync tree") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_resync_tree/ha_resync_tree.md` |
| Skill installe | `.claude/skills/ha-resync-tree/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Ancien "resync GitHub vers local", retire le 2026-10-18 parce que le local fait foi. Le skill ne fait plus que comparer en lecture seule, avec `Verif_emplacements.py`, et analyser les ecarts. Quand tu dis "resync tree", c'est `update-arbo` qu'il faut lancer, pas celui-ci.

## Les etapes

1. Lancer `Verif_emplacements.py` (lecture seule).
2. Analyser : PROD DIFFERENTE DU LOCAL -> proposer `/ha-push-yaml` ; GITHUB EN ATTENTE DU BACKUP -> normal apres un push ; present en prod ou sur GitHub mais pas en local -> le signaler a Eric.
3. Copie vers le local seulement sur ordre explicite d'Eric, fichier par fichier, depuis la prod (pas depuis GitHub), avec `.bak` avant.
4. Automations et scripts YAML : comparaison unite par unite par `/ha-trigul`.

## Regles cles

- Lecture seule par defaut ; ne jamais ecraser un fichier local sans le signaler.
- `secrets.yaml` ne se copie jamais, dans aucun sens.
- Les `.md` ne sont jamais synchronises par ce skill (c'est `/ha-push-docs`).

## Decisions datees

- 2026-10-18 : retrait de l'ancien workflow GitHub vers local.
- 2026-10-20 : reprise de la procedure de l'ancien skill `ha-resync-docs`.

## Points a verifier avec Eric

- Corrige le 2026-10-31 dans la copie anglaise : le rapport est range dans `historique\03_RAPPORTS\06_MD5\03_VERIF_EMPLACEMENTS\`.
- Aucun autre point ouvert.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
