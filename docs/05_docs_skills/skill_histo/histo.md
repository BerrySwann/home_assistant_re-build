---
name: "histo"
description: "Skill HA ReBuild - genere un journal de bord ultra-compact et le sauvegarde, puis enchaine automatiquement le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, GLOBAL_INDEX_REPO.md), le journal fusionne et la copie Obsidian et le menage des sauvegardes .bak puis la mise a jour du tree (IA_ARBO_DETAIL.md). Declencher OBLIGATOIREMENT quand l'utilisateur tape /histo, demande un journal de bord, genere l'histo, fais un resume a sauvegarder, cree un log de session, exporte l'historique. Usage typique : fin de session, avant de fermer Cowork."
---

# Skill : /histo - Journal de bord + sync_index (dont GLOBAL_INDEX_REPO) + journal fusionne + copie Obsidian + menage .bak + tree

> Fichiers presents a plusieurs emplacements (config, GLOBAL_INDEX_REPO, README) : voir `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 emplacements : local, prod racine, prod miroir docs, GitHub racine, GitHub docs/) et le controle en lecture seule `docs\04_docs_scripts\04_docs_scripts_sh\Verif_emplacements\Verif_emplacements.py` (decide par Eric le 2026-10-18, point 9 de l'etape 6).

## Objectif

Six actions, plus l'etape 5B, enchainees sans interruption :
1. Generer et sauvegarder le journal de bord de session
2. Executer le sync_index (DEPENDANCES_GLOBALES.md, docs impactees, GLOBAL_INDEX_REPO.md, GLOBAL_INDEX_AUTOMATIONS.md, GLOBAL_INDEX_VIGNETTES_PAGES.md, GLOBAL_INDEX_SCRIPTS_SH.md, GLOBAL_INDEX_SCRIPTS_YAML.md, GLOBAL_INDEX_IA.md)

3. Mettre a jour le JOURNAL FUSIONNE (historique\02_HISTO_ET_FUSIONNE\FUSIONNE\) avec la session qui vient d'etre ecrite
4. Copier le journal de session et le journal fusionne dans le coffre Obsidian
4B. Generer les pages HTML sombres du journal du jour et du fusionne (histo_html.py), puis mettre a la corbeille Windows les originaux .md/.txt convertis (etape 4B)
5. Faire le menage des sauvegardes (.bak) du perimetre docs, du dossier historique\03_RAPPORTS\06_MD5\ (rapports trigul, audits, Hermes compris) ET des sauvegardes des pages HTML de historique\01_JOURNAL_TRACE\ et de historique\02_HISTO_ET_FUSIONNE\ (journaux et FUSIONNE\), puis de toute l'arborescence de historique\ (03_RAPPORTS compris : une sauvegarde par jour sans limite de jours, fusion des `_sN`, chapitre "Cas particulier : historique\ toute l'arborescence"), selon la REGLE DE SAUVEGARDE (etape 5)
5B. Verifier l'export Dashboard depose a la racine de la prod et ne garder qu'un export en prod (etape 5B)
6. Mettre a jour les tree : IA_ARBO_DETAIL.md (comptages local, prod, GitHub), avec le skill update-arbo (etape 6)
6B. Controler les 9 fichiers de SOUS_CONTEXT_IA (lecture seule, rapport d'ecarts, etape 6 point 7)
6C. Controler tous les index globaux (lecture seule, rapport d'ecarts, etape 6 point 8)
6D. Controler les fichiers a plusieurs emplacements (lecture seule, rapport d'ecarts, etape 6 point 9)
6E. Controler les integrations File (notify) de HA contre leur fiche (lecture seule, rapport d'ecarts, etape 6 point 10)

Ne jamais demander confirmation entre les etapes. Les faire dans la foulee. Seule exception : le DRY-RUN du menage (etape 5) a la premiere execution sur un dossier, qui s'arrete pour presenter la liste et attendre le go de l'utilisateur (voir les garde-fous de l'etape 5).

## JOURNAL DE TRACE (demande par Eric le 2026-10-19, commun a /histo et /histo-final)

Pour voir ou la sequence plante ou se bloque en silence, et garder la trace des validations demandees a Eric, ecrire une ligne avant et apres chaque etape avec `histo_trace.py` : `python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\histo_trace\histo_trace.py" <commande>`. Journal brut : `historique\01_JOURNAL_TRACE\LOGS\histo_trace_AAAA-MM-JJ.log` (un par jour, chaque ligne forcee sur le disque ; dossier renomme `01_JOURNAL_TRACE` par Eric le 2026-10-21 pour etre en haut de `historique\`). Les `.log` sont hors perimetre du menage .bak. Les pages HTML directement dans `01_JOURNAL_TRACE\` ont leur propre regle de menage (chapitre "Cas particulier : historique\01_JOURNAL_TRACE\" plus bas).

