# Skill histo-final - histo complet puis extinction des lumieres et du PC

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
| Skill | `histo-final` (commande `/histo-final`) |
| Copie utilisable (anglais) | `docs/05_docs_skills/05_docs_skills_PURE/skill_histo_final/histo_final.md` |
| Skill installe | `.claude/skills/histo-final/SKILL.md` |
| Declenchee par | Eric (`/histo-final`, "fin de journee", "j'eteins tout") |
| Appelle | le skill `histo` (voir `05_docs_skills_MD/skill_histo/histo.md`) |
| Langue de la copie | anglais ; chemins, ids d'entites, noms d'etapes de trace et etiquettes du rapport restent en francais |

## A quoi ca sert

Fin de journee : le skill lance tout `/histo`, verifie que tout est ecrit et pousse, envoie une notification sur le telephone d'Eric, coupe Hue Sync puis eteint les 3 Hue Play du bureau, et arrete le PC avec un delai de 5 minutes. A utiliser a la place de `/histo` quand Eric part. En cours de journee, utiliser `/histo`.

## Les etapes

1. Question de depart (le tout premier geste) : "Histo final definitif ?", Oui ou Non. Oui = le menage des `.bak` de `docs` et `Claude md SAVE` est fait, avec la purge de la corbeille (elements de plus de 3 mois). Non = essai, pas de ce menage. Pas de reponse : Non. Puis coupure de l'automation qui rallume les Play, et lancement de `/histo`.
2. Verification que tout est ecrit : journal des modifs complet, aucun script encore en cours, MD5 de `GLOBAL_INDEX_REPO.md` et de `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` identiques en local et en prod, rapport des emplacements et du push, `histo_trace.py verifier` sans echec.
3. Pas de question : enchainement direct.
4. Notification sur le telephone (`notify.mobile_app_eric`), attente de 10 s, puis arret du flux Hue Sync par l'API du pont, attente du mode normal des 3 Play, `light.turn_off` sur les 3 Play, et remise en route de l'automation.
5. Arret du PC : dernieres ecritures (journal des modifs, fermeture de la trace), message final a Eric, puis `shutdown /s /t 300` en tout dernier appel. Annulation possible avec `shutdown /a`.

## Regles cles

- La sequence est irreversible : l'arret du PC coupe la liaison avec Claude, donc tout doit etre ecrit et verifie avant. Aucun appel d'outil apres la commande d'arret.
- Pas d'extinction (ni lumieres ni PC) si une etape de `/histo` a echoue ou reste incomplete : le PC reste allume et le rapport le dit.
- Ne bloquent pas l'extinction : le controle des fiches et badges, un ecart restant sur les fichiers memoire de Claude, un fichier signale "PROD DIFFERENTE INCONNUE" (non ecrase). Bloque l'extinction : un MD5 different apres une copie en prod, une etape sans fin ou en echec dans la trace.
- Les lumieres eteintes sont les 3 Hue Play (`light.hue_play_1_pc_bureau`, `_2_`, `_3_`). La prise `switch.ecran_p_c_3_play_hue` reste toujours `on`.
- La cle du pont Hue est dans la variable d'environnement Windows `HUE_BRIDGE_KEY` : elle n'est jamais affichee ni ecrite.
- Le statut des fiches (`Actif`, `bak_h`, `bak_d`, `Trash`...) est pose par `/histo`, jamais par `/histo-final`.

## Decisions datees

- 2026-10-11 : extinction par les 3 Hue Play (la prise est abandonnee) ; arret de Hue Sync par l'API du pont avant `light.turn_off`.
- 2026-10-21 : delai d'arret ramene a 5 minutes (300 s) ; automation remise en route avant l'arret.
- 2026-10-29 : id de l'automation corrige (`automation.nouvelle_automatisation`) ; fichiers memoire de Claude obligatoirement a jour avant l'extinction.
- 2026-10-30 : push general de `docs` en prod avant l'arret.
- 2026-10-31 : question "Histo final definitif ?" au debut ; menage des `.bak` de `docs` seulement sur Oui.
- 2026-10-31 : chemin corrige dans le skill : `historique/03_RAPPORTS/06_MD5/` (ancien `historique/MD5/`).
- 2026-10-31 : le skill est traduit en anglais et range dans `05_docs_skills_PURE` ; cette fiche est son explication en francais.

## Quand modifier cette fiche

Chaque fois que `histo_final.md` change dans `05_docs_skills_PURE/skill_histo_final/`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change. Le skill installe dans `.claude/skills/histo-final/` doit rester identique a la copie `histo_final.md`.
