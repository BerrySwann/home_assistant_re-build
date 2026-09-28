# 🌳 ARBORESCENCES COMPLÈTES & INDEX GITHUB
*Dernière mise à jour : 2026-09-20 (relevés LOCAL + PROD + GitHub rafraîchis ; suppression `P2_ui_dashboard` prod notée)*
*Lire ce fichier si : audit fichiers, sync GitHub, recherche d'un fichier prod, vérification arbo locale, URLs raw GitHub.*

---

## ⚠️ RÈGLES DE CASSE - PIÈGE PRINCIPAL

| Contexte | Nom du dossier docs |
|:---------|:--------------------|
| Local ReBuild (Windows, insensible à la casse) | `docs/` ou `docs/` - indifférent |
| Prod H:\ (Windows, insensible à la casse) | `docs/` (renommé 2026-07-19, ex `Docs/`) |
| **GitHub (case-sensitive)** | `docs/` (tout minuscule depuis 2026-07-19) |

> ⚠️ **Changement du 2026-07-19** : le dossier était `Docs/` (D majuscule) jusqu'au 07-18. Renommé en `docs/` (tout minuscule) côté H:\, puis pushé sur GitHub qui ne fait plus du tout la distinction historique - **tous les liens doivent utiliser `docs/` minuscule**. Les 385 liens de `INDEX_GLOBAL.md` ont été réécrits en conséquence le 2026-07-19 (247/249 OK, 2 morts = entrée Gardien Éco connue).
> GitHub reste **case-sensitive** : ne jamais écrire `Docs/` ni `docs/` dans un lien vers le repo.

---

## 🌳 ARBORESCENCE - LOCAL ReBuild/ (relevé 2026-09-20)

```text
ReBuild/                                (C:\Users\Berry Swann\Documents\ReBuild\ - relevé 2026-09-20)
├── CLAUDE.md                           (source de vérité contexte - sync avec IA_CONTEXT_BASE.md)
│   · CLAUDE_backup_2026-07-31.md · CLAUDE_backup_2026-08-01.md   (backups)
├── TODO.txt · a mettre en place.txt    (backlog projet)
├── ha-erodi.html · index.html          (maquettes - l'architecture HA est dans docs/00_IA/ha-erodi-architecture.html)
├── presentation_HACF_2026.md/.txt · PROMPT_REPRODUCTION_ha-erodi.md · prompt_site_HA.txt · PROMPT_TEMPLATE_SITE_WEB.md · histo_2026-08-07.txt
├── autounattend_FR.xml · z2m-backup.*.zip   (hors périmètre HA)
├── Github/                             (INDEX_GLOBAL.md · README.md - miroirs travail du repo)
├── HTML/                               (41 fichiers - maquettes/captures)
├── prompt/ · Claude outputs/ · _old_avant_staging/ · energie/   (travaux et conteneurs)
├── Infra_Proxmox/                      (réseau, certs - + save/)
├── scripts/                            (4 - audit_md5_md.sh · audit_md5_yaml.sh · ha_git_backup.sh · hermes_gen_dependances.py)
├── historique/                         (71 - JOURNAL_COMPLET_*.md · histo_YYYY-MM-DD_S*.txt · archives MD5 / P2_ui_dashboard.retire)
└── docs/                               (562 fichiers)
    ├── 00_IA/                          (14 - IA_CONTEXT_BASE.md · ha-erodi-architecture.html · RAPPORT_AUDIT_ENERGETIQUE_*.md ×2 · Grille_Tarif_Bleu_EDF_2026-08-01.csv · confort_cible_calcul_flow.png)
    │   └── sous_context_ia/            (8 sous-contextes IA_*.md)
    ├── 01_docs_config_system/          (104 - config_system_MD · config_system_YAML)
    ├── 02_docs_dashboard/              (207 - dashboard_docs_MD · dashboard_docs_YAML)
    ├── 03_docs_automations/            (212 - docs_automations_MD · docs_automations_YAML)
    ├── 04_docs_scripts/                (16 - SH · SH_MD · YAML · YAML_MD)
    └── 05_docs_MD_system/              (7)
```

