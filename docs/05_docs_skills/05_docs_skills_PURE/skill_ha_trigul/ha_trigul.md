---
name: "ha-trigul"
description: "HA ReBuild skill - triangulation of the docs between local (ReBuild), prod (H:) and GitHub: overlay of the 3 trees (extra, missing, case, content, format of the docs MD5 audit), deep step on automations/scripts and check of the files kept in 5 locations. Trigger on /trigul, trigul, triangulation, audit md5 des docs, les docs sont-ils a jour en prod et sur GitHub."
---

# Skill: /ha-trigul - triangulation of the docs (local / prod / GitHub)

> Files present in several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18, step C below).

## Goal

Three chained checks, reports stored in `historique\03_RAPPORTS\06_MD5\`, one numbered sub-folder per report type (see "Files and paths"). Read-only: the skill does not modify, push or correct any documentation file. It only writes the reports (and, for the deep step, the dated copies of prod in the ORIGINAL folders).

1. Overlay of the 3 trees (python script): does what the docs MD5 audit does on the HA side (H:\.scripts\audit_md5_md_yaml.sh, which compares prod to GitHub), but on the 3 levels GitHub, local, prod. It builds the union of the paths, all file types, sets aside what is extra or missing (with its origin) and the case differences, then compares the content of what is common. It replaces the bash .md trigul since 2026-10-18 (Eric's decision: the .md trigul only saw the .md files and started from the local list, so it saw neither the files of prod or GitHub missing from local, nor the .yaml, nor the .sh).
2. Deep step: automations and YAML scripts unit by unit, then HA categories.
3. Files kept in several locations (config, GLOBAL_INDEX_REPO, README): 5 locations compared (step C).

The trigul is started by a launcher that writes a trace journal (see "Launch and trace journal"): it shows where the trigul stops the day it crashes, and detects silent failures (an old report taken for a new one, a script dead without noise).

Scope of the overlay: the whole `docs/` + the root README (`docs/01_docs_config_system/01_config_system_MD/README/README.md` in local, the original since 2026-10-18; `README.md` at the root of H: and of the repository, compared under the name `(racine)/README.md`), except `.bak` (completely ignored, neither counted nor quoted) and except the `modifs/` folder (agents' journals, ignored at the 3 levels since 2026-10-18, like the HA audit). The config YAML at the root of H: are not in the overlay: they are checked by step C.

Checked extensions (decided by Eric on 2026-10-25, based on prod `H:\docs`: only what makes HA work counts): `.md`, `.yaml`, `.sh`, `.py`, `.svg` and `.js` (the `.js` is a dashboard card: `Meteocss-card.js`). These 6 extensions are checked without exception: presence at the 3 levels, case, content. Everything else is ignored or set aside as an expected gap: `.bak` backups, `_archive_` archives, old `Dashboard_COMPLET` exports, `.pyc` caches, pending local `.patch`, `.gitignore` types (.txt .png .jpg .jpeg .gif .webp .ico), editor locks `#...#` (prod only), `modifs/` folder. Prod survey of 2026-10-25: 513 files = 235 .yaml, 228 .md, 18 .py, 16 .svg, 12 .sh, 1 .js, 3 locks. State of the script on 2026-10-25: it already scans all the paths, but the `RESULTAT AUDIT` line only counts .md .yaml .sh .py .svg: the `.js` falls into "autres" (to be changed in `hermes_audit_trigul_arbres.py`, Hermes perimeter, on Eric's request).

Source of truth = LOCAL (ReBuild). A local/prod gap means prod is BEHIND; a prod/repository gap means the repository is BEHIND. GitHub = last commit of the repository, fed by the HA backup (never a direct push): a delay after a push to prod is normal until the next backup.

Prerequisite: the session must be linked to the PC (Claude desktop). Without the link, neither H:, nor the local disk, nor the GitHub API are reachable (GitHub answers 403 from the cloud container): say so, do not conclude.

## Files and paths

