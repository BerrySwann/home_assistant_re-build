#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hermes_gen_dependances.py - generateur de DEPENDANCES_GLOBALES_HERMES_V1.md
# Ecrit le 2026-10-25 par Hermes, sur ordre d'Eric (relayant Claude) : l'ancien generateur
# hermes_gen_dependances.py n'existait plus sur le disque. Celui-ci est une RECONSTRUCTION
# a partir de l'arbre local ReBuild. Il ne pretend pas reproduire a l'identique l'ancien :
# il produit la meme structure de sections, avec des regles explicites ci-dessous.
#
# Lecture : tout le local ReBuild/docs. Ecriture : UNIQUEMENT le fichier de sortie, en local.
# Rien en prod, rien sur GitHub.
#
# Usage : python -I -X utf8 hermes_gen_dependances.py [--out CHEMIN]
import os, re, sys, json, datetime, collections, hashlib

BASE = os.path.join("C:" + chr(92), "Users", "Berry Swann", "Documents", "ReBuild")
DOCS = os.path.join(BASE, "docs")
DASH = os.path.join(DOCS, "02_docs_dashboard", "02_dashboard_docs_YAML")
CFG = os.path.join(DOCS, "01_docs_config_system", "01_config_system_SH_PY_YAML")
AUTO = os.path.join(DOCS, "03_docs_automations", "03_docs_automations_YAML")
SH = os.path.join(DOCS, "04_docs_scripts", "04_docs_scripts_SH")
OUT_DEFAUT = os.path.join(DOCS, "99_docs_MD_system", "DEPENDANCES_GLOBALES_HERMES",
                          "DEPENDANCES_GLOBALES_HERMES_V1.md")
ANN_DEFAUT = os.path.join(BASE, "scripts", "annotations_v1.json")
SKIP = re.compile(r"\.bak")
DOMAINES = ("binary_sensor sensor switch light climate input_boolean input_number input_select "
            "input_datetime input_button person device_tracker sun weather script automation group "
            "media_player button number select fan cover lock camera update text time date todo image "
            "event humidifier water_heater vacuum remote siren valve alarm_control_panel notify timer "
            "counter zone scene").split()
RX_ENT = re.compile(r"\b(" + "|".join(sorted(DOMAINES, key=len, reverse=True)) + r")\.([a-z0-9_]{2,})")
RX_CARTE = re.compile(r"^\s*-?\s*type:\s*[a-z_\-]+", re.M)


def fichiers(racine, ext=(".yaml", ".yml")):
    out = []
    for dp, dn, fn in os.walk(racine):
        dn[:] = [d for d in dn if d != "__pycache__"]
        for f in fn:
            if SKIP.search(f):
                continue
            if os.path.splitext(f)[1].lower() in ext:
                out.append(os.path.join(dp, f))
    return sorted(out)


def lire(p):
    try:
        return open(p, encoding="utf-8", errors="replace").read()
    except OSError:
        return ""


def rel(p, depuis=DOCS):
    return os.path.relpath(p, depuis).replace(chr(92), "/")


def nettoie(texte):
    """Retire les commentaires YAML/Python avant de chercher des entites : un commentaire qui
    cite une entite supprimee (cas binary_sensor.meteoalarm, c20261025-01) ne doit pas la faire
    revivre dans le document."""
    out = []
    for ligne in texte.split("\n"):
        s = ligne.lstrip()
        if s.startswith("#"):
            continue
        i = ligne.find(" #")
        if i > 0:
            ligne = ligne[:i]
        out.append(ligne)
    return "\n".join(out)


def entites(texte):
    return {"%s.%s" % (d, o) for d, o in RX_ENT.findall(nettoie(texte))}


# ---------- 1. index des definitions (qui definit quelle entite) ----------
def index_definitions():
    types = {"templates": "TPL", "sensors": "SEN", "utility_meter": "UM", "command_line": "NAT"}
    defs = {}
    for p in fichiers(CFG):
        txt = lire(p)
        relp = rel(p, CFG)
        sous = relp.split("/")[0]
        typ = types.get(sous, "NAT")
        for e in entites(txt):
            defs.setdefault(e, (typ, relp))
    return defs


