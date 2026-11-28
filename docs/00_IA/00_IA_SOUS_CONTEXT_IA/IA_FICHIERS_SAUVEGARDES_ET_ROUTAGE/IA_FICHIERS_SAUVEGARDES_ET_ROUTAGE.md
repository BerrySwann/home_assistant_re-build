# FICHIERS : SOURCE DE VERITE, SAUVEGARDES .bak, VERSIONING, EMPLACEMENTS ET ROUTAGE
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

*Lire ce fichier si : modification d'un fichier (.bak, retour arriere), nom d'un fichier de travail, badges d'une fiche .md, suppression sur H:, TEMPO, corbeille, push vers H:, dossiers XX_ / 98_ / 99_, injection ou extraction par type de fichier, ou va quel fichier.*

> Extrait mot pour mot de `Claude md SAVE/CLAUDE.md` (lignes 253-347, 596-611, 613-625, 767-791, 349-389, 748-766, version du 2026-11-23, date de derniere modification du fichier), le 2026-11-28. Aucun mot modifie dans les sections ci-dessous.

---

## ⚠️ SOURCE DE VÉRITÉ

> Regle du 2026-10-13, unique et sans exception (remplace toutes les anciennes cascades de sources de verite) :

1. A partir du 2026-10-13, chaque fichier est modifie depuis le LOCAL (`ReBuild/`) : le local est la source de verite unique.
2. Aucun fichier n'est modifie en prod (`H:\`, `D:\`) sans que le local ait d'abord ete modifie.
3. Chaque `push_*` (`/ha_push_yaml`, `/ha_push_docs`, `/ha_push_md`) met systematiquement a jour le `.md` (la fiche) du fichier pousse : `03_docs_automations_MD`, `04_docs_scripts_YAML_MD`, `04_docs_scripts_SH_MD`, `02_dashboard_docs_MD`.

