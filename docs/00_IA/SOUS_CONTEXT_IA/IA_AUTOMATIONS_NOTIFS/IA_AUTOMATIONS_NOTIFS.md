# ⚙️ RÈGLES AUTOMATIONS & RÉFÉRENTIEL NOTIFICATIONS
*Dernière mise à jour : 2026-10-13 (relevé prod du jour : automations.yaml = 62 automations dont 31 avec notify, scripts.yaml = 9 scripts dont 5 avec notify ; refonte d'origine du 2026-07-18)*
*Lire ce fichier si : création/modification d'une automation, écriture d'un message notify, script HA.*

---

## 🛠️ RÈGLES DE CODAGE STRICTES - AUTOMATIONS

- ⛔ **INTERDIT** : Jamais de tiret "`-`" devant le premier `alias` (Titre). Bloc objet, pas élément de liste.
- ⛔ **INTERDIT** : Jamais d'`id:` au niveau global (laisser HA le gérer).
- ✅ **OBLIGATOIRE** : `alias` en MAJUSCULES pour chaque sous-bloc (trigger, condition, action).
- 🆗 **AUTORISÉ** : `id:` permis UNIQUEMENT à l'intérieur des déclencheurs (ciblage d'actions).
- **MODIFICATIONS** : Annoter chaque ligne modifiée `# "[L...] modif"` + bloc `# annotations_log:` en fin de réponse.
- **DÉPLOIEMENT** : jamais de modification directe d'`automations.yaml` - passer par l'UI HA, un par un, en s'appuyant sur `docs/03_docs_automations/03_docs_automations_yaml/`.

---

## 🔔 STANDARDS DE NOTIFICATION (POCO X7 PRO & MONTRE)

**Cible : Poco X7 Pro + Xiaomi Watch Lite (écran carré, émojis limités)**

1. **TITRE (`title`)** : Max **21 caractères** - MAJUSCULES recommandées.
2. **MESSAGE (`message`)** : Texte pur ASCII de préférence. Éviter les émojis → remplacer par `!`, `[ ]`, `OK`, `>>`. Info critique dans les 20 premiers caractères.

**Exemple valide :** Titre `SDB : ARRET` (11 car.) / Message `Minuteur 1h fini. RAZ OK.`

> État réel prod : quelques titres contiennent encore des émojis (⚠️ Watchdog SDB, 🪫 Piles, ⚠️ Zigbee). Tolérés sur mobile, à éviter pour la montre.

---

## 📨 CANAUX DE NOTIFICATION EN PROD

| Canal | Service | Usage |
|:------|:--------|:------|
| Mobile Eric | `notify.mobile_app_eric` | 26 automations + 5 scripts |
| Mobile Mamour | `notify.mobile_app_mamour` | 3 automations (alarmes congélateur, en double de Eric) |
| Fichiers log (File UI) | `notify.send_message` → entité File | 6 automations (7 fichiers .txt) |

> ⛔ Plateforme `notify.file` **interdite en YAML** (breaking change 2026). Les cibles fichier passent par l'intégration **File** créée dans l'UI, appelée via `notify.send_message`.