_CACHE_PROD = {}


def etat_prod(relp):
    """Statut d'un fichier de config face a la prod H: (meme arborescence sous H:\\<1er segment>).
    Rend (chemin prod, statut) ; statut = identique | different | absent | prod inaccessible."""
    if relp in _CACHE_PROD:
        return _CACHE_PROD[relp]
    morceaux = relp.split("/")
    p_prod = os.path.join("H:" + chr(92), *morceaux)
    res = (p_prod, "prod inaccessible")
    if os.path.isdir("H:" + chr(92)):
        if not os.path.exists(p_prod):
            res = (p_prod, "absent en prod")
        else:
            try:
                a = hashlib.md5(open(os.path.join(CFG, *morceaux), "rb").read()).hexdigest()
                b = hashlib.md5(open(p_prod, "rb").read()).hexdigest()
                res = (p_prod, "identique" if a == b else "different")
            except OSError:
                res = (p_prod, "illisible")
    _CACHE_PROD[relp] = res
    return res


# ---------- 2. vignettes ----------
def vignettes():
    out = []
    if not os.path.isdir(DASH):
        return out
    for d in sorted(os.listdir(DASH)):
        chemin = os.path.join(DASH, d)
        if not os.path.isdir(chemin) or not re.match(r"L\dC\d_", d):
            continue
        code, nom = d.split("_", 1)
        ents, cartes, yamls = set(), 0, []
        for p in fichiers(chemin):
            # L0C0 : Page_Home.yaml est le dashboard COMPLET et reference tout ; il n'est pas
            # compte, sinon les 18 autres vignettes sont absorbees dans L0C0 (regle de l'ancien
            # document, ou L0C0 ne compte que ses cartes permanentes).
            if code == "L0C0" and os.path.basename(p).startswith("Page_"):
                continue
            txt = lire(p)
            ents |= entites(txt)
            cartes += len(RX_CARTE.findall(txt))
            yamls.append(rel(p))
        out.append({"code": code, "nom": nom, "entites": ents, "cartes": cartes, "yaml": yamls,
                    "dossier": rel(chemin)})
    return out


# ---------- 3. automations, scripts, sh ----------
def automations():
    out = []
    if not os.path.isdir(AUTO):
        return out
    for pole in sorted(os.listdir(AUTO)):
        p = os.path.join(AUTO, pole)
        if not os.path.isdir(p) or pole.startswith("XX_"):
            continue
        files = fichiers(p)
        ents = set()
        alias = []
        for f in files:
            txt = lire(f)
            ents |= entites(txt)
            alias += re.findall(r"^\s*-?\s*alias:\s*[\"']?(.+?)[\"']?\s*$", txt, re.M)
        out.append({"pole": pole, "fichiers": len(files), "entites": ents,
                    "alias": [a for a in alias if a.strip()]})
    return out


def scripts_racine():
    out = {"sh": [], "autre": []}
    if not os.path.isdir(SH):
        return out
    for dp, dn, fn in os.walk(SH):
        dn[:] = [d for d in dn if d != "__pycache__"]
        for f in fn:
            if SKIP.search(f):
                continue
            p = os.path.join(dp, f)
            ext = os.path.splitext(f)[1].lower()
            if ext in (".sh", ".py"):
                cible = out["sh"] if ext == ".sh" else out["autre"]
                cible.append((rel(p), entites(lire(p))))
    out["sh"].sort()
    out["autre"].sort()
    return out


