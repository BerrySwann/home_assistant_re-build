# Histo Nodon Quotidien

**Catégorie :** energie
**Alias HA :** `[P0] Histo Nodon quotidien`

## Description

Enregistre chaque nuit à 23h59 la consommation Nodon J-1 (`last_period` du UM quotidien) dans `/config/notifs/nodon_histo.txt` via l'intégration File `notify.log_nodon_histo`.

Format de ligne : `JJ/MM | Nodon : X.XX kWh`

## Déclencheurs

- `time` 23:59:00

## Entités principales

- `sensor.genelec_appart_quotidien_um` (attr `last_period`)
- `notify.send_message` -> `notify.log_nodon_histo` -> `/config/notifs/nodon_histo.txt`

## Fichier source

`energie/histo_nodon_quotidien.yaml`

## Prérequis

Intégration File créée dans l'UI HA : Paramètres > Appareils > Ajouter intégration > File
- Nom : `log_nodon_histo` | Fichier : `/config/notifs/nodon_histo.txt`

---
*Doc créée le 2026-09-01*