**Cibles File actives (7, créées dans l'UI, chemins vus depuis `/config/` = `/homeassistant/`) :**
- `/config/notifs/diag_conso_elec.txt` (`notify.file_diag_log_file`) ← DIAG - ENREGISTREMENT JOURNALIER (7 POSTES + DUT)
- `/config/notifs/ecart_liky_vs_nodon.txt` (`notify.log_ecart_energie`) ← Log Écart Linky vs Nodon
- `/config/.logs/zone_eric.txt` (`notify.zone_eric`) ← [P4] Eric - Log Zones
- `/config/notifs/linky_histo.txt` (`notify.log_linky_histo`) et `/config/notifs/ecart_histo.txt` (`notify.log_ecart_histo`) ← A - [P0] Histo Linky quotidien + Ecart J-1
- `/config/notifs/nodon_histo.txt` (`notify.log_nodon_histo`) ← B - [P0] Histo Nodon quotidien
- `/config/notifs/nodon_complet_histo.txt` (`notify.nodon_complet_histo`) ← E - [P0] Histo Nodon complet quotidien (Total HP HC Cout)

---

## 📲 RÉFÉRENTIEL NOTIFICATIONS - RELEVÉ PROD 2026-10-13

> Source : `automations.yaml` + `scripts.yaml` (GitHub = reflet prod). Yaml individuels : `docs/03_docs_automations/03_docs_automations_yaml/`.

### 🌡️ P1 - CLIM CHAUFFAGE

**⚠️ RESTRUCTURATION vs ancien référentiel** : les automations (A-0) Clim Jour et (B-0) Clim Nuit n'émettent **plus** de notify directement - tout passe par le script **`p1_master_gestion_clim`** (voir section Scripts). L'automation "(C) Gardien Éco" a été **supprimée** de prod.

**(C) Notification température Jour (7h30 → 21h00)** *(relai sensor)*

| Titre | Message |
|:------|:--------|
| `[Automa. Notif. Jrs]` | `{{ states('sensor.message_clim_personnalise_7h30_21h00') }}` |
| `[ANJ] Erreur Capteurs` | `Un capteur (Temperature, Wifi ou Message) est indisponible. Verifiez...` |

**(D) Notification température Nuit (21h00 → 7h30)** *(relai sensor)*

| Titre | Message |
|:------|:--------|
| `[Automa. Notif. Nuit]` | `{{ states('sensor.message_clim_personnalise_21h00_7h30') }}` |
| `[ANN] Erreur Capteurs` | `Erreur: Un capteur TENDANCE est indisponible! Verifiez les dependances` |

Structure du message relayé (`sensor.message_clim_personnalise_*`) :
```
[sensor.presence]           ← en-tête
T°Ext Up/Down/stable -> X°  ← tendance T° ext.
[BLOC MODE]                 ← [UNITS OFF] / [ECO HEAT] / [COOL] / [HEAT] / [FAN ONLY] / [OFF] par prise
```

**(E) Notification fermeture fenêtres**

| Titre | Message |
|:------|:--------|
| `Fermeture en cours` | `La fenêtre du/de la [Salon/Cuisine/Bureau/Chambre] a été fermée. [+ Toutes les fenêtres sont maintenant fermées.]` |

**(F) Arrêt Clim**

| Titre | Message |
|:------|:--------|
| `ARRÊT CLIM` | `La clim. [du Salon / du Bureau / de la Chambre] a été coupée.` (map sur `climate.clim_*_rm4_mini`) |

**(G) Changement de mode Été/Fan/Hiver**

| Titre | Message |
|:------|:--------|
| `CHANGEMENT DE MODE` | `Le mode a changé pour: {{ states('sensor.mode_ete_hiver_etat') \| upper }}` |

**(H) Force Mode Correct & Sécurité (WATCHDOG)**

| Titre | Message |
|:------|:--------|
| `SÉCURITÉ CLIM` | `Tentative de démarrage interdite (Prise coupée ou Arrêt en cours). Retour forcé à OFF pour : - [nom clim]` |
| `CORRECTION MODE` | `Mauvais mode détecté. Correction vers {{ mode_saison \| upper }} pour : - [nom clim]` |

**(I) Synchro & Notif Clim si Prise Coupée**

| Titre | Message |
|:------|:--------|
| `CLIM COUPÉE` | `La prise extérieure [du Salon / du Bureau / de la Chambre] vient d'être éteinte.` |

**(J) Debug changements message clim** *(sans titre)*

| Message | Condition (`in trigger.to_state.state`) |
|:--------|:----------------------------------------|
| `[Présence] Personne n'est à la maison (mode CELL/WIFI_?!)` | `'CELL'` |
| `[Présence] Seul Mamour est à la maison (Wi-Fi)` | `'Mamour'` |
| `[Présence] Seul Eric est à la maison (Wi-Fi)` | `'Eric'` |
| `[Présence] Mamour et Eric sont à la maison (Wi-Fi)` | `'[2] en [WIFI]'` |
| `[Tendance] Température extérieure en hausse : {{ temp_ext }}°` | `'Up ↗'` |
| `[Tendance] Température extérieure en baisse : {{ temp_ext }}°` | `'Down ↘'` |
| `[Tendance] Température extérieure stable : {{ temp_ext }}°` | `'stable →'` |
| `[Mode] Chauffage activé : {{ message_part }}` | `'HEAT]'` |
| `[Mode] Rafraîchissement activé : {{ message_part }}` | `'COOL]'` |
| `[Mode] Ventilation activée` | `'FAN ONLY]'` |

### 🍳 P1 - CUISINE

**A - Chauffage Cuisine** + **B - Vacances** *(sans titre)*

| Message | Déclencheur |
|:--------|:------------|
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin Semaine) /!\` | 07:00 L-Ma-Me-Je |
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin W-E) /!\` | 08:00 Ve-Sa-Di |
| `/!\ RADIATEUR CUISINE est 'ON' /!\` puis `... 'OFF' /!\` | T° < 19.9°C puis > 20.5°C (A) |
| `/!\ RADIATEUR CUISINE est 'OFF' FORCE (Fin Vacances 8h30) /!\` | fin des vacances 8h30 (B) |
| `/!\ Chauffage Cuisine 'ON' /!\` puis `... 'OFF' /!\` | idem pendant vacances (B) |

### 🚿 P1 - SDB

| Automation | Titre | Message |
|:-----------|:------|:--------|
| F - Minuterie Sèche-Serviettes (Timer Absolu 2h) | `Sèche-Serv. OFF` | `2h écoulees. Arret automatique.` |
| G - Décompte 2 H (timer) *(doublon de F, F reste actif jusqu'à décision d'Eric)* | `Seche-Serv. OFF` | `Duree maximale ecoulee. Arret automatique.` |
| C - WATCHDOG SÉCURITÉ SOUFFLANT | `⚠️ Watchdog SDB` | `Dérive thermique détectée à {{ th_salle_de_bain_temperature }}°C. Reset IR lancé.` |

> Sans notify : A (bouton IKEA RODRET), B (routage), D (décompte 60 min), E (rattrapage au démarrage soufflant), H (rattrapage au démarrage sèche-serviettes), Z (2026/02/01 gestion intelligente soufflant).

### 🔌 P2 - PRISES

| Automation | Titre | Message |
|:-----------|:------|:--------|
| ECO. PRISES DYNAMIQUE | `ECO PRISES: {{ g \| upper }}` | Comptage prises ON/OFF (7 prises - absent_only sur TV Salon / PC Bureau / TV Chambre) |
| Gestion PC Bureau | `Allumage PC` / `Veille détectée` | `PC Bureau [ON]` / `PC Bureau [OFF]` |
| Gestion TV Chambre | `Allumage TV` / `Veille détectée` | `Prise TV [ON]` / `Prise TV [OFF]` |
| P2 - ALARME Congélateur : porte mal fermée (probable) *(Eric + Mamour)* | `Congélateur : porte mal fermée ?` | `Température {{ tongel_temperature }}°C depuis au moins 5 min, compresseur actif. Vérifie la fermeture de la porte.` |
| P2 - ALARME Congélateur : panne probable *(Eric + Mamour)* | `Congélateur : panne probable` | `Température {{ tongel_temperature }}°C, aucun appel de courant du compresseur depuis au moins 1h. Vérifie le congélateur et la prise.` |
| P2 - ALARME Congélateur : perte de supervision capteur Tongel *(Eric + Mamour)* | `Congélateur : capteur muet` | `sensor.tongel_temperature ne remonte plus rien depuis au moins 2h. Plus de supervision du congélateur (pile ? Zigbee ?).` |

### ⚙️ SYSTÈME

| Automation | Titre | Message |
|:-----------|:------|:--------|
| Économie Énergie VS Code | `ALERTE VSC CPU` | `CPU VSC >10% dps 10m. Le couper pour economiser ?` |
| | `ALERTE VSC INAC` | `VSC inactif dps 15m. Le couper pour economiser ?` |
| | `VSC ARRETE` | `Arret auto VSC OK. (Economie energie).` |
| Watchdog Piles | `🪫 Alerte Pile Faible (<10%)` | Liste appareils + % restant |
| Z2M last_seen | `⚠️ Problème capteur Zigbee` | `Des capteurs Zigbee ne répondent plus : {{ sensors }}` |
| VEILLE GITHUB | `RELEASE GITHUB` / `! BREAKING CHANGE !` | Repo + release détectée / alerte changelog |

### 🌩️ MÉTÉO

| Automation | Titre | Message |
|:-----------|:------|:--------|
| Notification de la foudre | `/!\ Attention foudre /!\` | Distance, direction, impacts |

### 💾 BACKUP

| Automation | Titre | Message |
|:-----------|:------|:--------|
| [03] Git weekly (dim 01:30) | `BACKUP WEEKLY` | `Backup hebdo + tag -> GitHub OK. Semaine {{ now W }}` |
| [00] Alerte si KO 15 min | `BACKUP KO` | `Git push KO depuis 15 min. Verif log backup.` |

> Sans notify mobile : [01] hourly · [02] daily · [04] push manuel · [05] weekly manuel · [06] au démarrage.

---

### 🔧 SCRIPTS (scripts.yaml)

**`p1_master_gestion_clim` - P1 MASTER : Gestion centralisée clim** *(remplace les notify de A-0/B-0)*

| Titre | Message | Contexte |
|:------|:--------|:---------|
| `{{ prefix }} SÉCURITÉ CLIM` | `Capteur(s) HS : {{ hs_list }}. Arrêt sécurité - les climatiseurs sont coupés (mode éco impossible à calculer).` | Capteur critique HS : clims coupées (prefix = [AJ]/[AN]) |
| `{{ prefix }} MODE DÉGRADÉ` | `Capteur(s) HS : {{ hs_list }}. Mode dégradé - réglage sur eco heat ou eco cool (température éco hiver ou été).` | Capteur non critique HS : mode éco dégradé |
| `{{ prefix }} CLIM {{ periode \| upper }} COUPÉE` | Fenêtre ouverte (mapping par trigger_entity_id) | Ouverture fenêtre |
| `{{ prefix }} {{ states('sensor.presence') }}` | Résumé état prises/modes/températures | Résumé périodique |

**`j_2_0_secu_arret_clim_protege` - Arrêt Clim Protégé**

| Titre | Message |
|:------|:--------|
| `Prise clim {{ p \| upper }}` | `La Clim {{ piece_nom }} est coupée (Repos complet).` |
| `ARRÊT CLIM EN COURS` | `La Clim {{ piece_nom }} est active. Attente de descente sous 9W (max 10 min).` |
| `CLIM À L'ARRÊT` | `La prise de la Clim {{ piece_nom }} a été coupée proprement (< 9W).` |
| `ERREUR ARRÊT CLIM` | `ÉCHEC : La Clim {{ piece_nom }} consomme toujours > 9W après 10 min. Prise maintenue.` |

**`j_1_1/2/3_*_clim_on_off_intelligent` (Salon / Bureau / Chambre)**

| Titre | Message |
|:------|:--------|
| `OULA DOUCEMENT !` | `Une procédure d'arrêt est déjà en cours sur [SALON/BUREAU/CHAMBRE].` |

---

> **Automations sans notify (31)** : météo (cartes, prev température, prev humidité, maj temps foudre) · db_purge_mariadb · basculement HC/HP · stores (×2) · P3 éclairage (×8 : entrée, rodret toggle, watchdog bureau, forcer play, activation écran, somrig, inter salon, sync miroir SDB) · backups [01][02][04][05][06] · [P0] rattrapage Linky J-2 et MANQUANT · clim A-0/B-0 (délèguent au master) · SDB A, B, D, E, H, Z.
