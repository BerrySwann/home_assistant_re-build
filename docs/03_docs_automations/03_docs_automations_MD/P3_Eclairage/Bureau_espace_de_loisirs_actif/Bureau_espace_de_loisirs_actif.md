# Bureau - Espace de loisirs actif, garder les indicateurs allumés

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Automation-ff9800?style=flat-square)](.)

</div>

**Catégorie :** P3_eclairage
**Alias HA :** `P3 BUREAU - Espace de loisirs actif, garder les indicateurs allumes`
**Entité :** `automation.nouvelle_automatisation` (id `1793131130516`), mode `restart`. Le nom de l'entité est le nom par défaut de l'interface : changer l'alias ne la renomme pas.
**Zone :** Bureau. **Étiquettes :** Eclairage(s), Watchdog.

## Description

Hue Sync démarre seul au démarrage du PC. Tant que l'espace de loisirs tourne (les 3 Hue Play du bureau sont en `mode: streaming`), les lampes éclairent mais HA les voit `off`. Cette automation rallume les 3 Hue Play pour que HA les voie allumées.

Elle remplace `P3_BUREAU - Forcer Play ON si PC tourne` (id `1775331547996`), retirée le 2026-10-27 (fusion en une seule automation, voir l'historique).

## Déclencheurs

- Une des 3 Hue Play (`light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau`) passe à `off`
- L'attribut `mode` d'une des 3 Hue Play passe à `streaming`
- `binary_sensor.moniteur_pc` passe à `on`
- Démarrage de Home Assistant (`homeassistant` / `start`)

## Condition

- Au moins une des 3 Hue Play a l'attribut `mode` égal à `streaming` (template)

## Actions

Un seul `light.turn_on` sur les 3 Hue Play (sans `brightness_pct` : la luminosité n'est plus forcée à 25 %).

## Entités principales

- `light.hue_play_1_pc_bureau`, `light.hue_play_2_pc_bureau`, `light.hue_play_3_pc_bureau`
- `binary_sensor.moniteur_pc`

## Limites connues

- La prise écran `switch.ecran_p_c_3_play_hue` n'est pas gérée ici : elle reste dans `P3_BUREAU_ACTIVATION_ECRAN_SYNCHRO`.
- Relevé d'Hermes du 2026-10-27 : l'horloge de HA retardait d'une heure sur celle du PC (à contrôler), ce qui peut fausser l'affichage de `last_triggered`. La trace d'exécution reste la source fiable.

## Historique

- 2026-10-27 : Eric crée l'automation. Hermes constate qu'elle entre en conflit avec le garde-fou `1775331547996`, puis fusionne les deux en une seule (mêmes `id`, 4 déclencheurs, une condition, une action). Le garde-fou est retiré de `automations.yaml` (64 blocs -> 63) et son entité fantôme supprimée du registre par Eric. Preuve après redémarrage complet de HA : déclenchement sur `Home Assistant starting`, `light.turn_on` exécuté sur les 3 Play (source : bilan d'Hermes h20261027-02).
- 2026-10-28 : export YAML local créé à partir de `automations.yaml` de la prod (bloc lignes 2902 à 2934), contenu identique.

## Fichier source

`docs/03_docs_automations/03_docs_automations_YAML/P3_Eclairage/P3_Bureau_espace_de_loisirs_actif/P3_Bureau_espace_de_loisirs_actif.yaml`

---
*Doc créée le 2026-10-28*
