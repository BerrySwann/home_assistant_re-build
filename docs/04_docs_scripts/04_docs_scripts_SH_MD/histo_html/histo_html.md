# histo_html.py - pages HTML des journaux de bord histo

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
| Source | `docs/04_docs_scripts/04_docs_scripts_SH/histo_html/histo_html.py` |
| Langage | Python 3 |
| Lance par | /histo (etape 4B). Ne fait pas tourner Home Assistant |
| Cree | le 2026-10-21 a la demande d'Eric |

## Role

Produit une page HTML sombre par jour, avec toutes les sessions du jour, a partir des journaux `histo_AAAA-MM-JJ[_sN].md` et `.txt` de `historique/` et du dossier `historique/02_*`. Les pages sont ecrites dans ce dossier `02_*`. Les originaux `.md` et `.txt` ne sont jamais modifies ni deplaces par le script. Dans tous les cas `index.html` est refait.

## Utilisation

```
python -I histo_html.py                 page du jour + page du journal fusionne le plus recent
python -I histo_html.py AAAA-MM-JJ      page d'un jour
python -I histo_html.py tout            toutes les pages (jours et journaux fusionnes)
python -I histo_html.py fusionne        pages des journaux fusionnes
```

## Regles (decidees par Eric le 2026-10-21)

- Une page par jour `histo_AAAA-MM-JJ.html`, gardee sans limite de jours.
- Si la page existe avec un contenu different, copie d'abord en `histo_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html` (10 au plus le meme jour, menage fait par /histo). Page identique : rien n'est ecrit.
- Une page existante sans la balise generator du script n'est jamais ecrasee : signalee COLLISION et ignoree.
- Un `.md` et un `.txt` de meme jour et meme session : le `.md` est pris, le `.txt` est signale.
- Les `.bak`, les `.html` et les journaux fusionnes ne sont pas lus comme sources de jour ; `JOURNAL_FUSIONNE_*.md` et `JOURNAL_COMPLET_*.md` donnent une page du meme nom en `.html`, avec sommaire.
- Contenu deterministe (pas d'heure de generation), pour que "identique" soit fiable. Aucun secret lu ou ecrit.
- Variable `HISTO_HTML_DIR` : remplace `historique/` (essais seulement).

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture de l'en-tete du fichier source. Le corps du script (generation du HTML) n'a pas ete relu en detail.
