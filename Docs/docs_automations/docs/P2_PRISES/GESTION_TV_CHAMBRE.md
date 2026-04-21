# GESTION TV CHAMBRE — SCÈNE DE FIN + NOTIF

> **Fichier :** `automations_corrige/P2_prises/gestion_tv_chambre.yaml`
> **Mode HA :** `parallel`

---

## 📝 Description

Gestion du cycle TV chambre. Allumage via bouton MQTT ou auto à 21h00.
Extinction détectée par veille < 20W pendant 2 min. L'éclairage ambiance
Hue TV chambre est couplé à la TV.

---

## ⚡ Déclencheurs

| ID | Type | Condition |
|:---|:---|:---|
| `bouton_mqtt` | `mqtt` | `zigbee2mqtt/Inter TV Chambre (IKEA RODRET)` |
| `allumage_auto` | `time` | 21:00:00 |
| `extinction_conso` | `numeric_state` | `sensor.prise_tv_chambre_nous_power` < 20W / 2 min |

---

## ⚙️ Actions — Choose

**ALLUMAGE (bouton ON ou 21h00) :**
- `light.turn_on → light.hue_smart_tv_chambre`
- `switch.turn_on → switch.prise_tv_chambre_nous`

**EXTINCTION (bouton OFF ou veille) :**
- `light.turn_off → light.hue_smart_tv_chambre`
- Notification `Veille détectée` / `Prise TV [OFF]`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Inter TV Chambre (IKEA RODRET)` | Bouton physique |
| `sensor.prise_tv_chambre_nous_power` | Puissance TV |
| `switch.prise_tv_chambre_nous` | Prise TV |
| `light.hue_smart_tv_chambre` | Ambiance lumière chambre |

### Notifications

| Titre | Message |
|:---|:---|
| `Veille détectée` | `Prise TV [OFF]` (tag: notif_tv_chambre) |
