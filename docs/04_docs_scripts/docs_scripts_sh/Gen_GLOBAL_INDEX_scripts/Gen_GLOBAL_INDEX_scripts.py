# -*- coding: utf-8 -*-
r"""
gen_global_index_scripts.py - genere GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md
a la racine de docs/04_docs_scripts.

Sources : arbre local docs_scripts_SH / docs_scripts_YAML / *_MD, et la prod en lecture seule :
H:\scripts.yaml, H:\automations.yaml, H:\shell_command, H:\.scripts, registre HA (entity_registry).
Ecrit uniquement les deux fichiers (sauvegarde locale .bak_AAAA_MM_JJ_HHhMMmSSs.md avant
ecrasement si le contenu change). Usage : python -I gen_global_index_scripts.py [--dry]
"""
import os, re, sys, json, hashlib, shutil, datetime
from urllib.parse import quote, unquote
import yaml

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild"
DOCS = os.path.join(ROOT, "docs", "04_docs_scripts")
SH = os.path.join(DOCS, "docs_scripts_SH")
SHMD = os.path.join(DOCS, "docs_scripts_SH_MD")
YA = os.path.join(DOCS, "docs_scripts_YAML")
YAMD = os.path.join(DOCS, "docs_scripts_YAML_MD")
SKILLS = os.path.join(ROOT, ".claude", "skills")
P_SCRIPTS = r"H:\scripts.yaml"
P_AUTO = r"H:\automations.yaml"
P_SC = r"H:\.scripts"
P_SHC = r"H:\shell_command"
P_ENT = r"H:\.storage\core.entity_registry"
OUT_SH = os.path.join(DOCS, "GLOBAL_INDEX_SCRIPTS_SH.md")
OUT_YA = os.path.join(DOCS, "GLOBAL_INDEX_SCRIPTS_YAML.md")
DRY = "--dry" in sys.argv


def esc(s):
    return str(s).replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def link(label, path):
    rel = os.path.relpath(path, DOCS) if os.path.isabs(path) else path
    return "[%s](%s)" % (esc(label), quote(rel.replace("\\", "/")))


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def files_of(root):
    res = []
    for dp, dn, fn in os.walk(root):
        for f in sorted(fn):
            if ".bak_" in f or f.endswith(".bak"):
                continue
            res.append(os.path.join(dp, f))
    return sorted(res)


def toks(s):
    return [x for x in re.split(r"[^a-z0-9]+", s.lower()) if x]


def tmatch(a, b):
    return a == b or (len(a) >= 4 and len(b) >= 4 and (a.startswith(b) or b.startswith(a)))


def find_fiche(mdroot, name, key=""):
    cands = [p for p in files_of(mdroot) if p.endswith(".md")]
    stem = os.path.splitext(name)[0]
    for p in cands:
        if os.path.splitext(os.path.basename(p))[0].lower() == stem.lower():
            return p
    for p in cands:
        t = read(p)
        if name in t or (key and re.search(r"\b%s\b" % re.escape(key), t)):
            return p
    yt = toks(stem)
    best, bk = None, None
    for p in cands:
        mt = toks(os.path.splitext(os.path.basename(p))[0])
        if len(mt) >= 2 and all(any(tmatch(x, y) for y in yt) for x in mt):
            k = (len(mt), -abs(len(yt) - len(mt)))
            if bk is None or k > bk:
                best, bk = p, k
    return best


EXPL = [
    "## Difference entre l'index SH et l'index YAML",
    "",
    "- Scripts SH (index GLOBAL_INDEX_SCRIPTS_SH.md, dossier docs_scripts_SH) : programmes bash ou python, executes par un interpreteur sur une machine, pas par Home Assistant lui-meme. En prod ils sont dans /config/.scripts (H:\\.scripts) et HA les lance par une commande shell_command (dossier H:\\shell_command). Les scripts de controle et de generation (hermes_*, gen_*) tournent sur le PC d'Eric, sans passer par HA. Un script SH se modifie et se pousse comme un fichier.",
    "- Scripts YAML (index GLOBAL_INDEX_SCRIPTS_YAML.md, dossier docs_scripts_YAML) : scripts Home Assistant definis dans H:\\scripts.yaml, qui existent comme entites script.xxx. Ce sont des suites d'actions HA, appelables par un bouton du dashboard, une automatisation ou un autre script. Un script YAML peut declencher un script SH par une action shell_command.xxx.",
    "- Chaine type : bouton du dashboard -> script YAML (scripts.yaml) -> commande shell_command (H:\\shell_command) -> script SH (/config/.scripts).",
    "- Verification par /histo : les deux index sont regeneres par docs/04_docs_scripts/docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py a chaque /histo. La section Controle liste les ecarts et /histo doit verifier que la ligne liens=N casses=M donne casses=0. Ne pas modifier ces fichiers a la main.",
    "",
]


