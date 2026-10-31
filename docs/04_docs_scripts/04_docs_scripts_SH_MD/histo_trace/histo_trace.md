# histo_trace.py - journal de trace de /histo et /histo-final

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/histo_trace/histo_trace.py` |
| Langage | Python 3 |
| Lance par | Claude, autour de chaque etape de /histo et /histo-final. Ne fait pas tourner Home Assistant |
| Cree | le 2026-10-19 a la demande d'Eric |

## Role

Voir ou une sequence histo s'arrete ou plante en silence, et garder la trace de chaque validation demandee a Eric. Chaque evenement est ecrit sur disque tout de suite (flush + fsync).

Journal brut : `historique/01_journal_trace/logs/histo_trace_AAAA-MM-JJ.log` (un par jour, ajout). Format : `HH:MM:SS.mmm | NIVEAU | ETAPE | message`. Niveaux : SEQ_DEBUT, SEQ_FIN, DEBUT, FIN, VALIDATION, NOTE. Pour FIN, le statut (OK, ATTENTION, ECHEC) est dans le message.

## Commandes

```
python -I histo_trace.py seq-debut histo|histo-final
python -I histo_trace.py debut ETAPE [texte]
python -I histo_trace.py fin ETAPE OK|ATTENTION|ECHEC [texte]
python -I histo_trace.py validation ETAPE texte
python -I histo_trace.py note ETAPE texte
python -I histo_trace.py seq-fin
python -I histo_trace.py verifier                 lit le journal du jour, code 1 si anomalie
python -I histo_trace.py recap [AAAA-MM-JJ]       horodatage des taches de la derniere sequence
python -I histo_trace.py html [AAAA-MM-JJ|tout]   page HTML du journal
```

- `verifier` signale : sequence sans SEQ_FIN (PC eteint, session fermee, plantage), etape DEBUT sans FIN (blocage silencieux), etapes ECHEC ou ATTENTION, validations demandees.
- `html` ecrit `historique/01_journal_trace/histo_trace_AAAA-MM-JJ.html` et `index.html` ; si la page du jour existe avec un contenu different, elle est d'abord copiee en `.bak_AAAA_MM_JJ_HHhMMmSSs.html` (10 au plus le meme jour). Page identique : rien n'est ecrit.
- Variable `HISTO_TRACE_DIR` : remplace le dossier de trace (essais seulement).

## A savoir

- Pas de secret dans les messages du journal.
- Les `.log` sont hors perimetre du menage des `.bak`.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture de l'en-tete du fichier source.
