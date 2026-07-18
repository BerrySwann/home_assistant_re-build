# 🛠️ COMMANDES TERMINAL HA — RÉFÉRENCE
*Dernière mise à jour : 2026-06-19*

> ⚠️ Chemin réel : `/homeassistant/` (et non `/config/` — symlink non suivi par `find`)

---

## 📂 TREE PROD — Export arborescence fichiers

```bash
DATE=$(date +%Y-%m-%d)
find /homeassistant \
  -name "*.yaml" -not -path "*/custom_components/*" -not -path "*/.git/*" \
  -not -path "*/blueprints/*" -not -path "*/.storage/*" \
  -not -path "*/www/*" -not -path "*/deps/*" \
  -print > /homeassistant/prod_tree_${DATE}.txt
find /homeassistant \
  -name "*.sh" -not -path "*/.git/*" \
  -print >> /homeassistant/prod_tree_${DATE}.txt
find /homeassistant \
  -name "*.txt" -not -path "*/.git/*" -not -name "prod_tree_*.txt" \
  -print >> /homeassistant/prod_tree_${DATE}.txt
sort -o /homeassistant/prod_tree_${DATE}.txt /homeassistant/prod_tree_${DATE}.txt
echo "✅ $(wc -l < /homeassistant/prod_tree_${DATE}.txt) fichiers listés"
```

Sortie : `/homeassistant/prod_tree_YYYY-MM-DD.txt` (accessible via Samba)

---

## 🔍 AUDIT MD5 — GitHub vs Prod

```bash
bash /homeassistant/.scripts/audit_md5.sh
```

Log : `/homeassistant/.logs/md5_audit_latest.txt`

---

## 🔄 GIT BACKUP — Push manuel

```bash
bash /homeassistant/.scripts/ha_git_backup.sh "Manuel"
```

Log : `/homeassistant/.logs/ha_git_backup.log`

---

## 📋 LOGS UTILES

```bash
# Dernier backup git
tail -5 /homeassistant/.logs/ha_git_backup.log

# Dernier audit MD5
cat /homeassistant/.logs/md5_audit_latest.txt

# Log zones Eric
tail -20 /homeassistant/.logs/zone_eric.txt

# Log diag conso
tail -20 /homeassistant/notifs/diag_conso_elec.txt
```

---

## 🗂️ CHEMINS CLÉS

| Quoi | Chemin prod |
|:-----|:-----------|
| Config HA | `/homeassistant/` |
| Scripts utilitaires | `/homeassistant/.scripts/` |
| Logs | `/homeassistant/.logs/` |
| Audit MD5 script | `/homeassistant/.scripts/audit_md5.sh` |
| Git backup script | `/homeassistant/.scripts/ha_git_backup.sh` |
| Prod tree script | `/homeassistant/.scripts/prod_tree.sh` |
| Samba accès | `\\10.32.154.243\config` |
