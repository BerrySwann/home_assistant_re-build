# histo_nodon_complet - Lecture de nodon_complet_histo.txt

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

> **Fichier :** `histo_nodon_complet.yaml`
> **Emplacement prod :** `/config/command_line/Energie/histo_nodon_complet.yaml` (et miroir `/config/docs/01_docs_config_system/01_config_system_SH_PY_YAML/...`)
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/command_line/Energie/histo_nodon_complet.yaml`
> **Empreinte relevée le 2026-10-23 :** MD5 `ed10f126`, 3372 octets, copie locale identique à la prod après le push du 2026-10-23
> **Inclus par :** `configuration.yaml` (`command_line: !include_dir_merge_list command_line/`)
> **Dernière modification :** 2026-10-23 (fichier créé)

---

## Description

Un capteur `command_line` : `Histo Energie Nodon Complet` (`unique_id: histo_energie_nodon_complet`, `scan_interval: 900`). Il lit `/config/notifs/nodon_complet_histo.txt` avec un court script Python et expose l'attribut `data` : un dictionnaire indexé par date `JJ/MM` avec `total` (kWh), `hp` (kWh), `hc` (kWh) et `cout` (EUR), sur les 14 dernières lignes valides. L'attribut `count` donne le nombre de dates lues. L'état du capteur est toujours `OK`.

Format d'une ligne du fichier : `22/10 | Total: 5.0 kWh | HP: 3.7 | HC: 1.3 | Cout: 1.0`. Les lignes `(MANQUANT)` et les lignes illisibles sont ignorées sans bloquer les autres.

## Automation rattachée

- **E - [P0] Histo Nodon complet quotidien** (id `1792780906393`, 23:59:10) écrit le fichier via `notify.nodon_complet_histo` (intégration File, chemin `/config/notifs/nodon_complet_histo.txt`, horodatage désactivé). Elle y consigne chaque nuit le total, le HP, le HC et le coût de la veille (coût aux tarifs `sensor.tarifelecinfo_tarif_heures_pleines` / `sensor.tarifelecinfo_tarif_heures_creuses`).

## Utilisé par

- `P0_MyElectricalData.yaml` : les capteurs `linky_jour_1` à `linky_jour_7` lisent `data[JJ/MM]` quand le relevé Linky d'une date vaut 0 (voir sa fiche). Le nom du jour reçoit alors une `*`.

## Points d'attention

- Le fichier n'existe pas avant la première écriture (23:59:10 le 2026-10-23, ligne du 22/10). Tant qu'il est absent, l'attribut `data` n'existe pas et les templates passent à leur repli suivant (`last_period` pour hier, sinon `nodon_histo.txt`).
- `scan_interval` 900 : une ligne écrite à 23:59:10 est visible dans le capteur au plus tard 15 minutes plus tard. Mise à jour immédiate possible avec `homeassistant.update_entity`.
- Aucun guillemet double dans le script Python : la commande est encadrée par des guillemets doubles dans le YAML.
- Prérequis côté HA : l'intégration File `nodon_complet_histo` (créée dans l'UI), sinon l'automation E ne peut pas écrire.

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
