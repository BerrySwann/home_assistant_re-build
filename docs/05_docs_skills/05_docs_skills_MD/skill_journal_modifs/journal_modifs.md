# Skill journal-modifs - Journal des modifications par auteur

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
| Skill | `journal-modifs` |
| Appel | automatique apres chaque ecriture, et au debut de session |
| Copie utilisable | `docs/05_docs_skills/05_docs_skills_PURE/skill_journal_modifs/journal_modifs.md` |
| Skill installe | `.claude/skills/journal-modifs/SKILL.md` |
| Langue de la copie | anglais (traduit le 2026-10-31) |

## A quoi ca sert

Chaque agent (Claude, Hermes) note une ligne par fichier modifie, au moment de la modification, dans son propre fichier du jour. L'autre agent le lit au debut de sa session. Cree pour eviter les modifications sans trace ni auteur.

## Les etapes

1. Apres chaque ecriture reussie (creation, modification, renommage, deplacement, suppression, copie, push), ajouter une ligne en fin de fichier.
2. Format : `date heure | auteur | ACTION | chemin | avant=MD5 apres=MD5 | raison`.
3. Au-dela de 10 fichiers dans une meme operation : une seule ligne LOT avec le chemin d'un rapport detaille.
4. Debut de session : lire les journaux du jour et de la veille, chercher les modifications non journalisees et les presenter avant de commencer.

## Regles cles

- Fichier maitre local : `historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_AAAA-MM-JJ_<auteur>.md`.
- Chaque agent n'ecrit que dans son propre fichier.
- Jamais de secret dans une ligne ; ces fichiers ne sont pas des sauvegardes (pas de `.bak`).
- Le journal est declaratif : une ligne absente ne prouve rien.

## Decisions datees

- 2026-10-10 : creation, apres des fichiers modifies sans trace.
- 2026-10-21 : dossier deplace dans `historique\03_RAPPORTS\01_MODIFS_IA\`.
- 2026-10-22 : plus de copie sur `H:` pour les journaux de Claude (decision d'Eric, une seule source locale).

## Points a verifier avec Eric

- Corrige le 2026-10-31 dans la copie anglaise : plus de copie du journal vers `H:`, lecture et ecriture en local (decision du 2026-10-22).
- Reste a confirmer avec toi : le dossier ou Hermes ecrit son propre journal (avant le 2026-10-22 il ecrivait dans `H:\docs\modifs\`).

## Quand modifier cette fiche

Chaque fois que la copie du skill change dans `05_docs_skills_PURE`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change.
