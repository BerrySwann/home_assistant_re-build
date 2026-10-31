# Reference /histo - Steps 2 and 3: sync_index and merged journal

> Reference file of the histo skill, read when steps 2 and 3 are executed. Paths, file names and badge values stay in French on purpose (they are real names on disk).

## STEP 2 - SYNC_INDEX (chained automatically, do not ask)

Right after saving the journal, run the complete sync_index.

### Scope

| Type of modified file | Index to update |
|:---|:---|
| Config YAML (sensors, templates, utility_meter...) | `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` + `GLOBAL_INDEX_REPO.md` |
| Automation | `docs/03_docs_automations/03_docs_automations_MD/{name}.md` + `GLOBAL_INDEX_REPO.md` |
| Script | `docs/04_docs_scripts/04_docs_scripts_YAML_MD/{name}.md` + `GLOBAL_INDEX_REPO.md` |
| Any type that impacts a tile | `DEPENDANCES_GLOBALES_CLAUDE_memoire.md` |
| File added, renamed or deleted (helper, export, sheet) | `GLOBAL_INDEX_REPO.md` |
| Project skill modified (`.claude/skills/<skill>/SKILL.md`) | copy `docs/05_docs_skills/05_docs_skills_PURE/skill_<name>/<name>.md` and its French sheet `docs/05_docs_skills/05_docs_skills_MD/skill_<name>/<name>.md` |

