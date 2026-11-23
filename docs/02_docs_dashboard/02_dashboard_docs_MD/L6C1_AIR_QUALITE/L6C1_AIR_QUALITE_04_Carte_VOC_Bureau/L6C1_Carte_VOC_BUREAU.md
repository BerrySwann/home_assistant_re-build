# L6C1 - Carte tCOV (VOC) Bureau

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--23-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Dashboard-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Path | `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_AIR_QUALITE/L6C1_AIR_QUALITE_04_Carte_VOC_Bureau/L6C1_Carte_VOC_BUREAU.yaml` |
| Entite | `sensor.tcov_bureau_ppb` |
| Layout | `custom:vertical-stack-in-card` : `custom:mushroom-entity-card` (icone animee selon le niveau) + `custom:mini-graph-card` (24 h, en fond) |
| Cartes HACS requises | mushroom, card-mod, vertical-stack-in-card, mini-graph-card |
| Cree le | 2026-11-22 (demande d'Eric) |
| Origine | copie de la carte tCOV (VOC) du Salon, `Dashboard_COMPLET/Dashboard_2026_11_07.yaml` lignes 37921-38257, avec le Salon remplace par Bureau |
| Etat | deploye en prod le 2026-11-22 (dashboard-tablette, vue air-quality, juste sous le separateur de la piece) |

---

## Ce que fait la carte

Une pastille mushroom affiche la valeur de `sensor.tcov_bureau_ppb` et change de couleur et d'animation selon le niveau. Le mini-graphique des 24 dernieres heures est place en fond de carte, en transparence. Aucune logique n'est ajoutee cote HA : les seuils sont dans le code de la carte (bloc card-mod).

## Seuils de couleur

| tCOV (ppb) | Couleur |
|:--|:--|
| sous 100 | vert |
| 100 a 199 | vert clair |
| 200 a 299 | jaune |
| 300 a 399 | orange |
| 400 et plus | rouge |

## Entites

| Entite | Role | Source |
|:--|:--|:--|
| `sensor.tcov_bureau_ppb` | valeur affichee et graphique | `templates/Air_Quality/AQ_01_air_quality.yaml` (conversion du VOC index en ppb) |

## Notes

- Le Salon n'a pas de fichier separe dans L6C1 : ses deux cartes (PM2.5 et VOC) ne sont que dans l'export `Dashboard_COMPLET`. La Page L6C1 actuelle (`L6C1_Page_AIR_QUALITE.yaml`) utilise d'autres cartes (streamline et bubble) pour les trois pieces.
- Le nom de la carte et l'entite sont les seuls elements qui changent d'une piece a l'autre. Tout le reste du code est identique.

## Journal des changements

| Date | Auteur | Modification |
|:--|:--|:--|
| 2026-11-22 | Claude | Creation, derivee de la carte du Salon (demande d'Eric). YAML relu : structure identique a la source, aucune occurrence restante de "salon". |

<!-- annotations_log:
[2026-11-22] deployee en prod dans la vue air-quality (dashboard-tablette), sous le separateur BUREAU ; hash dashboard apres ecriture fa09dad1f0f5a828 ; entites verifiees (etat lu dans HA).
[2026-11-22] creation : carte tCOV (VOC) Bureau derivee de la carte du Salon ; non deployee en prod. -->
