# Skill ha-update-check-cli - Analyse avant mise a jour HA, sans MCP

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
| Skill | `ha-update-check-cli` |
| Appel | /ha-update-cli |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_update_check_cli/ha_update_check_cli.md` |
| Skill installe | `.claude/skills/ha-update-check-cli/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Analyse les mises a jour HA en attente quand les outils MCP ne sont pas disponibles (Claude Code en ligne de commande). Le skill lit les changements, les croise avec ta config reelle par grep et sort un top court : quoi faire avant, ce qui va casser, quoi faire apres. Il n'installe rien.

## Les etapes

1. Versions : core installee lue dans `H:\.HA_VERSION`, core disponible par l'API GitHub, cartes et integrations HACS demandees a Eric.
2. Lire les notes de version de toutes les versions sautees (breaking changes, options renommees, suppressions).
3. Croiser par grep avec la config locale et la prod ; ce qui n'est pas verifie reste "non verifie".
4. Pieges ReBuild a verifier systematiquement (token API 403, `parseFloat`, cartes custom, `mqtt.publish`...).
5. Verdict par mise a jour : INSTALLER ou BLOQUER, puis le rapport court.

## Regles cles

- N'installe jamais : Eric installe depuis l'interface HA apres sauvegarde (ordre conseille : cartes HACS, integrations HACS, apps, core, OS).
- Chaque fait precis est qualifie : etabli, deduit ou inconnu ; jamais de compatibilite devinee.
- Si les outils MCP HA sont disponibles, utiliser plutot `ha-update-check`.

## Decisions datees

- 2026-10-13 : liste des pieges ReBuild donnee par Eric.

## Points a verifier avec Eric

- L'etape 4 (detail des pieges) et l'etape 6 (checklist post-MAJ en 14 points) sont marquees "A COMPLETER par Eric" dans le skill, toujours ouvertes au 2026-10-31.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
