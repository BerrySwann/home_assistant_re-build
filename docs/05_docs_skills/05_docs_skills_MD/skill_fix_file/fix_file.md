# Skill fix-file - Correcteur YAML Home Assistant

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
| Skill | `fix-file` |
| Appel | /fix_file |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_fix_file/fix_file.md` |
| Skill installe | `.claude/skills/fix-file/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Tu colles une erreur Home Assistant (log, trace, message de l'interface) ou un bloc YAML qui plante. Le skill identifie le fichier et le type d'erreur, applique les regles du projet et renvoie uniquement le bloc corrige, avec une annotation par ligne modifiee. Il ne renvoie pas le fichier complet sauf demande.

## Les etapes

1. Identifier le fichier source (sensors, templates, utility_meter, command_line), le type d'erreur et le bloc precis ; lire le fichier local avant de corriger.
2. Appliquer les regles du projet : bordure ASCII de 78 caracteres, slug tertiaire `# --- unique_id ---`, `name` avec majuscules et prefixe de pole, `unique_id` en minuscules et underscores.
3. Repondre au format `[NOM_FICHIER] - [TYPE ERREUR]`, bloc corrige, puis bloc `# annotations_log:`.
4. Signaler l'impact possible sur une vignette (`/sync_index` recommande).

## Regles cles

- `notify.file` est interdit : remplacer par `notify.file_diag_log_file`.
- La correction se fait en local ; la mise en prod passe par `/ha-push-yaml`.
- Ne jamais renvoyer le fichier entier sans demande.

## Decisions datees

- 2026-10-18 : renvoi vers `Verif_emplacements.py` pour les fichiers a plusieurs emplacements.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
