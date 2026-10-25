# -*- coding: utf-8 -*-
r"""
gen_global_index_vignettes_pages.py - genere GLOBAL_INDEX_VIGNETTES_PAGES.md

Index des vignettes (LxCy) et des pages du dashboard, construit a partir de l'arbre local
docs/02_docs_dashboard (02_dashboard_docs_MD et 02_dashboard_docs_YAML). Lecture seule sur tout
sauf le fichier de sortie (et sa sauvegarde locale .bak_AAAA_MM_JJ_HHhMMmSSs.md avant
ecrasement si le contenu change). Dashboard_COMPLET n'est jamais lu ni modifie.

Usage : python -I gen_global_index_vignettes_pages.py [--dry]
"""
import os, re, sys, shutil, datetime
from urllib.parse import quote, unquote

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild"
DOCS = os.path.join(ROOT, "docs", "02_docs_dashboard")
MDIR = os.path.join(DOCS, "02_dashboard_docs_MD")
YDIR = os.path.join(DOCS, "02_dashboard_docs_YAML")
DEP = os.path.join(ROOT, "docs", "XX_docs_MD_system", "DEPENDANCES_GLOBALES", "DEPENDANCES_GLOBALES.md")
OUT = os.path.join(DOCS, "GLOBAL_INDEX_VIGNETTES_PAGES.md")
SKIP = {"Dashboard_COMPLET"}
DRY = "--dry" in sys.argv


def esc(s):
    return str(s).replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def link(label, rel):
    return "[%s](%s)" % (esc(label), quote(rel.replace("\\", "/")))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def cell(lst):
    return "<br>".join(link(os.path.basename(x), x) for x in lst) if lst else "-"


def collect(root, kind, groups):
    for d in sorted(os.listdir(root)):
        full = os.path.join(root, d)
        if not os.path.isdir(full) or d in SKIP:
            continue
        m = re.match(r"^(L\d+C\d+)", d)
        key = m.group(1) if m else d
        g = groups.setdefault(key, {"md": {"v": [], "p": [], "o": []}, "yaml": {"v": [], "p": [], "o": []}, "dirs": {}})
        g["dirs"][kind] = d
        for dp, dn, fn in os.walk(full):
            for f in sorted(fn):
                if ".bak_" in f or f.endswith(".bak"):
                    continue
                rel = os.path.relpath(os.path.join(dp, f), DOCS)
                parts = rel.split(os.sep)
                sub = parts[2] if len(parts) > 3 else ""
                sl = sub.lower()  # insensible a la casse (01_Vignette, 01_L1C1_Vignette ; corrige le 2026-10-18)
                slot = "v" if re.search(r"(^|_)01_(l\d+c\d+_)?vignette", sl) else ("p" if re.search(r"(^|_)02_(l\d+c\d+_)?page", sl) else "o")
                g[kind][slot].append(rel)


def title_of(g):
    for rel in g["md"]["v"] + g["md"]["p"]:
        if rel.endswith(".md"):
            for ln in read(os.path.join(DOCS, rel)).splitlines()[:60]:
                if ln.startswith("# "):
                    return ln[2:].strip()
    return g["dirs"].get("md") or g["dirs"].get("yaml") or ""


