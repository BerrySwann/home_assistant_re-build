# BOUTON IKEA RODRET — TV CHAMBRE

> **Fichier :** `automations_corrige/P2_prises/rodret_tv_chambre.yaml`
> **Mode HA :** `restart`

---

## 📝 Description

Pilotage direct de la prise TV chambre via le bouton RODRET.
Traduit `on`/`off` MQTT en `switch.turn_on/off` direct (sans passer par un helper).

---

## ⚡ Déclencheurs

| Type | Topic MQTT |
|:---|:---|
| `mqtt` | `zigbee2mqtt/Inter TV Chambre (IKEA RODRET)` |

---

## ⚙️ Actions — Choose

| Action MQTT | Résultat |
|:---|:---|
| `on` | `switch.turn_on → switch.prise_tv_chambre_nous` |
| `off` | `switch.turn_off → switch.prise_tv_chambre_nous` |

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| MQTT `zigbee2mqtt/Inter TV Chambre (IKEA RODRET)` | Bouton physique |
| `switch.prise_tv_chambre_nous` | Prise TV chambre |

---

## ⚠️ Interaction avec gestion_tv_chambre.yaml

Les deux automations écoutent le même topic MQTT. `gestion_tv_chambre` gère
l'ambiance lumière + la détection veille. `rodret_tv_chambre` ne gère que
la prise. Assurer la cohérence pour éviter les conflits.
