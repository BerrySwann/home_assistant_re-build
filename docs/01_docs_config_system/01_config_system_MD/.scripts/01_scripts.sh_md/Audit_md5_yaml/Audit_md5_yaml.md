# AUDIT_MD5_YAML - Audit MD5 des YAML de la config, prod contre GitHub

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--29-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-System-ffeb3b?style=flat-square)](.)

</div>

> **Script :** `audit_md5_yaml.sh` (bash)
> **Emplacement prod :** `/config/.scripts/audit_md5_yaml.sh`
> **Emplacement local :** `docs/01_docs_config_system/01_config_system_SH_PY_YAML/`.scripts/01_scripts.sh/audit_md5_yaml_sh/audit_md5_yaml.sh` (copie identique dans `docs/04_docs_scripts/04_docs_scripts_SH/Audit_md5_yaml/Audit_md5_yaml.sh`)
> **Empreinte relevée le 2026-10-29 :** MD5 `0534BD4E`, 8070 octets, identique dans les 2 copies locales et en prod (l'ancienne version de la prod était `4b9b7f24`, 7672 octets ; date du push de la version corrigée non retrouvée)
> **Appelé par :** bouton de la carte L5C3 -> `script.audit_md5` -> `shell_command.audit_md5` (fichier `shell_command/GitHub/GitHub_backup_GitHub.yaml`, commande `bash /config/.scripts/audit_md5_yaml.sh >> /config/.logs/md5_audit_yaml_AAAA-MM-JJ.txt 2>&1`)
> **Dernière entrée du journal du script :** 2026-10-18

---

## Description

Compare, côté HA, les YAML de la configuration (pas ceux de `docs/`) avec ceux du dépôt GitHub `BerrySwann/home_assistant_re-build` (branche `main`), plus les scripts `.sh` de `.scripts/`. Son pendant pour `docs/` est `audit_md5_md_yaml.sh`.

## Périmètre lu dans le script

- Dossiers (tous les `*.yaml`) : `sensors`, `templates`, `utility_meter`, `command_line`, `shell_command`, `packages`, `groups`, `input_booleans`, `input_number`, `timers` (`timers` ajouté le 2026-10-18 dans la version locale).
- Fichiers de la racine : `automations.yaml`, `scripts.yaml`, `configuration.yaml`, `sql.yaml`, `input_select.yaml`, `input_datetime.yaml`, `input_button.yaml`.
- Scripts : les `*.sh` de `.scripts/` et, depuis la version locale du 2026-10-18, ceux de `scripts/` (`mf_vigilance_images.sh`).
- Exclus : `streamline_templates.example.yaml` et `scenes.yaml`.

## Fonctionnement

- Passe 1 : liste les fichiers du périmètre.
- Passe 2 : MD5 de chaque fichier en prod.
- Passe 3 : téléchargement de chaque fichier sur `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/<chemin>` (délai de 15 s) et MD5 du fichier téléchargé.
- Statuts : SYNC, DIFF, PUSH MANQUANT (réponse HTTP différente de 200 ou fichier vide).
- Dernière ligne du rapport : `RESULTAT : N fichiers` suivi des comptes SYNC, DIFF et PUSH MANQUANT. Le script note (2026-10-10) que les lignes `RESULTAT` et `Audit MD5 terminé` sont lues par la carte L5C3 et ne doivent pas changer de forme.

## Sorties

- Rapport : `/config/.logs/md5_audit_yaml_AAAA-MM-JJ.txt` (les anciens rapports de ce nom sont supprimés à chaque lancement). Copie du dernier rapport : `/config/.logs/md5_audit_latest.txt`.

## Points d'attention (lus dans le script, relevé du 2026-10-18)

- Corrigé le 2026-10-18 : `timers` est dans les dossiers audités, `scripts/*.sh` est ajouté à la liste (relevé le 2026-10-29 : le script contient bien `timers` et `mf_vigilance_images`, et la prod a le même MD5 que le local).
- `notifs` n'est pas ajouté : il ne contient que des `.txt` (journaux écrits en continu) et le script ne lit que les `*.yaml`. Les `.py` de `.scripts/` ne sont pas audités non plus.
- `themes` n'est pas audité : décision d'Eric le 2026-10-18 (le dossier n'existe plus en local).
- `packages` est dans la liste, mais ce dossier n'existe pas à la racine de la prod. Sans effet (`|| true`).
- Les 4 marques BOM (octets `EF BB BF`) du début du fichier sont supprimées depuis le 2026-10-18 (relevé le 2026-10-29 : pas de BOM, MD5 local = prod).
- Le script contient des caractères hors ASCII dans ses messages d'affichage (cadres, flèches, pictogrammes) : non modifié, pas demandé.
- GitHub distingue la casse : un fichier renommé en prod avec une autre casse sort PUSH MANQUANT jusqu'à la sauvegarde GitHub suivante.

## Dépendances

- `curl` et `md5sum`, accès réseau à `raw.githubusercontent.com`, dossier `/config/.logs`.
- Carte L5C3 du dashboard (lit les lignes de résultat).

## Historique (journal du script)

- 2026-06-14 : création, 3 passes.
- 2026-06-15 : passage de `git show` à `curl` sur l'adresse raw. Comparaison sur les octets exacts (fichier téléchargé, pas de `$()`).
- 2026-06-17 : ajout de `shell_command/` et `packages/`.
- 2026-06-28 : correction de `pipefail`. Ajout des `.sh` de `.scripts/`.
- 2026-10-10 : colonnes du tableau PROD, GITHUB, STATUT, FICHIER.
- 2026-10-18 : périmètre étendu à `timers` et `scripts/*.sh` (`themes` écarté sur décision d'Eric), suppression des 4 BOM (version locale, `bash -n` valide, sauvegarde `.bak_2026_10_18_16h35m52s` à côté du script).
- 2026-10-29 : fiche corrigée (empreinte, version en prod, chemin local par dossier, cascade du bouton L5C3). Aucune modification du script.