- Script 1 (overlay of the trees): `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_trigul_arbres.py`
- Script 2 (deep): `...\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_unitaire.py` (same folder)
- Script 3 (locations): `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py`
- Launcher with trace journal (decided by Eric on 2026-10-18): `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\hermes_audit_md5_trigul_3md\trigul_run.py` (same folder as scripts 1 and 2). It runs scripts 1, 2 and 3 without modifying them.
- Old bash .md trigul: `...\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_3md.sh` (same folder as script 1). Do not run it anymore: it is redundant with script 1. The file stays in place (do not delete it without Eric's request).
- Interpreter: `python -I` (scripts 1, 2 and 3 and launcher).
- Reports folder: `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\06_MD5\`, with one numbered sub-folder per report type (decided by Eric on 2026-10-18):
  - `00_VERIF_FINAL_TRIGUL_ARBRES`: `trigul_arbres_[YYYY-MM-DD].txt` and `.html`, written by script 1 (tested on 2026-10-18: the 2 reports of the day are there);
  - `01_TRIGUL_PROFOND`: `trigul_profond_[YYYY-MM-DD].txt`, written by script 2 (checked on 2026-10-18: the report does arrive in this folder);
  - `02_CATEGORIES_HA`: `categories_ha_[YYYY-MM-DD].txt`, written by Claude at step B2, not by a script;
  - `03_VERIF_EMPLACEMENTS`: `verif_emplacements_[YYYY-MM-DD].txt`, written by script 3 (created on 2026-10-18).
  - `04_JOURNAL_TRIGUL`: `trigul_journal_[YYYY-MM-DD].log`, trace journal written by the launcher (one line per event, one file per day, appended);
  - A new report type = the next folder (`05_...`, then `06_...`): create it with its number, then add it here and in CLAUDE.md.
  - The cleanup of the `.bak` of these folders is done by /histo (step 5, chapter "Cas particulier : historique\03_RAPPORTS\06_MD5\"): 10 timestamped backups at most on the same day, 3 dated backups for past days; the reports themselves (one per day) are not limited.
- The old `hermes_md5_audit_md_*.txt` is no longer produced.
- HA audit report (prod against GitHub, for cross-checking): `H:\.logs\md5_audit_md_yaml_[YYYY-MM-DD].txt`.

The scripts can be modified on Eric's request (decision of 2026-10-17): backup `nom.bak_AAAA_MM_JJ_HHhMMmSSs.ext` in the same folder before any modification, syntax check (`python -I -W error -c "import ast..."` or `bash -n`), line in the modifications journal. Never push a script to prod (docs or H:\.scripts) without Eric's order. Script 1 has no sheet yet in 04_docs_scripts_SH_MD.

## Protocol

### Launch and trace journal (decided by Eric on 2026-10-18)

Start the trigul with the launcher: `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\hermes_audit_md5_trigul_3md\trigul_run.py"` (about 10 s). It chains A (script 1), B1 (script 2) and C (script 3), without modifying the scripts, and writes `historique\03_RAPPORTS\06_MD5\04_JOURNAL_TRIGUL\trigul_journal_[YYYY-MM-DD].log` line by line (time | level | step | message; levels INFO, SORTIE, STDERR, NOTE, OK, ATTENTION, ECHEC), each line forced to disk. After each script it checks: return code, Traceback, timeout (300 s), report missing, empty or not updated during this launch (an old report would be taken for the new one), end markers of the report (RESULTAT, script check: OK, ANOMALIES), temporary folder of the deep step left behind, the word "injoignable" in the output of script 3. Verdict per step: OK, ATTENTION or ECHEC. Launcher return code: 0 without ECHEC, 1 otherwise.

After the launch:
1. Read the ECHEC and ATTENTION lines of today's journal and put them AT THE TOP of the report.
2. If the last line of the journal is not `FIN DU LANCEUR`, the launcher was interrupted (PC off, session closed): say so and quote the last line.
3. Step B2 (HA categories) is done by Claude: add its line to the journal with `python -I trigul_run.py --note B2_categories_ha "texte"`.
4. An ECHEC is not corrected without a request: quote the step, the journal line and the file concerned.

Sections A, B and C below describe what each script does and how to read its report. Running a script alone is only for a test, outside the journal.

### A. Overlay of the 3 trees (script 1)

Run: `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_trigul_arbres.py"`. Duration: about 5 s, a single call. The script writes the `.txt` report and its `.html` version in `historique\03_RAPPORTS\06_MD5\00_VERIF_FINAL_TRIGUL_ARBRES\` and itself saves the reports of the day as `.bak_...` if they exist. It reads the complete list of the last GitHub commit through the API (api.github.com, one request, no download): it must run on the PC. If the list is truncated or the API does not answer, it stops with an error: say so, do not conclude. `--tout` option: also lists the SYNC files in the report.

Method:
- Each level is scanned entirely (local and prod: disk; GitHub: API list with the git blob SHA-1 of each file). Paths are grouped without regard to case, then the case is compared exactly.
- A path that is not at the 3 levels is set aside with its origin: `[L]` local only, `[P]` prod only, `[R]` GitHub only, `[LP]` absent from GitHub, `[LR]` absent from prod, `[PR]` absent from local. The same path with a different case between levels goes to the CASSE section.
- On the paths present at the 3 levels and with the same case: comparison of the fingerprint (git blob SHA-1 of the bytes; local and prod are recomputed the same way). Verdicts: SYNC, end of line only (no action), LOCAL ahead (prod = GitHub, local different: to push), GITHUB behind (local = prod, GitHub different: waits for the HA backup), PROD alone different (suspect), 3 different contents (to look at by hand).
- Expected gaps set aside with their reason (`EXCEPTIONS_TXT` list and `attendu()` function of the script, to be changed on Eric's request): local `_archive_` archives (local only), types ignored by the `.gitignore` of H: present in local + prod (.txt .png .jpg .jpeg .gif .webp .ico .pyc). The .svg are no longer an expected gap since 2026-10-18: Eric added `!docs/**/*.svg` to H:\.gitignore (the .svg outside docs stay ignored). The editor lock files `#...#` present in prod only (for example `.scripts/#MP_01_monitor_temp.sh.#`) are an expected gap since 2026-10-18 (decided by Eric: the `.gitignore` ignores them, they will never reach GitHub); script 3 lists them in section 3 ECARTS ATTENDUS of its report. Everything else is an anomaly.

DIFF column (Eric's rule of 2026-10-18): number of levels where the file is missing, plus 1 if the content differs between the present levels (end of line only: 0 for content). `aucune` if all is good, otherwise `x N diff` (1 missing level = 1 diff, 2 missing = 2 diff, different content = 1 diff, different content plus one missing = 2 diff, three contents all different = 2 diff).

Reading the report `trigul_arbres_[date].txt`, in order:
- header: GitHub commit used (sha, date, message), number of files per level;
- `== AUDIT ==`: line `RESULTAT AUDIT : N fichiers (a .md - b .yaml - c .sh - d .py - e .svg - f .js) - SYNC - fin de ligne seule - DIFF - CASSE - ABSENT GITHUB - ABSENT PROD - ABSENT LOCAL - ABSENT 2 NIVEAUX`, same scope (.md .yaml .sh .py .svg .js; the script today counts the first 5, the .js is in "autres") and same spirit as the RESULTAT of the HA audit, on the 3 levels; the statuses are mutually exclusive and their sum equals the total (the script checks it);
- `== COMPTES PAR NIVEAU ==`: one line `RESULTAT GitHub / local / prod / union : N fichiers (.md, .yaml, .sh, .py, .svg, .js, autres)`;
- `== VUE D ENSEMBLE ==`: paths of the union, SYNC, to handle by verdict, expected gaps;
- `== 1. A TRAITER ==`: columns `R (GitHub) | L (local) | P (prod) | R L P | DIFF | FICHIER`, a cell = short 8-character fingerprint or `-` if absent, `R L P` = presence (1 present, 0 absent). Caution: the mention `[meme contenu]` on a line where one level is absent means that the TWO present levels have the same fingerprint (for example GitHub = prod for a file absent from local). It does not mean that a local file with the same content exists under another name: check that separately by fingerprint;
- `== 2. ECARTS ATTENDUS == `;
- `== CONTROLE ==`: the sum of the paths (SYNC + to handle + expected) must equal the union, a file present everywhere must have 3 - 1 - 1 - 1 = 0; line `controle du script : OK` otherwise `ERREURS DU SCRIPT` (to report at the top of the account);
- last lines: `ANOMALIES : aucune` or `ANOMALIES : x N fichiers, M diff au total`, the `RESULTAT AUDIT` line, the `RESULTAT` line.

If almost everything is absent on the prod side, the H: prod was not visible from the launched process: check the access to H: before concluding.

Case trap (found on 2026-10-17): the H: prod is a case-insensitive SMB share. Copying a renamed file or folder from local to H: keeps the old name in prod, without error and with an identical MD5, and GitHub (fed by the HA backup from H:) also keeps the old name. The script reports this case in the CASSE section. To change the case in prod you must rename explicitly on H: (Rename-Item), files first then folders; GitHub follows at the next HA backup. On 2026-10-17: 283 names renamed in prod, then 0 case gap.

Other traps: the `.gitignore` of H: is a hidden file (writing it with `[IO.File]::WriteAllText` gives access denied: open with FileMode.Open, SetLength(0), then write). Right after an HA backup, GitHub can change: the report states the commit used.

### B. Deep step (automations and scripts, decided on 2026-10-11)

Unit-by-unit comparison of H:\automations.yaml and H:\scripts.yaml with the local YAML (prod against local; GitHub is not compared at this step). It is integrated in the /trigul (less than a second for 71 units). Full protocol: section PROTOCOLE TRIGUL PROFOND of CLAUDE.md.

1. Run: `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\hermes_audit_md5_trigul_3md\hermes_audit_md5_trigul_unitaire.py"`. The script follows 8 numbered steps (displayed `ETAPE n` and repeated in the report, line `ETAPES :`): (1) bak points: reserves the names `AUTOMATIONS_YAML_ORIGINAL\automations.bak_<date_heure>.yaml` and `04_docs_script_ORIGINAL\scripts.bak_<date_heure>.yaml`, creates the folders, stops (code 3) if a point already exists; (2) copy of `H:\automations.yaml` and `H:\scripts.yaml` to these points; (3) MD5 of each prod file against its bak: if one differs, ATTENTION but the analysis continues (decided by Eric on 2026-10-18: it is the analysis that says which automations or scripts changed); (4) the analysis reads the bak COPIES, no longer H:; (5) extraction of each unit into `ReBuild\_tmp_trigul_profond\`; (6) final check: prod MD5 read again after the analysis, ATTENTION in the report if prod moved during the analysis; (7) comparison with the local YAML and writing of `historique\03_RAPPORTS\06_MD5\01_TRIGUL_PROFOND\trigul_profond_[YYYY-MM-DD].txt` (`.bak_date_heure` backup if the report of the day exists); (8) deletion of the temporary folder. The launcher checks that the report contains the `ETAPES :` line and the AUTOMATIONS and SCRIPTS lines, and reports any ATTENTION. Prod is always more important than local: a prod ahead of local (DIFFERENT units) is to be reported first.
2. HA categories: read `ha_config_get_category` (automation and script scopes), write `historique\03_RAPPORTS\06_MD5\02_CATEGORIES_HA\categories_ha_[YYYY-MM-DD].txt` (lines `scope | category_id | nom | icone`, sorted, header `CATEGORIES HA - date heure (lues via ha_config_get_category)`), compare with the data lines of the previous version in the same folder and report additions, deletions, renames. Survey of 2026-10-18: 15 automation categories, 0 for scripts, unchanged.
3. Account: summary of the deep report, DIFFERENT and ABSENT_LOCAL (on 2026-10-18: 62/62 automations identical, 9/9 scripts identical, three local exports without an automation in prod: `Automations_yaml_original\Automations.yaml`, `P1_SDB\h_soufflant_SDB_routage.yaml`, `P1_SDB\i_soufflant_SDB_bouton_rodret.yaml`), category gaps. Correct nothing without a request.

### C. Files kept in several locations (script 3, decided on 2026-10-18)

Run: `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py"`. Read-only. Map: `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md`.

- Tracked files: all of `docs\01_docs_config_system\01_config_system_SH_PY_YAML\` (except `.bak`, except `notifs`, `themes`, `blueprints`, except `secrets.yaml`, `scenes.yaml`, `ip_bans.yaml`) and, in `01_config_system_MD`, `GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` and `README\README.md`.
- 5 columns: L (local), PR (prod root /config), PM (prod docs mirror), GR (GitHub root), GD (GitHub docs/). Scripts: sub-folders `01_scripts.sh` / `02_scripts.py` in local, flat in `/config/.scripts/`.
- Verdicts: SYNC, PROD DIFFERENTE DU LOCAL, GITHUB EN ATTENTE DU BACKUP (normal right after a push), ABSENT (missing locations); section 2: PROD RACINE SEULE, PROD MIROIR SEUL, GITHUB RACINE SEUL, GITHUB DOCS SEUL; section 3 ECARTS ATTENDUS: editor lock files `#...#` in prod only (not counted in the anomalies).
- Report: `historique\03_RAPPORTS\06_MD5\03_VERIF_EMPLACEMENTS\verif_emplacements_[YYYY-MM-DD].txt`, last lines `ANOMALIES` and `RESULTAT`.
- Survey of 2026-10-18 17:41 (commit f45a765c): 97 tracked files, 94 SYNC, 2 waiting for the GitHub backup, 1 prod different (`check_yaml_forme.py`), 1 editor lock in prod (since then an expected gap, section 3 of the report). Landmark only: read the report of the day.

### C2. Analyze the gaps of step C (taken from the old ha-resync-docs skill, removed on 2026-10-20 as a duplicate of the trigul)

LOCAL is the truth, prod must never be ahead of local, GitHub is only a reflection of prod through the HA backup. Never copy GitHub to local without Eric's explicit order, file by file. The `themes/`, `blueprints/` and `notifs/` folders stay prod only.

| Case | Action |
|:----|:-------|
| PROD DIFFERENTE DU LOCAL | Local is the truth: propose `/ha-push-yaml`. If prod was modified by hand (unexplained gap), report it to Eric before any push. |
| GITHUB EN ATTENTE DU BACKUP | Normal after a push: the HA backup launched by Eric will update GitHub. |
| Present in prod or on GitHub, absent from local | Report it to Eric (file created by hand in prod?). Copy to local only on his order. |
| Absent from prod | Propose `/ha-push-yaml`. |

Copy to local (only on Eric's explicit order): file by file, from prod `H:\` (not from GitHub, which may be behind), after a `.bak_AAAA_MM_JJ_HHhMMmSSs` backup of the local file if it exists. Report each copy and write it to the modifications journal. Propose /sync_index if key entities changed.

Rules: `secrets.yaml` is NEVER copied, in either direction. The `.md` files are NEVER synchronized by this skill (local source of truth, managed by /ha-push-docs).

## Reference state of 2026-10-18 (08h02, GitHub at commit b6eddd9 of the 01h30 backup)

Overlay: 567 paths, 402 SYNC, 160 to handle for 214 diff in total, 5 expected gaps, script check OK. `RESULTAT AUDIT : 530 fichiers (184 .md - 338 .yaml - 8 .sh) - SYNC 398 - DIFF 2 - ABSENT LOCAL 88 - ABSENT 2 NIVEAUX 42`. The 2 DIFF: Ha_git_backup.sh and the trigul script (local different from prod and GitHub). The 160 anomalies: 52 local only, 88 prod + GitHub without a local path (old names, including 14 orphan .md with no local equivalent by content or name, and files of `_old_avant_staging`), 3 editor lock files (2 in prod, 1 in local), 16 .svg of the weather icons waiting for the HA backup (after the backup, rerun the script: they must go SYNC), 2 local ahead. Deep: 62/62 automations, 9/9 scripts identical. These figures are landmarks, not values to copy: read the report of the day.

Second survey of 2026-10-18 (rerun of script 1 at 10h26, GitHub at commit c723097): 477 paths, 472 SYNC, 2 to handle (the two trigul scripts, LOCAL ahead), 3 expected gaps. `RESULTAT AUDIT : 468 fichiers - SYNC 466 - DIFF 2`. The 2 DIFF are the two trigul scripts modified in local and not yet pushed to prod (waiting for an order from Eric). Landmark too: read the report of the day.

## Account to the user

- Put at the top the ECHEC and ATTENTION lines of today's trace journal, if any.
- Give the `ANOMALIES`, `RESULTAT AUDIT` and `RESULTAT` lines of script 1, the summary of the deep step and the `ANOMALIES` and `RESULTAT` lines of script 3, as they are.
- List the gaps other than expected gaps: file, origin or level that is behind. For section 1, give the number per origin then the useful examples; the full detail is in the report. If there is no anomaly, say so (`ANOMALIES : aucune`).
- Once the results are given, Eric looks for the missing or different files: propose a read-only investigation on the groups (identical fingerprint under another name, old names, orphans) before any action.
- Give the paths of the reports, in their numbered folders of `historique\03_RAPPORTS\06_MD5\` (`00_VERIF_FINAL_TRIGUL_ARBRES`, `01_TRIGUL_PROFOND`, `02_CATEGORIES_HA`, `03_VERIF_EMPLACEMENTS`, `04_JOURNAL_TRIGUL`).
- Push, rename or delete nothing without a request, case by case. For a prod that is behind, propose ha-push-md, ha-push-docs or ha-push-yaml. For GitHub: never a direct push, the repository is fed by the HA backup launched by Eric.
- Add a line to the modifications journal of the day for the reports written (journal-modifs skill; one LOT line is enough).
- Answer in French, concise, without emojis or tables.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_trigul/ha_trigul.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-trigul/SKILL.md` must stay identical to this copy.
