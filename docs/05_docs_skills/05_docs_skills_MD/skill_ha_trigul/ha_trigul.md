# Skill ha-trigul - Triangulation des docs : local, prod, GitHub

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
| Skill | `ha-trigul` |
| Appel | /trigul (ou "triangulation", "audit md5 des docs") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_trigul/ha_trigul.md` |
| Skill installe | `.claude/skills/ha-trigul/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Trois controles enchaines, en lecture seule, qui comparent la documentation entre le local (ReBuild, qui fait foi), la prod `H:` et GitHub. Les rapports sont ranges dans `historique\03_RAPPORTS\06_MD5\`, un sous-dossier numerote par type.

## Les etapes

1. Lancement par le lanceur `trigul_run.py`, qui ecrit un journal de trace et controle chaque script (code de retour, rapport absent ou ancien, marqueurs de fin).
2. A. Superposition des 3 arbres : chemins en trop ou manquants (avec leur origine), differences de casse, contenu different, pour `.md .yaml .sh .py .svg .js`.
3. B. Etape profonde : automations et scripts YAML compares unite par unite entre la prod et le local, puis categories HA.
4. C. Fichiers a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) sur 5 emplacements, avec `Verif_emplacements.py`.
5. Compte rendu : les lignes ECHEC et ATTENTION du journal d'abord, puis les ecarts.

## Regles cles

- Le local fait foi : un ecart local/prod veut dire prod en retard ; un ecart prod/GitHub veut dire GitHub en retard (alimente par le backup HA, jamais de push direct).
- Le skill ne modifie, ne pousse et ne corrige rien ; il n'ecrit que ses rapports.
- Il doit tourner sur le PC lie (sans liaison, `H:` et GitHub ne sont pas accessibles).
- Piege de la casse : `H:` est un partage insensible a la casse ; changer une casse en prod demande un renommage explicite.
- Un ECHEC ne se corrige pas sans demande.

## Decisions datees

- 2026-10-11 : etape profonde automations et scripts.
- 2026-10-18 : superposition des 3 arbres en python, lanceur avec journal de trace, controle des 5 emplacements.
- 2026-10-20 : integration de l'ancien skill `ha-resync-docs`.
- 2026-10-25 : extensions controlees limitees a `.md .yaml .sh .py .svg .js`.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
