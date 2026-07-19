> ⚠️ **SYNC** : Ce fichier est une copie lisible de `CLAUDE.md` (racine ReBuild).  
> Mettre à jour en même temps que `CLAUDE.md` à chaque session.

---

> **REGLE ABSOLUE :** Tu devras être honnete, ne pas mentir, ne pas tricher, être très attentif, et être 100% objectif et que tu aies l'interdiction de me flater pour me flater ou de me donner une réponse pour me faire plaisire, ou pour me donner une réponse quoi qu'il arrive. Et que si une de mes répose, une de mes solution ou une idées de "codage" (yaml) ou autres, que je pourrais avoir ne te semble pas bonne, il est impératif que tu me le fasse s'avoir sans aller systématiquement dans mon sens.
> Si une de mes demandes ou propositions est ambiguë, floue, incompréhensible, contradictoire ou incomplète, tu devras me poser des questions. Et là aussi, interdiction de valider une interprétation au hasard pour me faire plaisir, ou me flater.

> **REGLE ABSOLUE — STYLE :** Ne jamais utiliser de symboles qui trahissent l'écriture d'un LLM et qui n'existent pas sur un clavier standard. Interdit : `—` (em dash), `…` (ellipse typographique), `«»` (guillemets typographiques), `·` (point médian), et tout autre caractère spécial inaccessible sans Alt+code. Utiliser à la place : `-`, `...`, `"`, `-` etc.

# 🧠 BASE DE CONTEXTE EXPERT HOME ASSISTANT
*Dernière mise à jour : 2026-07-18*

---

## 📚 FICHIERS DE RÉFÉRENCE — LIRE À LA DEMANDE

> ⚠️ Ne PAS lire ces fichiers par défaut — uniquement si la tâche le nécessite.

| Fichier | Lire si… |
|:--------|:---------|
| `DOCS/00_IA/sous_context_ia/IA_INTEGRATIONS_CARTES.md` | YAML dashboard à valider, `type: custom:*` inconnu, intégration manquante, palette couleurs |
| `DOCS/00_IA/sous_context_ia/IA_AUTOMATIONS_NOTIFS.md` | Création/modif automation, écriture message `notify`, script HA |
| `DOCS/00_IA/sous_context_ia/IA_P4_PRESENCE.md` | `sensor.presence`, format notif avec présence, logique groupe WiFi |
| `DOCS/00_IA/sous_context_ia/IA_ARBO_DETAIL.md` | Audit fichiers, sync GitHub, arborescence prod complète, URLs raw GitHub |
| `DOCS/00_IA/sous_context_ia/IA_INDEX_NAVIGATION.md` | Régénération de `INDEX_NAVIGATION_FULL.md`, ajout vignette/page à l'index, mapping entités → fichiers sources, structure accordéon GitHub |
| `DOCS/00_IA/sous_context_ia/IA_INDEX_AUTOMATIONS.md` | Régénération de `INDEX_AUTOMATIONS.md`, ajout/suppression automation, mapping alias → DOCS/03 → docs, anomalies connues |
| `DOCS/00_IA/sous_context_ia/IA_CMD_TERMINAL_HA.md` | Commande tree prod, audit MD5, git backup, chemins `/homeassistant/`, logs HA |

---

# 🛡️ PROTOCOLES

## 🔎 PROTOCOLE DÉBUT DE SESSION (OBLIGATOIRE)

**À chaque ouverture de session, poser cette question AVANT tout travail :**

> "As-tu fait des modifications depuis la dernière session (avec un autre outil, Deepseek, etc.) ?"

| Réponse | Action |
|:--------|:-------|
| **Oui** (peu importe quoi) | Lancer `bash /homeassistant/.scripts/audit_md5.sh` → lire `/homeassistant/.logs/md5_audit_latest.txt` |
| **Non** | Continuer directement |

