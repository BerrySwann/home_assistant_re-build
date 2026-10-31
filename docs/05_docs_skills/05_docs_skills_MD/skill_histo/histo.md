# Skill histo - journal de bord, index, menage et controles de fin de session

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
| Skill | `histo` (commande `/histo`) |
| Copie utilisable (anglais) | `docs/05_docs_skills/05_docs_skills_PURE/skill_histo/histo.md` |
| Fichiers de reference (anglais) | `histo_ref_sync_index.md`, `histo_ref_menage.md`, `histo_ref_controles.md` dans le meme dossier |
| Skill installe | `.claude/skills/histo/SKILL.md` |
| Declenchee par | Eric (`/histo`), ou par `/histo-final` qui l'appelle |
| Langue de la copie | anglais (pour economiser des tokens) ; chemins, noms de fichiers, etiquettes du rapport et valeurs de badges restent en francais |

## A quoi ca sert

Ce skill fait le point sur une session de travail et remet tout en ordre : il ecrit le journal de bord, met a jour les index et les fiches, sauvegarde, fait le menage des anciennes sauvegardes, pousse la documentation en prod et controle que tout est coherent. Il tourne sans poser de question entre les etapes. Eric le lance en milieu de journee ou en fin de session ; `/histo-final` l'appelle puis eteint les lumieres et le PC.

## Les etapes

1. Journal de bord : un fichier `histo_AAAA-MM-JJ_sN.md` dans `historique/02_HISTO_ET_FUSIONNE/` (fichiers modifies, erreurs resolues, prochaine action).
2. Mise a jour des index (sync_index) : `DEPENDANCES_GLOBALES_CLAUDE_memoire.md`, `GLOBAL_INDEX_REPO.md`, et regeneration des index d'automations, de vignettes, de scripts et de `IA_GLOBAL_INDEX_memoire.md` par leurs scripts. Les copies de skills sont recopiees vers `05_docs_skills`.
3. Journal fusionne : ajoute la session au journal fusionne.
4. Copie Obsidian : journal et fusionne copies dans le coffre Obsidian, MD5 compare.
4B. Pages HTML sombres du jour et du fusionne ; les `.md` convertis partent a la corbeille Windows.
5. Menage des `.bak` (voir plus bas), 5B export Dashboard (un seul export en prod), 5C push de tout `docs` en prod (hors `XX_` et hors `.bak`, MD5 avant et apres).
6. Tree et controles : comptages de `IA_ARBO_DETAIL.md`, puis controles en lecture seule (sous-contexte IA, index globaux, fichiers a plusieurs emplacements, integrations File, fiches et badges, fraicheur des 2 fichiers memoire de Claude), puis rattrapage du push.
7. Rapport final au format de `histo_ref_controles.md`.

## Regles cles

- Pas de confirmation entre les etapes. Seule pause possible : le dry-run du menage la toute premiere fois sur un dossier.
- Trace : une ligne avant et apres chaque etape dans `historique/01_JOURNAL_TRACE/LOGS/` (script `histo_trace.py`). Une etape sans fin revele un blocage silencieux.
- Histo definitif ou non : le menage des `.bak` de `docs` et `Claude md SAVE` n'est fait que si Eric a repondu Oui a "Histo final definitif ?" (question posee par `/histo-final`). `/histo` seul ne fait jamais ce menage.
- Corbeille Windows : le menage n'envoie que des fichiers a la corbeille (jamais de suppression definitive). Seuls les elements de plus de 3 mois sont purges, au menage definitif.
- Jamais de sauvegarde sur `H:` ni sur `D:` : les `.bak` sont locaux.
- Les controles sont en lecture seule : un ecart est signale, jamais corrige sans demande d'Eric (sauf les 2 fichiers memoire de Claude, que Claude corrige).
- Les fichiers de reference sont lus seulement quand l'etape correspondante est executee (economie de tokens). S'il en manque un, l'etape concernee s'arrete et le dit.

## Regles des .bak (decidees le 2026-10-31)

- Horodates du jour : `fichier.bak_AAAA_MM_JJ_HHhMMmSSs.ext`, 10 au plus par fichier, Statut `bak_h` (orange).
- Au menage definitif : le plus recent devient `fichier.bak_AAAA_MM_JJ.ext` (Statut `bak_d`, orange), 3 au plus par fichier ; les autres horodates passent au Statut `Trash` (rouge) puis partent a la corbeille.
- `historique/` : une sauvegarde par jour sans limite de jours (chapitres dedies dans `histo_ref_menage.md`).

## Decisions datees

- 2026-10-21 : pages HTML sombres des journaux (etape 4B), originaux `.md` a la corbeille.
- 2026-10-30 : push general de tout `docs` en prod (etape 5C) avec rattrapage apres les controles.
- 2026-10-31 : badges partout (8 badges sur tous les `.md` de `docs`, `.bak` compris) ; menage des `.bak` seulement a l'histo definitif ; Statuts `bak_h`, `bak_d`, `Trash`.
- 2026-10-31 : le skill est traduit en anglais et range dans `05_docs_skills_PURE` ; cette fiche est son explication en francais.
- 2026-10-31 : un `.bak_AAAA_MM_JJ` garde la date du jour de sa derniere modification, pas celle du menage (precision d Eric, ecrite dans `histo_ref_menage`).

## Quand modifier cette fiche

Chaque fois que `histo.md` ou un de ses 3 fichiers de reference change dans `05_docs_skills_PURE/skill_histo/`, relire cette fiche et la mettre a jour si une etape, une regle ou une decision a change. Le skill installe dans `.claude/skills/histo/` doit rester identique a la copie `histo.md`.
