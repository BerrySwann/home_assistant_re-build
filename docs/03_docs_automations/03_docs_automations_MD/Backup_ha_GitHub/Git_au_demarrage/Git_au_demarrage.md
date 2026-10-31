# [BACKUP] GIT - PUSH AU DÉMARRAGE HA

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

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Backup_ha_GitHub/git_push_au_demarrage_ha/git_push_au_demarrage_ha.yaml`
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

1. `delay: 30s` - attente stabilisation réseau
2. `shell_command.git_backup_push` - push Git (mode auto)
3. `system_log.write` (level: info) - `[Backup] Démarrage HA - push Git exécuté`

---

## 🔌 DÉPENDANCES

| Entité | Rôle |
|:---|:---|
| `shell_command.git_backup_push` | Script shell défini dans `shell_command.yaml` |
