#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check_prod_fonctionnelle.py - controle en lecture seule des fichiers qui font tourner la prod HA.

Decide par Eric le 2026-10-31 : la priorite absolue, ce sont les fichiers qui font tourner la prod.
Le manifeste est dans ce script (constantes P1_*, P2_*, ASSETS, KNOWN_ROOT). Fiche : 04_docs_scripts_SH_MD.

Paliers :
  P1 vital      : YAML racine + dossiers charges par configuration.yaml + .scripts
  P2 donnees    : historiques notifs/*.txt et export Dashboard_*.yaml de la racine
  ASSETS        : images citees par le dashboard (decision d'Eric 2026-10-31)
Hors manifeste (decide par Eric) : scenes.yaml, blueprints, themes, custom_components, www/community, .storage,
  www/images non cites, tous les .bak et fichiers locaux seuls.

Lecture seule : rien n'est modifie sauf le rapport dans historique\\03_RAPPORTS\\06_MD5\\06_PROD_FONCTIONNELLE.
Code de retour : 0 palier 1 conforme, 1 ecart palier 1, 2 H: injoignable.
"""
import os, sys, re, json, hashlib, fnmatch, shutil, datetime, urllib.request

H = "H:\\"
REBUILD = r"C:\Users\Berry Swann\Documents\ReBuild"
LOC = REBUILD + r"\docs\01_docs_config_system\01_config_system_SH_PY_YAML"
RAPPORTS = REBUILD + r"\historique\03_RAPPORTS\06_MD5\06_PROD_FONCTIONNELLE"
API = "https://api.github.com/repos/BerrySwann/home_assistant_re-build/git/trees/main?recursive=1"

P1_FILES = ["configuration.yaml", "automations.yaml", "scripts.yaml", "sql.yaml",
            "input_button.yaml", "input_datetime.yaml", "input_select.yaml"]
P1_DIRS = ["sensors", "templates", "utility_meter", "command_line", "shell_command", "groups",
           "input_booleans", "input_number", "timers", "scripts", ".scripts"]
P2_NOTIFS_DIR = "notifs"
METEOCONS = ["clear-night", "cloudy", "exceptional", "fog", "hail", "lightning", "lightning-rainy",
             "partlycloudy", "pouring", "rainy", "snowy", "snowy-rainy", "sunny", "windy", "windy-variant"]
ASSETS = ["www/images/meteocons/%s.svg" % n for n in METEOCONS] + [
    "www/images/mini pc.png", "www/images/RPi4B3.png", "www/weather/meteo_france_alerte_nodata.png"]
# Elements presents a la racine de H: et deja classes (dans le manifeste ou volontairement hors manifeste)
KNOWN_ROOT = (P1_FILES + P1_DIRS + [
    "notifs", "Dashboard_*.yaml", "www", "custom_components", ".storage", "docs", "blueprints", "themes",
    "scenes.yaml", "ip_bans.yaml", "secrets.yaml", ".secrets", ".cloud", ".cache", ".git", ".gitignore",
    ".ha_mcp", ".logs", ".vscode", "deps", "tts", ".HA_VERSION", ".ha_run.lock", "README.md",
    "GLOBAL_INDEX_REPO.md", "home-assistant_v2.db*", "home-assistant.log*", ".uuid", ".google.token"])


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def gsha(p):
    b = open(p, "rb").read()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def github_tree():
    try:
        req = urllib.request.Request(API, headers={"User-Agent": "Check_prod_fonctionnelle"})
        t = json.load(urllib.request.urlopen(req, timeout=40))
        if t.get("truncated"):
            return None, "liste GitHub tronquee"
        return {x["path"]: x["sha"] for x in t["tree"] if x["type"] == "blob"}, ""
    except Exception as e:
        return None, "GitHub injoignable (%s)" % e.__class__.__name__


MIR = H + r"docs\01_docs_config_system\01_config_system_SH_PY_YAML"
_IDX = {}


def _index(base):
    """Index (dossier de tete, nom de fichier) -> chemin, hors .bak. Local et miroir rangent chaque
    fichier dans un sous-dossier a son nom (ex. command_line/Audit/x_yaml/x.yaml pour command_line/Audit/x.yaml)."""
    if base in _IDX:
        return _IDX[base]
    idx = {}
    for r, d, f in os.walk(base):
        for x in f:
            if re.search(r"\.bak", x, re.I):
                continue
            p = os.path.join(r, x)
            rel = os.path.relpath(p, base).replace("\\", "/")
            top = rel.split("/", 1)[0] if "/" in rel else ""
            idx.setdefault((top, x), []).append(p)
    _IDX[base] = idx
    return idx


def counterpart(base, rel):
    top = rel.split("/", 1)[0] if "/" in rel else ""
    name = rel.rsplit("/", 1)[-1]
    c = _index(base).get((top, name), [])
    if len(c) > 1:
        # plusieurs homonymes : garder celui dont le dossier parent contient les dossiers du chemin prod
        parts = rel.split("/")[:-1]
        c2 = [p for p in c if all(("/" + q + "/") in p.replace("\\", "/") for q in parts)]
        c = c2 or c
    return c[0] if c else None


PROFOND_DIRS = {
    "automations.yaml": (REBUILD + r"\docs\03_docs_automations\03_docs_automations_YAML\AUTOMATIONS_YAML_ORIGINAL", "AUTOMATIONS"),
    "scripts.yaml": (REBUILD + r"\docs\04_docs_scripts\04_docs_script_ORIGINAL", "SCRIPTS"),
}
PROFOND_RAPPORT = REBUILD + r"\historique\03_RAPPORTS\06_MD5\01_TRIGUL_PROFOND\trigul_profond_%s.txt"


def profond_info(rel):
    """Copie ORIGINAL du jour (la plus recente, faite par le trigul profond) et resultat 'N/M' unite par unite."""
    d, tag = PROFOND_DIRS[rel]
    base = rel[:-5]
    today = datetime.date.today().strftime("%Y_%m_%d")
    cp = None
    if os.path.isdir(d):
        c = sorted(x for x in os.listdir(d) if x.startswith(base + ".bak_" + today + "_") and x.endswith(".yaml"))
        if c:
            cp = d + "\\" + c[-1]
    rep = "?"
    rf = PROFOND_RAPPORT % datetime.date.today().isoformat()
    if os.path.exists(rf):
        for ln in open(rf, encoding="utf-8", errors="ignore"):
            m = re.match(r"^" + tag + r" : (\d+) identiques sur (\d+)", ln)
            if m:
                rep = "%s/%s" % (m.group(1), m.group(2))
                break
    return cp, rep


def local_counterpart(rel):
    return counterpart(LOC, rel)


def mirror_counterpart(rel):
    return counterpart(MIR, rel)


def walk_dir(rel_dir):
    out = []
    base = H + rel_dir
    for r, d, f in os.walk(base):
        d[:] = [x for x in d if x != "__pycache__"]
        for x in f:
            if x.lower().endswith((".pyc",)) or re.search(r"\.bak", x, re.I) or (x.startswith("#") and x.endswith("#")):
                continue
            out.append(os.path.relpath(os.path.join(r, x), H).replace("\\", "/"))
    return out


def main():
    if not os.path.isdir(H):
        print("H: injoignable - palier 1 non verifie")
        return 2
    gh, gh_err = github_tree()
    lines = []
    problems_p1 = []   # ecarts bloquants palier 1
    notes = []

    # ---------------- PALIER 1 ----------------
    p1 = []
    for f in P1_FILES:
        p1.append(f)
    for d in P1_DIRS:
        if not os.path.isdir(H + d):
            problems_p1.append("dossier absent de la prod : %s" % d)
        else:
            p1 += walk_dir(d)
    n_ok = 0
    rows = []        # (rel, P, R, L, M, verdict)
    UNITAIRE = ("automations.yaml", "scripts.yaml")   # comparees unite par unite par le trigul profond
    for rel in p1:
        p = H + rel.replace("/", "\\")
        if not os.path.exists(p):
            problems_p1.append("fichier absent de la prod : %s" % rel)
            rows.append((rel, "-", "?", "?", "?", "ABSENT PROD"))
            continue
        sp = gsha(p)
        sr = (gh.get(rel) if gh is not None else "?") or "-"
        if rel in UNITAIRE:
            # regle d'Eric (2026-10-31) : on ne compare pas H: directement. Le trigul profond copie d'abord le
            # fichier dans le dossier ORIGINAL local, puis compare unite par unite local / copie. Ici : P = la
            # copie du jour, L = resultat unite par unite du rapport profond ; la copie doit egaler H: maintenant.
            cp, rep = profond_info(rel)
            if cp is None:
                sp, sl, sm = "-", "pas de copie du jour", "-"
                problems_p1.append("%s : pas de copie ORIGINAL du jour, lancer le trigul profond d'abord" % rel)
            else:
                same_now = (gsha(cp) == gsha(p))
                if not same_now:
                    problems_p1.append("%s : la prod a change depuis la copie ORIGINAL, relancer le trigul profond" % rel)
                sp = gsha(cp)
                sl, sm = rep, "n/a"
                if not (rep and rep.split("/")[0] == rep.split("/")[-1] and rep != "?"):
                    problems_p1.append("%s : trigul profond, unites non toutes identiques (%s)" % (rel, rep))
        else:
            lp = local_counterpart(rel)
            mp = mirror_counterpart(rel)
            sl = gsha(lp) if lp else "-"
            sm = gsha(mp) if mp else "-"
        vals = [sp, sr, sl, sm]
        comp = [v for v in vals if v not in ("?", "n/a") and not re.match(r"^\d+/\d+$|^pas de copie", v)]
        flag = []
        if "-" in comp:
            flag.append("manquant")
        if len(set(comp)) > 1:
            flag.append("contenus differents")
        if rel not in UNITAIRE and sl not in ("-",) and sl != sp:
            problems_p1.append("prod DIFFERENTE du local : %s" % rel)
        if rel not in UNITAIRE and sm not in ("-",) and sm != sp:
            problems_p1.append("prod racine DIFFERENTE du miroir docs : %s" % rel)
        if sl == "-" and rel not in UNITAIRE:
            problems_p1.append("pas de copie locale : %s" % rel)
        if sm == "-" and rel not in UNITAIRE:
            problems_p1.append("pas de copie miroir docs : %s" % rel)
        if sr == "-":
            notes.append("P1 absent de GitHub : %s" % rel)
        elif sr not in ("?", sp):
            notes.append("P1 GitHub en retard (attend le backup HA) : %s" % rel)
        verdict = "VERT" if not flag else ("A VOIR : " + ", ".join(flag))
        rows.append((rel, sp[:8], sr[:8] if sr not in ("?", "-") else sr, sl[:8] if sl not in ("-",) else sl,
                     sm[:8] if sm not in ("-",) else sm, verdict))
        if not flag:
            n_ok += 1
    # includes de configuration.yaml
    cfg = H + "configuration.yaml"
    inc_total = inc_ok = 0
    if os.path.exists(cfg):
        for ln in open(cfg, encoding="utf-8", errors="ignore"):
            s = ln.strip()
            if s.startswith("#"):
                continue
            m = re.search(r"!include(?:_dir_[a-z_]+)?\s+([^\s#]+)", s)
            if m:
                inc_total += 1
                tgt = H + m.group(1).strip("'\"").rstrip("/").replace("/", "\\")
                if os.path.exists(tgt):
                    inc_ok += 1
                else:
                    problems_p1.append("!include vers un chemin absent : %s" % m.group(1))
    # scripts cites par chemin /config/.scripts/xxx
    sc_total = sc_ok = 0
    refs = set()
    for rel in p1:
        if rel.lower().endswith((".yaml", ".yml", ".sh", ".py")):
            try:
                t = open(H + rel.replace("/", "\\"), encoding="utf-8", errors="ignore").read()
            except Exception:
                continue
            for ln in t.splitlines():
                if ln.lstrip().startswith("#"):
                    continue
                for m in re.findall(r"/config/\.scripts/[A-Za-z0-9_.\-]+\.(?:sh|py)", ln):
                    refs.add(m)
    for r_ in sorted(refs):
        sc_total += 1
        if os.path.exists(H + r_[len("/config/"):].replace("/", "\\")):
            sc_ok += 1
        else:
            problems_p1.append("script cite introuvable : %s" % r_)

    # ---------------- PALIER 2 ----------------
    p2_problems = []
    notifs = []
    if os.path.isdir(H + P2_NOTIFS_DIR):
        for f in sorted(os.listdir(H + P2_NOTIFS_DIR)):
            if f.lower().endswith(".txt"):
                notifs.append(P2_NOTIFS_DIR + "/" + f)
    n_notif_gh = 0
    notif_non_sauv = []
    for rel in notifs:
        if gh is None:
            continue
        if rel in gh:
            n_notif_gh += 1
        else:
            notif_non_sauv.append(rel)
    dash = sorted([f for f in os.listdir(H) if fnmatch.fnmatch(f, "Dashboard_*.yaml")])
    dash_msg = "aucun export Dashboard_*.yaml a la racine"
    if dash:
        dd = dash[-1]
        age = (datetime.date.today() - datetime.date.fromtimestamp(os.path.getmtime(H + dd))).days
        dash_msg = "%s (age %d jour(s))" % (dd, age)
        if gh is not None and gh.get(dd) != gsha(H + dd):
            dash_msg += ", GitHub different ou absent"
    else:
        p2_problems.append("pas d'export dashboard a la racine")

    # ---------------- IMAGES ----------------
    miss_assets = [a for a in ASSETS if not os.path.exists(H + a.replace("/", "\\"))]

    # ---------------- DERIVE ----------------
    new_items = []
    for name in sorted(os.listdir(H)):
        if not any(fnmatch.fnmatch(name, k) for k in KNOWN_ROOT):
            new_items.append(name)

    # ---------------- RAPPORT ----------------
    p1_ok = (not problems_p1) and n_ok == len(p1)
    lines.append("PALIER 1 (vital) : %s - %d fichiers, %d verts (4 colonnes identiques), "
                 "%d !include sur %d resolus, %d scripts cites sur %d presents"
                 % ("OK" if p1_ok and n_ok == len(p1) else "ECART", len(p1), n_ok, inc_ok, inc_total, sc_ok, sc_total))
    for pb in problems_p1:
        lines.append("   ECART P1 : " + pb)
    for nt in notes:
        lines.append("   NOTE : " + nt)
    lines.append("   Colonnes : P prod racine (celle qui tourne) | R GitHub | L local | M prod miroir docs ; "
                 "empreinte git courte, - absent, profond = comparee unite par unite par le trigul profond")
    lines.append("   TREE PROD (98 fichiers qui font tourner la prod, H:\\) :")
    byd = {}
    for rel in p1:
        byd.setdefault(rel.rsplit("/", 1)[0] if "/" in rel else "(racine)", []).append(rel)
    for dname in sorted(byd):
        lines.append("      %s  (%d)" % (dname, len(byd[dname])))
    lines.append("   TABLEAU : P        | R        | L        | M        | verdict | fichier")
    for rel, a, b, c, d_, v in rows:
        lines.append("      %-8s | %-8s | %-8s | %-8s | %s | %s" % (a, b, c, d_, v, rel))
    lines.append("PALIER 2 (donnees) : %s - notifs/*.txt : %d fichiers%s ; export dashboard : %s"
                 % ("OK" if not p2_problems else "ECART", len(notifs),
                    (", %d sur GitHub" % n_notif_gh) if gh is not None else "", dash_msg))
    for pb in p2_problems:
        lines.append("   ECART P2 : " + pb)
    for r_ in notif_non_sauv:
        lines.append("   NON SAUVEGARDE SUR GITHUB : " + r_ + " (ignore par le .gitignore de H:)")
    lines.append("IMAGES du dashboard : %s - %d attendues, %d presentes" % (
        "OK" if not miss_assets else "ECART", len(ASSETS), len(ASSETS) - len(miss_assets)))
    for a in miss_assets:
        lines.append("   IMAGE MANQUANTE : " + a)
    if new_items:
        lines.append("DERIVE : %d element(s) a la racine de H: hors manifeste : %s" % (len(new_items), ", ".join(new_items)))
    else:
        lines.append("DERIVE : aucun element inconnu a la racine de H:")
    if gh is None:
        lines.append("GITHUB : non verifie (%s)" % gh_err)
    lines.append("RESULTAT : palier1=%s palier2=%s images=%s derive=%d" % (
        "OK" if p1_ok else "ECART", "OK" if not p2_problems else "ECART",
        "OK" if not miss_assets else "ECART", len(new_items)))

    head = "CONTROLE PROD FONCTIONNELLE - %s (lecture seule)" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    out = [head] + lines
    print("\n".join(out))
    try:
        os.makedirs(RAPPORTS, exist_ok=True)
        f = RAPPORTS + "\\prod_fonctionnelle_%s.txt" % datetime.date.today().isoformat()
        txt = "\r\n".join(out) + "\r\n"
        if os.path.exists(f):
            old = open(f, "rb").read().decode("utf-8", "ignore").split("\r\n", 1)[1:]
            new = txt.split("\r\n", 1)[1:]
            if old != new:
                shutil.copy2(f, f[:-4] + ".bak_" + datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss") + ".txt")
        open(f, "wb").write(txt.encode("utf-8"))
        print("rapport : " + f)
    except Exception as e:
        print("rapport non ecrit : %s" % e)
    return 0 if p1_ok else 1


if __name__ == "__main__":
    sys.exit(main())