def main():
    for p in (MDIR, YDIR):
        if not os.path.isdir(p):
            print("ERREUR : dossier absent : " + p)
            sys.exit(2)
    groups = {}
    collect(MDIR, "md", groups)
    collect(YDIR, "yaml", groups)
    dep = read(DEP) if os.path.exists(DEP) else ""
    keys = sorted(groups, key=lambda k: (not re.match(r"^L\d+C\d+$", k), k))
    vign = [k for k in keys if re.match(r"^L[1-9]C\d+$", k)]

    manque = {"fiche vignette": [], "YAML vignette": [], "fiche page": [], "YAML page": []}
    seul_md, seul_yaml = [], []
    for k in vign:
        g = groups[k]
        for lab, kind, slot in (("fiche vignette", "md", "v"), ("YAML vignette", "yaml", "v"),
                                ("fiche page", "md", "p"), ("YAML page", "yaml", "p")):
            if not g[kind][slot]:
                manque[lab].append(k)
    for k in keys:
        g = groups[k]
        if "md" in g["dirs"] and "yaml" not in g["dirs"]:
            seul_md.append(k)
        if "yaml" in g["dirs"] and "md" not in g["dirs"]:
            seul_yaml.append(k)
    sans_dep = [k for k in vign if not re.search(r"\b%s\b" % k, dep)]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = ["# GLOBAL_INDEX_VIGNETTES_PAGES.md - index des vignettes et des pages du dashboard", ""]
    L.append("Fichier GENERE le %s par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_vignettes_pages/gen_global_index_vignettes_pages.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications." % now)
    L.append("")
    L.append("Source : arbre local docs/02_docs_dashboard (02_dashboard_docs_MD et 02_dashboard_docs_YAML), sauvegardes .bak_ exclues, Dashboard_COMPLET non detaille. Les liens sont relatifs a ce fichier. La colonne Dependances indique si le code de la vignette est cite dans DEPENDANCES_GLOBALES.md.")
    L.append("")
    L.append("## Controle")
    L.append("")
    L.append("- Vignettes detectees (L1C1 a L6C3) : %d ; dossiers au total (avec PAGE_Home et autres pages) : %d" % (len(vign), len(keys)))
    for lab, lst in manque.items():
        L.append("- Vignettes sans %s : %d%s" % (lab, len(lst), (" (" + ", ".join(lst) + ")") if lst else ""))
    L.append("- Dossiers presents seulement cote MD : %d%s" % (len(seul_md), (" (" + ", ".join(seul_md) + ")") if seul_md else ""))
    L.append("- Dossiers presents seulement cote YAML : %d%s" % (len(seul_yaml), (" (" + ", ".join(seul_yaml) + ")") if seul_yaml else ""))
    L.append("- Vignettes dont le code n'apparait pas dans DEPENDANCES_GLOBALES.md : %d%s" % (len(sans_dep), (" (" + ", ".join(sans_dep) + ")") if sans_dep else ""))
    L.append("")
    L.append("## Vignettes et pages")
    L.append("")
    L.append("| Code | Titre | Fiche vignette | YAML vignette | Fiche page | YAML page | Autres fichiers (cartes, tutos, YAML annexes) | Dependances |")
    L.append("|:-----|:------|:---------------|:--------------|:-----------|:----------|:----------------------------------------------|:------------|")
    for k in keys:
        g = groups[k]
        autres = g["md"]["o"] + g["yaml"]["o"]
        dp = "oui" if re.search(r"\b%s\b" % re.escape(k), dep) else "non"
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s |" % (
            esc(k), esc(title_of(g)), cell(g["md"]["v"]), cell(g["yaml"]["v"]),
            cell(g["md"]["p"]), cell(g["yaml"]["p"]), cell(autres), dp))
    L.append("")
    content = "\n".join(L)
    print("vignettes=%d dossiers=%d" % (len(vign), len(keys)))
    print("manques : " + "; ".join("%s=%d" % (a, len(b)) for a, b in manque.items()) +
          " | seul_md=%d seul_yaml=%d sans_dependances=%d" % (len(seul_md), len(seul_yaml), len(sans_dep)))
    ko = []
    nb = 0
    for mm in re.finditer(r"\]\(([^)]+)\)", content):
        nb += 1
        rel = unquote(mm.group(1))
        if not os.path.exists(os.path.join(DOCS, rel.replace("/", os.sep))):
            ko.append(rel)
    print("liens=%d casses=%d" % (nb, len(ko)))
    for x in ko[:20]:
        print("  LIEN_CASSE : " + x)
    if DRY:
        print("--dry : rien ecrit")
        return
    old = read(OUT) if os.path.exists(OUT) else None

    def norm(s):
        return re.sub(r"Fichier GENERE le \S+ \S+", "Fichier GENERE le X", s.replace("\r\n", "\n"))

    if old is not None and norm(old) == norm(content):
        print("inchange : fichier deja a jour")
        return
    if old is not None:
        stamp = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")
        bak = OUT[:-3] + ".bak_" + stamp + ".md"
        shutil.copy2(OUT, bak)
        print("sauvegarde : " + bak)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("ecrit : %s (%d lignes)" % (OUT, len(L)))


main()
