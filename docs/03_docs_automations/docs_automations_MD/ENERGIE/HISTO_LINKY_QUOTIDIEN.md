# Histo Linky Quotidien + Ecart J-1

**Catégorie :** energie
**Alias HA :** `[P0] Histo Linky quotidien + Ecart J-1`

## Description

Enregistre chaque nuit à 23h59 la consommation Linky J-1 (`day_1`) dans `/config/notifs/linky_histo.txt`.
Si `day_1 = 0` (Enedis n'a pas encore publié les données) : écrit `(MANQUANT)` pour permettre le rattrapage par l'automation `rattrapage_linky_ecart`.
Si `day_1 > 0` : calcule et logue aussi l'écart Linky/Nodon dans `/config/notifs/ecart_histo.txt`.

Formats de lignes :
- Normal : `JJ/MM | Linky : X.XX kWh`
- Manquant : `JJ/MM | Linky : 0.00 kWh (MANQUANT)`
- Ecart : `JJ/MM | Linky: X.XX kWh | Nodon: X.XX kWh | Ecart: X.XX (X.X%)`

## Déclencheurs

- `time` 23:59:00

## Entités principales

- `sensor.linky_25481620821301_consumption` (attr `day_1`)
- `sensor.genelec_appart_quotidien_um` (attr `last_period`)
- `notify.send_message` -> `notify.log_linky_histo` -> `/config/notifs/linky_histo.txt`
- `notify.send_message` -> `notify.log_ecart_histo` -> `/config/notifs/ecart_histo.txt`

## Fichier source

`energie/histo_linky_quotidien.yaml`

## Prérequis

Intégrations File créées dans l'UI HA : Paramètres > Appareils > Ajouter intégration > File
- Nom : `log_linky_histo` | Fichier : `/config/notifs/linky_histo.txt`
- Nom : `log_ecart_histo` | Fichier : `/config/notifs/ecart_histo.txt`

---
*Doc créée le 2026-09-01*
