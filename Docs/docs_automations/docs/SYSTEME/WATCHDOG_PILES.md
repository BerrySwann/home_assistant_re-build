# SYSTÈME — WATCHDOG PILES (HUE/IKEA/SONOFF)

> **Fichier :** `automations_corrige/systeme/watchdog_piles.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Vérification 3×/jour des batteries des équipements Zigbee.
Parcourt les groupes `group.hue_devices`, `group.ikea_devices`, `group.sonoff_devices`
et notifie si batterie ≤ 11%.

---

## ⚡ Déclencheurs

| Type | Horaire |
|:---|:---|
| `time` | 08:00 / 14:00 / 20:00 |

---

## ⚙️ Actions

1. Calcul variable `low_batt` : liste des entités ≤ 11% dans les 3 groupes
2. Si liste non vide → notification `🪫 Alerte Pile Faible (<10%)` avec nom + %

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `group.hue_devices` | Groupe ampoules Hue |
| `group.ikea_devices` | Groupe équipements IKEA |
| `group.sonoff_devices` | Groupe capteurs SONOFF |
