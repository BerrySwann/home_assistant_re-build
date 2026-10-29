# SDB_soufflant_demarrer.yaml - script.sdb_soufflant_demarrer

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script_Executant-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_demarrer/SDB_soufflant_demarrer.yaml` |
| Entite | `script.sdb_soufflant_demarrer` (mode `single`) |
| Role | [EXECUTANT] sequence de demarrage du soufflant de la salle de bain (2000 W, verrou 30 s) |
| Appele par | l'automation SDB - SOUFFLANT - ROUTAGE |

## Sequence (lue dans le fichier)

1. SECURITE : refus de demarrer si `sensor.mode_ete_hiver` vaut `cool` (premiere ligne, avant le verrou, la prise et l'IR).
2. Attente de la fin d'une sequence d'arret en cours (`script.sdb_soufflant_arreter` a `off`, 2 minutes au plus).
3. Pose du verrou `input_boolean.verrou_soufflant_salle_de_bain` (30 secondes).
4. Prise `switch.prise_soufflant_salle_de_bain_nous` sur `on`, puis 1 s.
5. Mise en route IR : `remote.send_command` sur `remote.soufflant_sdb` (`on_off`, appareil `radiateur_sdb`), puis deux impulsions `1000w` (soit 2000 W).
6. Compteur d'etat logiciel : `input_select.etat_resistance_soufflant_sdb` sur `2000W`.
7. Affichage : `climate.soufflant_salle_de_bain` sur `heat`.
8. Verrou de 30 secondes, puis levee du verrou ; si `input_boolean.inter_soufflant_salle_de_bain` est `off`, lancement de `script.sdb_soufflant_arreter`.
9. SECURITE : arret force apres 60 minutes de marche (attente de `switch.inter_soufflant_salle_de_bain` a `off`, puis extinction et arret en chaine s'il tourne encore). Le compte vit dans le script : un redemarrage de Home Assistant l'efface.

## Etat (journal du fichier)

- Deploye en prod le 2026-09-28. Complete le 2026-09-29. Modifie le 2026-10-07 : garde 25 degres remplacee par la garde de saison (mode `cool`) ; verrou ramene de 2 minutes a 30 secondes (decision d'Eric : eviter un `off` premature).

## Voir aussi

- Fiches de chauffage SDB : `docs/03_docs_automations/03_docs_automations_MD/P1_03_Chauffage_salle_de_bain/`.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du YAML local. Le YAML n'a pas ete compare a `H:\scripts.yaml` pour cette fiche.
