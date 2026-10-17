---
name: ha-resync-docs
description: >
  Skill HA ReBuild - compare et resynchronise les fichiers YAML config locaux depuis GitHub
  (source de verite n 2). Declencher sur : "resync depuis GitHub", "compare local vs GitHub",
  "audit MD5 YAML", "est-ce que le local est a jour", "debut de session", "on commence par un audit".
---

# HA Resync Docs - Local <- GitHub

Resynchronise les fichiers YAML de config locaux avec le repo GitHub (`home_assistant_re-build`),
reflet de la prod HA (source de verite n 2).

## CHEMINS DE REFERENCE

- **Local (Windows)** : `C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\config_system_YAML\`
- **Automations local** : `docs\03_docs_automations\docs_automations_YAML\`

> Les commandes bash ci-dessous tournent dans un environnement avec shell (sandbox Cowork ou
> autre). Le point de montage du dossier local n'est PAS fixe d'une session a l'autre : avant
> toute execution, verifier le chemin reel (`ls /sessions/` en sandbox Cowork, ou tout autre
> moyen selon l'environnement) et resoudre `{LOCAL_MNT}` ci-dessous avant de lancer le bloc.
> Ne jamais reutiliser un prefixe de session note dans une execution precedente sans le
> reverifier : il change a chaque nouvelle session.

**Regle** : GitHub -> local uniquement (jamais l'inverse sans validation).

## WORKFLOW

### 1 - Telecharger le repo GitHub
```bash
rm -rf /tmp/ha_repo && mkdir -p /tmp/ha_repo
wget -q --timeout=30 "https://github.com/BerrySwann/home_assistant_re-build/archive/refs/heads/main.zip" -O /tmp/ha_repo.zip
unzip -q -o /tmp/ha_repo.zip -d /tmp/ha_repo/
```

### 2 - MD5 GitHub vs local (perimetre config uniquement)

Exclure du repo GitHub : `docs/` (302 fichiers documentation), `automations.yaml`, fichiers racine.

```bash
REPO="/tmp/ha_repo/home_assistant_re-build-main"
LOCAL="{LOCAL_MNT}/docs/01_docs_config_system/config_system_YAML"   # resoudre {LOCAL_MNT} avant execution (voir note ci-dessus)

find "$REPO" -type f -name "*.yaml" \
  -not -path "*/docs/*" -not -name "automations.yaml" \
  -not -name "Dashboard_*.yaml" -not -name "ip_bans.yaml" \
  -not -name "scenes.yaml" -not -name "scripts.yaml*" \
  -not -name "sql.yaml" -not -name "configuration.yaml" \
  | sort | xargs md5sum | sed "s|$REPO/||" | sort > /tmp/github_yaml_md5.txt

find "$LOCAL" -type f -name "*.yaml" \
  | sort | xargs md5sum | sed "s|$LOCAL/||" | sort > /tmp/local_yaml_md5.txt

echo "GitHub config : $(wc -l < /tmp/github_yaml_md5.txt) fichiers"
echo "Local config  : $(wc -l < /tmp/local_yaml_md5.txt) fichiers"
```

Comparer avec join :
```bash
# MD5 differents (meme fichier)
join -1 2 -2 2 <(sort -k2 /tmp/github_yaml_md5.txt) <(sort -k2 /tmp/local_yaml_md5.txt) | awk '$2 != $3 {print "DIFF " $1}'
# Absent local
comm -23 <(awk '{print $2}' /tmp/github_yaml_md5.txt | sort) <(awk '{print $2}' /tmp/local_yaml_md5.txt | sort) | sed 's/^/ABSENT_LOCAL /'
# Absent GitHub
comm -13 <(awk '{print $2}' /tmp/github_yaml_md5.txt | sort) <(awk '{print $2}' /tmp/local_yaml_md5.txt | sort) | sed 's/^/ABSENT_GITHUB /'
```

Statuts : OK / DIFF (conflit - demander) / ABSENT_LOCAL (copier) / ABSENT_GITHUB (investiguer)

### 3 - Copier les fichiers manquants (GitHub -> local)
```bash
cp "$REPO/{chemin/fichier.yaml}" "$LOCAL/{chemin/}"
```
Signaler chaque copie. Ne jamais ecraser sans signaler.

### 4 - Audit automations (si demande)
```bash
grep "^  alias:" "$REPO/automations.yaml" | wc -l
find "$LOCAL_ATMA" -name "*.yaml" -not -path "*/old/*" | wc -l
```

### 5 - Resume
- Fichiers compares, copies, en conflit, absents GitHub
- Etat global : OK / N fichiers en ecart
- Proposer /sync_index si entites cles ont change

## REGLES

1. Ne jamais ecraser un fichier local sans le signaler.
2. Conflit MD5 -> demander a l'utilisateur quelle version garder.
3. secrets.yaml -> NE JAMAIS COPIER dans aucun sens.
4. docs/ du repo GitHub = documentation - ne pas inclure dans le perimetre config.
5. ***.md -> NE JAMAIS SYNCHRONISER** dans aucun sens. Les .md sont la source de verite locale, geres exclusivement par /ha_push_docs.
