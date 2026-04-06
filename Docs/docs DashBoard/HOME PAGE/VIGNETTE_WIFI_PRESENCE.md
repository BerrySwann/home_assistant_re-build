<div align="center">

[![Statut](https://img.shields.io/badge/Statut-En%20cours-ff9800?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2025.2-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--03--01-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Vignette-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `Dashboard 2026-02-07 → Vue: Home → Groupe "Personne(s)"` |
| 🔗 **Accès depuis** | Vue principale Home |
| 🏗️ **Layout** | `bubble-card separator + 2× bubble-card button` |
| 🔴 **Statut** | Affichage présence ✅ — Liaison clim (P4 → P1) 🔧 à faire en dernier |
| 🚧 **Bloquant** | Automations clim basées sur `sensor.groupe` — à documenter après finalisation Pôle 1 |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-03-01 |
| 🏠 **Version HA** | 2025.2.x → v2.0 |

---

# 📶 L1C2 — Vignette : Détection WiFi & Présence

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
- La présence individuelle de **Eric** et de **Mamour** avec leur photo de profil et l'heure du dernier changement d'état

La couleur du séparateur est pilotée par `sensor.etat_wifi_maison` qui agrège la connexion WiFi des deux téléphones sur les réseaux `Module B.E.R.Y.L. [GG-5.0]` ou `Module B.E.R.Y.L. [GG-2.4]`.

### Intégrations requises

- ✅ `mobile_app` (Companion App sur Poco X7 Pro × 2) — fournit `device_tracker.*`
- ✅ `person` (intégration native HA) — combine `device_tracker` (eric / mamour) + zones

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
│  ├─ Entité principale : device_tracker.eric              │
│  └─ Sub-button : person.eric  (photo de profil)          │
├──────────────────────────────────────────────────────────┤
│  BOUTON MAMOUR  [bubble-card button]  grid: 2 col / 1 row│
│  ├─ Entité principale : device_tracker.mamour            │
│  └─ Sub-button : person.mamour  (photo de profil)        │
└──────────────────────────────────────────────────────────┘
```

---

## 📍 SECTION — Séparateur "Personne(s)"

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

## 📍 SECTION — Carte Présence Eric

### Code

```yaml
- type: custom:bubble-card
  card_type: button
  button_type: state
  entity: device_tracker.eric
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

Affiche l'état de présence de Eric (`home` / `not_home` / nom de zone) avec l'heure du dernier changement et la photo de profil en sub-button. La grille 2 colonnes permet d'aligner la carte Mamour côte à côte.

---

## 📍 SECTION — Carte Présence Mamour

### Code

```yaml
- type: custom:bubble-card
  card_type: button
  button_type: state
  entity: device_tracker.mamour
  show_name: true
  show_last_changed: true
  show_attribute: false
  card_layout: normal
  layout_options:
    grid_columns: 2
    grid_rows: 1
  show_state: false
  sub_button:
    - entity: person.mamour
      show_state: false
      show_icon: true
      show_background: true
      show_attribute: false
      attribute: entity_picture
  name: Mamour
```

### Rôle

Identique à la carte Eric — affiche la présence de Mamour avec sa photo de profil. Le champ `name: Mamour` surcharge le nom de l'entité `device_tracker.mamour` pour un affichage plus lisible.

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

---

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| `device_tracker.eric` | `mobile_app` | App Companion → Paramètres > Intégrations |
| `device_tracker.mamour` | `mobile_app` | App Companion → Paramètres > Intégrations |
| `person.eric` | `person` | Paramètres > Personnes |
| `person.mamour` | `person` | Paramètres > Personnes |

---

### 📁 `templates/06_1_phones_wifi_cellular_card_autom.yaml`

> Capteurs de détection WiFi — vérifient la connexion à `Freebox_GG` pour chaque téléphone et calculent l'état agrégé du domicile.

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

### Les deux cartes Eric/Mamour ne s'affichent pas côte à côte

- Vérifier que le layout parent de la vue utilise `grid_columns: 2` (nécessite HA 2024.x+)
- `layout_options.grid_columns: 2` est défini sur chaque carte bubble-card

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| `mobile_app` (Companion App) | Intégration native | ✅ Essentiel |
| `person` | Intégration native | ✅ Essentiel |
| `bubble-card` | HACS | ✅ Essentiel |
| `templates/06_1_phones_wifi_cellular_card_autom.yaml` | Template sensor | ✅ Essentiel |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML (sources HA v2.0)

- `templates/06_1_phones_wifi_cellular_card_autom.yaml`

### Dashboard source

- `Dashboard 2026-02-07`

---

← Retour : `L1C1_METEO/PAGE_METEO.md` | → Suivant : `L1C3_TEMPERATURES/L1C3_VIGNETTE_TEMPERATURES.md`
