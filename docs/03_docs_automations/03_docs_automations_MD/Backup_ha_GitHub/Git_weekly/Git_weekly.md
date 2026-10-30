# [BACKUP] GIT - PUSH HEBDO + TAG (DIM 01H30)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-ff9800?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Backup_ha_GitHub/03_backup_git_weekly_dim_01_30/03_backup_git_weekly_dim_01_30.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Chaque dimanche à 01h30 : push Git avec création d'un tag hebdomadaire.
Notifie sur mobile avec confirmation.

---

## ⚡ Déclencheurs

| Type | Horaire |
|:---|:---|
| `time` | 01:30:00 |

---

## 🔒 Conditions

- `weekday: sun`

---

## ⚙️ Actions

1. `shell_command.git_backup_push_weekly`
2. `system_log.write` (level: info)
3. Notification `🚀 Sauvegarde Git` / `Backup hebdo & tag -> GitHub.`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `shell_command.git_backup_push_weekly` | Script push + tag hebdo |
