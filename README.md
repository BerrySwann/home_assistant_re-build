# 🏠 Home Assistant — Re-Build (Berry Swann)

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.x-blue?logo=home-assistant&logoColor=white)](https://www.home-assistant.io/)
[![GitHub last commit](https://img.shields.io/github/last-commit/BerrySwann/home_assistant_re-build)](https://github.com/BerrySwann/home_assistant_re-build)
[![Expert HA](https://img.shields.io/badge/Expert-HAOS_Proxmox-success)](#)
[![Powered by Claude IA](https://img.shields.io/badge/AI_Partner-Claude_Sonnet-blueviolet)](#)

Ce depot est la **refonte complete et modulaire** de la configuration Home Assistant OS (HAOS) tournant sur un **mini-PC Intel NUC sous Proxmox VE**. Il remplace l'ancien depot `home-assistant-config` avec une architecture repensee : 1 fonction = 1 fichier YAML, organisation par Pole fonctionnel, documentation exhaustive par vignette de dashboard.

---

## 📚 Vous voulez comprendre ou reutiliser ce code ?

> **Commencez par le repertoire [`DOCS/`](./DOCS/)**

Chaque vignette du dashboard possede sa propre documentation dans `DOCS/02_docs_dashboard/` : entites utilisees, fichiers sources, chaines de dependances, pieges a eviter. C'est la **porte d'entree** pour comprendre comment tout s'articule avant de plonger dans les YAML.

### Comment ca s'articule (en 3 phrases)

Une donnee suit toujours le meme chemin : **capteur natif** (Zigbee2MQTT, Hue, Linky...) -> **sensor/template** (calcul, kWh, moyenne) -> **utility_meter** (cumul Annuel/Mensuel/Hebdo/Quotidien si besoin) -> **vignette dashboard**. Cote fiabilite, la prod Home Assistant fait toujours foi ; GitHub est une sauvegarde automatique de la prod ; ce depot local (`ReBuild/`) n'est qu'un poste de travail de correction, jamais une verite en soi. Si un jour vous cherchez pourquoi un fichier `.yaml` a un nom bizarre ou une bordure ASCII, c'est dans `CLAUDE.md`.

| Document cle | Role |
|---|---|
| [`INDEX_GLOBAL.md`](./INDEX_GLOBAL.md) | Index unique — 6 sections (IA, config, dashboard, automations, scripts, systeme) — accordeon GitHub. *(3900+ lignes, prevoyez du cafe)* |
| [`DOCS/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md`](./DOCS/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md) | Carte -> Template -> Sensor -> Utility Meter -> Source native — 18 vignettes |
| [`DOCS/05_docs_MD_system/workflow/WORKFLOW_REBUILD.md`](./DOCS/05_docs_MD_system/workflow/WORKFLOW_REBUILD.md) | Procedure de maintenance + historique des sessions |
| [`CLAUDE.md`](./CLAUDE.md) | Regles de codage, nomenclature, arborescences — directives IA completes |

---

## 🧠 Methodologie & IA Thought Partner

La configuration est regie par le fichier maitre :

- 👉 **[`CLAUDE.md`](./CLAUDE.md)** — directives IA actives (nomenclature, hierarchie visuelle, regles de codage, arborescences)

Developpee en collaboration avec **Claude (Anthropic)** pour garantir :

- **Architecture modulaire stricte** : 1 fonction = 1 fichier `.yaml`, 0 approche monolithique
- **Standardisation visuelle** : Boites ASCII arrondies (78 car.) / carrees (37 car.) / tertiaires `# --- slug ---`
- **YAML auto-documente** : chaque fichier embarque un en-tete obligatoire (`## 📝 DESCRIPTION`, `## 🧮 CALCUL & SOURCES`, `## ⚠️ IMPORTANT`, `## 🖥️ TABLEAU DE BORD`)
- **Qualite du code** : `unique_id` rigoureuse, chaînes de dependances documentees par vignette

---

## ⚙️ Systeme & Materiel

| Composant | Detail |
|-----------|--------|
| **OS** | Home Assistant OS (HAOS) — VM Proxmox VE 7.0.0-3 |
| **Materiel** | Mini-PC Intel NUC — SSD 512 Go / RAM 16 Go |
| **Hyperviseur** | Proxmox VE — VM HAOS + LXC services |
| **Zigbee** | Sonoff EFR32MG21 V2 (recue 22/05/2026) — LXC 200 |
| **Acces** | Samba Share, Studio Code Server, SSH, Cloudflared, Tailscale |

### 📦 Services

| Type | Nom | Localisation |
|:-----|:----|:-------------|
| LXC 200 | Zigbee2MQTT + Mosquitto | Proxmox (10.32.154.244) |
| LXC 201 | MariaDB | Proxmox (10.32.154.242) |
| LXC 202 | MyElectricalData | Proxmox (10.32.154.245) |
| Add-on | Cloudflared - Tailscale - Studio Code Server | HA Supervisor |

---

## 🧩 Integrations

### HACS — Custom Components

| Slug | Nom | Role |
|:-----|:----|:-----|
| `spook` | Spook | Extension HA (entites et services supplementaires) |
| `powercalc` | PowerCalc | Calcul puissance virtuelle (ampoules sans wattmetre) |
| `browser_mod` | Browser Mod | Controle navigateur depuis HA |
| `smartir` | SmartIR | Telecommandes IR (clim salon, bureau, chambre) |
| `scheduler` | Scheduler | Planificateur avance (custom:scheduler-card) |
| `meross_lan` | Meross LAN | Prises Meross en local sans cloud |
| `blitzortung` | Blitzortung | Detection foudre temps reel |
| `atmo_france` | Atmo France | Qualite air exterieur (IQA) |
| `vigieau` | VigiEau | Restrictions d'eau en vigueur (L6C3) |
| `soleil` | Soleil (Sun2) | Lever/coucher + azimut/elevation solaire precis |
| `tarifs_edf` | Tarifs EDF | Index HP/HC, couts Tempo/Base (P0) |

### Officielles HA Core

| Integration | Role |
|:------------|:-----|
| `mqtt` | Bus Z2M, Blitzortung, capteurs divers |
| `philips_hue` | Pont Hue (toutes ampoules P3) |
| `broadlink` | Emetteur IR (relai SmartIR) |
| `meteo_france` | Alertes vigilance, previsions, cameras cartes |
| `moon` | Phase lunaire |
| `season` | Detection saison courante |
| `proxmox_ve` | Supervision Proxmox PVE — CPU, RAM, Storage, Status (L4C1) |
| `system_monitor` | Supervision systeme Mini PC — CPU, RAM, disque (L4C2) |
| `mobile_app` | Telephones (presence P4 + batteries portables L5C2) |
| `local_file` | Images vigilance Meteo France |
| `file` | Logs notify (diag conso, ecart Linky/Nodon) |
| `restful` | sensor.blitzortung_lightning_localisation |
| `backup` | Sauvegardes HA |

---

## 🃏 Cartes HACS utilisees

| Type | Carte | Usage principal |
|:-----|:------|:----------------|
| **Graph/Data** | `apexcharts-card` | Graphiques energie, moyennes glissantes, seuils couleur |
| | `mini-graph-card` | Tendances rapides (temperatures, humidite) |
| | `plotly-graph` | Analyse de donnees complexe |
| | `bar-card` | Jauges de consommation et batteries |
| | `flex-table-card` | Tableaux flexibles multi-entites |
| | `history-explorer-card` | Exploration interactive de l'historique |
| **UI/Design** | `bubble-card` | Navigation, pop-ups par piece, boutons tactiles |
| | `mushroom-card` | Eclairage, titres, chips d'etat |
| | `card-mod` | Personnalisation CSS avancee |
| | `layout-card` | Structure des vues (Grid, Masonry) |
| | `stack-in-card` | Groupement de cartes sans bordures |
| | `swipe-card` | Carousels (Meteo, Cameras) |
| | `auto-entities` | Listes dynamiques (fenetres ouvertes, piles faibles) |
| | `tabbed-card` | Onglets glissants JOUR/MOIS/30J |
| | `button-card` | Boutons programmables avances |
| | `streamline-card` | Templates de cartes reutilisables |
| **Specialisees** | `battery-state-card` | Surveillance batteries/piles par groupe (L5C1) |
| | `entity-progress-card` | Barre de progression avec label dynamique (L6C2) |
| | `enhanced-shutter-card` | Gestion visuelle des stores (L3C3) |
| | `tempometer-gauge-card` | Jauges temperature et humidite |
| | `ring-tile-card` | Indicateurs circulaires (MariaDB, CPU) |
| | `multiple-entity-row` | Multi-affichage sur une ligne d'entite |
| | `navbar-card` | Barre de navigation personnalisee |
| | `linky-card` | Suivi MyElectricalData (L2C1) |
| | `windrose-card` | Rose des vents (L1C1 Meteo) |
| | `meteofranceweathercard` | Carte Meteo-France (L1C1) |
| | `horizon-card` | Visualisation lever/coucher soleil |
| | `tsmoon-card` | Phase lunaire |
| | `hass-hue-icons` | Pack icones Hue (prefix `hue:`) |
| | `custom-brand-icons` | Pack icones marques (prefix `phu:`) |

---

## 📊 Architecture modulaire — Organisation par Pole

La configuration est **100% eclatee** — zero fichier monolithique. Chaque fichier a une responsabilite unique, nommee et rangee dans le Pole fonctionnel correspondant.

```
/homeassistant/
├── configuration.yaml          <- point d'entree (includes, integrations)
├── automations.yaml            <- toutes les automations
├── scripts.yaml / scenes.yaml  <- scripts et scenes
│
├── sensors/
│   ├── P0_Energie_total/       <- kWh Nodon + mini/maxi + diag
│   ├── P1_clim_chauffage/      <- kWh + DUT chauffage/clim
│   ├── P2_prise/               <- kWh prises, veilles, mini-pc
│   ├── P3_eclairage/           <- kWh ampoules (unite / zone / total)
│   ├── Air_quality/            <- stats PM2.5 + tCOV (mean 24h)
│   └── meteo/                  <- Blitzortung
│
├── templates/
│   ├── P0_Energie_total_diag/  <- couts HP/HC, ratios, Linky, diag conso
│   ├── P1_clim_chauffage/      <- logique clim, DUT, AVG, totaux, ui_dashboard
│   ├── P2_prise/               <- AVG prises/veilles/mini-pc, all_standby
│   ├── P3_eclairage/           <- puissance (POWER), AVG, ui_dashboard
│   ├── P4_groupe_presence/     <- detection Wi-Fi/reseau, affichage telephones
│   ├── Air_quality/            <- tCOV en ppb (template)
│   ├── Stores/                 <- etats volets motorises (HTML couleur)
│   ├── Inter_BP_Virtuel/       <- interrupteur soufflant SdB (binary_sensor + switch)
│   └── meteo/                  <- alertes, vent, Blitzortung, tendances
│
└── utility_meter/              <- compteurs AMHQ (Annuel/Mensuel/Hebdo/Quotidien)
    ├── P0_Energie_total/       <- index kWh + HP/HC
    ├── P1_clim_chauffage/      <- 6 equipements x 4 periodes
    ├── P2_prise/               <- prises + veilles + mini-pc
    └── P3_eclairage/           <- ampoules (unite / zone / total)
```

**Poles fonctionnels :**

| Pole | Perimetre |
|------|-----------|
| **P0** | Energie globale (Linky, Nodon pince, bilans generaux) |
| **P1** | Chauffage & Climatisation (5 pieces) |
| **P2** | Prises connectees (18 appareils + veilles) |
| **P3** | Eclairage (19 ampoules Hue/Sonoff — unite / zone / total) |
| **P4** | Groupe Presence (Wi-Fi, reseau mobile, localisation) |
| **M/A/S/B/MP** | Categories lettrees : Meteo, Air, Stores, BP Virtuel, Mini-PC |

---

## 🖥️ Dashboard — Matrice 18 Vignettes

Dashboard optimise tablette + mobile. Structure en 6 lignes x 3 colonnes.

| | C1 | C2 | C3 |
|--|----|----|-----|
| **L1** | Meteo | Temperatures (6 pieces + ext.) | Commandes Clim |
| **L2** | Energie Generale (Nodon/Linky) | Energie Clim / Radiateur | Energie Eclairage |
| **L3** | Commandes Eclairage | Commandes Eco (Prises) | Fenetres + Stores |
| **L4** | Proxmox (PVE) | Mini-PC (NUC) | Mises a jour HA |
| **L5** | Batteries / Piles | Batteries Portables | MariaDB |
| **L6** | Qualite de l'air (PM2.5 + tCOV) | Pollution / Pollen (AtmoFrance) | Vigilance Eau (Vigieau) |

---

## 📁 Documentation (`DOCS/`) — Structure complete

```
DOCS/
├── 00_IA/                          <- contextes IA (IA_CONTEXT_BASE + sous_md/)
├── 01_docs_config_system/
│   ├── config_system_YAML/         <- YAML config HA (source -> /homeassistant/)
│   └── config_system_MD/           <- documentation configuration.yaml
├── 02_docs_dashboard/
│   ├── dashboard_docs_MD/          <- docs 18 vignettes + DEPENDANCES_GLOBALES
│   └── dashboard_docs_YAML/        <- YAML vignettes/pages + Dashboard_COMPLET/
├── 03_docs_automations/
│   ├── docs_automations_MD/        <- docs par automation
│   └── docs_automations_YAML/      <- YAML individuels par automation
├── 04_docs_scripts/
│   ├── docs_scripts_SH/            <- scripts bash (.sh)
│   ├── docs_scripts_SH_MD/         <- docs scripts bash
│   ├── docs_scripts_YAML/          <- scripts HA YAML
│   └── docs_scripts_YAML_MD/       <- docs scripts HA
└── 05_docs_MD_system/              <- MOC, templates, workflow, index entites
```

---

## 🏗️ Dossier de travail local (`ReBuild/`)

Le depot est maintenu depuis un **dossier de travail local** (`C:\Users\Berry Swann\Documents\ReBuild\`) via Claude (Cowork mode) :

```
ReBuild/
├── CLAUDE.md                   <- directives IA (source de verite)
├── Github/
│   ├── INDEX_GLOBAL.md         <- index unique 6 sections (accordeon GitHub)
│   └── README.md
├── DOCS/                       <- toute la documentation + YAML de travail
├── historique/                 <- journaux de session
└── secrets.yaml                <- identifiants (NE PAS synchroniser)
```

> Procedure de maintenance detaillee : [`DOCS/05_docs_MD_system/workflow/WORKFLOW_REBUILD.md`](./DOCS/05_docs_MD_system/workflow/WORKFLOW_REBUILD.md)

---

## 📖 Liens

- [Forum HACF](https://forum.hacf.fr)
- [Documentation Officielle HA](https://www.home-assistant.io/docs/)
- [Ancien depot](https://github.com/BerrySwann/home-assistant-config) *(archive — remplace par ce re-build)*

---

✨ **Projet vivant — architecture modulaire, documentee, maintenue avec Claude (Anthropic)**
