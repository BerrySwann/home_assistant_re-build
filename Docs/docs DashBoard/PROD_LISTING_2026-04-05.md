# 📋 LISTING AUTOMATIONS PROD — 2026-04-05
> Source : Export HA UI (37 automations actives en production)
> Référence croisée : PROD_vs_REBUILD_DIFF.md

---

## 🟢 P1 — SALON (CLIM)

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 01 | [P1-Salon] Clim Salon — Mode CHAUD si T<18 | 05/04 03:28 | ✅ Dans ReBuild |
| 02 | [P1-Salon] Clim Salon — Mode FROID si T>27 | 04/04 14:11 | ✅ Dans ReBuild |
| 03 | [P1-Salon] Clim Salon — Gardien OFF si Fenêtre | 05/04 03:28 | ✅ Dans ReBuild |
| 04 | [P1-Salon] Clim Salon — OFF si 21h | 04/04 21:00 | ✅ Dans ReBuild |
| 05 | [P1-Salon] Clim Salon — Notif Puissance >50W | 04/04 14:11 | ✅ Dans ReBuild |

---

## 🟢 P1 — BUREAU (CLIM)

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 06 | [P1-Bureau] Clim Bureau — Mode CHAUD si T<18 | 05/04 04:47 | ✅ Dans ReBuild |
| 07 | [P1-Bureau] Clim Bureau — Mode FROID si T>27 | Jamais | ✅ Dans ReBuild |
| 08 | [P1-Bureau] Clim Bureau — Gardien OFF si Fenêtre | 05/04 04:47 | ✅ Dans ReBuild |
| 09 | [P1-Bureau] Clim Bureau — OFF si 21h | 04/04 21:00 | ✅ Dans ReBuild |
| 10 | [P1-Bureau] Clim Bureau — Notif Puissance >50W | Jamais | ✅ Dans ReBuild |

---

## 🟢 P1 — CHAMBRE (CLIM)

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 11 | [P1-Chambre] Clim Chambre — Mode CHAUD si T<18 | 05/04 03:28 | ✅ Dans ReBuild |
| 12 | [P1-Chambre] Clim Chambre — Mode FROID si T>27 | Jamais | ✅ Dans ReBuild |
| 13 | [P1-Chambre] Clim Chambre — Gardien OFF si Fenêtre | 05/04 03:28 | ✅ Dans ReBuild |

---

## 🟢 P1 — CUISINE (RADIATEUR)

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 14 | [P1-Cuisine] Radiateur — ON Semaine (4h45) | 05/04 04:45 | ✅ Dans ReBuild |
| 15 | [P1-Cuisine] Radiateur — OFF Semaine (7h00) | 04/04 07:00 | ✅ Dans ReBuild |

---

## 🟢 P1 — SDB (SOUFFLANT / SÈCHE-SERVIETTES)

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 16 | [P1-SdB] Soufflant — OFF si T>23°C | 04/04 16:04 | ✅ Dans ReBuild |
| 17 | [P1-SdB] Sèche-Serviettes — Minuterie 2h après douche | 04/04 19:11 | ✅ Dans ReBuild ⚠️ ReBuild GitHub était 1h → corrigé 2h |

---

## 🟢 P2 — PRISES (PC / TV)

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 18 | [P2-Bureau] PC Bureau — ON si présent | 04/04 09:02 | ✅ Dans ReBuild |
| 19 | [P2-Bureau] PC Bureau — OFF si absent | 04/04 22:17 | ✅ Dans ReBuild |
| 20 | [P2-Chambre] TV Chambre — OFF si absent | 04/04 22:17 | ✅ Dans ReBuild |
| 21 | [P2-Chambre] Rodret TV Chambre — Synchro état | 04/04 09:05 | ✅ Dans ReBuild |
| 22 | [P2-Salon] TV Salon — OFF si absent | 04/04 22:17 | ✅ Dans ReBuild |

---

## 🟢 P3 — ÉCLAIRAGE

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 23 | [P3] Lumière Entrée — ON à l'arrivée | 04/04 09:04 | ✅ Dans ReBuild |

---

## 🟢 STORES

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 24 | [Store] Salon — Automatisation Volet | 04/04 19:43 | ⚠️ 2 versions (PROD=Simple / ReBuild=Optimisée) — décision requise |
| 25 | [Store] Bureau — Automatisation Volet | 04/04 07:30 | ✅ Dans ReBuild |

---

## 🟢 MÉTÉO

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 26 | [Météo] Alerte Vigilance — Notification | 03/04 10:15 | ✅ Dans ReBuild |
| 27 | [Météo] Alerte Foudre — Notification | 04/04 13:44 | ✅ Dans ReBuild |
| 28 | [Météo] Tendance T° — Rapport Matin | 05/04 07:00 | ✅ Dans ReBuild |
| 29 | [Météo] Tendance T° — Rapport Soir | 04/04 21:00 | ✅ Dans ReBuild |
| 30 | [Météo] Cycle Solaire — Mise à jour | 05/04 00:00 | ✅ Dans ReBuild |

---