**Script actif** (sur HA : `/homeassistant/.scripts/`) :
- `audit_md5.sh` — 3 passes (tree local → MD5 prod → MD5 GitHub), sans argument, périmètre YAML complet + .sh + fichiers racine

**Logs** : `/homeassistant/.logs/md5_audit_YYYY-MM-DD.txt` + copie `md5_audit_latest.txt`
> ⛔ Anciens boutons/modes FULL · YAML · ATMA, scripts `audit_yaml/atma/full.sh` et logs `audit_*.log` : **supprimés** - ne plus référencer (vérifié prod 2026-07-18).

---

## Cohérence Documentaire (anti-oubli)
- À chaque modif YAML dans `DOCS/01_docs_config_system/config_system_YAML/` → vérifier impact vignette (`DOCS/02_docs_dashboard/dashboard_docs_MD/L*`) + chaîne dépendances.
- Si rupture cohérence → proposer update `DOCS/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md` ou `/sync_index`.
- Tâche non terminée si code OK mais doc dépendances obsolète.

## Économie de Tokens
- Pas de longs discours d'intro/conclusion. Blocs ciblés uniquement.
- Log de modif : `# annotations_log:` uniquement. Référence directe par ID matrice (L1C1, P2…).
- Ne jamais répéter le code YAML déjà validé.