def load_prod():
    scripts = yaml.safe_load(read(P_SCRIPTS)) or {}
    autos = yaml.safe_load(read(P_AUTO)) or []
    cmds = {}
    for f in files_of(P_SHC):
        if not f.endswith((".yaml", ".yml")):
            continue
        try:
            dd = yaml.safe_load(read(f))
        except Exception:
            continue
        if isinstance(dd, dict):
            for k, v in dd.items():
                cmds[k] = (str(v), os.path.basename(f))
    ent = json.loads(read(P_ENT))["data"]["entities"]
    reg = {str(e["unique_id"]): e["entity_id"] for e in ent if e.get("platform") == "script"}
    return scripts, autos, cmds, reg


def dump(v):
    return yaml.safe_dump(v, allow_unicode=True)


def header(title, now, counts):
    L = ["# " + title, "",
         "Fichier GENERE le %s par docs/04_docs_scripts/docs_scripts_SH/gen_global_index_scripts/gen_global_index_scripts.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications." % now, ""]
    L += EXPL
    return L


def write_out(path, content, label):
    nb, ko = 0, []
    for mm in re.finditer(r"\]\(([^)]+)\)", content):
        nb += 1
        rel = unquote(mm.group(1))
        if not os.path.exists(os.path.join(DOCS, rel.replace("/", os.sep))):
            ko.append(rel)
    print("%s : liens=%d casses=%d" % (label, nb, len(ko)))
    for x in ko[:20]:
        print("  LIEN_CASSE : " + x)
    if DRY:
        return
    old = read(path) if os.path.exists(path) else None

    def norm(s):
        return re.sub(r"Fichier GENERE le \S+ \S+", "Fichier GENERE le X", s.replace("\r\n", "\n"))

    if old is not None and norm(old) == norm(content):
        print("%s : inchange" % label)
        return
    if old is not None:
        stamp = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")
        shutil.copy2(path, path[:-3] + ".bak_" + stamp + ".md")
        print("%s : sauvegarde .bak_%s" % (label, stamp))
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("%s : ecrit" % label)


def build_sh(now, scripts, autos, cmds):
    rows, sans_fiche, prod_diff, prod_abs = [], [], [], []
    skill_txt = {}
    if os.path.isdir(SKILLS):
        for s in os.listdir(SKILLS):
            p = os.path.join(SKILLS, s, "SKILL.md")
            if os.path.exists(p):
                skill_txt[s] = read(p)
    for folder in sorted(os.listdir(SH)):
        fd = os.path.join(SH, folder)
        if not os.path.isdir(fd):
            continue
        for p in files_of(fd):
            name = os.path.basename(p)
            if name.lower().endswith(".pyc") or (len(name) > 2 and name.startswith("#") and name.endswith("#")):
                continue  # bytecode et verrous d editeur : pas des scripts (decide par Eric le 2026-10-18)
            ext = os.path.splitext(name)[1].lower()
            typ = {".sh": "bash", ".py": "python"}.get(ext, "autre")
            pp = os.path.join(P_SC, name)
            if os.path.exists(pp):
                st = "identique" if md5(pp) == md5(p) else "DIFFERENT"
            else:
                st = "absent de H:\\.scripts"
            if st == "DIFFERENT":
                prod_diff.append(name)
            keys = [k for k, (c, fn) in cmds.items() if re.search(r"(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])" % re.escape(name), c)]
            users = []
            for k in keys:
                for sk, sv in scripts.items():
                    if re.search(r"shell_command\.%s(?![A-Za-z0-9_])" % re.escape(k), dump(sv)):
                        users.append("script " + sk)
                for a in autos:
                    if isinstance(a, dict) and re.search(r"shell_command\.%s(?![A-Za-z0-9_])" % re.escape(k), dump(a)):
                        users.append("automation " + str(a.get("alias", a.get("id"))))
            sk = [s for s, t in skill_txt.items() if name in t]
            fi = find_fiche(SHMD, name, folder)
            if not fi:
                sans_fiche.append(name)
            rows.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
                link(name, p), typ, st,
                esc(", ".join("shell_command." + k for k in keys) or "-"),
                esc(", ".join(users) or "-"), esc(", ".join(sk) or "-"),
                link(os.path.basename(fi), fi) if fi else "aucune", esc(folder)))
    L = header("GLOBAL_INDEX_SCRIPTS_SH.md - index des scripts shell et python", now, None)
    L += ["## Controle", "",
          "- Scripts SH indexes : %d" % len(rows),
          "- Scripts sans fiche dans docs_scripts_SH_MD : %d%s" % (len(sans_fiche), (" (" + ", ".join(sans_fiche) + ")") if sans_fiche else ""),
          "- Scripts presents dans H:\\.scripts avec un contenu different du local : %d%s" % (len(prod_diff), (" (" + ", ".join(prod_diff) + ")") if prod_diff else ""),
          "- Les scripts 'absent de H:\\.scripts' tournent sur le PC ou ne sont pas deployes : a lire avec la colonne Skill.", "",
          "## Scripts SH", "",
          "| Script | Type | Copie dans H:\\.scripts | Lance par (shell_command) | Appele par (HA) | Skill (PC) | Fiche | Dossier |",
          "|:-------|:-----|:-----------------------|:--------------------------|:----------------|:-----------|:------|:--------|"]
    L += rows
    L.append("")
    print("SH : scripts=%d sans_fiche=%d prod_different=%d" % (len(rows), len(sans_fiche), len(prod_diff)))
    return "\n".join(L)


