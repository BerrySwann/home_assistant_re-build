# [BACKUP] GIT — PUSH HEBDO + TAG (DIM 01H30)

> **Fichier :** `automations_corrige/backup/git_weekly.yaml`
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
