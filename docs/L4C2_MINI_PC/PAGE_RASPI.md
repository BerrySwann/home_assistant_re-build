# PAGE — Raspberry Pi 4 (ancienne page — transitoire)
*Dernière mise à jour : 2026-03-24*
*Path : `/dashboard-tablette/raspberry-pi4`*

> ⚠️ **STATUT : PAGE TRANSITOIRE**
> Cette page documente l'ancienne page RPi4 encore active. Elle sera **remplacée** par `PAGE_MINI_PC.md`
> lors de la bascule définitive vers le Mini PC.
> Les entités spécifiques RPi4 (`fan.rpi_cooling_fan`, `binary_sensor.rpi_power_status`, etc.)
> devront être remappées vers les équivalents Mini PC lors de la migration.

---

## 📋 TABLE DES MATIÈRES

- [Architecture de la page](#architecture-de-la-page)
- [Détail des sections](#détail-des-sections)
  - [Image RPi4](#1-image-rpi4)
  - [IP + Uptime + Ventilateur RPi](#2-ip--uptime--ventilateur-rpi)
  - [Séparateur](#3-séparateur)
  - [Bar-cards métriques système](#4-bar-cards-métriques-système)
  - [Uptime Card](#5-uptime-card)
  - [Commandes ventilateur (6 boutons)](#6-commandes-ventilateur--6-boutons)
- [Entités utilisées](#entités-utilisées--provenance-complète)
- [Logique ventilateur (animations)](#logique-ventilateur--animations)
- [Dépannage](#dépannage)

---

## Architecture de la page

```
/dashboard-tablette/raspberry-pi4
│
├── [stack-in-card vertical] Image RPi4
│   └── picture: /local/images/RPi4B3.png
│
├── [stack-in-card vertical] Infos système (3 lignes)
│   ├── Ligne IP : "IP Int. / Ext." + local_ip + myip
│   ├── Ligne Uptime : label + calcul Jours/Heures/Minutes
│   └── Ligne Fan : état RPi Fan + toggle + pourcentage
│
├── [bubble-card separator]
│
├── [bar-card] CPU %           — target 75, max 100     (rgb(68,115,158))
├── [bar-card] T° CPU          — target 65, max 100     (orange) + min/max
├── [bar-card] Mem USED (MB)   — target 3072, max 4096  (red) + min/max
├── [bar-card] Mem FREE (MB)   — target 3072, max 4096  (rgb(31,111,235)) + min/max
├── [bar-card] SSD 120Go (GB)  — target 100, max 120    (grey) + min/max  [grid 4 cols]
├── [bar-card] Download (MB/s) — target 150, max 1000   (green) + min/max
├── [bar-card] Upload (MB/s)   — target 150, max 1000   (red) + min/max
│
├── [uptime-card] binary_sensor.rpi_power_status — 48h
│
└── [layout-card grid 6 zones] Boutons commandes ventilateur
    ├── zone1: Lent   30%  (lightblue,    rotation 3s)
    ├── zone2: Faible 40%  (rgb(19,160,200), rotation 2.5s)
    ├── zone3: Normal 50%  (rgb(0,158,11),   rotation 2s)
    ├── zone4: Moyen  65%  (rgb(255,197,3),  rotation 1.5s)
    ├── zone5: Fort   85%  (rgb(158,9,24),   rotation 1s)
    └── zone6: Maxi   100% (rgb(255,0,0),    rotation 0.5s)
```

---

## Détail des sections

### 1. Image RPi4

```yaml
type: custom:stack-in-card
mode: vertical
cards:
  - type: picture
    image: /local/images/RPi4B3.png
```

Image statique du Raspberry Pi 4B. Fichier dans `/config/www/images/`.

---

### 2. IP + Uptime + Ventilateur RPi

Bloc `stack-in-card vertical` contenant 3 `stack-in-card horizontal` :

**Ligne 1 — IP :**

| Colonne | Contenu | Entité |
|---------|---------|--------|
| Label | "IP Int. / Ext.:" | _(statique)_ |
| IP locale | `{{ states("sensor.local_ip") }}` | `sensor.local_ip` |
| IP publique | `{{ states('sensor.myip') }}` | `sensor.myip` |

**Ligne 2 — Uptime :**
Calcule la durée écoulée depuis `sensor.system_monitor_dernier_demarrage` :
```jinja
{% set uptime = (now()|as_timestamp - states('sensor.system_monitor_dernier_demarrage')|as_timestamp) %}
{% set jours = (uptime / 86400) | int(0) %}
{%- if jours > 0 -%}
  {{ jours }}d {{ (uptime - (jours * 86400)) | int(0) | timestamp_custom('%Hh %Mm', false) }}
{%- else -%}
  {{ uptime | int(0) | timestamp_custom('%Hh %Mm', false) }}
{%- endif -%}
```
Affiche par ex. `3d 14h 22m` ou `06h 45m`.

**Ligne 3 — Ventilateur RPi :**

| Colonne | Contenu | Entité |
|---------|---------|--------|
| Icône `mdi:fan` | couleur ON=vert / OFF=rouge + animation rotation si ON | `fan.rpi_cooling_fan` |
| Toggle | "Allumé / Éteint" — `tap_action: toggle` | `fan.rpi_cooling_fan` |
| % vitesse | `state_attr('fan.rpi_cooling_fan', 'percentage')` % | `fan.rpi_cooling_fan` |

L'icône fan a une animation CSS `rotation 2s linear infinite` quand la fan est ON.

---

### 3. Séparateur

```yaml
type: custom:bubble-card
card_type: separator
rows: 2
```

Ligne de séparation pleine largeur (`grid_columns: 12`, `grid_rows: 0.5`).

---

### 4. Bar-cards métriques système

Chaque bar-card est dans un `stack-in-card vertical > horizontal-stack`. Style commun : `background: none`, font bold 12px, icon blanc, `bar-card-currentbar/backgroundbar` sans bordure.

| Bar-card | Entité | Couleur | Min | Max | Target | Grid |
|----------|--------|---------|-----|-----|--------|------|
| CPU % | `sensor.system_monitor_utilisation_du_processeur` | rgb(68,115,158) | 0 | 100 | 75 | 2 cols |
| T° CPU | `sensor.system_monitor_temperature_du_processeur` | orange | 0 | 100 | 65 | 2 cols |
| Mem USED | `sensor.system_monitor_memoire_utilisee` | red | 0 | 4096 | 3072 | 2 cols |
| Mem FREE | `sensor.system_monitor_memoire_libre` | rgb(31,111,235) | 0 | 4096 | 3072 | 2 cols |
| SSD 120Go | `sensor.system_monitor_utilisation_du_disque` | grey | 0 | 120 | 100 | **4 cols** |
| Download | `sensor.system_monitor_debit_du_reseau_entrant_via_end0` | green | 0 | 1000 | 150 | 2 cols |
| Upload | `sensor.system_monitor_debit_du_reseau_sortant_via_end0` | red | 0 | 1000 | 150 | 2 cols |

**Positions indicator/minmax :**
- CPU : `indicator: inside` uniquement
- Autres : `indicator: "on"`, `minmax: "on"`

> **Note SSD :** L'entité `system_monitor_utilisation_du_disque` renvoie en % (0-100), mais le max est mis à `120` — à vérifier/corriger lors de la migration Mini PC (SSD réel 120 Go).

---

### 5. Uptime Card

```yaml
type: custom:uptime-card
entity: binary_sensor.rpi_power_status
ok: "off"
ko: "on"
bar:
  amount: 48
  height: 30
hours_to_show: 48
color:
  ok: green
  ko: rgb(250,0,1)
alias:
  ok: Raspberry Pi4 Power - OK
  ko: Raspberry Pi4 Power - Danger
```

Affiche 48 barres (1 par heure) représentant l'état de la prise RPi sur les 48 dernières heures.
Logique inversée : `ok: "off"` = la prise est **sans alerte** (état binaire `off` = normal), `ko: "on"` = problème.

---

### 6. Commandes ventilateur — 6 boutons

`custom:layout-card` avec `custom:grid-layout` — 6 zones égales (`16.75%` chacune).

Chaque bouton `custom:button-card` :
- `tap_action: call-service` → `fan.set_percentage` avec `entity_id: fan.rpi_cooling_fan`
- Couleur icône/nom/label : **active** (% correspondant) ou gris `rgb(128,128,128)` (inactif) ou rouge (fan OFF)
- Animation rotation (vitesse décroissante selon vitesse croissante) :

| Zone | Nom | % | Couleur active | Vitesse rotation |
|------|-----|---|----------------|-----------------|
| zone1 | Lent | 30% | `lightblue` | 3s |
| zone2 | Faible | 40% | `rgb(19,160,200)` | 2.5s |
| zone3 | Normal | 50% | `rgb(0,158,11)` | 2s |
| zone4 | Moyen | 65% | `rgb(255,197,3)` | 1.5s |
| zone5 | Fort | 85% | `rgb(158,9,24)` | 1s |
| zone6 | Maxi | 100% | `rgb(255,0,0)` | 0.5s |

Si `fan.rpi_cooling_fan` est `off` : toutes les icônes/noms passent en rouge `rgb(255,0,0)`, animation `none`.
Condition détection bouton actif : `states['fan.rpi_cooling_fan'].attributes.percentage == XX`.

**Fond des boutons :** `background-color: rgb(255,255,255)` (blanc — contraste pour les couleurs des icônes).

---

## Entités utilisées — Provenance complète

### Catégorie A — System Monitor (intégration HA native)

| Entité | Description |
|--------|-------------|
| `sensor.system_monitor_temperature_du_processeur` | T° CPU (°C) |
| `sensor.system_monitor_utilisation_du_processeur` | CPU (%) |
| `sensor.system_monitor_utilisation_de_la_memoire` | RAM utilisée (%) |
| `sensor.system_monitor_memoire_utilisee` | RAM utilisée (MB) — bar-card |
| `sensor.system_monitor_memoire_libre` | RAM libre (MB) — bar-card |
| `sensor.system_monitor_utilisation_du_disque` | Disque (%) / GB |
| `sensor.system_monitor_debit_du_reseau_entrant_via_end0` | Download réseau (MB/s) |
| `sensor.system_monitor_debit_du_reseau_sortant_via_end0` | Upload réseau (MB/s) |
| `sensor.system_monitor_dernier_demarrage` | Timestamp dernier boot — calcul uptime |

### Catégorie B — Réseau / IP

| Entité | Description | Source |
|--------|-------------|--------|
| `sensor.local_ip` | IP locale du serveur HA | Intégration `local_ip` |
| `sensor.myip` | IP publique (WAN) | Intégration externe |

### Catégorie C — RPi matériel

| Entité | Description | Source |
|--------|-------------|--------|
| `fan.rpi_cooling_fan` | Ventilateur actif du RPi4 (ON/OFF + % vitesse) | Intégration RPi GPIO / custom |
| `binary_sensor.rpi_power_status` | État alimentation RPi4 | Intégration power |

> ⚠️ **Ces entités sont spécifiques au Raspberry Pi 4 et devront être supprimées / remplacées lors de la migration vers le Mini PC.**

### Catégorie D — Automation RPi (régulation ventilateur)

| Entité | Description | Impact visuel page |
|--------|-------------|-------------------|
| `automation.ventilateur_rpi_*` *(nom exact à confirmer)* | Règle automatiquement la vitesse de `fan.rpi_cooling_fan` en fonction de la T° CPU | Le `%` affiché dans le bloc ventilateur et l'animation de rotation **reflètent l'état piloté par cette automation** — sans elle, vitesse figée / manuelle uniquement |

> ⚠️ **Dépendance visuelle directe** : la page ne pilote pas le ventilateur elle-même. Elle affiche uniquement ce que l'automation a déjà réglé. Le bouton-card lit `fan.rpi_cooling_fan.attributes.percentage` pour déterminer le bouton "actif" (en couleur).
> ⚠️ **RPi4 uniquement** — À ne pas migrer sur Mini PC (pas de GPIO, pas de ventilateur physique piloté par HA).

---

## Logique ventilateur — Animations

L'animation CSS `rotating` est définie dans `card_mod` du `button-card` :
```css
@keyframes rotation {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(359deg); }
}
```

Appliquée sur `ha-state-icon` conditionnellement. La durée varie selon le % sélectionné, créant un effet visuel de vitesse progressive.

**Condition "bouton actif" :** `states['fan.rpi_cooling_fan'].attributes.percentage == X` — si le % courant correspond, le bouton s'allume en couleur.

---

## Dépannage

**Fan.rpi_cooling_fan introuvable :**
L'entité dépend de la configuration GPIO du RPi4. Non disponible sur Mini PC — à ne pas migrer tel quel.

**Upload/Download à 0 ou N/A :**
Vérifier que l'interface réseau `end0` est bien le bon nom dans `system_monitor`. Sur certains systèmes, c'est `eth0`, `enp3s0`, etc. Ajuster dans `configuration.yaml`.

**Mémoire USED/FREE incohérentes avec % :**
`memoire_utilisee` et `memoire_libre` sont en MB. Le max est hardcodé à `4096` (4 Go) — correct pour RPi4 4Go. À adapter au Mini PC (RAM différente).

**Image RPi4B3.png absente :**
Le fichier doit être dans `/config/www/images/`. Sur Mini PC, remplacer par une image appropriée.

---

## Fichiers liés

| Fichier | Rôle |
|---------|------|
| `configuration.yaml` | Intégration `system_monitor` + `local_ip` |
| *(futur)* `docs/L4C2_MINI_PC/PAGE_MINI_PC.md` | À créer après migration Mini PC |