def build_yaml(now, scripts, autos, cmds, reg):
    rows, sans_yaml, diff, sans_fiche = [], [], [], []
    local = {}
    for p in files_of(YA):
        if p.endswith(".yaml"):
            local[os.path.splitext(os.path.basename(p))[0].lower()] = p  # cle insensible a la casse (corrige le 2026-10-18)
    sh_files = {os.path.basename(p): p for p in files_of(SH)}
    for key, v in scripts.items():
        v = v or {}
        lp = local.get(key.lower())
        if lp:
            try:
                ld = yaml.safe_load(read(lp)) or {}
            except Exception:
                ld = {}
            st = "identique" if ld.get(key) == v else "DIFFERENT"
            if st == "DIFFERENT":
                diff.append(key)
        else:
            st = "aucun YAML local"
            sans_yaml.append(key)
        called, shl = [], []
        for k in sorted(set(re.findall(r"shell_command\.([a-z0-9_]+)", dump(v)))):
            called.append("shell_command." + k)
            for fn in re.findall(r"/config/\.scripts/([^\s'\"]+)", cmds.get(k, ("", ""))[0]):
                shl.append(link(fn, sh_files[fn]) if fn in sh_files else esc(fn))
        fi = find_fiche(YAMD, os.path.basename(lp) if lp else key + ".yaml", key)
        if not fi:
            sans_fiche.append(key)
        rows.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            esc(key), esc(v.get("alias", "")), "`%s`" % reg[key] if key in reg else "inconnu",
            esc(v.get("mode", "")), link(os.path.basename(lp), lp) if lp else "aucun", st,
            esc(", ".join(called) or "-") + (" -> " + ", ".join(shl) if shl else ""),
            link(os.path.basename(fi), fi) if fi else "aucune"))
    only_local = sorted(k for k in local if k not in scripts)
    pys = [p for p in files_of(YA) if p.endswith(".py")]
    L = header("GLOBAL_INDEX_SCRIPTS_YAML.md - index des scripts Home Assistant", now, None)
    L += ["## Controle", "",
          "- Scripts dans H:\\scripts.yaml (prod) : %d" % len(scripts),
          "- Scripts de la prod sans YAML local : %d%s" % (len(sans_yaml), (" (" + ", ".join(sans_yaml) + ")") if sans_yaml else ""),
          "- Scripts dont le contenu local differe de la prod : %d%s" % (len(diff), (" (" + ", ".join(diff) + ")") if diff else ""),
          "- Scripts sans fiche dans docs_scripts_YAML_MD : %d%s" % (len(sans_fiche), (" (" + ", ".join(sans_fiche) + ")") if sans_fiche else ""),
          "- YAML locaux absents de scripts.yaml : %d%s" % (len(only_local), (" (" + ", ".join(only_local) + ")") if only_local else ""),
          "- Fichiers .py rangés dans docs_scripts_YAML (ce sont des scripts de type SH) : %d" % len(pys), "",
          "## Scripts YAML", "",
          "| Cle | Alias | Entite HA | Mode | YAML local | Local = prod | Appelle (shell_command -> script SH) | Fiche |",
          "|:----|:------|:----------|:-----|:-----------|:-------------|:-------------------------------------|:------|"]
    L += rows
    L += ["", "## Fichiers .py rangés dans docs_scripts_YAML", "",
          "Ces fichiers sont des scripts python lances par shell_command : ils releveraient plutot de l'index SH. Ils sont listes ici parce qu'ils sont rangés dans ce dossier.", ""]
    for p in pys:
        pp = os.path.join(P_SC, os.path.basename(p))
        st = ("identique" if md5(pp) == md5(p) else "DIFFERENT") if os.path.exists(pp) else "absent de H:\\.scripts"
        L.append("- %s : copie dans H:\\.scripts : %s" % (link(os.path.basename(p), p), st))
    L.append("")
    print("YAML : scripts=%d sans_yaml=%d different=%d sans_fiche=%d yaml_hors_scripts=%d py_dans_yaml=%d" % (
        len(scripts), len(sans_yaml), len(diff), len(sans_fiche), len(only_local), len(pys)))
    return "\n".join(L)


def main():
    for p in (P_SCRIPTS, P_AUTO, P_SC, P_SHC, P_ENT):
        if not os.path.exists(p):
            print("ERREUR : prod non accessible : " + p)
            sys.exit(2)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    scripts, autos, cmds, reg = load_prod()
    write_out(OUT_SH, build_sh(now, scripts, autos, cmds), "GLOBAL_INDEX_SCRIPTS_SH")
    write_out(OUT_YA, build_yaml(now, scripts, autos, cmds, reg), "GLOBAL_INDEX_SCRIPTS_YAML")


main()
