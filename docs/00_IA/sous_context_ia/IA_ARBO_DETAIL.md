# 🌳 ARBORESCENCES COMPLÈTES & INDEX GITHUB
*Dernière mise à jour : 2026-10-10 (relevés LOCAL + PROD + GitHub rafraîchis 2026-10-10 ; liste des fichiers racine corrigée, ajout de Claude md SAVE/ et TODO/, `ha-resync-docs` ; comptages recalculés, la mention "dont N sauvegardes" compte les fichiers .bak)*
*Lire ce fichier si : audit fichiers, sync GitHub, recherche d'un fichier prod, vérification arbo locale, URLs raw GitHub.*

---

## ⚠️ RÈGLES DE CASSE - PIÈGE PRINCIPAL

| Contexte | Nom du dossier docs |
|:---------|:--------------------|
| Local ReBuild (Windows, insensible à la casse) | `docs/` ou `docs/` - indifférent |
| Prod H:\ (Windows, insensible à la casse) | `docs/` (renommé 2026-07-19, ex `Docs/`) |
| **GitHub (case-sensitive)** | `docs/` (tout minuscule depuis 2026-07-19) |

> ⚠️ **Changement du 2026-07-19** : le dossier était `Docs/` (D majuscule) jusqu'au 07-18. Renommé en `docs/` (tout minuscule) côté H:\, puis pushé sur GitHub - **tous les liens doivent utiliser `docs/` minuscule**. Les 385 liens de `INDEX_GLOBAL.md` ont été réécrits le 2026-07-19 ; l'index a été intégralement réécrit le 2026-09-29 (**255 liens, 0 mort**).
> GitHub reste **case-sensitive** : ne jamais écrire `Docs/` ni `docs/` dans un lien vers le repo.

---

## 🌳 ARBORESCENCE - LOCAL ReBuild/ (relevé 2026-10-10)

```text
ReBuild/                                (C:\Users\Berry Swann\Documents\ReBuild\ - relevé 2026-10-10)
├── 10 fichiers racine
│   ha-erodi.html · index.html          (maquettes - l'architecture HA est dans docs/00_IA/ha-erodi-architecture.html)
│   presentation_HACF_2026.md · presentation_HACF_2026.txt
│   PROMPT_REPRODUCTION_ha-erodi.md · prompt_site_HA.txt · PROMPT_TEMPLATE_SITE_WEB.md
│   hermes_cle_ssh.pub                  (cl publique SSH)
│   autounattend_FR.xml · z2m-backup.2.10.1.*.zip   (hors périmètre HA)
├── Claude md SAVE/                     (CLAUDE.md + ses sauvegardes/archives ; aucun CLAUDE.md a la racine)
├── TODO/                               (TODO.md - backlog projet)
├── Github/                             (14 dont 12 sauvegardes - INDEX_GLOBAL.md · README.md, miroirs travail du repo)
├── HTML/                               (41 - maquettes/captures)
├── prompt/ · Claude outputs/ · _old_avant_staging/ · energie/   (travaux et conteneurs)
├── Infra_Proxmox/                      (docs/proxmox|reseau|sonoff/ · scripts/ .sh+.ps1 · certificats/ .crt · journaux/ .log ; save/ vide)
├── MOC/                                (un dossier par MOC : MOC_DASHBOARD/ · MOC_DEPENDANCES/ · MOC_PRESENCE/, chacun avec son .md et ses sauvegardes ; hors périmètre /histo)
├── scripts/                            (5 - audit_md5_md.sh · audit_md5_yaml.sh · check_yaml_forme.py · ha_git_backup.sh · hermes_gen_dependances.py)
├── historique/                         (153 dont 24 sauvegardes - journaux JOURNAL_COMPLET/JOURNAL_FUSIONNE_*.md, histo_YYYY-MM-DD_S*.txt/.md, ARCHIVE_SESSIONS_HA_*.md, archive MD5, histo.md = copie du skill + ses sauvegardes)
└── docs/                               (679 fichiers)
    ├── 00_IA/                          (35 dont 26 sauvegardes - IA_CONTEXT_BASE.md · ha-erodi-architecture.html · RAPPORT_AUDIT_ENERGETIQUE_*.md ×2 · Grille_Tarif_Bleu_EDF_2026-08-01.csv/.pdf · confort_cible_calcul_flow.png)
    │   └── sous_context_ia/            (20 dont 12 sauvegardes - 8 sous-contextes IA_*.md + index arbo)
    ├── 01_docs_config_system/          (113 - config_system_MD/ 2 + config_system_YAML/ 111 fichiers dont 7 sauvegardes, resynchronisé GitHub->local 2026-10-04, SYNC=80 DIFF=0)
    ├── 02_docs_dashboard/              (242 - dashboard_docs_MD 87 · dashboard_docs_YAML 155)
    ├── 03_docs_automations/            (241 dont 9 sauvegardes - docs_automations_MD · docs_automations_YAML)
    ├── 04_docs_scripts/                (24 - SH · SH_MD · YAML · YAML_MD)
    ├── 05_docs_MD_system/              (6 dont 3 sauvegardes)
    └── 05_docs_skills/                 (9 - 9 dossiers skill_<nom>/ contenant la copie .md de chaque SKILL.md du projet ; histo.md vit dans historique/)
```

