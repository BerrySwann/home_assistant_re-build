# 🌳 ARBORESCENCES COMPLÈTES & INDEX GITHUB
*Dernière mise à jour : 2026-07-18 (refonte complète - l'ancienne version décrivait l'arbo d'avant la réorg du 07-14 et était tronquée en fin de fichier)*
*Lire ce fichier si : audit fichiers, sync GitHub, recherche d'un fichier prod, vérification arbo locale, URLs raw GitHub.*

---

## ⚠️ RÈGLES DE CASSE - PIÈGE PRINCIPAL

| Contexte | Nom du dossier docs |
|:---------|:--------------------|
| Local ReBuild | `DOCS/` (majuscules) |
| Prod H:\ et GitHub | `Docs/` (mixte) |

> GitHub est **case-sensitive** : tout lien écrit `DOCS/...` vers le repo est **mort**. Toujours `Docs/...` dans les liens GitHub (INDEX_GLOBAL.md, etc.).

---

## 🌳 ARBORESCENCE - LOCAL ReBuild/ (relevé 2026-07-18)

```text
ReBuild/                                (C:\Users\Berry Swann\Documents\ReBuild\)
├── CLAUDE.md                           (source de vérité contexte - sync avec IA_CONTEXT_BASE.md)
├── TODO.txt                            (backlog projet)
├── autounattend_FR.xml · z2m-backup.*.zip   (hors périmètre HA)
├── Analyse énergétique/                (analyse_energetique_appart.md - prompt audit 02/2026)
├── Github/                             (INDEX_GLOBAL.md · README.md - miroirs travail du repo)
├── HTML/                               (exports HTML - ha_erodi_ha_com_*.html)
├── Infra_Proxmox/                      (réseau, certs - + save/)
├── historique/                         (JOURNAL_COMPLET_*.md · histo_YYYY-MM-DD_S*.txt)
└── DOCS/
    ├── 00_IA/                          (IA_CONTEXT_BASE.md · confort_cible_calcul_flow.png)
    │   └── sous_md/                    (7 sous-contextes IA_*.md - ⚠️ prod = "sous_context/")
    ├── 01_docs_config_system/
    │   ├── config_system_MD/           (configuration.md)
    │   └── config_system_YAML/         (→ déployé /homeassistant/ - détail = arbo PROD ci-dessous)
    ├── 02_docs_dashboard/
    │   ├── dashboard_docs_MD/          (DEPENDANCES_GLOBALES.md · L*C*_*/ · INDEX_PAGES.md)
    │   └── dashboard_docs_YAML/        (Dashboard_COMPLET/ · L1C1→L6C3 · PAGE_Home · PAGE_RASPI)
    ├── 03_docs_automations/
    │   ├── docs_automations_MD/        (docs par automation, par catégorie P*/systeme/...)
    │   └── docs_automations_YAML/      (yaml individuels par automation → UI HA)
    ├── 04_docs_scripts/
    │   ├── docs_scripts_SH/            (audit_md5.sh · ha_git_backup.sh)
    │   ├── docs_scripts_SH_MD/         (docs des .sh)
    │   ├── docs_scripts_YAML/          (yaml scripts HA)
    │   └── docs_scripts_YAML_MD/       (docs + INDEX_SCRIPTS.md)
    └── 05_docs_MD_system/              (workflow/ · map_of_content_obsidian/ · matrisse_template_doc/)
```

> ⛔ `TREE_CORRIGE/`, `TREE_ORIGINE/`, `Dashboard/`, `docs_dashboard/`, `docs_automations/`, `docs_scripts/`, `IA/` racine : **supprimés le 2026-07-14** - toute référence à ces chemins est morte.

---

## 🌳 ARBORESCENCE - PROD /homeassistant/ (= H:\ - relevé GitHub 2026-07-18, 495 fichiers)

```text
/homeassistant/
├── configuration.yaml · automations.yaml · scripts.yaml · scenes.yaml
├── input_button.yaml · input_datetime.yaml · input_select.yaml
├── sql.yaml · ip_bans.yaml · .gitignore · .ha_run.lock
├── INDEX_GLOBAL.md                     (index navigable GitHub - 158 Ko)
├── README.md
├── Dashboard_YYYY_MM_DD.yaml           (export dashboard le plus récent - racine)
│
├── .scripts/                           (3)
│   ├── audit_md5.sh                    (FULL · YAML · ATMA - log → .logs/audit_md5.log)
│   ├── ha_git_backup.sh                (backup git → GitHub)
│   └── #MP_01_monitor_temp.sh.#        (⛔ NE PAS TOUCHER - actif Raspberry Pi)
│
├── blueprints/                         (4 - automation/2 · script/1 · template/1, natifs HA)
├── command_line/                       (4)
│   ├── audit/audit_logs.yaml           (sensor.audit_md5_journal)
│   ├── github_maintenance/github_maintenance.yaml
│   ├── ip_externe/ip_externe.yaml      (sensor.ip_externe)
│   └── meteo/carte_meteo_france.yaml
├── groups/                             (3 - GRP_01_batteries_hue · GRP_02_ikea · GRP_03_sonoff)
├── input_booleans/                     (5 - P1/2 · P3/2 · P4/1)
├── input_number/input_number.yaml      (1)
├── notifs/                             (2 .txt - diag_conso_elec · ecart_liky_vs_nodon [File UI])
├── shell_command/                      (2 - Ghithub/backup_github · P4/P4_log_eric_zone)
│
├── sensors/                            (4)
│   ├── Air_quality/                    (1)
│   ├── P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/  (1)
│   ├── P1_clim_chauffage/              (P1_DUT/1 · P1_kWh/1)
│   └── meteo/                          (1)
│
├── templates/                          (36)
│   ├── Air_quality/                    (1 - A_01_AIR_QUALITY)
│   ├── Inter_BP_Virtuel/               (P1/1 · P3/2)
│   ├── P0_Energie_total_diag/          (P0_Diag/3 · P0_Genelec_appart/3 · P0_Linky/1 · P0_total_pour_les_7_postes/1)
│   ├── P1_clim_chauffage/              (P1_01_MASTER/3 · P1_AVG/2 · P1_DUT_TOTAL/1 · P1_TOTAL/1
│   │                                    · P1_kWh_riemann_cuisine/1 · P1_ui_dashboard/1)
│   ├── P2_prise/                       (P2_AVG/3 · P2_I_all_standby_power/1 · P2_eCO_prises/1 · P2_ui_dashboard/1)
│   ├── P3_eclairage/                   (P3_AVG/3 · P3_ENERGIE_TPL/3 · P3_POWER_TPL/1 · ui_dashboard/1)
│   ├── P4_groupe_presence/             (2)
│   ├── Stores/                         (1 - S_01_STORES)
│   ├── meteo/                          (5 - M_01 → M_05)
│   └── utilitaires/                    (3)
│
├── utility_meter/                      (8)
│   ├── P0_Energie_total/Genelec_appart/  (01_UM_AMHQ · 02_UM_genelec_appart_HPHC_AMHQ)
│   ├── P1_clim_chauffage/              (P1_UM_AMHQ)
│   ├── P2_prise/                       (P2_UM_AMHQ_mini_pc · _prises · _veilles)
│   ├── P3_eclairage/                   (P3_UM_AMHQ_1_UNITE - seul actif)
│   └── meteo/                          (M_03_meteo_UM_blitzortung)
│
└── Docs/                               (miroir pushé depuis local DOCS/ - JAMAIS de YAML config ici)
    ├── 00_IA/                          (1 + sous_context/7  ⚠️ à renommer sous_md/)
    ├── 01_docs_config_system/          (config_system_MD/1 · config_system_YAML/81)
    ├── 02_docs_dashboard/              (dashboard_docs_MD/52 · dashboard_docs_YAML/73)
    ├── 03_docs_automations/            (docs_automations_MD/59 · docs_automations_YAML/107)
    ├── 04_docs_scripts/                (SH/2 · SH_MD/2 · YAML/4 · YAML_MD/4)
    └── 05_docs_MD_system/              (2 + workflow/1 · map_of_content_obsidian/1 · matrisse_template_doc/1)
```

**Supprimés de prod (ne jamais recréer)** : `mqtt/` (capteur NodOn chambre, nettoyé 2026-07-18) · `packages/` (cssmeteo, retiré ~07/2026) · `camera.yaml` · `shell_command.yaml` monolithique · `#sensors.yaml` / `#templates.yaml` / `#utility_meter.yaml` désactivés · `templates/Mini-PC/` (capteurs lus à la source).

---

## 🔗 GITHUB - REPO & URLS RAW

- **Repo actif unique** : `BerrySwann/home_assistant_re-build` (ancien `home-assistant-config` supprimé le 2026-04-27)
- **Contenu** : reflet exact de `/homeassistant/` - pushé par `.scripts/ha_git_backup.sh` (boutons page Système L5C3)
- **Point d'entrée navigation** : [INDEX_GLOBAL.md](https://github.com/BerrySwann/home_assistant_re-build/blob/main/INDEX_GLOBAL.md)

**Patterns URLs :**

| Usage | Pattern |
|:------|:--------|
| Fichier (vue web) | `https://github.com/BerrySwann/home_assistant_re-build/blob/main/<chemin>` |
| Fichier (raw) | `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/<chemin>` |
| Arbo complète (API) | `https://api.github.com/repos/BerrySwann/home_assistant_re-build/git/trees/main?recursive=1` |
| Zip complet | `https://github.com/BerrySwann/home_assistant_re-build/archive/refs/heads/main.zip` |

Exemples :
- `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/configuration.yaml`
- `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/meteo/M_01_meteo_alertes_card.yaml`
- `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/Docs/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md`

---

## 🔍 AUDIT & SYNC - RAPPELS

- **Audit MD5** : script unique `audit_md5.sh` (FULL · YAML · ATMA) - boutons dashboard L5C3 - log `/homeassistant/.logs/audit_md5.log`. Commandes détaillées : voir `IA_CMD_TERMINAL_HA.md`.
- **Sens YAML config** : prod → GitHub → local (local converge vers prod).
- **Sens Docs .md** : local `DOCS/` → `H:\Docs\` → GitHub (local gagne en conflit).
- **Après tout changement prod** : déclencher le git backup, sinon GitHub reste en retard (liens INDEX cassés, audits faussés).

## ⚠️ INCOHÉRENCES CONNUES (à régler)

- `H:\Docs\00_IA\sous_context\` vs local `DOCS/00_IA/sous_md/` : renommer côté prod en `sous_md/` (local = vérité docs).
- Sous-contextes `IA_*.md` datés 05/06-2026 : antérieurs à la réorg du 07-14, en cours de refonte (TODO F-5).
