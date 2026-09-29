# Watchdog Sécurité Radiateur SDB

**Catégorie :** P1_sdb
**Alias HA :** `D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR`

## Description

Surveillance de la chauffe du soufflant de la salle de bain. Si l'appareil est alimenté, que
l'interrupteur est en marche, que la pièce dépasse 25 degrés et qu'elle vient de monter de
0,5 degré, l'automation envoie une minute plus tard l'ordre d'arrêt infrarouge, éteint
l'interrupteur, puis coupe la prise après une minute supplémentaire, et prévient le téléphone.
Elle ne refuse pas un démarrage, elle agit pendant la chauffe.

## Déclencheurs

- `state` sur `sensor.th_salle_de_bain_temperature`

## Conditions

- `switch.prise_soufflant_salle_de_bain_nous` sur `on`
- `input_boolean.inter_soufflant_salle_de_bain` sur `on`
- `sensor.th_salle_de_bain_temperature` au-dessus de 25
- hausse d'au moins 0,5 degré entre deux mesures consécutives

## Entités principales

- `sensor.th_salle_de_bain_temperature`
- `switch.prise_soufflant_salle_de_bain_nous`
- `input_boolean.inter_soufflant_salle_de_bain`
- `remote.soufflant_sdb`
- `notify.mobile_app_eric`

## État au 2026-09-29

Réactivée le 2026-09-29 après avoir été éteinte. Elle n'a jamais déclenché : son compteur
d'exécutions est à zéro. La condition de hausse de 0,5 degré est infaisable avec ce capteur, qui
remonte par pas de 0,2. Depuis que le script de démarrage refuse de démarrer au-dessus de
25 degrés, cette condition de dérive est devenue inutile, et les trois autres suffisent.

## Fichier source

`docs_automations_YAML/P1_sdb/d_salle_de_bain_watchdog_securite_radiateur_2026-09-10.yaml`

---
*Doc générée le 2026-05-30, complétée le 2026-09-29.*
