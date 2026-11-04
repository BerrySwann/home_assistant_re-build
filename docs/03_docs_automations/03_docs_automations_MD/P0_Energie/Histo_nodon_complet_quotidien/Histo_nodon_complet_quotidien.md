# Histo Nodon Complet Quotidien

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--04-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

**Catégorie :** energie
**Alias HA :** `E - [P0] Histo Nodon complet quotidien (Total HP HC Cout)`
**ID HA :** `1792780906393`

## Description

Enregistre chaque nuit à 23h59m10s la consommation Nodon complète de la veille (Total, HP, HC) et son coût dans `/config/notifs/nodon_complet_histo.txt` via l'intégration File `notify.nodon_complet_histo`.

Ce fichier sert de source de remplacement quand le tableau hebdomadaire de L2C1 (capteurs `linky_jour_1` à `linky_jour_7`) affiche 0 parce qu'Enedis n'a pas publié le relevé Linky. Il complète `nodon_histo.txt` (qui ne contient que le total) avec le split HP/HC et le coût.

Formats de ligne :
- `JJ/MM | Total: X.X kWh | HP: X.X | HC: X.X | Cout: X.XX`
- total à 0 : `JJ/MM | Total: 0.0 kWh | HP: 0.0 | HC: 0.0 | Cout: 0.0 (MANQUANT)`

Le coût = HP x `sensor.tarifelecinfo_tarif_heures_pleines` + HC x `sensor.tarifelecinfo_tarif_heures_creuses` (tarifs EDF HPHC 6kVA TTC lus en direct, rien en dur).

## Déclencheurs

- `time` 23:59:10 (après A, B et C qui tournent à 23:59:00)

## Entités principales

- `sensor.genelec_appart_quotidien_um` (attr `last_period`) : total
- `sensor.genelec_appart_hphc_quotidien_um_hp` (attr `last_period`) : HP
- `sensor.genelec_appart_hphc_quotidien_um_hc` (attr `last_period`) : HC
- `sensor.tarifelecinfo_tarif_heures_pleines`, `sensor.tarifelecinfo_tarif_heures_creuses` : tarifs
- `notify.send_message` -> `notify.nodon_complet_histo` -> `/config/notifs/nodon_complet_histo.txt`

## Fichier source

`docs\03_docs_automations\03_docs_automations_YAML\P0_Energie\Histo_nodon_complet_quotidien\Histo_nodon_complet_quotidien.yaml`

## Prérequis

Intégration File créée dans l'UI HA : Paramètres > Appareils > Ajouter intégration > File
- Nom : `nodon_complet_histo` | Fichier : `/config/notifs/nodon_complet_histo.txt` | horodatage désactivé

## Notes

- Les valeurs sont celles de la veille (`last_period`), la ligne est donc datée J-1, comme `linky_histo.txt` et `nodon_histo.txt`.
- Le fichier se remplit à partir du 23/10/2026 (première ligne : 22/10). Les jours antérieurs n'ont pas de split HP/HC.
- Évolution prévue : un capteur command_line qui lit ce fichier et les templates `linky_jour_1` à `linky_jour_7` qui l'utilisent comme valeur de remplacement (avec une * sur le jour).

---
*Doc créée le 2026-10-23*

---

## Changement d'integration : tarif_edf -> TarifElecInfo (2026-11-04)

**Pourquoi.** L'integration `tarif_edf` venait d'un depot HACS supprime (404 sur GitHub, plus aucune
mise a jour possible), reinstallee a la main en 2.0.1. L'integration personnelle `tarifelecinfo`,
installee le 2026-11-01, la remplace : memes prix, plus le prochain changement de tarif et le nombre
de jours restants, et elle est publiable au lieu de dependre d'un depot mort.

**Correspondance des capteurs**, valeurs relevees cote a cote avant la bascule :

| Avant (`tarif_edf`) | Apres (`tarifelecinfo`) |
|:---|:---|
| `sensor.tarif_heures_pleines_ttc` | `sensor.tarifelecinfo_tarif_heures_pleines` |
| `sensor.tarif_heures_creuses_ttc` | `sensor.tarifelecinfo_tarif_heures_creuses` |
| `sensor.puissance_souscrite_hphc_6kva` | `sensor.tarifelecinfo_puissance_souscrite` |

**Ce qui a change dans ce fichier** : toutes les references a ces trois capteurs ont ete remplacees.
La formule, les periodes et les arrondis ne changent pas : seul le nom de la source bouge.

**Preuve que la bascule est neutre** : le calcul de cout rejoue par l'API `/api/template` rend le
MEME resultat avec les anciens capteurs et avec les nouveaux. Aucun prix n'est ecrit en dur ici : les
montants se lisent sur les capteurs, qui changent au 1er fevrier et au 1er aout. Les douze capteurs de cout P0
(quotidien, hebdomadaire, mensuel, annuel, en HP et en HC) sont restes vivants apres la migration.

**Ce qui a ete retire le 2026-11-04** : l'entree de configuration `tarif_edf` et le dossier
`H:/custom_components/tarif_edf`. Les trois anciens capteurs ont disparu des etats.

**Ce qui n'est PAS touche** : les capteurs TEMPO (`sensor.rte_tempo_today`,
`sensor.edf_tempo_days_blue`) sont en `platform: mqtt`, ils n'ont jamais dependu de `tarif_edf`.
