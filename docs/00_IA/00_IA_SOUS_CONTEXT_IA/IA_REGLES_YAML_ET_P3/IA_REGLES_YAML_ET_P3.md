# REGLES YAML, NOMMAGE DES FICHIERS ET P3 ECLAIRAGE (SLUGS, CHAINE TPL)
<div align="center">

[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;
[![MàJ](https://img.shields.io/badge/MàJ-2026--11--28-44739e?style=flat-square)](.)&nbsp;
[![HA](https://img.shields.io/badge/HA-2026.11.3-03a9f4?style=flat-square&logo=home-assistant&logoColor=white)](.)&nbsp;
[![IA Partner](https://img.shields.io/badge/IA_Partner-Claude_Sonnet_5.5-blueviolet?style=flat-square)](.)&nbsp;
[![Source](https://img.shields.io/badge/Source-Interne-2196f3?style=flat-square)](.)&nbsp;
[![Modifs](https://img.shields.io/badge/Modifs-Autorisees-0f9d58?style=flat-square)](.)&nbsp;
[![Expert](https://img.shields.io/badge/Expert-HAOS_Proxmox-success?style=flat-square)](.)&nbsp;
[![Type](https://img.shields.io/badge/Type-IA_System-ffeb3b?style=flat-square)](.)

</div>

*Lire ce fichier si : creation ou modification d'un YAML de config, nommage d'un fichier ou dossier de docs, bordures ASCII, headers, slug, name, unique_id, Zero Helper UI, pas de valeur en dur, tout YAML P3 (slug, unique_id de lampe, zone, total).*

> Extrait mot pour mot de `Claude md SAVE/CLAUDE.md` (lignes 445-592, 662-727, version du 2026-11-23, date de derniere modification du fichier), le 2026-11-28. Aucun mot modifie dans les sections ci-dessous.

---

## 📋 RÈGLES YAML - CONVENTIONS (CRITÈRES DE CONFORMITÉ)

> S'appliquent aux fichiers `.yaml` modulaires (sensors/, templates/, utility_meter/, command_line/). Jamais pour les automations.

### 1 - Numérotation officielle des poles
5 poles, préfixés P0 à P4. 1 fichier YAML = 1 seul pole - jamais deux poles dans le même fichier.

| Pole | Domaine |
|:-----|:--------|
| P0 | Énergie Globale (Linky, Nodon) |
| P1 | Chauffage & Clim |
| P2 | Prises connectées |
| P3 | Éclairage |
| P4 | Présence (Wi-Fi, mobile) |

### 2 - Numérotation officielle des pièces (index 1-9)
1 Entrée · 2 Cellier · 3 Toilette · 4 Salon · 5 Cuisine · 6 Couloir · 7 Bureau · 8 SDB · 9 Chambre

- Ordre obligatoire au sein de chaque bloc de Pole.
- ⛔ Jamais mélanger deux Poles dans la même pièce.

### 3 - Répertoires HA & préfixes hors-pôles

**Répertoires (plateforme HA chargée selon le dossier) :**
`SNS` -> `sensors/` · `UM` -> `utility_meter/` · `TPL` -> `templates/` · `CMD` -> `command_line/` · `GRP_` -> `groups/` (groupes d'entités par constructeur - batteries Hue/IKEA/Sonoff)

**Préfixes hors-pôles (remplacent `P{n}` pour les fichiers sans pôle énergie) :**
`M_` Météo · `AQ_` Air Quality · `S_` Stores · `MPC_` Mini-PC

### 4 - Bordures ASCII
- **Titre principal** - coins arrondis `╭─╮/╰─╯` - largeur 78 car. - texte MAJUSCULES.
  - Si >74 car. : élargir la boîte. ⛔ Ne jamais supprimer les références techniques du titre.
- **Titre secondaire** - coins carrés `┌─┐/└─┘` - largeur 37 car. - texte MAJUSCULES, numérotation 1-9.
- **Largeur** - 78 et 37 sont le cadre standard, pas une limite : une boite peut etre plus large si le titre ne tient pas, mais le haut, le titre et le bas gardent la meme largeur (controle : `check_yaml_forme.py` et le skill `ha-verif-headers`). Un `#` suivi d'une lettre (code commente) n'est pas un en-tete colle.

### 5 - Headers en-tête obligatoires (juste sous la boite ASCII)
```yaml
# ## 📝 DESCRIPTION :
# ## 🧮 CALCUL & SOURCES :
# ## 🔗 CHAÎNE DE DÉPENDANCES :   <- tableau MATÉRIEL / CAPTEUR BRUT / CE FICHIER / AVAL
# ## ⚠️ IMPORTANT (PIÈGES) :
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
```
Tableau chaîne dépendances : `MATÉRIEL` = device physique ou intégration HA (si calculé -> `[calculé]`). `AVAL` = fichier(s) consommateurs + vignette (ex: `P1_UM_AMHQ.yaml -> L2C2`).

### 6 - Convention de nommage : chaîne de suffixes
Chaque suffixe documente la dernière transformation subie par l'entité.

| Étape | Pattern `unique_id` | Fichier source |
|:------|:--------------------|:---------------|
| Source brute | `{slug}_energy` | natif HA (Z2M / Hue / Shelly) |
| Utility Meter | `{slug}_{cycle}_um` | `P*_UM_AMHQ_*` |
| Relais kWh | `{slug}_{cycle}_um_kwh_tpl` | `P*_ENERGIE_TPL` |
| Relais kWh agrégat | `{zone}_{cycle}_kwh_tpl` | agrégat addition des `_um_kwh_tpl` (zone P3) |
| Moyenne W | `{zone}_{cycle}_um_avg_tpl` | `P*_AVG` |

Cycles : `quotidien` | `hebdomadaire` | `mensuel` | `annuel`

- **Règle absolue** : tout sensor sorti d'un UM finit par `_um`. Template kWh -> `_um_kwh_tpl`. Moyenne W -> `_um_avg_tpl`.
- **Règle d'agrégation** : si un fichier `_kwh_tpl` existe, tout nouveau sensor du même type porte aussi `_kwh_tpl` - même fichier, même suffixe.

### 7 - Slug tertiaire
- Format : `# --- unique_id_exact ---` - juste au-dessus de chaque bloc d'entité.
- Utility_meter : un slug par entrée (annuel/mensuel/hebdo/quotidien).
- ⛔ Jamais grouper plusieurs entités sous un seul slug. Le slug doit être l'image exacte du `unique_id` qui suit.

### 8 - name & unique_id
- `name: "Préfixe Nom Lisible Période"` - majuscules initiales - préfixe pôle obligatoire.
- `unique_id: prefixe_nom_lisible_periode` - minuscules, underscores.
- Cohérence croisée obligatoire : `name` et `unique_id` décrivent la même entité.
- ⛔ Jamais d'abréviation inventée hors liste officielle.

### 9 - Nommage fichiers YAML

**Pattern général :** `{POLE}_{TYPE}[_AMHQ][_{VARIANTE}].yaml`

| TYPE | Signification | Pattern complet | Exemple |
|:-----|:-------------|:----------------|:--------|
| `UM` | Utility Meter | `{P}_UM_AMHQ[_{variante}].yaml` | `P1_UM_AMHQ.yaml` |
| `TPL` | Template | `{P}_TPL_AMHQ_{niveau}.yaml` | `P3_TPL_AMHQ_1_UNITE.yaml` |
| `AVG` | Moyenne watts | `{P}_AVG_AMHQ[_{variante}].yaml` | `P2_AVG_AMHQ_prises.yaml` |
| `TOTAL` | Agrégat global | `{P}_TOTAL_AMHQ.yaml` | `P1_TOTAL_AMHQ.yaml` |
| `kWh` | Énergie Riemann/spécifique | `{P}_kWh_{description}.yaml` | `P1_kWh_clim_chauffage.yaml` |
| `DUT` | Durée d'utilisation | `{P}_DUT_{description}.yaml` | `P1_DUT_clim_chauffage.yaml` |
| `DIAG` | Template diagnostic en cours (1 cycle) | `{P}_DIAG_{description}_{cycle}.yaml` | `P0_DIAG_conso_hebdomadaire.yaml` |
| `POWER` | Puissance instantanée totale | `{P}_POWER_{niveau}.yaml` | `P3_POWER_3_TOTAL_ZONE.yaml` |
| `BV` | Bouton Virtuel - interrupteur logique sans hardware | paire IB + SW obligatoire, sans numéro | voir IB + SW ci-dessous |
| `IB` | Input Boolean - stockage état on/off du BV | `{P}_BV_IB_{description}.yaml` dans `input_booleans/` | `P3_BV_IB_inter_smorig_salon.yaml` |
| `SW` | Switch - template switch exposé utilisateur | `{P}_BV_IB_SW_{description}.yaml` dans `templates/Inter_BP_Virtuel/` | `P3_BV_IB_SW_inter_smorig_salon.yaml` |
| `MINI_MAXI_AVG` | Stats min/max/avg sur période glissante | `{P}_MINI_MAXI_AVG_{description}.yaml` | `P0_MINI_MAXI_AVG_Genelec_appart.yaml` |
| `UI_DASHBOARD` | Spécification de fichiers propre à un pôle : change un état en signal ou autre chose (templates d'affichage) | `{P}_UI_DASHBOARD.yaml` | `P1_UI_DASHBOARD.yaml` |

**Règles :**
- `_AMHQ` = present si le fichier couvre les 4 cycles (Annuel/Mensuel/Hebdo/Quotidien)
- `_VARIANTE` = discriminant si plusieurs fichiers du même TYPE dans le même pole : nom fonctionnel minuscules (`prises`) ou niveau numéroté (`1_UNITE`, `2_ZONE`, `3_TOTAL`) ; exception : `MINI_PC` toujours en majuscules dans tous les noms de dossiers et de fichiers, y compris les YAML de config (`P2_AVG_AMHQ_MINI_PC.yaml`, `P2_UM_AMHQ_MINI_PC.yaml`) ; jamais `mini_pc` ni `Mini_pc` (décidé par Eric le 2026-10-25)
- Niveaux P3 (suffixe de `_VARIANTE`, motif `_{n}_UNITE`, `_{n}_ZONE`, `_{n}_TOTAL`, toujours en majuscules, extension `.yaml` inchangée) : `_1_UNITE` = une lampe individuelle ; `_2_ZONE` = agrégat par pièce (somme des lampes d'une zone) ; `_3_TOTAL` = appartement entier. Le détail des `unique_id` par niveau est dans la section P3 (convention nommage TPL)
- Un nom qui se termine par `_UNITE`, `_ZONE` ou `_TOTAL`, avec ou sans numéro, n'est pas renommé à cause de ce suffixe
- Cas à part : `P1_AVG_AMHQ_UNITE.yaml` porte `_UNITE` sans numéro de niveau ; `P3_POWER_3_TOTAL_ZONE.yaml` est de niveau 3 (TOTAL) avec un suffixe ZONE en plus. Noms d'origine conservés
- Hors-poles : `{PREFIXE}_{index}_{description}.yaml` - ex: `M_04_tendances_th_ext_card.yaml`
- 1 fichier = 1 seul pole - jamais deux poles dans le même fichier
- ⛔ `P*_UI_DASHBOARD` (ancien nom `ui_dashboard`) : templates d'affichage uniquement (texte, couleurs, icônes) - jamais de calculs kWh/W/DUT
- `MINI_` ou `MAXI_` peuvent s'utiliser seuls ; `MINI_MAXI_AVG` est l'agglomération de `MINI_`, `MAXI_` et `AVG` (Eric, 2026-10-17)
- `SDB` = salle de bain : toute variante d'écriture de l'abréviation (`sdb`, `Sdb`...) s'écrit `SDB` dans un nom de dossier ou de fichier de `docs` ; un nom écrit en toutes lettres (`salle_de_bain`) n'est pas touché
- `eCO` s'écrit toujours `eCO` (exemple `P2_eCO_prises`)
- Un nom de module HACS ou d'application s'écrit comme lui, majuscules comprises (exemple `P0_MyElectricalData`)
- `Z2M` = Zigbee2MQTT : toute variante d'écriture de l'abréviation (`z2m`, `Z2m`, `z2M`) s'écrit `Z2M` dans un nom de dossier ou de fichier de `docs` (exemple `card_services_ha_Z2M_mariadb.yaml`) ; le nom écrit en toutes lettres (`zigbee2mqtt`) et les identifiants d'entités Home Assistant (minuscules obligatoires) ne sont pas touchés
- `RASPI` = Raspberry Pi : l'abréviation, écrite `raspi` (`Raspi`, `RasPi`) ou `rpi` (`Rpi`, `RPI`), s'écrit `RASPI` dans un nom de dossier ou de fichier de `docs` (exemple `A_rpi_fan_pwm_6_states` devient `A_RASPI_fan_pwm_6_states`) ; `rpi` n'est écrit `RASPI` que comme mot isolé entre séparateurs (pas dans `scorpion`) ; le nom écrit en toutes lettres (`raspberry`) et les identifiants d'entités Home Assistant (minuscules obligatoires) ne sont pas touchés ; `Rpi4` s'écrit aussi `RASPI` (le numéro de modèle disparaît, décidé le 2026-10-17)
- `AQ_` remplace `A_` pour Air Quality : `A_01_air_quality.yaml` s'écrit `AQ_01_air_quality.yaml`, et le dossier `Air_quality/` s'écrit `Air_Quality/` (exception limitée à ce nom, chaque mot garde sa majuscule) ; ne pas confondre avec les lettres d'ordre `A_`, `B_`, `C_`, `D_` des automations
- `GitHub` s'écrit toujours `GitHub` (G et H majuscules) : toute autre écriture (`github`, `Github`, `GITHUB`) devient `GitHub` dans un nom de dossier ou de fichier de `docs` ; cette règle l'emporte sur la règle de la première lettre (exemple : `Github_maintenance` devient `GitHub_maintenance`, `GITHUB` devient `GitHub`)
- `GLOBAL_INDEX` s'écrit toujours en majuscules dans un nom de dossier ou de fichier de `docs`, sauvegardes `.bak` comprises (exemple : `Gen_global_index_ia.py` devient `Gen_GLOBAL_INDEX_ia.py`)
- Les dossiers de type de fichiers (md, yaml, sh...) enfants d'un dossier racine `0x_` de `docs` reprennent son numéro : `03_docs_automations_MD` (et non `docs_automations_md`) ; détail dans le fichier des règles de nommage (2026-10-17)
- Aucun accent dans les noms de dossiers et de fichiers de `docs`
- Caracteres dans les noms de dossiers et de fichiers de `docs` (decide par Eric le 2026-10-25, 9 regles) :
  1. Base : un espace devient `_` ; `-` devient `_` ; `&` devient `_et_` (toujours en minuscules) ; `(` et `)` sont supprimes.
  2. Autres caracteres : tout caractere qui n'est ni lettre, ni chiffre, ni `_`, ni `.` devient `_` (`,` `;` `'` `+` `=` `%` `[ ]` `{ }` `!` `@` `$` `~`). Les accents ont leur propre regle.
  3. Reduction : plusieurs espaces de suite, et les `_` produits par ces regles, donnent un seul `_` (`Backup ha - GitHub` donne `Backup_ha_GitHub`). Les `__` voulus (`__pycache__`) ne sont pas touches.
  4. Debut et fin : un espace en tete ou en fin de nom, un `_` en fin de nom et l'espace juste avant l'extension sont supprimes ; un `_` en tete reste (`_Sans_categorie`, `_Template_doc.md`) (`fichier .md` donne `fichier.md`).
  5. Point : un `.` a l'interieur du nom, hors extension finale, devient `_` (`monitor_temp.sh_save` donne `monitor_temp_sh_save`). Les noms caches qui commencent par `.` restent intacts (`.scripts`).
  6. Exceptions a toutes ces regles : `L0C0_PAGE_Home` (contenu compris) ; `.scripts` et ses sous-dossiers (`01_scripts.sh`, `02_scripts.py`, `01_scripts.sh_md`, `02_scripts.py_md`) ; les noms de modules HACS et d'applications (voir plus haut) ; les fichiers generes (`__pycache__`, `*.pyc`, `#...#`, `.bak_...`) ; `.claude\skills`, hors de `docs` ; les dates AAAA-MM-JJ (avec ou sans heure `_HHhMM`), qui gardent leurs `-` (`MODIFS_2026-10-10_claude.md`, `DEPENDANCES_GLOBALES_archive_2026-09-28.md`).
  7. Perimetre : uniquement les noms de dossiers et de fichiers de `docs`, pas les titres dans les fichiers, ni les `name:` et alias HA, ni les ancres de liens markdown, ni les YAML de la racine de `H:`. Les dossiers d'automations (`03_docs_automations_MD` et `03_docs_automations_YAML`) sont soumis aux memes regles (decide par Eric le 2026-10-25) : `Tarif hc-hp` donne `Tarif_hc_hp`, `Automations.yaml original` donne `Automations_yaml_original`.
  8. Collisions : si deux noms donnent le meme nom apres remplacement, on s'arrete et on demande a Eric.
  9. Alias des automations et des scripts : INTERDICTION de toucher aux alias (titres) des automations de `automations.yaml` et des scripts de `scripts.yaml`, ni aux cles des scripts (decide par Eric le 2026-10-25), sauf si un jour ils posent probleme. Les renommer ne sert a rien : ils sont lus sans erreur par les scripts et ce sont des titres affiches dans HA.
- Dossiers LxCx de `docs/02_docs_dashboard` (décidé par Eric le 2026-10-25, définitif ; seul `L0C0_PAGE_Home` reste tel quel) : dans `02_dashboard_docs_MD` comme dans `02_dashboard_docs_YAML`, un dossier `LxCx_{NOM}` en majuscules et sans numéro (`L3C3_STORES`) contient `LxCx_{NOM}_01_Vignette` et `LxCx_{NOM}_02_Page` (`LxCx_{NOM}_03_Page`... si plusieurs pages), et les fichiers s'appellent `LxCx_Vignette_{NOM}.md` ou `.yaml` et `LxCx_Page_{NOM}.md` ou `.yaml` (`L3C3_STORES_01_Vignette\L3C3_Vignette_STORES.md`, `L3C3_STORES_02_Page\L3C3_Page_STORES.yaml`). Tout nom commence par `LxCx` pour repérer où on se trouve. Un suffixe éventuel (page gauche, page droite...) s'écrit en minuscules après le {NOM} dans le nom du fichier et dans le nom du dossier de page (`L3C1_ECLAIRAGE_02_Page_gauche`, `L3C1_Page_ECLAIRAGE_gauche.md`, validé par Eric le 2026-10-25).
- Détail et écarts de toutes les règles de nommage de `docs` : `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_NOM_DES_REPERTOIRES_ET_FICHIERS/IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md` (brouillon à valider ; aucun renommage sans go séparé d'Eric)
- Fichiers legacy non conformes : pas de renommage sec en prod - renommer uniquement si le fichier est modifié pour autre chose
- ⚠️ Exception legacy TOTAL : `P0_total_pour_les_7_postes.yaml` agrège 7 postes (chauffage/hygiène/multimédia...) sur 4 cycles - devrait s'appeler `P0_TOTAL_AMHQ.yaml` mais nom d'origine conservé
- 🧊 Cas particulier en attente : `P2_current_all_standby.yaml` - puissance totale veilles, TYPE non encore formalisé

### NOTA: PHILOSOPHIE - Zero Helper UI
Aucun `input_boolean`, `input_number` ou `input_select` pour la logique métier. Tout est en YAML - versionnable, auditable, rollbackable sur Git.
- ⛔ Helper UI : valeur stockée en base HA, non versionnée, diff illisible (`"entity changed"`), perd sa valeur au crash/restore.
- ✅ Template YAML : commit Git avec date et contexte, diff lisible (`t >= 26.5` -> `t >= 27`), rollback instantané, restore exact.

### NOTA: REGLE - PAS DE VALEUR EN DUR DANS UN YAML (decidee par Eric le 2026-11-09)
- INTERDIT de mettre des valeurs en dur (hard code) dans un YAML : seuils, durees, consignes, listes d'entites, textes, etc. Une valeur qui existe deja ailleurs dans HA (capteur, attribut, config centralisee comme `sensor.eco_prises_config`) se lit, elle ne se recopie pas.
- Exception : seulement si c'est IMPOSSIBLE de faire autrement. Avant de conclure que c'est impossible, Claude cherche activement les alternatives et ne prend pas la solution la plus simple ou la plus rapide pour elle-meme.
- Si l'exception est retenue : dire a Eric quelles alternatives ont ete etudiees et pourquoi elles ne marchent pas, et le noter en commentaire dans le YAML.
- Cette regle s'applique avec "Zero Helper UI" ci-dessus (pas de helper UI) : l'alternative cherchee reste en YAML, versionnable.
- Application : tout YAML cree ou modifie a partir du 2026-11-09. Un YAML existant n'est pas corrige sans demande d'Eric.

---

## 🛠️ RÈGLE DOCS VIGNETTES - DÉPENDANCES OBLIGATOIRES

À chaque création/modif d'une doc vignette (`docs/02_docs_dashboard/02_dashboard_docs_MD/L*`) :
1. Remplir **ENTITÉS UTILISÉES - PROVENANCE COMPLÈTE** dans la doc.
2. Mettre à jour `docs/00_IA/00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md` (🔲 → ✅).
3. Mettre à jour la date en haut de `DEPENDANCES_GLOBALES_CLAUDE_memoire.md`.

---

#### SLUGS CANONIQUES P3 - SOURCE DE VÉRITÉ

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

#### CONVENTION NOMMAGE TPL - CHAÎNE COMPLÈTE P3 (3 NIVEAUX)

> ⚠️ P3 a 3 niveaux distincts. Le pattern de suffixe change selon le niveau.

**Niveau 1 - UNITÉ** (par lampe individuelle, 19 slugs canoniques) :

| Étape | Pattern `unique_id` | Fichier |
|:------|:--------------------|:--------|
| Source Hue | `{slug}_energy` | natif HA (Hue bridge) |
| Utility Meter | `{slug}_{cycle}_um` | `P3_UM_AMHQ_1_UNITE.yaml` |
| Relais kWh | `{slug}_{cycle}_um_kwh_tpl` | `P3_TPL_AMHQ_1_UNITE.yaml` |
| Moyenne W | `{slug}_avg_watts_{cycle}` | `P3_AVG_AMHQ_1_UNITE.yaml` |

**Niveau 2 - ZONE** (agrégat par pièce - somme des lampes d'une zone) :

| Étape | Pattern `unique_id` | Fichier |
|:------|:--------------------|:--------|
| Relais kWh zone | `eclairage_{zone}_{nb}_{cycle}_um_kwh_tpl` | `P3_TPL_AMHQ_2_ZONE.yaml` |
| Moyenne W zone | `eclairage_{zone}_{nb}_avg_watts_{cycle}` | `P3_AVG_AMHQ_2_ZONE.yaml` |

Zones définies (slug_zone + nb lampes) : `entree_1` · `salon_5` · `cuisine_1` · `couloir_1` · `bureau_5` · `sdb_2` · `chambre_4`
Agrégats multi-zones dans le même fichier : `appart_2`, `appart_3`

**Niveau 3 - TOTAL** (appart entier) :

| Étape | Pattern `unique_id` | Fichier |
|:------|:--------------------|:--------|
| Total kWh | `eclairage_total_unit_{cycle}_kwh_tpl` | `P3_TPL_AMHQ_3_TOTAL.yaml` |
| Total AVG W | `eclairage_total_unit_avg_watts_{cycle}` | `P3_AVG_AMHQ_3_TOTAL.yaml` |
| Total puissance | `eclairage_total_group_puissance_tpl` | `P3_POWER_3_TOTAL_ZONE.yaml` |

**Distinctions critiques - anti-hallucination :**
- `_um_kwh_tpl` = **niveau 1 ET niveau 2** (lampe individuelle OU zone agrégée) - suffixe identique, pattern de nom différent
- `_kwh_tpl` (sans `_um_`) = **UNIQUEMENT niveau 3** (total appart) - ne jamais l'utiliser à un autre niveau
- AVG P3 : calculé depuis `_um_kwh_tpl` (pas depuis `_um` directement). Suffixe de sortie : `_avg_watts_{cycle}` - pas `_um_avg_tpl`
- AVG P0 + P1 + P2 : calculé directement depuis `_um` - pas de `_um_kwh_tpl` intermédiaire
- PowerCalc : P3 uniquement, Hue sans monitoring natif + exception `relais_lumiere_sdb_sonoff` (10W fixe)

<!-- annotations_log: [2026-11-28] creation par extraction de CLAUDE.md pour l'alleger (demande d'Eric), contenu inchange -->
<!-- annotations_log: [2026-11-28] corrections_refonte : texte corrige : contre-exemple de la regle des dossiers de type (docs_automations_md) et nombre de regles du bloc caracteres (9 et non 8), a la demande d'Eric 2026-11-28 -->
