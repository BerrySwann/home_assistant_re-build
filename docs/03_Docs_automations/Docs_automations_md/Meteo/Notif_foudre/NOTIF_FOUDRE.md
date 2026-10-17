# NOTIFICATION FOUDRE - DISTANCE, DIRECTION, IMPACTS

> **Fichier :** `docs/03_docs_automations/docs_automations_YAML/Meteo/notification_de_la_foudre/notification_de_la_foudre.yaml`
> **ID HA :** `1775243260631` (`automation.notification_de_la_foudre`)
> **Mode HA :** `single`
> **MàJ :** 2026-10-11 (fiche corrigée d'après le YAML, identique à H:\automations.yaml)

---

## Description

Alerte sur le téléphone d'Eric (`notify.mobile_app_eric`) à chaque changement du compteur de foudre : distance en km, ville si le géocodage est disponible, sinon direction (16 points cardinaux calculés depuis l'azimut), date du dernier éclair et nombre d'impacts. Pause de 1 min après la notification (anti-spam, mode `single`).

---

## Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.maison_lightning_counter` (tout changement d'état) |

---

## Conditions

- `sensor.maison_lightning_counter` au-dessus de 0 (`numeric_state`).

---

## Actions

1. `homeassistant.update_entity` sur `sensor.blitzortung_lightning_localisation` (rafraîchit le géocodage).
2. Notification `notify.mobile_app_eric`, titre "/!\ Attention foudre /!\" :
   - ville : lue dans l'attribut `features[0].properties.geocoding.city` de `sensor.blitzortung_lightning_localisation`, si l'état n'est pas `0` ;
   - phrase : "Un éclair a été détecté à X Km de la maison à <ville>." ; sans ville, "... Km" suivi de la direction (nord, nord-nord-est, ... nord-nord-ouest, 16 secteurs d'après l'azimut) ; sans azimut, "... Km." ; si la distance est 0, "Pas d'impact de foudre détecté." ;
   - ajoute la valeur de `input_datetime.dernier_eclair` et "N impact(s) détecté(s)" si le compteur est au-dessus de 0.
3. `delay: 00:01:00`.

---

## Dépendances

| Entité | Rôle |
|:---|:---|
| `sensor.maison_lightning_counter` | Déclencheur, condition et nombre d'impacts |
| `sensor.maison_lightning_distance` | Distance en km |
| `sensor.maison_lightning_azimuth` | Azimut en degrés (direction) |
| `sensor.blitzortung_lightning_localisation` | Géocodage (ville) ; rafraîchi par `update_entity` |
| `input_datetime.dernier_eclair` | Date et heure du dernier éclair, ajoutées au message |
| `notify.mobile_app_eric` | Notification (seul Eric est notifié) |

---

## Notes

- L'ancienne fiche citait `sensor.maison_lightning_localisation` et `sensor.dernier_impact_temps_reel` : ces deux entités n'existent pas dans HA (vérifié le 2026-10-11) et ne sont pas dans le YAML.
- Le texte du message contient une faute de langue dans le YAML : la direction 146-169 degrés s'affiche "au sud-south-est" (au lieu de "sud-sud-est").
- La mise à jour de `input_datetime.dernier_eclair` est faite par une autre automation (voir `MAJ_TEMPS_FOUDRE.md`), pas par celle-ci.