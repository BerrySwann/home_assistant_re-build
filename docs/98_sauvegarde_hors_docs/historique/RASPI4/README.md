# 📦 ARCHIVE — RASPI4 (télémétrie Raspberry Pi 4)

<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Archive-9e9e9e?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--10--30-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.4-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-README-ff9800?style=flat-square)](.)

</div>

*Archivé le 2026-09-20 — retiré de la prod Home Assistant le même jour (GO Berry).*

## Ce que c'est
**13 capteurs `template` + 1 automation fantôme**, restes de la télémétrie du **Raspberry Pi 4**
(cœurs 0-3 = machine 4 cœurs, `cpu_package`, carte mère) — attribution Berry : « c'est pour le raspi à tous les coups ».

## Chronologie
- **28/03/2026** : création des capteurs (cœurs + cpu_package) ;
- **02/05/2026** : ajout carte mère ;
- **24/05/2026** : création + modif de l'automation `p3_sdb_bouton_hue_toggle_relais_lumiere` (jamais déclenchée) ;
- **30/05/2026** : définitions retirées du YAML → entités orphelines (`unavailable`) ;
- **20/09/2026** : archivage + purge du registre HA (compteur indispo 201 → 187).

## Inventaire exact
| Entité | unique_id | Créée | Dernière modif |
|:-------|:----------|:------|:---------------|
| `sensor.temperature_carte_mere` | `temperature_carte_mere_sys` | 2026-05-02 | 2026-05-05 |
| `sensor.temperature_carte_mere_2` | `temperature_carte_mere` | 2026-03-28 | 2026-05-30 |
| `sensor.temperature_carte_mere_sys` | `temperature_carte_mere_sys` | 2026-02-23 | 2026-05-30 |
| `sensor.temperature_cpu_package_sys` | `temperature_cpu_package_sys` | 2026-02-23 | 2026-05-30 |
| `sensor.temperature_core_0_sys` | `temperature_core_0_sys` | 2026-02-23 | 2026-05-30 |
| `sensor.temperature_core_1_sys` | `temperature_core_1_sys` | 2026-02-23 | 2026-05-30 |
| `sensor.temperature_core_2_sys` | `temperature_core_2_sys` | 2026-02-23 | 2026-05-30 |
| `sensor.temperature_core_3_sys` | `temperature_core_3_sys` | 2026-02-23 | 2026-05-30 |
| `sensor.temperature_cpu_package` | `temperature_cpu_package` | 2026-03-28 | 2026-05-30 |
| `sensor.temperature_core_0` | `temperature_core_0` | 2026-03-28 | 2026-05-30 |
| `sensor.temperature_core_1` | `temperature_core_1` | 2026-03-28 | 2026-05-30 |
| `sensor.temperature_core_2` | `temperature_core_2` | 2026-03-28 | 2026-05-30 |
| `sensor.temperature_core_3` | `temperature_core_3` | 2026-03-28 | 2026-05-30 |
| `automation.p3_sdb_bouton_hue_toggle_relais_lumiere` | `1779618286845` | 2026-05-24 | 2026-05-24 |

## Contenu du dossier
- `registre_ha_2026-09-20.json` — entrées de registre HA complètes (avant purge) ;
- `historique_recorder/` — état final côté recorder (13 fichiers ; les vraies mesures ne sont plus conservées par la purge — il ne reste que les états `unavailable`) ;
- `references/` — documents de la config qui les citaient (vignette L4C1).

## Références retrouvées
- `vignette_L4C1_proxmox_2026-05-19.yaml` (L4C1) : affichait `sensor.temperature_cpu_package` ;
- `ENTITES_INDEX.md` (~l.1419 / l.1451 — vignettes L4C1/L4C2).

## Pour plus tard (si le RPi4 repart)
Recréer des capteurs **neufs** pointés sur la vraie source (MQTT/SSH/agent) — les anciens templates
ne sont pas réutilisables tels quels (définitions perdues le 30/05).
