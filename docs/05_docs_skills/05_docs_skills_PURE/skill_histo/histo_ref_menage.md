# Reference /histo - Step 5, 5B, 5C: backup cleanup, Dashboard export, push to prod

> Reference file of the histo skill, read only when step 5 is executed. The backup rules are also in CLAUDE.md (section REGLE DE SAUVEGARDE). Everything happens LOCALLY, never on H: or D:. Paths, file names and badge values stay in French on purpose (they are real names on disk).

## Scope and condition

- `docs\00_*` to `05_*` (recursive) and `Claude md SAVE\`: cleanup of the `.bak` ONLY when the histo is definitive (point 8). Otherwise, no cleanup of these two scopes.
- `historique\03_RAPPORTS\06_MD5\`, `historique\01_JOURNAL_TRACE\` (HTML pages and `.bak`, without `LOGS\`), `historique\02_HISTO_ET_FUSIONNE\` (HTML pages, `FUSIONNE\`, `.bak`), `TODO\` (`TODO.bak_*` only), then the rest of `historique\`: cleanup at every /histo, following the chapters below.
- Out of scope: Github, `historique\01_JOURNAL_TRACE\LOGS\`, `historique\03_RAPPORTS\01_MODIFS_IA\`, Infra_Proxmox, `_old_avant_staging`, the rest of `.claude`, `.claude\ARCHIVE\`, `Dashboard_COMPLET\`, any `_ARCHIVE` / `ARCHIVE` folder, any `*_archive_*` file.
- Trash = Windows recycle bin, never a permanent deletion (only exception: purging the recycle bin items older than 3 months, point 9):
```powershell
Add-Type -AssemblyName Microsoft.VisualBasic
[Microsoft.VisualBasic.FileIO.FileSystem]::DeleteFile($f,'OnlyErrorDialogs','SendToRecycleBin')
```

## Names and Statuts of the backups (docs and Claude md SAVE)

- Timestamped (of the day): `fichier.bak_AAAA_MM_JJ_HHhMMmSSs.ext`, 10 at most per file; the 11th sends the oldest to the recycle bin. Statut `bak_h` (orange).
- Dated (past days): `fichier.bak_AAAA_MM_JJ.ext`, 3 at most per file (3 days back), beyond that the oldest goes to the recycle bin. Statut `bak_d` (orange).
- Before sending a `.md` that carries a badge block to the recycle bin: Statut `Trash` (red f44336), a single line changed, then the file goes. A `.md` without badges goes as it is. Non-`.md` files carry no badge.
- The badges of the `.bak` are set by `python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_badges_fiches\Check_badges_fiches.py" --bak --fix` (only the Statut changes, a value that cannot be found = `Inconnu`). Skill copies in English (`docs\05_docs_skills\05_docs_skills_PURE`): no badge, same naming rule. The French sheets (`docs\05_docs_skills\05_docs_skills_MD`) are normal sheets: 8 badges, Type `Skill`, their `.bak` follow the normal rule.
- Other recognized formats (renamed `{working_name}.bak_AAAA_MM_JJ.{ext}`, date read from the name, otherwise modification date): old `.bak` (`.bak_2026-09-28`, `.bak_20260929`, `.bak2_...`, `.bak-...`); dated versions of a working file (`page_..._2026-06-18.yaml`) only if the undated working file exists in the folder; named backups (`CLAUDE_backup_2026-07-31.md`, `fichier_old.md`). An undated file containing `backup`, `save` or `old`, without a neighbouring working version, is a real file: do not process it. A working file name never carries a date.

## Protocol (docs and Claude md SAVE)