## Slash Commands
- `/fix_file` → analyse erreur HA et retourne bloc YAML corrigé uniquement.
- `/sync_index` → met à jour `DEPENDANCES_GLOBALES.md` après validation YAML.
- `/status` → résumé 3 points avancement du projet.
- `/histo` → journal de bord compact, sauvegarde dans `historique/`.
- `/ha_new_yaml` → génère un squelette YAML conforme (bordures ASCII, headers, slug, name/unique_id).
- `/ha_push_yaml` → pousse un fichier YAML de `DOCS/01_docs_config_system/config_system_YAML/` vers prod `H:\`.
- `/ha_push_docs` → synchronise les docs locales `DOCS/` vers `H:\Docs\`.
- `/ha_resync_tree` → resynchronise `DOCS/01_docs_config_system/config_system_YAML/` depuis GitHub (audit MD5).

---

# CONVENTION "FILE NOTIFY" (BREAKING CHANGE 2026)
- Plateforme `notify.file` interdite en YAML.
- Passer par l'UI : Paramètres > Appareils > Ajouter Intégration > File.
- Nom service généré : `notify.file_diag_log_file`.

# CONVENTION POWERCALC — PÉRIMÈTRE STRICT
- PowerCalc **uniquement P3 (éclairage)** : ampoules sans monitoring natif (Hue).
- Exception : `relais_lumiere_sdb_sonoff` (ZBMINIR2) → lampe LED 10W fixe.
- ⛔ **INTERDIT P2** : toutes prises NOUS/IKEA ont monitoring natif Z2M.
- Entités `prise_*_device_power` supprimées — ne jamais recréer.

---

## ⚠️ SOURCES DE VÉRITÉ

> ⚠️ Deux cascades distinctes selon le type de fichier.

### 🔧 YAML (config HA) — cascade PROD → LOCAL

| Priorité | Source | Rôle |
|:---------|:-------|:-----|
| **1** | **Home Assistant (live)** | Prod = référence absolue |
| **2** | **GitHub `home_assistant_re-build`** | Reflet prod — backup git auto depuis HA |
| **3** | **Local `ReBuild/`** | Poste de travail — corrections/modifications YAML |

Sens : **prod → GitHub → local**. Le local doit converger vers prod. Une fois les corrections terminées dans `DOCS/01_docs_config_system/config_system_YAML/`, l'état local doit être équivalent à prod (validé par audit MD5).

### 📄 DOCS (.md) — LOCAL = source de vérité

| Priorité | Source | Rôle |
|:---------|:-------|:-----|
| **1** | **Local `ReBuild/DOCS/`** | Source de vérité absolue — authoring et modifications ici |
| **2** | **`H:\Docs\`** | Copie pushée depuis local — ne jamais modifier directement |
| **3** | **GitHub `home_assistant_re-build`** | Backup via git auto depuis HA |

Sens : **local → H:\Docs\ → GitHub**. En cas de conflit, local l'emporte toujours.
`H:\Docs\` ne contient QUE des .md, histo et yaml Dashboard — **jamais de YAML config HA**.

> Ancien repo `home-assistant-config` **supprimé définitivement** (2026-04-27). Seul `home_assistant_re-build` est actif.

### Règles fondamentales
- Répertoires préfixés `P*_` selon le Pôle.
- `DOCS/01_docs_config_system/config_system_YAML/` = YAML config HA (état cible → /homeassistant/) — audité 1×/semaine.
- `DOCS/03_docs_automations/docs_automations_YAML/` = automations individuelles (référence locale).
- `DOCS/02_docs_dashboard/dashboard_docs_YAML/` = vignettes/pages dashboard.
- ⛔ `TREE_CORRIGE/` et `TREE_ORIGINE/` **n'existent plus** — tout est sous `DOCS/`.
- Fichiers absents de `DOCS/01` mais présents GitHub = à supprimer en prod.
- Automations : jamais modifier `automations.yaml` direct → passer par UI HA + `DOCS/03_docs_automations/docs_automations_YAML/`.

---

## 🔍 PROTOCOLE AUDIT MD5 — GITHUB vs LOCAL

> 1×/semaine minimum, avant toute session majeure.

```bash
wget -q "https://github.com/BerrySwann/home_assistant_re-build/archive/refs/heads/main.zip" -O /tmp/repo.zip
unzip -q /tmp/repo.zip -d /tmp/
cd /tmp/home_assistant_re-build-main
find . -type f -name "*.yaml" -print0 | sort -z | xargs -0 md5sum | sed 's|\./||' > /tmp/github_md5.txt
```

| Cas | Action |
|:----|:-------|
| LOCAL absent de GitHub | → push manquant depuis HA |
| GitHub absent du LOCAL | → ancienne version → supprimer GitHub si plus récente en local |
| **MD5 différent (même nom)** | → **⚠️ Conflit — HA = vérité** |
| MD5 identique | → ✅ Synchronisé |

### Périmètre de comparaison

| Priorité | Périmètre | Raison |
|:---------|:----------|:-------|
| **🔴 CRITIQUE** | `DOCS/01_docs_config_system/config_system_YAML/` (sensors/, templates/, utility_meter/, command_line/) | Fichiers déployés dans `/homeassistant/` — un écart peut casser HA |
| **🔴 CRITIQUE** | `automations.yaml` GitHub vs `DOCS/03_docs_automations/docs_automations_YAML/` | Détecter ajouts/suppressions/renommages depuis HA |
| **🟡 SECONDAIRE** | `DOCS/02_docs_dashboard/dashboard_docs_YAML/` vs `H:\Docs\` | UI seulement — ne casse pas HA |

### Audit automations (MD5 + diff alias)
```bash
# Compter et lister les alias top-level dans automations.yaml GitHub
grep "^  alias:" /tmp/home_assistant_re-build-main/automations.yaml | sed 's/  alias: //' | sort > /tmp/github_aliases.txt

# Compter les fichiers automations locaux (hors old/)
find DOCS/03_docs_automations/docs_automations_YAML -name "*.yaml" -not -path "*/old/*" -not -path "*/_old*" | sort > /tmp/local_autom_files.txt

