# [P3-SALON] BOUTON IKEA SOMRIG (2 TOUCHES) — ON/OFF

> **Fichier :** `automations_corrige/P3_salon_bouton_inter_somrig.yaml`
> **Mode HA :** `restart`

---

## 📝 Description

Même rôle que l'Inter IKEA 4 touches, mais via le bouton SOMRIG 2 touches.
Mappage différent : `1_short_release` → ON, `2_short_release` → OFF.

---

## ⚡ Déclencheurs

| Type | Topic MQTT |
|:---|:---|
| `mqtt` | `zigbee2mqtt/Inter (SOMRIG)/action` |

---

## ⚙️ Actions — Choose

| Action MQTT | Résultat |
|:---|:---|
| `1_short_release` | `input_boolean.turn_on → input_boolean.inter_lumiere_salon` |
| `2_short_release` | `input_boolean.turn_off → input_boolean.inter_lumiere_salon` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Inter (SOMRIG)/action` | Bouton physique |
| `input_boolean.inter_lumiere_salon` | Helper état lumière salon |
