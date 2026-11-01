# AUDIT_MD5_YAML - Script d'audit MD5 des YAML, PROD vs GitHub

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--01-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

> **Doublon (decide par Eric le 2026-11-01) :** fiches qui decrivent le meme audit MD5 : `04_docs_scripts_SH_MD/Audit_md5/Audit_md5.md` (audit_md5.sh), `04_docs_scripts_YAML_MD/Audit_md5/Audit_md5.md` (script Home Assistant), `01_docs_config_system/01_config_system_MD/.scripts/01_scripts.sh_md/Audit_md5_yaml/Audit_md5_yaml.md` (fiche historique du meme script) et `04_docs_scripts_SH_MD/Audit_md5_yaml/Audit_md5_yaml.md` (cette fiche, une par script).
> Toute modification se fait dans toutes les fiches listees.

> **Script shell :** `audit_md5_yaml.sh`
> **Source locale :** `docs/04_docs_scripts/04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh`
> **Emplacement prod :** `/config/.scripts/audit_md5_yaml.sh` (copie identique au local, releve du 2026-11-01)
> **Appelé par :** `shell_command.audit_md5` (`shell_command/GitHub/GitHub_backup_GitHub.yaml`, ligne 52 : `bash /config/.scripts/audit_md5_yaml.sh`, relevé dans la prod le 2026-11-01), lui-même lancé par le script Home Assistant `audit_md5` (index GLOBAL_INDEX_SCRIPTS_SH)
> **Dernière modif :** fiche créée le 2026-11-01

---

## 📝 Description

Même principe que `audit_md5.sh` : compare chaque fichier YAML entre la prod HA (`/config/`) et le dépôt GitHub (`home_assistant_re-build/main`) en 3 passes (tree, MD5 prod, MD5 GitHub), avec les statuts `SYNC`, `DIFF` et `PUSH MANQUANT`. Le fichier `Audit_md5.md` décrit les passes en détail.

**Différences relevées dans le script :**

| Point | `audit_md5_yaml.sh` |
|:------|:----------------------|
| Log | `/config/.logs/md5_audit_yaml_AAAA-MM-JJ.txt` |
| Rotation | supprime les anciens `md5_audit_yaml_*.txt` avant d'écrire |
| Répertoires audités | `sensors templates utility_meter command_line shell_command packages groups input_booleans input_number timers` |
| Fichiers racine | `automations.yaml scripts.yaml configuration.yaml sql.yaml input_select.yaml input_datetime.yaml input_button.yaml` |
| Option shell | `set -euo pipefail` |

---

## ⚠️ Points d'attention

- `timers` fait partie des répertoires audités ici ; la fiche `Audit_md5.md` ne le cite pas dans son périmètre.
- Un timeout de curl peut faire apparaître un fichier en `PUSH MANQUANT` à tort : relancer l'audit.
- `secrets.yaml` n'est jamais dans le périmètre.

---

*Fiche créée le 2026-11-01 à la demande d'Eric (une fiche par script, même si elle fait doublon).*