- Commandes : `seq-debut histo|histo-final`, `debut ETAPE [texte]`, `fin ETAPE OK|ATTENTION|ECHEC [texte]`, `validation ETAPE texte`, `note ETAPE texte`, `seq-fin`, `verifier`, `recap`, `html`.
- Appele seul (/histo) : ecrire `seq-debut histo` au debut et `seq-fin` apres le rapport final. Appele par /histo-final : ne pas ecrire `seq-debut` ni `seq-fin` (c'est /histo-final qui ouvre et ferme la sequence), seulement les `debut` / `fin` des etapes.
- Noms d'etape : journal (etape 1), sync_index (2), fusionne (3), obsidian (4), pages_html (4B), menage (5), export_5B (5B), tree (6 points 1 a 6), controles_6B (point 7), controles_6C (point 8), controles_6D (point 9), controles_6E (point 10), rapport.
- A la fin (apres le rapport) : lancer `histo_trace.py verifier` et mettre sa sortie dans le rapport final (ligne TRACE). Appele seul (/histo) : lancer aussi `histo_trace.py recap` apres `seq-fin` (lecture seule) ; sa sortie horodate chaque tache : heure de debut de la tache 1, puis pour chaque tache suivante la duree de la tache precedente et son heure de debut (demande d'Eric le 2026-10-21) ; la mettre dans le rapport final (ligne HORODATAGE). Appele par /histo-final : ne pas la lancer, c'est /histo-final qui la lance. Appele seul (/histo) : lancer ensuite `histo_trace.py html` (demande d'Eric le 2026-10-21) : il ecrit la page HTML du jour `historique\01_JOURNAL_TRACE\histo_trace_AAAA-MM-JJ.html` (toutes les sequences du jour, duree de chaque tache, resultat de la ligne FIN, notes) et refait `index.html` ; si la page du jour existe avec un contenu different, il la copie d'abord en `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html` ; page identique : rien n'est ecrit. Mettre sa sortie dans le rapport final (ligne PAGE). Appele par /histo-final : ne pas le lancer, c'est /histo-final qui le lance.
- Une ligne `debut` sans `fin` revele un blocage silencieux (appel qui n'a jamais rendu la main, par exemple une validation restee sans reponse). Une sequence sans `seq-fin` revele une interruption (PC eteint, session fermee, plantage).
- Limite : Claude ne voit pas l'ecran d'Eric. Il ne sait qu'une validation a ete demandee que si le resultat de l'outil le dit (refus, attente, message d'approbation) ; sinon la trace montre seulement une etape longue ou sans fin. Ne jamais inventer une ligne `validation`.
- Pas de secret dans les messages du journal. Si le script de trace est absent ou echoue : le dire dans le rapport et continuer (la trace ne bloque jamais la sequence).

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

- Chemins courts (ex : `docs/01_docs_config_system/config_system_SH_PY_YAML/sensors/P1_kWh_clim.yaml`)
- IDs matrice pour les vignettes (L2C1, L1C3, etc.)
- Si session vide : indiquer `SESSION VIDE - aucune modification`
- Bloc autonome : lisible sans contexte par quelqu'un qui reprend le projet plus tard

---
## ETAPE 2 - SYNC_INDEX (enchaine automatiquement, sans demander)

Immediatement apres la sauvegarde du journal, executer le sync_index complet.

### Perimetre

| Type de fichier modifie | Index a mettre a jour |
|:---|:---|
| Config YAML (sensors, templates, utility_meter...) | `DEPENDANCES_GLOBALES.md` + `GLOBAL_INDEX_REPO.md` |
| Automation | `docs/03_docs_automations/03_docs_automations_md/{nom}.md` + `GLOBAL_INDEX_REPO.md` |
| Script | `docs/04_docs_scripts/04_docs_scripts_yaml_md/{nom}.md` + `GLOBAL_INDEX_REPO.md` |
| Tout type impactant une vignette | `DEPENDANCES_GLOBALES.md` |
| Fichier ajoute, renomme ou supprime (helper, export, fiche) | `GLOBAL_INDEX_REPO.md` |
| Skill du projet modifie (`.claude/skills/<skill>/SKILL.md`) | copie `docs/05_docs_skills/skill_<nom>/<nom>.md` |

**Chemins Windows :**
- `C:\Users\Berry Swann\Documents\ReBuild\docs\XX_docs_MD_system\DEPENDANCES_GLOBALES\DEPENDANCES_GLOBALES.md`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\03_docs_automations_md\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_yaml_md\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md`

**Chemin bash sandbox :** detecter via `ls /sessions/` si necessaire (prefixe de session variable).

### Protocole

1. Identifier les fichiers modifies pendant la session (depuis le journal de bord qui vient d'etre genere)
2. Pour chaque fichier impactant DEPENDANCES_GLOBALES.md : mettre a jour la date en tete de fichier, puis pousser le fichier en prod (decide par Eric le 2026-10-14) : comparer le MD5 de la copie locale a `H:\docs\XX_docs_MD_system\DEPENDANCES_GLOBALES\DEPENDANCES_GLOBALES.md`, copier seulement si different (sans sauvegarde sur H: : le `.bak` reste local), verifier le MD5 apres, y compris quand la ligne de date est la seule modification. Si la prod differe de la version locale d'avant la modification (quelqu'un d'autre a ecrit en prod) : ne pas pousser et le signaler. Si H: est inaccessible : le noter sans bloquer.
3. Pour chaque automation validee : verifier/mettre a jour son `.md` dans `03_docs_automations_md/`
4. Pour chaque script valide : verifier/mettre a jour son `.md` dans `04_docs_scripts_yaml_md/`
5. Mettre a jour `GLOBAL_INDEX_REPO.md` (voir ci-dessous)
6. Si un `.md` de doc est absent : le signaler (ne pas bloquer)
7. Pour chaque skill du projet modifie pendant la session : copier d'abord le fichier existant `docs/05_docs_skills/skill_<nom>/<nom>.md` en `docs/05_docs_skills/skill_<nom>/<nom>.bak_AAAA_MM_JJ_HHhMMmSSs.md` (sauvegarde avant ecrasement, jusqu'a 10 par jour ; le menage de l'etape 5 range les jours passes en `<nom>.bak_AAAA_MM_JJ.md`, 3 au plus), puis recopier le `SKILL.md` modifie vers `docs/05_docs_skills/skill_<nom>/<nom>.md`. Pas de copie dans `.claude/ARCHIVE`. Pas de push des skills vers `H:` tant qu'Eric ne le demande pas (decision du 2026-10-11).
8. Regenerer GLOBAL_INDEX_AUTOMATIONS.md (decide le 2026-10-13) : lancer `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\gen_global_index_automations\gen_global_index_automations.py"`. Le script lit H:\automations.yaml et le registre HA (lecture seule), croise avec 03_docs_automations_yaml et 03_docs_automations_md, et ecrit `docs\03_docs_automations\GLOBAL_INDEX_AUTOMATIONS.md` (sauvegarde `.bak_AAAA_MM_JJ_HHhMMmSSs.md` automatique si le contenu change ; rien d'ecrit si identique). Ne jamais modifier ce fichier a la main. VERIFIER la sortie du script : la ligne liens=N casses=M doit avoir casses=0 (sinon signaler chaque LIEN_CASSE en tete du rapport final) ; mettre dans le rapport final les lignes de resume du script et chaque ecart cite (sans_yaml, sans_fiche, sans_entity, id_different, erreurs_yaml). Un ecart nouveau par rapport a la session precedente doit etre signale a Eric, pas corrige sans demande. Si H: est inaccessible (code retour 2) : le noter sans bloquer. Pas de push automatique (poussable avec /ha-push-docs sur demande).
9. Regenerer GLOBAL_INDEX_VIGNETTES_PAGES.md (decide le 2026-10-13), meme principe que le point 8 : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\gen_global_index_vignettes_pages\gen_global_index_vignettes_pages.py"`. Le script lit l'arbre local docs\02_docs_dashboard (02_dashboard_docs_md et 02_dashboard_docs_yaml, sauvegardes exclues, Dashboard_COMPLET jamais lu) et ecrit `docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md` (sauvegarde `.bak_...md` automatique si le contenu change). Ne jamais modifier ce fichier a la main. VERIFIER la sortie du script : la ligne liens=N casses=M doit avoir casses=0 (sinon signaler chaque LIEN_CASSE en tete du rapport final) ; mettre dans le rapport final les lignes de resume du script (vignettes sans fiche ou sans YAML, dossiers d un seul cote, sans_dependances). Pas de push automatique.
10. Regenerer GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md (decide le 2026-10-13), meme principe : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\gen_global_index_scripts\gen_global_index_scripts.py"`. Le script lit l'arbre local docs\04_docs_scripts et la prod en lecture seule (H:\scripts.yaml, H:\automations.yaml, H:\shell_command, H:\.scripts, registre HA) et ecrit les deux fichiers a la racine de docs\04_docs_scripts (sauvegarde `.bak_...md` automatique si le contenu change). Chaque fichier explique la difference entre scripts SH (programmes bash/python) et scripts YAML (scripts Home Assistant). VERIFIER la sortie : les deux lignes `liens=N casses=M` doivent avoir casses=0 ; signaler dans le rapport final les lignes de resume SH et YAML et chaque ecart (script sans fiche, copie de H:\.scripts DIFFERENT du local, script YAML different de la prod ou sans YAML local, fichiers .py ranges dans 04_docs_scripts_yaml). Si H: est inaccessible (code retour 2) : le noter sans bloquer. Ne jamais pousser un script de H:\.scripts sans ordre d'Eric. Ne jamais modifier ces fichiers a la main.
11. Regenerer GLOBAL_INDEX_IA.md (decide le 2026-10-13) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\gen_global_index_ia\gen_global_index_ia.py"`. Le script liste tous les fichiers de docs\00_IA (IA_CONTEXT_BASE et SOUS_CONTEXT_IA) avec qui s'en sert, leur but, quand les lire, leur MD5 prod et un lien, et resume les `.bak` par dossier. Il ecrit docs\00_IA\GLOBAL_INDEX_IA.md (sauvegarde `.bak_...md` automatique si le contenu change). VERIFIER la sortie : la ligne `liens=N casses=M sans_description=K` doit avoir casses=0 et sans_description=0. Si un fichier est nouveau dans docs\00_IA (sans_description > 0) : le lire, ajouter son entree (qui, but, quand) dans le dictionnaire DESC du script apres sauvegarde du script, puis relancer ; ne jamais inventer une description sans avoir lu le fichier. Ne jamais modifier GLOBAL_INDEX_IA.md a la main.

### Mise a jour de GLOBAL_INDEX_REPO.md

Fichier : `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` (copie de travail locale, deplacee par Eric le 2026-10-18 depuis `docs\XX_docs_MD_system\GLOBAL_INDEX_REPO\` ; ses liens sont relatifs a la racine du depot : elle ne se clique pas ici ; poussee en prod a chaque /histo aux deux endroits (miroir H:\docs\01_docs_config_system\config_system_MD\GLOBAL_INDEX_REPO\ et racine H:\GLOBAL_INDEX_REPO.md, lue sur GitHub), voir le point 8 ci-dessous ; GitHub est alimente par le backup HA depuis H:, jamais en push direct).

1. Si aucun fichier de la session n'est ajoute, renomme, supprime ou deplace, et qu'aucune entite citee n'a change : noter "GLOBAL_INDEX_REPO deja a jour" et passer au point 8 (le push compare quand meme les MD5).
2. Sinon, faire d'abord une sauvegarde dans le meme dossier : `GLOBAL_INDEX_REPO.bak_AAAA_MM_JJ_HHhMMmSSs.md` (format PowerShell `Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"` ; le dossier INDEX_GLOBAL est dans le perimetre du menage de l'etape 5).
3. Ne reecrire que les lignes concernees, jamais le fichier entier :
   - ajouter une entree pour chaque nouveau fichier (automation, script, helper YAML, fiche), dans la section de son type, a cote des entrees voisines, avec le meme format que celles-ci
   - mettre a jour les entrees renommees ou supprimees
   - mettre a jour les compteurs de section concernes (par exemple le nombre d'automations ou de fichiers de scripts) en les recomptant, sans les deduire de l'ancien nombre
   - mettre a jour la ligne d'en-tete de date
4. Garder le format existant du fichier : UTF-8 sans BOM, fins de ligne LF (verifie le 2026-10-11 : le fichier est en LF, ne pas le convertir en CRLF). Controler le format avant d'ecrire.
5. Controles apres ecriture : le fichier se relit en UTF-8, les compteurs modifies correspondent au nombre d'entrees, les liens ajoutes pointent vers des fichiers qui existent avec la casse exacte (GitHub distingue la casse ; resync des 315 liens le 2026-10-18). Les entites ajoutees doivent avoir ete verifiees en live ou lues dans un fichier de la session, jamais recopiees de memoire.
6. Les ecarts deja presents avant la session (entites citees qui ne repondent plus, desequilibres de compteurs) ne sont pas corriges ici : les mentionner dans le rapport s'ils concernent la session.
7. Note pour ha-trigul : depuis le push de /histo (decide par Eric le 2026-10-14), `GLOBAL_INDEX_REPO.md` est present en prod sous docs/01_docs_config_system/config_system_MD/GLOBAL_INDEX_REPO/ (miroir) ; il reste ABSENT sur le depot tant que le backup HA ne l'a pas repris ; son exemplaire a la racine de H: (GLOBAL_INDEX_REPO.md) n'est pas compare par le script du trigul ; il l'est par Verif_emplacements.py (point 9 de l'etape 6).
8. Push en prod (decide par Eric le 2026-10-14, il remplace l'ancienne regle "pas de push automatique" : Eric avait pris ce fichier pour un autre) : apres les controles du point 5, que le fichier ait ete modifie ou non, comparer le MD5 de la copie de travail a chacune des DEUX destinations, comme l'etape 5B de ha-push-docs : `H:\docs\01_docs_config_system\config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` (miroir) et `H:\GLOBAL_INDEX_REPO.md` (racine). Copier seulement celles qui different, sans sauvegarde sur H: (les `.bak` restent locaux), puis verifier le MD5 : source = miroir = racine. Jamais un seul des deux. Ne pas pousser si les controles du point 5 ont echoue. Si H: est inaccessible : le noter sans bloquer. GitHub : jamais de push direct (le depot est alimente par le backup HA depuis H:).

### Regles sync_index

- Ne reecrire que les lignes concernees - pas le fichier complet (economie tokens)
- Si aucune dependance impactee : noter "Index deja a jour" dans le rapport final
- Chemin bash sandbox : toujours verifier avec `ls /sessions/` si le prefixe est incertain

---
## ETAPE 3 - JOURNAL FUSIONNE (enchaine automatiquement, sans demander)

Le journal fusionne est un seul fichier Markdown qui regroupe tous les journaux de session depuis le 2026-07-15. Il se lit en premier quand on reprend le projet : le FAIT en haut (par date), le RESTE A FAIRE en bas (par date).

**Dossier :** `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\FUSIONNE\`
**Nom :** `JOURNAL_FUSIONNE_2026-07-15_[DATE_FIN].md`, ou `[DATE_FIN]` = date de la derniere session incluse (format YYYY-MM-DD).

### Protocole

1. Reperer le fusionne le plus recent : `JOURNAL_FUSIONNE_*.md` (sans suffixe `.bak`), trie par date de fin dans le nom. Il sert de base.
2. Reperer les journaux `histo_*.md` et anciens `histo_*.txt` pas encore integres (dossier `historique\02_HISTO_ET_FUSIONNE\` ; depuis le 2026-10-21 les anciens sont en HTML et a la corbeille, il ne reste que les journaux de la session en cours ; en cas de doute lire la page HTML du jour) : comparer les dates et suffixes aux lignes `SESSION 2026-...` du fusionne. Y inclure celui qui vient d'etre ecrit a l'etape 1. Ne pas dependre de la seule date de modification des fichiers.
3. Lire chaque journal manquant en entier avant de l'integrer. Ne rien ajouter qui ne soit pas dans ces journaux (ni chiffre, ni etat, ni decision deduits). Un journal au format Markdown mis en forme (titres `##`, gras, icones) est integre au fusionne en ASCII : retirer les icones et pastilles, garder le fond (le gras du fusionne vient du format de bloc ci-dessous).
4. Construire le nouveau fichier a partir de la base, sans toucher au contenu existant :
   - ligne 2 d'en-tete : remplacer la date de fin dans `Periode : 2026-07-15 -> [DATE_FIN]` (la base utilise une fleche, ne changer que la date)
   - partie `PAR DATE - CE QUI A ETE FAIT` : ajouter un bloc par session, dans l'ordre chronologique, juste avant la ligne de titre `## **PAR DATE - CE QUI RESTE A FAIRE**` (le bandeau est un titre Markdown, hors bloc de code). Les blocs de session sont en vrai Markdown, hors bloc de code, pour que le gras s'affiche. Format du bloc (rubriques utiles seulement) :

         ### **SESSION [date] ([Sn]) - [duree] - [titre court]**

         **[FICHIERS VALIDES]**
         - ...

         **[ERREURS RESOLUES]**
         - ...

         **[DECISIONS]** / **[CONSTATS]**
         - ...

     Titre de session entier en gras, dates en gras, crochets en gras ; pas d'icone ni d'emoji dans le fusionne ; ASCII sauf les `**` du gras. Chemins en code inline. Session vide : une seule ligne `**SESSION [date] ([Sn], [heure]) : session vide - aucune modification depuis ...**`. Laisser une ligne vide avant et apres chaque bloc. Les anciennes sessions (titres et rubriques en gras, corps dans des blocs de code) ne sont pas modifiees.
   - partie `PAR DATE - CE QUI RESTE A FAIRE` : le bandeau est le titre `## **PAR DATE - CE QUI RESTE A FAIRE**`. Ajouter a la FIN du fichier, apres la derniere ligne ```, une entree par date en Markdown, le texte de chaque rubrique restant dans un bloc de code :

         ### **[date]**

         **[EN COURS]**

         (bloc de code ```text, contenu indente de 4 espaces, puis ```)

         **[PROCHAINE ACTION]**

         (bloc de code ```text, contenu indente de 4 espaces, puis ```)

         ### **ETAT ACTUEL AU [date] (soir, curated)**

         (bloc de code ```text : resume de l'etat courant et de ce qui reste ouvert, puis ```)

     Quand un item d'une entree plus ancienne a ete ferme depuis, le noter dans la nouvelle entree (par exemple `(ferme le 07/10)`), sans modifier l'ancienne. Le fichier se termine ainsi par une ligne ``` de fin de bloc de code.
5. Ecrire le nouveau fichier. Les blocs ajoutes sont en ASCII (pas de tiret long, pas de fleche, pas de caracteres speciaux, pas d'emoji ; seul le gras `**` est ajoute dans les nouveaux blocs de session) ; le contenu existant est repris tel quel, y compris ses caracteres speciaux.

### Regles

- Ne jamais ecraser un fusionne existant : un nouveau nom par nouvelle date de fin. Si le fichier cible existe deja (meme date de fin, nouvelle session du meme jour), le sauvegarder d'abord en `JOURNAL_FUSIONNE_..._[DATE_FIN].bak_AAAA_MM_JJ_HHhMMmSSs.md` puis le mettre a jour.
- L'ancien fusionne reste en place. Ne pas le supprimer sans demande.
- Format du fichier : CRLF, UTF-8 sans BOM, comme la base.
- Verifier apres ecriture : pas de BOM, aucun LF isole, un seul bandeau `RESTE A FAIRE`, le fichier se termine par la ligne ``` suivie d'une fin de ligne, nombre pair de lignes ``` (clotures equilibrees), nombre de lignes coherent avec base + ajouts.
- Ecrire par script (Python ou PowerShell) en passant les blocs par fichiers temporaires dans `%TEMP%` : une commande trop longue echoue (WinError 206). Ne jamais reconstituer le contenu existant a partir d'un affichage tronque : lire le fichier.
- Si la base est introuvable ou illisible : le signaler et s'arreter a cette etape, sans recreer tout le fusionne de memoire.

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

Les journaux de session et les journaux fusionnes sont lisibles en HTML sombre (meme palette que `TODO\TODO.html`) : une page par jour pour les journaux, une page par fusionne. Script : `python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\histo_html\histo_html.py"`. Trace : `debut pages_html` / `fin pages_html`.

1. Lancer le script sans argument : il regenere la page du jour `historique\02_HISTO_ET_FUSIONNE\histo_AAAA-MM-JJ.html` (toutes les sessions du jour dedans, une balise `<section>` par session) et la page du fusionne le plus recent `historique\02_HISTO_ET_FUSIONNE\FUSIONNE\JOURNAL_FUSIONNE_..._[DATE_FIN].html`, puis refait les deux `index.html`. Autres usages : `AAAA-MM-JJ` (un jour), `fusionne` (tous les fusionnes), `tout` (rattrapage complet). Le script trouve les dossiers par le debut de leur nom (`02_*` et `FUSION*`, sans tenir compte de la casse).
2. Lire chaque ligne de sortie : `cree`, `mis a jour` (l'ancienne page est copiee en `.bak_AAAA_MM_JJ_HHhMMmSSs.html`), `inchange`, `COLLISION`. COLLISION = une page du meme nom existe sans la marque du script : elle n'est JAMAIS ecrasee ; le signaler en tete du rapport final et ne pas mettre sa source a la corbeille.
3. Verifier avant toute corbeille : la page du jour existe et contient la session qui vient d'etre ecrite (une balise `<section>` de plus), la page du fusionne existe.
4. Mettre a la corbeille Windows (commande de l'etape 5, jamais de suppression definitive) les originaux dont la page HTML existe : les `histo_AAAA-MM-JJ_sN.md` et `.txt` de `02_HISTO_ET_FUSIONNE\` ; les `JOURNAL_FUSIONNE_*.md` et `JOURNAL_COMPLET_*.md` de `FUSIONNE\`, SAUF le `JOURNAL_FUSIONNE_*.md` le plus recent (date de fin la plus grande) qui reste la base de l'etape 3 de la prochaine fois. Jamais de corbeille si la page est absente ou en COLLISION. Les `.bak` ne sont pas concernes (menage de l'etape 5).
5. Ecrire la liste des fichiers envoyes a la corbeille (chemin d'origine de chacun) dans `historique\03_RAPPORTS\02_MENAGE_BAK\pages_html_AAAA-MM-JJ.txt` et la citer dans le rapport final. Journal des modifs : une ligne par fichier, ou une ligne LOT avec le chemin de ce rapport au-dela de 10 (skill journal-modifs ; le journal du jour est dans `historique\03_RAPPORTS\01_MODIFS_IA\`).
6. Pas de go a attendre. Echec du script ou page absente : le dire dans le rapport, ne rien mettre a la corbeille, continuer.

---

## ETAPE 5 - MENAGE DES SAUVEGARDES (enchaine automatiquement, apres l'etape 4B)

Applique la REGLE DE SAUVEGARDE du 2026-10-08 (definie dans CLAUDE.md). Tout se passe en LOCAL, jamais sur H: ni sur D:.

**Perimetre :** `C:\Users\Berry Swann\Documents\ReBuild\docs\00_*` a `05_*` (recursif) + `C:\Users\Berry Swann\Documents\ReBuild\Claude md SAVE\` + `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\06_MD5\` (ajoute par Eric le 2026-10-18 : regles propres a ce dossier dans le chapitre "Cas particulier : historique\03_RAPPORTS\06_MD5\" plus bas) + `C:\Users\Berry Swann\Documents\ReBuild\historique\01_JOURNAL_TRACE\` (pages HTML et leurs sauvegardes seulement, sans le sous-dossier `LOGS\` ; ajoute par Eric le 2026-10-21 : regles dans le chapitre "Cas particulier : historique\01_JOURNAL_TRACE\" plus bas).
**Perimetre (suite, ajoute par Eric le 2026-10-21) :** `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\` (pages HTML, `FUSIONNE\` compris, et les `.bak` de journaux : regles dans le chapitre "Cas particulier : historique\02_HISTO_ET_FUSIONNE\" plus bas).
**Perimetre (suite, ajoute par Eric le 2026-10-24) :** `C:\Users\Berry Swann\Documents\ReBuild\TODO\` (sauvegardes `TODO.bak_*` seulement : `TODO.html` n'est jamais touche ; regles dans le chapitre "Cas particulier : TODO\" plus bas).
**Hors perimetre (ne pas toucher) :** Github, historique pour ce que les chapitres dedies ne couvrent pas : `historique\01_JOURNAL_TRACE\LOGS\` (journaux bruts `.log`) et `historique\03_RAPPORTS\01_MODIFS_IA\` (journaux des modifs, un fichier par jour et par auteur) ne sont jamais touches ; le reste de historique suit le chapitre "Cas particulier : historique\ toute l'arborescence", Infra_Proxmox, `_old_avant_staging` (racine et sous-dossiers `docs\`), le reste de `.claude` (skills et commands actifs). Le dossier `.claude\ARCHIVE\` est HORS perimetre (decision d'Eric le 2026-10-11 : conserve pour un eventuel retour en arriere, a supprimer quand il ne servira plus ; il ne vit plus avec histo). Les sauvegardes d'un skill vivent dans `docs\05_docs_skills\skill_<nom>\` et suivent la meme regle que le reste (jusqu'a 10 `.bak_AAAA_MM_JJ_HHhMMmSSs` pour le jour, 3 `.bak_AAAA_MM_JJ` pour les jours passes). Les exports `docs\02_docs_dashboard\02_dashboard_docs_yaml\Dashboard_COMPLET\` sont conserves tels quels : jamais renommes en `.bak`, jamais mis a la corbeille par ce menage (voir etape 5B). Ignorer tout dossier `_ARCHIVE` / `ARCHIVE` et tout fichier dont le nom contient `_archive_` (ex : `_ARCHIVE\DEPENDANCES_GLOBALES_archive_2026-10-07_18h13.md`).

**"Poubelle" = corbeille Windows**, jamais de suppression definitive :
```powershell
Add-Type -AssemblyName Microsoft.VisualBasic
[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($f,'OnlyErrorDialogs','SendToRecycleBin')
```

### Principe de conformite (aucune exception)

Tout fichier du perimetre dont le nom porte une date ou un marqueur de sauvegarde, et qui ne suit pas
la REGLE DE SAUVEGARDE courante, est ramene aux regles. Aucun cas n'est laisse de cote sous pretexte
qu'il n'entre dans aucune famille : s'il porte une date ou un marqueur de sauvegarde, il est traite.

Deux cibles seulement :
- une version ou une sauvegarde -> `{nom_de_travail}.bak_AAAA_MM_JJ.{ext}` (le nom de travail ne contient pas de date) ;
- la version courante d'un fichier de travail -> le nom sans date (`{nom}.ext`).

Un nom de fichier ne porte JAMAIS de date dans sa partie courante. En cas de doute (nom qui pourrait
etre un vrai document et non une sauvegarde), on signale et on ne touche pas.

(Exception : dans `historique\03_RAPPORTS\06_MD5\`, les rapports quotidiens portent leur date dans leur nom par construction, par exemple `trigul_arbres_2026-10-18.txt`. Ce sont de vrais fichiers, jamais des sauvegardes : voir le chapitre dedie.)

### Formats reconnus (dans le perimetre uniquement)

| Famille | Exemple | Traitement |
|:---|:---|:---|
| A - sauvegarde horodatee | `fichier.bak_2026_10_07_21h14m05s.yaml` | voir protocole |
| B - sauvegarde finale | `fichier.bak_2026_10_07.yaml` | gardee, soumise au plafond de 3 |
| C - anciens `.bak` | `.bak_2026-09-28`, `.bak_20260929`, `.bak2_...`, `.bak-...` | renommes `fichier.bak_AAAA_MM_JJ.yaml` |
| D - versions datees d'un fichier de travail | `page_L4C2_proxmox_2026-06-18.yaml`, `fichier_2026-10-07_22h00.ext` | seulement si le fichier de travail non date `{nom}.ext` existe dans le meme dossier : chaque version datee devient `{nom}.bak_AAAA_MM_JJ.{ext}` (plafond 3). Sans fichier de travail non date : nom douteux, signaler, ne pas toucher |
| E - sauvegardes nommees | `CLAUDE_backup_2026-07-31.md`, `CLAUDE_2026-10-04.md`, `fichier_old.md` | renommees `{nom_de_travail}.bak_AAAA_MM_JJ.{ext}`, ou `{nom_de_travail}` est le nom du fichier de travail courant, extension comprise : `CLAUDE_backup_2026-07-31.md` -> `CLAUDE.bak_2026_07_31.md`, `CLAUDE_2026-10-04.md` -> `CLAUDE.bak_2026_10_04.md`, `fichier_old.md` -> `fichier.bak_<date>.md`. Le nom de travail est le nom complet du fichier non date voisin, jamais tronque (`04_backup_git_push_manuel_2026-05-31.yaml` -> `04_backup_git_push_manuel.bak_2026_05_31.yaml`, pas `04.bak_...`). Date lue dans le nom, a defaut date de modification. Un fichier non date, sans version de travail correspondante, dont le nom contient `backup`, `save` ou `old` (ex : `ha_git_backup.sh`, `HA_GIT_BACKUP.md`) est un vrai fichier : ne pas le traiter |

> Aucune famille n'est une liste fermee. Tout nom portant une date (`AAAA-MM-JJ`, `AAAA_MM_JJ`,
> `AAAAMMJJ`) ou un marqueur `backup`, `save`, `old`, `ancien`, `avant`, `orig`, et qui n'est pas le
> fichier de travail courant, entre dans la conformite (famille E). Restent exclus les dossiers
> `_ARCHIVE` / `ARCHIVE` (dont `.claude\ARCHIVE\`), les fichiers `*_archive_*` et `Dashboard_COMPLET\` restent exclus. Un marqueur seul ne suffit pas : sans date et sans version de travail voisine, le fichier est un vrai fichier.

### Protocole

1. Date du jour = `Get-Date -Format "yyyy_MM_dd"`. **Les sauvegardes du jour ne sont jamais touchees** (famille A du jour, et famille D du jour). (Dans `historique\` et `TODO\` : plafond de 10 au jour meme et aucun plafond de jours, voir les chapitres dedies.)
2. Regrouper par fichier d'origine (meme dossier, meme nom de base, meme famille) puis, dans chaque groupe, par jour passe.
3. Pour chaque jour passe d'un groupe :
   - garder la sauvegarde la plus RECENTE : d'abord par l'horodatage lu dans le nom (jour + heure) ; a egalite (noms sans heure, ex `.bak_2026-09-20`, `.bak_2026-09-20b`, `.bak2_...`), par la date de modification du fichier ; si l'egalite persiste et que les contenus different (MD5), ne rien supprimer et signaler le groupe ; si les contenus sont identiques, garder n'importe lequel ;
   - la renommer en `fichier.bak_AAAA_MM_JJ.yaml` (famille A), les autres de ce jour vont a la corbeille Windows ;
   - famille C : renommer en `.bak_AAAA_MM_JJ.{ext}` (la date est lue dans le nom) ;
   - famille D : seulement si le fichier de travail non date `{nom}.ext` existe dans le dossier ; chaque version datee devient `{nom}.bak_AAAA_MM_JJ.{ext}` (nom de travail complet, jamais tronque ; plusieurs versions du meme jour : la plus recente est gardee, les autres vont a la corbeille ; plafond 3) ; sans fichier de travail non date, signaler et ne pas toucher ;
   - famille E : renommer en `{nom_de_travail}.bak_AAAA_MM_JJ.{ext}`, ou `{nom_de_travail}` est le nom du fichier de travail courant, extension comprise (ex : `CLAUDE_backup_2026-07-31.md` -> `CLAUDE.bak_2026_07_31.md`, `CLAUDE_2026-10-04.md` -> `CLAUDE.bak_2026_10_04.md`) ; date lue dans le nom, a defaut date de modification.
4. Plafond : si un fichier a plus de 3 `.bak_AAAA_MM_JJ.{ext}` (apres les renommages ci-dessus, famille A, B et C), la plus ancienne va a la corbeille Windows, et ainsi de suite jusqu'a 3. Le plafond de 3 s'applique a toutes les familles (A, B, C, D, E), SAUF dans `historique\` et `TODO\` ou il n'y a aucun plafond de jours (une sauvegarde par jour indefiniment, decision d'Eric le 2026-10-21).
5. Si la date change pendant l'execution (minuit passe), garder la date relevee au lancement de l'etape.

### Cas particulier : historique\03_RAPPORTS\06_MD5\ (decide par Eric le 2026-10-18, "Hermes compris")

Dossier : `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\06_MD5\` (rapports de trigul, audits, rapports et sauvegardes produits par Hermes dans ce dossier ; sous-repertoires numerotes `00_VERIF_FINAL_TRIGUL_ARBRES`, `01_TRIGUL_PROFOND`, `02_CATEGORIES_HA`, `03_VERIF_EMPLACEMENTS`, `04_JOURNAL_TRIGUL`, `05_VERIF_INTEGRATIONS_FILE` ajoute le 2026-10-23 pour le controle des integrations File). Eric a deplace ce dossier de `historique\MD5\` vers `historique\03_RAPPORTS\06_MD5\` le 2026-10-21 ; les scripts du trigul (trigul_run, hermes_audit_trigul_arbres, Hermes_audit_md5_trigul_unitaire) et Verif_emplacements.py ecrivent dans le nouvel emplacement depuis le 2026-10-23 (point R104.2 du TODO). Un dossier `historique\MD5\` qui reapparait est un ecart a signaler a Eric. Les histos suivent la meme regle de menage que les docs, avec ces precisions :

- **Groupe = un rapport**, identifie par son nom complet, date comprise (ex : `trigul_arbres_2026-10-18.txt`). La date du nom d'un rapport fait partie de son nom de travail : les familles D et E ne s'appliquent PAS a un rapport (un rapport date n'est jamais traite comme une version datee d'un autre fichier). Les rapports eux-memes et les copies `_latest` ne sont jamais renommes, jamais mis a la corbeille, jamais modifies par le menage.
- **Sauvegardes du jour** (date lue dans le nom de la sauvegarde) : 10 au plus par rapport, au format `rapport.bak_AAAA_MM_JJ_HHhMMmSSs.ext`. Au-dela de 10, les plus anciennes vont a la corbeille Windows.
- **Jours passes** : par rapport et par jour, garder la sauvegarde la plus recente (horodatage du nom, sinon date de modification), renommee `rapport.bak_AAAA_MM_JJ.ext` ; les autres de ce jour vont a la corbeille Windows. Pas de plafond de jours (decision d'Eric le 2026-10-21) : une sauvegarde par jour indefiniment.
- **Sauvegarde sans extension** (ex : `rapport.bak_2026_10_17`) : elle prend l'extension du rapport (`.txt`, `.html`...). Collision avec un nom existant : ne rien renommer, signaler.
- **Ancien nom `bak_HHhMM_libelle`** (sans date de sauvegarde dans le nom) : la date prise est celle du nom du rapport ; le cas est signale dans le rapport de menage comme "date deduite du nom du rapport".
- Garde-fous du chapitre commun (collision, date illisible, nom douteux, erreur de la corbeille) : ne rien supprimer, signaler.
- Premiere execution faite le 2026-10-18 : plan `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_dryrun_2026-10-18.txt`, execution `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_2026-10-18.txt` (go d'Eric obtenu apres dry-run). Les executions suivantes n'attendent plus de go : ecrire le plan dans `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_dryrun_AAAA-MM-JJ.txt`, le citer dans le rapport final, executer, ecrire le compte rendu dans `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_AAAA-MM-JJ.txt` (chemin d'origine de chaque envoi en corbeille, restaurable depuis la corbeille Windows).
- Le menage de ce dossier se fait avant le tree (etape 6), comme le reste de l'etape 5. Journal des modifs : une ligne LOT avec le chemin du rapport (skill journal-modifs).

### Cas particulier : historique\01_JOURNAL_TRACE\ (decide par Eric le 2026-10-21)

Dossier : `C:\Users\Berry Swann\Documents\ReBuild\historique\01_JOURNAL_TRACE\` (ancien `journal_trace`, renomme par Eric pour etre en haut de `historique\`). Il contient directement les pages HTML ecrites par `histo_trace.py html` (`histo_trace_AAAA-MM-JJ.html`, une par jour, et `index.html`), leurs sauvegardes, et le sous-dossier `LOGS\` (journaux bruts `.log`) qui est HORS perimetre : le menage n'y touche jamais.

- **Groupe = une page journaliere**, identifiee par son nom complet date. Les pages `histo_trace_AAAA-MM-JJ.html` et `index.html` ne sont jamais renommees, jamais mises a la corbeille, jamais modifiees par le menage. Une page par jour, gardee sans limite de jours (decision d'Eric : comme la TODO, un fichier par jour indefiniment). La date du nom d'une page fait partie de son nom de travail : les familles D et E ne s'y appliquent pas.
- **Sauvegardes du jour** (date lue dans le nom de la sauvegarde) : `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html`, 10 au plus par page et par jour (creees par `histo_trace.py html` quand une page du jour est regeneree avec un contenu different). Au-dela de 10, les plus anciennes vont a la corbeille Windows.
- **Jours passes** : par page et par jour de sauvegarde, garder la plus recente renommee `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ.html` ; les autres de ce jour vont a la corbeille Windows. Pas de plafond de jours (une sauvegarde par jour indefiniment, comme la TODO).
- Garde-fous du chapitre commun (collision, date illisible, nom douteux, erreur de la corbeille) : ne rien supprimer, signaler.
- Pas de go a attendre sur ce dossier, meme a la premiere execution (une pause bloquerait /histo-final avant l'arret du PC ; tout part a la corbeille Windows, restaurable) : ecrire le plan dans le fichier de plan du menage, executer, citer le compte rendu dans le rapport final.
- Le menage de ce dossier se fait avec l'etape 5, avant le tree. Journal des modifs : une ligne par fichier, ou une ligne LOT avec le chemin du rapport au-dela de 10 (skill journal-modifs).

### Cas particulier : TODO\ (decide par Eric le 2026-10-24)

Dossier : `C:\Users\Berry Swann\Documents\ReBuild\TODO\`. Il contient `TODO.html` (la todo : source et vue depuis le 2026-10-24) et ses sauvegardes `TODO.bak_AAAA_MM_JJ_HHhMMmSSs.html`, creees a chaque modification de la todo (regle TODO de CLAUDE.md). L'ancien `TODO.md` et ses sauvegardes `.md` ont ete envoyes a la corbeille le 2026-10-24 sur ordre d'Eric.

- `TODO.html` n'est jamais renomme, jamais mis a la corbeille, jamais modifie par le menage. Les familles C, D et E ne s'y appliquent pas. Plus aucun fichier `.md` ni `.txt` dans ce dossier (ordre d'Eric du 2026-10-24) : tout `TODO.md`, `TODO.bak_*.md` ou `.txt` qui y reapparait est signale dans le rapport et envoye a la corbeille Windows.
- **Groupe = une extension** (`.html`, `.md`, `.txt`) : les sauvegardes de formats differents ne se melangent jamais.
- **Sauvegardes du jour** (date lue dans le nom) : jamais renommees ; 10 au plus par groupe, au-dela les plus anciennes vont a la corbeille Windows.
- **Jours passes** : par groupe et par jour, garder la plus recente (horodatage lu dans le nom) renommee `TODO.bak_AAAA_MM_JJ.{ext}` ; les autres de ce jour vont a la corbeille Windows. Une sauvegarde par jour indefiniment, sans plafond de jours (decision d'Eric). Les `TODO.bak_AAAA_MM_JJ.{ext}` deja au bon format ne sont pas touchees.
- Anciens noms (`TODO.txt.bak_...`, `TODO.md.bak_...`) : famille C, renommes en `TODO.bak_AAAA_MM_JJ.{ext}` s'il n'y a pas de collision.
- Garde-fous du chapitre commun (collision, date illisible, nom douteux, erreur de la corbeille) : ne rien supprimer, signaler.
- Pas de go a attendre sur ce dossier, meme a la premiere execution (tout part a la corbeille Windows, restaurable) : ecrire le plan dans le fichier de plan du menage, executer, citer le compte rendu dans le rapport final.
- Journal des modifs : une ligne par fichier, ou une ligne LOT avec le chemin du rapport au-dela de 10 (skill journal-modifs). Le menage de ce dossier se fait avec l'etape 5, avant le tree.

### Cas particulier : historique\02_HISTO_ET_FUSIONNE\ (decide par Eric le 2026-10-21)

Dossier : `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\` : une page `histo_AAAA-MM-JJ.html` par jour (toutes les sessions du jour), son `index.html`, et le sous-dossier `FUSIONNE\` (une page `JOURNAL_FUSIONNE_..._[DATE_FIN].html` par fusionne, son `index.html`, le `.md` du fusionne le plus recent et les anciennes sauvegardes). Les pages sont ecrites par `histo_html.py` (etape 4B). Memes regles que `01_JOURNAL_TRACE` :

- **Groupe = une page**, identifiee par son nom complet date. Les pages de jour, les pages de fusionnes et les `index.html` ne sont jamais renommees, jamais mises a la corbeille, jamais modifiees par le menage. Une page par jour, gardee sans limite de jours (decision d'Eric : comme la TODO, une par jour indefiniment). Les familles D et E ne s'y appliquent pas.
- **Sauvegardes du jour** : `histo_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html` et `JOURNAL_FUSIONNE_..._[DATE_FIN].bak_AAAA_MM_JJ_HHhMMmSSs.html` (creees par `histo_html.py` quand une page est regeneree avec un contenu different), 10 au plus par page et par jour ; au-dela, les plus anciennes vont a la corbeille Windows.
- **Jours passes** : par page et par jour de sauvegarde, garder la plus recente renommee `<nom>.bak_AAAA_MM_JJ.html` ; les autres de ce jour vont a la corbeille. Pas de plafond de jours.
- **Anciennes sauvegardes `.md`** (`histo_*.bak_*.md`, `JOURNAL_FUSIONNE_*.md.bak_*` et variantes sans `.md` final) : familles A, B et C du chapitre commun, mais SANS plafond de 3 jours (une par jour indefiniment, la plus recente, comme pour les pages).
- Les `.md` de journaux qui ne sont pas des `.bak` ne sont pas traites par le menage : ils partent a la corbeille a l'etape 4B.
- Garde-fous du chapitre commun (collision, date illisible, nom douteux, erreur de la corbeille) : ne rien supprimer, signaler. Une page en COLLISION n'est jamais touchee.
- Pas de go a attendre, meme a la premiere execution (tout part a la corbeille Windows, restaurable). Le menage de ce dossier se fait avec l'etape 5, avant le tree. Journal des modifs : une ligne par fichier, ou une ligne LOT avec le chemin du rapport au-dela de 10.

### Cas particulier : historique\ toute l'arborescence (decide par Eric le 2026-10-21)

Perimetre : tous les repertoires et sous-repertoires de `C:\Users\Berry Swann\Documents\ReBuild\historique\` (racine, `03_RAPPORTS\` et tous ses sous-dossiers, `save`, anciens dossiers `RASPI4`, `FANTOMES...`, `orphelins...`, etc.), SAUF `01_JOURNAL_TRACE\LOGS\` (journaux bruts `.log`) et `03_RAPPORTS\01_MODIFS_IA\` (journaux des modifs, un fichier par jour et par auteur) qui ne sont jamais touches. Les chapitres dedies plus haut (`MD5`, `01_JOURNAL_TRACE`, `02_HISTO_ET_FUSIONNE`) restent valables ; ce chapitre complete et, en cas de conflit sur le plafond de jours, l'emporte. Difference avec la regle "normale" (docs) : dans `historique\` on garde les fichiers indefiniment, aucun plafond de jours.

1. **Un fichier par jour, sans limite de jours** : une sauvegarde `.bak_AAAA_MM_JJ` par fichier et par jour, gardee indefiniment (le plafond de 3 jours de l'etape 5 ne s'applique pas ici).
2. **`.bak` horodates (`.bak_AAAA_MM_JJ_HHhMMmSSs`)** : pour chaque fichier et chaque jour, le plus recent (heure lue dans le nom) est renomme `.bak_AAAA_MM_JJ` (meme extension), les autres vont a la corbeille Windows. Si le nom `.bak_AAAA_MM_JJ` existe deja : garder l'existant, mettre les horodates a la corbeille et le signaler. Le jour meme, les horodates sont gardes (10 au plus) tant qu'Eric n'ordonne pas autrement ; ordre d'Eric du 2026-10-21 : renommage fait aussi pour le jour meme.
3. **Fichiers du meme jour a suffixe `_sN`** (`menage_dry_run_2026-10-18_s2.txt`, etc.) : fusionnes en un seul fichier du jour (`menage_dry_run_2026-10-18.txt`), les sources dans l'ordre de leur heure de modification, chacune precedee de la ligne `=== SOURCE : nom (modifie AAAA-MM-JJ HH:MM) ===`, en UTF-8 sans BOM. Controler que la taille du fusionne couvre la somme des sources AVANT d'envoyer les sources a la corbeille. Un fichier `_sN` seul ce jour-la (sans base) est renomme sans le suffixe seulement si son nom ne change pas de famille ; les `.json` et les noms de famille differente ne sont pas fusionnes.
4. **`.txt` avec jumeau `.html`** : un `.txt` dont le `.html` de meme nom existe dans le meme dossier (taille non nulle) va a la corbeille Windows (cas des rapports `trigul_arbres_*`), y compris ses `.bak`.
5. **Doublons exacts** (meme MD5) : signales a Eric, jamais supprimes sans ordre.
6. Garde-fous du chapitre commun (collision, date illisible, nom douteux, erreur de la corbeille) : ne rien supprimer, signaler. Tout part a la corbeille Windows (restaurable : une fois restaure, `Shell.Application` espace 10, deplacer le fichier `$R` vers le nom cible) ; pas de go a attendre.
7. Plan et compte rendu dans `historique\03_RAPPORTS\02_MENAGE_BAK\menage_historique_AAAA-MM-JJ.txt` (chemin d'origine de chaque envoi en corbeille, liste des renommages et des fusions), cite dans le rapport final. Journal des modifs : une ligne LOT avec ce chemin au-dela de 10 fichiers.
### Garde-fous (ne rien supprimer, remonter le souci)

- Collision : le nom cible existe deja (ex : un `.bak_2026_10_07` est deja present pour ce fichier) -> ne pas renommer, ne pas supprimer, signaler le groupe.
- Date illisible ou impossible (mois 13, jour 32) -> ne pas traiter, signaler.
- Nom douteux (pourrait etre un vrai fichier et non une sauvegarde) -> ne pas traiter, signaler.
- Famille D sans fichier de travail non date dans le dossier -> ne pas traiter, signaler.
- Fichier non date contenant `backup`, `save` ou `old`, sans version de travail voisine (ex : `ha_git_backup.sh`) -> vrai fichier, ne pas traiter.
- Exports `Dashboard_COMPLET` -> jamais traites.
- Erreur de la corbeille (fichier verrouille, acces refuse) -> ne pas retenter par une autre methode, signaler.
- Avant de lancer l'etape pour la premiere fois sur un dossier : produire d'abord la liste (DRY-RUN : renommages et envois en corbeille prevus) et la presenter, sans rien modifier, puis attendre le go de l'utilisateur (seul arret autorise de /histo). Dans tous les autres cas, quel que soit le nombre de fichiers (decision d'Eric le 2026-10-15) : aucun go a attendre ; ecrire la liste dans historique\03_RAPPORTS\02_MENAGE_BAK\menage_dry_run_AAAA-MM-JJ.txt, la citer dans le rapport final, puis executer. Relire le plan avant de le presenter ou de l'executer : aucune cible ne doit etre tronquee, aucun export Dashboard ni vrai fichier ne doit y figurer, et le plafond de 3 doit etre calcule apres les renommages de la famille D. Executer ensuite sans re-demander ; le tree (etape 6) est fait apres l'execution du menage, ou le rapport precise que ses comptages sont d'avant menage.

### Rapport (a mettre dans le rapport final)

- nombre de fichiers renommes, envoyes a la corbeille, ignores (archives / jour courant)
- liste des soucis signales (collision, date illisible, nom douteux, erreur) avec le chemin complet
- pour chaque envoi en corbeille : le chemin d'origine (restaurable depuis la corbeille Windows)
- pour `historique\` (toute l'arborescence) : .bak horodates renommes, fusions `_sN`, `.txt` avec `.html` a la corbeille, corbeille, signales, avec le chemin de `historique\03_RAPPORTS\02_MENAGE_BAK\menage_historique_AAAA-MM-JJ.txt`
- pour `historique\03_RAPPORTS\06_MD5\` : les memes comptes, separes de ceux de docs, avec le chemin du plan et du compte rendu (`historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_*.txt`) et la liste des cas "date deduite du nom du rapport"
- pour `TODO\` : sauvegardes renommees, envoyees a la corbeille, signalees, avec le chemin du plan du menage

---

## ETAPE 5B - EXPORT DASHBOARD (enchaine automatiquement, apres le menage, sans demander)

Eric depose de temps en temps un export du dashboard a la racine de la prod (`H:\Dashboard_*.yaml`). Cette etape le recupere en local, puis ne garde qu'un seul export en prod. Elle compare par MD5, jamais par le nom (le 2026-10-11, `H:\Dashboard_2026_10_04.yaml` avait le contenu de l'export du 11/10).

Dossiers : local `C:\Users\Berry Swann\Documents\ReBuild\docs\02_docs_dashboard\02_dashboard_docs_yaml\Dashboard_COMPLET\` ; prod `H:\docs\02_docs_dashboard\02_dashboard_docs_yaml\Dashboard_COMPLET\`.

1. Pour chaque `H:\Dashboard_*.yaml` a la racine : calculer le MD5 et le comparer a celui de chaque export du dossier local. Si un export local a le meme MD5 : rien a copier. Sinon l'export est nouveau : le copier dans le dossier local en gardant le meme nom. Si ce nom existe deja en local avec un autre contenu (erreur de nommage), le copier sous `Dashboard_AAAA_MM_JJ.yaml`, date = date de derniere modification du fichier de la racine ; si ce nom existe aussi avec un autre contenu : ne rien copier, signaler. Le fichier de la racine n'est jamais modifie ni supprime.
2. Les exports locaux sont tous conserves tels quels, sans `.bak` (le menage de l'etape 5 ne les traite pas).
3. Prod : prendre l'export local le plus recent (date dans le nom `Dashboard_AAAA_MM_JJ`, a defaut date de modification). Si le dossier prod ne contient pas un fichier de meme MD5 : le copier dans le dossier prod, verifier le MD5 apres copie, puis supprimer les autres exports du dossier prod. H: n'a pas de corbeille, donc jamais de suppression definitive : chaque export a supprimer est d'abord copie dans `TEMPO\Dashboard_prod_supprimes_AAAA-MM-JJ\` (meme arborescence), le MD5 de la copie est verifie, et seulement ensuite le fichier est supprime sur H: ; rapport dans le journal des modifs (regle TEMPO de CLAUDE.md, decidee par Eric le 2026-10-18 ; la copie TEMPO ira plus tard a la corbeille Windows). Il ne doit rester qu'un seul export en prod, le plus recent. Jamais de sauvegarde sur H:.
4. Si le dossier prod contient deja le plus recent et lui seul : noter "Dashboard deja a jour".

---

## ETAPE 6 - TREE (enchaine automatiquement, apres le menage)

Met a jour l'arborescence documentee : `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` (comptages LOCAL, PROD et GitHub). Cette etape vient en dernier pour que les comptages refletent l'etat final apres le menage de l'etape 5.

1. Appliquer le protocole du skill `update-arbo` : comptages reels local et prod `H:\docs`, dernier commit et arbre GitHub, remplacements `.Replace()` stricts sur les seules lignes qui changent. Aucune valeur estimee ou memorisee.
2. Si les comptages sont identiques a ceux du fichier : ne rien modifier, noter "tree deja a jour".
3. Avant de modifier `IA_ARBO_DETAIL.md` : sauvegarde locale `IA_ARBO_DETAIL.bak_AAAA_MM_JJ_HHhMMmSSs.md` a cote du fichier (REGLE DE SAUVEGARDE, 10 max le jour meme).
4. Pousser ensuite vers `H:\docs\00_IA\SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` (MD5 local contre prod avant et apres). Jamais de sauvegarde sur H:.
5. Si l'API GitHub est injoignable : ne pas inventer de valeur, garder les anciennes valeurs GitHub du fichier et le signaler dans le rapport.
6. Ne pas modifier les sections narratives du fichier.
7. Controle des 9 fichiers de `docs\00_IA\SOUS_CONTEXT_IA\` (decide le 2026-10-13, apres le push de IA_ARBO_DETAIL pour que le MD5 prod soit definitif) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\check_sous_context_ia\check_sous_context_ia.py"`. Script en LECTURE SEULE : il ne corrige rien. Il verifie par fichier la structure (un dossier par fichier, baks bien nommes, plafonds 10 le jour meme / 3 par jour passe), le MD5 prod (IA_SKILLS_INVENTAIRE absent de la prod = attendu), la date declaree en en-tete (ecart au-dela de 60 jours), les chemins `docs/NN_...` cites qui n'existent plus, les nombres "N automations" / "N vignettes" contre la prod et les dossiers, et les entites citees absentes du registre HA et des etats. Mettre dans le rapport final la derniere ligne `controle sous_context_ia: dossiers=N baks=N ecarts=N casses=N` et chaque ecart cite. Le script controle aussi (depuis le 2026-10-17) que chaque chemin `docs/00_IA/...md` cite dans `Claude md SAVE\CLAUDE.md` existe en local avec la casse exacte : mettre dans le rapport la ligne `CLAUDE.md : chemins docs/00_IA cites=N morts=N` ; un chemin mort est un ecart signale a Eric, a corriger dans CLAUDE.md et ses 3 fichiers apparentes seulement sur sa demande. Un ecart nouveau par rapport a la session precedente est signale a Eric, jamais corrige sans demande. Si H: est inaccessible : le noter sans bloquer. Fichiers figes : ceux listes dans la constante FIGES du script (nom -> date du gel) ne subissent plus de controle de contenu, seulement structure, baks et MD5 prod, plus un ecart "fige mais modifie depuis" ; seul Eric decide de figer un fichier, ne jamais en figer de soi-meme. (Depuis le 2026-10-18, SOUS_CONTEXT_IA compte aussi IA_CARTE_EMPLACEMENTS : si le script annonce un nombre de dossiers different de 9, c'est attendu, le signaler sans corriger.)
8. Controle de tous les index globaux (decide le 2026-10-13, apres les regenerations de l'etape 2 et les pushs) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\check_global_index\check_global_index.py"`. Script en LECTURE SEULE. Il verifie, pour GLOBAL_INDEX_REPO, GLOBAL_INDEX_AUTOMATIONS, GLOBAL_INDEX_VIGNETTES_PAGES, GLOBAL_INDEX_SCRIPTS_SH, GLOBAL_INDEX_SCRIPTS_YAML, ENTITES_GLOBAL_INDEX et GLOBAL_INDEX_IA : l'existence, les liens casses (ceux de GLOBAL_INDEX_REPO sont relatifs a la racine du depot : resolus dans ReBuild puis en prod), l'equilibre des balises details et blockquote du REPO, la presence et le MD5 en prod (GLOBAL_INDEX_REPO aux 2 emplacements), les entites citees absentes du registre HA et des etats (REPO et ENTITES). Mettre dans le rapport final la derniere ligne `controle global_index: index=N liens=N casses=N ecarts=N` et chaque ecart cite. Ne rien corriger sans demande : les liens casses deja connus de la section 03 de GLOBAL_INDEX_REPO sont signales a Eric, jamais reecrits en masse. Pour un index genere, un lien casse ou un ecart de contenu = relancer d'abord le generateur (etape 2) puis ce script ; si l'ecart reste, le signaler. Si H: est inaccessible : le noter sans bloquer.
9. Controle des fichiers a plusieurs emplacements (decide par Eric le 2026-10-18, apres les pushs) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\Verif_emplacements\Verif_emplacements.py"`. Script en LECTURE SEULE (carte : `docs\00_IA\SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md`). Il compare chaque fichier de config, GLOBAL_INDEX_REPO et README aux 5 emplacements (local, prod racine, prod miroir docs, GitHub racine, GitHub docs/). Mettre dans le rapport final les lignes `ANOMALIES` et `RESULTAT` du script et chaque fichier PROD DIFFERENTE DU LOCAL ou present ailleurs qu'en local. GITHUB EN ATTENTE DU BACKUP juste apres un push est normal. Ne rien corriger sans demande. Si H: est inaccessible (code retour 2) : le noter sans bloquer.
10. Controle des integrations File (notify) de HA (decide par Eric le 2026-10-23) : `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_sh\Verif_integrations_file\Verif_integrations_file.py"`. Script en LECTURE SEULE (fiche : `docs\01_docs_config_system\config_system_MD\integrations_file\integrations_file.md`). Il compare les entrees File de HA (H:\.storage\core.config_entries et core.entity_registry, domaine et plateforme file seulement) au tableau de la fiche : chemin, entite notify, horodatage, entree desactivee. Mettre dans le rapport final les lignes `ANOMALIES` et `RESULTAT` et chaque ligne en ecart (MANQUANT DANS HA, ENTITE DIFFERENTE, HORODATAGE ACTIF, ENTREE DESACTIVEE, EN TROP). Un ECART apres un ajout ou un retrait d'integration par Eric : mettre a jour la fiche sur sa demande, ne jamais ecrire dans .storage. Rapport : `historique\03_RAPPORTS\06_MD5\05_VERIF_INTEGRATIONS_FILE\`. H: inaccessible (code retour 2) ou fiche illisible (code 3) : le noter sans bloquer.

---
## ORDRE D'EXECUTION STRICT

0. Journal de trace : `seq-debut histo` (sauf si appele par /histo-final), puis `debut` / `fin` autour de chaque etape ci-dessous
1. Bash : determiner date + numero session
2. Generer le bloc journal
3. Ecrire `historique/histo_[date]_s[N].md`
4. Presenter le fichier
5. Enchainer sync_index (dont GLOBAL_INDEX_REPO.md) sans pause ni question
6. Mettre a jour le journal fusionne (etape 3)
7. Copier dans Obsidian (etape 4)
7B. Pages HTML sombres (etape 4B) : `histo_html.py`, verification, originaux `.md`/`.txt` convertis a la corbeille
8. Menage des sauvegardes (etape 5, docs, puis historique\03_RAPPORTS\06_MD5\, puis historique\01_JOURNAL_TRACE\, puis historique\02_HISTO_ET_FUSIONNE\, puis le reste de historique\)
9. Export Dashboard (etape 5B)
10. Mettre a jour le tree et lancer les controles (etape 6, points 1 a 10)
11. Journal de trace : `histo_trace.py verifier`, puis `seq-fin`, puis `histo_trace.py recap`, puis `histo_trace.py html` (sauf si appele par /histo-final)
12. Afficher le rapport final

### Format de rapport final (apres toutes les etapes)

```
SYNC_INDEX - [date]

Fichiers mis a jour :
- DEPENDANCES_GLOBALES.md : date en tete -> [date session] | push prod : [MD5 identique | non pousse (raison)]
- GLOBAL_INDEX_REPO.md : [entrees ajoutees / compteurs modifies] | deja a jour (sauvegarde : [nom du .bak]) | push prod : [miroir docs et racine H: MD5 identiques | non pousse (raison)]
- GLOBAL_INDEX_AUTOMATIONS.md : [regenere | inchange] | resume du script : [prod / local_yaml / fiches / sans_yaml / sans_fiche / sans_entity / id_different]
- GLOBAL_INDEX_VIGNETTES_PAGES.md : [regenere | inchange] | resume du script : [vignettes / dossiers / manques / seul_md / seul_yaml / sans_dependances]
- GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md : [regenere | inchange] | resume du script : [SH scripts / sans_fiche / prod_different ; YAML scripts / sans_yaml / different / sans_fiche / py_dans_yaml]
- GLOBAL_INDEX_IA.md : [regenere | inchange] | resume du script : [liens / casses / sans_description]
- [autres fichiers si applicable]

JOURNAL FUSIONNE :
- [nom du fichier] : [n] lignes, sessions ajoutees : [liste]

OBSIDIAN :
- [fichier] : copie, MD5 identique | non copie (deja present) | DIFFERENT

PAGES HTML :
- page du jour : [cree | mis a jour (bak ...) | inchange | COLLISION] ; page du fusionne : [cree | mis a jour | inchange | COLLISION]
- originaux .md/.txt a la corbeille Windows : [n] (liste : historique\03_RAPPORTS\02_MENAGE_BAK\pages_html_AAAA-MM-JJ.txt) | aucun

MENAGE .bak :
- docs : renommes : [n] | corbeille Windows : [n] | ignores : [n]
- historique\03_RAPPORTS\06_MD5\ : renommes : [n] | corbeille Windows : [n] | signales : [n] (date deduite du nom du rapport : [n]) | plan et compte rendu : [historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_dryrun_AAAA-MM-JJ.txt, historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_AAAA-MM-JJ.txt]
- historique\01_JOURNAL_TRACE\ (pages HTML, sans LOGS\) : renommes : [n] | corbeille Windows : [n] | signales : [n]
- historique\02_HISTO_ET_FUSIONNE\ (pages HTML, FUSIONNE\ compris, et .bak) : renommes : [n] | corbeille Windows : [n] | signales : [n]
- historique\ (toute l'arborescence, 03_RAPPORTS compris) : .bak horodates renommes en .bak_DATE : [n] | fusions _sN : [n] | txt avec html a la corbeille : [n] | corbeille Windows : [n] | signales : [n] | plan : historique\03_RAPPORTS\02_MENAGE_BAK\menage_historique_AAAA-MM-JJ.txt
- soucis a traiter : [liste avec chemin complet] | aucun

DASHBOARD :
- racine H: : [fichier] : nouveau, copie en local | deja present (MD5) | aucun export
- prod Dashboard_COMPLET : [export unique] ; supprimes : [liste] | deja a jour

TREE :
- IA_ARBO_DETAIL.md : [comptages modifies] | deja a jour (sauvegarde : [nom du .bak]) ; MD5 local = prod : OK | ECART

SOUS_CONTEXT_IA :
- controle sous_context_ia: dossiers=[n] baks=[n] ecarts=[n] casses=[n] ; ecarts : [liste fichier : ecart] | aucun
- CLAUDE.md : chemins docs/00_IA cites=[n] morts=[n]
- entites introuvables a verifier : [liste] | aucune

INDEX GLOBAUX :
- controle global_index: index=[n] liens=[n] casses=[n] ecarts=[n] ; detail : [liste index : ecart] | aucun

EMPLACEMENTS :
- [ligne ANOMALIES] ; [ligne RESULTAT] ; ecarts : [liste fichier : verdict] | aucun

INTEGRATIONS FILE :
- [ligne ANOMALIES] ; [ligne RESULTAT] ; ecarts : [liste ligne : verdict] | aucun

TRACE :
- historique\01_JOURNAL_TRACE\LOGS\histo_trace_AAAA-MM-JJ.log : [aucune anomalie | anomalies et validations demandees]

PAGE :
- historique\01_JOURNAL_TRACE\histo_trace_AAAA-MM-JJ.html : [cree | mis a jour (bak ...) | inchange | non lance]

HORODATAGE :
- [sortie de `histo_trace.py recap` : tache 1 debut HH:MM:SS ; tache N (duree de la tache N-1) -> debut HH:MM:SS ; fin de sequence ; duree totale | absent si appele par /histo-final]

>> [fichier introuvable ou incomplet si applicable]
```

---
## NOTE HISTORIQUE - limite de 30 fichiers du menage, supprimee le 2026-10-15

Trace gardee a la demande d'Eric (2026-10-15 20h11), pour retrouver ce qui a change si un menage touche un fichier par erreur. Cette note ne s'applique pas : c'est un historique.

- Avant le 2026-10-15, l'etape 5 s'arretait apres le dry-run et attendait le go d'Eric si c'etait la premiere execution sur un dossier OU si plus de 30 fichiers etaient concernes. /histo-final (ligne 15) reprenait cette regle : pas d'extinction tant que le menage attendait le go.
- Le 2026-10-15 (ordres d'Eric a 19h27, 19h35 et 20h08), le go au-dela de 30 fichiers a ete supprime. Le plan est ecrit dans historique\03_RAPPORTS\02_MENAGE_BAK\menage_dry_run_AAAA-MM-JJ.txt, cite dans le rapport final, puis execute sans attente. Seule pause restante : la premiere execution du menage sur un dossier.
- Contexte de la decision : le 2026-10-14, un /histo-final est reste 2h20 en attente du go (77 actions) et n'a pas pu eteindre les lumieres ni le PC. Ce soir-la, mon premier calcul du dry-run annoncait 362 envois en corbeille a cause d'un bug de ma part (plage PowerShell 1..0 sur un groupe d'un seul fichier) ; il avait ete rattrape avant execution justement grace a la relecture du plan. Sans la pause, ce plan faux aurait ete execute.
- Si un fichier a ete envoye a tort a la corbeille : il est dans la corbeille Windows (jamais de suppression definitive) tant qu'elle n'est pas videe. Plans et rapports : historique\03_RAPPORTS\02_MENAGE_BAK\menage_dry_run_*.txt et historique\03_RAPPORTS\02_MENAGE_BAK\menage_execute_*.txt (chemins d'origine). Journal des modifs : historique\modifs\MODIFS_AAAA-MM-JJ_claude.md.
- Texte exact de l'ancienne ligne (supprimee de l'etape 5) :

```text
- Avant de lancer l'etape pour la premiere fois sur un dossier, ou si plus de 30 fichiers sont concernes : produire d'abord la liste (DRY-RUN : renommages et envois en corbeille prevus) et la presenter, sans rien modifier, puis attendre le go de l'utilisateur (seul arret autorise de /histo). Relire le plan avant de le presenter : aucune cible ne doit etre tronquee, aucun export Dashboard ni vrai fichier ne doit y figurer, et le plafond de 3 doit etre calcule apres les renommages de la famille D. Executer ensuite sans re-demander ; le tree (etape 6) est fait apres l'execution du menage, ou le rapport precise que ses comptages sont d'avant menage.
```