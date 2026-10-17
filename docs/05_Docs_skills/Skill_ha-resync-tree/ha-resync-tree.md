---
name: "ha-resync-tree"
description: "Skill HA ReBuild - resynchronise les fichiers YAML locaux depuis le repo GitHub (source de verite n 2). Declencher OBLIGATOIREMENT quand l'utilisateur dit \"resync tree\", \"resync depuis GitHub\", \"met a jour le local depuis GitHub\", \"les fichiers locaux sont en retard\", \"compare local vs GitHub\", \"audit MD5 YAML\", \"quels fichiers ont change sur GitHub\", \"synchro depuis le repo\", \"pull depuis GitHub\", \"met le local a jour depuis la prod\". S'active aussi sur : \"debut de session\", \"on commence par un audit\", \"est-ce que le local est a jour\"."
---

# HA Resync Tree - Local <- GitHub

Resynchronise les fichiers YAML de config locaux avec le repo GitHub (`home_assistant_re-build`),
qui est le reflet de la prod HA (source de verite n 2).

---

## CONTEXTE

| Source | Role |
|:---|:---|
| **GitHub `home_assistant_re-build`** | Source de verite n 2 - reflet de la prod HA |
| **Local `docs/01_docs_config_system/config_system_YAML/`** | Espace de travail - peut etre en retard |
| **Local `docs/03_docs_automations/docs_automations_YAML/`** | Automations individuelles locales |

**Base projet locale** : `C:\Users\Berry Swann\Documents\ReBuild\`
**Chemin bash sandbox** : `/sessions/bold-determined-wright/mnt/Documents--ReBuild/`

> Note : le prefixe de session bash peut changer. Verifier avec `ls /sessions/` si besoin.

**Regle** : Si GitHub est plus recent que le local -> copier GitHub -> local (jamais l'inverse sans validation).

---

## WORKFLOW

### Etape 1 - Telecharger le repo GitHub

```bash
rm -rf /tmp/ha_repo && mkdir -p /tmp/ha_repo
wget -q --timeout=30 "https://github.com/BerrySwann/home_assistant_re-build/archive/refs/heads/main.zip" \
     -O /tmp/ha_repo.zip
unzip -q -o /tmp/ha_repo.zip -d /tmp/ha_repo/
echo "Repo extrait dans : /tmp/ha_repo/home_assistant_re-build-main/"
ls /tmp/ha_repo/home_assistant_re-build-main/
```

### Etape 2 - MD5 GitHub vs local (perimetre config uniquement)

Perimetre critique : `sensors/`, `templates/`, `utility_meter/`, `command_line/`, `groups/`, `input_booleans/`, `input_number/`, `shell_command/`, `notifs/`, `blueprints/`.
**Exclure** : `docs/` (302 fichiers de documentation - pas de config live), `automations.yaml`, fichiers racine.

```bash
REPO="/tmp/ha_repo/home_assistant_re-build-main"
LOCAL="/sessions/bold-determined-wright/mnt/Documents--ReBuild/docs/01_docs_config_system/config_system_YAML"

# MD5 GitHub - perimetre config seulement (hors docs/ et automations*)
find "$REPO" -type f -name "*.yaml" \
  -not -path "*/docs/*" \
  -not -name "automations.yaml" \
  -not -name "Dashboard_*.yaml" \
  -not -name "ip_bans.yaml" \
  -not -name "scenes.yaml" \
  -not -name "scripts.yaml*" \
  -not -name "sql.yaml" \
  -not -name "configuration.yaml" \
  | sort | xargs md5sum | sed "s|$REPO/||" | sort > /tmp/github_yaml_md5.txt

# MD5 local config_system_YAML
find "$LOCAL" -type f -name "*.yaml" \
  | sort | xargs md5sum | sed "s|$LOCAL/||" | sort > /tmp/local_yaml_md5.txt

echo "=== GitHub config : $(wc -l < /tmp/github_yaml_md5.txt) fichiers ==="
echo "=== Local config  : $(wc -l < /tmp/local_yaml_md5.txt) fichiers ==="
```

Puis comparer avec join pour un tableau propre :

```bash
# Fichiers presents des deux cotes : detecter les MD5 differents
join -1 2 -2 2 \
  <(sort -k2 /tmp/github_yaml_md5.txt) \
  <(sort -k2 /tmp/local_yaml_md5.txt) | \
  awk '$2 != $3 {print "DIFF " $1}' | head -30

