# [BACKUP] ALERTE SI KO 15 MIN

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Backup_ha_GitHub/00_backup_alerte_si_ko_15_min/00_backup_alerte_si_ko_15_min.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Notification persistante si le capteur de statut backup reste à `KO`
pendant plus de 15 minutes. Pointe vers le fichier de log.

---

## ⚡ Déclencheurs

| Type | Entité | État | Durée |
|:---|:---|:---|:---|
| `state` | `sensor.backup_github_status` | `KO` | 15 min |

---

## ⚙️ Actions

- `persistent_notification.create` : `Échec ou pas de commit depuis 15 min.`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `sensor.backup_github_status` | Capteur état backup (défini dans sensors ou command_line) |
