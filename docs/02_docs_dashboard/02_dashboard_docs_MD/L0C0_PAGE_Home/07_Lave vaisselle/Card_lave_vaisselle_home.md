<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_YAML/L0C0_PAGE_Home/07_Lave Vaisselle/card_lave_vaisselle_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `custom:mushroom-entity-card + card_mod` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-11 |
| 🏠 **Version HA** | 2026.10.0 |

---

# 🍽 Carte : Lave-vaisselle (WashData)

---

## 📋 VUE D'ENSEMBLE

Carte conditionnelle du lave-vaisselle sur la page Home (refonte WashData du 2026-09-19). Elle affiche l'état du cycle, une barre de progression, le temps restant et la puissance. Elle n'apparaît que si la prise du lave-vaisselle dépasse 2 W (machine en marche).

Carte HACS utilisée : `custom:mushroom-entity-card`, mise en forme par `card_mod` (template Jinja dans le style). Intégration WashData (HACS) pour l'état, la progression et le temps restant.

---

## 🎯 FONCTIONNEMENT

- Visibilité : `numeric_state` sur `sensor.prise_lave_vaisselle_nous_power`, au-dessus de 2.
- Carte : entité = `sensor.prise_lave_vaisselle_nous_power`, nom "Lave Vaisselle", icône `mdi:dishwasher`, tap = `more-info`.
- Taille : 12 colonnes, 2 lignes (pleine largeur).
- Le bloc `visibility` se trouve à la fin du fichier YAML (ligne 273 environ).

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle | Source |
|:---------|:-----|:-------|
| `sensor.lave_vaisselle_etat` | État du cycle (badge principal) | WashData (HACS) |
| `sensor.lave_vaisselle_temps_restant` | Temps restant | WashData (HACS) |
| `sensor.lave_vaisselle_progres` | Progression du cycle | WashData (HACS) |
| `sensor.prise_lave_vaisselle_nous_power` | Puissance instantanée (W) : condition d'affichage + badge | NOUS SP via Z2M (P2) |

---

## 📁 FICHIERS LIÉS

- YAML : `card_lave_vaisselle_home.yaml` (dossier `07_Lave Vaisselle` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 6
- Carte jumelle : lave-linge (`06_Lave Linge`)
