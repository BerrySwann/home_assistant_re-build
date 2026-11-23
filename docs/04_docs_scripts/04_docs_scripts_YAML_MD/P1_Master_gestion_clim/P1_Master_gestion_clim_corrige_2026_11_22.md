# P1_MASTER_GESTION_CLIM - version corrigée du 2026-11-22 (avec clé racine)

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
> **Fichier source :** `docs/04_docs_scripts/04_docs_scripts_YAML/Climatisation/P1_Master_gestion_clim/P1_Master_gestion_clim_corrige_2026_11_22.yaml`
> **Fiche du script :** [P1_Master_gestion_clim.md](P1_Master_gestion_clim.md)
> **Fichier jumeau :** `P1_Master_gestion_clim_corrige_pour_editeur_UI.yaml` (même contenu, sans la clé racine)

---

## Description

Instantané du script maître du 2026-11-22 (fichier daté 13h11), au format de `scripts.yaml` : le script est sous la clé racine `p1_master_gestion_clim:`. C'est une version intermédiaire, **antérieure** au réalignement du soir sur la prod.

## Contrôle fait le 2026-11-23

- Comparé au fichier de référence `P1_Master_gestion_clim.yaml` (lignes nettoyées comme pour la copie de lecture) : 132 lignes propres à cet instantané et 165 propres à la référence. Il ne représente donc plus la prod.
- Comparé au jumeau `..._pour_editeur_UI.yaml` : seule la ligne de clé racine `p1_master_gestion_clim:` diffère.

## Points d'attention

- Ne pas déployer : la prod est la référence `P1_Master_gestion_clim.yaml`.
- Décision d'Eric à prendre pour la suite : garder cet instantané ou l'archiver (non décidé).

<!-- annotations_log:
[2026-11-23] fiche créée (demande d'Eric) : le contrôle 6F signalait ce YAML sans fiche. Contenu comparé à la référence et au jumeau. -->
