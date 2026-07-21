# 🔌 RÉFÉRENTIEL INTÉGRATIONS & CARTES HA
*Lire ce fichier si : YAML dashboard à valider, `type: custom:*` inconnu, intégration manquante, nouvelle carte à ajouter.*

---

## 🔌 INTÉGRATIONS HA INSTALLÉES

### HACS — Custom Components

| Slug | Nom | Rôle |
|:-----|:----|:-----|
| `spook` | Spook | Extension HA (entités et services supplémentaires) |
| `powercalc` | PowerCalc | Calcul puissance virtuelle (ampoules sans wattmètre) |
| `browser_mod` | Browser Mod | Contrôle navigateur depuis HA |
| `smartir` | SmartIR | Télécommandes IR (clim salon, bureau, chambre) |
| `scheduler` | Scheduler | Planificateur avancé (custom:scheduler-card) |
| `meross_lan` | Meross LAN | Prises Meross en local sans cloud |
| `blitzortung` | Blitzortung | Détection foudre temps réel |
| `atmofrance` | Atmo France | Qualité air extérieur (IQA) |
| `vigieau` | VigiEau | Restrictions d'eau en vigueur (L6C3) |
| `tarif_edf` | Tarifs EDF | Index HP/HC, couts Tempo/Base (P0) |

### Officielles HA Core

| Intégration | Rôle |
|:------------|:-----|
| `mqtt` | Bus Z2M, Blitzortung, capteurs divers |
| `hue` | Pont Hue (toutes ampoules P3) |
| `broadlink` | Émetteur IR (relai SmartIR) |
| `meteo_france` | Alertes vigilance, prévisions, cameras cartes |
| `moon` | Phase lunaire (`lune` = nom FR intégration Core `moon`) |
| `season` | Détection saison courante (`saison` = nom FR) |
| `feedreader` | Suivi flux RSS (releases GitHub) |
| `proxmoxve` | Supervision Proxmox PVE — CPU %, RAM %, Storage %, Status (L4C1) — 6 appareils |
| `systemmonitor` | Supervision systeme Mini PC — CPU, RAM, disque (L4C2) — inclut "Vitesse CPU" |
| `mobile_app` | 7 appareils : 2 Poco (accroche WiFi présence P4) + autres (L5C2 batteries portables) |
| `local_file` | 2 entités météo : `MF_alerte_today` + `MF_alerte_tomorrow` (images vigilance Météo France) |
| `file` | 2 entités notify : `diag_conso_elec.txt` + `ecart_liky_vs_nodon.txt` (logs /homeassistant/notifs/) |
| `restful` | 1 entité : `sensor.blitzortung_lightning_localisation` |
| `backup` | Sauvegardes HA (core) |
| `local_ip` | 1 entite IP du Mini PC |

### Add-ons Supervisor (7 add-ons actifs)

> ⚠️ Zigbee2MQTT et MariaDB tournent sur LXC Proxmox (LXC 200 / LXC 201) — pas des add-ons HA.

| Add-on | Slug | Role |
|:-------|:-----|:-----|
| Advanced SSH & Web Terminal | `a0d7b954_ssh` | Terminal SSH + Web Terminal |
| Cloudflared | `9074a9fa_cloudflared` | Tunnel HTTPS acces distant securise |
| Linky | `cf6b56a3_linky` | Donnees MyElectricalData (index HP/HC, historique conso) -> P0 |
| Mosquitto broker | `core_mosquitto` | Broker MQTT — bus de communication Blitzortung + capteurs MQTT |
| Samba share | `core_samba` | Acces reseau aux fichiers /homeassistant/ (H:\) |
| Studio Code Server | `a0d7b954_vscode` | VSCode integre HA (edition fichiers YAML en prod) |
| Tailscale | `a0d7b954_tailscale` | VPN acces distant securise a HA |

---

## ⚠️ RÈGLE D'AUDIT — FICHIER DASHBOARD FOURNI

À chaque fichier YAML dashboard fourni par l'utilisateur, vérifier **systématiquement** :
- Les `type: custom:*` présents → croiser avec **CARTES HACS** ci-dessous
- Les intégrations référencées → croiser avec **INTÉGRATIONS** ci-dessus
- Tout élément absent de ces deux référentiels → **signaler immédiatement** pour ajout éventuel

---

## 🎨 CARTES HACS ET NATIVES UTILISÉES

