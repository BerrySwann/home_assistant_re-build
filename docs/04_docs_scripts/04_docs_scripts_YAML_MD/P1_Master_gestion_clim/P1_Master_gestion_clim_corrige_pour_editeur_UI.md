# P1_MASTER_GESTION_CLIM - version corrigée pour l'éditeur UI (sans clé racine)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--23-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>
> **Fichier source :** `docs/04_docs_scripts/04_docs_scripts_YAML/Climatisation/P1_Master_gestion_clim/P1_Master_gestion_clim_corrige_pour_editeur_UI.yaml`
> **Fiche du script :** [P1_Master_gestion_clim.md](P1_Master_gestion_clim.md)
> **Fichier jumeau :** `P1_Master_gestion_clim_corrige_2026_11_22.yaml` (même contenu, avec la clé racine)

---

## Description

Instantané du script maître du 2026-11-22 (fichier daté 13h15), **sans** clé racine : c'est le corps du script, à coller dans l'éditeur YAML de l'interface HA (Paramètres, Scripts). Version intermédiaire, **antérieure** au réalignement du soir sur la prod.

## Contrôle fait le 2026-11-23

- Comparé au jumeau `..._corrige_2026_11_22.yaml` : seule la ligne de clé racine `p1_master_gestion_clim:` manque ici, tout le reste est identique.
- Comparé à la référence `P1_Master_gestion_clim.yaml` : il diffère (voir la fiche du jumeau). Il ne représente plus la prod.

## Points d'attention

- Ne pas coller ce corps dans l'éditeur UI sans comparer avant à la prod : la référence a changé depuis.
- Décision d'Eric à prendre pour la suite : garder cet instantané ou l'archiver (non décidé).

<!-- annotations_log:
[2026-11-23] fiche créée (demande d'Eric) : le contrôle 6F signalait ce YAML sans fiche. Contenu comparé au jumeau et à la référence. -->
