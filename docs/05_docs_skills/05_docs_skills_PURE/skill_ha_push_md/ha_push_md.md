---
name: ha-push-md
description: >
  HA ReBuild skill - pushes only the local documentation *.md files to H:\Docs (HA Samba share).
  Trigger on: "pousse les md en prod", "sync les docs markdown", "met a jour les docs texte",
  "push les md vers H:", "les md sont a jour en prod ?". Strict scope: *.md only.
---

# HA Push MD - Local *.md -> H:\Docs

Pushes only the documentation `*.md` files to the Samba share `H:\Docs\`.

> Strict scope: *.md only. *.yaml files are never touched here.

## REFERENCE PATHS

**Project base (Windows)**: `C:\Users\Berry Swann\Documents\ReBuild\`

| Local source | Prod destination |
|:---|:---|
| `docs\02_docs_dashboard\02_dashboard_docs_MD\` | `H:\Docs\` |
| `docs\03_docs_automations\03_docs_automations_MD\` | `H:\Docs\` |
| `docs\04_docs_scripts\04_docs_scripts_YAML_MD\` | `H:\Docs\` |
| `docs\04_docs_scripts\04_docs_scripts_SH_MD\` | `H:\Docs\` |

> Use `mcp__Windows-MCP__PowerShell` for H:\ (Samba). secrets.yaml is strictly forbidden.

## WORKFLOW

### BEFORE ANY PUSH - Check of the XX_ folders (decided by Eric on 2026-10-25 21:19, mandatory)

The `XX_` folders exist only locally and must never be lost. Before the first computation of this skill, AND a second time right after the push (before/after check), run:
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"`
It also refuses any XX_ folder present in prod (ALERTE). It compares the XX_ folders and their files with the manifest `XX_manifest.json` (same folder). `RESULTAT : OK` = continue. An ALERTE (missing folder or file) = push NOTHING, warn Eric, restore from `TEMPO\XX_sauvegarde_2026-10-25` only on his order. XX_ folders are never pushed to prod. The manifest is updated (`--maj`) only on Eric's order.

### 1 - Local MD5 of all *.md
```powershell
$base = "C:\Users\Berry Swann\Documents\ReBuild"
$sources = @(
  "$base\docs\02_docs_dashboard\02_dashboard_docs_MD",
  "$base\docs\03_docs_automations\03_docs_automations_MD",
  "$base\docs\04_docs_scripts\04_docs_scripts_YAML_MD",
  "$base\docs\04_docs_scripts\04_docs_scripts_SH_MD"
)
$localMd5 = @{}
$sources | ForEach-Object {
  if (Test-Path $_) {
    Get-ChildItem $_ -Recurse -Filter "*.md" | ForEach-Object {
      $rel = $_.FullName.Replace($_ + "\", "")
      $localMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
    }
  }
}
```

### 2 - Prod MD5 of all *.md in H:\Docs
```powershell
$prodMd5 = @{}
Get-ChildItem "H:\Docs" -Recurse -Filter "*.md" | ForEach-Object {
  $rel = $_.FullName.Replace("H:\Docs\", "")
  $prodMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
}
```

### 3 - Diff computation: identify only the files to push
```powershell
$toPush = @()
$localMd5.Keys | ForEach-Object {
  if (-not $prodMd5.ContainsKey($_)) {
    $toPush += [PSCustomObject]@{ File=$_; Raison="NOUVEAU" }
  } elseif ($localMd5[$_] -ne $prodMd5[$_]) {
    $toPush += [PSCustomObject]@{ File=$_; Raison="DIFF" }
  }
}
# Show the summary before pushing
$toPush | Format-Table -AutoSize
Write-Host "$($toPush.Count) fichier(s) a pousser."
```

If `$toPush.Count -eq 0` -> display "Tous les *.md sont a jour - rien a pousser" and stop.

### 4 - Push only the different files
```powershell
$toPush | ForEach-Object {
  $src  = "C:\Users\Berry Swann\Documents\ReBuild\...\$($_.File)"
  $dest = "H:\Docs\$($_.File)"
  $destDir = Split-Path $dest
  New-Item -ItemType Directory -Path $destDir -Force | Out-Null
  Copy-Item $src $dest -Force
  Write-Host "Pousse ($($_.Raison)) : $($_.File)"
}
```

### 5 - Final MD5 verification on the pushed files
```powershell
$toPush | ForEach-Object {
  $h1 = (Get-FileHash "C:\Users\Berry Swann\Documents\ReBuild\...\$($_.File)" -Algorithm MD5).Hash
  $h2 = (Get-FileHash "H:\Docs\$($_.File)" -Algorithm MD5).Hash
  if ($h1 -eq $h2) { Write-Host "OK  $($_.File)" } else { Write-Host "DIFF $($_.File)" }
}
```

## RULES

1. **MD5 first, push only the different files** - never a mass overwrite.
2. **Show the diff before pushing** - the user must see what will change.
3. ***.yaml -> never in this workflow.**
4. **secrets.yaml -> strictly forbidden.**
5. **Local = absolute truth**: in case of conflict, local wins.
6. **DEPENDANCES_GLOBALES_CLAUDE_memoire.md** (in `docs\00_IA\00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire\` since 2026-10-29): not one of this skill's sources. Since 2026-10-30 it goes to prod with the general push of /histo (step 5C, all of `docs` except `XX_` and `.bak`), no longer "local only" (that was the 2026-10-25 rule, replaced). If it shows up in a diff here, ignore it and report it.
7. **CLAUDE.md rule of 2026-10-13**: a push updates the `.md` of the pushed file. Here the pushed files ARE `.md` files: check they were updated locally before the push (this is the job of `ha-push-yaml` and `ha-push-docs` upstream). Never modify a `.md` directly on H:\ : local first, with a backup.

## Maintenance note

This is the usable English copy of the skill (written in English to save tokens). Paths, file names, entity ids and report labels stay in French. The French explanation sheet is `docs/05_docs_skills/05_docs_skills_MD/skill_ha_push_md/ha_push_md.md`: when this file changes, re-read that sheet and update it. The installed skill `.claude/skills/ha-push-md/SKILL.md` must stay identical to this copy.
