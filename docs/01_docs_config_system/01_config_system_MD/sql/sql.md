# SQL - Capteur de taille de la base MariaDB

> **Fichier :** `sql.yaml`
> **Emplacement prod :** `/config/sql.yaml`
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/sql.yaml`
> **Empreinte relevée le 2026-10-18 :** MD5 `5a33b0fb`, 2031 octets, copie locale identique à la prod
> **Inclus par :** `configuration.yaml` (`sql: !include sql.yaml`)
> **Dernière modification :** 2026-07-19 (date du fichier)

---

## Description

Utilise l'intégration `sql` native de Home Assistant pour interroger MariaDB. Un seul capteur : `Taille Db Home Assistant` (`unique_id: taille_db_home_assistant`).

## Contenu

- `db_url: !secret mariadb_url` : l'adresse de la base est dans `secrets.yaml`, aucun identifiant en clair dans ce fichier.
- Requête : `SELECT Round(Sum(data_length + index_length) / POWER(1024,2), 1) AS value FROM information_schema.tables WHERE table_schema = "homeassistant";`
- Colonne lue : `value`, unité `MiB`, `device_class: data_size` (HA affiche en MiB ou GiB).
- Aval : vignette L5C3 (taille de la base MariaDB) du dashboard, d'après l'en-tête du fichier.

## Points d'attention

- `!secret` fonctionne ici parce que `db_url` est une valeur YAML entière (en-tête du fichier). Ne pas passer par `command_line`.
- `sql.yaml` est audité par `audit_md5_yaml.sh` (fichiers de la racine).
- Ne jamais copier la valeur de `mariadb_url` dans une fiche, un journal ou un rapport.