# Z2M LAST SEEN - SURVEILLANCE CAPTEURS ZIGBEE

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Contrôle Entity z2m/z2m_last_seen/z2m_last_seen.yaml`
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