**Dossiers d'archive** (contenu sorti du flux, gardé pour l'historique) :
`docs/02_docs_dashboard/dashboard_docs_MD/_ARCHIVE/` (créé le 2026-09-28 : `DEPENDANCES_GLOBALES_archive_2026-09-28.md`, l'ancien fichier manuel) · `docs/03_docs_automations/docs_automations_YAML/_old_avant_staging/` · `_old_avant_staging/` à la racine du projet.

> ⛔ `TREE_CORRIGE/`, `TREE_ORIGINE/`, `Dashboard/`, `docs_dashboard/`, `docs_automations/`, `docs_scripts/`, `IA/` racine : **supprimés le 2026-07-14** - toute référence à ces chemins est morte.

> 🗑️ **Purge du 2026-09-29** : config_system_YAML vidé de 104 YAML (risque de divergence). Le dossier P3 boutons salon supprimé + 4 entités purgées HA. Les 2 WORKFLOW_REBUILD.md supprimés. **RATTRAPÉ 2026-10-04** : ha-resync-docs GitHub->local, 85 fichiers resynchronisés (SYNC=80 DIFF=0) - copie locale de nouveau conforme à la prod.

---

## 🌳 ARBORESCENCE - PROD /homeassistant/ (= H:\ - relevé 2026-10-10)

```text
/homeassistant/   (relevé 2026-10-10 ; = H:\)
│
├── Fichiers racine :
│   configuration.yaml · automations.yaml · scripts.yaml · scenes.yaml · secrets.yaml
│   input_button.yaml · input_datetime.yaml · input_select.yaml · sql.yaml · ip_bans.yaml
│   INDEX_GLOBAL.md · README.md · Dashboard_2026_10-04.yaml (export le plus récent)
│   .HA_VERSION · .gitignore · .ha_run.lock · home-assistant_v2.db · home-assistant.log.fault
│   sauvegardes : automations.yaml.bak ×2 · INDEX_GLOBAL.md.bak ×2 · scripts.yaml.bak ×3
│
├── .scripts/                           (6)
│   ├── audit_md5_yaml.sh               (audit YAML)
│   ├── audit_md5_md_yaml.sh            (audit MD + YAML - boutons page L5C3)
│   ├── check_yaml_forme.py             (contrôle de forme des YAML - ajouté 2026-09-29)
│   ├── ha_git_backup.sh                (backup git → GitHub)
│   ├── correct_linky.py                (rattrapage Linky/Nodon - 2026-09-01)
│   └── #MP_01_monitor_temp.sh.#        (résidu d'éditeur, statut à élucider)
│
├── blueprints/                         (1 - template/homeassistant/inverted_binary_sensor.yaml, natif HA)
├── command_line/                       (6)
│   ├── audit/audit_md5_yaml.yaml · audit/audit_md5_md_yaml.yaml   (sensors journal audit)
│   ├── github_maintenance/github_maintenance.yaml
│   ├── ip_externe/ip_externe.yaml      (sensor.ip_externe_wan)
│   ├── meteo/carte_meteo_france.yaml
│   └── energie/histo_energie.yaml      (histo Linky/Nodon - 2026-09-03)
├── groups/                             (3 + 1 sauvegarde - GRP_01_batteries_hue · GRP_02_batteries_ikea · GRP_03_batteries_sonoff)
├── input_booleans/                     (3 - P1/2 · P4/1)   [P3 supprimé le 2026-09-29]
├── input_number/input_number.yaml      (1)
├── notifs/                             (5 .txt - diag_conso_elec · ecart_liky_vs_nodon · ecart_histo · linky_histo · nodon_histo)
├── shell_command/                      (3 - Ghithub/backup_github · P0/P0_correct_linky · P4/P4_log_eric_zone)
├── sensors/                            (4)
│   ├── Air_quality/ (A_01_AIR_QUALITY)
│   ├── P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/ (P0_MINI_MAXI_AVG_Genelec_appart)
│   ├── P1_clim_chauffage/ (P1_DUT/P1_DUT_clim_chauffage)
│   └── meteo/ (M_meteo_sensors_blitzortung)
│
├── templates/                          (52)   [2 supprimés le 2026-09-29 : P3 du salon ; +9 le 2026-10-04 : meteo/ refactorisé (M_02/M_03/M_04/M_05)]
│   ├── Air_quality/ (1) · Inter_BP_Virtuel/P1/ (1 - soufflant SdB) · Stores/ (1) · utilitaires/ (3 - jour_nuit · Mise_a_jour_home_assistant · nb_fenetre_ouvert_ferme_autom)
│   ├── meteo/ (14 - M_01/1 · M_02_meteo_vent/3 · M_03_Meteo_orage_eclaires/5 · M_04_meteo_tendances/2 · M_05_meteo_cycle_solaire/3 ; refactorisé 2026-10-04 : M_02/M_03/M_05 éclatés en fichiers individuels par entité, M_04 splitté temp/humidité)
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
└── docs/                               (569 - miroir pushé depuis local docs/)
    ├── 00_IA/                          (9 - IA_CONTEXT_BASE.md + sous_context_ia/8, aucune sauvegarde .bak sur H:)
    ├── 01_docs_config_system/          (99 - config_system_MD/1 + config_system_YAML/98)
    ├── 02_docs_dashboard/              (204 - dashboard_docs_MD 52 · dashboard_docs_YAML 151)
    ├── 03_docs_automations/            (224 - docs_automations_MD · docs_automations_YAML)
    ├── 04_docs_scripts/                (20 - SH/6 · SH_MD/3 · YAML/8 · YAML_MD/3)
    ├── 05_docs_MD_system/              (4 - ENTITES_INDEX.md · RAPPORT_TRI_ENTITES_2026-09-20.md · map_of_content_obsidian/ vide · matrisse_template_doc/)
    └── 05_docs_skills/                 (9 - 9 dossiers skill_<nom>/ copies des SKILL.md, poussés depuis local docs/05_docs_skills/)
```

**Supprimés de prod (ne jamais recréer)** : `mqtt/` (capteur NodOn chambre, nettoyé 2026-07-18) · `packages/` (cssmeteo, retiré ~07/2026) · `camera.yaml` · `shell_command.yaml` monolithique · `#sensors.yaml` / `#templates.yaml` / `#utility_meter.yaml` désactivés · `templates/Mini-PC/` (capteurs lus à la source) · `templates/P2_prise/P2_ui_dashboard/` (retiré le 2026-09-20) · `input_booleans/P3/` + `templates/Inter_BP_Virtuel/P3/` (boutons virtuels du salon, retirés le 2026-09-29).

---

## 🔗 GITHUB - REPO & URLS RAW

- **Repo actif unique** : `BerrySwann/home_assistant_re-build` (ancien `home-assistant-config` supprimé le 2026-04-27)
- **Contenu** : reflet exact de `/homeassistant/` - pushé par `.scripts/ha_git_backup.sh` (boutons page Système L5C3)
- **Point d'entrée navigation** : [INDEX_GLOBAL.md](https://github.com/BerrySwann/home_assistant_re-build/blob/main/INDEX_GLOBAL.md)
- **Dernier relevé arbre (API git trees)** : 2026-10-10 - **1021 objets (fichiers + dossiers)** ; dernier commit `8f085d03` (2026-10-10 12:10 CEST, HAOS auto-backup: 2026-10-10 12:10:00 CEST, HA 2026.10.0)
- Répartition : `docs/` 731 · `templates/` 43 · `utility_meter/` 8 · `input_booleans/` 6 · `sensors/` 4

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
- `https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/docs/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES_HERMES_V1.md`

---

## 🔍 AUDIT & SYNC - RAPPELS

- **Audit MD5** : scripts `.scripts/audit_md5_yaml.sh` (YAML) + `.scripts/audit_md5_md_yaml.sh` (MD + YAML) - sans argument - boutons dashboard L5C3 - log `/homeassistant/.logs/`. Commandes détaillées : voir `IA_CMD_TERMINAL_HA.md`.
- **Triangulation (trigul)** : `docs/04_docs_scripts/docs_scripts_SH/hermes_audit_md5_trigul_3md.sh` - compare chaque `.md` sur les 3 niveaux (local, prod, dépôt). Dernier passage 2026-09-29 : 145 fichiers, 145 synchronisés, 0 écart.
- **Sens YAML config** : prod → GitHub → local (local converge vers prod).
- **Sens Docs .md** : local `docs/` → `H:\docs\` → GitHub (local gagne en conflit).
- **Après tout changement prod** : déclencher le git backup, sinon GitHub reste en retard (liens INDEX cassés, audits faussés).

## ⚠️ INCOHÉRENCES CONNUES (à régler)

- Sous-contextes `IA_*.md` : dossier renommé `sous_context_ia/` le 2026-07-18 (local + prod alignés). Restent à refondre : IA_INDEX_NAVIGATION, IA_INDEX_AUTOMATIONS, IA_INTEGRATIONS_CARTES, IA_P4_PRESENCE (TODO F-5).
- `INDEX_GLOBAL.md` : 26 entités citées n'existent plus en base (relevé 2026-09-29), à retirer ou à requalifier.
- `hermes_gen_dependances.py` : écrit dans `%LOCALAPPDATA%\Temp` et lit `docs/01_docs_config_system/config_system_YAML`, vidé le 2026-09-29 - **à repointer sur la prod ou le dépôt avant toute régénération**.
