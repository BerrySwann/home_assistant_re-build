# L6C1 - Carte PM2.5 Bureau

| Champ | Valeur |
|:------|:-------|
| Path | `docs/02_docs_dashboard/02_dashboard_docs_YAML/L6C1_AIR_QUALITE/L6C1_AIR_QUALITE_03_Carte_PM_Bureau/L6C1_Carte_PM_BUREAU.yaml` |
| Entite | `sensor.qualite_air_bureau_ikea_pm25` |
| Layout | `custom:vertical-stack-in-card` : `custom:mushroom-entity-card` (icone animee selon le niveau) + `custom:mini-graph-card` (24 h, en fond) |
| Cartes HACS requises | mushroom, card-mod, vertical-stack-in-card, mini-graph-card |
| Cree le | 2026-11-22 (demande d'Eric) |
| Origine | copie de la carte PM2.5 du Salon, `Dashboard_COMPLET/Dashboard_2026_11_07.yaml` lignes 37465-37920, avec le Salon remplace par Bureau |
| Etat | deploye en prod le 2026-11-22 (dashboard-tablette, vue air-quality, juste sous le separateur de la piece) |

---

## Ce que fait la carte

Une pastille mushroom affiche la valeur de `sensor.qualite_air_bureau_ikea_pm25` et change de couleur et d'animation selon le niveau. Le mini-graphique des 24 dernieres heures est place en fond de carte, en transparence. Aucune logique n'est ajoutee cote HA : les seuils sont dans le code de la carte (bloc card-mod).

## Seuils de couleur

| PM2.5 (ug/m3) | Couleur | Niveau EAQI |
|:--|:--|:--|
| 0 a 5 | vert fonce | Bon |
| 6 a 15 | vert clair | Correct |
| 16 a 50 | jaune | Moyen |
| 51 a 90 | orange | Mauvais |
| 91 a 140 | rouge | Tres mauvais |
| au-dessus de 140 | bordeaux | Extremement mauvais |

## Entites

| Entite | Role | Source |
|:--|:--|:--|
| `sensor.qualite_air_bureau_ikea_pm25` | valeur affichee et graphique | integration IKEA (capteur qualite d air) |

## Notes

- Le Salon n'a pas de fichier separe dans L6C1 : ses deux cartes (PM2.5 et VOC) ne sont que dans l'export `Dashboard_COMPLET`. La Page L6C1 actuelle (`L6C1_Page_AIR_QUALITE.yaml`) utilise d'autres cartes (streamline et bubble) pour les trois pieces.
- Le nom de la carte et l'entite sont les seuls elements qui changent d'une piece a l'autre. Tout le reste du code est identique.

## Journal des changements

| Date | Auteur | Modification |
|:--|:--|:--|
| 2026-11-22 | Claude | Creation, derivee de la carte du Salon (demande d'Eric). YAML relu : structure identique a la source, aucune occurrence restante de "salon". |

<!-- annotations_log:
[2026-11-22] deployee en prod dans la vue air-quality (dashboard-tablette), sous le separateur BUREAU ; hash dashboard apres ecriture fa09dad1f0f5a828 ; entites verifiees (etat lu dans HA).
[2026-11-22] creation : carte PM2.5 Bureau derivee de la carte du Salon ; non deployee en prod. -->
