---
name: "histo"
description: "HA ReBuild skill - writes an ultra-compact session log and saves it, then chains sync_index (DEPENDANCES_GLOBALES_CLAUDE_memoire.md, impacted docs, GLOBAL_INDEX_REPO.md), the merged journal, the Obsidian copy, the .bak cleanup and the tree update (IA_ARBO_DETAIL.md). MUST trigger when the user types /histo, asks for a logbook (journal de bord), generates the histo, asks for a summary to save, creates a session log or exports the history. Typical use: end of session, before closing Cowork."
---

# Skill: /histo - Logbook + sync_index (incl. GLOBAL_INDEX_REPO) + merged journal + Obsidian copy + .bak cleanup + tree

> Language note: this skill is written in English to save tokens. Paths, file names, step labels of the final report, trace step names and badge values stay in French on purpose (they are real names on disk or exact strings other tools grep). Eric talks French: reports and messages to him are in French.

> Files present at several locations (config, GLOBAL_INDEX_REPO, README): see `docs\00_IA\00_IA_SOUS_CONTEXT_IA\IA_CARTE_EMPLACEMENTS\IA_CARTE_EMPLACEMENTS.md` (5 locations: local, prod root, prod docs mirror, GitHub root, GitHub docs/) and the read-only check `docs\04_docs_scripts\04_docs_scripts_SH\Verif_emplacements\Verif_emplacements.py` (decided by Eric on 2026-10-18, step 6 point 9).

