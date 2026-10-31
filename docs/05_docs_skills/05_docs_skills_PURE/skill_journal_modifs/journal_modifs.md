---
name: journal-modifs
description: HA ReBuild skill - logs as you go every file modification (creation, modification, rename, deletion, push) in a per-author journal readable by Claude and Hermes. Apply after every write and read at the start of a session.
---

# Skill: journal-modifs

## Goal

Avoid modifications without a trace or an author (observed on 2026-10-10: CLAUDE.md, DEPENDANCES_GLOBALES_CLAUDE_memoire.md and presence cards were modified without a journal). Each agent (Claude, Hermes) writes one line per modified file, at the time of the modification, in its own file of the day. The other agent reads it at the start of its session.

## Locations

- Master (local, the only source since 2026-10-22): `C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_AAAA-MM-JJ_<auteur>.md`
- Old path historique\modifs\: folder moved as a whole on 2026-10-21 (Eric's order), do not recreate it.
- No copy to H: since 2026-10-22 (Eric's decision: a single local source). The old prod folder `H:\docs\modifs\` is no longer updated.
- `<auteur>`: `claude` or `hermes` (lowercase). Another agent takes its own name.
- Each agent writes ONLY in its own file, never in the other one's (avoids simultaneous writes).
- Hermes writes its own file in the same local folder (to confirm with Eric: before 2026-10-22 it wrote to `H:\docs\modifs\`).
- These files are not backups: no .bak, outside the scope of the /histo cleanup.

## When to log

After every SUCCESSFUL write in the project scope: creation, modification, rename, move, deletion (recycle bin), copy to H: or D:, push.

Scope: ReBuild (docs, scripts, historique, Github, TODO, MOC, Claude md SAVE, .claude), H: (docs, .scripts, config YAML), copies D:\Cerveau-Obsidian and D:\hermes.

Do not log: reads, temporary files in %TEMP%, the journal itself.

The line is written after the write, never before. If the write fails: log nothing, or log ECHEC with the cause.

## Line format

One line per file, appended at the end of the file (never rewrite the file). The action words stay in French:

`AAAA-MM-JJ HH:MM:SS | auteur | ACTION | full path | avant=XXXXXXXX apres=XXXXXXXX | short reason`

- ACTION: CREE, MODIFIE, RENOMME, DEPLACE, SUPPRIME, COPIE, POUSSE, ECHEC, LOT
- MD5: first 8 characters, lowercase; `-` if not applicable (created file: avant=- ; deleted file: apres=-)
- RENOMME, DEPLACE, COPIE, POUSSE: the path is the destination, the source goes in the reason (`depuis ...`)
- Backup made before modification: quote its name in the reason (`bak : nom`)
- Reason: a few words, no secret (never a password, token or file content)
- No line break inside a line. Plain ASCII preferred.
- First line of a new file: `# MODIFS AAAA-MM-JJ - <auteur>`

## Bulk operations

Beyond 10 files in one operation (.bak cleanup, folder push, resync): a single LOT line, with the number of files and the path of a report listing each file (dry-run, execution, log). This report must exist.

`AAAA-MM-JJ HH:MM:SS | auteur | LOT | <folder or operation> | n=<number> | rapport : <path>`

## Writing (PowerShell, adapt to the agent)

```powershell
$a='claude'   # or 'hermes'
$d=Get-Date -Format 'yyyy-MM-dd'
$enc=New-Object Text.UTF8Encoding($false)
$f="C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_${d}_$a.md"
New-Item -ItemType Directory -Force (Split-Path $f) | Out-Null
if(-not (Test-Path $f)){ [IO.File]::WriteAllText($f,"# MODIFS $d - $a`r`n",$enc) }
$ligne='{0} | {1} | MODIFIE | {2} | avant={3} apres={4} | {5}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'),$a,$chemin,$avant,$apres,$raison
[IO.File]::AppendAllText($f,$ligne+"`r`n",$enc)
```

File format: CRLF, UTF-8 without BOM. No copy to H: (decision of 2026-10-22).

## Start of session (mandatory)

1. Read the last lines of today's and yesterday's journals in `historique\03_RAPPORTS\01_MODIFS_IA\`: your own and the other agent's.
2. Look for unlogged modifications: list the files of the scope whose modification date is later than the last journal line and that have no line. Present them to the user BEFORE starting ("modifications sans journal : ..."), without guessing the author: it is unknown as long as no line says it.
3. Do not assume that a modification missing from the journal is your own.

## End of session and /histo

The two authors' journals of the day are the source of step 1 of /histo: each file quoted in the logbook must find its line. A gap is reported in the logbook ("modifications non journalisees : ...").

## Limits (know them)

- Does not cover modifications made by hand by the user or by HA (automatic git backup): hence the check at the start of the session.
- The journal is declarative: a missing line proves nothing, and an existing line does not prove that the file stayed as it was (compare the MD5 in case of doubt).

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, action words and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_journal_modifs/journal_modifs.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/journal-modifs/SKILL.md` must stay identical to this copy.
