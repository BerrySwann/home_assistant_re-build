---
name: "ha-resync-tree"
description: "Skill HA ReBuild - comparaison config locale / prod / GitHub en lecture seule (ancien resync GitHub -> local, retire le 2026-10-18 : le local fait foi). Declencher sur : resync depuis GitHub, pull depuis GitHub, met le local a jour depuis GitHub, quels fichiers ont change sur GitHub. Pas sur \"resync tree\" (= update-arbo)."
---

# HA Resync Tree - comparaison en lecture seule (ancien Local <- GitHub)

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_docs_scripts\04_docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18).

> ATTENTION (2026-10-18) : le LOCAL fait foi, la prod ne doit jamais etre en avance sur le local et GitHub n'est qu'un reflet de la prod via le backup HA. Ne jamais copier GitHub vers le local sans ordre explicite d'Eric, fichier par fichier. Les dossiers `themes/`, `blueprints/` et `notifs/` restent en prod seule.

## Quand Eric dit "resync tree"

Cela veut dire : mettre a jour `IA_ARBO_DETAIL.md` (comptages local, prod, GitHub) avec le skill `update-arbo` (constate le 2026-10-18). Ne PAS lancer ce skill-ci.

## Ce que fait ce skill

L'ancien workflow (telecharger le zip GitHub et recopier GitHub vers `config_system_YAML`) est retire : il contredisait la regle "le local fait foi" et le dossier `config_system_YAML` n'existe plus en local (remplace par `config_system_SH_PY_YAML` le 2026-10-18).

Ce skill suit maintenant la procedure de l'etape C de `/ha-trigul` (reprise de l'ancien skill `ha-resync-docs`, supprime le 2026-10-20 car doublon du trigul) :

1. Comparer en lecture seule, sur le PC :
   `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\Verif_emplacements\Verif_emplacements.py"`
   Rapport : `historique\MD5\03_verif_emplacements\verif_emplacements_[date].txt`.
2. Analyser : PROD DIFFERENTE DU LOCAL -> proposer `/ha-push-yaml` (le local fait foi) ; GITHUB EN ATTENTE DU BACKUP -> normal apres un push ; present en prod ou sur GitHub mais pas en local -> le signaler a Eric.
3. Copie vers le local : uniquement sur ordre explicite d'Eric, fichier par fichier, depuis la prod `H:\` (pas depuis GitHub), apres sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs` du fichier local s'il existe, avec une ligne au journal des modifs.
4. Automations et scripts YAML : comparaison unite par unite par l'etape profonde de `/ha-trigul`.

## REGLES

1. Lecture seule par defaut.
2. Ne jamais ecraser un fichier local sans le signaler.
3. `secrets.yaml` -> NE JAMAIS COPIER dans aucun sens.
4. Les `.md` ne sont jamais synchronises par ce skill (geres par /ha-push-docs).
5. Apres une copie validee par Eric, proposer `/sync_index` si des entites cles ont change.