# [BACKUP] GIT — PUSH HORAIRE (H+10)

> **Fichier :** `automations_corrige/backup/git_hourly.yaml`
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
