# 🔄 WORKFLOW — ORGANISATION & MAINTENANCE DU DOSSIER REBUILD
*Dernière mise à jour : 2026-06-19*

---

## 📁 STRUCTURE DU DOSSIER REBUILD

```
ReBuild/                        ← C:\Users\Berry Swann\Documents\HA\ReBuild\
├── CLAUDE.md                   ← Instructions IA (contexte projet — source de vérité)
├── README.md / SYNC_REPORT.md / COMMANDES.md
├── secrets.yaml                ← NE JAMAIS synchroniser sur GitHub
├── IA/                         ← Fichiers contexte IA complémentaires à CLAUDE.md
│   ├── IA_ARBO_DETAIL.md       ← Arborescences prod + GitHub complètes, URLs raw
│   ├── IA_CMD_TERMINAL_HA.md   ← Commandes terminal HA (tree prod, audit MD5, git backup)
│   ├── IA_AUTOMATIONS_NOTIFS.md
│   ├── IA_INTEGRATIONS_CARTES.md
│   ├── IA_P4_PRESENCE.md
│   ├── IA_INDEX_NAVIGATION.md
│   ├── IA_INDEX_AUTOMATIONS.md
│
├── Dashboard/                  ← YAML vignettes + pages (18 sous-dossiers + Dashboard_COMPLET/)
│   ├── Dashboard_COMPLET/      ← dashboards complets — conservation illimitée
│   ├── L*C*_NN_NomVignette/    ← 1 sous-dossier par vignette (L1C1→L6C3) — max 3 versions
│   └── PAGE_*/                 ← pages orphelines
│
├── docs_dashboard/             ← tout ce qui concerne la config dashboard HA
│   ├── TREE_CORRIGE/           ← SOURCE DE VÉRITÉ → /homeassistant/ (sensors/ templates/ utility_meter/ command_line/ groups/ input_booleans/ packages/ shell_command/)
│   ├── TREE_ORIGINE/           ← snapshot GitHub avant corrections (référence historique)
│   └── docs/                   ← 18 vignettes documentées + DEPENDANCES_GLOBALES
│
├── docs_automations/           ← TREE_CORRIGE/ TREE_ORIGINE/ docs/
├── docs_scripts/               ← TREE_CORRIGE/.scripts/ docs/
└── historique/                 ← histo_COMPLET_*.txt + histo_YYYY-MM-DD.txt (session courante)
```

**Règle d'or :** `docs_dashboard/TREE_CORRIGE/` est la seule source de vérité à déployer sur HA.
Copier les dossiers concernés directement dans `/homeassistant/`.
⚠️ Chemin réel HA : `/homeassistant/` (et non `/config/` — symlink non suivi par `find`)

---

## 🔁 WORKFLOW COMPLET (6 ÉTAPES)

### ÉTAPE 1 — Vérification GitHub vs Local (Audit MD5)

Objectif : identifier les fichiers nouveaux, modifiés ou absents entre GitHub et `TREE_CORRIGE/`.

**Méthode automatisée (recommandée) :**
```bash
bash /homeassistant/.scripts/audit_md5.sh
cat /homeassistant/.logs/md5_audit_latest.txt
```

**Méthode manuelle (si besoin) :**
- Consulter les URLs dans `IA/IA_ARBO_DETAIL.md` (section INDEX INTÉGRAL GitHub)
- Générer l'arborescence prod via `IA/IA_CMD_TERMINAL_HA.md` (section TREE PROD)
- Comparer prod vs `TREE_CORRIGE/` fichier par fichier
- Documenter les écarts dans `SYNC_REPORT.md`

---

### ÉTAPE 2 — Corrections dans TREE_CORRIGE/

Objectif : appliquer toutes les corrections nécessaires aux fichiers avant déploiement.

**Corrections standard à vérifier :**
- Boîtes ASCII arrondies : top/bottom = largeur du titre (standard 78 chars, sauf exception)
- En-têtes secondaires : `#┌` → `# ┌` (espace obligatoire après `#`)
- Titres normalisés selon la convention `PÔLE X. TYPE : DESCRIPTION`
- Références obsolètes (ex: `P3_01_somme_par_piece` → `P3_POWER_2_TOTAL_MULTI_ZONE`)

**Corrections spécifiques :**
- Si nouveau fichier GitHub → télécharger et placer dans la bonne arborescence
- Si fichier modifié GitHub → remplacer dans `TREE_CORRIGE/` et réappliquer les corrections

---

### ÉTAPE 3 — Audit / Vérification TREE_CORRIGE/

