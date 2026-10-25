# DB PURGE MARIADB + REPACK

> **Fichier :** `docs/03_docs_automations/03_docs_automations_yaml/Mariadb_et_vscode_optimisation/db_purge_mariadb_repack/db_purge_mariadb_repack.yaml`
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
