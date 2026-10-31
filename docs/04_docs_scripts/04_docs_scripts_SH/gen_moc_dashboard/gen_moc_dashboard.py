# -*- coding: utf-8 -*-
"""gen_moc_dashboard.py - genere MOC_DASHBOARD.md (regle d'Eric du 2026-10-28 : 1 YAML = 1 fiche .md).

Perimetre : docs/02_docs_dashboard/02_dashboard_docs_YAML (.yaml/.yml) hors sauvegardes .bak,
dossiers XX_, Dashboard_COMPLET, *_ORIGINAL, *_archive*. Pour chaque YAML, cherche sa fiche .md dans
02_dashboard_docs_MD : meme nom (insensible a la casse et aux separateurs), sinon fiche de la meme
cellule (puis de tout l'arbre) qui cite le nom du fichier YAML. Ecrit uniquement MOC_DASHBOARD.md
(sauvegarde .bak_AAAA_MM_JJ_HHhMMmSSs.md si le contenu change, rien d'ecrit si identique).
Usage : python -I -X utf8 gen_moc_dashboard.py [--dry]
"""
import os, re, sys, datetime, urllib.parse

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild"
DOCS = os.path.join(ROOT, "docs", "02_docs_dashboard")
YD = os.path.join(DOCS, "02_dashboard_docs_YAML")
MD = os.path.join(DOCS, "02_dashboard_docs_MD")
OUT = os.path.join(DOCS, "MOC_DASHBOARD.md")
SKIP = re.compile(r"(^|[\\/])(XX_[^\\/]*|Dashboard_COMPLET|[^\\/]*_ORIGINAL|[^\\/]*_archive[^\\/]*)([\\/]|$)", re.I)

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def walk(root, exts):
    res = []
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if ".bak" in f.lower() or os.path.splitext(f)[1].lower() not in exts:
                continue
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, root)
            if SKIP.search(rel):
                continue
            res.append((full, rel))
    return sorted(res, key=lambda t: t[1].lower())

def link(label, full):
    rel = os.path.relpath(full, DOCS).replace("\\", "/")
    return "[%s](%s)" % (label, urllib.parse.quote(rel, safe="/"))

def cell_of(rel):
    return rel.split(os.sep)[0]

def code_of(cell):
    m = re.match(r"(L\d+C\d+)", cell)
    return m.group(1) if m else cell

def slot_of(rel):
    parts = rel.split(os.sep)
    if len(parts) >= 3:
        s = parts[1].lower()
        if re.search(r"(^|_)01_(l\d+c\d+_)?vignette", s):
            return "v"
        if re.search(r"(^|_)0[2-9]_(l\d+c\d+_)?page", s):
            return "p"
    return "o"

def avec_badges(texte, path):
    """Banniere des 8 badges via Check_badges_fiches.reconstruire (regle unique, ordre d'Eric le 2026-10-31 : badges partout sauf .bak). 00_IA et 05_docs_skills restent exemptes."""
    sys.path.insert(0, r"C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_badges_fiches")
    import Check_badges_fiches as cb
    rel = os.path.relpath(path, r"C:\Users\Berry Swann\Documents\ReBuild\docs")
    if cb.SKIP.search(rel):
        return texte
    ha = cb.ha_version()
    if not ha:
        print("ATTENTION : H:\\.HA_VERSION illisible, badge HA absent pour " + rel)
    nt = cb.reconstruire(texte, {}, cb.ORDRE, rel, ha)
    if nt is None:
        print("ATTENTION : badges non ajoutes pour " + rel)
        return texte
    return nt


def sans_maj(s):
    return re.sub(r"M.J-\d{4}--\d{2}--\d{2}", "MaJ-X", s)