## 🟢 SYSTÈME

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 31 | [Système] Diag Conso — Rapport Quotidien | 05/04 00:01 | ✅ Dans ReBuild |
| 32 | [Système] Purge DB MariaDB — Mensuelle | 01/04 02:00 | ✅ Dans ReBuild |
| 33 | [Système] VSCode — Démarrage auto | 05/04 03:10 | ✅ Dans ReBuild |
| 34 | [Système] Watchdog Piles — Alerte | 04/04 09:00 | ✅ Dans ReBuild |

---

## 🟢 BACKUP

| # | Alias | Dernier déclenchement | Statut ReBuild |
|:--|:------|:----------------------|:---------------|
| 35 | [Backup] Git Push — Horaire auto | 05/04 04:00 | ✅ Dans ReBuild |
| 36 | [Backup] Git Push — Hebdo manuel | 01/04 08:00 | ⚠️ YAML complet non récupéré de PROD |
| 37 | [Backup] HA — Alerte démarrage | 05/04 03:10 | ✅ Dans ReBuild |

---

## 📊 SYNTHÈSE

| Catégorie | Nb |
|:----------|:---|
| Total PROD | **37** |
| Total ReBuild GitHub | **52** |
| Communs (PROD ∩ ReBuild) | **30** |
| PROD-only (absents de ReBuild) | **7** |
| ReBuild-only (à déployer en PROD) | **22** |

---

## ⚠️ PROD-ONLY — 7 automations absentes du ReBuild GitHub

Action requise : récupérer YAML depuis HA UI → placer dans `automations_corrige/`.

| # | Alias PROD | Dossier cible |
|:--|:-----------|:--------------|
| 1 | [P1-SdB] Soufflant — OFF si T>23°C | automations_corrige/P1_sdb/ |
| 2 | [P2-Chambre] Rodret TV Chambre — Synchro état | automations_corrige/P2_prises/ |
| 3 | [P2-Salon] TV Salon — OFF si absent | automations_corrige/P2_prises/ |
| 4 | [Météo] Cycle Solaire — Mise à jour | automations_corrige/meteo/ |
| 5 | [Backup] Git Push — Hebdo manuel | automations_corrige/backup/ |
| 6 | [Système] VSCode — Démarrage auto | automations_corrige/systeme/ |
| 7 | [Système] Watchdog Piles — Alerte | automations_corrige/systeme/ |

---

## 🆕 REBUILD-ONLY — 22 automations à déployer en PROD (via UI HA, une par une)

| # | Alias ReBuild | Fichier source dans automations_corrige/ |
|:--|:--------------|:-----------------------------------------|
| 1 | [P1-SdB] Inter SdB — B | P1_sdb/B_... |
| 2 | [P1-SdB] Inter SdB — C | P1_sdb/C_... |
| 3 | [P1-SdB] Inter SdB — E (minuterie) | P1_sdb/E_minuterie_seche_serviettes.yaml |
| 4 | [P1-Bureau] Bureau Allumage PC | P1_clim_chauffage/... |
| 5 | [P2-Chambre] Rodret TV — Mode nuit | P2_prises/... |
| 6 | [Backup] Git — Alerte démarrage HA | backup/... |
| 7 | [Backup] Git — Commit horaire | backup/... |
| 8 | [Backup] Git — Commit hebdo | backup/... |
| 9 | [Backup] Git — Push horaire | backup/... |
| 10 | [Backup] Git — Push hebdo | backup/... |
| 11 | [Système] Diag Conso quotidienne | systeme/... |
| 12 | [Système] Diag Conso mensuelle | systeme/... |
| 13 | [Système] Purge DB | systeme/... |
| 14 | [Système] Z2M Surveillance | systeme/... |
| 15 | [Énergie] Alerte gros électro HP | energie/... |
| 16 | [Énergie] Surveillance lave-linge | energie/... |
| 17 | [Énergie] Surveillance lave-vaisselle | energie/... |
| 18 | [Météo] Tendances Rapport AM | meteo/... |
| 19 | [Météo] Tendances Rapport PM | meteo/... |
| 20 | [Météo] Blitzortung Alerte foudre | meteo/... |
| 21 | [Météo] Vigilance Couleur | meteo/... |
| 22 | [P3] Éclairage Gestion présence | P3_eclairage/... |

---

## 🔧 CORRECTIONS DÉJÀ APPLIQUÉES

| # | Problème | Correction | Statut |
|:--|:---------|:-----------|:-------|
| 1 | `notify.mobile_app_poco_x7_pro_eric` | → `notify.mobile_app_eric` — 26 occurrences | ✅ FAIT |
| 2 | Minuterie sèche-serv : 1h (GitHub) | → 2h (correct PROD) dans E_minuterie_seche_serviettes.yaml | ✅ FAIT |

---

> ⚠️ Note technique : Ce fichier doit être déplacé dans `docs DashBoard/AUTOMATIONS/`
> Le répertoire AUTOMATIONS est un dossier fantôme sandbox — à recréer manuellement sur Windows si besoin.

*Généré le 2026-04-05*
