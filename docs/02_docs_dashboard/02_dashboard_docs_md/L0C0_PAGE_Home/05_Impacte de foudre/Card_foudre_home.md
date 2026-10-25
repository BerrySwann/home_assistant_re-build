<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_yaml/L0C0_PAGE_Home/05_Impacte de Foudre/card_foudre_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `custom:button-card (visibility numeric_state)` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-11 |
| 🏠 **Version HA** | 2026.10.0 |

---

# ⚡ Carte : Foudre Blitzortung

---

## 📋 VUE D'ENSEMBLE

Carte d'alerte foudre (Blitzortung) de la page Home. Elle affiche la distance du dernier impact, la ville (géocodage) ou, à défaut, la direction (azimut), le temps écoulé et le nombre d'impacts. Elle n'apparaît que si `sensor.maison_lightning_counter` dépasse 1.

Carte HACS utilisée : `custom:button-card`.

---

## 🎯 FONCTIONNEMENT

| Distance du dernier impact | Bordure / fond | Animation |
|:---------------------------|:---------------|:----------|
| 0 à 5 km | rouge, fond `rgba(255,0,0,0.2)` | clignotement (`blink-danger`, 1 s) |
| plus de 5 km | orange, fond `rgba(255,123,0,0.1)` | aucune |
| aucun impact (distance 0) | vert, fond `rgba(0,255,0,0.05)` | aucune |

- Message : "Impact à X Km" + ville si le géocodage la fournit, sinon direction déduite de l'azimut (16 secteurs) ; "Aucun impact récent détecté" si la distance est 0.
- Tap : navigation vers `meteo/#foudre`.
- Mise à jour de la carte déclenchée aussi par `sensor.dernier_impact_temps_reel` et `sensor.maison_lightning_distance`.
- Taille : 12 colonnes, 2,5 lignes.

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle |
|:---------|:-----|
| `sensor.maison_lightning_counter` | Compteur d'impacts + condition de visibilité (> 1) |
| `sensor.maison_lightning_distance` | Distance du dernier impact (km) : couleurs et animation |
| `sensor.maison_lightning_localisation` | Géocodage : ville (`features[0].properties.geocoding.city`) |
| `sensor.maison_lightning_azimuth` | Azimut en degrés (utilisé si pas de ville) |
| `sensor.dernier_impact_temps_reel` | Temps écoulé depuis le dernier impact |

---

## 📁 FICHIERS LIÉS

- YAML : `card_foudre_home.yaml` (dossier `05_Impacte de Foudre` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 4 (et section Dépannage)
