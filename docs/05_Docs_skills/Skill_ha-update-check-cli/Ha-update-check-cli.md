---
name: "ha-update-check-cli"
description: "Skill HA ReBuild - analyse les mises a jour HA en attente SANS outils MCP (Claude Code en ligne de commande) : versions via .HA_VERSION et API GitHub, notes de version, croisement grep contre la config reelle, pieges ReBuild, checklist post-MAJ. N'installe rien. Declencher sur /ha-update-cli, mise a jour HA en CLI, maj HA sans MCP."
---

# ha-update-check-cli - Analyse pre-mise a jour HA (sans MCP)

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_Docs_scripts\Docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18).

Objectif: lire les changements des mises a jour HA en attente, les croiser avec la config reelle d'Eric (grep), et sortir un top court: ce qu'il doit faire avant, ce qui va casser, ce qui est a faire apres. Cette version N'INSTALLE RIEN: l'installation, la sauvegarde et le restart se font depuis l'UI HA, par Eric.

Si les outils MCP HA (ha_manage_updates, ha_get_overview, ha_manage_backup...) sont disponibles dans la session, utiliser plutot le skill ha-update-check du compte (analyse, sauvegarde, installation, restart, cache).

## Regles

- Francais, concis, direct. Pas de tableau, pas d'emoji, pas de gras systematique.
- Typographie: uniquement tiret simple, trois points, guillemets droits, apostrophe droite. Aucun caractere Alt. Fleche = ->, puce = -.
- Chaque fait precis (version, nom d'option, date) est qualifie: etabli (lu dans un fichier, une API ou une page, dire laquelle), deduit (dire a partir de quoi), ou inconnu (dire qu'on ne sait pas, jamais de valeur approximative).
- Les notes de version resumees par WebFetch ne sont PAS le texte integral: le dire.
- Ne jamais deviner une compatibilite (version minimale de HA, etc.): inconnu.
- Un point "non verifie" n'est jamais presente comme "sans impact".
- Ne jamais afficher un token, un mot de passe ou une cle API (voir pieges ReBuild).

## Etape 1 - Versions (sans MCP)

- Core installee: lire H:\.HA_VERSION (deduit: H:\ est le dossier de config de la prod, voir ha-push-yaml; a confirmer au premier usage). Si illisible: inconnu, demander a Eric.
- Core disponible: API GitHub, https://api.github.com/repos/home-assistant/core/releases/latest (WebFetch ou curl selon ce qui est dispo). Si l'API est inaccessible (limite de debit, reseau): inconnu, ne pas deviner.
- Cartes et integrations custom (HACS): leurs versions ne sont pas lisibles de facon fiable sans MCP. Demander a Eric la liste des mises a jour en attente (HACS -> mises a jour, ou capture) et noter pour chacune: nom, version installee -> version cible, lien de la release.
- Si plusieurs versions sont sautees: lire les notes de TOUTES les versions intermediaires.

## Etape 2 - Lire les changements

Pour chaque mise a jour:
1. Notes de la release GitHub (lien fourni par Eric, ou API releases du depot). Pour le core: https://www.home-assistant.io/blog/categories/release-notes/.
2. WebFetch avec la demande explicite: breaking changes, options renommees ou depreciees ou supprimees, entites/services supprimes, version minimale de HA, migrations, bandeaux "restart HA" ou "vider le cache".
3. Classer chaque point: breaking change, suppression, deprecation, option renommee, nouveaute, correctif.

## Etape 3 - Croiser avec la config reelle (grep)

Ne declarer impacte que ce qui est verifie. Sinon: "non verifie".

Perimetre (lecture seule):
- Local: C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_SH_PY_YAML\ et docs\03_docs_automations\docs_automations_YAML\
- Prod: H:\ (config YAML ; themes/, blueprints/ et notifs/ n'existent qu'en prod)

Pour chaque option, entite, service ou carte (custom:xxx) citee par les notes: grep -rIn sur le perimetre, noter fichier et ligne. Zero resultat = "non utilise (verifie dans <perimetre>)". Les dashboards stockes hors YAML et le contenu imbriques ne sont pas couverts par ce grep: le signaler.

## Etape 4 - Pieges ReBuild a verifier systematiquement

Libelles repris de la liste d'Eric du 2026-10-13. Le detail (symptome exact et verification) n'a pas ete fourni: A COMPLETER par Eric dans ce fichier. En attendant, ne verifier que ce que le grep permet et dire le reste en "non verifie".

- token API 403
- dashboard 1.7 Mo
- 5 sensors uptime avec parseFloat (grep -rIn "parseFloat")
- cartes custom a surveiller: mushroom v5, button-card, etc. (grep -rIn "custom:mushroom" et "custom:button-card")
- condition state + for + attribute
- mqtt.publish admin-only (grep -rIn "mqtt.publish")
- CARTO / API key (ne jamais afficher la cle)

## Etape 5 - Decision et rapport

Verdict par mise a jour: INSTALLER / BLOQUER.
BLOQUER si un breaking change ou une suppression touche un element verifie a l'etape 3 ou un piege de l'etape 4, si une migration manuelle est exigee, ou si les notes sont introuvables. Une deprecation sans suppression ne bloque pas: la lister.

Format de sortie, court:

Verdict: (une ligne par mise a jour, avec la raison)

TOP (par gravite, max 5 lignes): quoi -> consequence pour Eric -> action.

A FAIRE AVANT: sauvegarde depuis l'UI HA, manipulations citees dans les notes.

CE QUI VA CASSER / A REFAIRE: elements impactes (verifies). Sinon: "rien de verifie".

A FAIRE APRES: restart HA si demande, vider le cache du frontend (Ctrl+F5 sur PC, cache de l'appli Companion sur mobile), controles de l'etape 6.

NON VERIFIE / INCONNU: tout ce que les notes, le grep ou les API n'ont pas permis d'etablir.

## Etape 6 - Checklist post-MAJ

La checklist detaillee en 14 points d'Eric n'a pas ete fournie: A COLLER ICI. En attendant, controles minimaux (a faire par Eric dans l'UI):
- Outils de developpement -> YAML -> verifier la configuration: valide.
- Parametres -> Systeme -> Reparations: comparer avec l'etat avant.
- Parametres -> Systeme -> Journaux: nouvelles erreurs liees aux composants mis a jour.
- Dashboards concernes: les cartes s'affichent.
- Cache du frontend vide.

## Etape 7 - Installation

Jamais par ce skill. Eric installe depuis l'UI HA apres sauvegarde (Parametres -> Systeme -> Sauvegardes). Ordre conseille: cartes HACS -> integrations HACS -> apps -> core -> OS. Le core et l'OS un par un.

## Fin de session

Si des fichiers du projet ont ete modifies: appliquer journal-modifs. Proposer /histo.