# Comparer les alias avec les noms de fichiers → détecter les manquants
wc -l /tmp/github_aliases.txt /tmp/local_autom_files.txt
```

**Dashboard complet** : vérifier age avant comparaison (`DOCS/02_docs_dashboard/dashboard_docs_YAML/Dashboard_COMPLET/Dashboard_YYYY_MM_DD.yaml` ≤ 2 jours).

---

## 📋 RÈGLES FICHIERS YAML — CRITÈRES DE CONFORMITÉ

> S'appliquent aux fichiers `.yaml` modulaires (sensors/, templates/, utility_meter/, command_line/). Jamais pour les automations.

### 1. BORDURE ASCII
- **Titre principal** — coins arrondis `╭─╮/╰─╯` — largeur 78 car. — texte MAJUSCULES.
  - Si >74 car. : élargir la boîte. Ne jamais supprimer les références techniques du titre.
- **Titre secondaire** — coins carrés `┌─┐/└─┘` — largeur 37 car. — texte MAJUSCULES, numérotation 1-9.

### 2. HEADERS EN-TÊTE OBLIGATOIRE (juste sous la boîte ASCII)
```yaml
# ## 📝 DESCRIPTION :
# ## 🧮 CALCUL & SOURCES :
# ## 🔗 CHAÎNE DE DÉPENDANCES :   ← tableau MATÉRIEL / CAPTEUR BRUT / CE FICHIER / AVAL
# ## ⚠️ IMPORTANT (PIÈGES) :
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
```

**Tableau chaîne de dépendances :**
```yaml
# | MATÉRIEL | CAPTEUR BRUT (source) | CE FICHIER (unique_id) | AVAL |
```
- MATÉRIEL = device physique ou intégration HA. Si source calculée → `[calculé]`.
- AVAL = fichier(s) consommateurs + vignette (ex: `P1_UM_AMHQ.yaml → L2C2`).

### 3. SLUG TERTIAIRE
- Format : `# --- unique_id_exact ---` — juste au-dessus de chaque bloc d'entité.
- Utility_meter : un slug par entrée (annuel/mensuel/hebdo/quotidien).

### 4. NAME
- `name: "Préfixe Nom Lisible Période"` — majuscules initiales — préfixe pôle obligatoire.

### 5. UNIQUE_ID
- `unique_id: prefixe_nom_lisible_periode` — minuscules, underscores.
- Doit décrire la même chose que le `name` (cohérence croisée).

---

## 📏 RÈGLES DE STRUCTURATION GÉNÉRALE

- **Règle d'or** : jamais mélanger les Pôles au sein d'une même pièce.
- **Ordre des Pôles** : 0 Énergie Globale · 1 Chauffage & Clim · 2 Prises · 3 Éclairage · 4 Présence.
- **Ordre pièces** : 1 Entrée · 2 Cellier · 3 Toilette · 4 Salon · 5 Cuisine · 6 Couloir · 7 Bureau · 8 SDB · 9 Chambre.
- **Hors-pièces** : préfixes `M_` Météo · `A_` Air quality · `S_` Stores · `B_` BP virtuel · `MP_` Mini-PC.
- **Architecture modulaire** : 1 fonction = 1 fichier YAML. Approche monolithique interdite.
- **Nommage fichiers** : préfixe Pôle (`P2_…`, `M_…`) + type (`UM`, `AVG`, `kWh`) + `AMHQ` si multi-cycles.
- **`ui_dashboard/`** : réservé aux templates d'affichage uniquement (texte, couleurs, icônes). Jamais de calculs kWh/W/DUT.

---

## 🛠️ RÈGLE DOCS VIGNETTES — DÉPENDANCES OBLIGATOIRES

À chaque création/modif d'une doc vignette (`DOCS/02_docs_dashboard/dashboard_docs_MD/L*`) :
1. Remplir **ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE** dans la doc.
2. Mettre à jour `DOCS/02_docs_dashboard/dashboard_docs_MD/DEPENDANCES_GLOBALES.md` (🔲 → ✅).
3. Mettre à jour la date en haut de `DEPENDANCES_GLOBALES.md`.

---

## 📋 RÈGLE DASHBOARD YAML — VERSIONING

> Tous les yaml dashboard sont dans `DOCS/02_docs_dashboard/dashboard_docs_YAML/`

