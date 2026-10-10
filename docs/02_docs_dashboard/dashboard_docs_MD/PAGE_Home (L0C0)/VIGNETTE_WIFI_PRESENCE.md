<div align="center">

[![Statut](https://img.shields.io/badge/Statut-En%20cours-ff9800?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.10.0-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--10--10-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `.../Carte Présence/card_presence_separateur.yaml` (séparateur), `.../card_presence_eric.yaml` (Eric), `.../card_presence_mamour.yaml` (Mamour) |
| 🔗 **Accès depuis** | Vue principale Home |
| 🏗️ **Layout** | `bubble-card separator + 2 bubble-card button` |
| 🔴 **Statut** | Affichage présence ✅ - Liaison clim (P4 → P1) 🔧 à faire en dernier |
| 🚧 **Bloquant** | Automations clim basées sur `sensor.groupe` - à documenter après finalisation Pôle 1 |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-10-10 |
| 🏠 **Version HA** | 2026.10.0 |

---

# 📶 Vignette : Détection WiFi & Présence (PAGE_Home L0C0)

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Sections](#sections)
   - [Séparateur "Personne(s)"](#séparateur-personnes)
   - [Carte Présence Eric](#carte-présence-eric)
   - [Carte Présence Mamour](#carte-présence-mamour)
4. [Entités utilisées](#entités-utilisées--provenance-complète)
5. [Logique des états](#logique-des-états)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Groupe de 3 cartes bubble-card affiché dans la vue Home. Il permet de visualiser d'un coup d'œil :

- L'état global du domicile (les deux présents / un seul / personne) via le **séparateur coloré**
- La présence d'**Eric** et de **Mamour**, chacune avec sa photo de profil et l'heure du dernier changement d'état

La couleur du séparateur est pilotée par `sensor.etat_wifi_maison` qui agrège la connexion WiFi des deux téléphones sur les réseaux `Module B.E.R.Y.L. [GG-5.0]` ou `Module B.E.R.Y.L. [GG-2.4]`.

### Intégrations requises

- ✅ `mobile_app` (Companion App sur Poco X7 Pro × 2) - fournit `device_tracker.*`
- ✅ `person` (intégration native HA) - combine `device_tracker` (eric / mamour) + zones

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `bubble-card` | Séparateur coloré + boutons de présence |

---

## 🏗️ ARCHITECTURE

```
┌──────────────────────────────────────────────────────────┐
│  SÉPARATEUR "Personne(s)"  [bubble-card separator]       │
│  ├─ Couleur fond : darkgreen / darkorange / grey         │
│  └─ Sub-button : sensor.etat_wifi_maison  (Maison)       │
├──────────────────────────────────────────────────────────┤
│  BOUTON ERIC  [bubble-card button]  grid: 2 col / 1 row  │
│  ├─ Entité principale : device_tracker.poco              │
│  └─ Sub-button : person.eric  (photo de profil)          │
├──────────────────────────────────────────────────────────┤
│  BOUTON MAMOUR  [bubble-card button]  grid: 2 col / 1 row│
│  ├─ Entité principale : device_tracker.mamour            │
│  └─ Sub-button : person.mamour  (photo de profil)        │
└──────────────────────────────────────────────────────────┘
```

---

## 📍 SECTION - Séparateur "Personne(s)"

### Code

```yaml
- type: custom:bubble-card
  card_type: separator
  name: Personne(s)
  icon: mdi:account-group
  card_layout: normal
  rows: 1
  styles: |
    .bubble-line {
      background: var(--primary-text-color);
      opacity: 0.8;
    }
    .bubble-sub-button {
      background-color: ${
        hass.states['sensor.etat_wifi_maison'].state === '2'
          ? 'darkgreen'
          : (hass.states['sensor.etat_wifi_maison'].state === 'Eric' ||
             hass.states['sensor.etat_wifi_maison'].state === 'Mamour')
            ? 'darkorange'
            : 'grey'
      } !important;
      color: gainsboro !important;
    }
    ha-card {
      margin-top: 20px !important;
    }
  sub_button:
    - entity: sensor.etat_wifi_maison
      show_last_changed: false
      show_state: true
      show_icon: true
      icon: mdi:home
      show_attribute: false
      show_name: true
      name: Maison
```

### Rôle

Séparateur de section avec indicateur coloré global. Le `sub_button` affiche l'état de `sensor.etat_wifi_maison` avec la couleur de fond injectée via JavaScript dans le champ `styles`.

### Logique des couleurs

| État du sensor | Couleur fond | Signification |
|:--------------|:-------------|:--------------|
| `'2'` | `darkgreen` | Eric + Mamour présents |
| `'Eric'` | `darkorange` | Eric seul à la maison |
| `'Mamour'` | `darkorange` | Mamour seule à la maison |
| tout autre | `grey` | Personne (ou indéfini) |

---

## 📍 SECTION - Carte Présence Eric

### Code

```yaml
- type: custom:bubble-card
  card_type: button
  button_type: state
  entity: device_tracker.poco
  show_name: true
  show_last_changed: true
  show_attribute: false
  card_layout: normal
  layout_options:
    grid_columns: 2
    grid_rows: 1
  show_state: false
  sub_button:
    - entity: person.eric
      show_state: false
      show_icon: true
      show_background: true
      show_attribute: false
      attribute: entity_picture
```

### Rôle

Affiche l'état de présence d'Eric avec l'heure du dernier changement et la photo de profil en sub-button.

Couleurs, pilotées par le JavaScript du champ `styles` :

| État | Rendu |
|:-----|:------|
| `home` | fond `green`, icône `darkgreen`, pictogramme `mdi:home` |
| tout autre état | aucune couleur forcée : la carte garde son rendu par défaut |

---

## 📍 SECTION - Carte Présence Mamour

### Code

```yaml
- type: custom:bubble-card
  card_type: button
  button_type: state
  entity: device_tracker.mamour
  name: Mamour
  show_name: true
  show_last_changed: true
  show_attribute: false
  card_layout: normal
  layout_options:
    grid_columns: 2
    grid_rows: 1
  show_state: false
  sub_button:
    main:
    - entity: person.mamour
      show_state: false
      show_icon: true
      show_background: true
      show_attribute: false
      attribute: entity_picture
  styles: |
    .bubble-button-background {
      background-color:
        ${ state === 'home' ? 'darkgreen'
          : state === 'not_home' ? 'rgb(255, 103, 0)'
          : ['LECLERC','MONOPRIX','AUCHAN'].concat(['ANITA','KIPUE']).includes(state)
            ? 'rgb(0, 102, 204)'
            : 'grey' } !important;
    }
```

### Rôle

Affiche la présence de Mamour avec sa photo de profil. Le champ `name: Mamour` surcharge
le nom de l'entité. Couleurs : maison en `darkgreen`, hors maison en orange, lieux
(courses `LECLERC`/`MONOPRIX`/`AUCHAN` avec `mdi:basket-check`, `ANITA`/`KIPUE` avec
`mdi:map-marker`) en bleu, tout autre état en gris.

⚠️ Les noms testés sont ceux des **vraies zones** déclarées dans HA. L'ancienne version
testait `LECLERC VENCE` (la zone s'appelle `LECLERC`) et `Primark` (inexistant) : deux
branches mortes, corrigées le 2026-10-10.

---

## 📊 ENTITÉS UTILISÉES - PROVENANCE COMPLÈTE

---

### 🌐 Intégrations natives HA (UI - aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| `device_tracker.poco` | `mobile_app` | App Companion → Paramètres > Intégrations (téléphone d'Eric) |
| `device_tracker.mamour` | `mobile_app` | App Companion → Paramètres > Intégrations |
| `person.eric` | `person` | Paramètres > Personnes |
| `person.mamour` | `person` | Paramètres > Personnes |

---

### 📁 `templates/P4_groupe_presence/P4_groupe_presence.yaml`

> Capteurs de détection WiFi - vérifient la connexion à `Freebox_GG` pour chaque téléphone et calculent l'état agrégé du domicile.

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.condition_eric_wifi` | `condition_eric_wifi` | `true` si Eric connecté WiFi sur `Module B.E.R.Y.L.` |
| `sensor.condition_mamour_wifi` | `condition_mamour_wifi` | `true` si Mamour connectée WiFi sur `Module B.E.R.Y.L.` |
| `sensor.etat_wifi_maison` | `etat_wifi_maison` | Agrégat : `2` / `Eric` / `Mamour` / `0` |

---

## 🔁 LOGIQUE DES ÉTATS

### sensor.condition_eric_wifi / condition_mamour_wifi

Renvoie `true` si le `device_tracker` correspondant est en mode `wifi` ET connecté au SSID `Module B.E.R.Y.L. [GG-5.0]` ou `[GG-2.4]`. Sinon `false`.

### sensor.etat_wifi_maison

```jinja2
{% set mamour = is_state('sensor.condition_mamour_wifi', 'true') %}
{% set eric   = is_state('sensor.condition_eric_wifi',   'true') %}
{% if mamour and eric %}    2
{% elif mamour %}           Mamour
{% elif eric %}             Eric
{% else %}                  0
{% endif %}
```

**Attribut `couleur`** (non utilisé dans le dashboard actuel, disponible pour futures automations) :

| État | Couleur |
|:-----|:--------|
| `2` | `green` |
| `Mamour` | `orange` |
| `Eric` | `gold` |
| `0` | `red` |

---

## 🐛 DÉPANNAGE

### Le séparateur reste gris alors qu'un téléphone est à la maison

1. Vérifier `sensor.condition_eric_wifi` ou `sensor.condition_mamour_wifi` dans Outils de développement → États
2. S'assurer que le téléphone est bien connecté à `Module B.E.R.Y.L. [GG-5.0]` ou `[GG-2.4]` (et non en 4G/5G)
3. Vérifier que l'App Companion est active et que `device_tracker.*` est en état `home`

### La photo de profil n'apparaît pas

1. Vérifier que `person.eric` / `person.mamour` ont une photo définie dans Paramètres > Personnes
2. L'attribut `entity_picture` doit être renseigné sur l'entité `person`


---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `mobile_app` (Companion App) | Intégration native | ✅ Essentiel |
| `person` | Intégration native | ✅ Essentiel |
| `bubble-card` | HACS | ✅ Essentiel |
| `templates/P4_groupe_presence/P4_groupe_presence.yaml` | Template sensor (détection WiFi) | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)

- `templates/P4_groupe_presence/P4_groupe_presence.yaml` (capteurs WiFi)
- `templates/P4_groupe_presence/P4_wifi_detection.yaml`

### Dashboard source

- `.../Carte Présence/card_presence_separateur.yaml` (séparateur), `.../card_presence_eric.yaml` (Eric), `.../card_presence_mamour.yaml` (Mamour)

---

← Retour : `L1C1_METEO/PAGE_METEO.md` | → Suivant : `L1C3_TEMPERATURES/L1C3_VIGNETTE_TEMPERATURES.md`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[PAGE_HOME]]*
