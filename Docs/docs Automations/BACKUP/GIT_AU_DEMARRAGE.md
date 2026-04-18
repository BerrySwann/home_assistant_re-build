# [BACKUP] GIT — PUSH AU DÉMARRAGE HA

> **Fichier :** `automations_corrige/backup/git_au_demarrage.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Déclenche un push Git immédiatement lors du démarrage de Home Assistant.
Garantit un snapshot au boot.

---

## ⚡ Déclencheurs

| Type | Événement |
|:---|:---|
| `homeassistant` | `start` |

---

## ⚙️ Actions

1. `shell_command.git_backup_push`
2. `system_log.write` (level: info)

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `shell_command.git_backup_push` | Script shell défini dans `shell_command.yaml` |