Objectif : garantir 0 problème avant déploiement.

Script de vérification (à lancer depuis le VM) :

```python
import os, re

DEST = "/path/to/TREE_CORRIGE"
issues = []

for root, dirs, fnames in os.walk(DEST):
    for fname in fnames:
        if not fname.endswith(".yaml"):
            continue
        path = os.path.join(root, fname)
        rel = path.replace(DEST + "/", "")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()

        # 1. En-têtes secondaires sans espace
        for i, ln in enumerate(lines):
            if re.match(r'^#[┌└│]', ln):
                issues.append(f"[NO_SPACE] {rel}:L{i+1}")

        # 2. Alignement boîtes ASCII
        for i, ln in enumerate(lines):
            ln_s = ln.rstrip()
            if re.match(r'^# ╭─+╮$', ln_s) and i+2 < len(lines):
                title = lines[i+1].rstrip()
                bottom = lines[i+2].rstrip()
                if re.match(r'^# ╰─+╯$', bottom):
                    if len(ln_s) != len(title) or len(bottom) != len(title):
                        issues.append(f"[BOX_MISMATCH] {rel}:L{i+1}")

        # 3. Références obsolètes (hors annotations_log)
        in_annot = False
        for i, ln in enumerate(lines, 1):
            if "# annotations_log:" in ln:
                in_annot = True
            if not in_annot and "P3_01_somme_par_piece" in ln:
                issues.append(f"[OBSOLETE_REF] {rel}:L{i}")

if not issues:
    print(f"=== TOUT EST PROPRE — 0 problème ===")
else:
    for iss in issues:
        print(f"  {iss}")
```

**Résultat attendu :** `=== TOUT EST PROPRE — 0 problème ===`

---

### ÉTAPE 4 — Mise à jour Dashboard/

Objectif : garder un seul fichier à jour dans `Dashboard/`.

- Si le dashboard principal a changé dans HA : exporter le fichier `.yaml` complet
- Nommer le fichier avec la date : `dashboard_YYYY-MM-DD.yaml`
- Supprimer l'ancienne version (1 seul fichier dans `Dashboard/` à tout moment)
- Mettre à jour la référence dans `CLAUDE.md` (section ARBORESCENCE DOSSIER DE TRAVAIL)

---

### ÉTAPE 5 — Mise à jour SYNC_REPORT.md

Objectif : documenter tous les changements effectués lors de la session.

Structure du rapport à compléter :

```markdown
## Résumé
| Catégorie        | Fichiers |
|------------------|----------|
| utility_meter/   | X        |
| templates/       | X        |
| sensors/         | X        |

## Corrections appliquées (session YYYY-MM-DD)
- [description des corrections]

## Notes
- [fichiers absents sur GitHub, cas particuliers]

## Historique
| Date       | Action                         |
|------------|--------------------------------|
| YYYY-MM-DD | [description]                  |
```

---

### ÉTAPE 6 — Mise à jour CLAUDE.md + fichiers IA/

Objectif : maintenir les fichiers de contexte synchronisés après chaque session.

**6a. Mettre à jour `CLAUDE.md`** (à la racine de ReBuild) :
- Date de dernière mise à jour en haut du fichier
- Arborescences si des fichiers ont été ajoutés/supprimés

**6b. Mettre à jour les fichiers `IA/` concernés** selon les modifications :
- `IA/IA_ARBO_DETAIL.md` → si fichiers ajoutés/supprimés en prod ou TREE_CORRIGE
- `IA/IA_CMD_TERMINAL_HA.md` → si nouvelles commandes terminal
- `IA/IA_INDEX_AUTOMATIONS.md` → si automations ajoutées/supprimées
- `IA/IA_INDEX_NAVIGATION.md` → si vignettes/pages modifiées

**6c. Synchroniser `IA_CONTEXT_BASE.md`** (copie lisible de `CLAUDE.md`) :
- Copier le contenu de `CLAUDE.md` dans `IA/IA_CONTEXT_BASE.md`
- Copier la même version dans `docs_dashboard/docs/IA/IA_CONTEXT_BASE.md`
- ⚠️ Ne jamais modifier `IA_CONTEXT_BASE.md` directement — toujours modifier `CLAUDE.md` d'abord


---

---

## 📝 WORKFLOW CRÉATION / MODIFICATION D'UNE DOC VIGNETTE

Chaque fois qu'une doc `docs/L*` est créée ou modifiée :

