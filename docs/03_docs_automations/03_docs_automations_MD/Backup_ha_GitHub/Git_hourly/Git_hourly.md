# [BACKUP] GIT - PUSH HORAIRE (H+10)

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Backup_ha_GitHub/01_backup_git_hourly_h_10/01_backup_git_hourly_h_10.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Push Git toutes les heures à H+10 (ex: 08:10, 09:10...).

---

## ⚡ Déclencheurs

| Type | Pattern |
|:---|:---|
| `time_pattern` | `minutes: /10` (toutes les heures) |

---

## ⚙️ Actions

1. `shell_command.git_backup_push`
2. `system_log.write` (level: info)

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `shell_command.git_backup_push` | Script push Git |
