# 🏠 Home Assistant — Re-Build (Berry Swann)

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.x-blue?logo=home-assistant&logoColor=white)](https://www.home-assistant.io/)
[![GitHub last commit](https://img.shields.io/github/last-commit/BerrySwann/home_assistant_re-build)](https://github.com/BerrySwann/home_assistant_re-build)
[![Expert HA](https://img.shields.io/badge/Expert-HAOS_x86--64-success)](#)
[![Powered by Claude IA](https://img.shields.io/badge/AI_Partner-Claude_Sonnet-blueviolet)](#)

Ce dépôt est la **refonte complète et modulaire** de la configuration Home Assistant OS (HAOS) tournant sur un **mini-PC x86-64 (Generic image)**. Il remplace l'ancien dépôt `home-assistant-config` avec une architecture repensée : 1 fonction = 1 fichier YAML, organisation par Pôle fonctionnel, documentation exhaustive par vignette de dashboard.

---

## 📚 Vous voulez comprendre ou réutiliser ce code ?

> **Commencez par le répertoire [`docs/`](./docs/)**

Chaque vignette du dashboard possède sa propre documentation dans `docs/` : entités utilisées, fichiers sources, chaînes de dépendances, pièges à éviter. C'est la **porte d'entrée** pour comprendre comment tout s'articule avant de plonger dans les YAML.

| Document clé | Rôle |
|---|---|
| [`INDEX_NAVIGATION.md`](./INDEX_NAVIGATION.md) | Index des 18 vignettes — accès direct docs, YAML, entités, pop-ups (accordéon GitHub) |
| [`Docs/docs_dashboard/docs/DEPENDANCES_GLOBALES.md`](./Docs/docs_dashboard/docs/DEPENDANCES_GLOBALES.md) | Carte → Template → Sensor → Utility Meter → Source native — pour les 18 vignettes |
| [`Docs/docs_dashboard/docs/WORKFLOW_REBUILD.md`](./Docs/docs_dashboard/docs/WORKFLOW_REBUILD.md) | Procédure de maintenance + historique de toutes les sessions |
| [`CLAUDE.md`](./CLAUDE.md) | Règles de codage, nomenclature, arborescences — directives IA complètes |
| [`Orphelin/orphelin.md`](./Orphelin/orphelin.md) | Inventaire lisible des entités fantômes détectées par Spook |

---

## 🧠 Méthodologie & IA Thought Partner

La configuration est régie par deux fichiers maîtres :

- 👉 **[`CLAUDE.md`](./CLAUDE.md)** — directives IA actives (nomenclature, hiérarchie visuelle, règles de codage, arborescences)
- 👉 **[`IA/IA_CONTEXT_BASE.md`](./IA/IA_CONTEXT_BASE.md)** — copie synchronisée de `CLAUDE.md` (référence IA)

Développée en collaboration avec **Claude (Anthropic)** pour garantir :

- **Architecture modulaire stricte** : 1 fonction = 1 fichier `.yaml`, 0 approche monolithique
- **Standardisation visuelle** : Boîtes ASCII arrondies (78 car.) / carrées (37 car.) / tertiaires `# --- slug ---`
- **YAML auto-documenté** : chaque fichier embarque un en-tête obligatoire (`## 📝 DESCRIPTION`, `## 🧮 CALCUL & SOURCES`, `## ⚠️ IMPORTANT`, `## 🖥️ TABLEAU DE BORD`) — comprendre à quoi sert chaque entité sans ouvrir la doc
- **Qualité du code** : Zéro `id:` global dans les automatisations, `unique_id` rigoureuse, annotations `# "[L...] modif"` sur chaque ligne modifiée
- **Traçabilité** : Inventaire complet des entités fantômes (`Orphelin/orphelin.yaml`), chaînes de dépendances documentées par vignette (`docs/DEPENDANCES_GLOBALES.md`)

---

## ⚙️ Système & Matériel

| Composant | Détail |
|-----------|--------|
| **OS** | Home Assistant OS (HAOS) — image Generic x86-64 |
| **Matériel** | Mini-PC Intel NUC — SSD SATA 512 Go / RAM 16 Go |
| **Zigbee** | Sonoff EFR32MG21 — Clé V2 (reçue 22/05/2026) — LXC 200 Proxmox |
| **Accès** | Samba Share, Studio Code Server, SSH, Cloudflared, Tailscale |

### 📦 Add-ons principaux

Zigbee2MQTT · Mosquitto (LXC 200) · MariaDB (LXC 201) · Cloudflared · Tailscale · Studio Code Server · Samba Share · Spook

---

## 🧩 Intégrations

| Catégorie | Intégrations |
|-----------|-------------|
| **Énergie** | `MyElectricalData` (Linky HP/HC) · `Ecojoko` (conso réseau temps réel) |
| **Météo & Env.** | `Météo France` · `Blitzortung` (foudre) · `AtmoFrance` (pollution/pollen) · `Vigieau` (restrictions eau) |
| **Hardware** | `Meross LAN` · `Philips HUE` · `IKEA Dirigera` · `NOUS` (prises smart) · `Sonoff SNZB` |
| **UI & Logique** | `Browser Mod` (pop-ups dynamiques) · `Streamline Card` · `HACS` (cartes custom) |
| **Qualité d'air** | `IKEA Vindstyrka` (PM2.5 + VOC index) × 3 pièces |

---

## 📊 Architecture modulaire — Organisation par Pôle

La configuration est **100% éclatée** — zéro fichier monolithique. Chaque fichier a une responsabilité unique, nommée et rangée dans le Pôle fonctionnel correspondant.

```
/config/
├── configuration.yaml          ← point d'entrée (includes, intégrations)
├── automations.yaml            ← toutes les automations
├── scripts.yaml / scenes.yaml  ← scripts et scènes
│
├── sensors/                    ← intégrations Riemann kWh, stats 24h, DUT
│   ├── P0_Energie_total_min_maxi_diag/  ← kWh cumulatif + mini/maxi AVG Genelec
│   ├── P1_clim_chauffage/      ← kWh + DUT chauffage/clim
│   ├── P2_prise/               ← kWh prises, veilles, mini-pc
│   ├── P3_eclairage/           ← kWh ampoules (unité / zone / total)
│   ├── Air_quality/            ← stats PM2.5 + tCOV (mean 24h)
│   └── meteo/                  ← Blitzortung
│
├── templates/                  ← calculs, AVG, UI dashboard, logique
│   ├── P0_Energie_total_diag/  ← coûts HP/HC, ratios, Linky, diag conso
│   ├── P1_clim_chauffage/      ← logique clim, DUT, AVG, totaux, ui_dashboard
│   ├── P2_prise/               ← AVG prises/veilles/mini-pc, all_standby
│   ├── P3_eclairage/           ← puissance (POWER), AVG, ui_dashboard
│   ├── P4_groupe_presence/     ← détection Wi-Fi/réseau, affichage téléphones
│   ├── Air_quality/            ← tCOV en ppb (template)
│   ├── SpeedTest/              ← Download / Upload / Ping
│   ├── Stores/                 ← états volets motorisés (HTML couleur)
│   ├── Inter_BP_Virtuel/       ← interrupteur soufflant SdB (binary_sensor + switch)
│   ├── Mini-PC/                ← 6 capteurs T° CPU/carte mère (command_line)
│   ├── meteo/                  ← alertes, vent, Blitzortung, tendances, cycle solaire
│   └── utilitaires/            ← jour/nuit, MAJ HA, fenêtres ouvertes
│
└── utility_meter/              ← compteurs AMHQ (Annuel/Mensuel/Hebdo/Quotidien)
    ├── P0_Energie_total/       ← index kWh + HP/HC (sous-dossier Genelec_appart/)
    ├── P1_clim_chauffage/      ← 6 équipements × 4 périodes
    ├── P2_prise/               ← prises + veilles + mini-pc
    ├── P3_eclairage/           ← ampoules (unité / zone / total)
    └── meteo/                  ← Blitzortung
```

**Pôles fonctionnels :**

| Pôle | Périmètre |
|------|-----------|
| **P0** | Énergie globale (Linky, Ecojoko, bilans généraux) |
| **P1** | Chauffage & Climatisation (5 pièces) |
| **P2** | Prises connectées (18 appareils + veilles) |
| **P3** | Éclairage (19 ampoules Hue/Sonoff — unité / zone / total) |
| **P4** | Groupe Présence (Wi-Fi, réseau mobile, localisation) |
| **M/A/ST/S/B/MP** | Catégories lettrées : Météo, Air, SpeedTest, Stores, BP Virtuel, Mini-PC |

---

## 🖥️ Dashboard — Matrice 18 Vignettes

Dashboard optimisé tablette + mobile. Structure en 6 lignes × 3 colonnes.

| | C1 | C2 | C3 |
|--|----|----|-----|
| **L1** | Météo | Températures (6 pièces + ext.) | Commandes Clim |
| **L2** | Énergie Générale (Ecojoko/Linky) | Énergie Clim / Radiateur | Énergie Éclairage |
| **L3** | Commandes Éclairage | Commandes Éco (Prises) | Fenêtres + Stores |
| **L4** | Proxmox (PVE) | Mini-PC (NUC) | Mises à jour HA |
| **L5** | Batteries / Piles (34 capteurs) | Batteries Portables (7 appareils) | MariaDB |
| **L6** | Qualité de l'air (PM2.5 + tCOV) | Pollution / Pollen (AtmoFrance) | Vigilance Eau (Vigieau) |

---

## 📁 Documentation (`docs/`) — 18 vignettes documentées

Le répertoire `docs/` est la **source de vérité** du projet. Avant de copier un fichier YAML ou de créer une entité, consultez la doc de la vignette concernée : vous y trouverez la liste exacte des entités utilisées, leur fichier source, et les pièges connus.

```
docs/
├── DEPENDANCES_GLOBALES.md         ← chaîne complète Carte → Template → Sensor → UM → Source
├── WORKFLOW_REBUILD.md             ← procédure de maintenance (6 étapes) + historique des sessions
├── _TEMPLATE_DOC.md                ← modèle de doc vignette
├── IA/IA_CONTEXT_BASE.md           ← copie de CLAUDE.md (référence IA)
├── CONFIG_ROOT/                    ← documentation configuration.yaml
│
├── L1C1_METEO/                     ✅ Vignette + Page Météo + Tuto alertes
├── L1C2_TEMPERATURES/              ✅ Vignette + Page Températures
├── L1C3_CLIM/                      ✅ Vignette + Page Commandes Clim
├── L2C1_ENERGIE/                   ✅ Vignette + Page Énergie (Mensuel + Temps Réel + Couleurs)
├── L2C2_ENERGIE_CLIM/              ✅ Vignette + Page Énergie Clim
├── L2C3_ENERGIE_ECLAIRAGE/         ✅ Vignette + Page Énergie Éclairage + Couleurs
├── L3C1_ECLAIRAGE/                 ✅ Vignette + Page Éclairage
├── L3C2_PRISES/                    ✅ Vignette + Page Prises
├── L3C3_STORES/                    ✅ Vignette + Page Stores
├── L4C1_PROXMOX/                   ⚠️ En cours — vignette créée, page à finaliser
├── L4C2_MINI_PC/                   ✅ Vignette + Page Mini-PC (NUC) + Page RPi4 (transitoire)
├── L4C3_MAJ_HA/                    ✅ Vignette + Page MAJ
├── L5C1_PILES_BATTERIES/           ✅ Vignette + Page Batteries
├── L5C2_BATTERIES_PORTABLES/       ✅ Vignette + Page Portables
├── L5C3_MARIADB/                   ✅ Vignette + Page Système
├── L6C1_AIR_QUALITE/               ✅ Vignette + Page Qualité de l'air
├── L6C2_POLLUTION_POLLEN/          ✅ Vignette + Page Pollution/Pollen
├── L6C3_VIGIEAU/                   ✅ Vignette + Page Vigieau
└── HOME PAGE/                      ✅ Page Home + Vignette Wi-Fi Présence
```

> **18 / 18 vignettes actives** *(L4C1 Proxmox en cours de finalisation)* — dépendances complètes dans `DEPENDANCES_GLOBALES.md`

---

## 👻 Suivi des entités orphelines

Le fichier [`Orphelin/orphelin.yaml`](./Orphelin/orphelin.yaml) (et sa version lisible [`orphelin.md`](./Orphelin/orphelin.md)) inventorie toutes les entités référencées dans le dashboard mais absentes de HA, détectées via l'intégration **Spook**.

Catégories suivies : ⛔ OBSOLÈTE · 🔴 FANTÔME · 🟡 PARTIEL · 🔲 ORPHELIN · 🔵 NON PRIO · ✅ COUVERT

---

## 🏗️ Dossier de travail local (`ReBuild/`)

Le dépôt est maintenu depuis un **dossier de travail local** (`C:\Users\Berry Swann\Documents\HA\ReBuild\`) via Claude (Cowork mode) :

```
ReBuild/
├── CLAUDE.md                        ← directives IA (source de vérité)
├── INDEX_NAVIGATION_FULL.md         ← index 18 vignettes (accordéon, entités, pop-ups)
├── SYNC_REPORT.md                   ← rapport de synchronisation GitHub ↔ local
├── IA/                              ← contextes IA spécialisés (INTEGRATIONS, ARBO, P4, INDEX…)
├── Dashboard/                       ← YAMLs dashboard versionnés (max 3 par vignette)
│   └── Dashboard_COMPLET/           ← exports dashboard complets (conservation illimitée)
├── docs_dashboard/
│   ├── TREE_CORRIGE/                ← fichiers corrigés → à copier dans /config/
│   ├── TREE_ORIGINE/                ← snapshot GitHub de référence (lecture seule)
│   └── docs/                        ← documentation complète (18 vignettes)
├── docs_automations/
│   ├── TREE_CORRIGE/                ← automations cibles → à coller dans HA UI
│   └── TREE_ORIGINE/                ← snapshot automations avant corrections
├── docs_scripts/
│   ├── TREE_CORRIGE/                ← scripts corrigés
│   └── TREE_ORIGINE/
└── Orphelin/                        ← inventaire entités fantômes
```

> Procédure de maintenance détaillée : [`docs/WORKFLOW_REBUILD.md`](./docs/WORKFLOW_REBUILD.md)

---

## 📸 Aperçu

<p align="center">
  <img width="600" height="3520" alt="Dashboard Home Assistant" src="https://github.com/user-attachments/assets/fc33371e-3d93-4102-a357-14aa3a4a8863" />
</p>

---

## 📖 Liens

- [Forum HACF](https://forum.hacf.fr)
- [Documentation Officielle HA](https://www.home-assistant.io/docs/)
- [Ancien dépôt](https://github.com/BerrySwann/home-assistant-config) *(archivé — remplacé par ce re-build)*

---

✨ **Projet vivant — architecture modulaire, documentée, maintenue avec Claude (Anthropic)**
