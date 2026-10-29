# IA_GLOBAL_INDEX_memoire - index des fichiers de docs/00_IA

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--29-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?logo=home-assistant&logoColor=white&style=flat-square)](.)&nbsp;
[![IA_Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Script_seul-ff9800?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Index_genere-ff9800?style=flat-square)](.)

</div>

> Fichier GENERE le 2026-10-29 21:50 par gen_global_index_ia.py - ne pas editer a la main (relancer le script ou /histo).
> 13 fichiers de contenu, 81 sauvegardes (.bak), 0 sans description.

> 🚨🚨🚨 **GYROPHARE ROUGE - DANS HOME ASSISTANT TOUT EST A PLAT** 🚨🚨🚨
>
> - Un script est en `/config/.scripts/<fichier>` (aucun sous-dossier) ; un YAML command_line est en `/config/command_line/<categorie>/<fichier>` (un seul niveau).
> - Le rangement par dossier (`<nom>_<extension>`) existe UNIQUEMENT en local (ReBuild) et dans le miroir docs de la prod. NE JAMAIS pousser ces dossiers tels quels vers `/config` : les `shell_command` appellent des chemins absolus plats, et un YAML pousse en double serait charge deux fois.
> - Avant tout push vers la prod racine : aplatir le chemin. Explication complete (arbre local trie, liste a plat, cascades bouton -> script -> fonction) : section SCRIPTS ET COMMAND_LINE de [DEPENDANCES_GLOBALES_CLAUDE_memoire.md](../00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md).

## A quoi sert ce fichier

Liste de tous les fichiers de docs/00_IA (le dossier des directives pour les IA), avec pour chacun : qui s'en sert, son but, quand le lire, et un lien. Il sert a Claude et Hermes pour savoir quel sous-contexte charger, et a Eric pour retrouver ou est quoi. Les descriptions viennent de la table de lecture de CLAUDE.md et de l'en-tete de chaque fichier ; les sauvegardes (.bak) ne sont pas listees une par une.

## Contexte de base (00_IA_CONTEXT_BASE)

