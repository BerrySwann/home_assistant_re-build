# ÉNERGIE — SURVEILLANCE GROS ÉLECTRO EN HP

> **Fichier :** `automations_corrige/energie/surveillance_gros_electro_hp.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Alerte si le lave-linge ou le lave-vaisselle démarre pendant les Heures Pleines.
Le départ différé n'a pas été activé — notification de rappel avec heure exacte.

---

## ⚡ Déclencheurs

| Type | Entité | Seuil | Durée |
|:---|:---|:---|:---|
| `numeric_state` | `sensor.prise_lave_linge_nous_power` | > 100W | 2 min |
| `numeric_state` | `sensor.prise_lave_linge_nous_power` | > 100W | 2 min |

> ⚠️ **Doublon** : les deux déclencheurs pointent vers le lave-linge. Le lave-vaisselle (`sensor.prise_lave_vaisselle_nous_power`) est absent — à corriger.

---

## 🔒 Conditions

- `binary_sensor.heures_creuses_electriques == off` (on est en HP)

---

## ⚙️ Actions

- Notification `⚡ Alerte Conso. HP` avec heure actuelle

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.prise_lave_linge_nous_power` | Puissance lave-linge |
| `binary_sensor.heures_creuses_electriques` | État HC/HP |

---

## ⚠️ Bug identifié

Le déclencheur lave-vaisselle (`sensor.prise_lave_vaisselle_nous_power`) est
manquant — remplacé par erreur par un doublon du lave-linge.