1. Today's date = `Get-Date -Format "yyyy_MM_dd"`. If midnight passes during execution, keep the date of the start.
2. Group by original file (same folder, same base name), then by day.
3. The `.bak` of the day are never touched, except by the definitive cleanup (point 8).
4. Cap: more than 3 `.bak_AAAA_MM_JJ` per file -> the oldest goes to the recycle bin.
   Date of a `.bak_AAAA_MM_JJ`: it keeps the date of the day of the most recent modification of its group (date read from the name of the most recent timestamped backup, otherwise its modification date), never the date of the cleanup (Eric's precision, 2026-10-31).
5. In `historique\` and `TODO\`: no day cap (dedicated chapters).
6. No go to wait for (except the first execution on a folder: dry-run presented, wait for the go). Everything is restorable from the recycle bin.
7. Statuts: see above. A `.md` whose badges are outside a `<div align="center">` block is "forme a revoir": Claude adds a clean banner under the title.
8. DEFINITIVE CLEANUP of `docs\00_*` to `05_*` and `Claude md SAVE\` (Eric's rule of 2026-10-31, 13h06): freezes the day to start clean the next day. CONDITION: the histo is definitive, that is /histo-final asked Eric the question "Histo final definitif ?" and he answered Oui. /histo alone, or answer Non, or no answer: no cleanup of these two scopes, it will be done at the next definitive histo. Procedure: (i) for each file, the most recent timestamped `.bak` of the day is renamed `.bak_AAAA_MM_JJ` (date of the day); if that name already exists, rename nothing and report the group; (ii) the other timestamped files of the day get the Statut `Trash` then go to the recycle bin; (iii) cap of 3 `.bak_AAAA_MM_JJ` per file, the oldest gets `Trash` then goes to the recycle bin; (iv) any timestamped file of a past day still present (missed cleanup): the most recent of each day becomes `.bak_AAAA_MM_JJ`, the others go to the recycle bin; (v) then run `Check_badges_fiches.py --bak --fix` to put `bak_h` / `bak_d` back; (vi) write the plan in `historique\03_RAPPORTS\02_MENAGE_BAK\menage_dry_run_AAAA-MM-JJ.txt` and cite it in the report. The next day no timestamped `.bak` remains.
9. Windows recycle bin (decided by Eric on 2026-10-31): the cleanup does not empty it. Once per definitive cleanup, after the sending of point 8, delete from the recycle bin the items whose deletion date is older than 3 months (`Shell.Application`, namespace 10, deletion date of each item). Write the list (original path, date) in the plan before deleting. Unreadable date: delete nothing, report it. First implementation on 2026-10-31: method to verify (no item is older than 3 months yet). CORBEILLE line of the report.

### Special case: historique\03_RAPPORTS\06_MD5\ (decided by Eric on 2026-10-18, "Hermes included")

Folder: `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\06_MD5\` (trigul reports, audits, reports and backups produced by Hermes in this folder; numbered sub-folders `00_VERIF_FINAL_TRIGUL_ARBRES`, `01_TRIGUL_PROFOND`, `02_CATEGORIES_HA`, `03_VERIF_EMPLACEMENTS`, `04_JOURNAL_TRIGUL`, `05_VERIF_INTEGRATIONS_FILE` added on 2026-10-23 for the File integrations check). Eric moved this folder from `historique\MD5\` to `historique\03_RAPPORTS\06_MD5\` on 2026-10-21; the trigul scripts (trigul_run, hermes_audit_trigul_arbres, Hermes_audit_md5_trigul_unitaire) and Verif_emplacements.py write to the new location since 2026-10-23 (TODO item R104.2). A `historique\MD5\` folder that reappears is a gap to report to Eric. The histos follow the same cleanup rule as docs, with these precisions:

- **Group = one report**, identified by its full name, date included (e.g. `trigul_arbres_2026-10-18.txt`). The date in a report name is part of its working name: families D and E do NOT apply to a report (a dated report is never treated as a dated version of another file). The reports themselves and the `_latest` copies are never renamed, never sent to the recycle bin, never modified by the cleanup.
- **Backups of the day** (date read from the backup name): 10 at most per report, in the format `rapport.bak_AAAA_MM_JJ_HHhMMmSSs.ext`. Beyond 10, the oldest go to the Windows recycle bin.
- **Past days**: per report and per day, keep the most recent backup (timestamp of the name, otherwise modification date), renamed `rapport.bak_AAAA_MM_JJ.ext`; the others of that day go to the Windows recycle bin. No day cap (Eric's decision of 2026-10-21): one backup per day indefinitely.
- **Backup without extension** (e.g. `rapport.bak_2026_10_17`): it takes the extension of the report (`.txt`, `.html`...). Collision with an existing name: rename nothing, report it.
- **Old name `bak_HHhMM_libelle`** (no backup date in the name): the date taken is the one in the report name; the case is reported in the cleanup report as "date deduite du nom du rapport".
- Safeguards of the common chapter (collision, unreadable date, doubtful name, recycle bin error): delete nothing, report.
- First execution done on 2026-10-18: plan `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_dryrun_2026-10-18.txt`, execution `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_2026-10-18.txt` (Eric's go obtained after the dry-run). The following executions no longer wait for a go: write the plan in `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_dryrun_AAAA-MM-JJ.txt`, cite it in the final report, execute, write the account in `historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_AAAA-MM-JJ.txt` (original path of each item sent to the recycle bin, restorable from the Windows recycle bin).
- The cleanup of this folder is done before the tree (step 6), like the rest of step 5. Modification journal: one LOT line with the path of the report (skill journal-modifs).

### Special case: historique\01_JOURNAL_TRACE\ (decided by Eric on 2026-10-21)

Folder: `C:\Users\Berry Swann\Documents\ReBuild\historique\01_JOURNAL_TRACE\` (formerly `journal_trace`, renamed by Eric to be at the top of `historique\`). It directly contains the HTML pages written by `histo_trace.py html` (`histo_trace_AAAA-MM-JJ.html`, one per day, and `index.html`), their backups, and the sub-folder `LOGS\` (raw `.log` journals) which is OUT of scope: the cleanup never touches it.

- **Group = one daily page**, identified by its full dated name. The pages `histo_trace_AAAA-MM-JJ.html` and `index.html` are never renamed, never sent to the recycle bin, never modified by the cleanup. One page per day, kept with no day limit (Eric's decision: like the TODO, one file per day indefinitely). The date in the name of a page is part of its working name: families D and E do not apply.
- **Backups of the day** (date read from the backup name): `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html`, 10 at most per page and per day (created by `histo_trace.py html` when a page of the day is regenerated with different content). Beyond 10, the oldest go to the Windows recycle bin.
- **Past days**: per page and per backup day, keep the most recent one renamed `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ.html`; the others of that day go to the Windows recycle bin. No day cap (one backup per day indefinitely, like the TODO).
- Safeguards of the common chapter (collision, unreadable date, doubtful name, recycle bin error): delete nothing, report.
- No go to wait for on this folder, even at the first execution (a pause would block /histo-final before the PC shutdown; everything goes to the Windows recycle bin, restorable): write the plan in the cleanup plan file, execute, cite the account in the final report.
- The cleanup of this folder is done with step 5, before the tree. Modification journal: one line per file, or one LOT line with the path of the report beyond 10 (skill journal-modifs).

### Special case: TODO\ (decided by Eric on 2026-10-24)

Folder: `C:\Users\Berry Swann\Documents\ReBuild\TODO\`. It contains `TODO.html` (the todo: source and view since 2026-10-24) and its backups `TODO.bak_AAAA_MM_JJ_HHhMMmSSs.html`, created at every modification of the todo (TODO rule of CLAUDE.md). The old `TODO.md` and its `.md` backups were sent to the recycle bin on 2026-10-24 on Eric's order.

- `TODO.html` is never renamed, never sent to the recycle bin, never modified by the cleanup. Families C, D and E do not apply. No more `.md` or `.txt` file in this folder (Eric's order of 2026-10-24): any `TODO.md`, `TODO.bak_*.md` or `.txt` that reappears is reported and sent to the Windows recycle bin.
- **Group = one extension** (`.html`, `.md`, `.txt`): backups of different formats never mix.
- **Backups of the day** (date read from the name): never renamed; 10 at most per group, beyond that the oldest go to the Windows recycle bin.
- **Past days**: per group and per day, keep the most recent (timestamp read from the name) renamed `TODO.bak_AAAA_MM_JJ.{ext}`; the others of that day go to the Windows recycle bin. One backup per day indefinitely, no day cap (Eric's decision). `TODO.bak_AAAA_MM_JJ.{ext}` files already in the right format are not touched.
- Old names (`TODO.txt.bak_...`, `TODO.md.bak_...`): family C, renamed `TODO.bak_AAAA_MM_JJ.{ext}` if there is no collision.
- Safeguards of the common chapter (collision, unreadable date, doubtful name, recycle bin error): delete nothing, report.
- No go to wait for on this folder, even at the first execution (everything goes to the Windows recycle bin, restorable): write the plan in the cleanup plan file, execute, cite the account in the final report.
- Modification journal: one line per file, or one LOT line with the path of the report beyond 10 (skill journal-modifs). The cleanup of this folder is done with step 5, before the tree.

### Special case: historique\02_HISTO_ET_FUSIONNE\ (decided by Eric on 2026-10-21)

Folder: `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\`: one page `histo_AAAA-MM-JJ.html` per day (all sessions of the day), its `index.html`, and the sub-folder `FUSIONNE\` (one page `JOURNAL_FUSIONNE_..._[DATE_FIN].html` per merged journal, its `index.html`, the `.md` of the most recent merged journal and the old backups). The pages are written by `histo_html.py` (step 4B). Same rules as `01_JOURNAL_TRACE`:

- **Group = one page**, identified by its full dated name. Day pages, merged-journal pages and `index.html` are never renamed, never sent to the recycle bin, never modified by the cleanup. One page per day, kept with no day limit (Eric's decision: like the TODO, one per day indefinitely). Families D and E do not apply.
- **Backups of the day**: `histo_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html` and `JOURNAL_FUSIONNE_..._[DATE_FIN].bak_AAAA_MM_JJ_HHhMMmSSs.html` (created by `histo_html.py` when a page is regenerated with different content), 10 at most per page and per day; beyond that, the oldest go to the Windows recycle bin.
- **Past days**: per page and per backup day, keep the most recent one renamed `<name>.bak_AAAA_MM_JJ.html`; the others of that day go to the recycle bin. No day cap.
- **Old `.md` backups** (`histo_*.bak_*.md`, `JOURNAL_FUSIONNE_*.md.bak_*` and variants without final `.md`): families A, B and C of the common chapter, but WITHOUT the 3-day cap (one per day indefinitely, the most recent, like the pages).
- Journal `.md` files that are not `.bak` are not processed by the cleanup: they go to the recycle bin in step 4B.
- Safeguards of the common chapter (collision, unreadable date, doubtful name, recycle bin error): delete nothing, report. A page in COLLISION is never touched.
- No go to wait for, even at the first execution (everything goes to the Windows recycle bin, restorable). The cleanup of this folder is done with step 5, before the tree. Modification journal: one line per file, or one LOT line with the path of the report beyond 10.

### Special case: historique\ whole tree (decided by Eric on 2026-10-21)

Scope: all directories and sub-directories of `C:\Users\Berry Swann\Documents\ReBuild\historique\` (root, `03_RAPPORTS\` and all its sub-folders, `save`, old folders `RASPI4`, `FANTOMES...`, `orphelins...`, etc.), EXCEPT `01_JOURNAL_TRACE\LOGS\` (raw `.log` journals) and `03_RAPPORTS\01_MODIFS_IA\` (modification journals, one file per day and per author) which are never touched. The dedicated chapters above (`MD5`, `01_JOURNAL_TRACE`, `02_HISTO_ET_FUSIONNE`) remain valid; this chapter completes them and, in case of conflict on the day cap, prevails. Difference with the "normal" rule (docs): in `historique\` files are kept indefinitely, no day cap. The evening cleanup and the 3-day limit (step 5, point 8) apply only to `docs` and `Claude md SAVE\`, not to `historique\`.

1. **One file per day, no day limit**: one `.bak_AAAA_MM_JJ` backup per file and per day, kept indefinitely (the 3-day cap of step 5 does not apply here).
2. **Timestamped `.bak` (`.bak_AAAA_MM_JJ_HHhMMmSSs`)**: for each file and each day, the most recent (time read from the name) is renamed `.bak_AAAA_MM_JJ` (same extension), the others go to the Windows recycle bin. If the name `.bak_AAAA_MM_JJ` already exists: keep the existing one, send the timestamped ones to the recycle bin and report it. On the same day, timestamped files are kept (10 at most) unless Eric orders otherwise; Eric's order of 2026-10-21: renaming also done for the same day.
3. **Files of the same day with an `_sN` suffix** (`menage_dry_run_2026-10-18_s2.txt`, etc.): merged into a single file of the day (`menage_dry_run_2026-10-18.txt`), sources in the order of their modification time, each preceded by the line `=== SOURCE : nom (modifie AAAA-MM-JJ HH:MM) ===`, in UTF-8 without BOM. Check that the size of the merged file covers the sum of the sources BEFORE sending the sources to the recycle bin. A lone `_sN` file that day (no base) is renamed without the suffix only if its name does not change family; `.json` files and names of a different family are not merged.
4. **`.txt` with an `.html` twin**: a `.txt` whose `.html` of the same name exists in the same folder (non-zero size) goes to the Windows recycle bin (case of the `trigul_arbres_*` reports), including its `.bak`.
5. **Exact duplicates** (same MD5): reported to Eric, never deleted without an order.
6. Safeguards of the common chapter (collision, unreadable date, doubtful name, recycle bin error): delete nothing, report. Everything goes to the Windows recycle bin (restorable: once restored, `Shell.Application` namespace 10, move the `$R` file to the target name); no go to wait for.
7. Plan and account in `historique\03_RAPPORTS\02_MENAGE_BAK\menage_historique_AAAA-MM-JJ.txt` (original path of each item sent to the recycle bin, list of renamings and merges), cited in the final report. Modification journal: one LOT line with this path beyond 10 files.

### Safeguards (delete nothing, raise the issue)

- Collision: the target name already exists (e.g. a `.bak_2026_10_07` is already present for this file) -> do not rename, do not delete, report the group.
- Unreadable or impossible date (month 13, day 32) -> do not process, report.
- Doubtful name (could be a real file and not a backup) -> do not process, report.
- Family D without an undated working file in the folder -> do not process, report.
- Undated file containing `backup`, `save` or `old`, without a neighbouring working version (e.g. `ha_git_backup.sh`) -> real file, do not process.
- `Dashboard_COMPLET` exports -> never processed.
- Recycle bin error (locked file, access denied) -> do not retry by another method, report.
- Before running the step for the first time on a folder: first produce the list (DRY-RUN: planned renamings and recycle bin sends) and present it, changing nothing, then wait for the user's go (the only stop allowed in /histo). In all other cases, whatever the number of files (Eric's decision of 2026-10-15): no go to wait for; write the list in historique\03_RAPPORTS\02_MENAGE_BAK\menage_dry_run_AAAA-MM-JJ.txt, cite it in the final report, then execute. Re-read the plan before presenting or executing it: no target must be truncated, no Dashboard export or real file must appear in it, and the cap of 3 (folders outside docs) must be computed after the renamings of family D. Then execute without asking again; the tree (step 6) is done after the cleanup is executed, or the report states that its counts are from before the cleanup.

### Report (to put in the final report)

- number of files renamed, sent to the recycle bin, ignored (archives / current day)
- list of reported issues (collision, unreadable date, doubtful name, error) with the full path
- for each recycle bin send: the original path (restorable from the Windows recycle bin)
- for `docs`: evening cleanup done or not (and why), timestamped files renamed `.bak_AAAA_MM_JJ`, `.bak` sent to the recycle bin (Statut `Trash` set before), Windows recycle bin: items older than 3 months deleted
- for `historique\` (whole tree): timestamped .bak renamed, `_sN` merges, `.txt` with `.html` to the recycle bin, recycle bin, reported, with the path of `historique\03_RAPPORTS\02_MENAGE_BAK\menage_historique_AAAA-MM-JJ.txt`
- for `historique\03_RAPPORTS\06_MD5\`: the same counts, separate from those of docs, with the path of the plan and of the account (`historique\03_RAPPORTS\02_MENAGE_BAK\menage_MD5_*.txt`) and the list of "date deduite du nom du rapport" cases
- for `TODO\`: backups renamed, sent to the recycle bin, reported, with the path of the cleanup plan

---
