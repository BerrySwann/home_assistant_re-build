# Skill ha-push-md - Push des seules fiches .md vers la prod

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
| Skill | `ha-push-md` |
| Appel | /ha-push-md (ou "pousse les md en prod") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_push_md/ha_push_md.md` |
| Skill installe | `.claude/skills/ha-push-md/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Version restreinte de `ha-push-docs` : elle ne pousse que les fichiers `*.md` de documentation (dashboard, automations, scripts YAML et SH) vers `H:\Docs`, apres comparaison MD5. Les `*.yaml` ne sont jamais touches ici.

## Les etapes

1. Controle des dossiers `XX_` avec `Check_XX_presents.py` avant ET apres le push (une ALERTE bloque tout push).
2. MD5 local et MD5 prod des `.md`, puis diff affiche avant de pousser.
3. Copie des seuls fichiers differents, puis verification MD5 finale.

## Regles cles

- Le local fait foi, `secrets.yaml` interdit, jamais d'ecrasement en masse.
- Les dossiers `XX_` n'existent qu'en local et ne se poussent jamais.
- Ne jamais modifier un `.md` directement sur `H:` : local d'abord, avec sauvegarde.

## Decisions datees

- 2026-10-25 : controle des dossiers `XX_` obligatoire.

## Points a verifier avec Eric

- Corrige le 2026-10-31 dans la copie anglaise : la regle sur `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` suit la decision du 2026-10-30 (il part en prod avec le push general de `/histo`, etape 5C).
- Reste a verifier : les chemins sources et les noms de dossiers cites par rapport a l'arborescence actuelle.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
