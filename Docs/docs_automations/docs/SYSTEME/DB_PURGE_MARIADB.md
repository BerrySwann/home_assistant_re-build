# DB PURGE MARIADB + REPACK

> **Fichier :** `automations_corrige/systeme/db_purge_mariadb.yaml`
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