> Skill maintenance rule (decided by Eric on 2026-10-31): the usable English copy of this skill lives in `docs\05_docs_skills\05_docs_skills_PURE\skill_histo\` and its French explanation sheet in `docs\05_docs_skills\05_docs_skills_MD\skill_histo\histo.md`. Whenever this skill or one of its reference files changes, re-read the French sheet and update it if needed.

## Goal

Six actions, plus steps 5B and 5C, chained without interruption:
1. Generate and save the session logbook
2. Run sync_index (DEPENDANCES_GLOBALES_CLAUDE_memoire.md, impacted docs, GLOBAL_INDEX_REPO.md, GLOBAL_INDEX_AUTOMATIONS.md, GLOBAL_INDEX_VIGNETTES_PAGES.md, GLOBAL_INDEX_SCRIPTS_SH.md, GLOBAL_INDEX_SCRIPTS_YAML.md, IA_GLOBAL_INDEX_memoire.md)
3. Update the MERGED JOURNAL (historique\02_HISTO_ET_FUSIONNE\FUSIONNE\) with the session just written
4. Copy the session journal and the merged journal into the Obsidian vault
4B. Generate the dark HTML pages of the day journal and of the merged journal (histo_html.py), then send the converted .md/.txt originals to the Windows recycle bin (step 4B)
5. Clean the backups (.bak): `docs` and `Claude md SAVE` only when the histo is definitive (Yes/No question asked by /histo-final), then `historique\03_RAPPORTS\06_MD5\`, the HTML pages of `historique\01_JOURNAL_TRACE\` and `historique\02_HISTO_ET_FUSIONNE\`, `TODO\`, the rest of `historique\`, and the purge of the Windows recycle bin (items older than 3 months). Details: `histo_ref_menage.md`
5B. Check the Dashboard export dropped at the prod root and keep only one export in prod (step 5B)
5C. Push to prod all of `docs` except `XX_` and except `.bak`, with MD5 before and after (step 5C, decided by Eric on 2026-10-30)
6. Update the trees: IA_ARBO_DETAIL.md (local, prod, GitHub counts), with the update-arbo skill (step 6)
6B. Check the 9 files of 00_IA_SOUS_CONTEXT_IA (read-only, gap report, step 6 point 7)
6C. Check all global indexes (read-only, gap report, step 6 point 8)
6D. Check files at several locations (read-only, gap report, step 6 point 9)
6E. Check the HA File (notify) integrations against their sheet (read-only, gap report, step 6 point 10)
6F. Check the `.md` sheets (one sheet per source) and the presence of the 8 badges, create the missing badges on the spot (step 6 point 11, added by Eric on 2026-10-28)
6G. Check the freshness of DEPENDANCES_GLOBALES_CLAUDE_memoire.md and IA_GLOBAL_INDEX_memoire.md (read-only, fixes by Claude, step 6 point 12)

Never ask for confirmation between steps. Chain them. Only exception: the cleanup DRY-RUN (step 5) at the first execution on a folder, which stops to present the list and wait for the user's go (see the safeguards of step 5).

## DEFINITIVE HISTO OR NOT (decided by Eric on 2026-10-31)

The `.bak` cleanup of `docs` and `Claude md SAVE` happens only if the histo is definitive.
- /histo alone (mid-day): not definitive, no cleanup of these two scopes.
- /histo-final: ask the question with AskUserQuestion, at the very start: "Histo final definitif ?", two choices: Oui (cleanup done) and Non (trial, no cleanup, it will be done at the next definitive histo). No answer (nobody there): Non.
- Record the choice in the trace: `histo_trace.py note menage "definitif : oui|non"`, and say it in the report.

## REFERENCE FILES (read only when the matching step is executed)

Folder: `C:\Users\Berry Swann\Documents\ReBuild\docs\05_docs_skills\05_docs_skills_PURE\skill_histo\`
- `histo_ref_sync_index.md`: steps 2 (sync_index, generated indexes, GLOBAL_INDEX_REPO) and 3 (merged journal).
- `histo_ref_menage.md`: step 5 (`.bak` cleanup, historique chapters, TODO, MD5), 5B (Dashboard export) and 5C (push of `docs` to prod).
- `histo_ref_controles.md`: step 6 (tree, checks, badges, push catch-up) and the final report format.
If a reference file cannot be found: say it at the top of the report and stop the step concerned, do not redo it from memory.

## STEP 2 - SYNC_INDEX and STEP 3 - MERGED JOURNAL

Chained without asking, after step 1. Read `histo_ref_sync_index.md` and follow all its rules. Trace: `debut sync_index` / `fin sync_index`, `debut fusionne` / `fin fusionne`.

## TRACE JOURNAL (requested by Eric on 2026-10-19, shared by /histo and /histo-final)

To see where the sequence crashes or blocks silently, and to keep the trace of the validations asked of Eric, write one line before and after each step with `histo_trace.py`: `python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\histo_trace\histo_trace.py" <command>`. Raw journal: `historique\01_JOURNAL_TRACE\LOGS\histo_trace_AAAA-MM-JJ.log` (one per day, each line forced to disk; folder renamed `01_JOURNAL_TRACE` by Eric on 2026-10-21 to sit at the top of `historique\`). The `.log` files are outside the .bak cleanup scope. The HTML pages directly in `01_JOURNAL_TRACE\` have their own cleanup rule (chapter "Cas particulier : historique\01_JOURNAL_TRACE\" of `histo_ref_menage.md`).

