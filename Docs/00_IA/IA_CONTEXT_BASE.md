> ⚠️ **SYNC** : Ce fichier est une copie lisible de `CLAUDE.md` (racine ReBuild).  
> Mettre à jour en même temps que `CLAUDE.md` à chaque session.

---

> **REGLE ABSOLUE :** Tu devras être honnete, ne pas mentir, ne pas tricher, être très attentif, et être 100% objectif et que tu aies l'interdiction de me flater pour me flater ou de me donner une réponse pour me faire plaisire, ou pour me donner une réponse quoi qu'il arrive. Et que si une de mes répose, une de mes solution ou une idées de "codage" (yaml) ou autres, que je pourrais avoir ne te semble pas bonne, il est impératif que tu me le fasse s'avoir sans aller systématiquement dans mon sens.
> Si une de mes demandes ou propositions est ambiguë, floue, incompréhensible, contradictoire ou incomplète, tu devras me poser des questions. Et là aussi, interdiction de valider une interprétation au hasard pour me faire plaisir, ou me flater.

> **REGLE ABSOLUE — STYLE :** Ne jamais utiliser de symboles qui trahissent l'écriture d'un LLM et qui n'existent pas sur un clavier standard. Interdit : `—` (em dash), `…` (ellipse typographique), `«»` (guillemets typographiques), `·` (point médian), et tout autre caractère spécial inaccessible sans Alt+code. Utiliser à la place : `-`, `...`, `"`, `-` etc.

# 🧠 BASE DE CONTEXTE EXPERT HOME ASSISTANT
*Dernière mise à jour : 2026-06-19*

---

## 📚 FICHIERS DE RÉFÉRENCE — LIRE À LA DEMANDE

> ⚠️ Ne PAS lire ces fichiers par défaut — uniquement si la tâche le nécessite.

| Fichier | Lire si… |
|:--------|:---------|
| `IA/IA_INTEGRATIONS_CARTES.md` | YAML dashboard à valider, `type: custom:*` inconnu, intégration manquante, palette couleurs |
| `IA/IA_AUTOMATIONS_NOTIFS.md` | Création/modif automation, écriture message `notify`, script HA |
| `IA/IA_P4_PRESENCE.md` | `sensor.presence`, format notif avec présence, logique groupe WiFi |
| `IA/IA_ARBO_DETAIL.md` | Audit fichiers, sync GitHub, arborescence prod complète, URLs raw GitHub |
| `IA/IA_INDEX_NAVIGATION.md` | Régénération de `INDEX_NAVIGATION_FULL.md`, ajout vignette/page à l'index, mapping entités → fichiers sources, structure accordéon GitHub |
| `IA/IA_INDEX_AUTOMATIONS.md` | Régénération de `INDEX_AUTOMATIONS.md`, ajout/suppression automation, mapping alias → TREE_CORRIGE → docs, anomalies connues |
| `IA/IA_CMD_TERMINAL_HA.md` | Commande tree prod, audit MD5, git backup, chemins `/homeassistant/`, logs HA |

---

# 🛡️ PROTOCOLES

## 🔎 PROTOCOLE DÉBUT DE SESSION (OBLIGATOIRE)

**À chaque ouverture de session, poser cette question AVANT tout travail :**

> "As-tu fait des modifications depuis la dernière session (avec un autre outil, Deepseek, etc.) ?"

| Réponse | Action |
|:--------|:-------|
| **Oui — tout** | Lancer `audit_full` (YAML + ATMA) → lire `/homeassistant/.logs/audit_full.log` |
| **Oui — fichiers YAML** | Lancer `audit_yaml` → lire `/homeassistant/.logs/audit_yaml.log` |
| **Oui — automations** | Lancer `audit_atma` → lire `/homeassistant/.logs/audit_atma.log` |
| **Non** | Continuer directement |

**Scripts disponibles** (sur HA : `/homeassistant/.scripts/`) :
- `audit_yaml.sh` — MD5 sensors/templates/utility_meter/command_line vs GitHub
- `audit_atma.sh` — MD5 + diff alias automations.yaml vs GitHub
- `audit_full.sh` — les deux en séquence

**Boutons dashboard** : page Système (L5C3) → carte "Audit GitHub" (FULL · YAML · ATMA)
**Logs** : `/homeassistant/.logs/audit_yaml.log` · `audit_atma.log` · `audit_full.log`

---

## Cohérence Documentaire (anti-oubli)
- À chaque modif YAML dans `TREE_CORRIGE` → vérifier impact vignette (`docs/L*`) + chaîne dépendances.
- Si rupture cohérence → proposer update `docs/DEPENDANCES_GLOBALES.md` ou `/sync_index`.
- Tâche non terminée si code OK mais doc dépendances obsolète.

## Économie de Tokens
- Pas de longs discours d'intro/conclusion. Blocs ciblés uniquement.
- Log de modif : `# annotations_log:` uniquement. Référence directe par ID matrice (L1C1, P2…).
- Ne jamais répéter le code YAML déjà validé.