**Workflow de modification (depuis le 2026-10-04)** : on ne modifie plus un fichier directement
en prod (H:\). On edite la copie LOCALE (`docs/01_docs_config_system/01_config_system_SH_PY_YAML/`,
image miroir 1:1 de H:\ - voir l'etape C de `ha-trigul` pour la tenir a jour), avec une sauvegarde locale
avant chaque modification (REGLE DE SAUVEGARDE ci-dessous), puis on pousse vers H:\ via
`ha-push-yaml` (MD5-first, confirmation obligatoire). La prod ne recoit jamais de sauvegarde ni de
nom de fichier avec suffixe de date - meme en cas de restauration d'une ancienne sauvegarde, le
suffixe est retire avant la copie vers H:\. En cas d'ambiguite sur quel fichier pousser, on prend
le plus recent (le fichier courant sans suffixe s'il existe, sinon la sauvegarde la plus recente).
Plus aucune sauvegarde (`.bak` ou autre) creee en prod : le SSD du mini PC ne doit pas se remplir.

**REGLE DE MODIFICATION ET RETOUR ARRIERE (quel que soit le fichier)**

- Toute modification se fait d'abord en LOCAL. Aucune edition directe en prod, jamais.
- On pousse ensuite vers H:\ (et D:\) pour valider la modification en prod.
- Coquille ou erreur constatee apres coup, quel que soit le fichier : on reprend la sauvegarde locale
  voulue (`.bak_...`), on retire le suffixe, on la remet en local, puis on la pousse vers H:\. C'est
  le retour arriere de reference - identique pour tous les fichiers (config YAML, dashboard YAML,
  docs .md, scripts, CLAUDE.md).
- Règle d'Eric 2026-10-24 : à chaque modification, si la stratégie choisie ne fonctionne pas ou n'est pas la bonne, Claude revient à l'état d'origine (retour arrière de référence ci-dessus) avant d'essayer autre chose, et le dit à Eric.

**REGLE DE SAUVEGARDE (depuis le 2026-10-08, remplace celle du 2026-10-04)**

- Perimetre : les dossiers `docs/00_*` a `docs/05_*` de `ReBuild/` (config YAML, dashboard YAML,
  automations, scripts, docs .md, contexte IA) et `Claude md SAVE/` (CLAUDE.md). Hors perimetre :
  `TODO/`, `Github/`, `historique/` (sauf `historique/03_RAPPORTS/06_MD5/`, voir plus bas), `.claude/`, `Infra_Proxmox/`. Les copies de `TODO/`, `historique/` et `Infra_Proxmox/` rangees dans `docs/98_sauvegarde_hors_docs` sont, elles, dans `docs`.
- Lieu : en local, a cote du fichier modifie. Jamais sur H:\ ni sur D:\ pour les fichiers de ReBuild et leurs copies (D:\docs, Obsidian). Exception (Eric, 2026-11-01 09h25) : les fichiers d Hermes gardent leur .bak a cote du fichier. Depuis le 2026-11-01 au soir, ils vivent sous `C:\Users\Berry Swann\AppData\Local\hermes` (skills, scripts, boite) ; `D:\hermes` n existe plus.
- Avant CHAQUE modification d'un fichier, creer `{nom}.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}`
  (ex : `P1_kWh_clim.bak_2026_10_08_08h54m30s.yaml`). Format PowerShell :
  `Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"` (les lettres h, m, s entre apostrophes).
- Le nom se termine TOUJOURS par l'extension du fichier (`.md`, `.yaml`, `.txt`...) : la date va
  AVANT l'extension, jamais apres. Un double-clic ouvre la sauvegarde directement.
- Le jour meme : 10 sauvegardes horodatees maximum par fichier. La 11e envoie la plus ancienne
  a la corbeille Windows.
- Fin de journee (regle d Eric du 2026-10-31, precisee a 13h06) : le menage des `.bak` se fait UNIQUEMENT
  au /histo-final du soir (Eric part, en general entre 19h et minuit), jamais au /histo de milieu de
  journee ni lors d un essai de /histo-final fait en journee (avant 19h, sauf ordre d Eric : pas de
  menage). Les modifications du jour sont alors figees : pour chaque fichier, le `.bak` horodate le plus
  recent devient `.bak_AAAA_MM_JJ` (date du jour de sa derniere modification, pas celle du menage : precise par Eric le 2026-10-31) et les autres horodates vont a la corbeille Windows.
  Le lendemain matin il n y a plus de `.bak` horodate : on repart propre. On garde au plus 3
  `.bak_AAAA_MM_JJ` par fichier (3 jours en arriere), le plus ancien va a la corbeille Windows ; au-dela
  de 3 jours, on retrouve la version dans la corbeille.
- Deux menages distincts, a ne pas confondre : le menage des `.bak` de `docs` decrit ici se fait au /histo-final du soir ; le menage des sauvegardes de `TODO\` et de `historique\` est une autre regle, faite par `/histo` (voir le perimetre plus bas et `IA_PROTOCOLES_ET_ECHANGES`, chapitre TODO).
- Badges des `.bak` `.md` : Statut `bak` (orange) tant qu ils sont conserves ; Statut `Trash` (rouge)
  pose juste avant l envoi a la corbeille Windows. Un badge introuvable est ecrit `Inconnu`.
- Corbeille Windows : le menage ne la vide pas. Tout fichier de plus de 3 mois dans la corbeille est
  efface (regle d Eric du 2026-10-31, verification a brancher sur `/histo-final`).
- Perimetre de cette regle : `docs/00_*` a `docs/05_*` et `Claude md SAVE/`. `TODO/` (une
  sauvegarde par jour, sans plafond de jours) et `historique/` (chapitres du skill histo ;
  `historique/03_RAPPORTS/06_MD5/` : 3 jours) ont leurs regles propres. Le jour meme, le plafond reste
  10 sauvegardes horodatees par fichier.
- Regle unique, sans exception : tout fichier de travail porte un nom SANS date, et toutes ses
  versions sont des `.bak_...`. Les dashboards ne sont plus versionnes dans leur nom : le fichier
  courant s'appelle `page_[id].yaml`, `vignette_[id].yaml`, `card_[nom].yaml` (plus de
  `_YYYY-MM-DD_HHhMMmSSs` ni de `_YYYY-MM-DD` dans un nom de fichier).
- Anciens formats, traites par `/histo` avec les memes principes : `{fichier}_YYYY-MM-DD_HHhmm.ext`
  et `{fichier}_YYYY-MM-DD.ext` (dashboards dates) - la version la plus recente devient le fichier
  courant renomme sans date `{fichier}.ext`, les autres sont des anciennes versions : renommees `.bak_AAAA_MM_JJ` (3 jours au plus, le reste a la corbeille Windows) ; `.bak_2026-09-28`, `.bak_20260929`, `.bak2_...`, `.bak-...` :
  renommes en `.bak_AAAA_MM_JJ.{ext}`. Tout souci (collision, date illisible, fichier hors des cas
  ci-dessus) : le signaler a Eric, ne rien supprimer.
- Corbeille Windows : `[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($chemin,
  'OnlyErrorDialogs','SendToRecycleBin')` apres `Add-Type -AssemblyName Microsoft.VisualBasic`
  (teste le 2026-10-08). Pas de corbeille sur H:\ : ne jamais supprimer un fichier de H:\ sans
  avoir verifie qu'il existe en local.
- Repertoire temporaire : `ReBuild\TEMPO\` (decide par Eric le 2026-10-18). C'est le seul dossier pour tout ce qui est temporaire :
  copies de securite avant une suppression en prod (H: n'a pas de corbeille, donc jamais de suppression definitive directe sur H: ; regle precisee par Eric le 2026-10-22 : 1. copier le fichier de H: dans `TEMPO\<operation>_AAAA-MM-JJ\`
  en gardant l'arborescence ; 2. verifier le MD5 de chaque copie contre le fichier de H: ; 3. seulement si tous les MD5 correspondent : mettre les copies de TEMPO a la corbeille Windows (SendToRecycleBin, jamais de suppression definitive), puis supprimer les fichiers sur H: ; si un MD5 differe : ne rien supprimer sur H: et le signaler ; 4. noter le rapport dans le journal des modifs),
  et tout autre besoin de fichiers temporaires (extractions, essais, copies de travail). Ne pas creer d'autre dossier temporaire
  dans ReBuild, sauf un dossier ephemere efface par son propre script (ex : `_tmp_trigul_profond`).
- Vidage de TEMPO (precision d Eric du 2026-10-31 22h10, relevee par Hermes h20261031-17) : le vidage de TEMPO est decide par Eric SEUL. La regle par defaut reste celle des deux regles ci-dessus : copie dans TEMPO, MD5 de chaque fichier, puis copies de TEMPO a la corbeille Windows et suppression sur H:. Les copies ne restent dans TEMPO que dans deux cas : apres un gros changement (pour pouvoir revenir en arriere) ou pour un fichier dit critique par Eric ou Claude. Ces dossiers conserves sont vides par Eric SEUL ; Claude et Hermes ne decident pas seuls qu un changement est gros ni qu un fichier est critique (en cas de doute : poser la question avant de supprimer). Exception (validee par Eric le 2026-11-04 a 19h57, alignement sur Hermes) : les copies de securite du push 5C, `TEMPO\push_5C_L_vers_P_*` pour Claude et `TEMPO\push_histo-final_L_vers_P_*` pour Hermes, partent d'elles-memes a la corbeille Windows apres 7 jours, a chaque push ; jamais de suppression definitive.
- TRI DE TEMPO (decide par Eric le 2026-11-01) : TEMPO contient les sous-dossiers `Groupe_A`, `Groupe_B` et `Groupe_C`, que Eric visualise a la main. Les dossiers d operation neufs arrivent a la racine de TEMPO (a trier). Au tri, Claude compare les MD5 des fichiers de chaque dossier au reste de ReBuild et de H: puis le range : Groupe_A = chaque fichier a une copie identique ailleurs (suppression sans risque) ; Groupe_B = ancien etat remplace, age d au moins 7 jours, local = prod confirme depuis par le trigul ; Groupe_C = a garder (fichier sans autre exemplaire, source originale, fichier qui fait tourner la prod, dossier cite par une regle, moins de 7 jours). Claude presente le tri avec une raison par dossier (deduite des noms, dates et MD5, contenus non lus sauf besoin) et n envoie A et B a la corbeille Windows qu apres le go d Eric ; C est re-propose au tri suivant. Exception : `XX_sauvegarde_2026-10-25` reste a la racine parce que des regles et des skills le citent. Une ligne au journal des modifs par tri.
- Mots de suppression (decide par Eric le 2026-10-25) : quand Eric dit shooter, shoote, shoote-le, vire, vire-le, poubelle, corbeille, corbeille Windows, ou tout autre mot qui veut dire qu'un fichier ou un dossier doit disparaitre, on applique la regle TEMPO ci-dessus sans autre confirmation : 1. copie dans TEMPO ; 2. MD5 de chaque fichier ; 3. si tous les MD5 sont bons, copies de TEMPO a la corbeille Windows puis suppression de l'original sur H: ; 4. note au journal des modifs. Aucun fichier de la prod n'est supprime definitivement sans copie recuperable dans la corbeille Windows. Vaut pour un dossier comme pour un fichier.
- Dossier `historique/03_RAPPORTS/06_MD5/` (ajoute au perimetre par Eric le 2026-10-18, menage des .bak hermes compris) : un sous-repertoire par type de rapport,
  numerotes `00_` a `XX_` : `00_Verif_Final_trigul_arbres` (`trigul_arbres_AAAA-MM-JJ.txt` et `.html`), `01_trigul_profond`,
  `02_categories_ha`, `03_verif_emplacements` (script des emplacements), `04_journal_trigul` (`trigul_journal_AAAA-MM-JJ.log`, ecrit par le lanceur `trigul_run.py`, un fichier par jour). Un nouveau type de rapport = le repertoire suivant (`05_...`, puis `06_...`). Dans chaque repertoire, meme regle
  que le reste (REGLE DE SAUVEGARDE ci-dessus), par fichier de rapport : `rapport.bak_AAAA_MM_JJ_HHhMMmSSs.ext` puis `rapport.bak_AAAA_MM_JJ.ext`. Une sauvegarde
  sans extension prend celle du rapport ; une ancienne `bak_HHhMM_libelle` (sans date) prend la date lue dans le nom du rapport (deduite : a signaler).
  Les rapports eux-memes (un par jour) et les copies `_latest` ne sont pas touches (Eric n'a pas encore dit s'il faut aussi limiter les rapports
  des jours passes a 3 jours). Premier menage execute le 2026-10-18 (dry-run `historique\menage_MD5_dryrun_2026-10-18.txt`, rapport
  `historique\menage_MD5_2026-10-18.txt`), puis tout le dossier a la corbeille sauf les 2 rapports du jour (`historique\menage_MD5_poubelle_2026-10-18.txt`).
  /histo applique cette regle a son etape 5 (skill histo mis a jour le 2026-10-18 ; histo-final et ha-trigul : modification proposee, a enregistrer par Eric).
  Etat au 2026-10-18 : le script des arbres (`hermes_audit_trigul_arbres.py`) ecrit dans `00_Verif_Final_trigul_arbres` (teste ; les 2 rapports du jour y sont) ;
  le script unitaire ecrit dans `01_trigul_profond` (modifie, pas encore lance) ; `02_categories_ha` est ecrit par Claude (etape 6 du protocole trigul profond), pas par un script.
  Les repertoires 01 et 02 restent vides tant que ces rapports ne sont pas regeneres.
- Restauration : copier la sauvegarde voulue, retirer le segment `.bak_...`, jamais de suffixe en prod.
- CLAUDE.md et `docs/00_IA/00_IA_CONTEXT_BASE/IA_CONTEXT_BASE.md` (et leur copie `D:\docs\00_IA\`) : meme regle avant toute
  reecriture (sauvegarde locale uniquement). Apres reecriture, resynchroniser les 3 copies et
  verifier leur MD5.

---

## 📋 VERSIONING FICHIERS - REGLE UNIQUE

> Tous les fichiers de `docs/00_*` a `docs/05_*` et `Claude md SAVE/` suivent UNE seule regle :
> la REGLE DE SAUVEGARDE ci-dessus. Plus aucune distinction dashboard / config / docs.

- Nom de travail : SANS date (ex : `page_L4C2_proxmox.yaml`, `vignette_L4C2_proxmox.yaml`,
  `card_services_ha_z2m_mariadb.yaml`, `P1_kWh_clim.yaml`).
- Versions : sauvegardes `.bak_...` selon la REGLE DE SAUVEGARDE ci-dessus (format, 10 par jour, menage du soir au /histo-final, 3 jours au plus).
- Un nom de fichier ne contient plus jamais de date. Les dashboards ne sont plus versionnes dans
  leur nom de fichier.
- Seule exception conservee : `docs/02_docs_dashboard/02_dashboard_docs_YAML/Dashboard_COMPLET/Dashboard_YYYY_MM_DD.yaml`
  (photo complete du dashboard, une par jour, conservation illimitee) - confirme par Eric le 2026-10-11.
- `Dashboard_COMPLET/` ne se vide JAMAIS (decide par Eric le 2026-10-11) : ses exports sont les mises a jour au fil de l'eau du dashboard complet.
  En local : aucun menage, aucune suppression, aucun `.bak`, aucun renommage. Ne jamais proposer de le purger ni de le consolider.
  (Cote prod, la regle de `/histo` etape 5B reste inchangee : un seul export, le plus recent.)

---

## BADGES DES FICHES .md - REGLE UNIQUE (decidee par Eric le 2026-10-28, completee les 2026-10-30 et 2026-10-31)

- Chaque fiche .md de `docs/` commence par une banniere de 8 badges shields.io, dans cet ordre : Statut, MàJ, HA, IA Partner, Source, Modifs, Expert, Type. Forme d'un badge : `[![Statut](https://img.shields.io/badge/Statut-Actif-0f9d58?style=flat-square)](.)&nbsp;`, le tout dans un `<div align="center">`. Modele : `docs/02_docs_dashboard/02_dashboard_docs_MD/L0C0_PAGE_Home/02_Page/Page_Home.md`. Inventaire des badges existants : `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_BADGES_FICHES/IA_BADGES_FICHES.md` (deplace dans l IA sous contexte par Eric le 2026-10-31, part en prod avec le 5C).
- Valeurs : Statut = Actif (defaut), En cours, A terminer, VERROUILLE, bak_h, bak_d, Trash, Archive ou Original (bak, Trash, Archive, Original ajoutes par Eric le 2026-10-30 ; bak remplace par bak_h et bak_d le 2026-10-31, badges uniquement sur les .md). Couleurs du Statut : Actif 0f9d58 (vert), bak_h et bak_d orange ff9800, Trash rouge f44336, Archive gris 9e9e9e, Original jaune ffeb3b (jaune decide par Eric le 2026-10-31 pour distinguer Original d Archive ; le code ffeb3b est choisi par Claude, a ajuster sur demande). Orange et rouge decides par Eric le 2026-10-30 ; les codes hex ff9800 et f44336 sont choisis par Claude dans la palette Material deja utilisee par les badges, a ajuster sur demande. bak = copie de sauvegarde .md ; Trash = pose juste avant l envoi a la corbeille Windows ; Archive = dossiers archive et XX_ ; Original = Statut des fiches des fichiers *_ORIGINAL (originaux d automations et de scripts), en jaune pour les reperer d un coup d oeil (decide par Eric le 2026-10-31, qui annule la decision du meme jour les mettant en Actif vert). MàJ = date du jour de la creation ou de la derniere modification (dans l'URL, tirets doubles : `2026--10--28`). HA = version de Home Assistant au moment de la creation ou de la mise a jour de la fiche, lue en live (jamais de memoire). IA Partner = `Claude_Sonnet_5.5` (modele configure au moment de l'ecriture, pas une preuve du modele qui a repondu ; si Hermes ecrit la fiche : son nom). Source = `Interne`, sinon le nom de la source avec son lien. Modifs = `Autorisees`, ou `INTERDITES` pour un fichier verrouille. Expert = `HAOS_Proxmox`. Type = Vignette, Page, Carte, Page droite, Page gauche, Dashboard Doc, Vignette Doc, Page Doc, Config Racine, Index_Pages, Scripts (fiche de plusieurs scripts), Script (fiche d un seul script, decide par Eric le 2026-10-30), Script_Executant, System, Dashboard, Automation, README, TUTO, Hacking ou Skill (fiches des skills, Skill ajoute par Eric le 2026-10-31, badge Type en jaune ffeb3b choisi par Claude, a ajuster ; System, IA_System, README, TUTO et Index_Pages sont aussi en jaune ffeb3b (README, TUTO et Index_Pages : ordre d Eric le 2026-10-31, 17h20) (ordre d Eric le 2026-10-31, 17h08) ; Hacking en rouge f44336 ; Automation, Script, Scripts, Script_Executant, Dashboard, Dashboard Doc, Vignette, Vignette Doc, Page, Page gauche, Page droite, Page Doc, Carte, Config Racine en bleu clair 4fc3f7 (plus clair que le bleu HA 03a9f4 ; ordre d Eric le 2026-10-31, 17h18 ; code choisi par Claude, a ajuster) ; les autres Types restent en orange ff9800) (liste a normaliser, une valeur nouvelle se decide avec Eric). Sur un `.bak`, une valeur de badge introuvable s ecrit `Inconnu` (decide par Eric le 2026-10-31).
- HA et MàJ ne sont mis a jour qu'a la creation ou a la modification de la fiche. Aucune mise a jour retroactive, aucun controle de peremption. Une fiche existante garde sa version HA actuelle (information d'origine inconnue) ; une fiche sans badge HA recoit la version actuelle de Home Assistant, lue en live au moment ou on la met en conformite (decide par Eric le 2026-10-28 ; cette version n'est donc pas celle d'origine de la fiche).
- Exemptes : seulement les copies utilisables des skills (`docs/05_docs_skills/05_docs_skills_PURE`, `.bak` compris : le frontmatter doit rester en premiere ligne, identique a claude.ai). Les `.bak` ne sont plus exemptes (regle des `.bak` plus bas) et `docs/00_IA` non plus (ordre d Eric le 2026-10-31 : badges partout). Depuis le 2026-10-31 (ordre d Eric : badges partout sauf les `.bak`), les `MOC_*` (`MOC_SKILLS.md` compris) et `GLOBAL_INDEX_*` ne sont plus exemptes : leurs generateurs (`Gen_GLOBAL_INDEX_automations`, `Gen_GLOBAL_INDEX_vignettes_pages`, `Gen_GLOBAL_INDEX_scripts`, `gen_moc_dashboard`, `gen_moc_docs`) ecrivent la banniere des 8 badges avec `Check_badges_fiches.reconstruire` (une seule regle). Type System pour tout `99_docs_MD_system`. Le gabarit `_Template_doc.md` n est jamais reecrit par `--fix`. Depuis le 2026-10-30, les dossiers `XX_*`, `*_ORIGINAL` et `*_archive*` ne sont plus exemptes : leurs fiches recoivent le Statut Archive (XX_ et archive) ou Original (*_ORIGINAL, jaune, decide par Eric le 2026-10-31).
- Controle (branche sur /histo, etape 6 point 11, nom de trace controles_6F) : script `docs/04_docs_scripts/04_docs_scripts_SH/Check_badges_fiches/Check_badges_fiches.py`, lecture seule sans option ; avec `--fix --limite 20` il cree les badges manquants (20 fiches au plus par passage, un `.bak` a cote de chaque fiche modifiee, jamais de modification d un badge existant, sauf le Statut d un `.bak` : l option `--bak --fix` badge tous les `.bak` de `docs` selon la regle des `.bak` plus bas). Il verifie : fiche sans banniere, badge manquant, valeur hors liste, gabarit non rempli (`{TYPE_DOC}`), lien de badge casse . Etat au 2026-10-30 : controle branche sur /histo, mise aux normes progressive des fiches existantes. Au 2026-10-31 : les exemptions XX_, *_ORIGINAL et *_archive* sont retirees du script, la couleur du Statut suit la valeur (une couleur incoherente est signalee StatutCouleur, jamais corrigee) ; controle en lecture seule : 200 fiches, 184 conformes, 16 a corriger (rien corrige sans ordre d Eric).
- Statut, regles du 2026-10-30 : defaut Actif. REGLE DES .bak (decidee par Eric le 2026-10-31, precisee a 13h06) : voir la REGLE DE SAUVEGARDE plus haut (10 horodates par jour, menage au /histo-final du soir, 3 `.bak_AAAA_MM_JJ` au plus). Un `.bak` horodate du jour porte le Statut `bak_h` et un `.bak_AAAA_MM_JJ` conserve le Statut `bak_d` (orange tous les deux) ; un `.bak` qui part a la corbeille porte le Statut `Trash` (rouge) avant l envoi, avec les autres badges quand c est possible (valeur introuvable : `Inconnu`). Sur un `.bak`, seul le Statut change, les autres badges restent inchanges. Perimetre : `docs` uniquement (pas `historique`), hors `05_docs_skills_PURE`. Le fichier de travail garde son Statut. Etat au 2026-10-31 : 736 `.bak` badges ; 7 a forme non standard restent a la main. La corbeille Windows n est pas videe par le menage ; nouvelle regle d Eric : tout fichier de plus de 3 mois dans la corbeille est efface (verification a brancher sur /histo, pas encore faite). Une fiche envoyee a la corbeille Windows recoit le Statut `Trash` AVANT l envoi (fait par le menage de /histo, etape 5 point 6). Dossiers `*archive*` et `XX_*` : Statut `Archive` ; fichiers `*_ORIGINAL` (originaux d automations et de scripts) : Statut `Original`, en jaune ffeb3b (decide par Eric le 2026-10-31, apres un passage en Actif vert le meme jour, annule). Les badges n existent que sur les `.md`, jamais sur les autres types de fichiers. Passer une fiche en Archive, bak, Trash ou Original ne change que son Statut : le Type (et les autres badges) ne change jamais (decide par Eric le 2026-10-30).
- Exceptions : une fiche a Modifs `INTERDITES` (ex : `PAGE_MAJ.md`) garde son badge Modifs, que Claude ne change jamais ; son Statut est fixe par Eric au cas par cas. Les 3 fiches `L4C3_MAJ_HA` (vignette, page gauche, page droite) sont en Statut Actif depuis le 2026-10-30.
- Type (decide par Eric le 2026-10-30) : pour une fiche sans Type, il suit la categorie du dossier de `docs` : `01_docs_config_system` = System, `02_docs_dashboard` = Dashboard, `03_docs_automations` = Automation, `04_docs_scripts` = Scripts (le script pose Scripts ; une fiche d un seul script passe en Script a la main, 27 fiches passees le 2026-10-31). `00_IA` = IA_System (decide par Eric le 2026-10-31). Hors de ces dossiers, le Type n est pas devine : la fiche est listee `a_decider` et tranchee avec Eric. Un Type deja present n est jamais change par le script. Types poses a la main sur ordre d Eric le 2026-10-30 : README pour le README du depot, TUTO pour les tutoriels, Hacking pour 01_Pont_hue_hacking. Une valeur hors liste (`Script_Executant` ou `VERROUILLE` ecrits avec accent, `Tutoriel`, `Technique`) est signalee, jamais corrigee sans demande.
- Prod : les fiches badgees partent en prod avec le push general de /histo (etape 5C : tout `docs` hors `XX_`, hors `99_docs_MD_system` (sauf ENTITES_GLOBAL_INDEX.md) et hors `.bak`) ; le rattrapage des fiches modifiees par le controle est l etape 6 point 13.

---

## 📅 RÈGLE DE VERSIONING (scripts YAML, automations et docs)

Un fichier versionnable suit la **règle unique de versioning** (voir REGLE DE SAUVEGARDE) : le nom du
fichier de travail ne porte **jamais** de date ; chaque version précédente est une sauvegarde
`.bak_AAAA_MM_JJ.{ext}` (consolidée par `/histo`).

Quand un script YAML de `docs/04_docs_scripts/04_docs_scripts_YAML/` (ou tout fichier versionnable) est modifié :
1. Avant modification, une sauvegarde locale `.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}` est créée à côté du fichier.
2. Le fichier de travail garde son nom **SANS date** : `p1_master_gestion_clim.yaml`.
3. Chaque fichier porte un **en-tête commenté** avec l'historique des versions (date + changement).
4. La fiche MD correspondante pointe vers le fichier de travail et son changelog liste **les différences à chaque itération**.

**Automations (`docs/03_docs_automations/03_docs_automations_YAML/`)** — même règle :
quand une fiche YAML d'automation est mise à jour (resync depuis `automations.yaml`, ajout d'`id`,
correction de template...), la **version précédente reste à côté sous forme de sauvegarde**
`.bak_AAAA_MM_JJ.{ext}` : `congelateur_alarme_porte.yaml` (version active, avec `id`) +
`congelateur_alarme_porte.bak_2026_09_01.yaml` (version précédente, sans `id`).
Exemple : les 3 alertes Congélateur — fiches du 2026-09-01 mises à jour le 2026-09-10
(ajout des `id` HA depuis le live), l'ancienne version devenant `.bak_2026_09_01`.

→ `H:/scripts.yaml` (Scripts, section Automations - miroir local `docs/04_docs_scripts/`) suit la meme regle que la config YAML : sauvegarde locale (`.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}`, voir REGLE DE SAUVEGARDE) a cote du fichier dans `docs/04_docs_scripts/` AVANT toute modification, jamais de sauvegarde creee en prod. Difference : le push vers `H:/scripts.yaml` se fait a la main par Eric via l'UI HA (jamais de copie fichier directe) - coherent avec la regle Automations (jamais d'edition directe du fichier live). Les `.sh` de `.scripts/` restent geres individuellement, hors de cette regle. Audit MD5 automations/scripts : plus complexe que sur la config YAML simple, a traiter au cas par cas.

→ Arborescences complètes prod + local : `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_ARBO_DETAIL/IA_ARBO_DETAIL.md`

---

### 📄 DOCS (.md + .yaml dashboard) - emplacements

> Deux types de fichiers :
> - `.md` : `docs/02_docs_dashboard/02_dashboard_docs_MD/` · `docs/03_docs_automations/03_docs_automations_MD/` · `docs/04_docs_scripts/04_docs_scripts_YAML_MD/` · `docs/04_docs_scripts/04_docs_scripts_SH_MD/` · etc.
> - `.yaml` dashboard : `docs/02_docs_dashboard/02_dashboard_docs_YAML/` (vignettes, pages, cartes, Dashboard_COMPLET)

Copie de prod : `H:\Docs\` (poussee depuis le local, ne jamais la modifier directement). GitHub `home_assistant_re-build` : backup via git auto depuis HA, reflet de la prod.

`H:\Docs\` (racine, hors `01_docs_config_system\01_config_system_SH_PY_YAML\`) ne contient QUE des .md, histo et yaml Dashboard - **jamais de YAML config HA**.
`H:\docs\01_docs_config_system\01_config_system_SH_PY_YAML\` est l'image locale miroir de la config YAML de prod (sensors, templates, utility_meter, command_line, groups, input_booleans, shell_command, themes, blueprints) - alimentee par la comparaison de `ha-trigul` (etape C, reprise de l'ancien skill `ha-resync-docs`, supprime le 2026-10-20) et par les push normaux (`ha-push-yaml`). Exception documentee a la regle ci-dessus, pas une contradiction.
`/config/notifs/` (`H:\notifs`) : TOUS les fichiers sont vivants (journaux regeneres par HA en continu). Ils ne vont jamais dans `docs/` (ni local, ni miroir `H:\docs`, ni `docs/` de GitHub) : pas de copie, pas de push, pas de bak de la part de Claude ; lecture seule sur `H:\notifs`. Ils sont sauvegardes au fil de l'eau sur GitHub, a la racine du depot (`notifs/`), par le backup HA : c'est voulu, pour retrouver les donnees anterieures si quelque chose casse (regle d'Eric du 2026-10-18).
- REGLE XX_ (decidee par Eric le 2026-10-25) : tout dossier dont le nom commence par `XX_` est LOCAL SEUL. Il n'est jamais pousse en prod (`H:`), jamais sur GitHub, et il est exclu des comparaisons de push et des audits prod/GitHub (trigul). Liste des dossiers : celle du manifeste `XX_manifest.json` (source qui fait foi, controlee par `Check_XX_presents.py`), sans enumeration ici pour qu elle ne devienne pas fausse (idee 4 de Hermes, h20261101-15, acceptee par Eric 2026-11-01) ; `99_docs_MD_system` y figure mais n est pas un dossier `XX_` (voir sa regle).  CONVENTION DE NOMMAGE (decidee par Eric le 2026-11-01) : un dossier `XX_` peut porter le suffixe ` (a ne pas jeter)` - espace, parenthese ouvrante, minuscules, sans accent - pour dire qu'il ne doit pas partir a la corbeille. Ce suffixe FAIT PARTIE DU NOM : il figure dans tout chemin, dans le manifeste et dans les fiches, et il ne se retire que sur ordre d'Eric. Un outil ne reconnait jamais un dossier `XX_` par une liste de noms : il teste le prefixe `XX_` ou lit le manifeste. Poser ce suffixe ne change pas la regle : le dossier reste LOCAL SEUL. Si un dossier `XX_` apparait en prod, ne pas le copier ailleurs : le signaler a Eric, qui decide (retrait avec la regle de suppression TEMPO). Restent aussi locaux, hors de `docs`, jamais en prod (confirme par Eric le 2026-10-25) : `TEMPO`, `Claude md SAVE\ARCHIVE`, `HTML`, `MOC`, `historique`. A cela s'ajoutent les interdits de push deja ecrits plus haut (`.bak`, fichiers de travail, `secrets.yaml`, `Dashboard_COMPLET`, `.md` dates et `_ARCHIVE`). CONTROLE DE PRESENCE (decide par Eric le 2026-10-25 21:19) : ces dossiers n'existent qu'en local, ils ne doivent jamais se perdre. Avant CHAQUE push (/ha-push-docs, /ha-push-md, /ha-push-yaml, et les skills equivalents de Hermes), lancer `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"` : il compare les dossiers XX_ et leurs fichiers au manifeste `XX_manifest.json` (range dans `docs\04_docs_scripts\04_docs_scripts_JSON\Check_XX_presents\`, deplace le 2026-11-01) (nombre de dossiers et de fichiers : voir le manifeste). Un dossier ou un fichier manquant = ALERTE : ne rien pousser, prevenir Eric, restaurer depuis `TEMPO\XX_sauvegarde_2026-10-25` sur son ordre. Le manifeste ne se met a jour (`--maj`) que sur ordre d'Eric ; tout dossier XX_ cree ou retire se declare a Eric.
- REGLE 99_docs_MD_system (decidee par Eric le 2026-10-31) : `docs\99_docs_MD_system` (ancien `XX_docs_MD_system`, renomme parce que ce sont des fichiers vivants et non des archives) est LOCAL SEUL comme un dossier `XX_` : jamais en prod, jamais sur GitHub, exclu de l etape 5C, du trigul et des audits prod/GitHub. EXCEPTION (Eric, 2026-10-31 17h33) : le seul fichier `docs\99_docs_MD_system\ENTITES_GLOBAL_INDEX\ENTITES_GLOBAL_INDEX.md` (jamais ses `.bak`) est pousse en prod au 5C, pour etre sauvegarde sur GitHub ; `Check_XX_presents.py` l autorise en prod (PROD_AUTORISE) et signale tout autre fichier de `99_` present en prod. Difference avec `XX_` : ses fiches ont le Statut Actif. `Check_XX_presents.py` le surveille comme les `XX_` (manifeste `XX_manifest.json`, nom conserve).
- REGLE 98_sauvegarde_hors_docs (decidee par Eric le 2026-10-31) : `docs\98_sauvegarde_hors_docs` contient une COPIE de `Infra_Proxmox`, `TODO` et `historique` (dossiers a la racine de ReBuild, hors `docs`) pour qu'ils soient sous GitHub. Elle est creee par `docs\04_docs_scripts\04_docs_scripts_SH\Sync_98_sauvegarde\Sync_98_sauvegarde.py` (a lancer en `exec` avant chaque 5C) : jamais de correction dans la copie, on corrige l'original. Elle va en prod avec le 5C. Exclus de la copie : `.bak` (sauf ceux d'`Infra_Proxmox`, gardes dans la copie locale et nommes `nom.bak_AAAA_MM_JJ.ext`, mais jamais pousses en prod : le 5C n'envoie aucun `.bak`, decision d'Eric du 2026-11-23), `.avant_*`. Dans la copie, identifiant, mot de passe, cle reseau Zigbee (fichier Sonoff 2026-05-23) et jetons `ghp_` sont caviardes (`***`). Ignoree par Check_badges_fiches, gen_moc_docs et gen_moc_dashboard.
- PUSH GENERAL EN PROD (decide par Eric le 2026-10-30, ecrit le 2026-10-31) : l etape 5C de /histo et /histo-final pousse vers `H:\docs` TOUT `docs` hors dossiers `XX_`, hors `99_docs_MD_system` (sauf ENTITES_GLOBAL_INDEX.md) et hors `.bak`, avec MD5 avant et apres, sans demander. `98_sauvegarde_hors_docs` est INCLUS dans le push (copie de `Infra_Proxmox`, `TODO` et `historique` faite par `Sync_98_sauvegarde.py` avant chaque 5C, secrets caviardes). Garde-fou : un fichier dont la prod differe du local n est ecrase que si la prod est identique a une ancienne version connue (`.bak` ou ancien local) ; sinon `PROD DIFFERENTE INCONNUE`, rien n est pousse et Eric est prevenu. Les interdits de push ecrits plus haut restent valables. Consequence : `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` et les copies de skills `docs/05_docs_skills` partent en prod (remplace les decisions du 2026-10-25 et du 2026-10-11 qui les gardaient en local). GitHub n est alimente que par le backup HA lance par Eric.
- SKILLS (decide par Eric le 2026-10-31) : `docs\05_docs_skills` contient `05_docs_skills_PURE\skill_<nom>\<nom>.md` (copie utilisable, en anglais pour economiser des tokens, sans badges, identique au skill installe, seule zone exemptee de badges), `05_docs_skills_MD\skill_<nom>\<nom>.md` (une fiche explicative en francais par skill, 8 badges, Type Skill jaune ffeb3b) et `MOC_SKILLS.md` (genere par `gen_moc_docs`, colonnes Skill, Anglais, FR, Explication, Date). Quand un skill change, relire et mettre a jour sa fiche FR. REGLE DU MIROIR (Eric, 2026-10-31) : `H:\docs` est le miroir de `docs` local et GitHub se sauvegarde depuis la prod ; un dossier qui n existe plus en local (anciens `H:\docs\05_docs_skills\skill_*` a plat) doit disparaitre de la prod, apres copie dans `TEMPO\<operation>_AAAA-MM-JJ\` et MD5 verifie (regle TEMPO).

> ⚠️ Audit MD5 docs : couvre les `.md` ET les `.yaml` dashboard (`02_dashboard_docs_YAML/`). Ne pas oublier les yaml lors d'un audit de cohérence local vs H:\Docs\.

> Ancien repo `home-assistant-config` **supprimé définitivement** (2026-04-27). Seul `home_assistant_re-build` est actif.

### Règles fondamentales
- Répertoires préfixés `P*_` selon le Pôle.
- `docs/` = YAML config HA (état cible → /homeassistant/) - audité 1×/semaine.
- `docs/03_docs_automations/03_docs_automations_YAML/` = automations individuelles (référence locale).
- `docs/02_docs_dashboard/02_dashboard_docs_YAML/` = vignettes/pages dashboard.
- ⛔ `TREE_CORRIGE/` et `TREE_ORIGINE/` **n'existent plus** - tout est sous `docs/`.
- Fichiers absents de `docs/01` mais présents GitHub = à supprimer en prod.
- Automations : jamais modifier `automations.yaml` direct → passer par l'API HA depuis la copie locale (ou par l'UI HA, Eric) + `docs/03_docs_automations/03_docs_automations_YAML/`.

### Qui fait quoi - extraction / injection (par type de fichier)

| Type | Injection en prod | Extraction / stockage local |
|:-----|:-------------------|:-----------------------------|
| **Config YAML** (sensors/templates/UM/command_line) | Edition depuis la copie LOCALE `docs/01_docs_config_system/01_config_system_SH_PY_YAML/`, sauvegarde locale `.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}` avant modif (REGLE DE SAUVEGARDE), puis push vers `H:\` via `ha-push-yaml` (MD5-first, confirmation obligatoire) | Le fichier local (sans suffixe de date) est deja la reference - pas d'extraction a faire apres coup |
| **Automations** | Le plus souvent Claude, par l'API HA, depuis la copie LOCALE (.bak local avant, voir ORDRE DE TRAVAIL de CLAUDE.md) ; Eric peut aussi le faire a la main dans l'UI HA. Jamais `automations.yaml` en direct | Une fois validée, **Claude** récupère uniquement le bloc modifié et le stocke individuellement dans `docs/03_docs_automations/03_docs_automations_YAML/{Pole}/` |
| **Dashboard** | Le plus souvent Claude, par l'API HA, depuis la copie locale (.bak local avant) ; Eric peut aussi le faire a la main dans l'UI HA (Parametres -> Tableau de bord -> Modifier en YAML) | Pas d'extraction automatique quand Eric edite dans l'UI HA - **Eric** récupère le code à la main et le colle. **Claude** vérifie, stocke dans `docs/02_docs_dashboard/02_dashboard_docs_YAML/L{x}C{x}_.../` sous le nom de travail **SANS date**, avec une sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}` avant chaque modification (REGLE DE SAUVEGARDE) |

> Raison de l'asymétrie Dashboard : limitation technique - pas d'accès filesystem direct au Lovelace YAML comme pour `/config`.

---

## 🌳 ROUTAGE DES FICHIERS (où va quoi)

| Type de fichier | Emplacement local (source) | Destination |
|:---|:---|:---|
| Config YAML (sensors, templates, utility_meter, command_line...) | `docs/01_docs_config_system/01_config_system_SH_PY_YAML/` | push `H:\` via `ha-push-yaml` |
| Docs `.md` (dashboard, automations, scripts, system) | `docs/0x_*_MD/` | push `H:\Docs\` via `ha-push-docs` / `ha-push-md` |
| Dashboards YAML (vignettes, pages, cartes) | `docs/02_docs_dashboard/02_dashboard_docs_YAML/` | push `H:\Docs\` |
| Automations YAML | `docs/03_docs_automations/03_docs_automations_YAML/` | UI HA à la main, jamais en direct |
| Scripts YAML + `.py` | `docs/04_docs_scripts/04_docs_scripts_YAML/` | UI HA à la main, jamais en direct |
| Hors ménage, hors circuit de push | `Github/` · `.claude/` | restent locaux |
| Originaux locaux, copie dans `docs/98_sauvegarde_hors_docs` (en prod par le 5C, copie faite par `Sync_98_sauvegarde.py`) | `TODO/` · `historique/` · `Infra_Proxmox/` | copie en prod, original local |

> Le détail des arborescences (local, prod, GitHub, comptages) vit dans
> `docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_ARBO_DETAIL/IA_ARBO_DETAIL.md`, maintenu par `/histo` (étape 6).
> **En cas de divergence, c'est ce fichier qui fait foi** : il est recompté à chaque passage,
> contrairement à cette page. Ne pas recopier d'arborescence ici.

⛔ `TREE_CORRIGE/`, `TREE_ORIGINE/`, `Dashboard/`, `docs_dashboard/`, `docs_automations/`, `docs_scripts/` **supprimés le 2026-07-14** - tout est sous `docs/`.

<!-- annotations_log: [2026-11-28] creation par extraction de CLAUDE.md pour l'alleger (demande d'Eric), contenu inchange -->
<!-- annotations_log: [2026-11-28] dedup_bak : dedoublonnage de la regle .bak : 3 copies remplacees par un renvoi vers REGLE DE SAUVEGARDE, precision date du .bak du soir, menage TODO/historique (/histo) distingue du menage .bak docs (/histo-final) (accord d Eric 2026-11-28) -->
<!-- annotations_log: [2026-11-28] qui_fait_quoi : Qui fait quoi aligne sur la regle de l'ordre de travail de CLAUDE.md : automations et dashboards pousses le plus souvent par Claude via l'API HA depuis la copie locale (.bak avant), Eric peut le faire dans l'UI HA (demande d'Eric 2026-11-28) -->
