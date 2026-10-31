# -*- coding: utf-8 -*-
r"""
gen_global_index_automations.py - genere GLOBAL_INDEX_AUTOMATIONS.md

Source de verite des automatisations : H:\automations.yaml (prod) + registre HA
(H:\.storage\core.entity_registry et core.category_registry : entity_id et categorie).
Croise avec les YAML locaux (03_docs_automations_YAML) et les fiches (03_docs_automations_MD).
Lecture seule sur la prod. Ecrit uniquement GLOBAL_INDEX_AUTOMATIONS.md (et sa sauvegarde
locale .bak_AAAA_MM_JJ_HHhMMmSSs avant ecrasement si le contenu change).

Usage : python -I gen_global_index_automations.py [--dry]
  --dry : n'ecrit rien, affiche seulement le resume des ecarts.
"""
import os, re, sys, json, shutil, datetime
from urllib.parse import quote, unquote
import yaml

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild"
DOCS = os.path.join(ROOT, "docs", "03_docs_automations")
YDIR = os.path.join(DOCS, "03_docs_automations_YAML")
MDIR = os.path.join(DOCS, "03_docs_automations_MD")
OUT = os.path.join(DOCS, "GLOBAL_INDEX_AUTOMATIONS.md")
P_AUTO = r"H:\automations.yaml"
P_ENT = r"H:\.storage\core.entity_registry"
P_CAT = r"H:\.storage\core.category_registry"
SKIP_DIRS = {"AUTOMATIONS_YAML_ORIGINAL"}
DRY = "--dry" in sys.argv


def esc(s):
    return str(s).replace("|", "\\|").replace("\r", " ").replace("\n", " ").strip()


