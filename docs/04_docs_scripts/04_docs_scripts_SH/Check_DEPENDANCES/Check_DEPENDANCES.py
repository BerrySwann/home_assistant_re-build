# -*- coding: utf-8 -*-
"""Check_DEPENDANCES.py - controle en LECTURE SEULE de la fraicheur des 2 fichiers memoire de Claude.

Fichiers controles (docs/00_IA) :
  1. 00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md
  2. 00_IA_GLOBAL_INDEX_memoire/IA_GLOBAL_INDEX_memoire.md
Cree le 2026-10-29 sur demande d'Eric. Ne modifie, ne pousse et ne corrige rien.
Usage : python -I Check_DEPENDANCES.py   (code retour 0 = rien a signaler, 1 = ecarts)
"""
import os, re, sys, unicodedata, datetime

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild"
DOCS = os.path.join(ROOT, "docs")
IA = os.path.join(DOCS, "00_IA")
DEP = os.path.join(IA, "00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire", "DEPENDANCES_GLOBALES_CLAUDE_memoire.md")
IDX = os.path.join(IA, "00_IA_GLOBAL_INDEX_memoire", "IA_GLOBAL_INDEX_memoire.md")
AUTO_PROD = r"H:\automations.yaml"
YAML_DIRS = [
    os.path.join(DOCS, "03_docs_automations", "03_docs_automations_YAML"),
    os.path.join(DOCS, "04_docs_scripts", "04_docs_scripts_YAML"),
    os.path.join(DOCS, "02_docs_dashboard", "02_dashboard_docs_YAML"),
    os.path.join(DOCS, "01_docs_config_system", "01_config_system_SH_PY_YAML"),
]
ecarts = []

def norm(s):
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"[^A-Z0-9]", "", s.upper())

def core(alias):
    a = re.sub(r"\[[^\]]*\]", " ", alias)
    a = re.sub(r"^\s*(\(?[A-Za-z0-9]{1,3}\)?\s*-\s*)+", "", a)
    a = re.sub(r"^\s*(syst[eè]me|P\d)\s*-\s*", "", a, flags=re.I)
    return norm(a)

def lire(p):
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def date_en_tete(txt):
    m = re.search(r"Derni[eè]re mise [àa] jour\s*:\s*(\d{4})-(\d{2})-(\d{2})(?:\s+(\d{1,2})h(\d{2})?)?", txt, re.I)
    if not m:
        return None
    y, mo, d = int(m.group(1)), int(m.group(2)), int(m.group(3))
    h = int(m.group(4) or 0); mi = int(m.group(5) or 0)
    return datetime.datetime(y, mo, d, h, mi)

def fichiers_recents(base, depuis):
    out = []
    for dp, dn, fn in os.walk(base):
        dn[:] = [x for x in dn if x.lower() not in ("__pycache__", "dashboard_complet", "_archive")]
        for n in fn:
            if ".bak" in n.lower() or n.lower().endswith((".pyc", ".tmp")):
                continue
            p = os.path.join(dp, n)
            try:
                if datetime.datetime.fromtimestamp(os.path.getmtime(p)) > depuis:
                    out.append(p)
            except OSError:
                pass
    return out