**Windows paths:**
- `C:\Users\Berry Swann\Documents\ReBuild\docs\00_IA\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\03_docs_automations_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_YAML_MD\`
- `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md`

**Bash sandbox path:** detect it with `ls /sessions/` if needed (the session prefix varies).

### Protocol

1. Identify the files modified during the session (from the session journal that was just generated).
2. For each file that impacts DEPENDANCES_GLOBALES_CLAUDE_memoire.md: update the date at the top of the file. It goes to prod with the general push of step 5C (decided by Eric on 2026-10-30: all of `docs` except `XX_` and `.bak` goes to prod; this replaces the 2026-10-25 rule that kept it local only; since 2026-10-29 it lives in docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\). `.bak` files stay local.
3. For each validated automation: check/update its `.md` in `03_docs_automations_MD/`.
4. For each validated script: check/update its `.md` in `04_docs_scripts_YAML_MD/`.
5. Update `GLOBAL_INDEX_REPO.md` (see below).
6. If a doc `.md` is missing: report it (do not block).
7. For each project skill modified during the session (rule of 2026-10-31: skills are stored in English in `05_docs_skills_PURE`, with a French sheet in `05_docs_skills_MD`): first copy the existing file `docs/05_docs_skills/05_docs_skills_PURE/skill_<name>/<name>.md` to `docs/05_docs_skills/05_docs_skills_PURE/skill_<name>/<name>.bak_AAAA_MM_JJ_HHhMMmSSs.md` (backup before overwriting, up to 10 per day; the evening cleanup (step 5, point 8) files the day as `<name>.bak_AAAA_MM_JJ.md`, 3 at most), then copy the modified `SKILL.md` to `docs/05_docs_skills/05_docs_skills_PURE/skill_<name>/<name>.md`. Then re-read the French sheet `docs/05_docs_skills/05_docs_skills_MD/skill_<name>/<name>.md` and update it if the skill changed in substance (backup `.bak_AAAA_MM_JJ_HHhMMmSSs.md` first, only the lines concerned, the 8 badges stay, MaJ = today). No copy in `.claude/ARCHIVE`. Both copies go to prod with the general push of step 5C (decided by Eric on 2026-10-30, it replaces the 2026-10-11 decision).
8. Regenerate GLOBAL_INDEX_AUTOMATIONS.md (decided 2026-10-13): run `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\gen_global_index_automations\gen_global_index_automations.py"`. The script reads H:\automations.yaml and the HA registry (read only), cross-checks with 03_docs_automations_YAML and 03_docs_automations_MD, and writes `docs\03_docs_automations\GLOBAL_INDEX_AUTOMATIONS.md` (automatic `.bak_AAAA_MM_JJ_HHhMMmSSs.md` backup if the content changes; nothing written if identical; since 2026-10-31 it also writes the 8-badge banner, like the other index and MOC generators). Never edit this file by hand. CHECK the script output: the line liens=N casses=M must have casses=0 (otherwise report each LIEN_CASSE at the top of the final report); put the script's summary lines and each cited gap in the final report (sans_yaml, sans_fiche, sans_entity, id_different, erreurs_yaml). A gap that is new compared with the previous session must be reported to Eric, not fixed without a request. If H: is unreachable (return code 2): note it without blocking. The push to prod is done in step 5C.
9. Regenerate GLOBAL_INDEX_VIGNETTES_PAGES.md (decided 2026-10-13), same principle as point 8: `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\gen_global_index_vignettes_pages\gen_global_index_vignettes_pages.py"`. The script reads the local tree docs\02_docs_dashboard (02_dashboard_docs_MD and 02_dashboard_docs_YAML, backups excluded, Dashboard_COMPLET never read) and writes `docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md` (automatic `.bak_...md` backup if the content changes). Never edit this file by hand. CHECK the script output: the line liens=N casses=M must have casses=0 (otherwise report each LIEN_CASSE at the top of the final report); put the script's summary lines in the final report (tiles without sheet or without YAML, folders on one side only, sans_dependances). The push to prod is done in step 5C.
10. Regenerate GLOBAL_INDEX_SCRIPTS_SH.md and GLOBAL_INDEX_SCRIPTS_YAML.md (decided 2026-10-13), same principle: `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\gen_global_index_scripts\gen_global_index_scripts.py"`. The script reads the local tree docs\04_docs_scripts and the prod in read only (H:\scripts.yaml, H:\automations.yaml, H:\shell_command, H:\.scripts, HA registry) and writes the two files at the root of docs\04_docs_scripts (automatic `.bak_...md` backup if the content changes). Each file explains the difference between SH scripts (bash/python programs) and YAML scripts (Home Assistant scripts). CHECK the output: both `liens=N casses=M` lines must have casses=0; report in the final report the SH and YAML summary lines and each gap (script without sheet, copy of H:\.scripts DIFFERENT from local, YAML script different from prod or without local YAML, .py files stored in 04_docs_scripts_YAML). If H: is unreachable (return code 2): note it without blocking. Never push a script from H:\.scripts without Eric's order. Never edit these files by hand.
11. Regenerate IA_GLOBAL_INDEX_memoire.md (decided 2026-10-13): `$env:PYTHONIOENCODING='utf-8'; python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\gen_global_index_ia\gen_global_index_ia.py"`. The script lists all files of docs\00_IA (00_IA_CONTEXT_BASE and 00_IA_SOUS_CONTEXT_IA) with who uses them, their purpose, when to read them, their prod MD5 and a link, and summarizes the `.bak` per folder. It writes docs\00_IA\ (automatic `.bak_...md` backup if the content changes). CHECK the output: the line `liens=N casses=M sans_description=K` must have casses=0 and sans_description=0. If a file is new in docs\00_IA (sans_description > 0): read it, add its entry (who, purpose, when) to the DESC dictionary of the script after backing up the script, then run again; never invent a description without having read the file. Never edit IA_GLOBAL_INDEX_memoire.md by hand.
12. Update IA_AUTOMATIONS_NOTIFS.md and IA_INDEX_AUTOMATIONS.md (decided by Eric on 2026-10-30), without asking: the local `.bak` and the Windows recycle bin are the safety net. Do it after point 8. First read the prod figures live: number of automations (`H:\automations.yaml`) and scripts (`H:\scripts.yaml`), including those with a notify action, and take the figures from the summary of the point 8 script (local YAML, sheets, attached sheets, split by pole). Files: `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_AUTOMATIONS_NOTIFS\IA_AUTOMATIONS_NOTIFS.md` (date at the top and prod reading line: N automations of which N with notify, N scripts of which N with notify) and `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_INDEX_AUTOMATIONS\IA_INDEX_AUTOMATIONS.md` (date, count line, split by pole, anomaly line about automations without an attached sheet). If a date or a figure differs: local backup `.bak_AAAA_MM_JJ_HHhMMmSSs.md` next to the file, then a strict `.Replace()` on the lines concerned only (UTF-8, same line ending), without touching the narrative sections or the dated reading titles (e.g. "RELEVE PROD 2026-10-13") unless Eric asks. A value that could not be read stays unchanged and is reported, never guessed. Nothing to change: note it in the report. Modification journal: one line per modified file. The push to prod is done in step 5C.

