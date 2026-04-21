# [P3-SALON] BOUTON IKEA INTER SALON (4 TOUCHES) — ON/OFF

> **Fichier :** `automations_corrige/P3_salon_bouton_inter_ikea_4.yaml`
> **Mode HA :** `restart`

---

## 📝 Description

Pilotage de `input_boolean.inter_lumiere_salon` via le bouton IKEA 4 touches.
Le `input_boolean` sert d'interrupteur virtuel qui déclenche la logique
d'éclairage salon en aval.

---

## ⚡ Déclencheurs

| Type | Topic MQTT |
|:---|:---|
| `mqtt` | `zigbee2mqtt/Inter Salon (4) (IKEA)/action` |

---

## ⚙️ Actions — Choose

| Action MQTT | Résultat |
|:---|:---|
| `on` | `input_boolean.turn_on → input_boolean.inter_lumiere_salon` |
| `off` | `input_boolean.turn_off → input_boolean.inter_lumiere_salon` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Inter Salon (4) (IKEA)/action` | Bouton physique |
| `input_boolean.inter_lumiere_salon` | Helper état lumière salon |
