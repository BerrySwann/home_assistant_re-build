<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--11-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-4fc3f7?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_YAML/L0C0_PAGE_Home/08_Congélateur/card_congelateur_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `custom:button-card (appliance)` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-11 |
| 🏠 **Version HA** | 2026.10.0 |

---

# ❄ Carte : Congélateur (alerte)

---

## 📋 VUE D'ENSEMBLE

Carte d'alerte du congélateur sur la page Home : elle n'est affichée que s'il y a un problème (température trop haute ou porte ouverte), pas en marche normale. Elle montre l'état de fonctionnement déduit de la puissance (Cooling / Super Cool / Defrost), la température, un badge de puissance et l'état de la porte, avec des animations (neige, givre, dégivrage).

Carte HACS utilisée : `custom:button-card` (carte "appliance").

---

## 🎯 FONCTIONNEMENT

- Visibilité (`or`) : `sensor.tongel_temperature` au-dessus de -15 °C, OU `binary_sensor.porte_congel_contact` = `on`.
- Seuils de puissance (variables du YAML) : Cooling à partir de 26 W, Super Cool à partir de 48 W, Defrost à partir de 235 W ; `max_power_w` = 60.
- `max_temp_freezer` = -14 ; `show_bar` = off ; deuxième porte et sonde frigo non utilisées (variables vides).
- Label : "Porte fermée" / "Porte Ouverte" (rouge à l'ouverture).
- Tap : `more-info`.
- Tailles (variables) : icône 45 px, forme 65 px, hauteur 95 px.

Point à vérifier : DEPENDANCES_GLOBALES_CLAUDE_memoire.md (entrée du 2026-09-20 S4) parle d'un seuil de visibilité passé à -14 °C ; le YAML local contient -15 pour la visibilité et -14 pour la variable `max_temp_freezer`. Comparer avec le live avant de corriger l'un ou l'autre.

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle | Source |
|:---------|:-----|:-------|
| `sensor.prise_congelateur_cuisine_nous_power` | Puissance instantanée (W) : états + badge | NOUS SP via Z2M (P2 cuisine) |
| `switch.prise_congelateur_cuisine_nous` | État de la prise (marche/arrét) | NOUS SP via Z2M (P2 cuisine) |
| `sensor.tongel_temperature` | Température congélateur (°C) : condition d'affichage + badge | SONOFF Tongel via Z2M |
| `binary_sensor.porte_congel_contact` | État de la porte : visibilité + icône + label | Porte Congél. via Z2M |

---

## 📁 FICHIERS LIÉS

- YAML : `card_congelateur_home.yaml` (dossier `08_Congélateur` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 7