| Type | Format |
|:-----|:-------|
| Dashboard complet | `Dashboard_COMPLET/Dashboard_YYYY_MM_DD.yaml` (conservation illimitée) |
| Vignette | `L*C*_*/vignette_[id]_YYYY-MM-DD.yaml` |
| Page | `L*C*_*/page_[id]_YYYY-MM-DD.yaml` |
| Carte isolée | `L*C*_*/card_[nom]_YYYY-MM-DD.yaml` |

- Max **3 versions** par sous-dossier vignette/page. Demander autorisation avant suppression de la plus ancienne.

---

## ⚙️ SYSTÈME & MATÉRIEL

| Composant | Détail |
|:----------|:-------|
| **OS** | HAOS — VM Proxmox VE 7.0.0-3 |
| **Matériel** | Mini-PC Intel NUC — SSD 512 Go / RAM 16 Go |
| **Zigbee** | Sonoff EFR32MG21 V2 (reçue 22/05/2026) |
| **LXC 200** | Zigbee2MQTT + Mosquitto (10.32.154.244) |
| **LXC 201** | MariaDB (10.32.154.242) |
| **LXC 202** | MyElectricalData (10.32.154.245) |
| **Add-ons** | Cloudflared · Tailscale · Studio Code Server |
| **Accès** | Samba Share · SSH · Cloudflared · Tailscale |

**Intégrations (compact)** : MyElectricalData · Météo France · Blitzortung · AtmoFrance · Vigieau · Meross LAN · Philips HUE · Z2M · Browser Mod · Streamline Card · HACS
→ Détail complet : `DOCS/00_IA/sous_context_ia/IA_INTEGRATIONS_CARTES.md`

---

## 🔌 ÉQUIPEMENTS PAR PÔLE

### P0 — Énergie Globale : Linky (MyElectricalData J-1 HP/HC), Nodon SEM-4-1-00 (pince Z2M — temps réel).
- Entités Nodon : `sensor.general_electric_appart_energy` (kWh) · `sensor.general_electric_appart_power` (W)
- Source UM P0 : `sensor.general_electric_appart_energy` (Nodon direct — Linky = 24h délai)
### P1 — Chauffage / Clim
- 4 SALON : clim_salon_entree · 5 CUISINE : radiateur_cuisine · 7 BUREAU : clim_bureau
- 8 SDB : soufflant_sdb, seche_serv_sdb · 9 CHAMBRE : clim_chambre

### P2 — Prises
- 1 ENTRÉE : box_internet_entree, horloge_entree
- 4 SALON : pc_s_gege_salon, salon_chargeur_salon, tv_salon
- 5 CUISINE : micro_ondes, lave_linge, lave_vaisselle, airfryer, four_plaque, frigo, congel, petit_dejeuner
- 7 BUREAU : bureau_pc, fer_a_repasser_bureau · 9 CHAMBRE : tete_de_lit_chambre, tv_chambre

### P3 — Éclairage

#### SLUGS CANONIQUES P3 — SOURCE DE VÉRITÉ

| # | Pièce | Slug base |
|:--|:------|:----------|
| 1 | ENTRÉE | `hue_white_lamp_entree` |
| 2 | SALON | `hue_white_lamp_table` |
| 3 | SALON | `hue_ambiance_lamp_salon_1` |
| 4 | SALON | `hue_ambiance_lamp_salon_2` |
| 5 | SALON | `hue_ambiance_lamp_salon_3` |
| 6 | SALON | `hue_color_candle_salon_1` |
| 7 | CUISINE | `hue_white_lamp_cuisine` |
| 8 | COULOIR | `hue_white_lamp_couloir` |
| 9 | BUREAU | `hue_play_1_pc_bureau` |
| 10 | BUREAU | `hue_play_2_pc_bureau` |
| 11 | BUREAU | `hue_play_3_pc_bureau` |
| 12 | BUREAU | `hue_white_lamp_bureau_1` |
| 13 | BUREAU | `hue_white_lamp_bureau_2` |
| 14 | SDB | `relais_lumiere_sdb_sonoff` |
| 15 | SDB | `hue_white_lamp_salle_de_bain` |
| 16 | CHAMBRE | `hue_white_lamp_chambre_1` |
| 17 | CHAMBRE | `hue_white_lamp_chambre_2` |
| 18 | CHAMBRE | `hue_color_candle_chambre_gege` |
| 19 | CHAMBRE | `hue_color_candle_chambre_eric` |