def main():
    out_path = OUT_DEFAUT
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]

    defs = index_definitions()
    vigs = vignettes()
    autos = automations()
    scr = scripts_racine()
    ann = {}
    if os.path.exists(ANN_DEFAUT):
        try:
            ann = json.load(open(ANN_DEFAUT, encoding="utf-8"))
        except (OSError, ValueError):
            ann = {}

    utilises = set()
    for v in vigs:
        utilises |= v["entites"]
    for a in autos:
        utilises |= a["entites"]
    for groupe in ("sh", "autre"):
        for _p, e in scr[groupe]:
            utilises |= e

    orphelines = sorted(e for e in defs if e not in utilises)

    L = []
    L.append("# DEPENDANCES GLOBALES HERMES - TABLEAU DE BORD HA")
    L.append("*Genere par `ReBuild/scripts/hermes_gen_dependances.py` (reconstruction Hermes du "
             "2026-10-25) a partir de l'arbre local : vignettes dashboard, scripts, automations par "
             "pole, orphelines. Types deduits de l'emplacement du fichier de definition.*")
    L.append("")
    L.append("*Genere le %s. Regles : une entite est rattachee a une vignette si son identifiant "
             "apparait dans un YAML de son dossier ; une carte est une ligne `type: ...` ; une entite "
             "est ORPHELINE si elle est definie dans la config et n'apparait ni dans un dashboard, ni "
             "dans une automation, ni dans un script.*" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    L.append("")
    L.append("## LEGENDE")
    L.append("")
    L.append("| Symbole | Signification |")
    L.append("|:-------:|:-------------|")
    L.append("| [type] | Type de carte |")
    L.append("| (TPL) | Entite definie dans templates/ |")
    L.append("| (SEN) | Entite definie dans sensors/ |")
    L.append("| (UM) | Entite definie dans utility_meter/ |")
    L.append("| (NAT) | Entite native/UI, command_line, ou fichier non classe |")
    L.append("| ORPHELINE | Entite dans aucun dashboard, automation ni script |")
    L.append("")
    L.append("## MATRICE DES VIGNETTES")
    L.append("")
    L.append("| ID | Vignette | Entites | Cartes |")
    L.append("|:---|:---------|:-------:|:------:|")
    for v in vigs:
        L.append("| **%s** | %s | %d | %d |" % (v["code"], v["nom"], len(v["entites"]), v["cartes"]))
    L.append("")
    L.append("## SOMMAIRE")
    L.append("")
    L.append("- 1. Vignettes dashboard, par carte")
    L.append("- 2. Scripts .sh")
    L.append("- 3. Automations par pole")
    L.append("- 4. Scripts non-sh")
    L.append("- 5. Entites orphelines")
    L.append("- 6. Statistiques")
    L.append("")
    L.append("## 1. VIGNETTES DASHBOARD (L0C0 -> L6C3) - PAR CARTE")
    L.append("")
    for v in vigs:
        L.append("### %s - %s" % (v["code"], v["nom"]))
        L.append("")
        if ann.get(v["code"]):
            L.append("*Annotations conservees de la version precedente (extraction du %s).*"
                     % datetime.date.today().isoformat())
            L.append("")
            L.append(ann[v["code"]])
            L.append("")
        L.append("*%d entites, %d cartes, %d fichiers YAML - dossier `%s`*"
                 % (len(v["entites"]), v["cartes"], len(v["yaml"]), v["dossier"]))
        L.append("")
        # --- chaine de dependances : entites regroupees par type et fichier de definition ---
        par_type = collections.defaultdict(lambda: collections.defaultdict(int))
        for e in sorted(v["entites"]):
            typ, src = defs.get(e, ("NAT", "(native/UI)"))
            par_type[typ][src] += 1
        L.append("### Chaine de dependances")
        L.append("")
        L.append("```")
        for typ in ("NAT", "TPL", "SEN", "UM"):
            if typ not in par_type:
                continue
            total = sum(par_type[typ].values())
            L.append("%s (%s: %d)" % ("MATERIEL" if typ == "NAT" else typ, typ, total))
            for src, n in sorted(par_type[typ].items()):
                L.append("  - %s: %s (%d)" % (typ, src, n))
        L.append("  -> VIGNETTE %s" % v["code"])
        L.append("```")
        L.append("")
        L.append("### Entites consommees par la vignette")
        L.append("")
        L.append("| Entite | Type | Fichier source |")
        L.append("|:-------|:----:|:--------------|")
        for e in sorted(v["entites"]):
            typ, src = defs.get(e, ("NAT", "(native/UI)"))
            L.append("| `%s` | %s | %s |" % (e, typ, src))
        L.append("")
        # --- fichiers YAML deployables : ceux qui DEFINISSENT les entites de la vignette ---
        L.append("### Fichiers YAML deployables")
        L.append("")
        sources = sorted({defs[e][1] for e in v["entites"] if e in defs})
        if sources:
            L.append("| Fichier de config | Destination prod | Statut |")
            L.append("|:------------------|:-----------------|:-------|")
            for s in sources:
                p_prod, statut = etat_prod(s)
                L.append("| `%s` | `%s` | %s |" % (s, p_prod, statut))
        else:
            L.append("*Aucun fichier de config ne definit les entites de cette vignette (tout est natif).*")
        L.append("")
        L.append("### Fichiers de la vignette (dashboard)")
        L.append("")
        for y in v["yaml"]:
            L.append("- `%s`" % y)
        L.append("")
    L.append("## 2. SCRIPTS .SH")
    L.append("")
    for p, ents in scr["sh"]:
        L.append("### %s" % os.path.basename(p))
        L.append("*%s - %d entites*" % (p, len(ents)))
        L.append("")
        if ents:
            for e in sorted(ents):
                L.append("- `%s`" % e)
            L.append("")
        else:
            L.append("*Aucune entite HA referencee (script systeme/fichiers).*")
            L.append("")
    L.append("## 3. AUTOMATIONS (PAR POLE)")
    L.append("")
    for a in autos:
        L.append("### %s" % a["pole"])
        L.append("*%d fichiers YAML, %d automations, %d entites*"
                 % (a["fichiers"], len(a["alias"]), len(a["entites"])))
        L.append("")
        for al in a["alias"]:
            L.append("- %s" % al.strip())
        L.append("")
    L.append("## 4. SCRIPTS NON-SH")
    L.append("")
    for p, ents in scr["autre"]:
        L.append("- `%s` - %d entites" % (p, len(ents)))
    L.append("")
    L.append("## 5. ENTITES ORPHELINES (NI DASHBOARD, NI AUTOMATIONS, NI SCRIPTS)")
    L.append("")
    L.append("%d entites definies dans la config et utilisees nulle part." % len(orphelines))
    L.append("")
    for e in orphelines:
        typ, src = defs.get(e, ("NAT", "?"))
        L.append("- `%s` (%s, %s)" % (e, typ, src))
    L.append("")
    L.append("## STATISTIQUES")
    L.append("")
    L.append("| Mesure | Valeur |")
    L.append("|:-------|-------:|")
    L.append("| Vignettes | %d |" % len(vigs))
    L.append("| Entites definies dans la config | %d |" % len(defs))
    L.append("| Entites referencees quelque part | %d |" % len(utilises))
    L.append("| Entites orphelines | %d |" % len(orphelines))
    L.append("| Scripts .sh | %d |" % len(scr["sh"]))
    L.append("| Scripts non-sh | %d |" % len(scr["autre"]))
    L.append("| Poles d'automations | %d |" % len(autos))
    L.append("| Cartes au total | %d |" % sum(v["cartes"] for v in vigs))
    L.append("")

    texte = "\n".join(L) + "\n"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    open(out_path, "w", encoding="utf-8", newline="\n").write(texte)
    print("ecrit :", out_path)
    print("%d lignes, %d octets" % (texte.count("\n"), len(texte.encode("utf-8"))))
    print("vignettes %d | entites definies %d | referencees %d | orphelines %d"
          % (len(vigs), len(defs), len(utilises), len(orphelines)))


if __name__ == "__main__":
    main()
