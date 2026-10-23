# Histo Nodon Complet Quotidien

**Catégorie :** energie
**Alias HA :** `E - [P0] Histo Nodon complet quotidien (Total HP HC Cout)`
**ID HA :** `1792780906393`

## Description

Enregistre chaque nuit à 23h59m10s la consommation Nodon complète de la veille (Total, HP, HC) et son coût dans `/config/notifs/nodon_complet_histo.txt` via l'intégration File `notify.nodon_complet_histo`.

Ce fichier sert de source de remplacement quand le tableau hebdomadaire de L2C1 (capteurs `linky_jour_1` à `linky_jour_7`) affiche 0 parce qu'Enedis n'a pas publié le relevé Linky. Il complète `nodon_histo.txt` (qui ne contient que le total) avec le split HP/HC et le coût.

Formats de ligne :
- `JJ/MM | Total: X.X kWh | HP: X.X | HC: X.X | Cout: X.XX`
- total à 0 : `JJ/MM | Total: 0.0 kWh | HP: 0.0 | HC: 0.0 | Cout: 0.0 (MANQUANT)`

Le coût = HP x `sensor.tarif_heures_pleines_ttc` + HC x `sensor.tarif_heures_creuses_ttc` (tarifs EDF HPHC 6kVA TTC lus en direct, rien en dur).

## Déclencheurs

- `time` 23:59:10 (après A, B et C qui tournent à 23:59:00)

## Entités principales

- `sensor.genelec_appart_quotidien_um` (attr `last_period`) : total
- `sensor.genelec_appart_hphc_quotidien_um_hp` (attr `last_period`) : HP
- `sensor.genelec_appart_hphc_quotidien_um_hc` (attr `last_period`) : HC
- `sensor.tarif_heures_pleines_ttc`, `sensor.tarif_heures_creuses_ttc` : tarifs
- `notify.send_message` -> `notify.nodon_complet_histo` -> `/config/notifs/nodon_complet_histo.txt`

## Fichier source

`docs\03_Docs_automations\Docs_automations_yaml\P0_Enrige\Histo_nodon_complet_quotidien\Histo_nodon_complet_quotidien.yaml`

## Prérequis

Intégration File créée dans l'UI HA : Paramètres > Appareils > Ajouter intégration > File
- Nom : `nodon_complet_histo` | Fichier : `/config/notifs/nodon_complet_histo.txt` | horodatage désactivé

## Notes

- Les valeurs sont celles de la veille (`last_period`), la ligne est donc datée J-1, comme `linky_histo.txt` et `nodon_histo.txt`.
- Le fichier se remplit à partir du 23/10/2026 (première ligne : 22/10). Les jours antérieurs n'ont pas de split HP/HC.
- Évolution prévue : un capteur command_line qui lit ce fichier et les templates `linky_jour_1` à `linky_jour_7` qui l'utilisent comme valeur de remplacement (avec une * sur le jour).

---
*Doc créée le 2026-10-23*