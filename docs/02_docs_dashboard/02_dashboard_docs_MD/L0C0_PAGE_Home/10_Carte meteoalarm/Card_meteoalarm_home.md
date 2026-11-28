<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--11--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.11.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_YAML/L0C0_PAGE_Home/10_Carte Meteoalarm/card_meteoalarm_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `custom:meteoalarm-card (integration: meteofrance, hide_when_no_warning, visibility sur sensor.alerte_avalanches)` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-11-28 |
| 🏠 **Version HA** | 2026.11.3 |

---

# ⚠️ Carte : Alertes Meteoalarm

---

## 📋 VUE D'ENSEMBLE

Carte des alertes de vigilance Météo-France de la page Home, placée entre le détecteur de fuite (carte 8) et la présence (carte 10). Elle est alimentée par `sensor.06_weather_alert` (intégration native Météo-France).

Carte HACS utilisée : `custom:meteoalarm-card` (Meteoalarm Card, version 2.9.0 installée le 2026-10-15).

---

## 🎯 FONCTIONNEMENT

- `integration: meteofrance` est obligatoire : une carte ajoutée sans cette option affiche "Cette intégration n'est pas valide !" dans l'éditeur.
- `hide_when_no_warning: true` : la carte n'affiche rien tant qu'aucune alerte n'est active (comportement déduit du nom de l'option, non vérifié à l'écran). Une carte invisible n'est donc pas un défaut quand les alertes sont vertes.
- `visibility` (2026-11-28, valeur changee par Eric le meme jour) : la carte est cachee tant que `sensor.alerte_avalanches` vaut `Jaune` (`state_not: [Jaune]`). Le capteur est actif dans `M_01_meteo_alertes_card.yaml` (inhibe puis reactive le 2026-11-28, car la tuile Avalanches du pop-up disparaissait). Effet : tant que l avalanche est Jaune, la carte est cachee pour tous les types d alerte, y compris une Orange ou Rouge d un autre type ; elle reapparait pour tout autre etat. Choix d Eric (avalanche sans objet chez lui, Orange et Rouge rares selon lui, non verifie). Condition sur la carte Home uniquement, pas sur la copie du pop-up `#alert`.
- `scaling_mode: disabled` : option ajoutée par l'éditeur de la carte, rôle non vérifié.
- La même carte (même configuration) se trouve aussi dans le pop-up `#alert` de la page Météo (L1C1), en dernier élément, sous les cartes caméra et les pastilles des capteurs `sensor.alerte_*`.
- À ne pas confondre avec la bannière "Vigilance Jaune / Orange / Rouge" de la carte météo animée (carte 1), qui lit `sensor.alerte_meteo`.

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle | Source |
|:---------|:-----|:-------|
| `sensor.06_weather_alert` | Alertes de vigilance Alpes-Maritimes | Intégration Météo-France (native) |
| `sensor.alerte_avalanches` | Condition de visibilite (carte cachee si Jaune) | Template M_01, actif (reactive le 2026-11-28) |

---

## 🐛 Points à vérifier

- Rendu non vérifié visuellement avec une alerte active (Jaune, Orange ou Rouge).
- Rendu non verifie visuellement avec `sensor.alerte_avalanches` a Jaune (carte attendue cachee sur Home).
- Historique : les exports `Dashboard_COMPLET` du 2026-03-16 au 2026-10-14 ne contiennent cette carte que dans la vue Météo, jamais dans la vue Home. Elle a été ajoutée à Home le 2026-10-15 (collée depuis l'éditeur par Eric).

---

## 📁 FICHIERS LIÉS

- YAML : `card_meteoalarm_home.yaml` (dossier `10_Carte Meteoalarm` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 9
- Capteurs du pop-up Météo : `templates/meteo/M_01_meteo_alerte/M_01_meteo_alertes_card.yaml` (`sensor.alerte_*`)
<!-- annotations_log: [2026-11-28] Card_meteoalarm_home : fiche carte : date et version HA, visibility, entite sensor.alerte_avalanches, points a verifier ; bak _2026_11_28_11h42m03s ; pousse H:\docs -->
<!-- annotations_log: [2026-11-28] Card_meteoalarm_home : fiche : visibility Jaune, capteur reactive, effet sur les autres alertes, rendu a verifier ; bak _2026_11_28_13h42m23s ; pousse H:\docs -->