> ⛔ `TREE_CORRIGE/`, `TREE_ORIGINE/`, `Dashboard/`, `docs_dashboard/`, `docs_automations/`, `docs_scripts/`, `IA/` racine : **supprimés le 2026-07-14** - toute référence à ces chemins est morte.

---

## 🌳 ARBORESCENCE - PROD /homeassistant/ (= H:\ - relevé SMB 243 le 2026-09-20)

```text
/homeassistant/   (relevé SMB 243 le 2026-09-20 ; = H:\)
│
├── Fichiers racine :
│   configuration.yaml · automations.yaml · scripts.yaml · scenes.yaml · secrets.yaml
│   input_button.yaml · input_datetime.yaml · input_select.yaml · sql.yaml · ip_bans.yaml
│   INDEX_GLOBAL.md · README.md · Dashboard_2026_09_20.yaml (export le plus récent)
│   .HA_VERSION · .gitignore · home-assistant_v2.db · home-assistant.log.fault
│
├── .scripts/                           (5)
│   ├── audit_md5_yaml.sh               (audit YAML)
│   ├── audit_md5_md_yaml.sh            (audit MD + YAML - boutons page L5C3)
│   ├── ha_git_backup.sh                (backup git → GitHub)
│   ├── correct_linky.py                (rattrapage Linky/Nodon - 2026-09-01)
│   └── #MP_01_monitor_temp.sh.#        (⛔ NE PAS TOUCHER - actif Raspberry Pi)
│
├── blueprints/                         (1 - template/homeassistant/inverted_binary_sensor.yaml, natif HA)
├── command_line/                       (6)
│   ├── audit/audit_md5_yaml.yaml · audit/audit_md5_md_yaml.yaml   (sensors journal audit)
│   ├── github_maintenance/github_maintenance.yaml
│   ├── ip_externe/ip_externe.yaml      (sensor.ip_externe_wan)
│   ├── meteo/carte_meteo_france.yaml
│   └── energie/histo_energie.yaml      (histo Linky/Nodon - 2026-09-03)
├── groups/                             (3 - GRP_01_batteries_hue · GRP_02_batteries_ikea · GRP_03_batteries_sonoff)
├── input_booleans/                     (5 - P1/2 · P3/2 · P4/1)
├── input_number/input_number.yaml      (1)
├── notifs/                             (5 .txt - diag_conso_elec · ecart_liky_vs_nodon · ecart_histo · linky_histo · nodon_histo)
├── shell_command/                      (3 - Ghithub/backup_github · P0/P0_correct_linky · P4/P4_log_eric_zone)
├── sensors/                            (5)
│   ├── Air_quality/ (A_01_AIR_QUALITY)
│   ├── P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/ (P0_MINI_MAXI_AVG_Genelec_appart)
│   ├── P1_clim_chauffage/ (P1_DUT/P1_DUT_clim_chauffage)
│   └── meteo/ (M_meteo_sensors_blitzortung)
│
├── templates/                          (46)
│   ├── Air_quality/ (1) · Inter_BP_Virtuel/ (P1/1 · P3/2) · Stores/ (1) · utilitaires/ (3 - jour_nuit · Mise_a_jour_home_assistant · nb_fenetre_ouvert_ferme_autom)
│   ├── meteo/ (5 - M_01 → M_05)
│   ├── P0_Energie_total_diag/ (P0_Diag/3 · P0_Genelec_appart/3 · P0_Linky/1 · P0_total_pour_les_7_postes/1)
│   ├── P1_clim_chauffage/ (P1_01_MASTER/3 · P1_AVG/2 [P1_AVG_AMHQ_TOTAL · P1_AVG_AMHQ_UNITE] · P1_DUT_TOTAL/1 · P1_TOTAL/1 · P1_ui_dashboard/1)
│   ├── P2_prise/ (P2_AVG/3 · P2_congelateur/1 [compresseur actif - ajouté 2026-09-02] · P2_eCO_prises/1 · P2_I_all_standby_power/1)
│   ├── P3_eclairage/ (P3_AVG/3 · P3_ENERGIE_TPL/3 · P3_POWER_TPL/1 · P3_ui_dashboard/1)
│   └── P4_groupe_presence/ (2)
│
├── utility_meter/                      (8)
│   ├── P0_Energie_total/Genelec_appart/  (P0_UM_AMHQ · P0_UM_AMHQ_HPHC)
│   ├── P1_clim_chauffage/ (P1_UM_AMHQ)
│   ├── P2_prise/ (P2_UM_AMHQ_mini_pc · _prises · _veilles)
│   ├── P3_eclairage/ (P3_UM_AMHQ_1_UNITE - seul actif)
│   └── meteo/ (M_03_meteo_UM_blitzortung)
│
├── custom_components/ · themes/ · tts/ · www/ · deps/   (divers, hors périmètre docs HA)
└── docs/                               (477 - miroir pushé depuis local docs/ - JAMAIS de YAML config ici)
    ├── 00_IA/                          (14 - 6 racine + sous_context_ia/8)
    ├── 01_docs_config_system/          (107 - config_system_MD/1 · config_system_YAML/106)
    ├── 02_docs_dashboard/              (177 - dashboard_docs_MD/53 · dashboard_docs_YAML/124)
    ├── 03_docs_automations/            (156 - docs_automations_MD/64 · docs_automations_YAML/92)
    ├── 04_docs_scripts/                (16 - SH/6 · SH_MD/3 · YAML/4 · YAML_MD/3)
    └── 05_docs_MD_system/              (5)
```

