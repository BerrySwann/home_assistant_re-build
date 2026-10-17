# UPDATE PREVIOUS HUMIDITY - TENDANCE HUMIDITÉ EXT

> **Fichier :** `docs/03_docs_automations/docs_automations_YAML/Meteo/update_previous_humidity/update_previous_humidity.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Miroir de `update_prev_temperature` pour l'humidité extérieure.
Snapshot toutes les 30 min pour calcul de tendance.

---

## ⚡ Déclencheurs

| Type | Pattern |
|:---|:---|
| `time_pattern` | `minutes: /30` |

---

## ⚙️ Actions

- `input_number.set_value → input_number.th_balcon_nord_humidity_previous`
  valeur = `sensor.th_balcon_nord_humidity | float(0)`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_humidity` | Source humidité ext |
| `input_number.th_balcon_nord_humidity_previous` | Helper snapshot |