### Updating GLOBAL_INDEX_REPO.md

File: `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` (local working copy, moved by Eric on 2026-10-18 from `docs\99_docs_MD_system\GLOBAL_INDEX_REPO\`; its links are relative to the repository root: it is not clickable here; pushed to prod at every /histo to both places (mirror H:\docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\ and root H:\GLOBAL_INDEX_REPO.md, read on GitHub), see point 8 below; GitHub is fed by the HA backup from H:, never by direct push).

1. If no file of the session was added, renamed, deleted or moved, and no cited entity changed: note "GLOBAL_INDEX_REPO deja a jour" and go to point 8 (the push still compares the MD5).
2. Otherwise, first make a backup in the same folder: `GLOBAL_INDEX_REPO.bak_AAAA_MM_JJ_HHhMMmSSs.md` (PowerShell format `Get-Date -Format "yyyy_MM_dd_HH'h'mm'm'ss's'"`; the INDEX_GLOBAL folder is within the scope of the step 5 cleanup).
3. Rewrite only the lines concerned, never the whole file:
   - add an entry for each new file (automation, script, YAML helper, sheet), in the section of its type, next to the neighbouring entries, with the same format as them
   - update renamed or deleted entries
   - update the section counters concerned (for example the number of automations or script files) by recounting them, not by deducing them from the old number
   - update the date header line
4. Keep the existing format of the file: UTF-8 without BOM, LF line endings (checked on 2026-10-11: the file is LF, do not convert it to CRLF). Check the format before writing.
5. Checks after writing: the file reads back in UTF-8, the modified counters match the number of entries, the added links point to files that exist with the exact case (GitHub is case sensitive; resync of the 315 links on 2026-10-18). Added entities must have been checked live or read from a file of the session, never copied from memory.
6. Gaps that already existed before the session (cited entities that no longer answer, counter imbalances) are not fixed here: mention them in the report if they concern the session.
7. Note for ha-trigul: since the /histo push (decided by Eric on 2026-10-14), `GLOBAL_INDEX_REPO.md` is present in prod under docs/01_docs_config_system/01_config_system_MD/GLOBAL_INDEX_REPO/ (mirror); it stays ABSENT from the repository until the HA backup takes it; its copy at the root of H: (GLOBAL_INDEX_REPO.md) is not compared by the trigul script; it is compared by Verif_emplacements.py (point 9 of step 6).
8. Push to prod (decided by Eric on 2026-10-14, it replaces the old rule "no automatic push": Eric had mistaken this file for another one): after the checks of point 5, whether the file was modified or not, compare the MD5 of the working copy with each of the TWO destinations, like step 5B of ha-push-docs: `H:\docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md` (mirror) and `H:\GLOBAL_INDEX_REPO.md` (root). Copy only those that differ, without a backup on H: (`.bak` files stay local), then check the MD5: source = mirror = root. Never only one of the two. Do not push if the checks of point 5 failed. If H: is unreachable: note it without blocking. GitHub: never a direct push (the repository is fed by the HA backup from H:).

### sync_index rules

- Rewrite only the lines concerned - not the whole file (saves tokens).
- If no dependency is impacted: note "Index deja a jour" in the final report.
- Bash sandbox path: always check with `ls /sessions/` if the prefix is uncertain.

---

## STEP 3 - MERGED JOURNAL (chained automatically, do not ask)

The merged journal is a single Markdown file that gathers all session journals since 2026-07-15. It is read first when resuming the project: what was DONE at the top (by date), what REMAINS TO DO at the bottom (by date).

**Folder:** `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\FUSIONNE\`
**Name:** `JOURNAL_FUSIONNE_2026-07-15_[DATE_FIN].md`, where `[DATE_FIN]` = date of the last session included (format YYYY-MM-DD).

### Protocol

1. Find the most recent merged journal: `JOURNAL_FUSIONNE_*.md` (without `.bak` suffix), sorted by end date in the name. It is the base.
2. Find the `histo_*.md` journals and old `histo_*.txt` not yet integrated (folder `historique\02_HISTO_ET_FUSIONNE\`; since 2026-10-21 the old ones are in HTML and in the recycle bin, only the journals of the current session remain; when in doubt read the HTML page of the day): compare the dates and suffixes with the `SESSION 2026-...` lines of the merged journal. Include the one that was just written in step 1. Do not rely on the modification date of the files alone.
3. Read each missing journal in full before integrating it. Add nothing that is not in these journals (no deduced figure, state or decision). A journal in formatted Markdown (`##` titles, bold, icons) is integrated into the merged journal in ASCII: remove the icons and dots, keep the substance (the bold of the merged journal comes from the block format below).
4. Build the new file from the base, without touching the existing content:
   - header line 2: replace the end date in `Periode : 2026-07-15 -> [DATE_FIN]` (the base uses an arrow, change only the date)
   - part `PAR DATE - CE QUI A ETE FAIT`: add one block per session, in chronological order, just before the title line `## **PAR DATE - CE QUI RESTE A FAIRE**` (the banner is a Markdown title, outside a code block). Session blocks are real Markdown, outside a code block, so that the bold is displayed. Block format (useful sections only):

         ### **SESSION [date] ([Sn]) - [duration] - [short title]**

         **[FICHIERS VALIDES]**
         - ...

         **[ERREURS RESOLUES]**
         - ...

         **[DECISIONS]** / **[CONSTATS]**
         - ...

     Whole session title in bold, dates in bold, brackets in bold; no icon or emoji in the merged journal; ASCII except the `**` of the bold. Paths in inline code. Empty session: a single line `**SESSION [date] ([Sn], [heure]) : session vide - aucune modification depuis ...**`. Leave an empty line before and after each block. Old sessions (titles and sections in bold, body in code blocks) are not modified.
   - part `PAR DATE - CE QUI RESTE A FAIRE`: the banner is the title `## **PAR DATE - CE QUI RESTE A FAIRE**`. Add at the END of the file, after the last ``` line, one entry per date in Markdown, the text of each section staying in a code block:

         ### **[date]**

         **[EN COURS]**

         (```text code block, content indented by 4 spaces, then ```)

         **[PROCHAINE ACTION]**

         (```text code block, content indented by 4 spaces, then ```)

         ### **ETAT ACTUEL AU [date] (soir, curated)**

         (```text code block: summary of the current state and of what remains open, then ```)

     When an item of an older entry has been closed since, note it in the new entry (for example `(ferme le 07/10)`), without modifying the old one. The file thus ends with a ``` line closing a code block.
5. Write the new file. The added blocks are in ASCII (no long dash, no arrow, no special characters, no emoji; only the bold `**` is added in the new session blocks); the existing content is kept as is, including its special characters.

### Rules

- Never overwrite an existing merged journal: a new name for each new end date. If the target file already exists (same end date, new session of the same day), first back it up as `JOURNAL_FUSIONNE_..._[DATE_FIN].bak_AAAA_MM_JJ_HHhMMmSSs.md`, then update it.
- The old merged journal stays in place. Do not delete it without a request.
- File format: CRLF, UTF-8 without BOM, like the base.
- Check after writing: no BOM, no isolated LF, a single `RESTE A FAIRE` banner, the file ends with the ``` line followed by a line ending, an even number of ``` lines (balanced fences), line count consistent with base + additions.
- Write with a script (Python or PowerShell), passing the blocks through temporary files in `%TEMP%`: a command that is too long fails (WinError 206). Never rebuild existing content from a truncated display: read the file.
- If the base is missing or unreadable: report it and stop at this step, without recreating the whole merged journal from memory.