| Fichier | Qui s'en sert | Son but | Quand le lire | Cite dans CLAUDE.md | Prod |
|---|---|---|---|---|---|
| [IA_CONTEXT_BASE.md](../00_IA_CONTEXT_BASE/IA_CONTEXT_BASE.md) | Claude (c'est son CLAUDE.md local), Hermes et toute IA du projet ; Eric pour relire les regles. Tenu identique en 3 emplacements (voir son en-tete) | Directives IA completes : regles de codage YAML, nomenclature, hierarchie visuelle, arborescences, protocoles, regle de sauvegarde. Meme contenu que le CLAUDE.md local. | Quand une IA doit travailler dans le projet : c'est le contexte de base, les sous-contextes ci-dessous le completent. | oui | OK (MD5 identique) |

## Sous-contextes (00_IA_SOUS_CONTEXT_IA)

Un dossier par fichier. Chargés a la demande : Claude ne les lit que si la tache le demande (colonne Quand le lire).

| Fichier | Qui s'en sert | Son but | Quand le lire | Cite dans CLAUDE.md | Prod |
|---|---|---|---|---|---|
| [IA_ARBO_DETAIL.md](../00_IA_SOUS_CONTEXT_IA/IA_ARBO_DETAIL/IA_ARBO_DETAIL.md) | Claude, via /update-arbo et /histo (etape 6) | Arborescences completes local, prod et GitHub avec les comptages de fichiers, URLs raw GitHub. | Audit de fichiers, synchro GitHub, recherche d'un fichier en prod, verification de l'arborescence locale. | oui | OK (MD5 identique) |
| [IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md](../00_IA_SOUS_CONTEXT_IA/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md) | Claude, en mode expert audit energetique | Prompt expert : caracteristiques du logement, equipements, methodes d'analyse, missions et format du rapport d'audit conso et thermique. | Audit de consommation, analyse DUT par piece, efficacite isolation/volets/rideaux, ecart entre la theorie des YAML et les logs reels. | oui | OK (MD5 identique) |
| [IA_AUTOMATIONS_NOTIFS.md](../00_IA_SOUS_CONTEXT_IA/IA_AUTOMATIONS_NOTIFS/IA_AUTOMATIONS_NOTIFS.md) | Claude, pour ecrire ou modifier des automations et des notifications | Regles de codage des automations et referentiel des notifications de la prod (canaux, titres, messages, fichiers log). | Creation ou modification d'une automation, ecriture d'un message notify, script HA. | oui | OK (MD5 identique) |
| [IA_CARTE_EMPLACEMENTS.md](../00_IA_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS/IA_CARTE_EMPLACEMENTS.md) | Claude et les skills qui copient ou comparent des fichiers (histo, ha-push-yaml, ha-push-docs, ha-trigul...) | Carte unique des fichiers presents a plusieurs emplacements (local, prod racine, prod miroir docs, GitHub racine et docs/) et regles de correspondance ; script de controle Verif_emplacements.py. | Avant un push de config, de GLOBAL_INDEX_REPO ou de README, ou un controle local / prod / GitHub. | non | OK (MD5 identique) |
| [IA_CMD_TERMINAL_HA.md](../00_IA_SOUS_CONTEXT_IA/IA_CMD_TERMINAL_HA/IA_CMD_TERMINAL_HA.md) | Claude et Eric, pour les commandes a lancer sur HA | Commandes terminal HA : commande tree prod, audits MD5, sauvegarde git vers GitHub, logs, chemins /homeassistant/. | Lancer un audit ou un backup, lire un log, retrouver un chemin /homeassistant/. | oui | OK (MD5 identique) |
| [IA_INDEX_AUTOMATIONS.md](../00_IA_SOUS_CONTEXT_IA/IA_INDEX_AUTOMATIONS/IA_INDEX_AUTOMATIONS.md) | Claude, pour tenir l'index des automations | Comment les automations sont indexees (index genere et resume de GLOBAL_INDEX_REPO), arborescence locale, comptage par categorie, procedure de mise a jour. | Ajout, suppression ou renommage d'une automation, regeneration de l'index. | oui | OK (MD5 identique) |
| [IA_INDEX_NAVIGATION.md](../00_IA_SOUS_CONTEXT_IA/IA_INDEX_NAVIGATION/IA_INDEX_NAVIGATION.md) | Claude, pour tenir l'index du dashboard | Comment la navigation du dashboard est indexee (index genere et section 02 de GLOBAL_INDEX_REPO), arborescence, chemins GitHub, limites connues. | Ajout d'une vignette ou d'une page, mapping des entites vers leurs fichiers sources. | oui | OK (MD5 identique) |
| [IA_INTEGRATIONS_CARTES.md](../00_IA_SOUS_CONTEXT_IA/IA_INTEGRATIONS_CARTES/IA_INTEGRATIONS_CARTES.md) | Claude, pour valider un YAML de dashboard | Referentiel des integrations HA (HACS, core, add-ons), des cartes du dashboard et de la palette de couleurs. | YAML dashboard a valider, type custom:* inconnu, integration manquante, nouvelle carte a ajouter. | oui | OK (MD5 identique) |
| [IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md](../00_IA_SOUS_CONTEXT_IA/IA_NOM_DES_REPERTOIRES_ET_FICHIERS/IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md) | Claude et Hermes (qui s'aligne dessus) pour nommer les dossiers et fichiers de docs ; Eric pour valider les regles | Regles de nommage des repertoires et des fichiers du dossier docs (poles, abreviations, accents, niveaux, releve des ecarts a renommer). Copie du maitre historique/IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md ; statut brouillon a valider par Eric. | Avant de creer, renommer ou deplacer un fichier ou un dossier de docs ; pour savoir quels noms sont encore en ecart. | oui | OK (MD5 identique) |
| [IA_P4_PRESENCE.md](../00_IA_SOUS_CONTEXT_IA/IA_P4_PRESENCE/IA_P4_PRESENCE.md) | Claude, pour les automations et messages qui dependent de la presence | Referentiel de la presence : logique de sensor.groupe (automatisation, reseau cible) et de sensor.presence (format dans les notifications). | Automation clim, message notify avec presence, logique groupe WiFi. | oui | OK (MD5 identique) |
| [IA_SKILLS_INVENTAIRE.md](../00_IA_SOUS_CONTEXT_IA/IA_SKILLS_INVENTAIRE/IA_SKILLS_INVENTAIRE.md) | Eric, et Claude ou Hermes pour aligner les skills | Inventaire des skills Hermes regroupees par sujet, avec les skills communes a Claude en face a face. | Savoir quelle skill existe, aligner les skills de Claude et d'Hermes. Pas dans la table de lecture de CLAUDE.md, pas pousse en prod. | non | OK (MD5 identique) |

## Memoires de Claude (00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire)

| Fichier | Qui s'en sert | Son but | Quand le lire | Cite dans CLAUDE.md | Prod |
|---|---|---|---|---|---|
| [DEPENDANCES_GLOBALES_CLAUDE_memoire.md](../00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md) | Claude (il la tient a jour via /sync_index et /histo) ; Hermes a sa propre version dans docs/XX_docs_MD_system/DEPENDANCES_GLOBALES_HERMES | Chaine de dependances du dashboard : matrice des 18 vignettes, entites, fichiers et automations par domaine, scripts, fichiers config racine. Citee par IA_CONTEXT_BASE, IA_ARBO_DETAIL, IA_INDEX_NAVIGATION et IA_NOM_DES_REPERTOIRES_ET_FICHIERS. | Apres validation d un YAML, d une automation ou d une vignette ; pour savoir quelles entites et quels fichiers dependent d une vignette. | oui | OK (MD5 identique) |

## Sauvegardes (.bak)

Copies datees a cote de chaque fichier (regle de sauvegarde de CLAUDE.md : 10 max le jour meme, 3 les jours precedents, menage par /histo). Jamais poussees en prod.

| Dossier | Nombre de sauvegardes |
|---|---|
| [00_IA_CONTEXT_BASE](../00_IA_CONTEXT_BASE/) | 6 |
| [00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire](../00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/) | 15 |
| [00_IA_GLOBAL_INDEX_memoire](./) | 20 |
| [00_IA_SOUS_CONTEXT_IA/IA_ARBO_DETAIL](../00_IA_SOUS_CONTEXT_IA/IA_ARBO_DETAIL/) | 8 |
| [00_IA_SOUS_CONTEXT_IA/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE](../00_IA_SOUS_CONTEXT_IA/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/) | 3 |
| [00_IA_SOUS_CONTEXT_IA/IA_AUTOMATIONS_NOTIFS](../00_IA_SOUS_CONTEXT_IA/IA_AUTOMATIONS_NOTIFS/) | 3 |
| [00_IA_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS](../00_IA_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS/) | 3 |
| [00_IA_SOUS_CONTEXT_IA/IA_CMD_TERMINAL_HA](../00_IA_SOUS_CONTEXT_IA/IA_CMD_TERMINAL_HA/) | 2 |
| [00_IA_SOUS_CONTEXT_IA/IA_INDEX_AUTOMATIONS](../00_IA_SOUS_CONTEXT_IA/IA_INDEX_AUTOMATIONS/) | 3 |
| [00_IA_SOUS_CONTEXT_IA/IA_INDEX_NAVIGATION](../00_IA_SOUS_CONTEXT_IA/IA_INDEX_NAVIGATION/) | 6 |
| [00_IA_SOUS_CONTEXT_IA/IA_INTEGRATIONS_CARTES](../00_IA_SOUS_CONTEXT_IA/IA_INTEGRATIONS_CARTES/) | 3 |
| [00_IA_SOUS_CONTEXT_IA/IA_NOM_DES_REPERTOIRES_ET_FICHIERS](../00_IA_SOUS_CONTEXT_IA/IA_NOM_DES_REPERTOIRES_ET_FICHIERS/) | 5 |
| [00_IA_SOUS_CONTEXT_IA/IA_P4_PRESENCE](../00_IA_SOUS_CONTEXT_IA/IA_P4_PRESENCE/) | 1 |
| [00_IA_SOUS_CONTEXT_IA/IA_SKILLS_INVENTAIRE](../00_IA_SOUS_CONTEXT_IA/IA_SKILLS_INVENTAIRE/) | 3 |

## Les autres index globaux du projet

Tous sont verifies par /histo (liens casses, existence, prod).

| Index | Role | Verification |
|---|---|---|
| [GLOBAL_INDEX_REPO.md](../../01_docs_config_system/01_config_system_MD/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md) | Index du depot GitHub, liens depuis la racine du depot. Tenu a la main par /histo (sync_index) ; a pousser aux 2 endroits de la prod (racine et miroir docs). | check_global_index.py |
| [GLOBAL_INDEX_AUTOMATIONS.md](../../03_docs_automations/GLOBAL_INDEX_AUTOMATIONS.md) | Genere par gen_global_index_automations.py. | etape 8 de /histo + check_global_index.py |
| [GLOBAL_INDEX_VIGNETTES_PAGES.md](../../02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md) | Genere par gen_global_index_vignettes_pages.py. | etape 9 de /histo + check_global_index.py |
| [GLOBAL_INDEX_SCRIPTS_SH.md](../../04_docs_scripts/GLOBAL_INDEX_SCRIPTS_SH.md) | Genere par gen_global_index_scripts.py (scripts bash et python). | etape 10 de /histo + check_global_index.py |
| [GLOBAL_INDEX_SCRIPTS_YAML.md](../../04_docs_scripts/GLOBAL_INDEX_SCRIPTS_YAML.md) | Genere par gen_global_index_scripts.py (scripts Home Assistant). | etape 10 de /histo + check_global_index.py |
| [ENTITES_GLOBAL_INDEX.md](../../XX_docs_MD_system/ENTITES_GLOBAL_INDEX/ENTITES_GLOBAL_INDEX.md) | Index des entites, sans generateur : tenu a la main. | check_global_index.py |
| [IA_GLOBAL_INDEX_memoire.md](IA_GLOBAL_INDEX_memoire.md) | Ce fichier, genere par gen_global_index_ia.py. | etape 11 de /histo + check_global_index.py |

