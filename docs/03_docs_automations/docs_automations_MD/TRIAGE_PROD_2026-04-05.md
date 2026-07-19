# 🗂️ TRIAGE AUTOMATIONS PROD — VERSION FINALE 2026-04-05 13:03
> Source : Export HA UI — 36 automations actives

---

## ❌ À SUPPRIMER DE PROD

| # | Alias PROD | Raison | Statut |
|:--|:-----------|:-------|:-------|
| 1 | (A - 0) 2026-01-01 Automatisation CLIM | ANCIENNE VERSION | ✅ FAIT |
| 2 | (B - 0) 2026-01-02 Automatisation CLIM NUIT | ANCIENNE VERSION | ✅ FAIT |
| 3 | NOTIF - Gardien Énergétique (Anomalies) | Absent du ReBuild | ✅ FAIT |
| 4 | ÉNERGIE - SURVEILLANCE GROS ÉLECTRO EN HP | Déclassée (31 déc. 2025) | ✅ FAIT |
| 5 | Météo Vence : Suivi Barométrique | Absent du ReBuild | ✅ FAIT |
| 6 | Raspberry CPU Fan PWM 6 States | Legacy RPi — absent du ReBuild | ⏳ À FAIRE |

---

## ✅ PROD → REBUILD ALIGNÉ (35 automations)

### BP / Z2M
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Bouton IKEA RODRET - Soufflant SdB Gestion ON/OFF (JSON) | P2_prises/ |
| Z2M last_seen | systeme/ |

### SYSTÈME (4)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| DB Purge MariaDB + Repack | systeme/ |
| Système - Économie Énergie VS Code | systeme/ |
| Système - Watchdog Piles (HUE/IKEA/SONOFF) | systeme/ |

### ÉCLAIRAGE (5)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Allumage Lumière Entrée | P3_eclairage/ |
| BUREAU - BOUTON RODRET TOGGLE BLANCHES | P3_eclairage/ |
| Bureau - Forcer Play ON si PC tourne | P3_eclairage/ |
| BUREAU - WATCHDOG SYNCHRONISATION LAMPES BLANCHES | P3_eclairage/ |
| BUREAU_ACTIVATION_ECRAN_SYNCHRO | P3_eclairage/ |

### ÉCO PRISES (3)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Automation éCO. Prises | P2_prises/ |
| Gestion PC bureau : Scène de Fin + Notif | P2_prises/ |
| Gestion TV Chambre : Scène de Fin + Notif | P2_prises/ |

### CAPTEURS TEMPÉRATURE (2 — rangés dans meteo/)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Update previous humidity | meteo/ |
| Update previous temperature | meteo/ |

### CLIM (11)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00) | P1_clim_chauffage/ |
| (B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30) | P1_clim_chauffage/ |
| (C) (CLIM OFF) Gardien Éco | P1_clim_chauffage/ |
| (D) Notification température (7h30 -> 21h00) | P1_clim_chauffage/ |
| (E) Notification température (21h00 -> 7h30) | P1_clim_chauffage/ |
| (F) (CLIM) Notification fermeture des fenêtres | P1_clim_chauffage/ |
| (G) (CLIM) Arrêt Clim Notification | P1_clim_chauffage/ |
| (H) (CLIM) Notification changement de mode | P1_clim_chauffage/ |
| (I) (CLIM DEBUG) Force Mode Correct & Sécurité | P1_clim_chauffage/ |
| (J) Synchro & Notif Clim si Prise Coupée | P1_clim_chauffage/ |
| (K) (DEBUG) Notifier changements de message clim | P1_clim_chauffage/ |

### CUISINE (2)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| A - Chauffage Cuisine (4h45-7h LMMJ / 5h45-8h VSD) | P1_cuisine/ |
| B - Chauffage Cuisine Vacances | P1_cuisine/ |

### SDB (2 — déployées)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| A - 2026/02/01 - SALLE DE BAIN - GESTION INTELLIGENTE SOUFFLANT | P1_sdb/ |
| D - SALLE DE BAIN : WATCHDOG SÉCURITÉ RADIATEUR | P1_sdb/ |

### STORES (2)
| Alias PROD | Dossier ReBuild | Note |
|:-----------|:----------------|:-----|
| Gestion Optimisée du Store Bureau | stores/ | ✅ aligné |
| Gestion Simple du Store Salon (Matin/Soir) | stores/ | ⏳ YAML à récupérer (alias différent du ReBuild) |

### MÉTÉO (3)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Alerte Météo France actualisation des "CARTES" | meteo/ |
| Mettre à jour le temps du dernier impact de foudre | meteo/ |
| Notification de la foudre | meteo/ |

---

## 🗑️ HORS PROD — ReBuild non déployé

| # | Alias ReBuild | Raison |
|:--|:--------------|:-------|
| 1 | A - SALLE DE BAIN — DÉMARRAGE ET INITIALISATION DU SOUFFLANT | Hors PROD |
| 2 | A - SALLE DE BAIN — GESTION INTELLIGENTE SOUFFLANT | Hors PROD |
| 3 | B - SALLE DE BAIN — GESTION RÉSISTANCES DU SOUFFLANT | Hors PROD |
| 4 | C - SALLE DE BAIN — GESTION ARRÊT SÉCURISÉ DU SOUFFLANT | Hors PROD |
| 5 | E - Minuterie Sèche Serviettes (Timer 2h) | Hors PROD |
| 6 | Gestion Optimisée du Store Salon (Anti-Reflet PC) | Abandonné — PROD Simple retenue |
| 7 | Mettre à jour le texte du temps écoulé | Hors PROD |

---

## ⏳ À RÉCUPÉRER DEPUIS PROD — YAML HA UI (1)

| # | Alias PROD | Dossier cible | Raison |
|:--|:-----------|:--------------|:-------|
| 1 | Gestion Simple du Store Salon (Matin/Soir) | automations_corrige/stores/ | Alias différent du ReBuild — PROD Simple retenue |

---

## 📊 RÉCAPITULATIF FINAL

| Catégorie | Nb |
|:----------|:---|
| PROD total (13:03) | **36** |
| ✅ Supprimés depuis triage initial | **5** (CLIM ×2, NOTIF, ÉNERGIE, Météo Barométrique) |
| ❌ Reste à supprimer | **1** (Raspberry CPU Fan) |
| ✅ PROD → ReBuild aligné | **34** |
| ⏳ YAML à récupérer | **1** (Store Salon Simple) |
| 🗑️ ReBuild hors PROD | **7** |

---

*Version finale — 2026-04-05 13:03*
