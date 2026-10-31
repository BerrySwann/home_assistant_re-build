# Skill ha-push-docs - Push des docs locales vers la prod

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
| Skill | `ha-push-docs` |
| Appel | /ha-push-docs (ou "pousse les docs en prod") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_push_docs/ha_push_docs.md` |
| Skill installe | `.claude/skills/ha-push-docs/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Le skill synchronise la documentation locale (`*.md` et `*.yaml` de dashboard) vers `H:\docs`, en ne poussant que les fichiers dont le MD5 differe de la prod. La prod reproduit l'arborescence de `docs`.

## Les etapes

1. Calculer le MD5 local de tous les fichiers concernes, puis le MD5 prod.
2. Calculer le diff (NOUVEAU / DIFF) et l'afficher avant de pousser.
3. Mettre a jour la fiche `.md` de chaque YAML de dashboard modifie, avant le push (etape 3B).
4. Pousser seulement les fichiers differents, puis verifier le MD5 apres copie.
5. Cas particulier `GLOBAL_INDEX_REPO.md` et `README.md` : toujours pousses aux deux endroits (miroir docs ET racine `H:\`).

## Regles cles

- Le local fait foi, jamais d'ecrasement en masse, `secrets.yaml` interdit.
- Jamais de sauvegarde sur `H:` ni `D:` ; les `.bak` ne sont jamais pousses.
- `Dashboard_COMPLET` n'est jamais touche (ni copie, ni suppression).
- Le nettoyage des doublons Dashboard demande un dry-run et une confirmation, et passe par `TEMPO\` (pas de corbeille sur `H:`).
- Apres un push, lancer `Verif_emplacements.py`.

## Decisions datees

- 2026-10-13 : cas des deux destinations pour `GLOBAL_INDEX_REPO` et `README`.
- 2026-10-18 : controle apres push par `Verif_emplacements.py`.
- 2026-10-30 : `/histo` pousse aussi tout `docs` en prod (etape 5C) ; ce skill reste l'outil manuel.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
