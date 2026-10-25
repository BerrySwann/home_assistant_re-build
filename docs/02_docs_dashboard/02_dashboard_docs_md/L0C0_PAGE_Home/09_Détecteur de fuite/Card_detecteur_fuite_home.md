<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_yaml/L0C0_PAGE_Home/09_Détecteur de fuite/card_detecteur_fuite_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `custom:mushroom-entity-card (visibility or)` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-11 |
| 🏠 **Version HA** | 2026.10.0 |

---

# 💧 Carte : Détecteur de fuite

---

## 📋 VUE D'ENSEMBLE

Carte d'alerte fuite d'eau de la page Home : détecteur placé sous l'évier de la cuisine (IKEA Vallhorn Water Sensor via Zigbee2MQTT). La carte est masquée tant que tout va bien.

Carte HACS utilisée : `custom:mushroom-entity-card`, fond, ombre et bordure supprimés par `card_mod`.

---

## 🎯 FONCTIONNEMENT

- Visibilité (`or`) : `binary_sensor.detecteur_de_fuite_ikea_water_leak` = `on` (fuite), `unavailable` ou `unknown`. Un capteur injoignable fait donc aussi apparaître la carte.
- Nom affiché : "Détecteur de fuite sous évier cuisine", mise en page verticale.
- Aucune action tap / hold / double tap.
- Taille : 12 colonnes, 2 lignes (pleine largeur).

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle | Source |
|:---------|:-----|:-------|
| `binary_sensor.detecteur_de_fuite_ikea_water_leak` | État du détecteur : visibilité + affichage | IKEA Vallhorn via Z2M |

---

## 📁 FICHIERS LIÉS

- YAML : `card_detecteur_fuite_home.yaml` (dossier `09_Détecteur de fuite` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 8
