# Reference /histo - Step 6: tree and checks, and final report format

> Reference file of the histo skill, read when step 6 is executed and when writing the final report. Paths, file names, script output lines and badge values stay in French on purpose (they are real names on disk or exact strings produced by scripts).

## STEP 6 - TREE (chained automatically, after the cleanup)

Updates the documented tree: `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` (LOCAL, PROD and GitHub counts). This step comes last so the counts reflect the final state after the step 5 cleanup.

1. Apply the protocol of the `update-arbo` skill: real counts for local and prod `H:\docs`, last commit and GitHub tree, strict `.Replace()` replacements on the changing lines only. No estimated or remembered value.
2. If the counts are identical to those in the file: change nothing, note "tree deja a jour".
3. Before modifying `IA_ARBO_DETAIL.md`: local backup `IA_ARBO_DETAIL.bak_AAAA_MM_JJ_HHhMMmSSs.md` beside the file (BACKUP RULE, 10 max per day).
4. Then push to `H:\docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_ARBO_DETAIL\IA_ARBO_DETAIL.md` (local MD5 against prod before and after). Never a backup on H:.
5. If the GitHub API is unreachable: do not invent a value, keep the old GitHub values of the file and report it.
6. Do not modify the narrative sections of the file.
7. Check of the 9 files of `docs\00_IA\00_IA_SOUS_CONTEXT_IA\` (decided 2026-10-13, after the IA_ARBO_DETAIL push so the prod MD5 is final): `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_sous_context_ia\check_sous_context_ia.py"`. READ-ONLY script: it corrects nothing. Per file it checks the structure (one folder per file, correctly named baks, caps 10 the same day / 3 per past day), the prod MD5 (IA_SKILLS_INVENTAIRE absent from prod = expected), the date declared in the header (gap beyond 60 days), the cited `docs/NN_...` paths that no longer exist, the numbers "N automations" / "N vignettes" against prod and folders, and the cited entities missing from the HA registry and states. Put in the final report the last line `controle sous_context_ia: dossiers=N baks=N ecarts=N casses=N` and each gap quoted. Since 2026-10-17 the script also checks that each `docs/00_IA/...md` path cited in `Claude md SAVE\CLAUDE.md` exists locally with the exact case: put in the report the line `CLAUDE.md : chemins docs/00_IA cites=N morts=N`; a dead path is a gap reported to Eric, to be fixed in CLAUDE.md and its 3 related files only on his request. A gap that is new compared to the previous session is reported to Eric, never fixed without a request. If H: is inaccessible: note it without blocking. Frozen files: those listed in the FIGES constant of the script (name -> freeze date) get no more content check, only structure, baks and prod MD5, plus a "fige mais modifie depuis" gap; only Eric decides to freeze a file, never freeze one on your own. (Since 2026-10-18, 00_IA_SOUS_CONTEXT_IA also holds IA_CARTE_EMPLACEMENTS: if the script announces a folder count different from 9, that is expected, report it without correcting.)
8. Check of all global indexes (decided 2026-10-13, after the step 2 regenerations and the pushes): `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\check_global_index\check_global_index.py"`. READ-ONLY script. For GLOBAL_INDEX_REPO, GLOBAL_INDEX_AUTOMATIONS, GLOBAL_INDEX_VIGNETTES_PAGES, GLOBAL_INDEX_SCRIPTS_SH, GLOBAL_INDEX_SCRIPTS_YAML, ENTITES_GLOBAL_INDEX and IA_GLOBAL_INDEX it checks: existence, broken links (those of GLOBAL_INDEX_REPO are relative to the repository root: resolved in ReBuild then in prod), balance of the details and blockquote tags of the REPO, presence and MD5 in prod (GLOBAL_INDEX_REPO at the 2 locations), cited entities missing from the HA registry and states (REPO and ENTITES). Put in the final report the last line `controle global_index: index=N liens=N casses=N ecarts=N` and each gap quoted. Correct nothing without a request: the already known broken links of section 03 of GLOBAL_INDEX_REPO are reported to Eric, never rewritten in bulk. For a generated index, a broken link or a content gap = first rerun the generator (step 2) then this script; if the gap remains, report it. If H: is inaccessible: note it without blocking.
9. Check of files at several locations (decided by Eric on 2026-10-18, after the pushes): `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py"`. READ-ONLY script (map: `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md`). It compares each config file, GLOBAL_INDEX_REPO and README across the 5 locations (local, prod root, prod docs mirror, GitHub root, GitHub docs/). Put in the final report the `ANOMALIES` and `RESULTAT` lines of the script and each file with PROD DIFFERENTE DU LOCAL or present somewhere other than local. GITHUB EN ATTENTE DU BACKUP right after a push is normal. Correct nothing without a request. If H: is inaccessible (return code 2): note it without blocking.
10. Check of the HA File (notify) integrations (decided by Eric on 2026-10-23): `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_integrations_file\Verif_integrations_file.py"`. READ-ONLY script (sheet: `docs\01_docs_config_system\01_config_system_MD\integrations_file\integrations_file.md`). It compares the File entries of HA (H:\.storage\core.config_entries and core.entity_registry, domain and platform file only) with the table of the sheet: path, notify entity, timestamp, disabled entry. Put in the final report the `ANOMALIES` and `RESULTAT` lines and each line in gap (MANQUANT DANS HA, ENTITE DIFFERENTE, HORODATAGE ACTIF, ENTREE DESACTIVEE, EN TROP). A gap after an integration was added or removed by Eric: update the sheet on his request, never write in .storage. Report: `historique\03_RAPPORTS\06_MD5\05_VERIF_INTEGRATIONS_FILE\`. H: inaccessible (return code 2) or unreadable sheet (code 3): note it without blocking.
11. Check of the `.md` sheets and of the 8 badges, creation of missing badges (requested by Eric on 2026-10-28). Trace: `debut controles_6F` / `fin controles_6F`. Badge rule: section "BADGES DES FICHES .md - REGLE UNIQUE" of CLAUDE.md (order Statut, MaJ, HA, IA Partner, Source, Modifs, Expert, Type). Four sub-checks, in this order:
    a. One sheet per source: `$env:PYTHONIOENCODING='utf-8'; python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\gen_moc_docs\gen_moc_docs.py" --dry` then `python -I -X utf8 "...\gen_moc_dashboard\gen_moc_dashboard.py" --dry`. Read-only (--dry writes nothing). Put in the report the lines `sources=N avec_fiche=N sans_fiche=N` and each source without a sheet. A source without a sheet is REPORTED, the sheet is not created on the spot (it is created at Eric's request, from a real reading of the source).
    b. Badges, check: `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_badges_fiches\Check_badges_fiches.py"` (read-only without option). Exempt: only the English skill copies `docs/05_docs_skills/05_docs_skills_PURE` (with their `.bak`) and the template `_Template_doc.md` (never rewritten by --fix). The French skill sheets of `docs/05_docs_skills/05_docs_skills_MD` are normal sheets (8 badges, Type `Skill`, yellow ffeb3b). Since 2026-10-31 (Eric's order: badges everywhere) are no longer exempt: the `.bak` (--bak mode, point d.), `MOC_*` (including `MOC_SKILLS.md`), `GLOBAL_INDEX_*` (their generators write the banner themselves) and `docs/00_IA`; since 2026-10-30, `XX_*`, `*_ORIGINAL` and `*_archive*` are no longer exempt: they receive the Statut Archive or Original. Put in the report the last line `controle badges: fiches=N conformes=N a_corriger=N a_decider=N corrigees=N`.
    c. Badges, creation on the spot: rerun with `--fix --limite 20`. It creates the missing badges (never modifies an existing badge), with a `.bak_AAAA_MM_JJ_HHhMMmSSs.md` beside each modified sheet, at most 20 sheets per pass (progressive catch-up, like the 19 or 20 deletions rule: no pause, the rest is resumed at the next /histo). Automatic values: HA read live from `H:\.HA_VERSION`, MaJ = today's date, IA Partner `Claude_Sonnet_5.5` (if Hermes writes the sheet: his name), Source `Interne`, Modifs `Autorisees`, Expert `HAOS_Proxmox`, Type by folder: `Scripts` for `04_docs_scripts`, `Automation` for `03_docs_automations`, `Dashboard` for `02_docs_dashboard`, `System` for `01_docs_config_system`, `99_docs_MD_system` and `00_IA` (decided by Eric on 2026-10-31), `Skill` for `05_docs_skills` (decided by Eric on 2026-10-31, yellow ffeb3b). The Statut is automatic (see the 2026-10-30 update below). The Type outside these folders is NEVER guessed: the sheet is listed `a_decider` in the report, to be settled with Eric. A sheet whose badges are outside a `<div align="center">` block is listed "forme a revoir", not corrected. A value outside the list (e.g. `Script_Executant` written with an accent) is reported, never corrected without a request.
    d. Badges of the `.bak` (Eric's order of 2026-10-31): `python -I -X utf8 "...\Check_badges_fiches\Check_badges_fiches.py" --bak` (read-only) then `--bak --fix`: all `.md` `.bak` of `docs` (except `05_docs_skills_PURE`) receive the Statut `bak_h` (timestamped of the day) or `bak_d` (dated, 3 days), orange; `Trash` (red) is set only by the definitive cleanup just before the recycle bin. The other badges stay unchanged or are added when possible (`Inconnu` if not found). No `.bak` of a `.bak`. Report line: `controle badges .bak: a_corriger=N corriges=N a_revoir=N`.
    e. Modification journal: one line per corrected sheet, or one LOT line with the report path beyond 10. If the script is missing or fails: say so in the report and continue (does not block the sequence, does not block the /histo-final shutdown).
   Update of 2026-10-30: the Statut is no longer guessed only by Eric. Automatic values: Statut `Actif` by default; `Original` (yellow `ffeb3b`, decided by Eric on 2026-10-31) for `*_ORIGINAL` paths (originals of automations and scripts); `Archive` (grey `9e9e9e`) for `*archive*` folders and `XX_` folders; `bak_h` / `bak_d` (orange `ff9800`) are set by the `--bak` mode and `Trash` (red `f44336`) by the definitive cleanup (step 5, point 8). Exceptions (sheet with Modifs INTERDITES, for example `PAGE_MAJ.md`) are given by Eric case by case: the existing Modifs badge is never changed. The Type is still not guessed outside the folders listed in point c: sheet `a_decider`. `XX_`, `*_ORIGINAL` and `*archive*` sheets are no longer exempt from the check, they receive their own Statut.
12. Freshness check of the 2 memory files of Claude (decided by Eric on 2026-10-29: they must be IMPERATIVELY up to date to quickly find the little one in case of trouble): `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_DEPENDANCES\Check_DEPENDANCES.py"`. Read-only, trace step `controles_6G`. It checks DEPENDANCES_GLOBALES_CLAUDE_memoire.md (automations of H:\automations.yaml without a section, docs YAML modified after the header date, dead paths) and IA_GLOBAL_INDEX_memoire.md (00_IA files missing or newer than the index). If `ecarts` > 0: Claude fixes without waiting (DEPENDANCES: the section or line concerned, .bak first, header date, modification journal, push to prod by step 5C, a name "A VERIFIER" may be a different label: check before adding; index: rerun Gen_GLOBAL_INDEX_ia.py), then reruns the script. A remaining gap is reported in the report (line MEMOIRE CLAUDE) and does not block /histo-final. Sheet: docs\04_docs_scripts\04_docs_scripts_SH_MD\Check_DEPENDANCES\Check_DEPENDANCES.md.
13. Push catch-up (decided by Eric on 2026-10-30): points 11 and 12 may modify `docs` files after step 5C (badged sheets, DEPENDANCES_GLOBALES_CLAUDE_memoire.md, IA_GLOBAL_INDEX_memoire.md, IA_ARBO_DETAIL.md). Redo the MD5 comparison of step 5C, but only for the files modified by points 11 and 12 (same exclusions, same safeguards), and push them. Trace: `debut push_docs` / `fin push_docs` (line `rattrapage`). The PROD counts of IA_ARBO_DETAIL.md are taken before this catch-up: a gap of a few files is reported in the report, not fixed by hand.

---

### Final report format (after all steps)

The labels below are kept in French on purpose: Eric reads the report and other files grep these labels.

```
SYNC_INDEX - [date]

Fichiers mis a jour :
- DEPENDANCES_GLOBALES_CLAUDE_memoire.md : date en tete -> [date session] | push prod : par l'etape 5C (voir PUSH PROD DOCS)
- GLOBAL_INDEX_REPO.md : [entrees ajoutees / compteurs modifies] | deja a jour (sauvegarde : [nom du .bak]) | push prod : [miroir docs et racine H: MD5 identiques | non pousse (raison)]
- GLOBAL_INDEX_AUTOMATIONS.md : [regenere | inchange] | resume du script : [prod / local_yaml / fiches / sans_yaml / sans_fiche / sans_entity / id_different]
- GLOBAL_INDEX_VIGNETTES_PAGES.md : [regenere | inchange] | resume du script : [vignettes / dossiers / manques / seul_md / seul_yaml / sans_dependances]
- GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md : [regenere | inchange] | resume du script : [SH scripts / sans_fiche / prod_different ; YAML scripts / sans_yaml / different / sans_fiche / py_dans_yaml]
- IA_GLOBAL_INDEX_memoire.md : [regenere | inchange] | resume du script : [liens / casses / sans_description]
- [autres fichiers si applicable]

JOURNAL FUSIONNE :
- [nom du fichier] : [n] lignes, sessions ajoutees : [liste]

OBSIDIAN :
- [fichier] : copie, MD5 identique | non copie (deja present) | DIFFERENT

PAGES HTML :
- page du jour : [cree | mis a jour (bak ...) | inchange | COLLISION] ; page du fusionne : [cree | mis a jour | inchange | COLLISION]
- originaux .md/.txt a la corbeille Windows : [n] (liste : historique\03_RAPPORTS\02_MENAGE_BAK\pages_html_AAAA-MM-JJ.txt) | aucun

MENAGE .bak :
- docs : menage definitif [fait | non fait (histo non definitif)] | horodates renommes en .bak_AAAA_MM_JJ : [n] | corbeille Windows : [n] | ignores : [n]
- CORBEILLE Windows : elements de plus de 3 mois supprimes : [n] | aucun | lecture de la date impossible
- historique\03_RAPPORTS\06_MD5\ : renommes : [n] | corbeille Windows : [n] | signales : [n] (date deduite du nom du rapport : [n]) | plan et compte rendu : [historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_dryrun_AAAA-MM-JJ.txt, historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_AAAA-MM-JJ.txt]
- historique\01_JOURNAL_TRACE\ (pages HTML, sans LOGS\) : renommes : [n] | corbeille Windows : [n] | signales : [n]
- historique\02_HISTO_ET_FUSIONNE\ (pages HTML, FUSIONNE\ compris, et .bak) : renommes : [n] | corbeille Windows : [n] | signales : [n]
- historique\ (toute l'arborescence, 03_RAPPORTS compris) : .bak horodates renommes en .bak_DATE : [n] | fusions _sN : [n] | txt avec html a la corbeille : [n] | corbeille Windows : [n] | signales : [n] | plan : historique\03_RAPPORTS\02_MENAGE_BAK\menage_historique_AAAA-MM-JJ.txt
- soucis a traiter : [liste avec chemin complet] | aucun

DASHBOARD :
- racine H: : [fichier] : nouveau, copie en local | deja present (MD5) | aucun export
- prod Dashboard_COMPLET : [export unique] ; supprimes : [liste] | deja a jour

PUSH PROD DOCS :
- fichiers compares=[n] copies=[n] identiques=[n] ; signales : PROD DIFFERENTE INCONNUE=[liste] | seuls en prod=[liste] | _archive_=[liste] | aucun ; rattrapage de l'etape 6 point 13 : copies=[n] ; rapport : historique\03_RAPPORTS\02_MENAGE_BAK\push_docs_AAAA-MM-JJ.txt | H: inaccessible

TREE :
- IA_ARBO_DETAIL.md : [comptages modifies] | deja a jour (sauvegarde : [nom du .bak]) ; MD5 local = prod : OK | ECART

00_IA_SOUS_CONTEXT_IA :
- controle sous_context_ia: dossiers=[n] baks=[n] ecarts=[n] casses=[n] ; ecarts : [liste fichier : ecart] | aucun
MEMOIRE CLAUDE :
- controle Check_DEPENDANCES: ecarts=[n] ; [liste] | aucun ; corrections faites : [liste]
- CLAUDE.md : chemins docs/00_IA cites=[n] morts=[n]
- entites introuvables a verifier : [liste] | aucune

INDEX GLOBAUX :
- controle global_index: index=[n] liens=[n] casses=[n] ecarts=[n] ; detail : [liste index : ecart] | aucun

EMPLACEMENTS :
- [ligne ANOMALIES] ; [ligne RESULTAT] ; ecarts : [liste fichier : verdict] | aucun

INTEGRATIONS FILE :
- [ligne ANOMALIES] ; [ligne RESULTAT] ; ecarts : [liste ligne : verdict] | aucun

FICHES ET BADGES :
- sources sans fiche : [gen_moc_docs : sources=N avec_fiche=N sans_fiche=N ; gen_moc_dashboard : idem ; liste des sources sans fiche] | aucune
- controle badges: fiches=[n] conformes=[n] a_corriger=[n] a_decider=[n] corrigees=[n] ; fiches corrigees (badges crees) : [liste, au plus 20] | aucune
- controle badges .bak: a_corriger=[n] corriges=[n] a_revoir=[n]
- a decider avec Eric (Statut ou Type non devinables), forme a revoir, valeurs hors liste : [liste] | aucun

TRACE :
- historique\01_JOURNAL_TRACE\LOGS\histo_trace_AAAA-MM-JJ.log : [aucune anomalie | anomalies et validations demandees]

PAGE :
- historique\01_JOURNAL_TRACE\histo_trace_AAAA-MM-JJ.html : [cree | mis a jour (bak ...) | inchange | non lance]

HORODATAGE :
- [sortie de `histo_trace.py recap` : tache 1 debut HH:MM:SS ; tache N (duree de la tache N-1) -> debut HH:MM:SS ; fin de sequence ; duree totale | absent si appele par /histo-final]

TOKENS :
- consommes pendant la sequence : [N - M] (deduit du compteur de tokens restants de la session : debut [N], fin [M] ; pas une facture ; compteur de session) | inconnu (releve de debut ou de fin manquant) | inconnu (compteur non visible). La consommation de l'ecriture du rapport final n'est pas comptee.

>> [fichier introuvable ou incomplet si applicable]
```

---
