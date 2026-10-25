# Watchdog Sécurité Radiateur SDB

**Catégorie :** P1_sdb
**Alias HA :** `D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR`

## Description

Surveillance de la chauffe du soufflant de la salle de bain. Si l'appareil est alimenté, que
l'interrupteur est en marche, que la pièce dépasse 25 degrés et qu'elle vient de monter de
0,4 degré, l'automation envoie une minute plus tard l'ordre d'arrêt infrarouge, éteint
l'interrupteur, puis coupe la prise après une minute supplémentaire, et prévient le téléphone.
Elle ne refuse pas un démarrage, elle agit pendant la chauffe.

## Déclencheurs

- `state` sur `sensor.th_salle_de_bain_temperature`

## Conditions

- `switch.prise_soufflant_salle_de_bain_nous` sur `on`
- `input_boolean.inter_soufflant_salle_de_bain` sur `on`
- `sensor.th_salle_de_bain_temperature` au-dessus de 25
- hausse d'au moins 0,4 degré entre deux mesures consécutives

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

## État au 2026-10-07

Seuil de dérive passé de 0,5 à 0,4 degré par Eric le 2026-10-07 vers 18 h 10. Relu en direct dans
Home Assistant : alias et template à +0,4, automation activée, jamais déclenchée.

Efficacité non démontrée : la condition compare deux relevés consécutifs, et le capteur avance par
pas de 0,2. Le 2026-09-29, la chauffe montait de 0,2 par relevé (d'après la todo) : un seuil de 0,4
ne l'aurait probablement pas captée. L'historique du 29/09 n'est plus disponible dans Home
Assistant, donc non revérifié. Valeur à valider au premier cycle de chauffe de l'hiver.

Risque connu, non testé : si D se déclenche, elle envoie un IR `on_off` puis passe le booléen sur
off. Le switch template suit ce booléen, le routage lance alors `script.sdb_soufflant_arreter`, qui
envoie lui aussi un IR `on_off` quelques secondes plus tard. La prise est coupée à la fin dans tous
les cas ; l'effet du second `on_off` sur l'appareil est inconnu.

## Fichier source

`docs_automations_YAML/P1_sdb/d_salle_de_bain_watchdog_securite_radiateur_2026-09-10.yaml`

---
*Doc générée le 2026-05-30, complétée le 2026-09-29 et le 2026-10-07.*
