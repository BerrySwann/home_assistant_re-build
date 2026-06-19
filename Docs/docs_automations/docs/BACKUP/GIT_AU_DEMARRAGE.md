# [BACKUP] GIT — PUSH AU DÉMARRAGE HA

> **Fichier :** `TREE_CORRIGE/backup/git_push_au_demarrage_ha.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Déclenche un push Git au démarrage de Home Assistant, après un délai de 30s
pour laisser le réseau se stabiliser. Garantit un snapshot au boot.
Si le push échoue, l'automation horaire H+10 prend le relai automatiquement.

---

## ⚡ Déclencheurs

| Type | Événement |
|:---|:---|
| `homeassistant` | `start` |

---

## ⚙️ Actions

1. `delay: 30s` — attente stabilisation réseau
2. `shell_command.git_backup_push` — push Git (mode auto)
3. `system_log.write` (level: info) — `[Backup] Démarrage HA — push Git exécuté`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `shell_command.git_backup_push` | Script shell défini dans `shell_command.yaml` |
