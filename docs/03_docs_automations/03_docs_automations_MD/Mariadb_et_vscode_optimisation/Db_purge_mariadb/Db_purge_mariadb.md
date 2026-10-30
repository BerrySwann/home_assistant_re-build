# DB PURGE MARIADB + REPACK

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** `docs/03_docs_automations/03_docs_automations_YAML/Mariadb_et_vscode_optimisation/db_purge_mariadb_repack/db_purge_mariadb_repack.yaml`
> **Mode HA :** `single`

---

## 📝 Description

Ménage nocturne automatique de MariaDB à 00:30. Conserve 7 jours d'historique
et repack la base pour libérer l'espace disque.

---

## ⚡ Déclencheurs

| Type | Horaire |
|:---|:---|
| `time` | 00:30:00 |

---

## ⚙️ Actions

- `recorder.purge` : `keep_days: 7`, `repack: true`

---

## 🔌 DÉPENDANCES

Aucune entité externe. Utilise uniquement le service HA natif `recorder.purge`.