def main():
    dry = "--dry" in sys.argv
    ys = walk(YD, {".yaml", ".yml"})
    ms = walk(MD, {".md"})
    mtext = {}
    for full, rel in ms:
        try:
            mtext[full] = open(full, encoding="utf-8", errors="replace").read().lower()
        except OSError:
            mtext[full] = ""
    used = set()
    # Rattachements manuels decides par Eric le 2026-10-28 (L0C0 03_Carte meteo) : YAML -> fiche, et fichiers non YAML -> fiche
    MC = "L0C0_PAGE_Home" + os.sep + "03_Carte m\u00e9t\u00e9o"
    FORCE = {"card_meteocss_home.yaml": os.path.join(MD, MC, "Carte m\u00e9t\u00e9o vence.md")}
    ASSOC = [("Meteocss-card.js (carte HACS modifiee)", os.path.join(YD, MC, "Meteocss-card.js"), os.path.join(MD, MC, "Meteocss_card_modif.md"), "fichier JS de la carte meteocss (HACS), range avec la carte ; sa fiche Meteocss_card_modif.md decrit la modification manuelle du JS, nom different du fichier"),
             ("Www_meteocons (SVG animes)", os.path.join(YD, MC, "Www_meteocons"), os.path.join(MD, MC, "www_meteocons", "Meteocons_install.md"), "dossier des icones meteo SVG animees, range avec la carte ; sa fiche Meteocons_install.md decrit leur installation, nom different du dossier")]

    def find(yfull, yrel):
        fm = FORCE.get(os.path.basename(yfull).lower())
        if fm and os.path.exists(fm):
            return fm, "rattachement manuel"
        stem = os.path.splitext(os.path.basename(yfull))[0]
        key = norm(stem)
        cell = cell_of(yrel)
        same = [m for m in ms if cell_of(m[1]) == cell]
        for pool in (same, ms):
            for full, rel in pool:
                if norm(os.path.splitext(os.path.basename(full))[0]) == key:
                    return full, "nom"
        name = os.path.basename(yfull).lower()
        for pool in (same, ms):
            for full, rel in pool:
                if name in mtext[full]:
                    return full, "chemin cite"
        return None, ""

    rows = []
    for yfull, yrel in ys:
        mfull, how = find(yfull, yrel)
        if mfull:
            used.add(mfull)
        rows.append({"yfull": yfull, "yrel": yrel, "cell": cell_of(yrel), "code": code_of(cell_of(yrel)),
                     "slot": slot_of(yrel), "md": mfull, "how": how})
    cells = {}
    for r in rows:
        cells.setdefault(r["cell"], []).append(r)
    n_ok = sum(1 for r in rows if r["md"])
    n_ko = len(rows) - n_ok
    NOTES = {
        "L1C1": [("Note : TUTO_L1C1_images_alertes_meteo_france", os.path.join(MD, "L1C1_METEO", "TUTO_L1C1_images_alertes_meteo_france.md"),
                  "tutoriel pour produire les images des alertes Meteo France (command_line/meteo/carte_meteo_france.yaml), utilise par le pop-up alerte de la page meteo ; pas de YAML du meme nom")],
        "L2C1": [("Note : COULEURS_PRISES_PAR_PIECE", os.path.join(MD, "L2C1_ENERGIE_GENERALE", "COULEURS_PRISES_PAR_PIECE.md"),
                  "palette de couleurs par piece pour harmoniser les cartes des prises connectees (graphiques et onglets de la page energie) ; note de reference sans YAML, cite d'anciens noms de YAML")],
        "L2C3": [("Note : Couleurs_eclairage_par_piece", os.path.join(MD, "L2C3_ENERGIE_ECLAIRAGE", "Couleurs_eclairage_par_piece.md"),
                  "palette officielle des 10 pieces pour harmoniser les couleurs des cartes eclairage ; note de reference sans YAML")],
    }
    for _c, _lst in NOTES.items():
        for _lab, _mdf, _expl in _lst:
            if os.path.exists(_mdf):
                used.add(_mdf)
    assoc_rows = []
    for lab, src, mdf, expl in ASSOC:
        ok_src = os.path.exists(src)
        ok_md = os.path.exists(mdf)
        if ok_md:
            used.add(mdf)
        assoc_rows.append((lab, src, mdf, ok_src, ok_md, expl))
    orphan = [m for m in ms if m[0] not in used]

    L = []
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L.append("# MOC_DASHBOARD.md - 1 YAML = 1 fiche .md (dashboard)")
    L.append("")
    L.append("GENEREDATE Genere par docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_dashboard/gen_moc_dashboard.py. Ne pas modifier a la main : le script ecrase les modifications.")
    L.append("")
    L.append("Regle d'Eric (2026-10-28) : chaque YAML de docs/02_docs_dashboard (hors Dashboard_COMPLET) a sa fiche .md. Le rapprochement se fait par le nom du fichier, sinon par une fiche de la meme cellule qui cite le fichier YAML, sinon par un rattachement manuel (table FORCE du script). Sous la ligne de chaque page ou vignette figurent toutes les cartes (autres YAML) de la meme cellule avec leur fiche (Page.md). Sont ignores : sauvegardes .bak, dossiers XX_, Dashboard_COMPLET, *_ORIGINAL, *_archive*, et les fichiers qui ne sont pas des YAML (.js, .svg, .sh). Les liens sont relatifs a ce fichier.")
    L.append("")
    L.append("## Controle")
    L.append("")
    L.append("- YAML suivis : %d" % len(rows))
    L.append("- YAML avec fiche : %d" % n_ok)
    L.append("- YAML sans fiche (MANQUANT) : %d" % n_ko)
    L.append("- Fiches .md sans YAML correspondant (tutos, fiches renommees, etc.) : %d" % len(orphan))
    L.append("")
    L.append("## Vignettes et pages")
    L.append("")
    L.append("| Code | Cellule | Vignette | Vignette.md | Page | Page.md |")
    L.append("|:-----|:--------|:---------|:------------|:-----|:--------|")
    for ci, cell in enumerate(sorted(cells, key=lambda c: (code_of(c)))):
        if ci > 0:
            L.append("| <br> |  |  |  |  |  |")
        rs = cells[cell]
        v = [r for r in rs if r["slot"] == "v"]
        p = [r for r in rs if r["slot"] == "p"]
        o = [r for r in rs if r["slot"] == "o"]
        first = True
        for i in range(max(len(v), len(p))):
            vi = v[i] if i < len(v) else None
            pi = p[i] if i < len(p) else None
            vy = link(os.path.basename(vi["yfull"]), vi["yfull"]) if vi else "-"
            vm = ("Vignette.md OK " + link("fiche", vi["md"])) if vi and vi["md"] else ("Vignette.md MANQUANT" if vi else "-")
            py = link(os.path.basename(pi["yfull"]), pi["yfull"]) if pi else "-"
            pm = ("Page.md OK " + link("fiche", pi["md"])) if pi and pi["md"] else ("Page.md MANQUANT" if pi else "-")
            L.append("| %s | %s | %s | %s | %s | %s |" % (code_of(cell) if first else "", cell if first else "", vy, vm, py, pm))
            first = False
        for r in o:
            suf = " (par chemin cite)" if r["how"] == "chemin cite" else (" (rattachement manuel : fiche Carte meteo vence.md, nom different du YAML)" if r["how"] == "rattachement manuel" else "")
            cm = ("Page.md OK " + link("fiche", r["md"]) + suf) if r["md"] else "Page.md MANQUANT"
            L.append("| %s | %s | - | - | %s | %s |" % (code_of(cell) if first else "", cell if first else "", link(os.path.basename(r["yfull"]), r["yfull"]), cm))
            first = False
            if os.path.basename(r["yfull"]).lower() == "card_meteocss_home.yaml":
                for lab, src, mdf, ok_src, ok_md, expl in assoc_rows:
                    am = ("Page.md OK " + link("fiche", mdf) + " (rattachement manuel : " + expl + ")") if ok_md else "Page.md MANQUANT"
                    L.append("|  |  | - | - | %s | %s |" % (link(lab, src) if ok_src else lab + " (ABSENT)", am))
        for _lab, _mdf, _expl in NOTES.get(code_of(cell), []):
            _am = ("Page.md OK " + link("fiche", _mdf) + " (rattachement manuel : " + _expl + ")") if os.path.exists(_mdf) else "Page.md MANQUANT"
            L.append("|  |  | - | - | %s | %s |" % (_lab, _am))
    L.append("")
    L.append("## Fiches sans YAML correspondant")
    L.append("")
    if orphan:
        for full, rel in orphan:
            L.append("- %s" % link(rel.replace("\\", "/"), full))
    else:
        L.append("- aucune")
    L.append("")
    text = "\n".join(L)
    stamp_line = lambda t: "\n".join(l for l in t.split("\n") if not l.startswith("GENEREDATE") and not l.startswith("Genere le "))
    final = text.replace("GENEREDATE", "Genere le " + now + ".")
    final = avec_badges(final, OUT)
    print("yaml=%d avec_fiche=%d sans_fiche=%d fiches_sans_yaml=%d" % (len(rows), n_ok, n_ko, len(orphan)))
    for r in rows:
        if not r["md"]:
            print("  MANQUANT : " + r["yrel"])
    if dry:
        print("--dry : rien d'ecrit")
        return
    old = open(OUT, encoding="utf-8", newline="").read() if os.path.exists(OUT) else None
    if old is not None:
        a = sans_maj("\n".join(l for l in old.split("\n") if not l.startswith("Genere le ")))
        b = sans_maj("\n".join(l for l in final.split("\n") if not l.startswith("Genere le ")))
        if a == b:
            print("MOC identique : rien d'ecrit")
            return
        bak = OUT[:-3] + ".bak_" + datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss") + ".md"
        open(bak, "w", encoding="utf-8", newline="").write(old)
        print("sauvegarde : " + bak)
    open(OUT, "w", encoding="utf-8", newline="").write(final)
    print("ecrit : %s (%d lignes)" % (OUT, final.count("\n") + 1))

if __name__ == "__main__":
    main()