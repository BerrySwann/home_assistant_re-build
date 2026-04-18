# 🔄 WORKFLOW — ORGANISATION & MAINTENANCE DU DOSSIER REBUILD
*Dernière mise à jour : 2026-04-02*

---

## 📁 STRUCTURE DU DOSSIER REBUILD

```
ReBuild/
├── CLAUDE.md                   ← Instructions IA (contexte projet)
├── SYNC_REPORT.md              ← Rapport de synchronisation
├── secrets.yaml                ← NE JAMAIS synchroniser sur GitHub
├── Dashboard/                  ← Dernier dashboard complet (1 fichier à jour)
├── TREE_CORRIGE/               ← Fichiers corrigés → copier dans /config/
│   ├── sensors/
│   ├── templates/
│   └── utility_meter/
├── TREE_ORIGINE/               ← Snapshot GitHub de référence (avant corrections)
└── docs/                       ← Documentation (vignettes, guides, workflow)
    └── IA/
        └── IA_CONTEXT_BASE.md  ← Copie synchronisée de CLAUDE.md
```

**Règle d'or :** `TREE_CORRIGE/` est la seule source de vérité à déployer sur HA.
Copier les 3 sous-dossiers (`sensors/`, `templates/`, `utility_meter/`) directement dans `/config/`.

---

## 🔁 WORKFLOW COMPLET (6 ÉTAPES)

### ÉTAPE 1 — Vérification GitHub vs Local

Objectif : identifier les fichiers nouveaux, modifiés ou absents entre GitHub et `TREE_CORRIGE/`.

- Consulter l'index des URLs dans `CLAUDE.md` (section INDEX INTÉGRAL)
- Pour chaque fichier GitHub : comparer avec `TREE_CORRIGE/` (date, contenu)
- Identifier les **fichiers absents sur GitHub** (ex: `Ecojoko_mini_maxi_avg_1h.yaml` — copie locale uniquement)
- Identifier les **nouveaux fichiers GitHub** absents en local (ex: `diag_conso_hebdomadaire_en_cours.yaml`)
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

### ÉTAPE 6 — Mise à jour CLAUDE.md + copie IA_CONTEXT_BASE.md

Objectif : maintenir les deux fichiers de contexte synchronisés.

**6a. Mettre à jour `CLAUDE.md`** (à la racine de ReBuild) :
- Arborescences (ReBuild + `/config/`) si des fichiers ont été ajoutés/supprimés
- Index GitHub (section INDEX INTÉGRAL) si de nouvelles URLs sont disponibles
- Date de dernière mise à jour en haut du fichier

**6b. Copier CLAUDE.md → `docs/IA/IA_CONTEXT_BASE.md`** :

```bash
cp ReBuild/CLAUDE.md ReBuild/docs/IA/IA_CONTEXT_BASE.md
```

> `IA_CONTEXT_BASE.md` est la copie de référence de `CLAUDE.md` accessible depuis le dossier `docs/`.
> Ces deux fichiers doivent toujours être identiques après chaque session.

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
| `Dashboard/` | 1 seul fichier à la fois (le plus récent) |
| `TREE_CORRIGE/` | Seul répertoire à déployer sur `/config/` |
| `IA_CONTEXT_BASE.md` | Toujours = copie de `CLAUDE.md` (étape 6 obligatoire) |

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


<!-- obsidian-wikilinks -->
---
*Liens : [[DEPENDANCES_GLOBALES]]*
