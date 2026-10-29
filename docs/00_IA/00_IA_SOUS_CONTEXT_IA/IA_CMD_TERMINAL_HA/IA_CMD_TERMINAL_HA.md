# 🛠️ COMMANDES TERMINAL HA - RÉFÉRENCE
*Dernière mise à jour : 2026-10-13 (vérifié contre `.scripts`, `shell_command`, `scripts.yaml`, `automations.yaml` et `.logs` prod du jour ; refonte d'origine du 2026-07-18)*

> ⚠️ Chemin réel : `/homeassistant/` (= `/config/`, symlink - les scripts internes utilisent `/config/`, `find` doit cibler `/homeassistant/`)

---

## 🔍 AUDIT MD5 - GitHub vs Prod

Deux scripts, 3 passes chacun (TREE local → MD5 prod → MD5 GitHub par curl raw → rapport), sans argument :

```bash
bash /homeassistant/.scripts/audit_md5_yaml.sh      # config YAML (fichiers)
bash /homeassistant/.scripts/audit_md5_md_yaml.sh   # docs (/config/docs : .md + .yaml + .sh)
```

- `audit_md5_yaml.sh` - périmètre codé en dur : sensors templates utility_meter command_line shell_command packages groups input_booleans input_number + `.scripts/*.sh` + racine (automations, scripts, configuration, sql, input_select, input_datetime, input_button). Statuts : ✅ SYNC · ❌ DIFF · ⚠️ PUSH MANQUANT
- `audit_md5_md_yaml.sh` - tout `/config/docs/`. Statuts : ✅ SYNC · ❌ DIFF · ⚠️ ABSENT GITHUB
- Depuis HA : `script.audit_md5` (shell_command `audit_md5`) et `script.audit_md5_md_yaml` (shell_command `audit_md5_md_yaml`)
- **Logs** : `/homeassistant/.logs/md5_audit_yaml_YYYY-MM-DD.txt` + copie `md5_audit_latest.txt` ; `md5_audit_md_yaml_YYYY-MM-DD.txt` + copie `md5_audit_md_yaml_latest.txt`. Les anciens logs du même type sont supprimés à chaque lancement.

```bash
cat /homeassistant/.logs/md5_audit_latest.txt
cat /homeassistant/.logs/md5_audit_md_yaml_latest.txt
```

> ⛔ `audit_md5.sh`, les modes FULL · YAML · ATMA et les logs `audit_*.log` n'existent plus (vérifié 2026-10-13 dans `.scripts` et `.logs` ; CLAUDE.md est à jour sur ce point).

---

## 🔄 GIT BACKUP - HA → GitHub

```bash
bash /homeassistant/.scripts/ha_git_backup.sh "Manuel"
```

| Mode (`$1`) | Déclenchement | Effet |
|:------------|:--------------|:------|
| `auto` (sans argument) | shell_command `git_backup_push` : automations [01] toutes les **H+10** (00:10, 01:10...), [02] daily 03:00, [06] au démarrage HA | commit + push si changements |
| `weekly` | shell_command `git_backup_push_weekly` : automation [03] dimanche 01:30 (ou [05] manuel) | + tag ISO `weekly-YYYY-WXX` |
| `manuel` (argument "Manuel") | shell_command `git_backup_push_manual` : automation [04] (bouton dashboard) | push immédiat |

- Filtre commit : `.yaml`, `.yml`, `.md` modifiés - `secrets.yaml` jamais tracké (garde-fou)
- Si push rejeté : `git pull --rebase` auto + retry
- **Log** : `/homeassistant/.logs/ha_git_backup.log`

```bash
tail -5 /homeassistant/.logs/ha_git_backup.log
```

> 💡 **Conséquence pratique** : GitHub est à jour **au plus tard H+10 après tout changement prod** - pas besoin de déclenchement manuel sauf urgence. "Manuel ne fonctionne pas" = en réalité rien à committer (le H+10 a déjà tout poussé).

---

## 📂 TREE PROD - Export arborescence seule (si besoin hors audit)

> La PASS 1 de `audit_md5_yaml.sh` génère déjà le tree - cette commande ne sert que pour un export isolé. (`prod_tree.sh` n'existe plus.)

```bash
DATE=$(date +%Y-%m-%d)
find /homeassistant \( -name "*.yaml" -o -name "*.sh" -o -name "*.md" \) \
  -not -path "*/custom_components/*" -not -path "*/.git/*" \
  -not -path "*/.storage/*" -not -path "*/www/*" -not -path "*/deps/*" \
  -not -path "*/blueprints/*" | sort > /homeassistant/prod_tree_${DATE}.txt
wc -l /homeassistant/prod_tree_${DATE}.txt
```

---

## 📋 LOGS UTILES

```bash
tail -5  /homeassistant/.logs/ha_git_backup.log      # dernier backup git
cat      /homeassistant/.logs/md5_audit_latest.txt   # dernier audit MD5 config YAML
cat      /homeassistant/.logs/md5_audit_md_yaml_latest.txt   # dernier audit MD5 docs
tail -20 /homeassistant/.logs/zone_eric.txt          # log zones Eric (P4)
tail -20 /homeassistant/notifs/diag_conso_elec.txt   # diag conso journalier
tail -20 /homeassistant/notifs/ecart_liky_vs_nodon.txt  # ecart Linky vs pince Nodon
tail -20 /homeassistant/notifs/linky_histo.txt   # histo Linky quotidien (P0)
tail -20 /homeassistant/notifs/nodon_histo.txt   # histo Nodon quotidien (P0)
tail -20 /homeassistant/notifs/ecart_histo.txt   # ecart Linky vs Nodon quotidien (P0)
```

---

## 🗂️ CHEMINS CLÉS

| Quoi | Chemin prod |
|:-----|:-----------|
| Config HA | `/homeassistant/` |
| Scripts utilitaires | `/homeassistant/.scripts/` (audit_md5_yaml.sh · audit_md5_md_yaml.sh · ha_git_backup.sh · check_yaml_forme.py · correct_linky.py · #MP_01_monitor_temp.sh.# ⛔ ne pas toucher) |
| Logs | `/homeassistant/.logs/` |
| Notifs fichiers (File UI) | `/homeassistant/notifs/` |
| Docs pushées | `/homeassistant/docs/` (= H:\docs - miroir de docs/ local, renommé minuscule 2026-07-19) |
| Samba accès | `\\10.32.154.243\config` (monté en `H:\`) |
