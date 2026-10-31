# Skill ha-new-yaml - Generation d'un squelette YAML conforme

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
| Skill | `ha-new-yaml` |
| Appel | /ha-new-yaml (ou "cree un nouveau fichier YAML") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_new_yaml/ha_new_yaml.md` |
| Skill installe | `.claude/skills/ha-new-yaml/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Le skill cree un fichier YAML vide mais entierement conforme aux conventions du projet : boites ASCII, 5 headers obligatoires, slug tertiaire, `name` et `unique_id` coherents. Il couvre sensors, templates, utility_meter et command_line, jamais les automations.

## Les etapes

1. Poser les questions : pole (P0 a P4, M, A, S, MP), type de fichier, piece, nom fonctionnel, entites sources, aval.
2. Generer le fichier avec la bordure principale (coins arrondis, 78 caracteres) et les bordures secondaires (coins carres, 37 caracteres).
3. Ecrire les 5 headers : DESCRIPTION, CALCUL & SOURCES, CHAINE DE DEPENDANCES (tableau), IMPORTANT (PIEGES), TABLEAU DE BORD.
4. Placer le fichier dans le bon dossier de `01_config_system_SH_PY_YAML`, puis lancer `/ha-verif-headers` et proposer `/sync_index`.

## Regles cles

- Nommage `P{N}_TYPE_NOM.yaml` (suffixe AMHQ si multi-cycles), voir `IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md`.
- Une boite plus longue que 78 est permise si le titre est long ; ne jamais tronquer.
- La mise en prod se fait avec `/ha-push-yaml` (racine `H:\` ET miroir docs).

## Decisions datees

- 2026-10-18 : renvoi vers `Verif_emplacements.py`.
- 2026-10-20 : lien avec `/ha-verif-headers` apres generation.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