1. Utiliser `_TEMPLATE_DOC.md` comme base
2. Remplir la section **ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE** (traçabilité fichier source → entité)
3. **Mettre à jour `docs/DEPENDANCES_GLOBALES.md`** :
   - Compléter la chaîne de dépendances de la vignette concernée
   - Passer le statut de 🔲 à ✅ dans le tableau STATUT
4. Mettre à jour la date en haut de `DEPENDANCES_GLOBALES.md`

---

## ⚠️ RÈGLES PERMANENTES

| Règle | Détail |
|-------|--------|
| `secrets.yaml` | Ne jamais synchroniser sur GitHub — gestion manuelle uniquement |
| `TREE_ORIGINE/` | Ne jamais modifier — snapshot de référence en lecture seule |
| `Dashboard/` | 18 sous-dossiers versionnés — max 3 fichiers par vignette (demander avant de supprimer la v1) |
| `TREE_CORRIGE/` | Seul répertoire à déployer sur `/homeassistant/` |

---

## 📅 HISTORIQUE DES SESSIONS

| Date       | Actions effectuées |
|------------|--------------------|
| 2026-03-15 | Sync initiale GitHub → TREE (151 fichiers détectés) |
| 2026-03-16 | Corrections headers (26 fichiers), ajout P3_POWER, diag_hebdo |
| 2026-03-17 | Réorganisation complète ReBuild (TREE_CORRIGE/ORIGINE/Dashboard/docs) |
| 2026-03-17 (s2) | Ajout `utilitaires/Mise_a_jour_home_assistant.yaml` — fix vignette L4C3 |
| 2026-03-17 (s3) | Création `docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md` — doc complète home page (18 vignettes) |
| 2026-03-18 (s4) | Création `docs/L4C3_MAJ_HA/L4C3_VIGNETTE_MAJ.md` — vignette button-card + page MAJ (2 grilles). Fix bug `margin-left: 250%` documenté. DEPENDANCES_GLOBALES L4C3 🔲→✅ |
| 2026-03-18 (s5) | Création `docs/L2C3_ENERGIE_ECLAIRAGE/PAGE_ENERGIE_ECLAIRAGE.md` — YAML complet page éclairage (5 pièces, tabbed-card JOUR/MOIS/30J, apexcharts). MàJ `L2C3_VIGNETTE_ECLAIRAGE.md` (métadonnées + liens). DEPENDANCES_GLOBALES L2C3 enrichi. |
| 2026-03-22 (s6) | Création `Orphelin/orphelin.yaml` — inventaire entités sans vignette (Pôle 1, Pôle 4 mobiles, Serveur, Réseau). Statuts 🔲/🟡/✅. |
| 2026-03-22 (s7) | Complétion docs existantes — ajout métadonnées et chaînes dépendances manquantes dans DEPENDANCES_GLOBALES. |
| 2026-03-25 (s8) | Création `docs/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md` — vignette Mini PC Intel NUC. Ajout sensors spéciaux command_line thermal zones documentés. |
| 2026-03-25 (s9) | Création `docs/L4C2_MINI_PC/PAGE_RASPI.md` — page transitoire RPi4 (conservée jusqu'à migration). Catégories A/B/C/D. |
| 2026-03-25 (s10) | Ajout UM + AVG prise Mini PC IKEA dans TREE_CORRIGE (`P2_UM_AMHQ_prises.yaml` + `P2_AVG_AMHQ_prises.yaml`). |
| 2026-03-25 (s11) | Clôture documentation L4C2 Mini PC. Création `docs/L4C2_MINI_PC/PAGE_MINI_PC.md` (page définitive Mini PC Intel NUC — 13 blocs, 5 pop-ups). Ajout automation ventilateur RPi dans `PAGE_RASPI.md` (Catégorie D). MàJ `DEPENDANCES_GLOBALES.md` (L4C2 chaîne complète). MàJ `CLAUDE.md` + `IA_CONTEXT_BASE.md` (date 2026-03-25). Création `TODO_2026-03-25.md` (8 tâches classées). Vérif GitHub : 2 nouveaux fichiers détectés (`P2_UM_AMHQ_mini_pc.yaml` + `P2_AVG_AMHQ_mini_pc.yaml`) — Mini PC déployé en prod comme fichiers séparés. ⚠️ TREE_CORRIGE : 2 fichiers présents sur 44 attendus (gap critique à traiter). |
| 2026-03-26 (s12) | Spook — analyse dashboard TABLETTE : **62 entités fantômes détectées**. Mise à jour `Orphelin/orphelin.yaml` avec catégorisation complète (⛔ OBSOLÈTE : gm1901 7 entités + sm_a530f 5 entités / 🔴 FANTÔME : 10 schedule_* P1 + statut_soufflant_sdb + 9 Mini-PC + 3 réseau / 🔵 NON PRIO : tablette + 4 smartphones). Création 10 nouveaux dossiers `docs/` : `L1C3_CLIM/`, `L2C2_ENERGIE_CLIM/`, `L3C1_ECLAIRAGE/`, `L3C2_PRISES/`, `L3C3_STORES/`, `L4C1_FREEBOX/`, `L5C2_BATTERIES_PORTABLES/`, `L6C1_AIR_QUALITE/`, `L6C2_POLLUTION_POLLEN/`, `L6C3_VIGIEAU/` (vignettes + pages). |
| 2026-03-27 (s13) | Création `input_booleans/P1/P1_arret_clim_securises.yaml` (arrêts sécurisés clim Salon/Bureau/Chambre + `inter_soufflant_salle_de_bain`). Création `input_booleans/P4/P4_presence_wifi.yaml` (détection présence Wi-Fi). Création `TABLETTE_card_conso_clim_FIXED.yaml` (button-card conso clim — entités corrigées `_kwh_um` vs anciens `_um`). Confirmation par Gemini : gm1901 + sm_a530f OBSOLÈTES → à supprimer du dashboard TABLETTE. Identification duplicate : `P1_switch_inter_soufflant_sdb.yaml` = doublon de `templates/Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml` → à supprimer. |
| 2026-03-28 (s14) | Vérification synchronisation GitHub ↔ local. Complétion `DEPENDANCES_GLOBALES.md` : **18/18 vignettes ✅** avec chaînes de dépendances complètes. Mise à jour date `DEPENDANCES_GLOBALES.md`. |
| 2026-04-02 (s15) | Analyse énergétique Jan-Mar 2026 (`diag_conso_elec.txt` — 8329 entrées 15min). Résultat : Jan 384 kWh / Fév 339 kWh / Mar ~166 kWh corrigé (anomalie UM reset 18-22/03 — 69.92 kWh était cumul 5 jours, pas 1 jour). Recommandation rideaux occultants : Chambre priorité 1. Comparaison rapport Spook (62 entités) vs `orphelin.yaml` → couverture 100%, statut P1 PARTIEL → ✅ COUVERT (doc `L2C2_VIGNETTE_ENERGIE_CLIM.md` confirmée existante). Création `Orphelin/orphelin.md` (version lisible et structurée par priorité d'action). Mise à jour `CLAUDE.md` arborescence `docs/` (10 dossiers manquants ajoutés, noms corrigés, fichiers fantômes supprimés). Mise à jour date `DEPENDANCES_GLOBALES.md` (2026-04-02). Mise à jour date `WORKFLOW_REBUILD.md`. |
| 2026-04-19→26 (s16-17) | Restructuration majeure TREE_CORRIGE : P3 éclairage refonte complète (`P3_ENERGIE_TLP/` = 76+40+4 sensors, P3_UM réduit à 1 fichier 1_UNITE, `P3_TPL_AMHQ_*.yaml` ×3). P0 Energie : ajout `01_kWh_UM_AMHQ.yaml` (test A/B vs Ecojoko). Suppression ancien repo prod (`home-assistant-config` effacé — `home_assistant_re-build` = prod unique). Ajout `groups/` (GRP_01/02/03 batteries Hue/IKEA/SONOFF). Refonte `command_line/` (ajout `sante_systeme_mini_pc/`). Mise à jour CLAUDE.md globale (date 2026-04-29, arbo prod complète). Sync GitHub ↔ local documentée dans `SYNC_REPORT.md`. |
| 2026-05-01→06 (s18-19) | Archivage Dashboard vignettes L1C1→L5C3 (15 vignettes + pages YAML). Création sous-dossiers `Dashboard/L*C*_NN_*/` avec versioning daté. Docs vignettes complétées. `DEPENDANCES_GLOBALES.md` enrichi (L1C1→L5C3 ✅). Corrections L5C1 (batteries tronquées — TODO #1 en attente). L5C2 (NE2213 Mamour — TODO #2). L5C3 (chip Weekly amber logique — TODO #3). |
| 2026-05-14 (s20) | Archivage L6C1/L6C2/L6C3 (vignettes + pages YAML + docs + DEPENDANCES). **18/18 vignettes archivées ✅**. Ajout TODO #4 (entity-progress-card absent du référentiel). Suppre