def link(label, rel):
    return "[%s](%s)" % (esc(label), quote(rel.replace("\\", "/")))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def header_comments(text):
    """Commentaires utiles du YAML local : ligne id: commentee, TODO, rubrique ETAT."""
    out = []
    m = re.search(r"^(?:-\s+)?id:\s*(?:'[^']*'|\"[^\"]*\"|[^\s#]+)\s+#\s*(.+)$", text, re.M)
    if m:
        out.append(m.group(1).strip())
    head = []
    for ln in text.splitlines():
        if ln.startswith("#"):
            head.append(ln)
        elif ln.strip() == "":
            continue
        else:
            break
    etat = False
    for h in head:
        t = h.lstrip("#").strip()
        if re.match(r"^##\s*ETAT", t, re.I):
            etat = True
            continue
        if t.startswith("##"):
            etat = False
            continue
        if re.search(r"\bTODO\b", t, re.I):
            out.append(t)
        elif etat and t.startswith("- "):
            item = t[2:].strip()
            if item.lower().startswith(("cree le", "entite ha")):
                continue
            out.append(item)
    seen, res = set(), []
    for o in out:
        if o not in seen:
            seen.add(o)
            res.append(o)
    return " ; ".join(res)


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
    for p in (P_AUTO, P_ENT, P_CAT):
        if not os.path.exists(p):
            print("ERREUR : prod non accessible : " + p)
            sys.exit(2)

    prod = yaml.safe_load(read(P_AUTO)) or []
    prod = [a for a in prod if isinstance(a, dict) and a.get("id") is not None]
    ent = json.loads(read(P_ENT))["data"]["entities"]
    by_uid = {str(e["unique_id"]): e for e in ent if e.get("platform") == "automation"}
    cats_raw = json.loads(read(P_CAT))["data"]["categories"]
    cats = {}
    for c in cats_raw.get("automation", []):
        cats[c["category_id"]] = c["name"]

    # YAML locaux
    local = []
    errs = []
    for dp, dn, fn in os.walk(YDIR):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.endswith(".yaml") or ".bak_" in f:
                continue
            path = os.path.join(dp, f)
            text = read(path)
            try:
                data = yaml.safe_load(text)
            except Exception as ex:
                errs.append((path, str(ex)[:80]))
                continue
            if isinstance(data, list):
                data = data[0] if data else {}
            if not isinstance(data, dict):
                continue
            rel = os.path.relpath(path, DOCS)
            local.append({
                "id": str(data["id"]) if data.get("id") is not None else "",
                "alias": str(data.get("alias", "")),
                "rel": rel,
                "cat": rel.split(os.sep)[1],
                "stem": os.path.splitext(f)[0],
                "comment": header_comments(text),
            })
    loc_by_id = {}
    for l in local:
        if l["id"]:
            loc_by_id.setdefault(l["id"], []).append(l)

    # fiches
    fiches = []
    for dp, dn, fn in os.walk(MDIR):
        dn[:] = [d for d in dn if d not in SKIP_DIRS]
        for f in fn:
            if not f.endswith(".md") or ".bak_" in f:
                continue
            path = os.path.join(dp, f)
            rel = os.path.relpath(path, DOCS)
            fiches.append({"rel": rel, "cat": rel.split(os.sep)[1],
                           "stem": os.path.splitext(f)[0], "text": read(path), "used": False})

    def find_fiche(cat, stem, aid, eid):
        cands = [m for m in fiches if m["cat"] == cat]
        for m in cands:
            if m["stem"].lower() == stem.lower():
                return m
        for m in cands:
            if "/" + stem + "/" + stem + ".yaml" in m["text"].replace("\\", "/") or stem + ".yaml" in m["text"]:
                return m
        for m in cands:
            if aid and aid in m["text"]:
                return m
        for m in cands:
            if eid and eid in m["text"]:
                return m
        return None

    rows = []
    sans_yaml, sans_fiche, ecart_id = [], [], []
    for a in prod:
        aid = str(a["id"])
        e = by_uid.get(aid)
        eid = e["entity_id"] if e else ""
        catname = "_SANS_CATEGORIE"
        if e:
            cid = (e.get("categories") or {}).get("automation")
            if cid in cats:
                catname = cats[cid]
        locs = loc_by_id.get(aid, [])
        l = locs[0] if locs else None
        fiche = find_fiche(l["cat"], l["stem"], aid, eid) if l else None
        if fiche:
            fiche["used"] = True
        if not l:
            sans_yaml.append(str(a.get("alias", aid)))
        if not fiche:
            sans_fiche.append(str(a.get("alias", aid)))
        if l and l["id"] != aid:
            ecart_id.append(aid)
        com = l["comment"] if l else ""
        if e and e.get("disabled_by"):
            com = ("DESACTIVEE (%s)" % e["disabled_by"]) + (" ; " + com if com else "")
        rows.append({"cat": catname, "alias": str(a.get("alias", "")), "id": aid,
                     "idl": l["id"] if l else "aucun YAML local", "eid": eid,
                     "fiche": fiche, "loc": l, "com": com})

    def toks(s):
        return [x for x in re.split(r"[^a-z0-9]+", s.lower()) if x]

    def tok_match(a, b):
        return a == b or (len(a) >= 4 and len(b) >= 4 and (a.startswith(b) or b.startswith(a)))

    # 2e passe : fiches dont le nom ne correspond pas exactement (tous les mots du nom de la fiche
    # se retrouvent dans le nom du YAML), parmi les fiches de la meme categorie encore libres
    for r in rows:
        if r["fiche"] or not r["loc"]:
            continue
        ytok = toks(r["loc"]["stem"])
        best, best_key = None, None
        for m in fiches:
            if m["used"] or m["cat"] != r["loc"]["cat"]:
                continue
            mt = toks(m["stem"])
            if len(mt) < 2 or not all(any(tok_match(x, y) for y in ytok) for x in mt):
                continue
            key = (len(mt), -abs(len(ytok) - len(mt)))
            if best_key is None or key > best_key:
                best, best_key = m, key
        if best:
            best["used"] = True
            r["fiche"] = best
            if r["alias"] in sans_fiche:
                sans_fiche.remove(r["alias"])

    prod_ids = {str(a["id"]) for a in prod}
    hors = [l for l in local if l["id"] not in prod_ids]
    sans_entity = [r["alias"] for r in rows if not r["eid"]]
    hors_fiche = {}
    for l in hors:
        fi = find_fiche(l["cat"], l["stem"], l["id"], "")
        hors_fiche[l["rel"]] = fi
        if fi:
            fi["used"] = True
    non_rattachees = [m["rel"] for m in fiches if not m["used"]]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    L.append("# GLOBAL_INDEX_AUTOMATIONS.md - index des automatisations")
    L.append("")
    L.append("Fichier GENERE le %s par docs/04_docs_scripts/04_docs_scripts_SH/gen_global_index_automations/gen_global_index_automations.py. Ne pas modifier a la main : /histo le regenere et ecrase les modifications." % now)
    L.append("")
    L.append("Sources : H:\\automations.yaml (liste et id prod), registre HA (entity_id et categorie), YAML locaux 03_docs_automations_YAML (id local et commentaires), fiches 03_docs_automations_MD. Les liens sont relatifs a ce fichier.")
    L.append("")
    L.append("## Controle")
    L.append("")
    L.append("- Automatisations en prod (automations.yaml) : %d" % len(prod))
    L.append("- YAML locaux unitaires retenus (hors sauvegardes et AUTOMATIONS_YAML_ORIGINAL) : %d" % len(local))
    L.append("- Fiches .md retenues : %d dont %d rattachees a un YAML" % (len(fiches), sum(1 for m in fiches if m["used"])))
    L.append("- Automatisations de la prod sans YAML local : %d%s" % (len(sans_yaml), (" (" + " ; ".join(sans_yaml) + ")") if sans_yaml else ""))
    L.append("- Automatisations de la prod sans fiche rattachee : %d%s" % (len(sans_fiche), (" (" + " ; ".join(sans_fiche) + ")") if sans_fiche else ""))
    L.append("- Automatisations sans entity_id dans le registre HA : %d%s" % (len(sans_entity), (" (" + " ; ".join(sans_entity) + ")") if sans_entity else ""))
    L.append("- YAML locaux absents de la prod ou sans id : %d (voir section Hors prod)" % len(hors))
    L.append("- Erreurs de lecture YAML : %d" % len(errs))
    if non_rattachees:
        L.append("- Fiches non rattachees a un YAML (fiches d'operation, specifications, etc.) : %d" % len(non_rattachees))
        for r in sorted(non_rattachees):
            L.append("  - " + link(r.replace("\\", "/"), r))
    L.append("")

    bycat = {}
    for r in rows:
        bycat.setdefault(r["cat"], []).append(r)
    n = 0
    HEAD = "| N | Alias | id prod | id local (ReBuild) | Entity HA | Documentation (md) | YAML source | Commentaire |"
    SEP = "|:--|:------|:--------|:-------------------|:----------|:-------------------|:------------|:------------|"
    for cat in sorted(bycat, key=lambda s: s.lower()):
        L.append("## %s (%d)" % (esc(cat), len(bycat[cat])))
        L.append("")
        L.append(HEAD)
        L.append(SEP)
        for r in sorted(bycat[cat], key=lambda x: x["alias"].lower()):
            n += 1
            fl = link(os.path.basename(r["fiche"]["rel"]), r["fiche"]["rel"]) if r["fiche"] else "aucune"
            yl = link(os.path.basename(r["loc"]["rel"]), r["loc"]["rel"]) if r["loc"] else "aucun"
            ent_s = "`%s`" % r["eid"] if r["eid"] else "inconnu"
            L.append("| %d | %s | %s | %s | %s | %s | %s | %s |" % (
                n, esc(r["alias"]), r["id"], r["idl"], ent_s, fl, yl, esc(r["com"])))
        L.append("")

    L.append("## Hors prod ou sans id (YAML locaux uniquement) (%d)" % len(hors))
    L.append("")
    L.append("Ces YAML ne correspondent a aucune entree de H:\\automations.yaml (id absent ou inconnu de la prod). Exemple : l'automatisation du ventilateur du Raspberry Pi 4, dont le YAML local n'a pas d'id.")
    L.append("")
    L.append(HEAD)
    L.append(SEP)
    for i, l in enumerate(sorted(hors, key=lambda x: x["alias"].lower()), 1):
        fi = hors_fiche.get(l["rel"])
        fl = link(os.path.basename(fi["rel"]), fi["rel"]) if fi else "aucune"
        L.append("| %d | %s | hors automations.yaml de la prod | %s | - | %s | %s | %s |" % (
            i, esc(l["alias"]), l["id"] or "aucun", fl, link(os.path.basename(l["rel"]), l["rel"]), esc(l["comment"])))
    L.append("")

    content = "\n".join(L)
    ecarts = len(sans_yaml) + len(sans_fiche) + len(sans_entity) + len(ecart_id) + len(errs)
    print("prod=%d local_yaml=%d fiches=%d rattachees=%d hors_prod=%d" % (
        len(prod), len(local), len(fiches), sum(1 for m in fiches if m["used"]), len(hors)))
    print("sans_yaml=%d sans_fiche=%d sans_entity=%d id_different=%d erreurs_yaml=%d" % (
        len(sans_yaml), len(sans_fiche), len(sans_entity), len(ecart_id), len(errs)))
    for lst, nom in ((sans_yaml, "SANS_YAML"), (sans_fiche, "SANS_FICHE"), (sans_entity, "SANS_ENTITY")):
        for x in lst:
            print("  %s : %s" % (nom, x))
    for p, ex in errs:
        print("  ERREUR_YAML : %s : %s" % (p, ex))
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
    content = avec_badges(content, OUT)  # apres le controle des liens
    old = read(OUT) if os.path.exists(OUT) else None
    def norm(s):
        return sans_maj(re.sub(r"Fichier GENERE le \S+ \S+", "Fichier GENERE le X", s.replace("\r\n", "\n")))

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
    print("ecrit : %s (%d lignes, %d ecarts)" % (OUT, len(L), ecarts))


main()