# Fichiers GitHub absents du local
comm -23 \
  <(awk '{print $2}' /tmp/github_yaml_md5.txt | sort) \
  <(awk '{print $2}' /tmp/local_yaml_md5.txt | sort) | \
  sed 's/^/ABSENT_LOCAL /'

# Fichiers locaux absents de GitHub
comm -13 \
  <(awk '{print $2}' /tmp/github_yaml_md5.txt | sort) \
  <(awk '{print $2}' /tmp/local_yaml_md5.txt | sort) | \
  sed 's/^/ABSENT_GITHUB /'
```

Resultat attendu : tableau avec statut par fichier :
- OK - MD5 identiques
- DIFF - meme nom, MD5 different -> conflit a traiter
- ABSENT_LOCAL - present GitHub, absent local -> a copier
- ABSENT_GITHUB - present local, absent GitHub -> a investiguer

### Etape 3 - Analyser les ecarts et proposer les actions

Pour chaque ecart identifie :

| Cas | Action |
|:----|:-------|
| Fichier GitHub absent du local | -> Copier GitHub -> local |
| **MD5 different (meme nom)** | -> **CONFLIT : verifier lequel est le plus recent - HA = verite n 1** |
| Fichier local absent de GitHub | -> Push manquant depuis HA ; signaler a l'utilisateur |
| MD5 identique | -> OK RAS |

**Avant de copier un fichier GitHub -> local** : verifier s'il n'y a pas de modifications locales non encore poussees vers HA. En cas de doute -> demander a l'utilisateur.

### Etape 4 - Copier les fichiers en retard (GitHub -> local)

```bash
REPO="/tmp/ha_repo/home_assistant_re-build-main"
LOCAL="/sessions/bold-determined-wright/mnt/Documents--ReBuild/docs/01_docs_config_system/config_system_YAML"

# Exemple : copier un fichier specifique
cp "$REPO/sensors/P1_clim_chauffage/P1_DUT/P1_DUT_clim_chauffage.yaml" \
   "$LOCAL/sensors/P1_clim_chauffage/P1_DUT/"

# Exemple : copier un dossier entier
cp -r "$REPO/templates/P0_Energie_total_diag/P0_Genelec_appart/" \
      "$LOCAL/templates/P0_Energie_total_diag/"
```

Signaler a chaque copie : `Copie : chemin/relatif/fichier.yaml`.

### Etape 5 - Audit automations (si demande)

```bash
REPO="/tmp/ha_repo/home_assistant_re-build-main"
LOCAL_ATMA="/sessions/bold-determined-wright/mnt/Documents--ReBuild/docs/03_docs_automations/docs_automations_YAML"

# Compter les alias dans automations.yaml GitHub
grep "^  alias:" "$REPO/automations.yaml" | wc -l

# Compter les fichiers YAML locaux (hors old/)
find "$LOCAL_ATMA" -name "*.yaml" -not -path "*/old/*" -not -path "*/_old*" | wc -l

# Lister les alias GitHub pour comparaison
grep "^  alias:" "$REPO/automations.yaml" | sed 's/  alias: //' | sort > /tmp/github_aliases.txt
cat /tmp/github_aliases.txt
```

### Etape 6 - Resume

Communiquer a l'utilisateur :
- Nombre de fichiers compares (GitHub vs local)
- Nombre de fichiers copies GitHub -> local
- Fichiers en conflit MD5 (a traiter manuellement)
- Fichiers locaux absents de GitHub (a investiguer)
- Etat global : OK local a jour / N fichiers en ecart

---

## REGLES

1. **Ne jamais ecraser un fichier local sans le signaler** - toujours indiquer ce qui va etre remplace.
2. **En cas de conflit MD5** (meme nom, MD5 different) -> demander a l'utilisateur quelle version garder.
3. **`secrets.yaml` -> NE JAMAIS COPIER** dans aucun sens.
4. **`docs/`** dans le repo GitHub = documentation archivee, pas config live - ne pas inclure dans le perimetre de comparaison config.
5. Apres resync, proposer de lancer `/sync_index` si des entites cles ont change.