| Type | Nom de la Carte | Utilisation Principale |
|:-----|:----------------|:----------------------|
| **Graph/Data** | `apexcharts-card` | Graphiques energie, moyennes glissantes, seuils couleur |
| | `mini-graph-card` | Tendances rapides (temperatures, humidite) |
| | `bar-card` | Jauges de consommation et niveaux de batteries |
| | `energy-overview-card` | Vue d'ensemble consommation energetique |
| | `flex-table-card` | Tableaux flexibles multi-entites |
| **UI/Design** | `bubble-card` | Navigation, Pop-ups par pièce, boutons tactiles |
| | `mushroom-card` | Éclairage (Mushroom Light), Titres, Chips d'état |
| | `mod-card` (card-mod) | Personnalisation CSS avancée des cartes |
| | `layout-card` | Structure des vues (Grid, Masonry) |
| | `stack-in-card` / `vertical-stack-in-card` | Groupement de cartes sans bordures |
| | `swipe-card` | Carrousels (Météo, Caméras) |
| | `auto-entities` | Listes dynamiques (Fenêtres ouvertes, Piles faibles) |
| | `tabbed-card` | Onglets glissants JOUR/MOIS/30J (pages éclairage, énergie) |
| | `button-card` | Boutons programmables avancés (templates, actions) |
| | `streamline-card` | Templates de cartes réutilisables |
| **Spécialisées** | `battery-state-card` | Surveillance état batteries/piles par groupe (L5C1) |
| | `entity-progress-card` | Barre de progression avec label dynamique (L6C2) |
| | `enhanced-shutter-card` | Gestion visuelle des stores (L3C3) |
| | `ring-tile` | Indicateurs circulaires (Statut MariaDB, CPU) |
| | `flex-horseshoe-card` | Jauges en fer à cheval (puissance, CPU…) |
| | `multiple-entity-row` | Multi-affichage sur une seule ligne d'entité |
| | `text-divider-row` | Séparateurs de sections textuels |
| | `navbar-card` | Barre de navigation personnalisée |
| | `content-card-linky` | Affichage donnees Linky (page energie) |
| | `rain-gauge-card` | Visualisation de la pluviométrie |
| | `uv-index-card` | Affichage de l'indice UV (L1C1) |
| | `windrose-card` | Rose des vents (L1C1 Météo) |
| | `meteoalarm-card` | Alertes Météo-Alarm européen (L1C1) |
| | `meteofranceweathercard` | Carte dédiée intégration Météo-France (L1C1) |
| | `uptime-card` | Disponibilité / uptime services |
| | `ha-tbaro-card` | Baromètre (pression atmosphérique) |
| | `horizon-card` | Visualisation lever/coucher soleil sur l'horizon |
| | `temperature-heatmap-card` | Heatmap températures |
| | `tsmoon-card` | Phase lunaire (HACS : "Simple Moon Card") |
| | `meteocss-card` | Carte meteo CSS animee (HACS : "MeteoCSS Card") |
| | `html-jinja2-template-card` | Templates Jinja2 inline dans le dashboard |
| | `scheduler-card` | Interface visuelle du planificateur (scheduler) |
| **Icônes** | `hass-hue-icons` | Pack icônes Hue — prefix `hue:` (ampoules, fixtures) |
| | `custom-brand-icons` | Pack icônes marques — prefix `phu:` (ex: `phu:proxmox`) |

---

## 🎨 PALETTE DE COULEURS OFFICIELLES HA (HEX & RGB)

| État / Type | HEX | RGB | Utilisation type |
|:------------|:----|:----|:----------------|
| **Primary** | `#03a9f4` | `3, 169, 244` | Icônes HA, Titres |
| **Success** | `#0f9d58` | `15, 157, 88` | Actif, Normal, OK |
| **Warning** | `#ff9800` | `255, 152, 0` | Standby, Attention |
| **Error** | `#f44336` | `244, 67, 54` | Alerte, Critique, Off |
| **Info** | `#2196f3` | `33, 150, 243` | Infos, Nuages, Réseau |
| **Inactive** | `#44739e` | `68, 115, 158` | Éteint, Absent |
| **Active** | `#fdd835` | `253, 216, 53` | Éclairage, Chauffage |
| **Text** | `#212121` | `33, 33, 33` | Polices, Bordures |
