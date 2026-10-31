# VERIF_INTEGRATIONS_FILE - Controle des integrations File (notify) de Home Assistant

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Script-4fc3f7?style=flat-square)](.)

</div>

> **Script :** `Verif_integrations_file.py` (Python, lance avec `python -I`)
> **Emplacement local :** `docs/04_docs_scripts/04_docs_scripts_SH/Verif_integrations_file/Verif_integrations_file.py`
> **Copie prod (miroir docs) :** `H:\docs\04_docs_scripts\04_docs_scripts_SH\Verif_integrations_file`
> **Execute depuis :** le PC (local ReBuild), appele par `/histo` et `/histo-final`
> **Cree :** 2026-10-23 (demande d'Eric) ; **derniere modification :** 2026-10-23
> **Fiche de reference controlee :** `docs/01_docs_config_system/01_config_system_MD/integrations_file/integrations_file.md`

---

## Description

Les integrations File (notify) ne peuvent pas etre ecrites en YAML : elles vivent dans `/config/.storage` et ne sont ni sauvegardees dans les docs ni visibles dans GitHub. Ce script compare, en lecture seule, ce que HA contient reellement avec le tableau de la fiche `integrations_file.md`.

Sources lues (H:\.storage\) :

- `core.config_entries` : uniquement les entrees du domaine `file` (chemin du fichier, option horodatage, entree desactivee) ;
- `core.entity_registry` : uniquement les entites de la plateforme `file` (lien entree -> entite notify).

Ces deux fichiers contiennent des secrets d'autres integrations : seuls les champs utiles des entrees `file` sont lus et ecrits dans le rapport. Aucune ecriture dans `.storage`, jamais.

## Verdicts

- Section 1, une ligne par ligne du tableau de la fiche : OK, MANQUANT DANS HA, ENTITE DIFFERENTE, HORODATAGE ACTIF, ENTREE DESACTIVEE.
- Section 2, entrees de HA absentes de la fiche : EN TROP (ABSENTE DE LA FICHE).
- Les chemins relatifs de HA (`notifs/x.txt`) sont ramenes a `/config/notifs/x.txt` avant comparaison.

## Sorties

- `historique/03_RAPPORTS/06_MD5/05_VERIF_INTEGRATIONS_FILE/verif_integrations_file_AAAA-MM-JJ.txt` (le rapport du jour deja present est d'abord renomme en `.bak_AAAA_MM_JJ_HHhMMmSSs.txt`). Dernieres lignes : `ANOMALIES` et `RESULTAT` (OK ou ECART).
- Codes retour : 0 rapport ecrit ; 2 prod H: inaccessible (rien n'est ecrit) ; 3 fiche illisible (rien n'est ecrit).

## Points d'attention

- Si le rapport donne ECART apres que Eric a ajoute, retire ou modifie une integration File : mettre a jour le tableau de `integrations_file.md` (et la liste de `IA_AUTOMATIONS_NOTIFS.md`), puis relancer.
- Le script lit le tableau de la fiche : les lignes doivent rester au format `| `/chemin` | `notify.x` | automation | horodatage |`.

## Dependances

- Fiche `integrations_file.md` ; skills `histo` et `histo-final` (etape de controle) ; `H:` monte.

## Historique des modifications

- 2026-10-23 : creation (7 integrations File, test OK sur la prod).
- 2026-10-23 : rapport redirige vers historique/03_RAPPORTS/06_MD5/05_VERIF_INTEGRATIONS_FILE/ (dossier MD5 deplace par Eric le 2026-10-21).