> **REGLE ABSOLUE :** Ne pas caresser dans le sens du poil. Etre honnete. Ne pas mentir. Ne pas tricher.

# 🧠 BASE DE CONTEXTE EXPERT HOME ASSISTANT
*Dernière mise à jour : 2026-04-19*

---

# 🛡️ PROTOCOLE DE COHÉRENCE DOCUMENTAIRE (ANTI-OUBLI)
- **Vérification Inter-fichiers** : À chaque modification d'un YAML dans `TREE_CORRIGE`, l'IA doit *obligatoirement* vérifier si l'entité modifiée impacte une vignette (`docs/L*`) ou la chaîne de dépendances.
- **Auto-Update de l'Index** : Si une modification YAML entraîne une rupture de cohérence, l'IA doit proposer la mise à jour de `docs/DEPENDANCES_GLOBALES.md` dans la même réponse ou via la commande `/sync_index`.
- **Zéro Latence** : Ne jamais considérer une tâche comme "terminée" si le code est prêt mais que la documentation de dépendance associée est obsolète.
  
---   

## 📉 STRATÉGIE D'ÉCONOMIE DE TOKENS
- **Sobriété** : Pas de longs discours d'introduction ou de conclusion.
- **Blocs ciblés** : Si on travaille sur un gros fichier, ne renvoyer que l'entité concernée (sauf demande de fichier complet).
- **Log de modif** : Utiliser exclusivement `# annotations_log:` à la fin pour expliquer les changements techniques.
- **Référence directe** : Utiliser les ID de la matrice (L1C1, P2, etc.) pour communiquer plus vite.

# STRATÉGIE ANTI-TOKEN (CONTEXTE OPTIMISÉ)
- Ne jamais répéter le code YAML déjà validé.
- Utiliser uniquement l'INDEX.md pour connaître l'état du projet.
- Interdiction de générer de longues explications si une commande de diagnostic est utilisée.

# COMMANDES DE TRAVAIL (SLASH COMMANDS)
- /fix_file : Analyse l'erreur HA donnée et propose uniquement le bloc de code corrigé.
- /sync_index : Met à jour INDEX.md après une validation.
- /status : Résume en 3 points l'avancement actuel (gain de tokens : évite de relire tout l'historique).
- /histo : Action -> Génère un bloc de texte ultra-compact (style "Journal de bord") à copier dans un fichier .txt. Contenu : les derniers fichiers validés et la tâche en cours.

