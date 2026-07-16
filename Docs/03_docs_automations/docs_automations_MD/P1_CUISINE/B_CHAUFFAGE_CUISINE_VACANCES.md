# (B) CHAUFFAGE CUISINE VACANCES

> **Fichier :** `automations_corrige/P1_cuisine/B_chauffage_cuisine_vacances.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Version vacances du chauffage cuisine. Plage unique 06:00–08:30,
7 jours/7. Requiert la présence des deux (Eric ET Mamour).

---

## ⚡ Déclencheurs

| Type | Entité / Horaire |
|:---|:---|
| `time` | 06:00:00 |
| `numeric_state` | `sensor.th_cuisine_temperature` < 19.9 |
| `numeric_state` | `sensor.th_cuisine_temperature` > 20.5 |

---

## 🔒 Conditions (dans choose)

- Eric ET Mamour dans `zone.home`
- `06:00 < heure < 08:30`
- T° < 19,9° ou > 20,5°

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.th_cuisine_temperature` | T° cuisine |
| `climate.radiateur_cuisine` | Radiateur |
| `person.eric` / `person.mamour` | Présence (ET obligatoire) |
