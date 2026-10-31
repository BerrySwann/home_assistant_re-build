# SDB_soufflant_arreter.yaml - script.sdb_soufflant_arreter

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifie](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script_Executant-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| Source | `docs/04_docs_scripts/04_docs_scripts_YAML/Soufflant_SDB/SDB_soufflant_arreter/SDB_soufflant_arreter.yaml` |
| Entite | `script.sdb_soufflant_arreter` (mode `single`) |
| Role | [EXECUTANT] sequence d'arret du soufflant de la salle de bain |
| Appele par | l'automation SDB - SOUFFLANT - ROUTAGE et le script de demarrage (`script.sdb_soufflant_demarrer`) |

## Sequence (lue dans le fichier)

1. Refus si le verrou de demarrage est actif (`input_boolean.verrou_soufflant_salle_de_bain` doit etre `off`).
2. Coupure des deux resistances par IR : `remote.send_command` sur `remote.soufflant_sdb` (commande `on_off`, appareil `radiateur_sdb`) ; le ventilateur continue.
3. Compteur d'etat logiciel : `input_select.etat_resistance_soufflant_sdb` sur `0W`.
4. Refroidissement : ventilateur pendant 1 min 30.
5. Dernier controle : on ne coupe pas si l'appareil a ete rallume (`input_boolean.inter_soufflant_salle_de_bain` doit etre `off`).
6. Coupure de la prise `switch.prise_soufflant_salle_de_bain_nous` (evite 4 W de veille).
7. Affichage : `climate.soufflant_salle_de_bain` sur `off`, place apres le dernier controle, donc un arret refuse ne remet pas le climate sur `off`.

## Etat (journal du fichier)

- Deploye en prod le 2026-09-28 dans `scripts.yaml`, recharge sans redemarrage. Complete le 2026-09-29 (climate `off` en fin de sequence). Version finale 2026/2027.

## Voir aussi

- Fiches de chauffage SDB : `docs/03_docs_automations/03_docs_automations_MD/P1_03_Chauffage_salle_de_bain/`.

## Origine de cette fiche

Creee le 2026-10-28 par Claude, a partir de la lecture du YAML local. Le YAML n'a pas ete compare a `H:\scripts.yaml` pour cette fiche.