def controle_dep():
    print("== 1. DEPENDANCES_GLOBALES_CLAUDE_memoire.md ==")
    if not os.path.isfile(DEP):
        ecarts.append("DEP : fichier absent"); print("ABSENT :", DEP); return
    txt = lire(DEP); ntxt = norm(txt)
    dt = date_en_tete(txt)
    print("date en tete :", dt.strftime("%Y-%m-%d %H:%M") if dt else "introuvable")
    if not dt:
        ecarts.append("DEP : date en tete introuvable"); dt = datetime.datetime(2000, 1, 1)
    # a. automations de la prod sans section possible
    if os.path.isfile(AUTO_PROD):
        t = lire(AUTO_PROD); ids = []
        cur = None
        for l in t.splitlines():
            m = re.match(r"^- id:\s*'?([^'\s]+)'?", l)
            if m: cur = m.group(1); continue
            m = re.match(r"^\s{2}alias:\s*(.+)$", l)
            if m and cur:
                ids.append((cur, m.group(1).strip().strip("'\""))); cur = None
        sans = [(i, a) for i, a in ids if core(a)[:16] not in ntxt]
        print("automations dans H:\\automations.yaml :", len(ids), "| sans section retrouvee :", len(sans))
        for i, a in sans:
            print("  - A VERIFIER :", i, "|", a)
            ecarts.append("DEP : automation sans section retrouvee : " + a)
        mt = datetime.datetime.fromtimestamp(os.path.getmtime(AUTO_PROD))
        if mt > dt:
            print("automations.yaml modifie le", mt.strftime("%Y-%m-%d %H:%M"), "apres la date du fichier")
            ecarts.append("DEP : automations.yaml plus recent que la date en tete")
    else:
        print("H:\\automations.yaml inaccessible : controle des automations non fait")
        ecarts.append("DEP : H: inaccessible (automations non controlees)")
    # b. YAML de docs modifies depuis la date en tete
    rec = []
    for b in YAML_DIRS:
        rec += [p for p in fichiers_recents(b, dt) if p.lower().endswith((".yaml", ".yml"))]
    print("YAML de docs modifies apres la date en tete :", len(rec))
    for p in rec[:40]:
        print("  -", p.replace(ROOT + os.sep, ""))
        ecarts.append("DEP : YAML plus recent que la date en tete : " + os.path.basename(p))
    # c. chemins cites qui n'existent plus
    morts = set()
    for l in txt.splitlines():
        if "\u26d4" in l or re.search(r"retir|absent|introuvable|supprim", l, re.I):
            continue
        for m in re.finditer(r"`(docs/[^`\s]+\.(?:yaml|md|py|sh))`", l):
            p = os.path.join(ROOT, *m.group(1).split("/"))
            if not os.path.exists(p): morts.add(m.group(1))
    print("chemins docs/ cites qui n'existent pas :", len(morts))
    for p in sorted(morts)[:40]:
        print("  - MORT :", p); ecarts.append("DEP : chemin mort : " + p)

def controle_idx():
    print("== 2. IA_GLOBAL_INDEX_memoire.md ==")
    if not os.path.isfile(IDX):
        ecarts.append("IDX : fichier absent"); print("ABSENT :", IDX); return
    txt = lire(IDX); mt = os.path.getmtime(IDX)
    print("modifie le", datetime.datetime.fromtimestamp(mt).strftime("%Y-%m-%d %H:%M"))
    manque, recents = [], []
    for dp, dn, fn in os.walk(IA):
        dn[:] = [x for x in dn if x.lower() != "__pycache__"]
        for n in fn:
            p = os.path.join(dp, n)
            if p == IDX or ".bak" in n.lower() or not n.lower().endswith(".md"):
                continue
            if os.path.dirname(p) == os.path.dirname(IDX):
                continue
            if n not in txt: manque.append(os.path.relpath(p, IA))
            if os.path.getmtime(p) > mt: recents.append(os.path.relpath(p, IA))
    print("fichiers .md de docs/00_IA absents de l'index :", len(manque))
    for p in manque: print("  - ABSENT DE L'INDEX :", p); ecarts.append("IDX : absent de l'index : " + p)
    print("fichiers modifies apres l'index :", len(recents))
    for p in recents: print("  - PLUS RECENT QUE L'INDEX :", p); ecarts.append("IDX : plus recent que l'index : " + p)
    if manque or recents:
        print("  -> relancer Gen_GLOBAL_INDEX_ia.py (regeneration, jamais a la main)")

if __name__ == "__main__":
    print("Check_DEPENDANCES - lecture seule -", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    controle_dep(); controle_idx()
    print("== RESULTAT :", "ecarts=%d" % len(ecarts), "| OK" if not ecarts else "| A TRAITER (voir ci-dessus)")
    sys.exit(1 if ecarts else 0)