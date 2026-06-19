# UPDATE PREVIOUS TEMPERATURE — TENDANCE T° EXT

> **Fichier :** `automations_corrige/meteo/update_prev_temperature.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Snapshot de la température extérieure toutes les 30 min dans un `input_number`.
Utilisé pour calculer la tendance (hausse/baisse/stable) dans les sensors templates.

---

## ⚡ Déclencheurs

| Type | Pattern |
|:---|:---|
| `time_pattern` | `minutes: /30` |

---

## ⚙️ Actions

- `input_number.set_value → input_number.th_balcon_nord_temperature_previous`
  valeur = `sensor.th_balcon_nord_temperature | float(0)`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_balcon_nord_temperature` | Source T° ext |
| `input_number.th_balcon_nord_temperature_previous` | Helper snapshot |
