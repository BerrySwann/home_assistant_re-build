# GESTION PC BUREAU — SCÈNE DE FIN + NOTIF

> **Fichier :** `automations_corrige/P2_prises/gestion_pc_bureau.yaml`
> **Mode HA :** `parallel`

---

## 📝 Description

Gestion du cycle PC bureau : allumage via bouton MQTT ou détection veille.
Coupe l'alim bureau (hue_smart_eco) mais laisse la prise IKEA active pour
le suivi de consommation.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt/Poussoir (IKEA TRADFRI)/action` |
| `extinction_conso` | `numeric_state` | `sensor.prise_bureau_pc_ikea_power` < 80W pendant 2 min |

---

## ⚙️ Actions — Choose

**ALLUMAGE (bouton ON) :**
- `switch.turn_on → switch.hue_smart_eco_pc_bureau`
- `switch.turn_on → switch.prise_bureau_pc_ikea`

**EXTINCTION (bouton OFF ou veille < 80W) :**
- `switch.turn_off → switch.hue_smart_eco_pc_bureau`
- Notification `Veille détectée` / `PC Bureau [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Poussoir (IKEA TRADFRI)/action` | Bouton physique |
| `sensor.prise_bureau_pc_ikea_power` | Puissance (détection veille) |
| `switch.hue_smart_eco_pc_bureau` | Alim principale PC |
| `switch.prise_bureau_pc_ikea` | Prise suivi conso |

### Notifications

| Titre | Message |
|:---|:---|
| `Veille détectée` | `PC Bureau [OFF]` (tag: notif_pc_bureau) |
