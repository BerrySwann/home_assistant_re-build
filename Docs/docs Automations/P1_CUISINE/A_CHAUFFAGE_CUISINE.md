# (A) CHAUFFAGE CUISINE — PLAGES HORAIRES SEMAINE/WE

> **Fichier :** `automations_corrige/P1_cuisine/A_chauffage_cuisine.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Gère le radiateur bain d'huile de la cuisine sur deux plages horaires :
- Semaine LMMJ : 04:45–07:00 (thermostat 19,9°–20,5°)
- Week-end VSD : 05:45–08:00 (thermostat 19,9°–20,5°)

Requiert la présence d'au moins Eric OU Mamour (zone.home).

---

## ⚡ Déclencheurs

| Type | Horaire / Entité |
|:---|:---|
| `time` | 04:45:00 |
| `time` | 05:45:00 |
| `time` | 07:00:00 (arrêt forcé semaine) |
| `time` | 08:00:00 (arrêt forcé WE) |
| `numeric_state` | `sensor.th_cuisine_temperature` < 19.9 |
| `numeric_state` | `sensor.th_cuisine_temperature` > 20.5 |

---

## 🔒 Conditions globales

- Eric OU Mamour dans `zone.home`
- Plage horaire (semaine ou WE) validée par `condition.time` + `weekday`

---

## ⚙️ Actions — Choose

| Cas | Action |
|:---|:---|
| Fin semaine 07:00 (LMMJ) | `climate.set_hvac_mode: off` + notif |
| Fin WE 08:00 (VSD) | `climate.set_hvac_mode: off` + notif |
| T° < 19,9° | `climate.set_hvac_mode: heat` + notif |
| T° > 20,5° | `climate.set_hvac_mode: off` + notif |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_cuisine_temperature` | Thermostat cuisine |
| `climate.radiateur_cuisine` | Radiateur bain d'huile |
| `person.eric` / `person.mamour` | Présence zone.home |
| `zone.home` | Zone domicile |

### Notifications

Toutes vers `notify.mobile_app_eric` avec `/!\ RADIATEUR CUISINE est 'ON/OFF' /!\`
