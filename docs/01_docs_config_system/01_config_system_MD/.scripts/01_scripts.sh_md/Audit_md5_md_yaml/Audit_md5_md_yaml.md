# AUDIT_MD5_MD_YAML - Audit MD5 des docs, prod contre GitHub

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--29-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Script :** `audit_md5_md_yaml.sh` (bash)
> **Emplacement prod :** `/config/.scripts/audit_md5_md_yaml.sh`
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/`.scripts/01_scripts.sh/audit_md5_md_yaml_sh/audit_md5_md_yaml.sh`
> **Empreinte relevée le 2026-10-18 :** MD5 `d50741b7`, 6686 octets, copie locale identique à la prod
> **Appelé par :** bouton de la carte L5C3 -> `script.audit_md5_md_yaml` -> `shell_command.audit_md5_md_yaml` (fichier `shell_command/GitHub/GitHub_backup_GitHub.yaml`, commande `bash /config/.scripts/audit_md5_md_yaml.sh 2>&1`)
> **Dernière entrée du journal du script :** 2026-10-18

---

## Description

Compare, côté HA, les fichiers `.md`, `.yaml` et `.sh` de `/config/docs/` avec ceux du dépôt GitHub `BerrySwann/home_assistant_re-build` (branche `main`). Deux niveaux seulement : la prod et GitHub. Le local n'intervient pas (c'est le rôle du trigul sur le PC).

## Fonctionnement

- Passe 1 : liste les fichiers de `/config/docs` (`*.md`, `*.yaml`, `*.sh`), sans le dossier `modifs/`.
- Passe 2 : calcule le MD5 de chaque fichier en prod.
- Passe 3 : télécharge chaque fichier sur `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/docs/<chemin>` (chemin encodé par `python3 urllib.parse.quote`, délai de 15 s) et calcule son MD5.
- Statuts : SYNC (MD5 identiques), DIFF (MD5 différents), ABSENT GITHUB (réponse HTTP différente de 200).
- Dernière ligne du rapport : `RESULTAT : N fichiers (a .md - b .yaml - c .sh)` suivi des comptes SYNC, DIFF et ABSENT GITHUB. Le script note (2026-10-10) que les lignes `RESULTAT` et `Audit MD5 docs terminé` ne doivent pas changer de forme.

## Sorties

- Rapport : `/config/.logs/md5_audit_md_yaml_AAAA-MM-JJ.txt`. À chaque lancement, les anciens rapports de ce nom sont supprimés.
- Copie du dernier rapport : `/config/.logs/md5_audit_md_yaml_latest.txt` (la copie dans `/config/www/logs/` a ete supprimee le 2026-10-29, demande d'Eric).
- Le script s'arrête à la première erreur non gérée (`set -euo pipefail`).

## Points d'attention

- Ne couvre ni les `.py` ni les `.svg` de `docs/` (le trigul local les compte depuis le 2026-10-18).
- GitHub distingue la casse (déduit : l'adresse raw est un chemin de fichier). Un fichier renommé en prod avec une autre casse sort donc ABSENT GITHUB tant que la sauvegarde GitHub n'est pas passée.
- Aucune automation de `automations.yaml` ne l'appelle (relevé du 2026-10-18). Il est lancé par le bouton de la carte L5C3 via `script.audit_md5_md_yaml` (cascade relevée le 2026-10-29).

## Dépendances

- `python3`, `curl` et `md5sum` dans l'environnement du shell_command.
- Accès réseau à `raw.githubusercontent.com`.
- Dossier `/config/.logs`.

## Historique (journal du script)

- 2026-08-08 : création, miroir de `audit_md5.sh` pour les `.md` de `/config/docs/`. Réécriture en LF (le fichier initial était en CRLF).
- 2026-08-09 : périmètre étendu à tout `docs/` (`.md`, `.yaml`, `.sh`).
- 2026-10-10 : colonnes du tableau PROD, GITHUB, STATUT, FICHIER.
- 2026-10-18 : exclusion du dossier `modifs/` (journaux des agents, écrits en prod avant la sauvegarde GitHub). Demande d'Eric.
- 2026-10-29 : fiche mise à jour (chemin local par dossier, cascade du bouton L5C3, copie `/config/www/logs/` supprimée). Aucune modification du script.