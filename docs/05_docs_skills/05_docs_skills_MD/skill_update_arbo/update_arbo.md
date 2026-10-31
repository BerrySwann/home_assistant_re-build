# Skill update-arbo - Mise a jour des comptages de IA_ARBO_DETAIL.md

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
| Skill | `update-arbo` |
| Appel | /update-arbo (aussi "resync tree") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_update_arbo/update_arbo.md` |
| Skill installe | `.claude/skills/update-arbo/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Apres une session qui ajoute, supprime ou deplace des fichiers, le skill rafraichit les comptages et les informations de version dans `IA_ARBO_DETAIL.md` : comptages reels du local, de la prod `H:\docs` et de GitHub (dernier commit et arbre).

## Les etapes

1. Comptages reels du local par dossier, puis de la prod, puis dernier commit et arbre GitHub.
2. Remplacer par `.Replace()` strict seulement les lignes qui changent (dates de releve, comptages, nom du dernier Dashboard, commit).
3. Pousser vers `H:\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\`, avec MD5 local contre prod.
4. Resume `UPDATE_ARBO - [date]` avec les comptages.

## Regles cles

- Comptages reels uniquement, jamais d'estimation ni de valeur memorisee.
- Pas de regex ; ne pas modifier les sections narratives ; la grille a deux colonnes garde une largeur fixe.
- `secrets.yaml` interdit.
- "resync tree" dit par Eric = ce skill (constate le 2026-10-18), pas une copie GitHub vers local.

## Decisions datees

- 2026-10-18 : "resync tree" signifie update-arbo.

## Points a verifier avec Eric

- Corrige le 2026-10-31 dans la copie anglaise : la ligne `05_docs_skills` compte maintenant PURE, MD et `MOC_SKILLS.md`.
- Le bloc PROD de `IA_ARBO_DETAIL.md` garde l'ancienne structure jusqu'au prochain push de `/histo` (etape 5C).

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
