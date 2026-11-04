---
name: "histo"
description: "Skill HA ReBuild - genere un journal de bord ultra-compact et le sauvegarde, puis enchaine automatiquement le sync_index (DEPENDANCES_GLOBALES_CLAUDE_memoire.md, docs impactees, GLOBAL_INDEX_REPO.md), le journal fusionne et la copie Obsidian et le menage des sauvegardes .bak puis la mise a jour du tree (IA_ARBO_DETAIL.md). Declencher OBLIGATOIREMENT quand l'utilisateur tape /histo, demande un journal de bord, genere l'histo, fais un resume a sauvegarder, cree un log de session, exporte l'historique. Usage typique : fin de session, avant de fermer Cowork."
---

# Skill : /histo - Journal de bord + sync_index (dont GLOBAL_INDEX_REPO) + journal fusionne + copie Obsidian + menage .bak + tree

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18, point 9 de l'etape 6).

## Objectif

Six actions, plus les etapes 5B et 5C, enchainees sans interruption :
1. Generer et sauvegarder le journal de bord de session
2. Executer le sync_index (DEPENDANCES_GLOBALES_CLAUDE_memoire.md, docs impactees, GLOBAL_INDEX_REPO.md, GLOBAL_INDEX_AUTOMATIONS.md, GLOBAL_INDEX_VIGNETTES_PAGES.md, GLOBAL_INDEX_SCRIPTS_SH.md, GLOBAL_INDEX_SCRIPTS_PY.md, GLOBAL_INDEX_SCRIPTS_YAML.md, IA_GLOBAL_INDEX_memoire.md), puis le recapitulatif des entites en fin des index globaux, APRES les generateurs (`Recap_index.py`, regle d'Eric du 2026-11-03)

3. Mettre a jour le JOURNAL FUSIONNE (historique\02_HISTO_ET_FUSIONNE\FUSIONNE\) avec la session qui vient d'etre ecrite
4. Copier le journal de session et le journal fusionne dans le coffre Obsidian
4B. Generer les pages HTML sombres du journal du jour et du fusionne (histo_html.py), puis mettre a la corbeille Windows les originaux .md/.txt convertis (etape 4B)
5. Faire le menage des sauvegardes (.bak) : `docs` et `Claude md SAVE` seulement quand l'histo est definitif (question Oui/Non posee par /histo-final), puis `historique\03_RAPPORTS\06_MD5\`, les pages HTML de `historique\01_JOURNAL_TRACE\` et `historique\02_HISTO_ET_FUSIONNE\`, `TODO\`, le reste de `historique\`, et la purge de la corbeille Windows (elements de plus de 3 mois). Details : `histo_ref_menage.md`
5B. Verifier l'export Dashboard depose a la racine de la prod et ne garder qu'un export en prod (etape 5B)
5C. Faire les copies de reference de `automations.yaml`, `scripts.yaml` et `configuration.yaml` (`Copie_reference.py`, regle d'Eric du 2026-11-02), puis pousser en prod tout `docs` hors `XX_` et hors `.bak`, avec MD5 avant et apres et copie TEMPO de l'ancienne prod avant chaque ecrasement (etape 5C, decide par Eric le 2026-10-30, garde-fous du 2026-11-03)
6. Mettre a jour les tree : IA_ARBO_DETAIL.md (comptages local, prod, GitHub), avec le skill update-arbo (etape 6)
6B. Controler les fichiers de 00_IA_SOUS_CONTEXT_IA (12 au 2026-11-04) (lecture seule, rapport d'ecarts, etape 6 point 7)
6C. Controler tous les index globaux (lecture seule, rapport d'ecarts, etape 6 point 8)
6D. Controler les fichiers a plusieurs emplacements (lecture seule, rapport d'ecarts, etape 6 point 9)
6E. Controler les integrations File (notify) de HA contre leur fiche (lecture seule, rapport d'ecarts, etape 6 point 10)
6F. Verifier les fiches .md (une fiche par source) et la presence des 8 badges, creer les badges manquants dans la foulee (etape 6 point 11, ajoute par Eric le 2026-10-28)
6G. Controler la fraicheur de DEPENDANCES_GLOBALES_CLAUDE_memoire.md et IA_GLOBAL_INDEX_memoire.md (lecture seule, corrections par Claude, etape 6 point 12)
6H. Controler la prod fonctionnelle : les fichiers vitaux de la prod (palier 1, 98 fichiers) doivent etre verts en prod racine, local et miroir docs ; la colonne GitHub est seulement notee (lecture seule, etape 6 point 14, ajoute par Eric le 2026-10-31, precise le 2026-11-03)
6I. Reparer les ecarts NOUVEAUX apparus pendant la session, puis relancer le controle jusqu'a 0 ; les ecarts anterieurs vont dans le rapport (etape 6 point 15, regle 6 d'Eric du 2026-11-01)

Ne jamais demander confirmation entre les etapes. Les faire dans la foulee. Seule exception : le DRY-RUN du menage (etape 5) a la premiere execution sur un dossier, qui s'arrete pour presenter la liste et attendre le go de l'utilisateur (voir les garde-fous de l'etape 5).

## HISTO DEFINITIF OU NON (decide par Eric le 2026-10-31)

Le menage des `.bak` de `docs` et `Claude md SAVE` n'a lieu que si l'histo est definitif.
- /histo seul (milieu de journee) : non definitif, pas de menage de ces deux perimetres.
- /histo-final : poser la question avec AskUserQuestion, au tout debut : "Histo final definitif ?", deux choix : Oui (menage fait) et Non (essai, pas de menage, il sera fait au prochain histo definitif). Pas de reponse (session sans personne) : Non.
- Noter le choix dans la trace : `histo_trace.py note menage "definitif : oui|non"`, et le dire dans le rapport.

## FICHIERS DE REFERENCE (a lire seulement quand l'etape correspondante est executee)

Dossier : `C:\Users\Berry Swann\Documents\ReBuild\docs\05_docs_skills\05_docs_skills_PURE\skill_histo\`
- `histo_ref_sync_index.md` : etapes 2 (sync_index, index generes, recapitulatif des entites, GLOBAL_INDEX_REPO) et 3 (journal fusionne).
- `histo_ref_menage.md` : etape 5 (menage des `.bak`, chapitres historique, TODO, MD5), 5B (export Dashboard) et 5C (copies de reference, regle des garde-fous, push en prod de `docs`).
- `histo_ref_controles.md` : etape 6 (tree, controles, badges, rattrapage du push, prod fonctionnelle, reparation des ecarts nouveaux) et format du rapport final.
Si un fichier de reference est introuvable : le dire en tete du rapport et arreter l'etape concernee, ne pas la refaire de memoire.

## ETAPE 2 - SYNC_INDEX et ETAPE 3 - JOURNAL FUSIONNE

Enchainees sans demander, apres l'etape 1. Lire `histo_ref_sync_index.md` et suivre toutes ses regles. Trace : `debut sync_index` / `fin sync_index`, `debut fusionne` / `fin fusionne`.

## JOURNAL DE TRACE (demande par Eric le 2026-10-19, commun a /histo et /histo-final)

Pour voir ou la sequence plante ou se bloque en silence, et garder la trace des validations demandees a Eric, ecrire une ligne avant et apres chaque etape avec `histo_trace.py` : `python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\histo_trace\histo_trace.py" <commande>`. Journal brut : `historique\01_JOURNAL_TRACE\LOGS\histo_trace_AAAA-MM-JJ.log` (un par jour, chaque ligne forcee sur le disque ; dossier renomme `01_JOURNAL_TRACE` par Eric le 2026-10-21 pour etre en haut de `historique\`). Les `.log` sont hors perimetre du menage .bak. Les pages HTML directement dans `01_JOURNAL_TRACE\` ont leur propre regle de menage (chapitre "Cas particulier : historique\01_JOURNAL_TRACE\" plus bas).

- Commandes : `seq-debut histo|histo-final`, `debut ETAPE [texte]`, `fin ETAPE OK|ATTENTION|ECHEC [texte]`, `validation ETAPE texte`, `note ETAPE texte`, `seq-fin`, `verifier`, `recap`, `html`.
- Appele seul (/histo) : ecrire `seq-debut histo` au debut et `seq-fin` apres le rapport final. Appele par /histo-final : ne pas ecrire `seq-debut` ni `seq-fin` (c'est /histo-final qui ouvre et ferme la sequence), seulement les `debut` / `fin` des etapes.
- Noms d'etape : journal (etape 1), sync_index (2), fusionne (3), obsidian (4), pages_html (4B), menage (5), export_5B (5B), push_docs (5C), tree (6 points 1 a 6), controles_6B (point 7), controles_6C (point 8), controles_6D (point 9), controles_6E (point 10), controles_6F (point 11), controles_6G (point 12), controles_6H (point 14), tokens (notes de comptage, voir ci-dessous), rapport.
- A la fin (apres le rapport) : lancer `histo_trace.py verifier` et mettre sa sortie dans le rapport final (ligne TRACE). Appele seul (/histo) : lancer aussi `histo_trace.py recap` apres `seq-fin` (lecture seule) ; sa sortie horodate chaque tache : heure de debut de la tache 1, puis pour chaque tache suivante la duree de la tache precedente et son heure de debut (demande d'Eric le 2026-10-21) ; la mettre dans le rapport final (ligne HORODATAGE). Appele par /histo-final : ne pas la lancer, c'est /histo-final qui la lance. Appele seul (/histo) : lancer ensuite `histo_trace.py html` (demande d'Eric le 2026-10-21) : il ecrit la page HTML du jour `historique\01_JOURNAL_TRACE\histo_trace_AAAA-MM-JJ.html` (toutes les sequences du jour, duree de chaque tache, resultat de la ligne FIN, notes) et refait `index.html` ; si la page du jour existe avec un contenu different, il la copie d'abord en `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html` ; page identique : rien n'est ecrit. Mettre sa sortie dans le rapport final (ligne PAGE). Appele par /histo-final : ne pas le lancer, c'est /histo-final qui le lance.
- Une ligne `debut` sans `fin` revele un blocage silencieux (appel qui n'a jamais rendu la main, par exemple une validation restee sans reponse). Une sequence sans `seq-fin` revele une interruption (PC eteint, session fermee, plantage).
- Limite : Claude ne voit pas l'ecran d'Eric. Il ne sait qu'une validation a ete demandee que si le resultat de l'outil le dit (refus, attente, message d'approbation) ; sinon la trace montre seulement une etape longue ou sans fin. Ne jamais inventer une ligne `validation`.
- Pas de secret dans les messages du journal. Si le script de trace est absent ou echoue : le dire dans le rapport et continuer (la trace ne bloque jamais la sequence).

### Comptage des tokens (demande par Eric le 2026-10-28, commun a /histo et /histo-final)

Claude ne dispose pas d'une facture de tokens. Seule mesure disponible : le compteur de tokens restants de la session (valeur `total_tokens left` visible apres les appels d'outils). Methode :

1. Au tout debut de la sequence (avant la premiere etape) : relever la valeur du compteur et l'ecrire dans la trace : `histo_trace.py note tokens "debut : N restants"`. Appele par /histo-final, c'est /histo-final qui fait ce releve avant l'etape 1 : ne pas le refaire.
2. A la fin de la sequence (juste avant le rapport final) : relever la valeur, ecrire `histo_trace.py note tokens "fin : M restants"`.
3. Dans le rapport final, ligne TOKENS : consommes = N - M, avec le mot "deduit" et la mention "compteur de session, pas une facture". Si l'un des deux releves manque : ecrire "inconnu", jamais de valeur approximative. La consommation de l'ecriture du rapport final lui-meme n'est pas comptee (releve fait avant).
4. Si le compteur n'est pas visible dans la session : ecrire "inconnu (compteur non visible)".

---

## ETAPE 1 - JOURNAL DE BORD

### Collecter depuis l'historique de la conversation

- Date du jour (depuis env ou bash)
- Numero de session du jour (S1, S2, S3... selon les journaux `histo_*.md`/`.txt` presents dans `historique\02_HISTO_ET_FUSIONNE\` ET le nombre de sessions deja dans la page `histo_AAAA-MM-JJ.html` du jour : une balise `<section>` par session ; les anciens originaux sont a la corbeille apres conversion)
- Fichiers YAML modifies/crees/valides (chemin court sous `docs/`)
- Entites creees ou corrigees (unique_id ou alias)
- Erreurs rencontrees et leur resolution
- Tache en cours ou terminee
- Backlog TODO.html si mentionne en session
- Prochaine action prioritaire

### Format de sortie obligatoire (Markdown mis en forme, depuis le 2026-10-08)

Le journal est du vrai Markdown (titres, gras, pastilles de couleur, icones), pas un bloc de code. Gabarit :

```
# 📓 Journal HA ReBuild - **[DATE]** (Session **S[N]**)

- ⏱️ **Session** : [duree estimee ou "N/A"]
- 🌿 **Branche active** : `docs/`

## ✅ Fichiers valides
- 🟢 `chemin/court/fichier.yaml` - [entite(s) concernee(s)] **[v]**
- ...

## 🟠 En cours
- 🟠 `fichier ou tache` - **[draft]** ou **[a tester]** ou **[a deployer]**
- (aucun si session terminee proprement)

## 🔴 Erreurs resolues
- 🔴 `fichier` : [type erreur] -> [correction appliquee] **[resolu]**
- (aucune si session propre)

## 📋 Taches backlog (TODO.html)
- 📌 [items identifies en session, si applicable]

## 🎯 Prochaine action
- [action prioritaire identifiee]

*Fin du journal*
```

Regles de mise en forme :
- Toute date est en gras (`**2026-10-08**`), dans le titre comme dans le texte.
- Tout commentaire ou etat entre crochets est en gras : `**[v]**`, `**[a tester]**`, `**[draft]**`, `**[a deployer]**`, `**[resolu]**`, `**[EN COURS]**`.
- Pastilles de couleur : 🟢 valide ou termine, 🟠 en cours ou a tester, 🔴 erreur, 🔵 information. Une icone par titre de rubrique comme dans le gabarit.
- Chemins, IDs d'entites et commandes en code inline (accents graves).
- Cette mise en forme s'applique uniquement aux NOUVEAUX journaux `histo_*.md`. Les anciens journaux, GLOBAL_INDEX_REPO.md et les autres fichiers restent inchanges et sans emoji (exception d'emojis accordee par Eric le 2026-10-08, limitee aux nouveaux journaux histo). Les nouveaux blocs de session du journal fusionne ont seulement le gras, sans emoji (etape 3).

### Sauvegarde obligatoire

- Determiner le numero de session : lister `historique\02_HISTO_ET_FUSIONNE\` (fichiers `.md` ET anciens `.txt`) ET compter les sessions de la page HTML du jour (`<section>`), puis choisir le suffixe suivant (le plus grand des deux + 1) (ex : si `histo_2026-08-08_s2.txt` ou `histo_2026-08-08_s2.md` existe -> creer `histo_2026-08-08_s3.md`)
- Sauvegarder dans `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\histo_[YYYY-MM-DD]_s[N].md` : le journal est ecrit en Markdown mis en forme, tel que defini ci-dessus, sans le placer dans un bloc de code (sinon gras et icones ne s'affichent pas). Les anciens journaux ont ete convertis en HTML le 2026-10-21. Ce `.md` est la source de la page HTML du jour (etape 4B) : il part a la corbeille Windows une fois la page generee et verifiee (decision d'Eric le 2026-10-21).
- Presenter le fichier avec `mcp__cowork__present_files` (si l'outil n'est pas disponible, le dire dans le rapport final, ne pas bloquer)

### Regles

- Chemins courts (ex : `docs/01_docs_config_system/01_config_system_SH_PY_YAML/sensors/P1_kWh_clim.yaml`)
- IDs matrice pour les vignettes (L2C1, L1C3, etc.)
- Si session vide : indiquer `SESSION VIDE - aucune modification`
- Bloc autonome : lisible sans contexte par quelqu'un qui reprend le projet plus tard

---
## ETAPE 4 - COPIE OBSIDIAN (enchainee automatiquement, sans demander)

**Dossier de destination :** `D:\Cerveau-Obsidian\14 Boulot\Journal\`

### A copier

- le fusionne qui vient d'etre ecrit a l'etape 3
- le journal `histo_[date]_s[N].md` de l'etape 1
- tous les `histo_*.md` / `histo_*.txt` plus recents que ceux deja presents dans le dossier Obsidian (cas d'un rattrapage)
- depuis le 2026-10-21 la copie se fait AVANT l'etape 4B, qui envoie les `.md` convertis a la corbeille ; les pages HTML ne sont pas copiees dans Obsidian (non demande)

### Regles

- Ne jamais ecraser un fichier existant du dossier Obsidian : s'il existe deja, ne pas le copier et le signaler. Seule exception : un fusionne de meme nom (mise a jour du meme jour), qui est ecrase SANS sauvegarde sur D: (regle : jamais de sauvegarde sur D:). La version precedente reste dans `historique\02_HISTO_ET_FUSIONNE\FUSIONNE\` (sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}` faite a l'etape 3).
- L'ancien fusionne reste dans le dossier Obsidian.
- Apres chaque copie, comparer le MD5 source / destination et le noter dans le rapport (`identique` ou `DIFFERENT`).
- Si `D:\` ou le dossier est inaccessible : le signaler dans le rapport, ne pas bloquer et ne pas creer d'autre dossier a la place.

---

## ETAPE 4B - PAGES HTML SOMBRES ET CORBEILLE DES ORIGINAUX (enchainee automatiquement, sans demander, apres la copie Obsidian ; decide par Eric le 2026-10-21)

Les journaux de session et les journaux fusionnes sont lisibles en HTML sombre (meme palette que `TODO\TODO.html`) : une page par jour pour les journaux, une page par fusionne. Script : `python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\histo_html\histo_html.py"`. Trace : `debut pages_html` / `fin pages_html`.

1. Lancer le script sans argument : il regenere la page du jour `historique\02_HISTO_ET_FUSIONNE\histo_AAAA-MM-JJ.html` (toutes les sessions du jour dedans, une balise `<section>` par session) et la page du fusionne le plus recent `historique\02_HISTO_ET_FUSIONNE\FUSIONNE\JOURNAL_FUSIONNE_..._[DATE_FIN].html`, puis refait les deux `index.html`. Autres usages : `AAAA-MM-JJ` (un jour), `fusionne` (tous les fusionnes), `tout` (rattrapage complet). Le script trouve les dossiers par le debut de leur nom (`02_*` et `FUSION*`, sans tenir compte de la casse).
2. Lire chaque ligne de sortie : `cree`, `mis a jour` (l'ancienne page est copiee en `.bak_AAAA_MM_JJ_HHhMMmSSs.html`), `inchange`, `COLLISION`. COLLISION = une page du meme nom existe sans la marque du script : elle n'est JAMAIS ecrasee ; le signaler en tete du rapport final et ne pas mettre sa source a la corbeille.
3. Verifier avant toute corbeille : la page du jour existe et contient la session qui vient d'etre ecrite (une balise `<section>` de plus), la page du fusionne existe.
4. Mettre a la corbeille Windows (commande de l'etape 5, jamais de suppression definitive) les originaux dont la page HTML existe : les `histo_AAAA-MM-JJ_sN.md` et `.txt` de `02_HISTO_ET_FUSIONNE\` ; les `JOURNAL_FUSIONNE_*.md` et `JOURNAL_COMPLET_*.md` de `FUSIONNE\`, SAUF le `JOURNAL_FUSIONNE_*.md` le plus recent (date de fin la plus grande) qui reste la base de l'etape 3 de la prochaine fois. Jamais de corbeille si la page est absente ou en COLLISION. Les `.bak` ne sont pas concernes (menage de l'etape 5).
5. Ecrire la liste des fichiers envoyes a la corbeille (chemin d'origine de chacun) dans `historique\03_RAPPORTS\02_MENAGE_BAK\pages_html_AAAA-MM-JJ.txt` et la citer dans le rapport final. Journal des modifs : une ligne par fichier, ou une ligne LOT avec le chemin de ce rapport au-dela de 10 (skill journal-modifs ; le journal du jour est dans `historique\03_RAPPORTS\01_MODIFS_IA\`).
6. Pas de go a attendre. Echec du script ou page absente : le dire dans le rapport, ne rien mettre a la corbeille, continuer.

---

## ETAPE 5, 5B, 5C - MENAGE, EXPORT DASHBOARD, PUSH EN PROD

Enchainees sans demander, apres l'etape 4B. Lire `histo_ref_menage.md`. Trace : `menage`, `export_5B`, `push_docs`. Regles cles :
- Menage des `.bak` de `docs` et `Claude md SAVE` seulement si l'histo est definitif. Horodates du jour : 10 au plus, Statut `bak_h`. Au menage definitif : le plus recent devient `.bak_AAAA_MM_JJ` (Statut `bak_d`), les autres horodates partent a la corbeille apres le Statut `Trash` ; 3 `.bak_AAAA_MM_JJ` au plus par fichier.
- Corbeille Windows : jamais videe par le menage, sauf les elements de plus de 3 mois (au menage definitif).
- Pas de plafond de volume (Eric, 2026-11-01 : "open bar, no limit") : le menage passe en une fois quel que soit le nombre de fichiers. Plus de lot de 19 ou 20, plus de dry-run declenche par un volume. Seul reste le dry-run de la premiere execution sur un dossier.
- Copies de reference (5C, Eric 2026-11-02) AVANT le push : `Copie_reference.py`. Son MD5 est une barriere : en cas d'echec il s'arrete et ecrit `ALERTE A ENVOYER PAR CLAUDE` ; Claude envoie alors lui-meme `notify.mobile_app_eric` et `persistent_notification.create`, et arrete l'etape 5C.
- Push en prod (5C) : `Push_5C.py`, tout `docs` hors `XX_` et hors `.bak`, MD5 avant et apres, jamais de sauvegarde sur H: ni sur D:. Avant chaque ecrasement, l'ancienne prod est copiee dans `TEMPO\push_5C_L_vers_P_<horodatage>\`. Une prod inconnue (modifiee hors circuit) est poussee quand meme et signalee `PROD INCONNUE` ; un fichier seul en prod est signale, jamais supprime sans ordre d'Eric, et n'arrete plus le push. Purge (validee par Eric le 2026-11-04, alignement sur Hermes) : a chaque `exec`, les dossiers `TEMPO\push_5C_L_vers_P_*` de plus de 7 jours partent a la corbeille Windows, jamais de suppression definitive ; le reste de TEMPO est vide par Eric seul.
- Regle des garde-fous (Eric, 2026-11-03) : un garde-fou protege une donnee, il ne doit jamais empecher sa propre reparation. Dans l'ordre : signaler, bloquer une action ciblee (ce fichier, pas la session), bloquer une action non recuperable (extinction, suppression, ecrasement sans copie). Une alerte de `Check_XX_presents.py` bloque le fichier en cause, pas toute la sequence.

## ETAPE 6 - TREE ET CONTROLES

Apres le menage. Lire `histo_ref_controles.md` (tree, controles 6B a 6H, badges, rattrapage du push, prod fonctionnelle, reparation des ecarts nouveaux, format du rapport final). Trace : `tree`, `controles_6B` a `controles_6H`. Un ecart au palier 1 de la prod fonctionnelle (point 14, `controles_6H`) bloque SEULEMENT l'extinction de /histo-final et est dit en tete du rapport ; il ne bloque pas le push 5C, qui est en general la reparation (Eric, 2026-11-03). Une prod differente du local se diagnostique avant d'etre reparee : si la prod contient plus que le local, c'est le local qui se realigne sur la prod. Point 15 (regle 6, Eric 2026-11-01) : un ecart NOUVEAU apparu pendant la session est repare tout de suite puis le controle est relance jusqu'a 0 ; un ecart deja present avant la session va dans le rapport ("soucis a traiter").

## ORDRE D'EXECUTION STRICT

0. Journal de trace : `seq-debut histo` (sauf si appele par /histo-final), releve des tokens de depart, puis `debut` / `fin` autour de chaque etape.
0B. Histo definitif ou non (voir plus haut).
1. Journal de bord : date, numero de session, bloc journal, ecriture de `historique/02_HISTO_ET_FUSIONNE/histo_[date]_s[N].md`, presentation du fichier.
2. Sync_index (etape 2), sans pause ni question.
3. Journal fusionne (etape 3).
4. Copie Obsidian (etape 4).
4B. Pages HTML sombres (etape 4B), originaux convertis a la corbeille.
5. Menage (etape 5), puis export Dashboard (5B), puis push en prod (5C).
6. Tree et controles (etape 6, points 1 a 15).
7. Releve des tokens de fin, `histo_trace.py verifier`, puis (sauf si appele par /histo-final) `seq-fin`, `recap`, `html`.
8. Rapport final au format de `histo_ref_controles.md`.