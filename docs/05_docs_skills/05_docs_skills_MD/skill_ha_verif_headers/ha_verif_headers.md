# Skill ha-verif-headers - Controle des en-tetes des YAML de config

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
| Skill | `ha-verif-headers` |
| Appel | /ha-verif-headers (ou "verifie les headers") |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_ha_verif_headers/ha_verif_headers.md` |
| Skill installe | `.claude/skills/ha-verif-headers/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Verifie en lecture seule qu'un YAML de `01_config_system_SH_PY_YAML` respecte les normes du CLAUDE.md : boites ASCII, 5 headers, slug tertiaire, `name` et `unique_id`. Complement de `ha-new-yaml`.

## Les etapes

1. Lancer `Verif_headers_yaml.py` (sans argument : tous les YAML ; avec un chemin : un fichier ou un dossier ; `--erreurs`, `--prefixe`).
2. Lire le resultat : ERREUR (structure, a corriger) et AVIS (convention, a juger avec Eric).
3. Compte rendu : ligne `controle verif_headers`, ERREUR par fichier, nombre d'AVIS par type.
4. Proposer la correction fichier par fichier, avec `.bak` avant, relance du controle et ligne au journal des modifs.

## Regles cles

- Lecture seule par defaut : rien n'est modifie sans ordre d'Eric.
- Une boite plus longue que 78 ou 37 caracteres est normale si le titre est long ; ne jamais tronquer un titre.
- Un AVIS n'est pas forcement une faute ; ne pas corriger en masse.
- Ne touche ni aux automations ni aux dashboards.

## Decisions datees

- 2026-10-20 : skill cree sur demande d'Eric.

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