**Supprimés de prod (ne jamais recréer)** : `mqtt/` (capteur NodOn chambre, nettoyé 2026-07-18) · `packages/` (cssmeteo, retiré ~07/2026) · `camera.yaml` · `shell_command.yaml` monolithique · `#sensors.yaml` / `#templates.yaml` / `#utility_meter.yaml` désactivés · `templates/Mini-PC/` (capteurs lus à la source) · `templates/P2_prise/P2_ui_dashboard/` (retiré le 2026-09-20).

---

## 🔗 GITHUB - REPO & URLS RAW

- **Repo actif unique** : `BerrySwann/home_assistant_re-build` (ancien `home-assistant-config` supprimé le 2026-04-27)
- **Contenu** : reflet exact de `/homeassistant/` - pushé par `.scripts/ha_git_backup.sh` (boutons page Système L5C3)
- **Point d'entrée navigation** : [INDEX_GLOBAL.md](https://github.com/BerrySwann/home_assistant_re-build/blob/main/INDEX_GLOBAL.md)
- **Dernier relevé arbre (API git trees)** : 2026-09-20 - 600 fichiers ; dernier commit `b6bd2eb5` (2026-09-20 18:10 CEST)

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
- `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/docs/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md`

---

## 🔍 AUDIT & SYNC - RAPPELS

- **Audit MD5** : scripts `.scripts/audit_md5_yaml.sh` (YAML) + `.scripts/audit_md5_md_yaml.sh` (MD + YAML) - sans argument - boutons dashboard L5C3 - log `/homeassistant/.logs/`. Commandes détaillées : voir `IA_CMD_TERMINAL_HA.md`.
- **Sens YAML config** : prod → GitHub → local (local converge vers prod).
- **Sens Docs .md** : local `docs/` → `H:\Docs\` → GitHub (local gagne en conflit).
- **Après tout changement prod** : déclencher le git backup, sinon GitHub reste en retard (liens INDEX cassés, audits faussés).

## ⚠️ INCOHÉRENCES CONNUES (à régler)

- Sous-contextes `IA_*.md` : dossier renommé `sous_context_ia/` le 2026-07-18 (local + prod alignés). Restent à refondre : IA_INDEX_NAVIGATION, IA_INDEX_AUTOMATIONS, IA_INTEGRATIONS_CARTES, IA_P4_PRESENCE (TODO F-5).
