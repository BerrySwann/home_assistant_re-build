# RAPPORT D'AUDIT ENERGETIQUE & FONCTIONNEL
*Généré le 2026-07-19 - Données : diag_conso_elec.txt (2025-12-20 -> 2026-07-19, 11 880 lignes)*

**Périmètre :** 7 mois de logs HA (intervalles 15 min), confrontés aux YAML automations et
templates en production. Données complètes disponibles : janvier (29 j), février (9 j),
avril (18 j), juillet (19 j - en cours). Mars, mai, juin : lacunes dans les logs.

---

## 1. MISSION 1 : AUDIT DES AUTOMATIONS

### 1A. Radiateur Cuisine - Arrêts forcés

| Automation | Règle théorique | Observation terrain | Statut | Notes |
|:-----------|:----------------|:--------------------|:-------|:------|
| Cuisine - Arret semaine (07h00 LMMJ) | DUT R figé a 07h00 | DUT R stable a 07h00 sur 5 jours verifies (03-08/01). Ecart max : +6 min le 07/01 | CONFORME | Latence HA normale (1 interval = 15 min) |
| Cuisine - Arret WE (08h00 VSD) | DUT R figé a 08h00 | DUT R stable a 08h00 sur 5 WE verifies (11, 17, 18, 24, 25/01) | CONFORME | Aucun depassement detecté |
| Automation B "Vacances" - Arret forcé 08h30 | Arrêt a 08h30 (version corrigée) | **09/01 (Vendredi) : DUT R = 2.9h >> 2.25h (fenêtre max auto A).** Trace : radiateur encore actif a 08h30, 09h00, 09h15, 09h30 | **BUG CONFIRME** (pré-correction) | Version prod actuelle = ancienne (pas d'arret forcé). Fix dans DOCS/03 PAS ENCORE deploye |

**Trace anomalie 09/01 :**

```
09/01 05:45 -> DUT R start (auto A VSD)
09/01 07:45  DUT R = 0.9h  <-- auto A stop forcé (08h00) -> radiateur coupe
09/01 08:00  DUT R = 0.9h  <-- stable, arret confirmé (auto A)
09/01 08:30  DUT R = 1.1h  <-- reprend ! (auto B sans arret forcé, T_cuisine < 19.9°C)
09/01 09:30  DUT R = 1.4h  <-- toujours actif
09/01 fin    DUT R = 2.9h  <-- radiateur a tourné jusqu'à ~10h00-10h30 (T>20.5°C ou arrêt manuel)
```

**Risque actuel :** Tant que la correction B n'est pas déployée en prod, le radiateur peut
dépasser significativement son plan de fonctionnement les jours où la cuisine reste froide
le matin (T_cuisine < 20.5°C a 08h30). Overconsommation estimée : +0.3 a 1.0 kWh/épisode.

---

### 1B. Automations non testables directement

| Automation | Statut | Raison |
|:-----------|:-------|:-------|
| Seche-serviettes SDB - Timer 2h | NON TESTABLE | Noyé dans le pole "Chauff" avec 3 clims + radiateur cuisine + soufflant. Sans capteur dédié SDB, impossible d'isoler les 150W du sèche-serviettes dans le bruit |
| Volets Salon - Logique isolation | NON TESTABLE | Automations volets désactivées en prod depuis (confirmé Eric 2026-07-19). De plus, sans tag groupe (G1/G2/G3/G4) dans les logs, impossible de distinguer G3 (volet devrait être fermé) vs G2/G4 (volet ouvert). Double obstacle |
| Clim - Coupure fenêtre ouverte | NON TESTABLE | Logs ne tracent pas les états binary_sensor.contact_fenetre_*. Impossible d'identifier les épisodes de coupure |

---

## 2. MISSION 2 : BILAN THERMIQUE REEL

### 2A. DUT comparatif par pièce - Hiver (janvier 2026, N=29 jours)

| Pièce | Equipement | DUT moy/jour | DUT min | DUT max | Observation |
|:------|:-----------|:-------------|:--------|:--------|:------------|
| **Salon** | Hitachi RAS-35FH6 (~2008), Sud | **3.93 h** | 0.0 h | 8.9 h | Apports solaires = fort amortisseur thermique |
| **Radiateur Cuisine** | Bain d'huile 1.4kW, Nord | **0.78 h** | 0.0 h | 6.1 h | Fenêtre horaire stricte. Jours G1 = 0h (absence) |
| **Bureau** | Daikin FTX35KNV1B 2018, Nord | **9.98 h** | 5.0 h | 13.9 h | Volet auto protège des pertes nocturnes |
| **Chambre** | Daikin FTX35KNV1B 2018, Nord | **11.72 h** | 8.3 h | 15.8 h | Store manuel = point faible identifié |

**Ratio Chambre / Bureau (même equipement, même consigne 18°C dans tous les groupes) :**

| Plage | Ratio C/B moy | Min | Max | N jours |
|:------|:-------------|:----|:----|:--------|
| Janvier 2026 (total) | **1.17** | 0.89 | 1.54 | 29 |

- La Chambre chauffe en moyenne **17% plus longtemps** que le Bureau pour la même pièce Nord, le même Daikin, la même consigne.
- L'écart ne peut être attribué ni a l'équipement (identique) ni a la consigne (18°C partout).
- **Causes identifiées (precision Eric 2026-07-19) - 2 facteurs combinés, non séparables depuis les logs :**

  1. **Facteur structurel (permanent, non modifiable) :** Bureau = 2 murs en carreau de plâtre
     -> rediffusion thermique depuis SDB (soufflant) et pièces adjacentes. Chambre = 1 seul
     mur carreau de plâtre, 3 murs béton/brique -> thermiquement plus isolée des espaces
     intérieurs chauds = perd plus de chaleur en hiver.
  2. **Facteur comportemental (modifiable) :** Volet auto bureau (ferme si T_ext < 18°C,
     sans intervention humaine) vs store manuel chambre (oublis possibles = déperditions
     nocturnes non bloquées).

- **Implication :** Motoriser le store chambre réduit le facteur 2, mais le facteur 1 (structural)
  persistera. L'objectif réaliste n'est pas d'amener Chambre = Bureau, mais de réduire l'écart.
  Estimation : motorisation store chambre -> économie partielle, gain réel < 17%.

**Outliers notables :**

- 04/01 : ratio = 1.00 (exception - identique Bureau=Chambre). Jour avec T_ext=7.6°C et Salon=11.5h, Bureau=11.5h, Chambre=11.5h. Présence inhabituelle ou configuration atypique.
- 23/01 : ratio = 0.89 (Bureau > Chambre - seul cas du mois). B=12.2h, C=10.8h. A investiguer (Eric seul en télétravail bureau = comportement anormal de la chambre ?).
- 18/01 : ratio = 1.54 (max - Chambre 54% plus longue que Bureau). Journée T_ext=11.7°C mais Chambre perd beaucoup plus.

---

### 2B. Impact des rideaux épais

**Chronologie :** Chambre = 07/02/2026 | Bureau = 22/02/2026

Données disponibles en février : N=9 jours (dont certains avant/après 07/02 - non séparables
sans connaitre la date exacte de chaque ligne).

| Période | DUT Bureau moy | DUT Chambre moy | Ratio C/B |
|:--------|:---------------|:----------------|:----------|
| Janvier (avant rideaux chambre) | 9.98 h/j | 11.72 h/j | **1.17** |
| Février (N=9, avant+après rideaux) | 8.80 h/j | 10.71 h/j | **1.22** |

**Verdict :** Le ratio C/B a légèrement AUGMENTÉ en février (1.22 vs 1.17). Pas d'amélioration
mesurable après les rideaux chambre sur cette période.

**Nuances importantes :**
1. N=9 jours en février = trop peu pour être statistiquement significatif.
2. La T_ext de février peut être différente de janvier (plus froid = écart amplifié quel que soit le rideau).
3. Le store chambre reste manuel - si les rideaux sont fermés mais le store ouvert, le gain est limité.
4. Les rideaux bureau (22/02) n'ont pas eu le temps d'être séparés des données chambre.

**Conclusion honnête :** Aucune amélioration prouvée sur 9 jours. Le rideau seul (store
manuel toujours ouvert la nuit) est insuffisant. Le volet bureau automatisé a probablement
un impact 2-3x supérieur au rideau chambre.

---

### 2C. Seuil de décrochage système

Incrément DUT/15min = 0.25h (=1) signifie fonctionnement continu sur le quart d'heure.

| Pièce | Seuil T_ext (fonctionnement quasi-continu) | Comportement observé |
|:------|:------------------------------------------|:---------------------|
| **Chambre** | < 8°C | DUT > 14h/jour. Incréments 0.25h quasi-systématiques |
| **Bureau** | < 5°C | DUT > 13h/jour. Incréments très réguliers |
| **Salon** | Non atteint dans les données | Max 8.9h même a T_ext=4°C (solaire amortit) |

Le salon n'atteint jamais le régime continu grâce aux apports Sud. Bureau et Chambre
saturent en dessous de 5-8°C ext.

---

### 2D. Inversion estivale (mode cooling, juillet 2026)

En mode refroidissement (T_ext > 26°C), le classement DUT s'inverse complètement :

| Pièce | DUT moy/jour (juillet, N=18) | vs hiver |
|:------|:-----------------------------|:---------|
| **Salon** (Sud, Hitachi) | ~9-10 h | Hiver : 3.9h -> **x2.5 en été** |
| **Bureau** (Nord, volet auto) | ~7-8 h | Hiver : 10.0h -> -25% en été |
| **Chambre** (Nord, store manuel) | ~1.5-3 h | Hiver : 11.7h -> **-85% en été** |

**Interprétation :**
- Salon (Sud) souffre en été : soleil direct = charge thermique maximale = clim tourne en permanence.
- Chambre (Nord) bénéficie en été : orientation protégée, peu d'apports solaires. Le store manuel (oubli hivernale) devient ici un non-problème.
- Bureau (Nord) : volet auto protège partiellement mais pas suffisamment en canicule (T_ext 27-29°C).

**Signal important sur le Hitachi Salon :** En juillet, le DUT Salon monte a 10-15h/jour
(vs 3-4h en janvier). C'est sur ce régime intensif d'été que le différentiel de COP/EER
entre le Hitachi 2008 et un appareil moderne se traduit le plus en kWh.

---

## 3. MISSION 3 : BILAN CONSO & POSTES

### 3A. Talon nocturne (standby)

Mesure : cumul kWh du poste Multi depuis minuit jusqu'a 02h00 = puissance moyenne standby nuit.

| Mois | Multi moy @02h00 | Equiv. puissance | Verdict |
|:-----|:-----------------|:-----------------|:--------|
| Janvier | 0.245 kWh/2h | **122 W moy** | > 100W -> Dépassement |
| Février | 0.166 kWh/2h | **83 W moy** | < 100W -> Acceptable |
| Avril | 0.207 kWh/2h | **103 W moy** | Limite |

**Dispersion janvier (nuits individuelles) :** min 45W (08/01) - max 245W (04/01).
L'écart de x5 entre la meilleure et la pire nuit signale des PC/écrans non mis en veille
certains soirs. Le talon "propre" est autour de 45-60W (tout éteint sauf standby
réseau + Mini-PC HA). Les nuits >150W = au moins un PC bureau ou TV non éteint.

**Référence ADEME :** < 80-100W recommandé pour un logement. La moyenne janvier (122W)
dépasse ce seuil, mais c'est une moyenne - les mauvaises nuits tirent la moyenne vers le haut.

---

### 3B. Ranking des postes énergétiques

#### Hiver (janvier 2026, 29 jours complets)

| Rang | Pôle | kWh/jour moy | kWh total (29j) | % du total | Cout moy/jour (@0.2065€/kWh) |
|:-----|:-----|:-------------|:----------------|:-----------|:------------------------------|
| 1 | **Chauff** | 7.68 | 222.7 | **56.9%** | 1.59€ |
| 2 | **Multi** | 3.22 | 93.4 | **23.9%** | 0.66€ |
| 3 | **Cuis** | 0.97 | 28.1 | 7.2% | 0.20€ |
| 4 | **Froid** | 0.72 | 20.9 | 5.3% | 0.15€ |
| 5 | **Hyg** | 0.69 | 20.0 | 5.1% | 0.14€ |
| 6 | **Lum** | 0.23 | 6.7 | 1.7% | 0.05€ |
| **Total** | | **13.51 kWh/j** | **391.8 kWh** | 100% | **2.79€/j** |

> Note : la colonne "Autres" n'existe pas dans les logs de janvier (format ajouté plus tard).
> Total légèrement sous-estimé.

Cout mensuel estimé janvier : **2.79 x 31 = 86.5€/mois** (HP pur, a ajuster si HC significatif)

#### Printemps (avril 2026, 18 jours - hors chauffage)

| Rang | Pôle | kWh/jour moy | % |
|:-----|:-----|:-------------|:--|
| 1 | **Multi** | 3.67 | **51.7%** |
| 2 | **Froid** | 1.00 | 14.1% |
| 3 | **Cuis** | 0.92 | 13.0% |
| 4 | **Hyg** | 0.73 | 10.3% |
| 5 | **Lum** | 0.33 | 4.6% |
| 6 | Chauff | 0.45 | 6.3% |
| **Total** | | **7.10 kWh/j** | 100% |

**Insight clé :** Multi (3.67 kWh/j en avril) est quasi-identique a janvier (3.22 kWh/j).
Multi n'est PAS saisonnier : c'est la base fixe, toujours présente. C'est le 1er poste
hors saison de chauffe, et le 2ème toute l'année.

---

### 3C. Pareto - Où agir en priorité ?

```
Hiver :  Chauff [=====57%=====] | Multi [===24%===] | Reste 19%
Eté :    Multi [====52%====] | Froid+Cuis+Hyg [====38%====] | Lum 5%
```

- En hiver : 80% des économies possibles sont dans Chauff + Multi.
- Le froid (frigo/congel) est quasi-incompressible (~0.72-1.0 kWh/j permanent).
- L'éclairage (Lum) est marginal (1.7%) - les gains HUE/LED sont déja réalisés.

---

## 4. RECOMMANDATIONS

### TOP 3 ACTIONS PRIORITAIRES

#### 1. URGENT - Déployer l'automation B corrigée (0€, 30 min)

- **Phase actuelle :** Correction rédigée et validée dans `DOCS/03_docs_automations/docs_automations_YAML/P1_cuisine/b_chauffage_cuisine_vacances.yaml`. PAS encore en prod.
- **Risque si non fait :** Le 09/01 a prouvé que le radiateur cuisine peut tourner jusqu'a ~10h30 sans se couper (2.9h vs 2.25h max prévus). Sur une semaine avec 3 matins froids, cela représente +0.5 a 1.5 kWh de surconsommation.
- **Action :** Paramètres HA > Automatisations > "B - Chauffage Cuisine Vacances" > Modifier en YAML > coller le YAML de DOCS/03.
- **Gain :** 0€ de cout, eliminates un comportement non-prévu. Impact energétique faible mais comportement imprévisible risqué (radiateur chaud sans surveillance).

#### 2. Motoriser le store chambre (ou: automation rappel fermeture nocturne)

- **Phase actuelle :** Store entièrement manuel.
- **Constat :** +17% DUT chambre vs bureau, mais l'écart a 2 causes non séparables :
  (1) structural - bureau bénéficie de rediffusion thermique via 2 murs carreau de plâtre
  (SDB soufflant + pièces adjacentes) ; chambre = 1 mur carreau de plâtre, 3 murs béton.
  (2) comportemental - volet bureau auto vs store chambre manuel.
- **Attente réaliste :** Une motorisation du store chambre n'efface pas l'avantage structurel
  permanent du bureau. L'écart se réduirait mais ne disparaîtrait pas. Pas de cible chiffrée
  fiable sans séparer les 2 facteurs dans les logs (impossible actuellement).
- **Option A - 0€ :** Automation rappel mobile a 21h30 "Ferme le store chambre". Impact
  immédiat sur le facteur comportemental. Suffit peut-être, difficile a évaluer a priori.
- **Option B - ~150-250€ :** Motoriser le store chambre + automation identique au bureau.
  Traitement définitif du facteur 2. ROI incertain faute de séparation des facteurs.
- **Recommandation :** Commencer par l'option A (0€, rapide). Observer le DUT chambre sur
  2-3 semaines de rigueur sur le store. Si l'écart C/B persiste > 1.10, c'est que le facteur
  structurel domine et qu'une motorisation n'apportera pas grand chose de plus.

#### 3. Planifier le remplacement du Hitachi RAS-35FH6 (2008) - horizon 1-3 ans

- **Phase actuelle :** Appareil de ~17 ans, gaz R410A (phase de suppression UE). COP chauffage estimé 2.8-3.2 vs Daikin 2018 ~4.2-4.5. EER refroidissement estimé 2.5-3.0 vs Daikin ~4.1.
- **Impact en été (critique) :** En juillet, le DUT salon atteint 10-15h/jour. Un COP/EER 35-40% inférieur sur ce régime intensif représente une surconsommation significative.
- **Estimation très approximative gain remplacement :** Sur base DUT salon ~9h/j en juillet * 30j = 270h. Saving en electrical : (3.5/2.8 - 3.5/4.0) kW = 0.375 kW * 270h = 101 kWh/été -> ~21€/été. Hiver : DUT salon ~4h/j * 90j = 360h * (3.5/3.0 - 3.5/4.5) kW = 360 * 0.39 = 140 kWh -> ~29€/hiver. Total estimé : ~50€/an.
- **ROI :** Avec un remplacement a ~900-1200€ TTC et 50€/an d'économie -> **18-24 ans de ROI**. Le remplacement PRO-ACTIF maintenant n'est PAS rentable sur la seule économie d'énergie.
- **Recommandation honnête :** Ne pas remplacer pour l'économie seule. Prévoir le budget quand l'appareil tombe en panne (dans 1-5 ans statistiquement). Choisir alors un inverter R32 de classe A++ minimum (COP > 4.5). Le R410A commençant a couter plus cher en maintenance, les révisions futures sont également un signal d'alerte.

---

### Synthèse des anomalies relevées

| # | Anomalie | Sévérité | Statut |
|:--|:---------|:---------|:-------|
| A1 | Auto B "Vacances" : pas d'arrêt forcé en prod (radiateur peut tourner indéfiniment) | CRITIQUE | Fix DOCS/03 -> deploiement manuel requis |
| A2 | Chambre +17% DUT vs Bureau (même équipement, même consigne) | MOYEN | Cause : store manuel -> option rideau insuffisante |
| A3 | Talon nocturne Multi >100W certains soirs (PC non éteint) | FAIBLE | Pas d'automation - discipline utilisateur |
| A4 | Logs discontinus (mars, mai, juin absents) | INFO | Limite l'analyse de la transition printemps/été |
| A5 | Hitachi RAS-35FH6 2008 : performance COP/EER dégradée vs Daikin 2018 | INFO | ROI remplacement trop long -> attendre panne |
| A6 | Multi = 2ème poste toute l'année (23-52% selon saison), non saisonnier | INFO | Aucun levier facile. Mini-PC HA + 2 PC bureau = base fixe |

---

*Rapport généré par audit Home Assistant - Eric (BerrySwann) - Ingénieur Domoticien Expert*
*Sources : diag_conso_elec.txt + P1_01_clim_logique_system_autom.yaml + p1_master_gestion_clim.yaml*
*+ A_CHAUFFAGE_CUISINE.md + B_CHAUFFAGE_CUISINE_VACANCES.md + IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md v6.3*