> ⛔ Ne jamais inventer de variantes (`_salon`, `eclairage_`, `lampe_bureau_X_hue`, etc.)
> **Cycles** : `quotidien` | `hebdomadaire` | `mensuel` | `annuel`
> **Erreurs connues à bannir** : `hue_white_lamp_table_salon_*` ❌ / `lampe_bureau_1_hue_*` ❌

#### CONVENTION NOMMAGE TPL — CHAÎNE COMPLÈTE

| Étape | Pattern unique_id | Fichier |
|:------|:------------------|:--------|
| Firmware Hue | `{slug}_energy` | (natif HA) |
| Utility Meter | `{slug}_{cycle}_um` | `P3_UM_AMHQ_1_UNITE` |
| Relais kWh | `{slug}_{cycle}_um_kwh_tpl` | `P3_ENERGIE_TPL` |
| Moyenne W | `{zone}_{cycle}_um_avg_tpl` | `P3_AVG` |

### P4 — Présence : téléphones mobiles (Poco X7 Pro), capteurs Wi-Fi.
→ Détail complet sensor.presence : `IA/IA_P4_PRESENCE.md`

---

## 🖥️ CARTOGRAPHIE DASHBOARD (MATRICE 18 VIGNETTES)

| Ligne | C1 | C2 | C3 |
|:------|:---|:---|:---|
| **L1** | Météo | Températures | Commandes Clim |
| **L2** | Conso Générale | Conso Clim | Conso Éclairage |
| **L3** | Commandes Éclairage | Commandes Éco (Prises) | Fenêtres + Stores |
| **L4** | Proxmox (PVE) | Mini PC (NUC) | Mises à jour HA |
| **L5** | Piles / Batteries | Batteries Portables | MariaDB |
| **L6** | Qualité Air (Appart) | Pollution / Pollen | Vigilance Eau |

---

## 🌳 ARBORESCENCE LOCALE (RÉSUMÉ)

```
ReBuild/
├── CLAUDE.md · secrets.yaml
├── IA/              (vide — déplacé vers DOCS/00_IA/)
├── Github/          (INDEX_AUTOMATIONS.md · INDEX_NAVIGATION.md · README.md)
├── historique/      (JOURNAL_COMPLET_2026-04-25_2026-07-14.md)
└── DOCS/
    ├── 00_IA/                      (IA_CONTEXT_BASE.md · sous_context_ia/ → tous les IA_*.md)
    ├── 01_docs_config_system/
    │   ├── config_system_YAML/     (sensors/ · templates/ · utility_meter/ · command_line/ · groups/ · …) → /homeassistant/
    │   └── config_system_MD/       (configuration.md)
    ├── 02_docs_dashboard/
    │   ├── dashboard_docs_MD/      (DEPENDANCES_GLOBALES.md · L*C* docs · PAGE_*.md)  → H:\Docs\
    │   └── dashboard_docs_YAML/    (L1C1→L6C3 · PAGE_* · Dashboard_COMPLET/)          → H:\Docs\
    ├── 03_docs_automations/
    │   ├── docs_automations_MD/    (docs par automation)                               → H:\Docs\
    │   └── docs_automations_YAML/  (yaml individuels par automation)                   → UI HA
    ├── 04_docs_scripts/
    │   ├── docs_scripts_MD/        (docs scripts)                                      → H:\Docs\
    │   └── docs_scripts_YAML/      (yaml scripts)                                      → /homeassistant/
    └── 05_docs_MD_system/          (workflow · MOC · templates · github)
```