- Commands: `seq-debut histo|histo-final`, `debut STEP [text]`, `fin STEP OK|ATTENTION|ECHEC [text]`, `validation STEP text`, `note STEP text`, `seq-fin`, `verifier`, `recap`, `html`.
- Called alone (/histo): write `seq-debut histo` at the start and `seq-fin` after the final report. Called by /histo-final: do not write `seq-debut` nor `seq-fin` (/histo-final opens and closes the sequence), only the `debut` / `fin` of the steps.
- Step names: journal (step 1), sync_index (2), fusionne (3), obsidian (4), pages_html (4B), menage (5), export_5B (5B), push_docs (5C), tree (6 points 1 to 6), controles_6B (point 7), controles_6C (point 8), controles_6D (point 9), controles_6E (point 10), controles_6F (point 11), controles_6G (point 12), tokens (counting notes, see below), rapport.
- At the end (after the report): run `histo_trace.py verifier` and put its output in the final report (line TRACE). Called alone (/histo): also run `histo_trace.py recap` after `seq-fin` (read-only); its output timestamps each task: start time of task 1, then for each following task the duration of the previous task and its start time (requested by Eric on 2026-10-21); put it in the final report (line HORODATAGE). Called by /histo-final: do not run it, /histo-final runs it. Called alone (/histo): then run `histo_trace.py html` (requested by Eric on 2026-10-21): it writes the day HTML page `historique\01_JOURNAL_TRACE\histo_trace_AAAA-MM-JJ.html` (all sequences of the day, duration of each task, result of the FIN line, notes) and rebuilds `index.html`; if the day page exists with different content, it first copies it to `histo_trace_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html`; identical page: nothing is written. Put its output in the final report (line PAGE). Called by /histo-final: do not run it, /histo-final runs it.
- A `debut` line without `fin` reveals a silent block (a call that never returned, for example a validation left unanswered). A sequence without `seq-fin` reveals an interruption (PC off, session closed, crash).
- Limit: Claude cannot see Eric's screen. It knows a validation was requested only if the tool result says so (refusal, wait, approval message); otherwise the trace only shows a long or unfinished step. Never invent a `validation` line.
- No secret in journal messages. If the trace script is missing or fails: say so in the report and continue (the trace never blocks the sequence).

### Token counting (requested by Eric on 2026-10-28, shared by /histo and /histo-final)

Claude has no token invoice. The only measure available is the session counter of remaining tokens (value `total_tokens left` visible after tool calls). Method:

1. At the very start of the sequence (before the first step): read the counter and write it in the trace: `histo_trace.py note tokens "debut : N restants"`. When called by /histo-final, /histo-final takes this reading before step 1: do not redo it.
2. At the end of the sequence (just before the final report): read the value, write `histo_trace.py note tokens "fin : M restants"`.
3. In the final report, line TOKENS: consumed = N - M, with the word "deduit" and the mention "compteur de session, pas une facture". If one of the two readings is missing: write "inconnu", never an approximate value. The consumption of writing the final report itself is not counted (reading taken before).
4. If the counter is not visible in the session: write "inconnu (compteur non visible)".

---

## STEP 1 - LOGBOOK

### Collect from the conversation history

