# 🏠 Home Assistant — Re-Build (Berry Swann)

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2026.x-blue?logo=home-assistant&logoColor=white)](https://www.home-assistant.io/)
[![GitHub last commit](https://img.shields.io/github/last-commit/BerrySwann/home_assistant_re-build)](https://github.com/BerrySwann/home_assistant_re-build)
[![Expert HA](https://img.shields.io/badge/Expert-HAOS_x86--64-success)](#)
[![Powered by Claude IA](https://img.shields.io/badge/AI_Partner-Claude_Sonnet-blueviolet)](#)

Ce dépôt est la **refonte complète et modulaire** de la configuration Home Assistant OS (HAOS) tournant sur un **mini-PC x86-64 (Generic image)**. Il remplace l'ancien dépôt `home-assistant-config` avec une architecture repensée : 1 fonction = 1 fichier YAML, organisation par Pôle fonctionnel, documentation exhaustive par vignette de dashboard.

---

## 🧠 Méthodologie & IA Thought Partner

La configuration est régie par deux fichiers maîtres :

- 👉 **[`CLAUDE.md`](./CLAUDE.md)** — directives IA actives (nomenclature, hiérarchie visuelle, règles de codage, arborescences)
- 👉 **[`docs/IA/IA_CONTEXT_BASE.md`](./docs/IA/IA_CONTEXT_BASE.md)** — copie synchronisée de `CLAUDE.md` (accessible depuis `docs/`)

Développée en collaboration avec **Claude (Anthropic)** pour garantir :

- **Architecture modulaire stricte** : 1 fonction = 1 fichier `.yaml`, 0 approche monolithique
- **Standardisation visuelle** : Boîtes ASCII arrondies (78 car.) / carrées (37 car.) / tertiaires `# --- slug ---`
- **Qualité du code** : Zéro `id:` global dans les automatisations, `unique_id` rigoureuse, annotations `# "[L...] modif"` sur chaque ligne modifiée
- **Traçabilité** : Inventaire complet des entités fantômes (`Orphelin/orphelin.yaml`), chaînes de dépendances documentées par vignette (`docs/DEPENDANCES_GLOBALES.md`)

---

## ⚙️ Système & Matériel

| Composant | Détail |
|-----------|--------|
| **OS** | Home Assistant OS (HAOS) — image Generic x86-64 |
| **Matériel** | Mini-PC Intel NUC — SSD SATA 512 Go / RAM 16 Go |
| **Zigbee** | Sonoff EFR32MG21 (USB + rallonge anti-interférence) |
| **Accès** | Samba Share, Studio Code Server, SSH, Cloudflared |

### 📦 Add-ons principaux

Zigbee2MQTT · MariaDB · Cloudflared · AdGuard Home · Studio Code Server · Samba Share · phpMyAdmin · Glances · Spook

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
│   ├── P0_Energie_total_diag/  ← Ecojoko mini/maxi
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
    ├── P0_Energie_total/       ← coûts + live Ecojoko
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
| **L4** | Freebox Pop | Mini-PC (NUC) | Mises à jour HA |
| **L5** | Batteries / Piles (34 capteurs) | Batteries Portables (7 appareils) | MariaDB |
| **L6** | Qualité de l'air (PM2.5 + tCOV) | Pollution / Pollen (AtmoFrance) | Vigilance Eau (Vigieau) |

---

## 📁 Documentation (`docs/`)

Chaque vignette du dashboard possède sa propre documentation dans `docs/`. Le répertoire est la **source de vérité** pour comprendre quelles entités alimentent quelles cartes.

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
├── L4C1_FREEBOX/                   ✅ Vignette + Page Freebox
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

> **18 / 18 vignettes documentées** — dépendances complètes dans `DEPENDANCES_GLOBALES.md`

---

## 👻 Suivi des entités orphelines

Le fichier [`Orphelin/orphelin.yaml`](./Orphelin/orphelin.yaml) (et sa version lisible [`orphelin.md`](./Orphelin/orphelin.md)) inventorie toutes les entités référencées dans le dashboard mais absentes de HA, détectées via l'intégration **Spook**.

Catégories suivies : ⛔ OBSOLÈTE · 🔴 FANTÔME · 🟡 PARTIEL · 🔲 ORPHELIN · 🔵 NON PRIO · ✅ COUVERT

---

## 🏗️ Dossier de travail local (`ReBuild/`)

Le dépôt est maintenu depuis un **dossier de travail local** (`C:\Users\Berry Swann\Documents\HA\ReBuild\`) via Claude (Cowork mode) :

```
ReBuild/
├── CLAUDE.md               ← directives IA (source de vérité)
├── SYNC_REPORT.md          ← rapport de synchronisation GitHub ↔ local
├── Dashboard/              ← dernier dashboard exporté (1 fichier versionné)
├── TREE_CORRIGE/           ← fichiers corrigés → à copier dans /config/
├── TREE_ORIGINE/           ← snapshot GitHub de référence (lecture seule)
├── Orphelin/               ← inventaire entités fantômes
└── docs/                   ← documentation complète (18 vignettes)
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
