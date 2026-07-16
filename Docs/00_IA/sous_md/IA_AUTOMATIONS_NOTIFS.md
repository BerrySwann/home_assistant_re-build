# ⚙️ RÈGLES AUTOMATIONS & RÉFÉRENTIEL NOTIFICATIONS
*Lire ce fichier si : création/modification d'une automation, écriture d'un message notify, script HA.*

---

## 🛠️ RÈGLES DE CODAGE STRICTES — AUTOMATIONS

- ⛔ **INTERDIT** : Jamais de tiret "`-`" devant le premier `alias` (Titre). Bloc objet, pas élément de liste.
- ⛔ **INTERDIT** : Jamais d'`id:` au niveau global (laisser HA le gérer).
- ✅ **OBLIGATOIRE** : `alias` en MAJUSCULES pour chaque sous-bloc (trigger, condition, action).
- 🆗 **AUTORISÉ** : `id:` permis UNIQUEMENT à l'intérieur des déclencheurs (ciblage d'actions).
- **MODIFICATIONS** : Annoter chaque ligne modifiée `# "[L...] modif"` + bloc `# annotations_log:` en fin de réponse.

---

## 🔔 STANDARDS DE NOTIFICATION (POCO X7 PRO & MONTRE)

**Cible : Poco X7 Pro + Xiaomi Watch Lite (écran carré, émojis limités)**

1. **TITRE (`title`)** : Max **21 caractères** — MAJUSCULES recommandées.
2. **MESSAGE (`message`)** : Texte pur ASCII uniquement. ⛔ Aucun émoji → remplacer par `!`, `[ ]`, `OK`, `>>`. Info critique dans les 20 premiers caractères.

**Exemple valide :** Titre `SDB : ARRET` (11 car.) / Message `Minuteur 1h fini. RAZ OK.`

---

## 📲 RÉFÉRENTIEL NOTIFICATIONS — FORMATS PAR AUTOMATION

> Inventaire exhaustif des `notify.mobile_app_eric` dans `docs_automations/TREE_CORRIGE/`.

### 🌡️ P1 — CLIM CHAUFFAGE

**A0 — Clim Jour (07h30 → 21h00)**

| Titre | Message | Contexte |
|:------|:--------|:---------|
| `[AJ] ATTENTE CAPTEURS` | `Essai n°{{ repeat.index }}... Les capteurs de jour ne sont pas prêts. Pause 30s.` | Boucle démarrage |
| `[AJ] CLIM JOUR COUPÉE` | `La fenêtre du [Salon/Cuisine/Bureau/Chambre] a été ouverte.` | Ouverture fenêtre |
| `[AJ] {{ states('sensor.presence') }}` | `[éCO HEAT]  Les 3 Clims : {{ temp_eco_c }}° (Absent)` | Résumé — absent |
| `[AJ] {{ states('sensor.presence') }}` | `Mode : {{ mode_saison \| upper }}  Salon: X°  Bureau: Y°  Chambre: Z°` | Résumé — présent |

**B0 — Clim Nuit (21h00 → 07h30)**

| Titre | Message | Contexte |
|:------|:--------|:---------|
| `[AN] ATTENTE CAPTEURS` | `Essai n°{{ repeat.index }}... Les capteurs de nuit ne sont pas prêts. Pause 30s.` | Boucle démarrage |
| `[AN] CLIM NUIT COUPÉE` | `La fenêtre du [Salon/Cuisine/Bureau/Chambre] a été ouverte.` | Ouverture fenêtre |
| `[AN] {{ states('sensor.presence') }}` | `[éCO HEAT]  Les 3 Clims : {{ temp_eco_c }}° (Absent)` | Résumé — absent |
| `[AN] {{ states('sensor.presence') }}` | `Mode : {{ mode_saison \| upper }} (NUIT)  Salon: X°  Bureau: Y°  Chambre: Z°` | Résumé — présent |

**C — Gardien Éco (CLIM OFF)**

| Titre | Message |
|:------|:--------|
| `Delta T° < -1°C` | `Les clim ont été éteintes. ({{ delta }}°C)  T° Ext.: ({{ t_ext }}°C)  Seuil réglé à: {{ seuil }}°C.` |

**D — Notif Temp Jour** *(relai sensor)*

