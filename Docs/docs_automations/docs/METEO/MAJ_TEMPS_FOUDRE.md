# METTRE À JOUR LE TEMPS DU DERNIER IMPACT FOUDRE

> **Fichier :** `automations_corrige/meteo/maj_temps_foudre.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Enregistre l'heure exacte du dernier impact de foudre dans `input_datetime.dernier_eclair`
à chaque changement du compteur Blitzortung.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.maison_lightning_counter` |

---

## 🔒 Conditions

- `sensor.maison_lightning_counter | int > 0`

---

## ⚙️ Actions

- `input_datetime.set_datetime` → `input_datetime.dernier_eclair` = `now().isoformat()`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.maison_lightning_counter` | Compteur impacts Blitzortung |
| `input_datetime.dernier_eclair` | Helper datetime dernier éclair |
