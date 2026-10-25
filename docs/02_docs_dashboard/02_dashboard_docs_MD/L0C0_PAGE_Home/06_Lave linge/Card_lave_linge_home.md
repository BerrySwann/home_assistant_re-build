<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_YAML/L0C0_PAGE_Home/06_Lave Linge/card_lave_linge_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `custom:mushroom-entity-card + card_mod` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-11 |
| 🏠 **Version HA** | 2026.10.0 |

---

# 🧺 Carte : Lave-linge (WashData)

---

## 📋 VUE D'ENSEMBLE

Carte conditionnelle du lave-linge sur la page Home (refonte WashData du 2026-09-19). Elle affiche l'état du cycle, une barre de progression, le temps restant et la puissance. Elle n'apparaît que si la prise du lave-linge dépasse 2 W (machine en marche).

Carte HACS utilisée : `custom:mushroom-entity-card`, mise en forme par `card_mod` (template Jinja dans le style). Intégration WashData (HACS) pour l'état, la progression et le temps restant.

---

## 🎯 FONCTIONNEMENT

- Visibilité : `numeric_state` sur `sensor.prise_lave_linge_nous_power`, au-dessus de 2.
- Carte : entité = `sensor.prise_lave_linge_nous_power`, nom "Lave Linge", icône `mdi:washing-machine`, tap = `more-info`.
- Taille : 12 colonnes, 2 lignes (pleine largeur).
- Le template `card_mod` lit le temps restant sous deux formes : horodatage de fin, ou durée contenant ":" ; la variable `max_time` du template vaut 120.
- Les tailles (icône 65 px, polices 15 / 12 / 12 px) sont réglées en téte du template (bloc "USER CONFIGURATION").

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle | Source |
|:---------|:-----|:-------|
| `sensor.lave_linge_etat` | État du cycle (badge principal) | WashData (HACS) |
| `sensor.lave_linge_temps_restant` | Temps restant | WashData (HACS) |
| `sensor.lave_linge_progres` | Progression du cycle | WashData (HACS) |
| `sensor.prise_lave_linge_nous_power` | Puissance instantanée (W) : condition d'affichage + badge | NOUS SP via Z2M (P2) |

---

## 📁 FICHIERS LIÉS

- YAML : `card_lave_linge_home.yaml` (dossier `06_Lave Linge` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 5
- Carte jumelle : lave-vaisselle (`07_Lave Vaisselle`)
