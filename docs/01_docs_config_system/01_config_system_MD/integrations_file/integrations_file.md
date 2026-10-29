# Intégrations File (notify) - fichiers de log écrits par les automations

<div align="center">

[![MàJ](https://img.shields.io/badge/MàJ-2026--10--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)

</div>

> **Fichier :** aucun. Ces intégrations n'existent pas en YAML : la plateforme `notify.file` est interdite en YAML depuis 2026. Elles sont créées dans l'UI de HA et stockées dans la config interne (`/config/.storage/core.config_entries`, domaine `file`).
> **Où les voir :** Paramètres > Appareils et services > File
> **Relevé du 2026-10-23 :** 7 entrées, toutes chargées, lues dans HA (API) et dans `core.config_entries` (lecture seule, domaine `file` uniquement)
> **Utilisées par :** les automations qui appellent `notify.send_message` avec une entité `notify.*` de cette liste

---

## Description

Chaque entrée File écrit les messages qu'elle reçoit à la suite d'un fichier texte dans `/config/notifs/` (ou `/config/.logs/`). Une automation envoie la ligne avec `notify.send_message` sur l'entité de l'entrée. Les fichiers `/config/notifs/` sont vivants (lus par des capteurs `command_line`) : ils ne sont ni copiés, ni sauvegardés, ni poussés.

## Les 7 intégrations (relevé 2026-10-23)

| Fichier écrit | Entité notify | Écrit par (automation) | Horodatage |
|:--|:--|:--|:--|
| `/config/notifs/diag_conso_elec.txt` | `notify.file_diag_log_file` | DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT) | non |
| `/config/notifs/ecart_liky_vs_nodon.txt` | `notify.log_ecart_energie` | Log Écart Linky vs Nodon | non |
| `/config/.logs/zone_eric.txt` | `notify.zone_eric` | [P4] Eric - Log Zones | non |
| `/config/notifs/linky_histo.txt` | `notify.log_linky_histo` | A - [P0] Histo Linky quotidien + Ecart J-1 (corrigé par C et D via script) | non |
| `/config/notifs/ecart_histo.txt` | `notify.log_ecart_histo` | A - [P0] Histo Linky quotidien + Ecart J-1 (corrigé par C et D via script) | non |
| `/config/notifs/nodon_histo.txt` | `notify.log_nodon_histo` | B - [P0] Histo Nodon quotidien | non |
| `/config/notifs/nodon_complet_histo.txt` | `notify.nodon_complet_histo` | E - [P0] Histo Nodon complet quotidien (Total HP HC Cout) | non |

Identifiants des entrées (`entry_id`) : `01KP8X8BBAGWX8ZP1S7Z9M5MGG` (diag_conso_elec), `01KPXW28JQBWE7KSS84ZHF2NGB` (ecart_liky_vs_nodon), `01KVGEBAK9411S889HDG49QK1T` (zone_eric), `01M1A41V4S9QDRBM7ARJ4HJP3H` (linky_histo), `01M1CG4WC7JZWBATG1NGKHZBCG` (ecart_histo), `01M1A3W9N3DZNQ54S31QG48KDF` (nodon_histo), `01M5N0WW6XZPAMBB3RXSYDGBD0` (nodon_complet_histo).

L'association entité / fichier se déduit du nom donné à la création et de l'usage dans `automations.yaml` (aucun lien direct n'est exposé par HA). Les automations qui appellent chaque entité ont été retrouvées dans `H:\automations.yaml` le 2026-10-23.

## Recréer une intégration (après une restauration de backup, par exemple)

1. Paramètres > Appareils et services > Ajouter une intégration > File.
2. Choisir "Notify" (écriture dans un fichier), pas "Sensor".
3. Chemin du fichier : le chemin complet, par exemple `/config/notifs/nodon_complet_histo.txt`.
4. Nom : le nom de l'entité attendue sans `notify.` (exemple : `nodon_complet_histo`). Ne jamais mettre le chemin dans le champ Nom : l'entité serait introuvable.
5. Horodatage : désactivé (case décochée), sinon chaque ligne est précédée d'une date et casse les lectures `command_line`.
6. Vérifier que l'entité `notify.<nom>` existe (Outils de développement > États) avant de relancer l'automation.

## Points d'attention

- Le titre affiché par HA est `Notify [/config/notifs/...]`. Dans `core.config_entries`, `linky_histo` et `nodon_histo` ont un chemin relatif (`notifs/...`) : c'est équivalent, HA les place sous `/config`.
- Le chemin d'une intégration File ne se modifie pas après création : il faut la supprimer et la recréer.
- Une entité notify n'a pas de fichier propre : sa perte (backup restauré, entrée supprimée) n'est visible qu'à l'exécution de l'automation (erreur dans les traces de l'automation).
- `notify.log_ecart_histo` n'a pas reçu d'écriture depuis le 2026-10-17 (A n'écrit que si le Linky J-1 est publié).
- Ne jamais écrire dans `core.config_entries` : le fichier contient des secrets d'autres intégrations. Les contrôles le lisent en filtrant le domaine `file` uniquement.

## Contrôle automatique

- Script en lecture seule `Verif_integrations_file.py` (fiche : `docs/04_docs_scripts/04_docs_scripts_SH_MD/Verif_integrations_file/Verif_integrations_file.md`), lancé par /histo (point 10 de l'étape 6).
- Il compare le tableau ci-dessus aux entrées File de HA (`core.config_entries` et `core.entity_registry`, domaine et plateforme `file`) : chemin, entité notify, horodatage, entrée désactivée.
- Rapport : `historique/03_RAPPORTS/06_MD5/05_VERIF_INTEGRATIONS_FILE/verif_integrations_file_AAAA-MM-JJ.txt` (dernières lignes ANOMALIES et RESULTAT).
- Après un ajout, un retrait ou une modification d'intégration : mettre à jour le tableau de cette fiche, puis relancer le script.