# GESTION PC BUREAU — SCÈNE DE FIN + NOTIF

> **Fichier :** `docs_automations/TREE_CORRIGE/P2_prises/gestion_pc_bureau.yaml`
> **Mode HA :** `parallel`
> **MàJ :** 2026-05-17

---

## 📝 Description

Gestion du cycle PC bureau : allumage/extinction via bouton MQTT (Poussoir IKEA TRADFRI)
ou détection veille < 40W pendant 2 min. Pilote uniquement l'éclairage `light.hue_smart_eco_pc_bureau`.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt/Poussoir PC (IKEA TRADFRI)/action` |
| `extinction_conso` | `numeric_state` | `sensor.prise_bureau_pc_ikea_power` < 40W pendant 2 min |

---

## ⚙️ Actions — Choose

**ALLUMAGE (bouton ON) :**
- `light.turn_on → light.hue_smart_eco_pc_bureau`

**EXTINCTION (bouton OFF ou veille < 40W) :**
- `light.turn_off → light.hue_smart_eco_pc_bureau`
- Notification `Veille détectée` / `PC Bureau [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Poussoir PC (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_bureau_pc_ikea_power` | Puissance (détection veille) |
| `light.hue_smart_eco_pc_bureau` | Éclairage bureau PC |

### Notifications

| Titre | Message |
|:---|:---|
| `Veille détectée` | `PC Bureau [OFF]` (tag: notif_pc_bureau) |

---

## ⚠️ Notes techniques

- Guard `trigger.payload_json is defined` obligatoire : le trigger `extinction_conso`
  (numeric_state) ne possède pas `payload_json` — sans le guard, UndefinedError au runtime.
