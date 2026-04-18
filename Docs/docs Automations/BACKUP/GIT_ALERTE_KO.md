# [BACKUP] ALERTE SI KO 15 MIN

> **Fichier :** `automations_corrige/backup/git_alerte_ko.yaml`
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
