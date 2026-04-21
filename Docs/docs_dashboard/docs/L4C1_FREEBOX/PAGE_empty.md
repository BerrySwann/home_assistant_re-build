<div align="center">

[![Statut](https://img.shields.io/badge/Statut-%E2%9B%94%20OBSOL%C3%88TE-f44336?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![Modifié](https://img.shields.io/badge/MàJ-2026--04--17-44739e?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-Page%20%2B%20Popup-ff9800?style=flat-square)](.)

</div>

| Champ | Valeur |
|:------|:-------|
| 📁 **Path** | `/dashboard-tablette/systeme-freebox` |
| 🔗 **Accès depuis** | Vignette L4C1 (tap) — placeholder Empty |
| 🏗️ **Layout** | `type: grid` — 2 colonnes |
| ✏️ **Prompt** | Eric · BerrySwann |
| 🤖 **Créateur** | Claude · Anthropic |
| 📅 **Modifié le** | 2026-04-17 |
| 🏠 **Version HA** | 2026.3 |

> ⛔ **PAGE OBSOLÈTE — 2026-04-17**
>
> **Freebox** : Routeur Beryl positionné en coupure entre la Freebox et HA → accès aux données Freebox impossible. Intégration supprimée du dashboard. Entités fantômes `sensor.freebox_download_speed` et `sensor.freebox_upload_speed` supprimées (voir `orphelin.md` section D).
>
> **SpeedTest** : Binaire CLI manquant au démarrage (`/config/3rdparty/speedtest/speedtest` → erreur 127). Causait des erreurs au boot. Intégration abandonnée et supprimée du dashboard (voir `orphelin.md` section E).
>
> Le contenu ci-dessous est conservé à titre d'archive historique.

---

# 🌐 L4C1 — Page Freebox Pop + Pop-up Speedtest ⛔ OBSOLÈTE

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Section Speedtest](#section-speedtest)
4. [Section Freebox Info](#section-freebox-info)
5. [Pop-up Historique Speedtest](#pop-up-historique-speedtest-speedtest_details)
6. [Entités utilisées](#entités-utilisées--provenance-complète)
7. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

Page réseau en 2 zones principales : le bloc **Speedtest** (déclenchement manuel + bouton popup historique) et le bloc **Freebox** (infos IP, uptime, firmware + températures graphe 24h). Un pop-up dédié `#speedtest_details` affiche l'historique Download/Upload/Ping sur 24h avec seuils de couleur.

> ⚠️ **Raspberry Pi vs x86-64** : les entités `sensor.freebox_temperature_*` et `device_tracker.freebox_v8_r1` sont fournies par l'intégration native Freebox. Les attributs disponibles (IPv4, IPv6, firmware_version) peuvent différer selon la version HA et l'architecture hôte.

### Intégrations requises

- ✅ Freebox (natif HA — Paramètres > Appareils & Services)
- ✅ Speedtest CLI (intégration HACS ou natif selon version)

### Cartes HACS utilisées

| Carte | Usage |
|-------|-------|
| `custom:bubble-card` | Boutons action, séparateurs, pop-up |
| `custom:stack-in-card` | Bloc Freebox info (image + entities + graph) |
| `custom:apexcharts-card` | Températures Freebox 24h |
| `custom:mini-graph-card` | Graphiques Download / Upload / Ping |
| `custom:multiple-entity-row` | IPv4, IPv6, Uptime, Connection multi-attributs |
| `custom:mushroom-chips-card` | Chip ISP + serveur Speedtest |

---

## 🏗️ ARCHITECTURE

```
┌─────────────────────────────────────────────┐
│  HEADING — FREEBOX                          │
├─────────────────────────────────────────────┤
│  SPEEDTEST                                  │
│  ├── Séparateur (phu:speedtest + last_changed)
│  ├── Bouton "Démarrer Speedtest"            │
│  │     └── homeassistant.update_entity      │
│  │           → sensor.speedtest_cli_data    │
│  └── Bouton "Afficher Historique"           │
│        └── navigate → #speedtest_details   │
├─────────────────────────────────────────────┤
│  FREEBOX INFO (stack-in-card)               │
│  ├── Image header (/local/images/free-1.jpeg)
│  ├── IPv4 / IPv6 (attributs device_tracker) │
│  ├── Uptime / Connection / Firmware         │
│  ├── Download speed / Upload speed         │
│  └── ApexCharts Températures 24h           │
│        (temp_1 × 2 + cpu_b)                │
└─────────────────────────────────────────────┘

POP-UP #speedtest_details
┌─────────────────────────────────────────────┐
│  Header : "Historique du Speedtest"         │
│  ├── Séparateur + last_changed              │
│  ├── Chip ISP + Serveur (nom/ville/pays)    │
│  ├── Download (bubble state + mini-graph)   │
│  │     seuils : 100/200/400/600/800 Mbps    │
│  ├── Upload (bubble state + mini-graph)     │
│  │     seuils : 50/100/200/400/600 Mbps     │
│  └── Ping (horizontal-stack + mini-graph)  │
│        seuils : 40/35/30/25/20 ms           │
└─────────────────────────────────────────────┘
```

---

## 📍 SECTION SPEEDTEST

### Code

```yaml
- type: custom:bubble-card
  card_type: separator
  name: Speedtest
  icon: phu:speedtest
  sub_button:
    - entity: sensor.speedtest_cli_data
      icon: mdi:clock-time-four-outline
      show_last_changed: true
      show_icon: true
      show_background: true

- type: custom:bubble-card
  card_type: button
  button_type: name
  name: Démarrer Speedtest
  icon: phu:speedtest
  tap_action:
    action: perform-action
    perform_action: homeassistant.update_entity
    target:
      entity_id: sensor.speedtest_cli_data
  button_action:
    tap_action:
      action: perform-action
      perform_action: homeassistant.update_entity
      target:
        entity_id: sensor.speedtest_cli_data

- type: custom:bubble-card
  card_type: button
  button_type: state
  name: Afficher Historique
  icon: mdi:chart-histogram
  entity: sensor.speedtest_cli_data
  tap_action:
    action: navigate
    navigation_path: "#speedtest_details"
```

### Rôle
Déclencher manuellement un test Speedtest CLI et accéder au popup historique. Le `last_changed` du séparateur indique l'heure du dernier test.

### Entités
- `sensor.speedtest_cli_data` [NAT] — capteur parent Speedtest CLI (attributs isp, server, download, upload, ping)
- `sensor.speedtest_download` [NAT] — utilisé comme cible secondaire dans le bouton démarrer

---

## 📍 SECTION FREEBOX INFO

### Code

```yaml
- type: custom:stack-in-card
  mode: vertical
  cards:
    - type: entities
      header:
        type: picture
        image: /local/images/free-1.jpeg
      entities:
        - entity: device_tracker.freebox_v8_r1
          type: custom:multiple-entity-row
          name: "External IPv4:"
          icon: mdi:ip
          show_state: false
          entities:
            - entity: device_tracker.freebox_v8_r1
              attribute: IPv4
              name: " "
        - entity: device_tracker.freebox_v8_r1
          type: custom:multiple-entity-row
          name: "External IPv6:"
          icon: mdi:ip
          show_state: false
          entities:
            - entity: device_tracker.freebox_v8_r1
              attribute: IPv6
              name: " "
        - entity: device_tracker.freebox_v8_r1
          type: custom:multiple-entity-row
          name: Uptime
          icon: mdi:web-clock
          show_state: false
          entities:
            - entity: device_tracker.freebox_v8_r1
              attribute: uptime
              format: total
        - entity: device_tracker.freebox_v8_r1
          type: custom:multiple-entity-row
          name: Connection
          icon: mdi:wan
          show_state: false
          entities:
            - entity: device_tracker.freebox_v8_r1
              attribute: connection_type
              name: Type
            - entity: device_tracker.freebox_v8_r1
              attribute: firmware_version
              name: firmware
        - entity: sensor.freebox_download_speed
          name: Freebox download speed
          icon: mdi:arrow-down-thick
        - entity: sensor.freebox_upload_speed
          name: Freebox upload speed
          icon: mdi:arrow-up-thick
    - type: custom:apexcharts-card
      graph_span: 24h
      update_interval: 1m
      header:
        show: true
        title: Température 1, 2 & CPU B
        show_states: true
        colorize_states: true
      series:
        - entity: sensor.freebox_temperature_1
          name: Température 1
        - entity: sensor.freebox_temperature_1
          name: Température 2
        - entity: sensor.freebox_temperature_cpu_b
          name: Température CPU B
          color: green
```

### Rôle
Afficher les informations réseau de la Freebox Pop : IP publiques, uptime, type de connexion, firmware, débits instantanés et évolution des températures sur 24h.

### Entités
- `device_tracker.freebox_v8_r1` [NAT] — tracker Freebox (attributs : IPv4, IPv6, uptime, connection_type, firmware_version)
- `sensor.freebox_download_speed` [NAT] — débit descendant Freebox (Mbps)
- `sensor.freebox_upload_speed` [NAT] — débit montant Freebox (Mbps)
- `sensor.freebox_temperature_1` [NAT] — température sonde 1 Freebox
- `sensor.freebox_temperature_cpu_b` [NAT] — température CPU B Freebox

---

## 📍 POP-UP HISTORIQUE SPEEDTEST (`#speedtest_details`)

### Code

```yaml
- type: vertical-stack
  cards:
    - type: custom:bubble-card
      card_type: pop-up
      hash: "#speedtest_details"
      name: Historique du Speedtest
      icon: phu:speedtest
      close_on_click: true
      bg_opacity: 0
    - type: custom:bubble-card
      card_type: separator
      name: Historique des Speedtest
      icon: mdi:chart-histogram
      sub_button:
        - entity: sensor.speedtest_cli_data
          show_last_changed: true
          icon: mdi:clock-time-two-outline
          show_background: true
          name: Date du dernier test
    - type: custom:mushroom-chips-card
      chips:
        - type: template
          icon: mdi:server-outline
          icon_color: gainsboro
          content: >-
            {{ state_attr('sensor.speedtest_cli_data', 'isp') }} <-> Server:
            {{ state_attr('sensor.speedtest_cli_data', 'server').name }} /
            {{ state_attr('sensor.speedtest_cli_data', 'server').location }} /
            {{ state_attr('sensor.speedtest_cli_data', 'server').country }}
    # Download bubble + mini-graph
    - type: custom:bubble-card
      card_type: button
      button_type: state
      entity: sensor.speedtest_cli_download
      name: Download
      icon: mdi:speedometer
    - type: custom:mini-graph-card
      entities:
        - entity: sensor.speedtest_cli_download
          name: Download
      hours_to_show: 24
      color_thresholds:
        - value: 100
          color: "#ef1d0f"
        - value: 200
          color: "#ef5a0f"
        - value: 400
          color: "#f0da11"
        - value: 600
          color: "#11f13a"
        - value: 800
          color: "#1da4f2"
    # Upload bubble + mini-graph
    - type: custom:bubble-card
      card_type: button
      button_type: state
      entity: sensor.speedtest_cli_upload
      name: Upload
      icon: mdi:speedometer
    - type: custom:mini-graph-card
      entities:
        - entity: sensor.speedtest_cli_upload
          name: Upload
      hours_to_show: 24
      color_thresholds:
        - value: 50
          color: "#ef1d0f"
        - value: 100
          color: "#ef5a0f"
        - value: 200
          color: "#f0da11"
        - value: 400
          color: "#11f13a"
        - value: 600
          color: "#1da4f2"
    # Ping
    - type: horizontal-stack
      cards:
        - type: custom:bubble-card
          card_type: button
          button_type: state
          entity: sensor.speedtest_cli_ping
          name: Ping
          icon: mdi:speedometer
    - type: custom:mini-graph-card
      entities:
        - entity: sensor.speedtest_cli_ping
          name: Ping (24h)
      hours_to_show: 24
      color_thresholds:
        - value: 40
          color: "#ef1d0f"
        - value: 35
          color: "#ef5a0f"
        - value: 30
          color: "#f0da11"
        - value: 25
          color: "#11f13a"
        - value: 20
          color: "#1da4f2"
```

### Rôle
Pop-up dédié à l'historique des tests Speedtest CLI sur 24h. Trois graphiques mini-graph avec seuils de couleur pour évaluer la qualité de la connexion (Download/Upload en Mbps, Ping en ms).

### Seuils de couleur Download

| Valeur | Couleur | Signification |
|--------|---------|---------------|
| < 100 Mbps | Rouge `#ef1d0f` | Faible |
| 100–200 Mbps | Orange `#ef5a0f` | Correct |
| 200–400 Mbps | Jaune `#f0da11` | Bon |
| 400–600 Mbps | Vert `#11f13a` | Très bon |
| > 600 Mbps | Bleu `#1da4f2` | Excellent |

### Entités
- `sensor.speedtest_cli_data` [NAT] — parent (attributs ISP, serveur)
- `sensor.speedtest_cli_download` [TPL] — `templates/SpeedTest/ST_01_speedTest.yaml`
- `sensor.speedtest_cli_upload` [TPL] — `templates/SpeedTest/ST_01_speedTest.yaml`
- `sensor.speedtest_cli_ping` [TPL] — `templates/SpeedTest/ST_01_speedTest.yaml`

---

## 📊 ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE

### 🌐 Intégrations natives HA (UI — aucun fichier YAML à créer)

| Entité | Intégration | Configuré via |
|--------|-------------|---------------|
| `device_tracker.freebox_v8_r1` [NAT] | Freebox (natif) | Paramètres > Appareils & Services |
| `sensor.freebox_download_speed` [NAT] | Freebox (natif) | idem |
| `sensor.freebox_upload_speed` [NAT] | Freebox (natif) | idem |
| `sensor.freebox_temperature_1` [NAT] | Freebox (natif) | idem |
| `sensor.freebox_temperature_cpu_b` [NAT] | Freebox (natif) | idem |
| `sensor.speedtest_cli_data` [NAT] | Speedtest CLI | Paramètres > Appareils & Services |
| `sensor.speedtest_download` [NAT] | Speedtest | idem |

---

### 📁 `templates/SpeedTest/ST_01_speedTest.yaml`
> Templates extraisant Download / Upload / Ping depuis `sensor.speedtest_cli_data`

| Entité | unique_id | Rôle |
|--------|-----------|------|
| `sensor.speedtest_cli_download` [TPL] | `speedtest_cli_download` | Débit descendant en Mbps |
| `sensor.speedtest_cli_upload` [TPL] | `speedtest_cli_upload` | Débit montant en Mbps |
| `sensor.speedtest_cli_ping` [TPL] | `speedtest_cli_ping` | Latence en ms |

---

## 🐛 DÉPANNAGE

### `sensor.speedtest_cli_data` indisponible
1. Vérifier que l'intégration Speedtest CLI est bien configurée dans Paramètres > Appareils & Services.
2. Lancer un test manuel depuis le bouton "Démarrer Speedtest" pour forcer la mise à jour.
3. Si l'attribut `.bandwidth` est absent, vérifier la version de l'intégration Speedtest (format JSON différent selon les versions).

### `device_tracker.freebox_v8_r1` — attributs manquants (IPv4, IPv6…)
1. Vérifier que l'intégration Freebox est bien configurée et authentifiée.
2. Sur x86-64 (vs Raspberry Pi), certains attributs peuvent ne pas être exposés selon la version du firmware Freebox et du pilote HA.
3. Consulter les logs HA → Outils développeur > Journaux pour détecter les erreurs Freebox.

### Températures Freebox absentes dans ApexCharts
1. `sensor.freebox_temperature_1` est doublement déclaré dans la série (Température 1 et 2) — il s'agit probablement d'un doublon volontaire ou d'une coquille (Température 2 devrait pointer vers `sensor.freebox_temperature_2`).
2. Vérifier l'existence de `sensor.freebox_temperature_2` dans Outils développeur > États.

---

## 📝 DÉPENDANCES CRITIQUES

| Élément | Type | Statut |
|---------|------|--------|
| Intégration Freebox | Native HA | ✅ Essentiel |
| Intégration Speedtest CLI | Native / HACS | ✅ Essentiel |
| `templates/SpeedTest/ST_01_speedTest.yaml` | Template YAML | ✅ Essentiel |
| `custom:bubble-card` | HACS | ✅ Essentiel |
| `custom:apexcharts-card` | HACS | ✅ Essentiel |
| `custom:mini-graph-card` | HACS | ✅ Essentiel |
| `custom:stack-in-card` | HACS | ✅ Essentiel |
| `custom:multiple-entity-row` | HACS | ✅ Essentiel |
| `custom:mushroom-chips-card` | HACS | ✅ Essentiel |
| `/local/images/free-1.jpeg` | Image locale | ⚠️ Optionnel (header visuel) |

---

## 🔗 FICHIERS LIÉS

### Configuration YAML
- `templates/SpeedTest/ST_01_speedTest.yaml` — sensors Download / Upload / Ping

### Documentation
- [`L4C1_VIGNETTE_FREEBOX.md`](./L4C1_VIGNETTE_FREEBOX.md) — vignette navigation

---

← Retour : `L3C3_STORES/` | → Suivant : `L4C2_MINI_PC/`


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]  [[L4C1_VIGNETTE_empty]]*
