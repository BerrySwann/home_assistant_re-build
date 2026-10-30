---
name: ha-push-md
description: >
  Skill HA ReBuild - pousse uniquement les fichiers *.md de documentation locaux vers H:\Docs (Samba HA).
  Declencher sur : "pousse les md en prod", "sync les docs markdown", "met a jour les docs texte",
  "push les md vers H:", "les md sont a jour en prod ?". Scope strict : *.md uniquement.
---

# HA Push MD - Local *.md -> H:\Docs

Pousse uniquement les fichiers `*.md` de documentation vers le partage Samba `H:\Docs\`.

> Scope strict : *.md uniquement. *.yaml jamais touches ici.

## CHEMINS DE REFERENCE

**Base projet (Windows)** : `C:\Users\Berry Swann\Documents\ReBuild\`

| Source locale | Destination prod |
|:---|:---|
| `docs\02_docs_dashboard\02_dashboard_docs_MD\` | `H:\Docs\` |
| `docs\03_docs_automations\03_docs_automations_MD\` | `H:\Docs\` |
| `docs\04_docs_scripts\04_docs_scripts_YAML_MD\` | `H:\Docs\` |
| `docs\04_docs_scripts\04_docs_scripts_SH_MD\` | `H:\Docs\` |

> Utiliser `mcp__Windows-MCP__PowerShell` pour H:\ (Samba). secrets.yaml interdit absolu.

## WORKFLOW

### AVANT TOUT PUSH - Controle des dossiers XX_ (decide par Eric le 2026-10-25 21:19, obligatoire)

Les dossiers `XX_` n'existent qu'en local et ne doivent jamais se perdre. Avant le premier calcul de ce skill, ET une seconde fois juste apres le push (controle avant/apres), lancer :
`python -I -X utf8 "C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_XX_presents\Check_XX_presents.py"`
Il refuse aussi tout dossier XX_ present en prod (ALERTE). Il compare les dossiers XX_ et leurs fichiers au manifeste `XX_manifest.json` (meme dossier). `RESULTAT : OK` = on continue. Une ALERTE (dossier ou fichier manquant) = ne RIEN pousser, prevenir Eric, restaurer depuis `TEMPO\XX_sauvegarde_2026-10-25` seulement sur son ordre. Les XX_ ne se poussent jamais en prod. Le manifeste ne se met a jour (`--maj`) que sur ordre d'Eric.

### 1 - MD5 local de tous les *.md
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

### 2 - MD5 prod de tous les *.md dans H:\Docs
```powershell
$prodMd5 = @{}
Get-ChildItem "H:\Docs" -Recurse -Filter "*.md" | ForEach-Object {
  $rel = $_.FullName.Replace("H:\Docs\", "")
  $prodMd5[$rel] = (Get-FileHash $_.FullName -Algorithm MD5).Hash
}
```

### 3 - Calcul du diff : identifier uniquement les fichiers a pousser
```powershell
$toPush = @()
$localMd5.Keys | ForEach-Object {
  if (-not $prodMd5.ContainsKey($_)) {
    $toPush += [PSCustomObject]@{ File=$_; Raison="NOUVEAU" }
  } elseif ($localMd5[$_] -ne $prodMd5[$_]) {
    $toPush += [PSCustomObject]@{ File=$_; Raison="DIFF" }
  }
}
# Afficher le resume avant de pousser
$toPush | Format-Table -AutoSize
Write-Host "$($toPush.Count) fichier(s) a pousser."
```

Si `$toPush.Count -eq 0` -> afficher "Tous les *.md sont a jour - rien a pousser" et arreter.

### 4 - Push uniquement les fichiers differents
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

### 5 - Verification MD5 finale sur les fichiers pousses
```powershell
$toPush | ForEach-Object {
  $h1 = (Get-FileHash "C:\Users\Berry Swann\Documents\ReBuild\...\$($_.File)" -Algorithm MD5).Hash
  $h2 = (Get-FileHash "H:\Docs\$($_.File)" -Algorithm MD5).Hash
  if ($h1 -eq $h2) { Write-Host "OK  $($_.File)" } else { Write-Host "DIFF $($_.File)" }
}
```

## REGLES

1. **MD5 d'abord, push uniquement les fichiers differents** - jamais d'ecrasement en masse.
2. **Afficher le diff avant de pousser** - l'utilisateur doit voir ce qui va changer.
3. ***.yaml -> jamais dans ce workflow.**
4. **secrets.yaml -> interdit absolu.**
5. **Local = verite absolue** : en cas de conflit, le local l'emporte.
6. **DEPENDANCES_GLOBALES_CLAUDE_memoire.md** : LOCAL SEUL (dossier XX_docs_MD_system, decide par Eric le 2026-10-25 21:25). Jamais pousse en prod ; s'il apparait dans un diff, l'ignorer et le signaler.
7. **Regle CLAUDE.md du 2026-10-13** : un push met a jour le `.md` du fichier pousse. Ici les fichiers pousses SONT des `.md` : verifier qu'ils ont ete mis a jour en local avant le push (c'est le travail de `ha-push-yaml` et `ha-push-docs` en amont). Ne jamais modifier un `.md` directement sur H:\ : local d'abord, avec sauvegarde.