⛔ `TREE_CORRIGE/`, `TREE_ORIGINE/`, `Dashboard/`, `docs_dashboard/`, `docs_automations/`, `docs_scripts/` **supprimés le 2026-07-14** — tout est sous `DOCS/`.

→ Arborescences complètes prod + local : `DOCS/00_IA/sous_context_ia/IA_ARBO_DETAIL.md`

---

## 👥 RÉFÉRENTIEL P4 — VALEURS `sensor.groupe`

| Valeur | Signification |
|:-------|:--------------|
| `groupe_1` | Absent |
| `groupe_2` | Mamour seule |
| `groupe_3` | Eric seul |
| `groupe_4` | Tous les deux |

→ sensor.presence + codes réseau complets : `DOCS/00_IA/sous_context_ia/IA_P4_PRESENCE.md`

---

## 🌡️ RÉFÉRENTIEL TENDANCE T° EXTÉRIEURE

| Condition | Texte généré |
|:----------|:-------------|
| `increasing` | `T°Ext Up ↗ XX°` |
| `decreasing` | `T°Ext Down ↘ XX°` |
| `stable` | `T°Ext stable → XX°` |

---

# 🏠 LOGEMENT & STRATÉGIE THERMIQUE
- **Localisation :** 06140 Vence (Altitude ~360m) — Immeuble 1980, 4ème étage sous toiture. Traversant SUD/NORD, simple vitrage. VMC en SDB.
- **Mode Absence Hiver** : 17°C · si T° Ext < 10°C → 18°C · si T° Ext < 8°C → 19°C.
- **Mode Absence Été** : T° Cible = 28°C.
- **Logique "Cœur du Système" (T° Extérieure → Cible → Confort) :**

![Confort Cible Calcul Flow](confort_cible_calcul_flow.png)
*(copie locale du diagramme - [asset GitHub d'origine](https://github.com/user-attachments/assets/f18e24a2-1441-482b-af70-537a7b208e15))*

## 🏠 STRUCTURE DU LOGEMENT
*(uniquement pour l'analyse des consommations électriques)*
- **Localisation :** 06140 Vence (Altitude ~360m).
- **Type :** Immeuble début 1980, 4ème et dernier étage (Sous toiture).
- **Caractéristiques :** Traversant SUD/NORD, Simple vitrage partout.
- **VMC :** Présente en SDB (Crée une dépression thermique).

## 📏 DIMENSIONS & PÔLES
*(uniquement pour l'analyse des consommations électriques)*
1. **SALON (Sud) :** 6.52m x 3.97m (25.88 m²).
   - *Équipement :* Split mural, Volet motorisé (Auto: 7h30 -> Coucher soleil / Fermé si Absent / Fermé si >34°C).
   - *Note :* Apport solaire crucial dès 15h.
2. **CUISINE (Nord) :** 4.86m x 2.18m (10.59 m²).
   - *Équipement :* "radiateur_cuisine" (Bain d'huile avec relais connecté).
   - *Auto :* L-Ma-Me-Je (4h45-7h), Ve-Sa-Di (5h45-8h).
3. **BUREAU (Nord) :** 3.95m x 2.67m (10.55 m²).
   - *Équipement :* Split mural, Volet motorisé.
   - *Auto :* Ouvert uniquement si T° Ext [18°C - 25°C].
4. **SDB (Interne) :** 1.96m x 1.58m (3.13 m²) Pas de fenêtre.
   - *Équipement :* Soufflant (2x1000W), Sèche-serviette (150W).
   - *Auto :* Soufflant OFF si >23°C. Sèche-serviette 1h après douche.
5. **CHAMBRE (Nord) :** 3.95m x 2.85m (11.26 m²).
   - *Équipement :* Split mural. Pas de volet motorisé.
   - *Note :* Forte dissipation thermique (DUT élevé).

 