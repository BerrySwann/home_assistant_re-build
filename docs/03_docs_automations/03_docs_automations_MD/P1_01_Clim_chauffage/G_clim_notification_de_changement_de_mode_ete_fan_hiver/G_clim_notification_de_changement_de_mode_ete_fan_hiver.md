# (G) NOTIFICATION CHANGEMENT DE MODE ÉTÉ/FAN/HIVER

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-4fc3f7?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/P1_01_CLIM_CHAUFFAGE/g_clim_notification_de_changement_de_mode_ete_fan_hiver/g_clim_notification_de_changement_de_mode_ete_fan_hiver.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Simple notification lors d'un changement de saison (heat / cool / fan_only).
Lit `sensor.mode_ete_hiver_etat` pour un texte lisible.

---

## ⚡ Déclencheurs

| Type | Entité |
|:---|:---|
| `state` | `sensor.mode_ete_hiver` |

---

## ⚙️ Actions

1. Pause 3s
2. Notification `CHANGEMENT DE MODE` avec `sensor.mode_ete_hiver_etat | upper`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.mode_ete_hiver` | Déclencheur |
| `sensor.mode_ete_hiver_etat` | Texte lisible du mode |
