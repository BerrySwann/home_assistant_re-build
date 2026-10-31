# Skill ha-push-yaml - Push des YAML de config vers la prod HA

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
| Skill | `ha-push-yaml` |
| Appel | /ha-push-yaml (ou "pousse le yaml en prod") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_push_yaml/ha_push_yaml.md` |
| Skill installe | `.claude/skills/ha-push-yaml/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Operation critique : le skill pousse des YAML de `01_config_system_SH_PY_YAML` vers la prod, aux deux emplacements (racine `H:\` et miroir `H:\docs`), avec une logique MD5 d'abord : si le fichier est identique en prod, rien n'est pousse.

## Les etapes

1. Controle des dossiers `XX_` avant le push.
2. Sauvegarde locale du fichier existant avant toute modification.
3. MD5 local, puis MD5 prod aux deux emplacements, puis comparaison.
4. Checks avant push et confirmation explicite d'Eric.
5. Push, verification MD5 finale, puis rechargement de HA.

## Regles cles

- MD5 d'abord, confirmation obligatoire avant tout push, `secrets.yaml` interdit, `automations.yaml` uniquement par l'interface HA.
- Jamais de sauvegarde en prod ni sur `D:` ; 10 `.bak` horodates au plus le jour meme, 3 `.bak_AAAA_MM_JJ` au plus par jour passe.
- La prod ne recoit jamais un nom avec suffixe `.bak_`.
- Aplatissement : les scripts `.sh` et `.py` vont a plat dans `H:\.scripts\` (sans les sous-dossiers `01_scripts.sh` et `02_scripts.py`).
- Prod seule : `themes/`, `blueprints/`, `notifs/`, `scenes.yaml`, `ip_bans.yaml`, `secrets.yaml`.
- En cas d'ambiguite sur le fichier a pousser, prendre le plus recent.

## Decisions datees

- 2026-10-08 : regle de sauvegarde (10 + 3).
- 2026-10-18 : deux destinations en prod (racine et miroir).
- 2026-10-25 : controle des dossiers `XX_`.
- 2026-10-29 : regle d'aplatissement, ordre d'Eric.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