## Slash Commands
- `/fix_file` → bloc YAML corrigé uniquement.
- `/sync_index` → met à jour `DEPENDANCES_GLOBALES.md`.
- `/status` → résumé 3 points avancement.
- `/histo` → journal de bord compact à copier en `.txt`.

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

| Priorité | Source | Rôle |
|:---------|:-------|:-----|
| **1** | **Home Assistant (live)** | Prod = référence absolue |
| **2** | **GitHub `home_assistant_re-build`** | Reflet prod — backup git auto depuis HA |
| **3** | **Local `ReBuild/`** | Espace de travail — draft uniquement |

> Ancien repo `home-assistant-config` **supprimé définitivement** (2026-04-27). Seul `home_assistant_re-build` est actif.

### Règles fondamentales
- Répertoires préfixés `P*_` selon le Pôle.
- `TREE_CORRIGE/` = état cible → /homeassistant/ (audité 1×/semaine).
- `TREE_ORIGINE/` = snapshot GitHub avant corrections.
- Fichiers absents de `TREE_CORRIGE` mais présents GitHub = à supprimer en prod.
- Jamais copier un fichier sans le valider dans `TREE_CORRIGE` d'abord.
- Automations : jamais modifier `automations.yaml` direct → passer par UI HA + `automations_corrige/`.

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
| **🔴 CRITIQUE** | `TREE_CORRIGE/` YAML (sensors/, templates/, utility_meter/, command_line/) | Fichiers déployés dans `/homeassistant/` — un écart peut casser HA |
| **🔴 CRITIQUE** | `automations.yaml` GitHub vs `docs_automations/TREE_CORRIGE/` | 48 automations — détecter ajouts/suppressions/renommages depuis HA |
| **🟡 SECONDAIRE** | `Dashboard/` vs `Docs/Dashboard/` | UI seulement — ne casse pas HA |

### Audit automations (MD5 + diff alias)
```bash
# Compter et lister les alias top-level dans automations.yaml GitHub
grep "^  alias:" /tmp/home_assistant_re-build-main/automations.yaml | sed 's/  alias: //' | sort > /tmp/github_aliases.txt

# Compter les fichiers TREE_CORRIGE automations (hors old/)
find docs_automations/TREE_CORRIGE -name "*.yaml" -not -path "*/old/*" | sort > /tmp/local_autom_files.txt

# Comparer les alias avec les noms de fichiers → détecter les manquants
wc -l /tmp/github_aliases.txt /tmp/local_autom_files.txt
```

**Dashboard complet** : vérifier age avant comparaison (`Dashboard_COMPLET/Dashboard_YYYY_MM_DD.yaml` ≤ 2 jours).

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

À chaque création/modif d'une doc vignette (`docs/L*`) :
1. Remplir **ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE** dans la doc.
2. Mettre à jour `docs/DEPENDANCES_GLOBALES.md` (🔲 → ✅).
3. Mettre à jour la date en haut de `DEPENDANCES_GLOBALES.md`.

---

## 📋 RÈGLE DASHBOARD/ — VERSIONING

| Type | Format |
|:-----|:-------|
| Dashboard complet | `Dashboard_YYYY_MM_DD.yaml` (conservation illimitée) |
| Vignette | `vignette_[id]_YYYY-MM-DD.yaml` |
| Page | `page_[id]_YYYY-MM-DD.yaml` |
| Carte isolée | `card_[nom]_YYYY-MM-DD.yaml` |

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
→ Détail complet : `IA/IA_INTEGRATIONS_CARTES.md`

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
├── CLAUDE.md · README.md · SYNC_REPORT.md · secrets.yaml
├── IA/          (IA_INTEGRATIONS_CARTES.md · IA_AUTOMATIONS_NOTIFS.md · IA_P4_PRESENCE.md · IA_ARBO_DETAIL.md)
├── Dashboard/   (Dashboard_COMPLET/ · L1C1→L6C3 · PAGE_*)
├── docs_dashboard/ (TREE_CORRIGE/ · TREE_ORIGINE/ · docs/)
├── docs_automations/ (TREE_CORRIGE/ · TREE_ORIGINE/ · docs/)
└── docs_scripts/    (TREE_CORRIGE/ · TREE_ORIGINE/ · docs/)
```

→ Arborescences complètes prod + local : `IA/IA_ARBO_DETAIL.md`

---

## 👥 RÉFÉRENTIEL P4 — VALEURS `sensor.groupe`

| Valeur | Signification |
|:-------|:--------------|
| `groupe_1` | Absent |
| `groupe_2` | Mamour seule |
| `groupe_3` | Eric seul |
| `groupe_4` | Tous les deux |

→ sensor.presence + codes réseau complets : `IA/IA_P4_PRESENCE.md`

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

 