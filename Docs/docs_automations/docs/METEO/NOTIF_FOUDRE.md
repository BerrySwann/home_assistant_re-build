# NOTIFICATION FOUDRE — DISTANCE, DIRECTION, IMPACTS

> **Fichier :** `automations_corrige/meteo/notif_foudre.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Alerte mobile complète sur la foudre : distance en km, direction (16 points cardinaux
via azimut), ville si géocodage disponible, nombre d'impacts.
Délai anti-spam de 1 min après notification.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.maison_lightning_counter` |

---

## 🔒 Conditions

- `sensor.maison_lightning_counter > 0`

---

## ⚙️ Actions

1. `homeassistant.update_entity → sensor.maison_lightning_localisation`
2. Notification complexe avec calcul direction 16 points + géocodage
3. `delay: 00:01:00`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.maison_lightning_counter` | Déclencheur |
| `sensor.maison_lightning_distance` | Distance en km |
| `sensor.maison_lightning_azimuth` | Azimut (degrés) |
| `sensor.maison_lightning_localisation` | Géocodage ville |
| `sensor.dernier_impact_temps_reel` | Texte "il y a X min" |