- Today's date (from env or bash)
- Session number of the day (S1, S2, S3... according to the `histo_*.md`/`.txt` journals present in `historique\02_HISTO_ET_FUSIONNE\` AND the number of sessions already in the day page `histo_AAAA-MM-JJ.html`: one `<section>` tag per session; the old originals are in the recycle bin after conversion)
- YAML files modified/created/validated (short path under `docs/`)
- Entities created or fixed (unique_id or alias)
- Errors met and their resolution
- Task in progress or finished
- TODO.html backlog if mentioned in the session
- Priority next action

### Mandatory output format (formatted Markdown, since 2026-10-08)

The journal is real Markdown (titles, bold, color dots, icons), not a code block. The journal itself stays in French. Template (the icons are the one emoji exception granted by Eric on 2026-10-08, limited to new histo journals):

```
# 📓 Journal HA ReBuild - **[DATE]** (Session **S[N]**)

- ⏱️ **Session** : [estimated duration or "N/A"]
- 🌿 **Branche active** : `docs/`

## ✅ Fichiers valides
- 🟢 `short/path/file.yaml` - [entity(ies) concerned] **[v]**
- ...

## 🟠 En cours
- 🟠 `file or task` - **[draft]** or **[a tester]** or **[a deployer]**
- (none if the session ended cleanly)

## 🔴 Erreurs resolues
- 🔴 `file` : [error type] -> [fix applied] **[resolu]**
- (none if the session was clean)

## 📋 Taches backlog (TODO.html)
- 📌 [items identified in the session, if applicable]

## 🎯 Prochaine action
- [priority action identified]

*Fin du journal*
```

Formatting rules:
- Every date is in bold (`**2026-10-08**`), in the title as in the text.
- Every comment or state in square brackets is in bold: `**[v]**`, `**[a tester]**`, `**[draft]**`, `**[a deployer]**`, `**[resolu]**`, `**[EN COURS]**`.
- Color dots: 🟢 valid or finished, 🟠 in progress or to test, 🔴 error, 🔵 information. One icon per section title as in the template.
- Paths, entity IDs and commands in inline code (backticks).
- This formatting applies only to NEW `histo_*.md` journals. Old journals, GLOBAL_INDEX_REPO.md and the other files stay unchanged and without emoji. The new session blocks of the merged journal have bold only, no emoji (step 3).

### Mandatory save

- Determine the session number: list `historique\02_HISTO_ET_FUSIONNE\` (`.md` files AND old `.txt`) AND count the sessions of the day HTML page (`<section>`), then pick the next suffix (the larger of the two + 1) (e.g. if `histo_2026-08-08_s2.txt` or `histo_2026-08-08_s2.md` exists -> create `histo_2026-08-08_s3.md`)
- Save to `C:\Users\Berry Swann\Documents\ReBuild\historique\02_HISTO_ET_FUSIONNE\histo_[YYYY-MM-DD]_s[N].md`: the journal is written in formatted Markdown as defined above, not placed in a code block (otherwise bold and icons do not render). Old journals were converted to HTML on 2026-10-21. This `.md` is the source of the day HTML page (step 4B): it goes to the Windows recycle bin once the page is generated and checked (Eric's decision of 2026-10-21).
- Present the file with `mcp__cowork__present_files` (if the tool is not available, say so in the final report, do not block)

### Rules

- Short paths (e.g. `docs/01_docs_config_system/01_config_system_SH_PY_YAML/sensors/P1_kWh_clim.yaml`)
- Matrix IDs for the tiles (L2C1, L1C3, etc.)
- Empty session: write `SESSION VIDE - aucune modification`
- Standalone block: readable without context by someone resuming the project later

---
## STEP 4 - OBSIDIAN COPY (chained automatically, without asking)

**Destination folder:** `D:\Cerveau-Obsidian\14 Boulot\Journal\`

### To copy

- the merged journal just written at step 3
- the journal `histo_[date]_s[N].md` of step 1
- all `histo_*.md` / `histo_*.txt` newer than those already in the Obsidian folder (catch-up case)
- since 2026-10-21 the copy is done BEFORE step 4B, which sends the converted `.md` to the recycle bin; the HTML pages are not copied to Obsidian (not requested)

### Rules

- Never overwrite an existing file of the Obsidian folder: if it already exists, do not copy it and report it. Only exception: a merged journal of the same name (same-day update), which is overwritten WITHOUT a backup on D: (rule: never a backup on D:). The previous version stays in `historique\02_HISTO_ET_FUSIONNE\FUSIONNE\` (backup `.bak_AAAA_MM_JJ_HHhMMmSSs.{ext}` made at step 3).
- The old merged journal stays in the Obsidian folder.
- After each copy, compare the source / destination MD5 and note it in the report (`identique` or `DIFFERENT`).
- If `D:\` or the folder is inaccessible: report it, do not block and do not create another folder instead.

---

## STEP 4B - DARK HTML PAGES AND RECYCLE BIN FOR THE ORIGINALS (chained automatically, without asking, after the Obsidian copy; decided by Eric on 2026-10-21)

The session journals and merged journals are readable as dark HTML (same palette as `TODO\TODO.html`): one page per day for the journals, one page per merged journal. Script: `python -I "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\histo_html\histo_html.py"`. Trace: `debut pages_html` / `fin pages_html`.

1. Run the script without argument: it regenerates the day page `historique\02_HISTO_ET_FUSIONNE\histo_AAAA-MM-JJ.html` (all sessions of the day inside, one `<section>` tag per session) and the page of the most recent merged journal `historique\02_HISTO_ET_FUSIONNE\FUSIONNE\JOURNAL_FUSIONNE_..._[DATE_FIN].html`, then rebuilds both `index.html`. Other uses: `AAAA-MM-JJ` (one day), `fusionne` (all merged journals), `tout` (full catch-up). The script finds the folders by the start of their name (`02_*` and `FUSION*`, case-insensitive).
2. Read each output line: `cree`, `mis a jour` (the old page is copied to `.bak_AAAA_MM_JJ_HHhMMmSSs.html`), `inchange`, `COLLISION`. COLLISION = a page of the same name exists without the script mark: it is NEVER overwritten; report it at the top of the final report and do not send its source to the recycle bin.
3. Check before any recycle bin: the day page exists and contains the session just written (one more `<section>` tag), the merged page exists.
4. Send to the Windows recycle bin (command of step 5, never a permanent deletion) the originals whose HTML page exists: the `histo_AAAA-MM-JJ_sN.md` and `.txt` of `02_HISTO_ET_FUSIONNE\`; the `JOURNAL_FUSIONNE_*.md` and `JOURNAL_COMPLET_*.md` of `FUSIONNE\`, EXCEPT the most recent `JOURNAL_FUSIONNE_*.md` (largest end date), which stays as the base of step 3 next time. Never recycle if the page is missing or in COLLISION. The `.bak` are not concerned (cleanup of step 5).
5. Write the list of files sent to the recycle bin (original path of each) in `historique\03_RAPPORTS\02_MENAGE_BAK\pages_html_AAAA-MM-JJ.txt` and cite it in the final report. Modification journal: one line per file, or one LOT line with the path of this report beyond 10 (journal-modifs skill; the day journal is in `historique\03_RAPPORTS\01_MODIFS_IA\`).
6. No go to wait for. Script failure or missing page: say it in the report, send nothing to the recycle bin, continue.

---

## STEPS 5, 5B, 5C - CLEANUP, DASHBOARD EXPORT, PUSH TO PROD

Chained without asking, after step 4B. Read `histo_ref_menage.md`. Trace: `menage`, `export_5B`, `push_docs`. Key rules:
- `.bak` cleanup of `docs` and `Claude md SAVE` only if the histo is definitive. Timestamped of the day: 10 at most, Statut `bak_h`. At the definitive cleanup: the most recent becomes `.bak_AAAA_MM_JJ` (Statut `bak_d`), the other timestamped ones go to the recycle bin after the Statut `Trash`; 3 `.bak_AAAA_MM_JJ` at most per file.
- Windows recycle bin: never emptied by the cleanup, except items older than 3 months (at the definitive cleanup).
- Push to prod (5C): all of `docs` except `XX_` and except `.bak`, MD5 before and after, never a backup on H: nor on D:. The English skill copies (`05_docs_skills_PURE`) and the French sheets (`05_docs_skills_MD`) go with the push like the rest of `docs`.

## STEP 6 - TREE AND CHECKS

After the cleanup. Read `histo_ref_controles.md` (tree, checks 6B to 6G, badges, push catch-up, final report format). Trace: `tree`, `controles_6B` to `controles_6G`.

## STRICT EXECUTION ORDER

0. Trace journal: `seq-debut histo` (unless called by /histo-final), reading of the starting tokens, then `debut` / `fin` around each step.
0B. Definitive histo or not (see above).
1. Logbook: date, session number, journal block, writing of `historique/02_HISTO_ET_FUSIONNE/histo_[date]_s[N].md`, presenting the file.
2. Sync_index (step 2), without pause or question.
3. Merged journal (step 3).
4. Obsidian copy (step 4).
4B. Dark HTML pages (step 4B), converted originals to the recycle bin.
5. Cleanup (step 5), then Dashboard export (5B), then push to prod (5C).
6. Tree and checks (step 6, points 1 to 13).
7. Reading of the end tokens, `histo_trace.py verifier`, then (unless called by /histo-final) `seq-fin`, `recap`, `html`.
8. Final report in the format of `histo_ref_controles.md`.
