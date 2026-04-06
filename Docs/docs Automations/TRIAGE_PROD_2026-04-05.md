# 🗂️ TRIAGE AUTOMATIONS PROD — 2026-04-05
> PROD : 36 automations | ReBuild : 42 automations (dont 10 non encore déployées)

---

## ❌ À SUPPRIMER DE PROD (3 confirmées)

> Action : supprimer depuis HA → Paramètres → Automatisations

| # | Alias PROD | Raison | Priorité |
|:--|:-----------|:-------|:---------|
| 1 | (A - 0) 2026-01-01 Automatisation CLIM (07h30 <-> 21h00) | ANCIENNE VERSION — remplacée par A-0 2026-01-11 | 🔴 URGENT |
| 2 | (B - 0) 2026-01-02 Automatisation CLIM NUIT (21h00 <-> 07h30) | ANCIENNE VERSION — remplacée par B-0 2026-01-11 | 🔴 URGENT |
| 3 | NOTIF - Gardien Énergétique (Anomalies) | Absent du ReBuild — dernier déclenchement 7 févr. | ⚠️ À CONFIRMER |

---

## ✅ PROD → REBUILD ALIGNÉ (33 automations)

### Z2M / SYSTÈME
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Z2M last_seen | systeme/ |
| DIAG - ENREGISTREMENT JOURNALIER (6 POSTES + DUT) | systeme/ |
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

### GESTION DES CLIM (11 — anciennes versions exclues)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| (A - 0) 2026-01-11 AUTOMATISATION CLIM JOUR (07H30 <-> 21H00) | P1_clim_chauffage/ |
| (B - 0) 2026-01-11 AUTOMATISATION CLIM NUIT (21H00 <-> 07H30) | P1_clim_chauffage/ |
| (C) (CLIM OFF) Gardien Éco (Delta T < -1 et T°Ext > Seuil) | P1_clim_chauffage/ |
| (D) Notification température Up ou Down (7h30 -> 21h00) | P1_clim_chauffage/ |
| (E) Notification température Up ou Down (21h00 -> 7h30) | P1_clim_chauffage/ |
| (F) (CLIM) Notification de fermeture des fenêtres | P1_clim_chauffage/ |
| (G) (CLIM) Automatisation Arrêt Clim Notification | P1_clim_chauffage/ |
| (H) (CLIM) Notification de changement de mode Été/Fan/Hiver | P1_clim_chauffage/ |
| (I) (CLIM DEBUG) Force Mode Correct & Sécurité | P1_clim_chauffage/ |
| (J) Synchro & Notif Clim si Prise Coupée | P1_clim_chauffage/ |
| (L) (DEBUG) Notifier les changements de message clim (Mobile) | P1_clim_chauffage/ |

### STORES (2)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Gestion Optimisée du Store Bureau | stores/ |
| Gestion Store Salon - VERSION FINALE SÉCURISÉE | stores/ |

### ÉNERGIE (1)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| ÉNERGIE - SURVEILLANCE GROS ÉLECTRO EN HP | energie/ |

### MÉTÉO (4)
| Alias PROD | Dossier ReBuild |
|:-----------|:----------------|
| Alerte Météo France actualisation des "CARTES" | meteo/ |
| Météo Vence : Suivi Barométrique | meteo/ |
| Mettre à jour le temps du dernier impact de foudre | meteo/ |
| Notification de la foudre | meteo/ |

---

## 🆕 À DÉPLOYER DE REBUILD → PROD (10 automations non encore en PROD)

> Action : copier le YAML depuis `automations_corrige/` → coller dans HA UI une par une

| # | Alias ReBuild (approximatif) | Dossier source | Statut fichier |
|:--|:-----------------------------|:---------------|:---------------|
| 1 | Backup Git — Push horaire | backup/ | ⏳ Fichier à créer |
| 2 | Backup Git — Push hebdo | backup/ | ⏳ Fichier à créer |
| 3 | Backup Git — Commit horaire | backup/ | ⏳ Fichier à créer |
| 4 | Backup Git — Alerte démarrage HA | backup/ | ⏳ Fichier à créer |
| 5 | Bouton virtuel — Soufflant SdB (activation) | P1_sdb/ | ⏳ Fichier à créer |
| 6 | Radiateur Cuisine — ON (semaine) | P1_cuisine/ | ⏳ Fichier à créer |
| 7 | Radiateur Cuisine — OFF (semaine) | P1_cuisine/ | ⏳ Fichier à créer |
| 8 | SdB Chauffage — 2026-02-01 | P1_sdb/ | ⏳ Fichier à créer |
| 9 | SdB Chauffage — (D) | P1_sdb/ | ⏳ Fichier à créer |
| 10 | SdB Chauffage — (E) Minuterie sèche-serv 2h | P1_sdb/ | ✅ Corrigé (1h→2h) |

---

## 📊 RÉCAPITULATIF FINAL

| Catégorie | Nb |
|:----------|:---|
| PROD total | 36 |
| À supprimer de PROD | **3** (dont 1 à confirmer) |
| PROD → ReBuild aligné | **33** |
| À déployer ReBuild → PROD | **10** |
| ReBuild total (après déploiement complet) | **43** |

---

## 🔧 ORDRE D'ACTIONS RECOMMANDÉ

1. **SUPPRIMER** les 2 ANCIENNES VERSIONS CLIM (A-0 2026-01-01 et B-0 2026-01-02)
2. **CONFIRMER** la suppression de NOTIF - Gardien Énergétique
3. **CRÉER** les sous-dossiers dans `automations_corrige/` et `automations_origine/`
4. **RÉCUPÉRER** le YAML des 10 automations manquantes (backup, SdB, cuisine) depuis HA UI
5. **DÉPLOYER** les 10 automations rebuild-only via HA UI

---

*Généré le 2026-04-05*
