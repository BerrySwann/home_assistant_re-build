# ARCHIVE - HISTORIQUE DES SESSIONS HA / REBUILD (mars a mai 2026)

> Recupere le 2026-09-29 depuis `docs/05_docs_MD_system/workflow/WORKFLOW_REBUILD.md`
> avant la suppression de ce fichier. C est le seul endroit ou ces sessions etaient
> racontees : le journal complet du dossier `historique/` ne commence qu au 2026-04-25,
> donc les sessions de mars et d avril n existaient que la.
>
> Suite de l historique : `JOURNAL_COMPLET_2026-04-25_2026-07-14.md`,
> puis `JOURNAL_FUSIONNE_2026-07-15_2026-09-20.md`, puis les `histo_*.txt`.

---

## 📅 HISTORIQUE DES SESSIONS

| Date       | Actions effectuées |
|------------|--------------------|
| 2026-03-15 | Sync initiale GitHub → TREE (151 fichiers détectés) |
| 2026-03-16 | Corrections headers (26 fichiers), ajout P3_POWER, diag_hebdo |
| 2026-03-17 | Réorganisation complète ReBuild (TREE_CORRIGE/ORIGINE/Dashboard/docs) |
| 2026-03-17 (s2) | Ajout `utilitaires/Mise_a_jour_home_assistant.yaml` - fix vignette L4C3 |
| 2026-03-17 (s3) | Création `docs/WIFI_PRESENCE (Home Page)/PAGE_HOME.md` - doc complète home page (18 vignettes) |
| 2026-03-18 (s4) | Création `docs/L4C3_MAJ_HA/L4C3_VIGNETTE_MAJ.md` - vignette button-card + page MAJ (2 grilles). Fix bug `margin-left: 250%` documenté. DEPENDANCES_GLOBALES L4C3 🔲→✅ |
| 2026-03-18 (s5) | Création `docs/L2C3_ENERGIE_ECLAIRAGE/PAGE_ENERGIE_ECLAIRAGE.md` - YAML complet page éclairage (5 pièces, tabbed-card JOUR/MOIS/30J, apexcharts). MàJ `L2C3_VIGNETTE_ECLAIRAGE.md` (métadonnées + liens). DEPENDANCES_GLOBALES L2C3 enrichi. |
| 2026-03-22 (s6) | Création `Orphelin/orphelin.yaml` - inventaire entités sans vignette (Pôle 1, Pôle 4 mobiles, Serveur, Réseau). Statuts 🔲/🟡/✅. |
| 2026-03-22 (s7) | Complétion docs existantes - ajout métadonnées et chaînes dépendances manquantes dans DEPENDANCES_GLOBALES. |
| 2026-03-25 (s8) | Création `docs/L4C2_MINI_PC/L4C2_VIGNETTE_MINI_PC.md` - vignette Mini PC Intel NUC. Ajout sensors spéciaux command_line thermal zones documentés. |
| 2026-03-25 (s9) | Création `docs/L4C2_MINI_PC/PAGE_RASPI.md` - page transitoire RPi4 (conservée jusqu'à migration). Catégories A/B/C/D. |
| 2026-03-25 (s10) | Ajout UM + AVG prise Mini PC IKEA dans TREE_CORRIGE (`P2_UM_AMHQ_prises.yaml` + `P2_AVG_AMHQ_prises.yaml`). |
| 2026-03-25 (s11) | Clôture documentation L4C2 Mini PC. Création `docs/L4C2_MINI_PC/PAGE_MINI_PC.md` (page définitive Mini PC Intel NUC - 13 blocs, 5 pop-ups). Ajout automation ventilateur RPi dans `PAGE_RASPI.md` (Catégorie D). MàJ `DEPENDANCES_GLOBALES.md` (L4C2 chaîne complète). MàJ `CLAUDE.md` + `IA_CONTEXT_BASE.md` (date 2026-03-25). Création `TODO_2026-03-25.md` (8 tâches classées). Vérif GitHub : 2 nouveaux fichiers détectés (`P2_UM_AMHQ_mini_pc.yaml` + `P2_AVG_AMHQ_mini_pc.yaml`) - Mini PC déployé en prod comme fichiers séparés. ⚠️ TREE_CORRIGE : 2 fichiers présents sur 44 attendus (gap critique à traiter). |
| 2026-03-26 (s12) | Spook - analyse dashboard TABLETTE : **62 entités fantômes détectées**. Mise à jour `Orphelin/orphelin.yaml` avec catégorisation complète (⛔ OBSOLÈTE : gm1901 7 entités + sm_a530f 5 entités / 🔴 FANTÔME : 10 schedule_* P1 + statut_soufflant_sdb + 9 Mini-PC + 3 réseau / 🔵 NON PRIO : tablette + 4 smartphones). Création 10 nouveaux dossiers `docs/` : `L1C3_CLIM/`, `L2C2_ENERGIE_CLIM/`, `L3C1_ECLAIRAGE/`, `L3C2_PRISES/`, `L3C3_STORES/`, `L4C1_FREEBOX/`, `L5C2_BATTERIES_PORTABLES/`, `L6C1_AIR_QUALITE/`, `L6C2_POLLUTION_POLLEN/`, `L6C3_VIGIEAU/` (vignettes + pages). |
| 2026-03-27 (s13) | Création `input_booleans/P1/P1_arret_clim_securises.yaml` (arrêts sécurisés clim Salon/Bureau/Chambre + `inter_soufflant_salle_de_bain`). Création `input_booleans/P4/P4_presence_wifi.yaml` (détection présence Wi-Fi). Création `TABLETTE_card_conso_clim_FIXED.yaml` (button-card conso clim - entités corrigées `_kwh_um` vs anciens `_um`). Confirmation par Gemini : gm1901 + sm_a530f OBSOLÈTES → à supprimer du dashboard TABLETTE. Identification duplicate : `P1_switch_inter_soufflant_sdb.yaml` = doublon de `templates/Inter_BP_Virtuel/BI_02_switch_inter_sdb.yaml` → à supprimer. |
| 2026-03-28 (s14) | Vérification synchronisation GitHub ↔ local. Complétion `DEPENDANCES_GLOBALES.md` : **18/18 vignettes ✅** avec chaînes de dépendances complètes. Mise à jour date `DEPENDANCES_GLOBALES.md`. |
| 2026-04-02 (s15) | Analyse énergétique Jan-Mar 2026 (`diag_conso_elec.txt` - 8329 entrées 15min). Résultat : Jan 384 kWh / Fév 339 kWh / Mar ~166 kWh corrigé (anomalie UM reset 18-22/03 - 69.92 kWh était cumul 5 jours, pas 1 jour). Recommandation rideaux occultants : Chambre priorité 1. Comparaison rapport Spook (62 entités) vs `orphelin.yaml` → couverture 100%, statut P1 PARTIEL → ✅ COUVERT (doc `L2C2_VIGNETTE_ENERGIE_CLIM.md` confirmée existante). Création `Orphelin/orphelin.md` (version lisible et structurée par priorité d'action). Mise à jour `CLAUDE.md` arborescence `docs/` (10 dossiers manquants ajoutés, noms corrigés, fichiers fantômes supprimés). Mise à jour date `DEPENDANCES_GLOBALES.md` (2026-04-02). Mise à jour date `WORKFLOW_REBUILD.md`. |
| 2026-04-19→26 (s16-17) | Restructuration majeure TREE_CORRIGE : P3 éclairage refonte complète (`P3_ENERGIE_TLP/` = 76+40+4 sensors, P3_UM réduit à 1 fichier 1_UNITE, `P3_TPL_AMHQ_*.yaml` ×3). P0 Energie : ajout `01_kWh_UM_AMHQ.yaml` (test A/B vs Ecojoko). Suppression ancien repo prod (`home-assistant-config` effacé - `home_assistant_re-build` = prod unique). Ajout `groups/` (GRP_01/02/03 batteries Hue/IKEA/SONOFF). Refonte `command_line/` (ajout `sante_systeme_mini_pc/`). Mise à jour CLAUDE.md globale (date 2026-04-29, arbo prod complète). Sync GitHub ↔ local documentée dans `SYNC_REPORT.md`. |
| 2026-05-01→06 (s18-19) | Archivage Dashboard vignettes L1C1→L5C3 (15 vignettes + pages YAML). Création sous-dossiers `Dashboard/L*C*_NN_*/` avec versioning daté. Docs vignettes complétées. `DEPENDANCES_GLOBALES.md` enrichi (L1C1→L5C3 ✅). Corrections L5C1 (batteries tronquées - TODO #1 en attente). L5C2 (NE2213 Mamour - TODO #2). L5C3 (chip Weekly amber logique - TODO #3). |
| 2026-05-14 (s20) | Archivage L6C1/L6C2/L6C3 (vignettes + pages YAML + docs + DEPENDANCES). **18/18 vignettes archivées ✅**. Ajout TODO #4 (entity-progress-card absent du référentiel). |  (ligne tronquee dans le fichier d origine, texte perdu)
