# SYSTEME, EQUIPEMENTS PAR POLE, DASHBOARD, REFERENTIELS ET LOGEMENT
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

*Lire ce fichier si : infra (Proxmox, LXC, IP), equipements P0 a P2, matrice des 18 vignettes, valeurs de sensor.groupe, tendance T ext, logement et absence.*

> Extrait mot pour mot de `Claude md SAVE/CLAUDE.md` (lignes 627-659, 728-746, 793-814, 816-828, version du 2026-11-23, date de derniere modification du fichier), le 2026-11-28. Aucun mot modifie dans les sections ci-dessous.

---

## ⚙️ SYSTÈME & MATÉRIEL

| Composant | Détail |
|:----------|:-------|
| **OS** | HAOS - VM Proxmox VE 9.2.24 (verifie en direct le 2026-10-31) |
| **Matériel** | Mini-PC Intel NUC - SSD 512 Go / RAM 16 Go |
| **Zigbee** | Sonoff EFR32MG21 V2 (reçue 22/05/2026) |
| **LXC 200** | Zigbee2MQTT (10.32.154.244) ; broker MQTT de HA = application Mosquitto (10.32.154.243) ; Mosquitto du CT 200 : port encore ouvert, usage inconnu (releve 2026-10-31) |
| **LXC 201** | MariaDB (10.32.154.242) |
| **LXC 202** | MyElectricalData (10.32.154.245) |
| **Add-ons** | Cloudflared *(vestige — arrêté le 2026-09-20)* · Tailscale · Studio Code Server |
| **Accès** | Samba Share · SSH · Tailscale · Cloudflare Tunnel (host Proxmox .240 → erodi-ha.com) |

**Intégrations (compact)** : MyElectricalData · Météo France · Blitzortung · AtmoFrance · Vigieau · Meross LAN · Philips HUE · Z2M · Browser Mod · Streamline Card · HACS
→ Détail complet : `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_INTEGRATIONS_CARTES/IA_INTEGRATIONS_CARTES.md`

---

## 🔌 ÉQUIPEMENTS PAR PÔLE

### P0 - Énergie Globale : Linky (MyElectricalData J-1 HP/HC), Nodon SEM-4-1-00 (pince Z2M - temps réel).
- Entités Nodon : `sensor.general_electric_appart_energy` (kWh) · `sensor.general_electric_appart_power` (W)
- Source UM P0 : `sensor.general_electric_appart_energy` (Nodon direct - Linky = 24h délai)
### P1 - Chauffage / Clim
- 4 SALON : clim_salon_entree · 5 CUISINE : radiateur_cuisine · 7 BUREAU : clim_bureau
- 8 SDB : soufflant_sdb, seche_serv_sdb · 9 CHAMBRE : clim_chambre

### P2 - Prises
- 1 ENTRÉE : box_internet_entree, horloge_entree
- 4 SALON : pc_s_gege_salon, salon_chargeur_salon, tv_salon
- 5 CUISINE : micro_ondes, lave_linge, lave_vaisselle, airfryer, four_plaque, frigo, congel, petit_dejeuner
- 7 BUREAU : bureau_pc, fer_a_repasser_bureau · 9 CHAMBRE : tete_de_lit_chambre, tv_chambre

---

### P4 - Présence : téléphones mobiles (Poco X7 Pro), capteurs Wi-Fi.
→ Détail complet sensor.presence : `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_P4_PRESENCE/IA_P4_PRESENCE.md`

---

## 🖥️ CARTOGRAPHIE DASHBOARD (MATRICE 18 VIGNETTES)

| Ligne | C1 | C2 | C3 |
|:------|:---|:---|:---|
| **L1** | Météo | Températures | Commandes Clim |
| **L2** | Conso Générale | Conso Clim | Conso Éclairage |
| **L3** | Commandes Éclairage | Commandes Éco (Prises) | Fenêtres + Stores |
| **L4** | Mini PC (NUC) | Proxmox (PVE) | Mises à jour HA |
| **L5** | Piles / Batteries | Batteries Portables | MariaDB |
| **L6** | Qualité Air (Appart) | Pollution / Pollen | Vigilance Eau |

> Page d'accueil L0C0 : le dossier s'appelle `L0C0_PAGE_Home` (cote MD et cote YAML). Nom decide par Eric le 2026-10-11 : ne pas le renommer, ne pas revenir a `PAGE_Home (L0C0)`.

---

## 👥 RÉFÉRENTIEL P4 - VALEURS `sensor.groupe`

Table des valeurs groupe_1 a groupe_4 (avec leurs conditions), sensor.presence et codes reseau : voir `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_P4_PRESENCE/IA_P4_PRESENCE.md`. Une seule version, ne pas la recopier ici.

---

## 🌡️ RÉFÉRENTIEL TENDANCE T° EXTÉRIEURE

| Condition | Texte généré |
|:----------|:-------------|
| `increasing` | `T°Ext Up ↗ XX°` |
| `decreasing` | `T°Ext Down ↘ XX°` |
| `stable` | `T°Ext stable → XX°` |

---

# 🏠 LOGEMENT & STRATÉGIE THERMIQUE
- **Localisation :** 06140 Vence (Altitude ~360m) - Immeuble 1980, 4ème étage sous toiture. Traversant SUD/NORD, simple vitrage. VMC en SDB.
- **Mode Absence Hiver** : 17°C · si T° Ext < 10°C → 18°C · si T° Ext < 8°C → 19°C.
- **Mode Absence Été** : T° Cible = 28°C.
- **Logique "Cœur du Système" (T° Extérieure → Cible → Confort) :**

![Confort Cible Calcul Flow](https://github.com/user-attachments/assets/f18e24a2-1441-482b-af70-537a7b208e15)
*(copie locale du fichier : `docs/00_IA/confort_cible_calcul_flow.png` ; asset GitHub d'origine : https://github.com/user-attachments/assets/f18e24a2-1441-482b-af70-537a7b208e15)*

> Caractéristiques détaillées du logement (dimensions, équipements par pièce, orientations) :
> déplacées dans `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md` (2026-07-19,
> usage limité à l'analyse des consommations électriques, hors périmètre des directives actives).

<!-- annotations_log: [2026-11-28] creation par extraction de CLAUDE.md pour l'alleger (demande d'Eric), contenu inchange -->
<!-- annotations_log: [2026-11-28] doublon_sensor_groupe : table sensor.groupe retiree (doublon de IA_P4_PRESENCE, memes 4 valeurs, P4 en plus detaille les conditions) et remplacee par un renvoi vers IA_P4_PRESENCE (accord d'Eric 2026-11-28) -->