| Titre | Message |
|:------|:--------|
| `[Automa. Notif. Jrs]` | `{{ states('sensor.message_clim_personnalise_7h30_21h00') }}` |
| `[ANN] Erreur Capteurs` | `Erreur : Un capteur TENDANCE est indisponible ! Vérifiez les dépendances.` |

Structure du message relayé (`sensor.message_clim_personnalise_7h30_21h00`) :
```
[sensor.presence]           ← en-tête
T°Ext Up/Down/stable -> X°  ← tendance T° ext.
[BLOC MODE]                 ← cf. tableau ci-dessous
```

| `[BLOC MODE]` | Condition |
|:--------------|:----------|
| `[UNITS OFF]` | Aucune des 3 prises clim alimentée |
| `[ECO HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_1 + heat (absent) |
| `[COOL]\nSalon X°\nBureau X°\nChambre X°` | groupe_1/2/3/4 + cool |
| `[HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_2/3/4 + heat (présent) |
| `[FAN ONLY]\nSalon [FAN/OFF]\nBureau [FAN/OFF]\nChambre [FAN/OFF]` | tous groupes + fan_only |
| `[OFF]` *(par prise)* | Prise individuelle coupée |

**E — Notif Temp Nuit** *(relai sensor)*

| Titre | Message |
|:------|:--------|
| `[Automa. Notif. Nuit]` | `{{ states('sensor.message_clim_personnalise_21h00_7h30') }}` |
| `[ANN] Erreur Capteurs` | `Erreur : Un capteur TENDANCE est indisponible ! Vérifiez les dépendances.` |

Structure identique à Jour. Différence : la nuit, groupe_2/3/4 utilisent `temp_nuit` uniforme.

| `[BLOC MODE]` Nuit | Condition |
|:-------------------|:----------|
| `[UNITS OFF]` | Aucune prise clim alimentée |
| `[ECO HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_1 + heat (absent) |
| `[COOL]\nSalon X°\nBureau X°\nChambre X°` | groupe_1 + cool (absent) |
| `[HEAT]\nSalon X°\nBureau X°\nChambre X°` | groupe_2/3/4 + heat — T° nuit uniforme |
| `[COOL]\nSalon X°\nBureau X°\nChambre X°` | groupe_2/3/4 + cool — T° nuit uniforme |
| `[FAN ONLY]\nSalon [FAN/OFF]\nBureau [FAN/OFF]\nChambre [FAN/OFF]` | tous groupes + fan_only |
| `[OFF]` *(par prise)* | Prise individuelle coupée |

**F — Fermeture Fenêtres**

| Titre | Message |
|:------|:--------|
| `Fermeture en cours` | `La fenêtre du/de la [Salon/Cuisine/Bureau/Chambre] a été fermée. [+ Toutes les fenêtres sont maintenant fermées.]` |

**G — Arrêt Clim**

| Titre | Message |
|:------|:--------|
| `ARRÊT CLIM` | `La clim. [du Salon / du Bureau / de la Chambre] a été coupée.` |

**H — Changement Mode**

| Titre | Message |
|:------|:--------|
| `CHANGEMENT DE MODE` | `Le mode a changé pour: {{ states('sensor.mode_ete_hiver_etat') \| upper }}` |

**I — Debug Force Mode (WATCHDOG)**

| Titre | Message |
|:------|:--------|
| `⛔ SÉCURITÉ CLIM` | `Tentative de démarrage interdite (Prise coupée ou Arrêt en cours). Retour forcé à OFF pour : - [nom clim]` |
| `🔧 CORRECTION MODE` | `Mauvais mode détecté. Correction vers {{ mode_saison \| upper }} pour : - [nom clim]` |

**J — Synchro Prise Coupée**

| Titre | Message |
|:------|:--------|
| `CLIM COUPÉE` | `La prise extérieure [du Salon / du Bureau / de la Chambre] vient d'être éteinte.` |

**L — Debug Présence** *(sans titre)*

| Message | Condition |
|:--------|:----------|
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
|:--------|:------------|
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin Semaine) /!\` | 07:00 L-Ma-Me-Je |
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin W-E) /!\` | 08:00 Ve-Sa-Di |
| `/!\ RADIATEUR CUISINE est 'ON' /!\` | T° < 19.9°C |
| `/!\ RADIATEUR CUISINE est 'OFF' /!\` | T° > 20.5°C |

**B — Chauffage Cuisine Vacances** *(sans titre)*

| Message | Déclencheur |
|:--------|:------------|
| `/!\ Chauffage Cuisine 'ON' /!\` | T° < 19.9°C pendant vacances |
| `/!\ Chauffage Cuisine 'OFF' /!\` | T° > 20.5°C pendant vacances |

---

### 🚿 P1 — SDB

**E — Minuterie Sèche-Serviettes**

| Titre | Message |
|:------|:--------|
| `Sèche-Serv. OFF` | `2h écoulees. Arret automatique.` |

---

### 🔌 P2 — PRISES

**eco_prises**

| Titre | Message |
|:------|:--------|
| `{{ states('sensor.presence') }}` | `[5] prises [OFF] / [X] prises [ON] ...` |

**gestion_pc_bureau**

| Titre | Message |
|:------|:--------|
| `Veille détectée` | `PC Bureau [OFF]` |

**gestion_tv_chambre**

| Titre | Message |
|:------|:--------|
| `Veille détectée` | `Prise TV [OFF]` |

---

### ⚙️ SYSTÈME

**z2m_last_seen**

| Titre | Message |
|:------|:--------|
| `⚠️ Problème capteur Zigbee` | Liste des capteurs sans signal (dépassement seuil last_seen) |

**economie_energie_vscode**

| Titre | Message | Note |
|:------|:--------|:-----|
| `🔋 Alerte Énergie - Mini-PC` | `VS Code actif depuis [X]h. Stop ?` | + actions `STOP_VSC` / `KEEP_VSC` |
| *(aucun)* | `VS Code éteint automatiquement.` | Confirmation arrêt auto |

**watchdog_piles**

| Titre | Message |
|:------|:--------|
| `🪫 Alerte Pile Faible (<10%)` | Liste des appareils avec % restant |

**veille_github_releases**

| Titre | Message |
|:------|:--------|
| `RELEASE GITHUB` | Infos sur la nouvelle release détectée |
| `! BREAKING CHANGE !` | Alerte breaking change dans le changelog |

---

### 🌩️ MÉTÉO

**notif_foudre**

| Titre | Message |
|:------|:--------|
| `/!\ Attention foudre /!\` | Distance, direction et nombre d'impacts détectés |

---

### ⚡ ÉNERGIE

**surveillance_gros_electro_hp**

| Titre | Message |
|:------|:--------|
| `⚡ Alerte Conso. HP` | Nom de l'équipement + puissance détectée en HP |

---

### 💾 BACKUP

**git_weekly**

| Titre | Message |
|:------|:--------|
| `🚀 Sauvegarde Git` | `Backup hebdo & tag -> GitHub.` |

> Pas de notify mobile : `git_hourly`, `git_au_demarrage` (system_log uniquement), `git_alerte_ko` (persistent_notification — tableau de bord HA uniquement).

---

> **Automations sans notify mobile :** `stores/`, `P3_eclairage/`, `meteo/alerte_meteo_cartes`, `meteo/maj_temps_foudre`, `meteo/update_prev_temperature`, `meteo/update_prev_humidity`, `systeme/db_purge_mariadb`, `systeme/diag_enregistrement_journalier` (utilise `notify.file`).

---

### 🔧 SCRIPTS (scripts.yaml)

**J 2-0 — Arrêt Clim Protégé** (`j_2_0_secu_arret_clim_protege`)

| Titre | Message | Contexte |
|:------|:--------|:---------|
| `Prise clim {{ p \| upper }}` | `La Clim {{ piece_nom }} est coupée (Repos complet).` | Clim à 0W — coupure immédiate |
| `ARRÊT CLIM EN COURS` | `La Clim {{ piece_nom }} est active. Attente de descente sous 9W (max 10 min).` | Cycle d'arrêt |
| `CLIM À L'ARRÊT` | `La prise de la Clim {{ piece_nom }} a été coupée proprement (< 9W).` | Coupure réussie |
| `ERREUR ARRÊT CLIM` | `ÉCHEC : La Clim {{ piece_nom }} consomme toujours > 9W après 10 min. Prise maintenue.` | Timeout 10 min |

**J 1-1/1-2/1-3 — Clim ON/OFF Intelligent** (Salon / Bureau / Chambre)

| Titre | Message | Contexte |
|:------|:--------|:---------|
| `OULA DOUCEMENT !` | `Une procédure d'arrêt est déjà en cours sur [SALON/BUREAU/CHAMBRE].` | Anti-tremblote |
