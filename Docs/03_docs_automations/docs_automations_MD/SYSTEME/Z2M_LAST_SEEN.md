# Z2M LAST SEEN — SURVEILLANCE CAPTEURS ZIGBEE

> **Fichier :** `automations_corrige/systeme/z2m_last_seen.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Surveille les capteurs Zigbee via leurs entités `last_seen`. Alerte si un capteur
est indisponible ou n'a pas répondu depuis plus de 8h (configurable via variable `hours`).

---

## ⚡ Déclencheurs

| Type | Condition |
|:---|:---|
| `time` | 06:00:00 |
| `time_pattern` | `minutes: /15` |

---

## 🔒 Conditions

- Template : `sensors != ''` ET condition sur `day` (0 = tous les jours)

---

## ⚙️ Variables configurables

| Variable | Valeur par défaut | Rôle |
|:---|:---|:---|
| `day` | `0` | Jour de la semaine (0 = tous) |
| `hours` | `8` | Seuil d'inactivité en heures |
| `exclude.entity_id` | `[]` | Liste d'exclusions |

---

## ⚙️ Actions

- Notification `⚠️ Problème capteur Zigbee` avec liste des capteurs KO

---

## 🔌 DÉPENDANCES

Parcourt dynamiquement **tous** les `sensor` avec `device_class: timestamp`
ayant `last_seen` dans leur `entity_id`.

| Dépendance | Rôle |
|:---|:---|
| Tous les `sensor.*_last_seen` (Zigbee2MQTT) | Capteurs surveillés |
