# TRIGUL_RUN - Lanceur du trigul avec journal de trace

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-ff9800?style=flat-square)](.)

</div>

> **Script :** `trigul_run.py` (Python, lance avec `python -I`)
> **Emplacement local :** `docs/04_docs_scripts/04_docs_scripts_SH/hermes_audit_md5_trigul_3md/trigul_run.py`
> **Copie prod (miroir docs) :** `H:\docs\04_docs_scripts\04_docs_scripts_SH\Hermes_audit_md5_trigul_3md\`
> **Execute depuis :** le PC (local ReBuild)
> **Cree :** 2026-10-18 (demande d'Eric : voir ou le trigul plante le jour ou il plante)
> **Derniere modification :** 2026-10-18

---

## Description

Lance les 3 scripts du trigul l'un apres l'autre sans les modifier : A (`hermes_audit_trigul_arbres.py`), B1 (`hermes_audit_md5_trigul_unitaire.py`) et C (`Verif_emplacements.py`). Il ecrit chaque evenement dans un journal (ouverture, ecriture, flush, fsync : une ligne n'est jamais perdue) et detecte les plantages silencieux.

## Controles apres chaque script

- code de retour different de 0, Traceback dans la sortie, depassement de temps (300 s) ;
- rapport absent, vide, ou pas mis a jour pendant ce lancement (un ancien rapport serait pris pour le nouveau) ;
- marqueurs de fin absents du rapport : A (`RESULTAT :` et `controle du script : OK`), B1 (`ETAPES : 1 -`, `AUTOMATIONS :`, `SCRIPTS :`), C (`ANOMALIES`, `RESULTAT`) ;
- dossier temporaire du profond laisse derriere (signe d'un arret au milieu) ;
- H: inaccessible : l'etape n'est pas lancee (ECHEC) ;
- GitHub injoignable dans la sortie du script C, ou ATTENTION dans la sortie du script B1 : verdict ATTENTION.

Verdict par etape : OK, ATTENTION ou ECHEC.

## Utilisation

- `python -I trigul_run.py` : lance A, B1, C (environ 10 s, avec `PYTHONIOENCODING=utf-8`).
- `python -I trigul_run.py --note ETAPE texte...` : ajoute une ligne NOTE au journal, sans rien lancer. Sert pour les etapes faites par Claude (par exemple B2, categories HA).
- Code de retour : 0 si aucune etape n'est en ECHEC, 1 sinon.

## Journal

`historique/03_RAPPORTS/06_MD5/04_JOURNAL_TRIGUL/trigul_journal_AAAA-MM-JJ.log`, un fichier par jour, en ajout. Format : `HH:MM:SS.mmm | NIVEAU | ETAPE | message`. Niveaux : INFO, SORTIE, STDERR, NOTE, OK, ATTENTION, ECHEC. Le journal doit se terminer par `FIN DU LANCEUR` : si cette ligne manque, le lanceur lui-meme a ete interrompu (PC eteint, session fermee) et la derniere ligne dit ou.

## Points d'attention

- Un ECHEC ne se corrige pas sans demande : citer l'etape, la ligne du journal et le fichier concerne.
- Le journal d'un jour garde les ECHEC anciens meme corriges ensuite : lire l'heure de chaque ligne.
- Lecture seule sur la documentation ; il n'ecrit que le journal.

## Dependances

- Les 3 scripts du trigul ; `H:` monte ; skill `ha-trigul`.

## Historique des modifications

- 2026-10-18 : creation (etapes A, B1, C, journal, detection des echecs silencieux).
- 2026-10-18 : marqueurs de fin du profond (`ETAPES : 1 -`, `AUTOMATIONS :`, `SCRIPTS :`) et alerte sur ATTENTION.