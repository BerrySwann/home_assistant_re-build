# 🛠️ COMMANDES TERMINAL HA - RÉFÉRENCE
*Dernière mise à jour : 2026-07-18 (refonte - vérifié contre les scripts et logs prod du jour)*

> ⚠️ Chemin réel : `/homeassistant/` (= `/config/`, symlink - les scripts internes utilisent `/config/`, `find` doit cibler `/homeassistant/`)

---

## 🔍 AUDIT MD5 - GitHub vs Prod

```bash
bash /homeassistant/.scripts/audit_md5.sh
```

- **3 passes** : TREE local → MD5 prod → MD5 GitHub (curl raw) → rapport
- **Sans argument** - périmètre codé en dur : sensors templates utility_meter command_line shell_command packages groups input_booleans input_number + racine (automations, scripts, configuration, sql, input_*)
- Statuts : ✅ SYNC · ❌ DIFF · ⚠️ PUSH MANQUANT
- **Logs** : `/homeassistant/.logs/md5_audit_YYYY-MM-DD.txt` + copie `md5_audit_latest.txt`

```bash
cat /homeassistant/.logs/md5_audit_latest.txt
```

> ⚠️ **Écart doc connu** : CLAUDE.md mentionne des modes "FULL · YAML · ATMA (4 passes)" et un log `audit_md5.log` - **inexistants en prod** (vérifié 2026-07-18 : script 3 passes sans argument, aucun audit_md5.log dans .logs/). CLAUDE.md à corriger.

---

## 🔄 GIT BACKUP - HA → GitHub

```bash
bash /homeassistant/.scripts/ha_git_backup.sh manuel
```

| Mode (`$1`) | Déclenchement | Effet |
|:------------|:--------------|:------|
| `auto` | shell_command HA toutes les **H+10** (00:10, 01:10...) | commit + push si changements |
| `weekly` | dimanche (ou manuel) | + tag ISO `weekly-YYYY-WXX` |
| `manuel` | bouton dashboard (shell_command `git_backup_manuel`) | push immédiat |

- Filtre commit : `.yaml`, `.yml`, `.md` modifiés - `secrets.yaml` jamais tracké (garde-fou)
- Si push rejeté : `git pull --rebase` auto + retry
- **Log** : `/homeassistant/.logs/ha_git_backup.log`

```bash
tail -5 /homeassistant/.logs/ha_git_backup.log
```

> 💡 **Conséquence pratique** : GitHub est à jour **au plus tard H+10 après tout changement prod** - pas besoin de déclenchement manuel sauf urgence. "Manuel ne fonctionne pas" = en réalité rien à committer (le H+10 a déjà tout poussé).

---

## 📂 TREE PROD - Export arborescence seule (si besoin hors audit)

> La PASS 1 de `audit_md5.sh` génère déjà le tree - cette commande ne sert que pour un export isolé. (`prod_tree.sh` n'existe plus.)

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
cat      /homeassistant/.logs/md5_audit_latest.txt   # dernier audit MD5
tail -20 /homeassistant/.logs/zone_eric.txt          # log zones Eric (P4)
tail -20 /homeassistant/notifs/diag_conso_elec.txt   # diag conso journalier
tail -20 /homeassistant/notifs/ecart_liky_vs_nodon.txt  # ecart Linky vs pince Nodon
```

---

## 🗂️ CHEMINS CLÉS

| Quoi | Chemin prod |
|:-----|:-----------|
| Config HA | `/homeassistant/` |
| Scripts utilitaires | `/homeassistant/.scripts/` (audit_md5.sh · ha_git_backup.sh · #MP_01_monitor_temp.sh.# ⛔ ne pas toucher) |
| Logs | `/homeassistant/.logs/` |
| Notifs fichiers (File UI) | `/homeassistant/notifs/` |
| Docs pushées | `/homeassistant/docs/` (= H:\docs - miroir de DOCS/ local, renommé minuscule 2026-07-19) |
| Samba accès | `\\10.32.154.243\config` (monté en `H:\`) |
