<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--15-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.1-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Carte-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `02_dashboard_docs_YAML/L0C0_PAGE_Home/11_Carte Présence/card_presence_home.yaml` |
| 🔗 **Accès depuis** | Vue principale Home (`L0C0_PAGE_Home`) |
| 🏗️ **Layout** | `vertical-stack : bubble-card separator + horizontal-stack de 2 bubble-card button` |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-15 |
| 🏠 **Version HA** | 2026.10.1 |

---

# 👤 Carte : Présence (séparateur + Eric + Mamour)

---

## 📋 VUE D'ENSEMBLE

Groupe de présence de la page Home, en une seule carte (`vertical-stack`) : un séparateur "Personne(s)", puis une ligne (`horizontal-stack`) avec le bouton d'Eric et celui de Mamour. Version fournie par Eric le 2026-10-11. Elle remplace la version en liste de 3 cartes (conservée en `card_presence_home.bak_2026_10_11.yaml`) et les trois fichiers séparés (`.bak_2026_10_11`).

Carte HACS utilisée : `custom:bubble-card` (`separator` puis deux `button` de type `state`).

La détection de présence WiFi se fait par le routeur Beryl : les capteurs de la config cherchent le SSID `Module B.E.R.Y.L. [GG-5.0]` ou `[GG-2.4]`.

Collage : carte unique, elle se colle dans l'éditeur de carte de Home Assistant. La version en liste de 3 cartes y était refusée ("Aucun type fourni").

---

## 🎯 CARTE 1 - SÉPARATEUR "PERSONNE(S)"

Couleur du sub-button selon `sensor.etat_wifi_maison` :

| État | Couleur | Signification |
|:------|:--------|:--------------|
| `2` | `darkgreen` | Eric + Mamour présents |
| `Eric` ou `Mamour` | `darkorange` | une seule personne |
| autre | `grey` | personne |

- Sub-button : entité `sensor.etat_wifi_maison`, icône `mdi:home`, nom "Maison", contenu affiché = l'état (`state_content: state`).
- Hauteur `rows: 0.8` ; marge haute 20 px ; ligne en couleur du texte principal, opacité 0,8.

---

## 🎯 CARTE 2 - ERIC (ligne du bas, à gauche)

- Entité : `device_tracker.poco` ; sub-button : `person.eric` (icône et fond affichés). Contenu affiché : dernière modification (`state_content: last_changed`).
- Fond du sub-button et de l'icône principale : noir pour le sub-button.

| État du tracker | Couleur (fond de la carte et icône) |
|:-----------------|:--------------------------------------|
| `home` | `darkgreen` |
| tout autre état | `grey` |

- Il n'y a plus de pictogramme `mdi:home` à l'état `home` : la ligne `subButtonIcon` a disparu du YAML.

---

## 🎯 CARTE 3 - MAMOUR (ligne du bas, à droite)

- Entité : `device_tracker.mamour`, nom "Mamour" ; sub-button : `person.mamour`. Contenu affiché : dernière modification (`state_content: last_changed`).

| État du tracker | Couleur (fond et icône) |
|:-----------------|:--------------------------|
| `home` | `darkgreen` |
| `not_home` | `rgb(255, 103, 0)` |
| `LECLERC`, `MONOPRIX`, `AUCHAN`, `ANITA`, `KIPUE` | `rgb(0, 102, 204)` |
| tout autre | `grey` |

- Les cinq zones sont maintenant dans une seule liste ; les couleurs sont les mémes qu'avant. Les pictogrammes par état (`mdi:home`, `mdi:home-off`, `mdi:basket-check`, `mdi:map-marker`, `mdi:crosshairs-question`) ont disparu avec la ligne `subButtonIcon`.
- Les noms de zones sont ceux déclarés dans Home Assistant (correction du 2026-10-10 : l'ancienne version testait "LECLERC VENCE" et "Primark", qui ne se déclenchaient jamais).

---

## 📊 ENTITÉS UTILISÉES

| Entité | Rôle |
|:---------|:-----|
| `sensor.etat_wifi_maison` | Agrégat WiFi (`2` / `Eric` / `Mamour` / `0`) : couleur et valeur du séparateur. Source : `templates/P4_groupe_presence/P4_groupe_presence.yaml` |
| `device_tracker.poco` | Présence du téléphone d'Eric |
| `device_tracker.mamour` | Présence du téléphone de Mamour |
| `person.eric`, `person.mamour` | Sub-buttons des cartes Eric et Mamour |

---

## 🐛 DÉTECTION WIFI (SOURCE DU SÉPARATEUR)

Capteurs de `templates/P4_groupe_presence/P4_groupe_presence.yaml` (et `P4_wifi_detection.yaml`). Le WiFi de référence est celui du routeur Beryl : SSID `Module B.E.R.Y.L. [GG-5.0]` ou `[GG-2.4]`.

| Entité | Rôle |
|:---------|:-----|
| `sensor.condition_eric_wifi` | `true` si le tracker d'Eric est en mode `wifi` ET connecté à l'un des deux SSID, sinon `false` |
| `sensor.condition_mamour_wifi` | idem pour Mamour |
| `sensor.etat_wifi_maison` | Agrégat : `2` (les deux), `Mamour`, `Eric` ou `0` |

L'attribut `couleur` de `sensor.etat_wifi_maison` (`2` green, `Mamour` orange, `Eric` gold, `0` red) n'est pas utilisé par le dashboard. Entités natives : `device_tracker.poco` et `device_tracker.mamour` (intégration `mobile_app`, App Companion), `person.eric` et `person.mamour` (Paramètres > Personnes).

### Dépannage

- Séparateur gris alors qu'un téléphone est à la maison : vérifier `sensor.condition_eric_wifi` / `sensor.condition_mamour_wifi` (Outils de développement > États), que le téléphone est bien sur le WiFi du Beryl (et non en 4G/5G), que l'App Companion est active et que le `device_tracker` est `home`.
- Photo de profil absente : vérifier qu'une photo est définie pour `person.eric` / `person.mamour` (Paramètres > Personnes) ; l'attribut `entity_picture` doit étre renseigné sur l'entité `person`.

Dépendances : `mobile_app`, `person`, `bubble-card` (HACS), le template P4 ci-dessus.

---
## 🐛 Points à vérifier

- La ligne `attribute: entity_picture` des sub-buttons a disparu par rapport aux anciens fichiers : si la photo de profil ne s'affiche plus, c'est la première piste. Non vérifié depuis cette session.
- Les `layout_options` (`grid_columns`, `grid_rows`) restent dans les deux boutons, mais à ma connaissance ils ne servent que pour les vues "sections" et n'ont pas d'effet dans un `horizontal-stack`. Non vérifié sur ton dashboard.

---

## 📁 FICHIERS LIÉS

- YAML : `card_presence_home.yaml` (dossier `11_Carte Présence` côté YAML)
- Page : [PAGE_HOME.md](../02_page/PAGE_HOME.md), carte 10
