# SYSTÈME - WATCHDOG PILES (HUE/IKEA/SONOFF)

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Watchdog_Piles_HUE_IKEA_SONOFF/systeme_watchdog_piles_hue_ikea_sonoff/systeme_watchdog_piles_hue_ikea_sonoff.yaml`
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