# CONVENTION "FILE NOTIFY" (BREAKING CHANGE 2026)
- Plateforme `notify.file` interdite en YAML.
- Obligation de passer par l'UI (Paramètres > Appareils > Ajouter Intégration > File).
- Nom du service généré par HA : `notify.file_diag_log_file` (ou nom choisi dans l'UI).

---

## ⚠️ CONTEXTE DU PROJET : NETTOYAGE ET RE-BUILD DE HA

> **Ce dossier ReBuild est le dépôt CIBLE — pas la production.**
> Toute modification, correction ou création de fichier doit cibler **TREE_CORRIGE** en priorité.
> Ne jamais aligner TREE_CORRIGE sur la prod — c'est TREE_CORRIGE qui fait référence.

| | Dépôt GitHub | Rôle |
|:---|:---|:---|
| **HA PROD** | https://github.com/BerrySwann/home-assistant-config | Config actuelle en production — état brut, non nettoyé |
| **HA RE-BUILD** | https://github.com/BerrySwann/home_assistant_re-build | Config cible refactorisée — **source de vérité absolu** |

### Règle fondamentale
- `le repertoire devra commencer par P*_ selon les types d'équipements (Pôles) voir plus bas pour les pôles`
- `TREE_CORRIGE/` = état cible déployable — **c'est lui qui a raison** (doit etre audité une foi par semaine)
- `TREE_ORIGINE/` = snapshot GitHub re-build avant corrections (référence historique)
- Les fichiers **absents de TREE_CORRIGE** mais présents sur GitHub = **anciens fichiers à supprimer de la prod**
- On ne copie **jamais** un fichier de la prod vers TREE_CORRIGE sans le valider et le corriger d'abord

> **Même logique pour les automations :**
> - `automations_corrige/` = état cible déployable — **c'est lui qui a raison**
> - `automations_origine/` = snapshot GitHub avant corrections (référence historique)
> - On ne modifie **jamais** `automations.yaml` en direct — tout changement passe par l'éditeur UI de HA, un par un, en s'appuyant sur les fichiers de `automations_corrige/`
 **Même logique pour les scripts :**
 
---

# 🏠 STRUCTURE DU LOGEMENT 
(uniquement pour l'analyse des consommations électriques)
- **Localisation :** 06140 Vence (Altitude ~360m).
- **Type :** Immeuble début 1980, 4ème et dernier étage (Sous toiture).
- **Caractéristiques :** Traversant SUD/NORD, Simple vitrage partout.
- **VMC :** Présente en SDB (Crée une dépression thermique).

# 📏 DIMENSIONS & PÔLES 
(uniquement pour l'analyse des consommations électriques)
1. **SALON (Sud) :** 6.52m x 3.97m (25.88 m²). 
   - *Équipement :* Split mural, Volet motorisé (Auto: 7h30 -> Coucher soleil / Fermé si Absent / Fermé si >34°C).
   - *Note :* Apport solaire crucial dès 15h.
2. **CUISINE (Nord) :** 4.86m x 2.18m (10.59 m²).
   - *Équipement : "radiateur_cuisine" (Bain d'huile avec relais connecté). 
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
  
---

## 📋 RÈGLES DES FICHIERS YAML — CRITÈRES DE CONFORMITÉ

> S'appliquent à tout fichier `.yaml` modulaire (sensors/, templates/, utility_meter/, command_line/). **Jamais pour les automations.**

### 1. BORDURE ASCII

- **TITRE PRINCIPAL** — Boîte coins arrondis `╭─╮ / │ / ╰─╯`
  - Largeur : `# ╭` + 74 tirets `─` + `╮` = **78 caractères total**
  - Texte en **MAJUSCULES** (ex: `CAPTEUR : INTÉGRATION KWH (PÔLE 1. CHAUFFAGE)`)
  - Si le contenu dépasse 74 caractères : **élargir la boîte** (76, 80+) — ne jamais passer à la ligne
  - Ne jamais supprimer les références techniques dans le titre (ex: "Ping HTTPS", "windrose-card")

- **TITRE SECONDAIRE** — Boîte coins carrés `┌─┐ / │ / └─┘`
  - Largeur : **37 caractères**
  - Texte en **MAJUSCULES**, numérotation officielle (1 à 9)

### 2. HEADERS EXPLICATION — EN-TÊTE OBLIGATOIRE

Juste sous la boîte ASCII, chaque fichier doit comporter ces 4 sections :

```yaml
#
# ## 📝 DESCRIPTION :
# Ce que fait le fichier.
#
# ## 🧮 CALCUL & SOURCES :
# Formules et entités sources.
#
# ## ⚠️ IMPORTANT (PIÈGES) :
# Points d'attention techniques.
#
# ## 🖥️ TABLEAU DE BORD (VIGNETTES PRINCIPALES) :
# Vignette(s) alimentée(s) par ce fichier (ex: L2C1 Énergie Générale).
```

### 3. CHAÎNE DE DÉPENDANCES — EN-TÊTE OBLIGATOIRE

Juste après `## 🧮 CALCUL & SOURCES :` et avant `## ⚠️ IMPORTANT`, insérer un tableau traçant la chaîne complète :

```yaml
# ## 🔗 CHAÎNE DE DÉPENDANCES :
#
# | MATÉRIEL        | CAPTEUR BRUT (source)              | CE FICHIER (unique_id)              | AVAL                    |
# |:----------------|:-----------------------------------|:------------------------------------|:------------------------|
# | [device/integ]  | sensor.nom_entite_source           | nom_unique_id_ce_fichier            | fichier_aval.yaml → L*C*|
```

**Règles du tableau :**
- **MATÉRIEL** : appareil physique ou intégration HA (ex: `NOUS SP (Z2M)`, `Hue Bridge`, `Ecojoko`, `Linky`)
- **CAPTEUR BRUT** : entité source exacte utilisée dans `source:` ou `entity_id:` du YAML
- **CE FICHIER** : `unique_id` exact de l'entité produite par ce fichier
- **AVAL** : fichier(s) qui consomment cette entité + vignette dashboard (ex: `P1_UM_AMHQ.yaml → L2C2`)
- Une ligne par entité produite
- Si la source est un autre sensor calculé (pas un device direct), indiquer `[calculé]` en MATÉRIEL

### 4. SLUG TERTIAIRE

- **Format** : `# --- unique_id_exact ---`
- **Règle absolue** : le slug doit être l'image **exacte** du `unique_id` de l'entité qui suit
- **Position** : obligatoire juste au-dessus de **chaque** bloc d'entité individuel
- **Utility_meter** : un slug **par entrée** (annuel, mensuel, hebdo, quotidien) — pas un slug groupé

### 5. NAME

- Format : `name: "Préfixe Nom Lisible Période"`
- **Majuscules initiales** sur chaque mot
- **Préfixe obligatoire** cohérent avec le pôle (ex: `"Genelec Appart Coût HP Quotidien"`)
- ⛔ Jamais de nom trop court ou sans préfixe (ex: ~~`"Conso Mini"`~~ → `"Genelec Appart Conso Mini 24h"`)

### 6. UNIQUE_ID

- Format : `unique_id: prefixe_nom_lisible_periode`
- Tout en **minuscules**, séparateurs **underscores**
- Doit décrire la même chose que le `name` (cohérence croisée obligatoire)
- Exemples : `genelec_appart_cout_hp_quotidien`, `clim_salon_energie_totale_kwh`

---

## 📏 RÈGLES DE STRUCTURATION GÉNÉRALE (YAML)
**Organisation des pôles, pièces et fichiers — Jamais pour les automations.**

### 1. LOGIQUE DE TRI (SÉPARATION STRICTE)
- **RÈGLE D'OR :** On ne mélange **JAMAIS** les types d'équipements (Pôles) au sein d'une même pièce.
- **MÉTHODE :** La structure suit d'abord le **PÔLE**, puis la **PIÈCE**.
- **ORDRE DES PÔLES (0 à 4) :**
    0. **ÉNERGIE GLOBALE** (Linky, Ecojoko, bilans généraux).
    1. **CHAUFFAGE & CLIMATISATION**
    2. **PRISES CONNECTÉES**
    3. **ÉCLAIRAGE**
    4. **GROUPE PRÉSENCE** (Wi-Fi, Réseau mobile, Localisation, Traceurs).

### 3. ORDRE OFFICIEL DES PIÈCES (INDEX 1 À 9)
Cette numérotation doit être suivie scrupuleusement au sein de chaque bloc de Pôle :
1. **ENTRÉE** | 2. **CELLIER** | 3. **TOILETTE** | 4. **SALON** | 5. **CUISINE** | 6. **COULOIR** | 7. **BUREAU** | 8. **SDB** | 9. **CHAMBRE**

### 4. NOMENCLATURE HORS-PIÈCES (SYSTÈME & DIVERS)
Pour tous les éléments qui ne sont pas rattachés à une pièce physique spécifique, l'indexation se fait par catégorie lettrée :

**[ M ] - MÉTÉO & ENVIRONNEMENT EXTERNE :**
- `M_01_meteo_alerte`
- `M_02_meteo_vent`
- `M_03_meteo_blitzortung`
- `M_04_tendances_th_ext_card`

**[ A ] - QUALITÉ DE L'AIR (Air quality) :**
- `A_01_AIR_QUALITY` — sensors stats 24h PM2.5 + tCOV (sensors/) + templates ppb tCOV (templates/)

**[ ST ] - SPEEDTEST (SpeedTest) :**
- `ST_01_SpeedTest` — capteurs Download / Upload / Ping depuis `sensor.speedtest_cli_data`

**[ S ] - STORES (Volets motorisés) :**
- `S_01_STORES` — templates d'état `store_salon_status` / `store_bureau_status` (HTML couleur)

**[ B ] - BP VIRTUEL / INTERRUPTEUR SDB :**
- `B1_01_inter_sdb` — `binary_sensor.radiateur_salle_de_bain_actif` (input_boolean → état)
- `BI_02_switch_inter_sdb` — `switch.inter_soufflant_salle_de_bain` (toggle via input_boolean)

**[ MP ] - MINI-PC (Températures système) :**
- `MP_01_sonde_température_mini-pc` — 6 sensors T° CPU/carte mère (thermal_zone → °C)

---

## 🛠️ RÈGLES DE CODAGE STRICTES

- **AUTOMATISATIONS (FORMATAGE)** : 
  - ⛔ **INTERDIT** : Jamais de tiret "`-`" devant le premier `alias` (Titre). Le code doit être fourni comme un bloc objet, pas un élément de liste.
  - ⛔ **INTERDIT** : Jamais d' `id:` au niveau global (laisser HA le gérer).
  - ✅ **OBLIGATOIRE** : `alias` en MAJUSCULES pour chaque sous-bloc (déclencheur/trigger, condition, action).
  - 🆗 **AUTORISÉ** : `id:` permis UNIQUEMENT à l'intérieur des déclencheurs (pour les ciblages d'actions).

- **MODIFICATIONS** : 
  - Annoter chaque ligne modifiée : `# "[L...] modif"`.
  - Bloc final obligatoire à la fin de la réponse : `# annotations_log:`.

---

## 🔔 STANDARDS DE NOTIFICATION (POCO X7 PRO & MONTRE)
**Cible matérielle : Poco X7 Pro couplé à Xiaomi Watch Lite (Écran carré, rendu émojis limité)**

1. **TITRE (`title`)** :
   - **Longueur Max** : **21 caractères** (Impératif pour lecture immédiate au poignet).
   - **Style** : MAJUSCULES recommandées pour l'alerte.
   
2. **CORPS DU MESSAGE (`message`)** :
   - **Encodage** : **TEXTE PUR (ASCII) UNIQUEMENT**.
   - ⛔ **INTERDICTION STRICTE** : Aucun émoji (🐛, ⚠️, 🔥) -> Remplacer par symboles ASCII (`!`, `[ ]`, `OK`, `>>`).
   - **Structure** : L'information critique doit être dans les **20 premiers caractères**.

3. **EXEMPLE VALIDE** :
   - Titre : `SDB : ARRET` (11 car.)
   - Message : `Minuteur 1h fini. RAZ OK.`

---

## 📋 RÈGLE DOCS VIGNETTES — DÉPENDANCES OBLIGATOIRES

**À chaque création ou modification d'une doc de vignette (`docs/L*`) :**

1. Remplir la section **ENTITÉS UTILISÉES — PROVENANCE COMPLÈTE** dans la doc (fichier source → entité)
2. **Mettre à jour `docs/DEPENDANCES_GLOBALES.md`** : compléter la chaîne de dépendances et passer le statut 🔲 → ✅
3. Mettre à jour la date en haut de `DEPENDANCES_GLOBALES.md`

> Référence : `docs/WORKFLOW_REBUILD.md` — section "Workflow création / modification d'une doc vignette"

---

## 🔌 DÉTAILS DES ÉQUIPEMENTS PAR PÔLE

### 0. Pôle Énergie Globale (Pôle 0)
- **Équipements** : Compteur Linky, Ecojoko.
- **Logique** : Centralisation des coûts globaux, des index totaux et des ratios (ex: Heures Creuses / Heures Pleines mensuel, coût journalier global).

### 1. Pôle Chauffage / Clim (Pôle 1)
- **4. SALON** : clim_salon_entree.
- **5. CUISINE** : radiateur_cuisine.
- **7. BUREAU** : clim_bureau.
- **8. SDB** : soufflant_sdb, seche_serv_sdb.
- **9. CHAMBRE** : clim_chambre.

### 2. Pôle Prises (Pôle 2)
- **1. ENTRÉE** : box_internet_entree, horloge_entree.
- **4. SALON** : pc_s_gege_salon, salon_chargeur_salon, tv_salon.
- **5. CUISINE** : micro_ondes_cuisine, lave_linge_cuisine, lave_vaisselle_cuisine, airfryer_cuisine, four_plaque_cuisine, frigo_cuisine, congel_cuisine.
- **7. BUREAU** : bureau_pc, fer_a_repasser_bureau.
- **9. CHAMBRE** : tete_de_lit_chambre, tv_chambre.

### 3. Pôle Éclairage (Pôle 3)
*Logique Physique (Ampoules) :*
- **1. ENTRÉE** : Hue White.
- **4. SALON** : Table: Hue White, Hue Ambiance 1, 2, 3, Hue Color 1.
- **5. CUISINE** : Hue White.
- **6. COULOIR** : Hue White.
- **7. BUREAU** : Play 1, 2, 3, Hue White 1, 2.
- **8. SDB** : Miroir Sonoff, Hue White.
- **9. CHAMBRE** : Hue White 1, 2, Hue Color Zone 1, 2.

*Logique de Somme (Zones) :*
- **ZONE 4. (5x) SALON** : [somme de] Table: Hue White, Hue Ambiance 1, 2, 3, Hue Color 1. (ex: eclairage_salon_5_*)
- **ZONE. ((3x) Entrée, cuisine & couloir) (APPART)** : [somme de] Hue White, Hue White, Hue White. (ex: eclairage_appart_3_*)
- **ZONE 5. (1x) CUISINE** : [somme de] Hue White. (ex: eclairage_cuisine_1_*)
- **ZONE. ((2x) Entrée & couloir) (APPART)** : [somme de] Hue White, Hue White. (ex: eclairage_appart_2_*)
- **ZONE 7. (5x) BUREAU** : [somme de] Play 1, 2, 3, Hue White, Hue White. (ex: eclairage_bureau_5_*)
- **ZONE 8. (2x) SDB** : [somme de] Miroir Sonoff, Hue White. (ex: eclairage_sdb_2_*)
- **ZONE 9. (4x) CHAMBRE** : [somme de] Hue White 1, 2, Hue Color Zone-1, Hue Color Zone-2. (ex: eclairage_chambre_4_*)

### 4. Pôle Groupe Présence (Pôle 4)
- **Équipements** : Téléphones mobiles (Poco X7 Pro, etc.), capteurs Wi-Fi (SSID/BSSID), réseau mobile.
- **Logique** : Centraliser les statuts de connexion pour déterminer la présence (Présent/Absent).

---

## 🌡️ STRATÉGIE THERMIQUE & MONITORING
*(Uniquement pour l'analyse des consommations électriques — cœur décisionnel Pôle 1)*

- **Sondes :** Thermostats SONOFF dans TOUTES les pièces + T° Extérieure (Balcon Nord).
- **Mode Absence :**
  - **Hiver** : 17°C par défaut — Si T° Ext < 10°C → 18°C — Si T° Ext < 8°C → 19°C.
  - **Été** : T° Cible = 28°C.
- **Logique "Cœur du Système" (T° Extérieure → Cible → Confort) :**

  ![Confort Cible Calcul Flow](https://github.com/user-attachments/assets/f18e24a2-1441-482b-af70-537a7b208e15)

---

## 🖥️ CARTOGRAPHIE DU TABLEAU DE BORD PRINCIPAL (MATRICE DES 18 VIGNETTES)
Cette matrice permet de cibler exactement quelle entité remonte dans quelle carte visuelle du Dashboard. Elle est indispensable pour la documentation interne des fichiers YAML.
Format : Ligne (L) / Colonne (C).

**LIGNE 1 : ENVIRONNEMENT & THERMIQUE**
- **L1C1** : Météo
- **L1C2** : Températures (Extérieure et 6 intérieures) avec humidité
- **L1C3** : Commandes Clim (incluant radiateur et soufflant)

**LIGNE 2 : CONSOMMATION ÉNERGÉTIQUE**
- **L2C1** : Conso Énergie Générale
- **L2C2** : Conso Énergie Clim / Radiateur / Soufflant
- **L2C3** : Conso Énergie Éclairage (Lampes)

**LIGNE 3 : COMMANDES & ACTIONNEURS**
- **L3C1** : Commandes Éclairage (Lampes)
- **L3C2** : Commandes Éco (Prises)
- **L3C3** : État des fenêtres + Commandes 2 stores

**LIGNE 4 : RÉSEAU & SYSTÈME**
- **L4C1** : *(supprimée — Freebox retirée du setup)*
- **L4C2** : Mini PC
- **L4C3** : Mises à jour HA

**LIGNE 5 : MAINTENANCE MATÉRIELLE**
- **L5C1** : Surveillance Batteries / Piles des équipements
- **L5C2** : Batterie du portail
- **L5C3** : Taille de la DB MariaDB (Lien Github au clic)

**LIGNE 6 : QUALITÉ & ALERTES**
- **L6C1** : Qualité de l'air (Appartement)
- **L6C2** : Pollution / Pollen (Extérieur)
- **L6C3** : Vigilance Eau (Restrictions)

---

## 🎨 RÉFÉRENTIEL UI — PALETTE DE COULEURS OFFICIELLES HA (HEX & RGB)

Indispensable pour la cohérence entre ApexCharts, Bubble-Card et Mushroom.

| État / Type   | HEX       | RGB             | Utilisation type      |
| :------------ | :-------- | :-------------- | :-------------------- |
| **Primary**   | `#03a9f4` | `3, 169, 244`   | Icônes HA, Titres     |
| **Success**   | `#0f9d58` | `15, 157, 88`   | Actif, Normal, OK     |
| **Warning**   | `#ff9800` | `255, 152, 0`   | Standby, Attention    |
| **Error**     | `#f44336` | `244, 67, 54`   | Alerte, Critique, Off |
| **Info**      | `#2196f3` | `33, 150, 243`  | Infos, Nuages, Réseau |
| **Inactive**  | `#44739e` | `68, 115, 158`  | Éteint, Absent        |
| **Active**    | `#fdd835` | `253, 216, 53`  | Éclairage, Chauffage  |
| **Text**      | `#212121` | `33, 33, 33`    | Polices, Bordures     |

---

## 🎨 RÉFÉRENTIEL UI — CARTES HACS ET NATIVES UTILISÉES

Cette liste sert de référence pour la création de nouveaux Dashboards afin de garantir la compatibilité système.

| Type             | Nom de la Carte                                  | Utilisation Principale                                  |
| :----------------| :------------------------------------------------| :------------------------------------------------------ |
| **Graph/Data**   | `apexcharts-card`                                | Graphiques énergie, moyennes glissantes, seuils couleur |
|                  | `mini-graph-card`                                | Tendances rapides (températures, humidité)              |
|                  | `plotly-graph`                                   | Analyse de données complexe                             |
|                  | `bar-card`                                       | Jauges de consommation et niveaux de batteries          |
|                  | `history-explorer-card`                          | Exploration interactive de l'historique                 |
| **UI/Design**    | `bubble-card`                                    | Navigation, Pop-ups par pièce, boutons tactiles         |
|                  | `mushroom-card`                                  | Éclairage (Mushroom Light), Titres, Chips d'état        |
|                  | `mod-card` (card-mod)                            | Personnalisation CSS avancée des cartes                 |
|                  | `layout-card`                                    | Structure des vues (Grid, Masonry)                      |
|                  | `stack-in-card` / `vertical-stack-in-card`       | Groupement de cartes sans bordures                      |
|                  | `swipe-card`                                     | Carrousels (Météo, Caméras)                             |
|                  | `auto-entities`                                  | Listes dynamiques (Fenêtres ouvertes, Piles faibles)    |
| **Spécialisées** | `enhanced-shutter-card`                          | Gestion visuelle des stores (Série 08)                  |
|                  | `tempometer-gauge-card`                          | Jauges de température et humidité pro                   |
|                  | `ring-tile-card`                                 | Indicateurs circulaires (Statut MariaDB, CPU)           |
|                  | `multiple-entity-row`                            | Multi-affichage sur une seule ligne d'entité            |
|                  | `text-divider-row`                               | Séparateurs de sections textuels                        |
|                  | `navbar-card`                                    | Barre de navigation personnalisée                       |
|                  | `linky-card`                                     | Suivi MyElectricalData (Compteur Linky)                 |
|                  | `rain-gauge-card`                                | Visualisation de la pluviométrie                        |
|                  | `uv-index-card`                                  | Affichage de l'indice UV (Série 01)                     |

---

## 🖥️ RÈGLES DE STRUCTURATION DES TEMPLATES D'INTERFACE (`ui_dashboard`)
Pour séparer la logique de calcul pur de la logique d'affichage, un sous-dossier `ui_dashboard` est utilisé dans les Pôles (ex: `P3_eclairage/ui_dashboard/`).

- **Usage strict** : Ce dossier est **exclusivement** réservé aux "Capteurs Modèles" (Templates) dont le seul but est de générer du contenu pour l'interface visuelle (les cartes sur le tableau de bord).
- **Contenu autorisé** : 
  - Regroupement textuel (ex: "3 lumières allumées", "Clim en mode Froid").
  - Formatage de couleurs ou d'icônes dynamiques pour les cartes.
- **Interdiction** : Ne **jamais** y placer de calculs d'énergie (`kWh`), de puissance (`W`) ou de durées (`DUT`).

---

## 📊 ARCHITECTURE MODULAIRE : 1 FONCTION = 1 FICHIER YAML
**L'approche monolithique est strictement interdite. La configuration est 100% éclatée et modulaire.**

**RÈGLE D'OR :** Chaque fonction, logique, calcul ou intégration doit posséder **son propre fichier `.yaml` dédié**, obligatoirement rangé dans le répertoire du Pôle correspondant (`P0` Énergie Globale, `P1` Chauffage & Clim, `P2` Prises, `P3` Éclairage, `P4` Groupe Présence, ou les catégories lettrées comme `M_` pour Météo).

### 1. DÉCOUPAGE PAR PÔLE (Exemples de structuration)
- **PÔLE 0 (Énergie Globale)** : Séparation stricte des entités. Un fichier pour les coûts, un autre pour le direct, etc. (ex: `01_UM_AMHQ_cout.yaml`, `02_UM_ecojoko_quotidien_direct.yaml` dans le dossier `Ecojoko`).
- **PÔLE 1 (Chauffage & Clim)** : Les calculs de puissance, les durées d'utilisation `[DUT]` et les moyennes `[AVG]` doivent avoir leurs propres fichiers sous le répertoire `P1_clim_chauffage`.
- **PÔLE 2 (Prises)** : Les calculs journaliers/mensuels de consommation et les lissages moyennes sont séparés (ex: dossier `P2_AVG`).
- **PÔLE 3 (Éclairage)** : Découpage obligatoire de la portée logique dans des fichiers distincts :
  - `..._1_UNITE.yaml` (Ampoules individuelles)
  - `..._2_ZONE.yaml` (Somme par pièce)
  - `..._3_TOTAL.yaml` (Somme globale de l'appartement)
- **PÔLE 4 (Groupe Présence)** : Séparation entre la logique de détection (Wi-Fi/Réseau mobile) et la carte d'affichage. Deux fichiers distincts sous `P4_groupe_presence` :
  - `01_phones_wifi_cellular_card_autom.yaml` (Templates d'affichage — carte état des téléphones)
  - `02_logique_wifi_cellular.yaml` (Logique de calcul — déduction présence/absence)

### 2. CONVENTION DE NOMMAGE DES FICHIERS
- **Préfixe Pôle** : Le fichier doit toujours commencer par son pôle (ex: `P2_...` ou `M_...`).
- **Type d'entité** : Indiquer clairement la nature du contenu (`UM` pour Compteur de services/Utility Meter, `AVG` pour moyennes, `kWh` pour intégration).
- **Le Standard "AMHQ"** : Si le fichier gère des cycles temporels multiples, utiliser l'acronyme `AMHQ` (Annuel, Mensuel, Hebdo, Quotidien) dans le nom du fichier pour raccourcir (ex: `P3_UM_AMHQ_2_ZONE.yaml`).

### 3. TITRAGE ET DOCUMENTATION INTERNE
- Chaque fichier commence par une boîte ASCII arrondie (titre principal) en ligne 1.
- Les 5 critères de conformité (bordure, headers, slug, name, unique_id) sont définis dans **RÈGLES DES FICHIERS YAML — CRITÈRES DE CONFORMITÉ** ci-dessus.

---

## 🌳 ARBORESCENCE — DOSSIER DE TRAVAIL LOCAL (ReBuild)

```text
ReBuild/                                         (dossier de travail local — C:\Users\Berry Swann\Documents\HA\ReBuild\)
├── CLAUDE.md                                    (instructions IA — contexte projet)
├── SYNC_REPORT.md                               (rapport de synchronisation GitHub ↔ local)
├── secrets.yaml                                 (identifiants HA — NE JAMAIS synchroniser sur GitHub)
│
├── Dashboard/                                   (YAML complets du dashboard + saves)
│   ├── dashboard_2026-04-15.yaml
│   └── [sous-dossiers par vignette/page — voir règle ci-dessous]
│
├── docs_dashboard/                              (tout ce qui concerne le dashboard HA config)
│   ├── TREE_CORRIGE/                            (← image exacte du GitHub re-build — dernière sync: 2026-04-19)
│   │   ├── sensors/                             (13 fichiers — intégrations kWh, mini/maxi, qualité air)
│   │   ├── templates/                           (34 fichiers — calculs, AVG, UI, météo, présence, stores, speedtest)
│   │   ├── utility_meter/                       (10 fichiers — compteurs AMHQ)
│   │   ├── command_line/                        (3 fichiers — météo, speedtest, github_maintenance)
│   │   ├── input_booleans/                      (5 fichiers — P1, P3, P4)
│   │   ├── input_number/                        (1 fichier)
│   │   └── [root]                               (configuration.yaml, groups.yaml, scripts.yaml, shell_command.yaml, sql.yaml, scenes.yaml, input_button.yaml, input_datetime.yaml, input_select.yaml, automations.yaml, #*.yaml ×4)
│   ├── TREE_ORIGINE/                            (snapshot GitHub de référence — état avant corrections)
│   │   ├── sensors/
│   │   ├── templates/
│   │   ├── utility_meter/
│   │   └── ...
│   └── docs/                                    (documentation vignettes + dépendances)
│
├── docs_automations/                            (tout ce qui concerne les automations)
│   ├── TREE_CORRIGE/                            (← SOURCE DE VÉRITÉ — coller dans HA UI un par un)
│   │   ├── P1_clim_chauffage/                   (13 fichiers — clim, gardien, notifs)
│   │   ├── P1_cuisine/                          (2 fichiers — radiateur)
│   │   ├── P1_sdb/                              (1 fichier — minuterie sèche-serv 2h ✅)
│   │   ├── P2_prises/                           (6 fichiers — PC, TV, prises éco)
│   │   ├── P3_eclairage/                        (1 fichier — lumière entrée)
│   │   ├── backup/                              (4 fichiers — git hourly/weekly/alerte/démarrage)
│   │   ├── energie/                             (1 fichier — surveillance gros électro HP)
│   │   ├── meteo/                               (5 fichiers — alertes, foudre, tendances)
│   │   ├── stores/                              (2 fichiers — salon, bureau)
│   │   └── systeme/                             (4 fichiers — diag, purge DB, VSCode, watchdog piles, Z2M)
│   ├── TREE_ORIGINE/                            (snapshot avant corrections — référence historique)
│   └── docs/                                    (INDEX_AUTOMATIONS, TRIAGE, PROD_vs_REBUILD_DIFF, IDs REF...)
│
└── docs_scripts/                                (tout ce qui concerne les scripts HA)
    ├── TREE_CORRIGE/                            (scripts YAML corrigés)
    ├── TREE_ORIGINE/                            (scripts YAML originaux)
    └── docs/                                    (SCRIPTS_CLIM_ON_OFF.md)
```

> **Note :** La documentation vignettes (18 vignettes) est dans `docs_dashboard/docs/`

```text
docs_dashboard/docs/                             (documentation — vignettes, pages, guides — 17 vignettes actives)
    ├── IA/
    │   └── IA_CONTEXT_BASE.md
    ├── CONFIG_ROOT/
    │   └── CONFIG_ROOT.md
    ├── L1C1_METEO/
    │   ├── L1C1_VIGNETTE_METEO.md
    │   ├── PAGE_METEO.md
    │   └── TUTO_IMAGES_ALERTES_METEO_FRANCE.md
    ├── L1C2_TEMPERATURES/
    │   ├── L1C2_VIGNETTE_TEMPERATURES.md
    │   └── PAGE_TEMPERATURES.md
    ├── L1C3_CLIM/
    │   ├── L1C3_VIGNETTE_CLIM.md
    │   └── PAGE_CLIM.md
    ├── L2C1_ENERGIE/
    │   ├── L2C1_VIGNETTE_ENERGIE.md
    │   ├── PAGE_ENERGIE.md
    │   ├── PAGE_ENERGIE_MENSUEL.md
    │   ├── PAGE_ENERGIE_TEMPS_REEL.md
    │   └── COULEURS_PRISES_PAR_PIECE.md
    ├── L2C2_ENERGIE_CLIM/
    │   ├── L2C2_VIGNETTE_ENERGIE_CLIM.md
    │   └── PAGE_ENERGIE_CLIM.md
    ├── L2C3_ENERGIE_ECLAIRAGE/
    │   ├── L2C3_VIGNETTE_ECLAIRAGE.md
    │   ├── PAGE_ENERGIE_ECLAIRAGE.md
    │   └── COULEURS_ECLAIRAGE_PAR_PIECE.md
    ├── L3C1_ECLAIRAGE/
    │   ├── L3C1_VIGNETTE_ECLAIRAGE.md
    │   └── PAGE_ECLAIRAGE.md
    ├── L3C2_PRISES/
    │   ├── L3C2_VIGNETTE_PRISES.md
    │   └── PAGE_PRISES.md
    ├── L3C3_STORES/
    │   ├── L3C3_VIGNETTE_STORES.md
    │   └── PAGE_STORES.md
    ├── L4C1_FREEBOX/                                ⚠️ Obsolète — Freebox supprimée du setup
    │   ├── L4C1_VIGNETTE_FREEBOX.md
    │   └── PAGE_FREEBOX.md
    ├── L4C2_MINI_PC/
    │   ├── L4C2_VIGNETTE_MINI_PC.md
    │   ├── PAGE_RASPI.md                        (page transitoire RPi4 — conservée jusqu'à migration)
    │   └── PAGE_MINI_PC.md                      (page définitive Mini PC Intel NUC — à déployer après migration)
    ├── L4C3_MAJ_HA/
    │   ├── L4C3_VIGNETTE_MAJ.md
    │   └── PAGE_MAJ.md
    ├── L5C1_PILES_BATTERIES/
    │   ├── L5C1_VIGNETTE_BATTERIES.md
    │   └── PAGE_BATTERIES.md
    ├── L5C2_BATTERIES_PORTABLES/
    │   ├── L5C2_VIGNETTE_BATTERIES_PORTABLES.md
    │   └── PAGE_BATTERIES_PORTABLES.md
    ├── L5C3_MARIADB/
    │   ├── L5C3_VIGNETTE_MARIADB.md
    │   └── PAGE_SYSTEME.md
    ├── L6C1_AIR_QUALITE/
    │   ├── L6C1_VIGNETTE_AIR_QUALITE.md
    │   └── PAGE_AIR_QUALITE.md
    ├── L6C2_POLLUTION_POLLEN/
    │   ├── L6C2_VIGNETTE_POLLUTION_POLLEN.md
    │   └── PAGE_POLLUTION_POLLEN.md
    ├── L6C3_VIGIEAU/
    │   ├── L6C3_VIGNETTE_VIGIEAU.md
    │   └── PAGE_VIGIEAU.md
    ├── HOME PAGE/
    │   ├── PAGE_HOME.md
    │   └── VIGNETTE_WIFI_PRESENCE.md
    ├── DEPENDANCES_GLOBALES.md                  (chaîne complète de dépendances — toutes vignettes)
    ├── WORKFLOW_REBUILD.md                      (workflow création/modification doc vignette)
    └── _TEMPLATE_DOC.md
```

---

## 📋 RÈGLE DASHBOARD/ — VERSIONING DES VIGNETTES ET PAGES

> S'applique à tout YAML créé ou modifié pour le dashboard (vignette, page, carte).

### Convention de nommage

| Type | Format | Exemple |
|:-----|:-------|:--------|
| Dashboard complet | `Dashboard_YYYY_MM_DD.yaml` | `Dashboard_2026_04_19.yaml` |
| Vignette | `vignette_[id]_YYYY-MM-DD.yaml` | `vignette_L2C1_energie_2026-04-19.yaml` |
| Page | `page_[id]_YYYY-MM-DD.yaml` | `page_L2C1_energie_2026-04-19.yaml` |
| Carte isolée | `card_[nom]_YYYY-MM-DD.yaml` | `card_energie_home_2026-04-19.yaml` |

> **Règle d'auto-correction :** si un fichier existant est mal nommé (casse incorrecte, extension `.yalm`, underscores/tirets incohérents), le renommer immédiatement selon la convention ci-dessus.

### Principe
- À chaque création ou modification d'une vignette/page, créer un **sous-dossier nommé par vignette** dans `Dashboard/` (ex: `L1C1_Météo/`, `L2C1_Energie/`, `PAGE_Clim/`).
- Placer le fichier YAML dedans avec la **date en suffixe** selon la convention ci-dessus.
- **Maximum 3 versions** par sous-dossier — pas plus.

### Gestion des versions
```
Dashboard/
└── L1C1_Météo/
    ├── L1C1_meteo_2026-04-10.yaml   ← version 1 (la plus ancienne)
    ├── L1C1_meteo_2026-04-15.yaml   ← version 2
    └── L1C1_meteo_2026-04-19.yaml   ← version 3 (la plus récente)
```

### Règle des 3 versions
- S'applique **uniquement aux vignettes et pages individuelles** — PAS aux dashboards complets.
- Les dashboards complets (`Dashboard_COMPLET/`) sont tous conservés sans limite.
- Si une **4ème version de vignette/page** doit être ajoutée → **demander l'autorisation avant de supprimer la plus ancienne**.
- Raison : revenir en arrière sur un YAML dashboard peut être complexe.
- Format de la demande : *"Je vais supprimer `L1C1_meteo_2026-04-10.yaml` pour ajouter la nouvelle version. OK ?"*

---

## 🌳 ARBORESCENCE — STRUCTURE HA EN PRODUCTION (/config/)

```text
/config/                                         (racine — fichiers de configuration globaux)
├── configuration.yaml                           (point d'entrée HA : includes, intégrations, packages)
├── automations.yaml                             (toutes les automations — géré via UI + éditeur YAML)
├── scripts.yaml                                 (séquences d'actions réutilisables déclenchables manuellement)
├── scenes.yaml                                  (états prédéfinis multi-entités : ambiances, modes)
├── camera.yaml                                  (entités caméra : command_line → images vigilance Météo France)
├── input_button.yaml                            (boutons virtuels helpers : déclencheurs manuels dans l'UI)
├── groups.yaml                                  (groupes d'entités : regroupement logique pour affichage/automations)
├── shell_command.yaml                           (commandes shell appelables depuis HA : scripts bash, wget, etc.)
├── sql.yaml                                     (capteurs SQL : requêtes sur MariaDB — taille DB, stats)
├── #sensors.yaml                                (désactivé — remplacé par /config/sensors/)
├── #templates.yaml                              (désactivé — remplacé par /config/templates/)
└── #utility_meter.yaml                          (désactivé — remplacé par /config/utility_meter/)
/config/utility_meter
├── P0_Energie_total
│   └── Genelec_appart
│       ├── 01_UM_AMHQ.yaml
│       └── 02_UM_genelec_appart_HPHC_AMHQ.yaml
├── P1_clim_chauffage
│   └── P1_UM_AMHQ.yaml
├── P2_prise
│   ├── P2_UM_AMHQ_prises.yaml
│   ├── P2_UM_AMHQ_veilles.yaml
│   └── P2_UM_AMHQ_mini_pc.yaml
├── P3_eclairage
│   ├── P3_UM_AMHQ_1_UNITE.yaml
│   ├── P3_UM_AMHQ_2_ZONE.yaml
│   └── P3_UM_AMHQ_3_TOTAL.yaml
└── meteo
    └── M_03_meteo_UM_blitzortung.yaml
/config/templates
├── P0_Energie_total_diag
│   ├── Diag
│   │   ├── diag_conso_jour_en_cours.yaml
│   │   ├── diag_conso_mois_en_cours.yaml
│   │   └── diag_conso_hebdomadaire_en_cours.yaml
│   ├── Genelec_appart
│   │   ├── 01_genelec_appart_AMHQ_cost.yaml
│   │   ├── 02_ratio_hp_hc.yaml
│   │   └── 03_AVG_genelec_appart.yaml
│   ├── Linky
│   │   └── MyElectricalData.yaml
│   └── total par poste_7
│       └── total_par_poste_7.yaml               (puissance instantanée × 7 pôles fonctionnels)
├── P1_clim_chauffage
│   ├── P1_01_MASTER
│   │   ├── P1_01_clim_logique_system_autom.yaml
│   │   ├── P1_02_automation_message_clim_7h30_21h.yaml
│   │   └── P1_03_automation message clim 21h 7h30.yaml
│   ├── P1_AVG
│   │   ├── P1_AVG.yaml
│   │   └── P1_AVG_TOTAL_AMHQ.yaml
│   ├── P1_TOTAL
│   │   └── P1_TOTAL_AMHQ.yaml                   (agrégat total P1 — AMHQ)
│   ├── P1_DUT_TOTAL
│   │   └── P1_DUT_TOTAL_SDB.yaml                (somme DUT soufflant + sèche-serv)
│   └── P1_ui_dashboard
│       └── P1_ui_dashboard.yaml                 (*_power_status / *_etat / affichage)
├── P2_prise
│   ├── P2_AVG
│   │   ├── P2_AVG_AMHQ_prises.yaml
│   │   ├── P2_AVG_AMHQ_veilles.yaml
│   │   └── P2_AVG_AMHQ_mini_pc.yaml
│   ├── P2_I_all_standby_power
│   │   └── P2_current_all_standby.yaml
│   └── P2_ui_dashboard
│       └── P2_ui_dashboard.yaml                 (lave_linge_en_cours / lave_vaisselle_en_cours — seuils 5W/50W)
├── P3_eclairage
│   ├── P3_POWER                                 (remplace P3_01_somme_par_piece.yaml — obsolète)
│   │   ├── P3_POWER_1_TOTAL_UNITE.yaml
│   │   ├── P3_POWER_2_TOTAL_MULTI_ZONE.yaml
│   │   └── P3_POWER_3_TOTAL_ZONE.yaml
│   ├── P3_AVG
│   │   ├── P3_AVG_AMHQ_1_UNITE.yaml
│   │   ├── P3_AVG_AMHQ_2_ZONE.yaml
│   │   └── P3_AVG_AMHQ_3_TOTAL.yaml
│   └── ui_dashboard
│       └── etats_status.yaml
├── P4_groupe_presence
│   ├── 01_phones_wifi_cellular_card_autom.yaml
│   └── 02_logique_wifi_cellular.yaml
├── Air_quality                                  ([ A ] — catégorie lettrée)
│   └── A_01_AIR_QUALITY.yaml                    (templates ppb tCOV × 3 pièces)
├── SpeedTest                                    ([ ST ] — catégorie lettrée)
│   └── ST_01_SpeedTest.yaml                     (Download / Upload / Ping depuis speedtest_cli_data)
├── Stores                                       ([ S ] — catégorie lettrée)
│   └── S_01_STORES.yaml                         (store_salon_status + store_bureau_status)
├── meteo
│   ├── M_01_meteo_alertes_card.yaml
│   ├── M_02_meteo_vent_vence_card.yaml
│   ├── M_03_meteo_blitzortung.yaml
│   ├── M_04_tendances_th_ext_card.yaml
│   └── M_05_cycle_solaire.yaml
├── Inter_BP_Virtuel                             ([ B ] — catégorie lettrée)
│   ├── P1
│   │   └── P1_BV_01_SW_inter_souflant_sdb.yaml  (switch soufflant SDB — input_boolean → toggle)
│   └── P3
│       ├── P3_BV_01_inter_smorig_salon.yaml     (inter lumière SMORIG salon)
│       └── P3_BV_02_inter_rodret_salon.yaml     (inter lumière RODRET salon)
├── Mini-PC                                      ([ MP ] — catégorie lettrée)
│   └── MP_01_sonde_température_mini-pc.yaml     (6 sensors T° CPU/carte mère)
└── utilitaires
    ├── jour_nuit.yaml
    ├── Mise_a_jour_home_assistant.yaml
    └── nb_fenetre_ouvert_ferme_autom.yaml       (nbre_de_fenetres_ouvertes/fermees ×2)
/config/sensors
├── P0_Energie_total_min_maxi_diag
│   ├── P0_Genelec_appart
│   │   └── P0_kWh_genelec_appart.yaml           (Riemann kWh — index cumulatif Genelec appart)
│   └── P0_Genelec_appart_mini_maxi
│       └── P0_MINI_MAXI_AVG_Genelec_appart.yaml (stats min/max AVG — puissance W Genelec)
├── Air_quality                                  ([ A ] — catégorie lettrée)
│   └── A_01_AIR_QUALITY.yaml                    (stats mean 24h PM2.5 + tCOV × 3 pièces)
├── P1_clim_chauffage
│   ├── P1_DUT
│   │   └── P1_DUT_clim_chauffage.yaml           (history_stats DUT × 6 équipements P1)
│   └── P1_kWh
│       └── P1_kWh_clim_chauffage.yaml           (Riemann kWh — sources NOUS smart plugs P1)
├── P2_prise
│   ├── P2_kWh_prises.yaml
│   ├── P2_kWh_veilles.yaml
│   └── P2_Wh_mini_pc.yaml                          (Riemann Wh — intentionnel, sans unit_prefix:k → AVG formule conso/h)
├── P3_eclairage
│   ├── P3_kWh_1_UNITE.yaml
│   ├── P3_kWh_2_ZONE.yaml
│   └── P3_kWh_3_TOTAL.yaml
└── meteo
    └── M_03_meteo_sensors_blitzortung.yaml
```

---

## 🔗 INDEX INTÉGRAL DES FICHIERS SOURCES (RAW GITHUB)
Dépôt Re-build : https://github.com/BerrySwann/home_assistant_re-build

### 📂 UTILITY METER

**Pôle 0 - Énergie Globale**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P0_Energie_total/Genelec_appart/01_UM_AMHQ.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P0_Energie_total/Genelec_appart/02_UM_genelec_appart_HPHC_AMHQ.yaml

**Pôle 1 - Chauffage & Clim**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P1_clim_chauffage/P1_UM_AMHQ.yaml

**Pôle 2 - Prises**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P2_prise/P2_UM_AMHQ_prises.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P2_prise/P2_UM_AMHQ_veilles.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P2_prise/P2_UM_AMHQ_mini_pc.yaml

**Pôle 3 - Éclairage**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P3_eclairage/P3_UM_AMHQ_1_UNITE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P3_eclairage/P3_UM_AMHQ_2_ZONE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/P3_eclairage/P3_UM_AMHQ_3_TOTAL.yaml

**Météo**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/utility_meter/meteo/M_03_meteo_UM_blitzortung.yaml

### 📂 TEMPLATES

**Pôle 0 - Diag & Énergie Globale**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Diag/diag_conso_jour_en_cours.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Diag/diag_conso_mois_en_cours.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Diag/diag_conso_hebdomadaire_en_cours.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Genelec_appart/01_genelec_appart_AMHQ_cost.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Genelec_appart/02_ratio_hp_hc.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Genelec_appart/03_AVG_genelec_appart.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/Linky/MyElectricalData.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P0_Energie_total_diag/total%20par%20poste_7/total_par_poste_7.yaml

**Pôle 1 - Chauffage & Clim**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_01_MASTER/P1_01_clim_logique_system_autom.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_01_MASTER/P1_02_automation_message_clim_7h30_21h.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_01_MASTER/P1_03_automation%20message%20clim%2021h%207h30.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_AVG/P1_AVG.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_AVG/P1_AVG_TOTAL_AMHQ.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_TOTAL/P1_TOTAL_AMHQ.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_DUT_TOTAL/P1_DUT_TOTAL_SDB.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P1_clim_chauffage/P1_ui_dashboard/P1_ui_dashboard.yaml

**Pôle 2 - Prises**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_prises.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_veilles.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P2_prise/P2_AVG/P2_AVG_AMHQ_mini_pc.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P2_prise/P2_I_all_standby_power/P2_current_all_standby.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P2_prise/P2_ui_dashboard/P2_ui_dashboard.yaml

**Pôle 3 - Éclairage & UI**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/P3_POWER/P3_POWER_1_TOTAL_UNITE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/P3_POWER/P3_POWER_2_TOTAL_MULTI_ZONE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/P3_POWER/P3_POWER_3_TOTAL_ZONE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_1_UNITE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_2_ZONE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/P3_AVG/P3_AVG_AMHQ_3_TOTAL.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P3_eclairage/ui_dashboard/etats_status.yaml

**Pôle 4 - Groupe Présence**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P4_groupe_presence/01_phones_wifi_cellular_card_autom.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/P4_groupe_presence/02_logique_wifi_cellular.yaml

**Météo**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/meteo/M_01_meteo_alertes_card.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/meteo/M_02_meteo_vent_vence_card.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/meteo/M_03_meteo_blitzortung.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/meteo/M_04_tendances_th_ext_card.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/meteo/M_05_cycle_solaire.yaml

**Qualité de l'Air [ A ]**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/Air_quality/A_01_AIR_QUALITY.yaml

**SpeedTest [ ST ]**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/SpeedTest/ST_01_SpeedTest.yaml

**Stores [ S ]**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/Stores/S_01_STORES.yaml

**Utilitaires**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/utilitaires/jour_nuit.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/utilitaires/Mise_a_jour_home_assistant.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/utilitaires/nb_fenetre_ouvert_ferme_autom.yaml

**Inter BP Virtuel [ B ]**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/Inter_BP_Virtuel/P1/P1_BV_01_SW_inter_souflant_sdb.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/Inter_BP_Virtuel/P3/P3_BV_01_inter_smorig_salon.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/Inter_BP_Virtuel/P3/P3_BV_02_inter_rodret_salon.yaml

**Mini-PC [ MP ]**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/templates/Mini-PC/MP_01_sonde_temp%C3%A9rature_mini-pc.yaml

### 📂 SENSORS

**Pôle 0 - Diag & Énergie Globale**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart/P0_kWh_genelec_appart.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P0_Energie_total_min_maxi_diag/P0_Genelec_appart_mini_maxi/P0_MINI_MAXI_AVG_Genelec_appart.yaml

**Qualité de l'Air [ A ]**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/Air_quality/A_01_AIR_QUALITY.yaml

**Pôle 1 - Chauffage & Clim**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P1_clim_chauffage/P1_kWh/P1_kWh_clim_chauffage.yaml

**Pôle 2 - Prises**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P2_prise/P2_kWh_prises.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P2_prise/P2_kWh_veilles.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P2_prise/P2_Wh_mini_pc.yaml

**Pôle 3 - Éclairage**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P3_eclairage/P3_kWh_1_UNITE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P3_eclairage/P3_kWh_2_ZONE.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/P3_eclairage/P3_kWh_3_TOTAL.yaml

**Météo**
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/sensors/meteo/M_03_meteo_sensors_blitzortung.yaml

### 📂 COMMAND_LINE
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/command_line/meteo/carte_meteo_france.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/command_line/speedtest/speedtest.yaml
- https://raw.githubusercontent.com/BerrySwann/home_assistant_re-build/main/command_line/github_maintenance/github_maintenance.yaml

---

## 👥 RÉFÉRENTIEL P4 — VALEURS FORMATÉES : `sensor.groupe` & `sensor.presence`

> Source : `templates/P4_groupe_presence/02_logique_wifi_cellular.yaml`
> Réseau cible : `'Module B.E.R.Y.L. [GG-5.0]'` ou `'Module B.E.R.Y.L. [GG-2.4]'`

### sensor.groupe — Logique d'automatisation

Utilisé par les automations (clim, volets, mode éco). Valeur = code du groupe actif.

| Valeur       | Signification                                     | Condition                              |
| :----------- | :------------------------------------------------ | :------------------------------------- |
| `groupe_1`   | **Absent** — personne sur le réseau cible         | ni Mamour ni Eric en WiFi cible        |
| `groupe_2`   | **Mamour seule** — Eric absent                    | Mamour en WiFi cible, Eric hors réseau |
| `groupe_3`   | **Eric seul** — Mamour absente                    | Eric en WiFi cible, Mamour hors réseau |
| `groupe_4`   | **Tous les deux** — présence simultanée           | Mamour ET Eric en WiFi cible           |

### sensor.presence — Affichage dashboard / en-tête notifications

Utilisé dans les messages de notification (`{{ states('sensor.presence') }}`).
Format : `[X: statut_X/statut_Y]` où statut = `WIFI` | `CELL` | `WIFI_!?`

| Valeur affichée          | Situation                                                        |
| :----------------------- | :--------------------------------------------------------------- |
| `[2] en [WIFI]`          | Les deux sur le réseau domestique                                |
| `[2] en [CELL]`          | Les deux en cellulaire                                           |
| `[2] en [WIFI_!?]`       | Les deux en WiFi, mais sur un autre réseau que le domestique     |
| `[Mamour: WIFI/CELL]`    | Mamour présente (domestique), Eric en cellulaire                 |
| `[Mamour: WIFI/WIFI_!?]` | Mamour présente (domestique), Eric sur un autre WiFi             |
| `[Eric: WIFI/CELL]`      | Eric présent (domestique), Mamour en cellulaire                  |
| `[Eric: WIFI/WIFI_!?]`   | Eric présent (domestique), Mamour sur un autre WiFi              |
| `[CELL / WIFI_!?]`       | Aucun sur le domestique — Mamour=CELL, Eric=autre WiFi           |
| `[WIFI_!? / CELL]`       | Aucun sur le domestique — Mamour=autre WiFi, Eric=CELL           |

> **Note ordre d'affichage :** `[Eric: e_stat/m_stat]` → Eric en premier, Mamour en second.

**Légende des statuts réseau :**

| Code       | Signification                                              |
| :--------- | :--------------------------------------------------------- |
| `WIFI`     | Connecté au réseau domestique (Beryl GG-5.0 ou GG-2.4)    |
| `WIFI_!?`  | Connecté à un autre WiFi (bureau, voisin, hotspot…)        |
| `CELL`     | Connexion cellulaire (4G/5G) — hors WiFi                   |

---

## 📲 RÉFÉRENTIEL NOTIFICATIONS — FORMATS PAR AUTOMATION

> Inventaire exhaustif des `notify.mobile_app_eric` dans `docs_automations/TREE_CORRIGE/`.
> *(Titre absent = pas de `title:` dans le YAML — message seul envoyé)*

### 🌡️ P1 — CLIM CHAUFFAGE

**A0 — Clim Jour (07h30 → 21h00)**

| Titre | Message | Contexte |
| :---- | :------ | :------- |
| `[AJ] ATTENTE CAPTEURS` | `Essai n°{{ repeat.index }}... Les capteurs de jour ne sont pas prêts. Pause 30s.` | Boucle démarrage |
| `[AJ] CLIM JOUR COUPÉE` | `La fenêtre du [Salon/Cuisine/Bureau/Chambre] a été ouverte.` | Ouverture fenêtre |
| `[AJ] {{ states('sensor.presence') }}` | `[éCO HEAT]  Les 3 Clims : {{ temp_eco_c }}° (Absent)` | Résumé — absent |
| `[AJ] {{ states('sensor.presence') }}` | `Mode : {{ mode_saison \| upper }}  Salon: X°  Bureau: Y°  Chambre: Z°` | Résumé — présent |

**B0 — Clim Nuit (21h00 → 07h30)**

| Titre | Message | Contexte |
| :---- | :------ | :------- |
| `[AN] ATTENTE CAPTEURS` | `Essai n°{{ repeat.index }}... Les capteurs de nuit ne sont pas prêts. Pause 30s.` | Boucle démarrage |
| `[AN] CLIM NUIT COUPÉE` | `La fenêtre du [Salon/Cuisine/Bureau/Chambre] a été ouverte.` | Ouverture fenêtre |
| `[AN] {{ states('sensor.presence') }}` | `[éCO HEAT]  Les 3 Clims : {{ temp_eco_c }}° (Absent)` | Résumé — absent |
| `[AN] {{ states('sensor.presence') }}` | `Mode : {{ mode_saison \| upper }} (NUIT)  Salon: X°  Bureau: Y°  Chambre: Z°` | Résumé — présent |

**C — Gardien Éco (CLIM OFF)**

| Titre | Message |
| :---- | :------ |
| `Delta T° < -1°C` | `Les clim ont été éteintes. ({{ delta }}°C)  T° Ext.: ({{ t_ext }}°C)  Seuil réglé à: {{ seuil }}°C.` |

**D — Notif Temp Jour** *(relai sensor)*

| Titre | Message |
| :---- | :------ |
| `[Automa. Notif. Jrs]` | `{{ states('sensor.message_clim_personnalise_7h30_21h00') }}` |
| `[ANN] Erreur Capteurs` | `Erreur : Un capteur TENDANCE est indisponible ! Vérifiez les dépendances.` |

Structure du message relayé (`sensor.message_clim_personnalise_7h30_21h00`) — 3 lignes assemblées :
```
[sensor.presence]          ← en-tête (ex: [2] en [WIFI])
T°Ext Up/Down/stable -> X° ← tendance T° extérieure
[BLOC MODE]                ← cf. tableau ci-dessous
```

| `[BLOC MODE]` | Condition |
| :------------ | :-------- |
| `[UNITS OFF]` | Aucune des 3 prises clim alimentée |
| `[ECO HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_1 + heat (absent) |
| `[COOL]\nSalon X°\nBureau X°\nChambre X°` | groupe_1/2/3/4 + cool |
| `[HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_2/3/4 + heat (présent) |
| `[FAN ONLY]\nSalon [FAN/OFF]\nBureau [FAN/OFF]\nChambre [FAN/OFF]` | tous groupes + fan_only |
| `[OFF]` *(par prise)* | Prise individuelle coupée — remplace la température |

**E — Notif Temp Nuit** *(relai sensor)*

| Titre | Message |
| :---- | :------ |
| `[Automa. Notif. Nuit]` | `{{ states('sensor.message_clim_personnalise_21h00_7h30') }}` |
| `[ANN] Erreur Capteurs` | `Erreur : Un capteur TENDANCE est indisponible ! Vérifiez les dépendances.` |

Structure du message relayé (`sensor.message_clim_personnalise_21h00_7h30`) — 3 lignes assemblées :
```
[sensor.presence]          ← en-tête (ex: [2] en [WIFI])
T°Ext Up/Down/stable -> X° ← tendance T° extérieure
[BLOC MODE]                ← cf. tableau ci-dessous
```

| `[BLOC MODE]` | Condition |
| :------------ | :-------- |
| `[UNITS OFF]` | Aucune des 3 prises clim alimentée |
| `[ECO HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_1 + heat (absent) |
| `[COOL]\nSalon X°\nBureau X°\nChambre X°` | groupe_1 + cool (absent) |
| `[HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_2/3/4 + heat — T° nuit uniforme |
| `[COOL]\nSalon X°\nBureau X°\nChambre X°` | groupe_2/3/4 + cool — T° nuit uniforme |
| `[FAN ONLY]\nSalon [FAN/OFF]\nBureau [FAN/OFF]\nChambre [FAN/OFF]` | tous groupes + fan_only |
| `[OFF]` *(par prise)* | Prise individuelle coupée — remplace la température |

> **Différence Jour/Nuit :** la nuit, groupe_2/3/4 utilisent tous `temp_nuit` uniforme (pas de T° personnalisée par personne).

**F — Notif Fermeture Fenêtres**

| Titre | Message |
| :---- | :------ |
| `Fermeture en cours` | `La fenêtre du/de la [Salon/Cuisine/Bureau/Chambre] a été fermée. [+ Toutes les fenêtres sont maintenant fermées.]` |

**G — Arrêt Clim Notif**

| Titre | Message |
| :---- | :------ |
| `ARRÊT CLIM` | `La clim. [du Salon / du Bureau / de la Chambre] a été coupée.` |

**H — Notif Changement Mode**

| Titre | Message |
| :---- | :------ |
| `CHANGEMENT DE MODE` | `Le mode a changé pour: {{ states('sensor.mode_ete_hiver_etat') \| upper }}` |

**I — Debug Force Mode (WATCHDOG)**

| Titre | Message |
| :---- | :------ |
| `⛔ SÉCURITÉ CLIM` | `Tentative de démarrage interdite (Prise coupée ou Arrêt en cours). Retour forcé à OFF pour : - [nom clim]` |
| `🔧 CORRECTION MODE` | `Mauvais mode détecté. Correction vers {{ mode_saison \| upper }} pour : - [nom clim]` |

**J — Synchro Notif Prise Coupée**

| Titre | Message |
| :---- | :------ |
| `CLIM COUPÉE` | `La prise extérieure [du Salon / du Bureau / de la Chambre] vient d'être éteinte.` |

**L — Debug Notif Message Clim** *(DEBUG — sans titre)*

| Message | Condition |
| :------ | :-------- |
| `[Présence] Personne n'est à la maison (mode CELLULAR/WIFI_?!)` | CELLULAR dans le sensor |
| `[Présence] Seul Mamour est à la maison (Wi-Fi)` | MAMOUR dans le sensor |
| `[Présence] Seul Eric est à la maison (Wi-Fi)` | ERIC dans le sensor |
| `[Présence] Mamour et Eric sont à la maison (Wi-Fi)` | `[2] en [WIFI]` dans le sensor |
| `[Tendance] Température extérieure en hausse : {{ temp_ext }}°` | `Up >>>` dans le sensor |
| `[Tendance] Température extérieure en baisse : {{ temp_ext }}°` | `Down <<<` dans le sensor |
| `[Tendance] Température extérieure stable : {{ temp_ext }}°` | `stable` dans le sensor |
| `[Mode] Chauffage activé : {{ message_part }}` | `Heat` dans le sensor |
| `[Mode] Rafraîchissement activé : {{ message_part }}` | `Cool` dans le sensor |
| `[Mode] Ventilation activée` | `Fan` dans le sensor |

---

### 🍳 P1 — CUISINE

**A — Chauffage Cuisine** *(sans titre)*

| Message | Déclencheur |
| :------ | :---------- |
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin Semaine) /!\` | 07:00 L-Ma-Me-Je |
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin W-E) /!\` | 08:00 Ve-Sa-Di |
| `/!\ RADIATEUR CUISINE est 'ON' /!\` | T° < 19.9°C |
| `/!\ RADIATEUR CUISINE est 'OFF' /!\` | T° > 20.5°C |

**B — Chauffage Cuisine Vacances** *(sans titre)*

| Message | Déclencheur |
| :------ | :---------- |
| `/!\ Chauffage Cuisine 'ON' /!\` | T° < 19.9°C pendant vacances |
| `/!\ Chauffage Cuisine 'OFF' /!\` | T° > 20.5°C pendant vacances |

---

### 🚿 P1 — SDB

**E — Minuterie Sèche-Serviettes**

| Titre | Message |
| :---- | :------ |
| `Sèche-Serv. OFF` | `2h écoulees. Arret automatique.` |

---

### 🔌 P2 — PRISES

**eco_prises**

| Titre | Message |
| :---- | :------ |
| `{{ states('sensor.presence') }}` | `[5] prises [OFF] / [X] prises [ON] ...` |

**gestion_pc_bureau**

| Titre | Message |
| :---- | :------ |
| `Veille détectée` | `PC Bureau [OFF]` |

**gestion_tv_chambre**

| Titre | Message |
| :---- | :------ |
| `Veille détectée` | `Prise TV [OFF]` |

---

### ⚙️ SYSTÈME

**z2m_last_seen**

| Titre | Message |
| :---- | :------ |
| `⚠️ Problème capteur Zigbee` | Liste des capteurs sans signal (dépassement seuil last_seen) |

**economie_energie_vscode**

| Titre | Message | Note |
| :---- | :------ | :--- |
| `🔋 Alerte Énergie - Mini-PC` | `VS Code actif depuis [X]h. Stop ?` | + actions `STOP_VSC` / `KEEP_VSC` |
| *(aucun)* | `VS Code éteint automatiquement.` | Confirmation arrêt auto |

**watchdog_piles**

| Titre | Message |
| :---- | :------ |
| `🪫 Alerte Pile Faible (<10%)` | Liste des appareils avec % restant |

**veille_github_releases**

| Titre | Message |
| :---- | :------ |
| `RELEASE GITHUB` | Infos sur la nouvelle release détectée |
| `! BREAKING CHANGE !` | Alerte breaking change dans le changelog |

---

### 🌩️ MÉTÉO

**notif_foudre**

| Titre | Message |
| :---- | :------ |
| `/!\ Attention foudre /!\` | Distance, direction et nombre d'impacts détectés |

---

### ⚡ ÉNERGIE

**surveillance_gros_electro_hp**

| Titre | Message |
| :---- | :------ |
| `⚡ Alerte Conso. HP` | Nom de l'équipement + puissance détectée en HP |

---

### 💾 BACKUP

**git_weekly**

| Titre | Message |
| :---- | :------ |
| `🚀 Sauvegarde Git` | `Backup hebdo & tag -> GitHub.` |

> **Pas de notify mobile :** `git_hourly`, `git_au_demarrage` (system_log uniquement), `git_alerte_ko` (`persistent_notification` — tableau de bord HA uniquement).

---

> **Automations sans notify mobile :** `stores/`, `P3_eclairage/`, `meteo/alerte_meteo_cartes`, `meteo/maj_temps_foudre`, `meteo/update_prev_temperature`, `meteo/update_prev_humidity`, `systeme/db_purge_mariadb`, `systeme/diag_enregistrement_journalier` (utilise `notify.file`).

---

### 🔧 SCRIPTS (scripts.yaml)

**J 2-0 — Arrêt Clim Protégé** (`j_2_0_secu_arret_clim_protege`) — script exécutant

| Titre | Message | Contexte |
| :---- | :------ | :------- |
| `Prise clim {{ p \| upper }}` | `La Clim {{ piece_nom }} est coupée (Repos complet).` | Clim déjà à 0W — coupure immédiate |
| `ARRÊT CLIM EN COURS` | `La Clim {{ piece_nom }} est active. Attente de descente sous 9W (max 10 min).` | Cycle d'arrêt en cours |
| `CLIM À L'ARRÊT` | `La prise de la Clim {{ piece_nom }} a été coupée proprement (< 9W).` | Coupure réussie |
| `ERREUR ARRÊT CLIM` | `ÉCHEC : La Clim {{ piece_nom }} consomme toujours > 9W après 10 min. Prise maintenue.` | Timeout 10 min dépassé |

**J 1-1/1-2/1-3 — Clim ON/OFF Intelligent** (Salon / Bureau / Chambre) — script routeur

| Titre | Message | Contexte |
| :---- | :------ | :------- |
| `OULA DOUCEMENT !` | `Une procédure d'arrêt est déjà en cours sur [SALON/BUREAU/CHAMBRE].` | Anti-tremblote — verrou actif |

---

## 🌡️ RÉFÉRENTIEL TENDANCE T° EXTÉRIEURE — FORMAT OFFICIEL

> Utilisé dans les templates de message clim (Jour/Nuit) et les notifications.

### Template Jinja2 (source)

```jinja2
{# --- PARTIE 1 : TENDANCE --- #}
{%- if tendance == 'increasing' %}
  {%- set message_tendance = "T°Ext Up ↗ " ~ temp_ext ~ "°" %}
{%- elif tendance == 'decreasing' %}
  {%- set message_tendance = "T°Ext Down ↘ " ~ temp_ext ~ "°" %}
{%- else %}
  {%- set message_tendance = "T°Ext stable → " ~ temp_ext ~ "°" %}
{%- endif %}
```

### Valeurs de sortie possibles

| Condition       | Texte généré              |
| :-------------- | :------------------------ |
| `increasing`    | `T°Ext Up ↗ XX°`          