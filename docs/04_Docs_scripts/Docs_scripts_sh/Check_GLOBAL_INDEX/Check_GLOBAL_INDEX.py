# -*- coding: utf-8 -*-
r"""check_global_index.py - controle LECTURE SEULE de tous les index globaux (appele par /histo).

Pour chaque index : existence, liens casses (markdown et href), equilibre <details>/<blockquote> (REPO),
presence et MD5 en prod (H:\ lecture seule, regle des 2 emplacements pour GLOBAL_INDEX_REPO),
entites citees absentes de core.entity_registry / core.restore_state / groupes YAML (REPO et ENTITES).
Faux positifs ecartes (voir ENTITES_SYSTEME, ENTITES_NOTES, TYPES_NON_ENTITES) : entites sans registre, noms cites comme retires, types de declencheur.
Ne modifie rien, ne corrige rien : il signale. Derniere ligne :
  controle global_index: index=N liens=N casses=N ecarts=N
Usage : $env:PYTHONIOENCODING='utf-8'; python -I check_global_index.py
"""
import os, re, sys, json, hashlib
from urllib.parse import unquote

BASE = r"C:\Users\Berry Swann\Documents\ReBuild"
D = os.path.join(BASE, "docs")
PH = "H:\\"
# cle : (chemin local, [chemins prod], mode de resolution des liens, controle entites)
INDEX = {
 "GLOBAL_INDEX_REPO": (os.path.join(D, "05_docs_MD_system", "GLOBAL_INDEX_REPO", "GLOBAL_INDEX_REPO.md"),
                       [r"H:\GLOBAL_INDEX_REPO.md", r"H:\docs\05_docs_MD_system\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md"], "racine", True),
 "GLOBAL_INDEX_AUTOMATIONS": (os.path.join(D, "03_docs_automations", "GLOBAL_INDEX_AUTOMATIONS.md"),
                       [r"H:\docs\03_docs_automations\GLOBAL_INDEX_AUTOMATIONS.md"], "dossier", False),
 "GLOBAL_INDEX_VIGNETTES_PAGES": (os.path.join(D, "02_docs_dashboard", "GLOBAL_INDEX_VIGNETTES_PAGES.md"),
                       [r"H:\docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md"], "dossier", False),
 "GLOBAL_INDEX_SCRIPTS_SH": (os.path.join(D, "04_docs_scripts", "GLOBAL_INDEX_SCRIPTS_SH.md"),
                       [r"H:\docs\04_docs_scripts\GLOBAL_INDEX_SCRIPTS_SH.md"], "dossier", False),
 "GLOBAL_INDEX_SCRIPTS_YAML": (os.path.join(D, "04_docs_scripts", "GLOBAL_INDEX_SCRIPTS_YAML.md"),
                       [r"H:\docs\04_docs_scripts\GLOBAL_INDEX_SCRIPTS_YAML.md"], "dossier", False),
 "ENTITES_GLOBAL_INDEX": (os.path.join(D, "05_docs_MD_system", "ENTITES_GLOBAL_INDEX", "ENTITES_GLOBAL_INDEX.md"),
                       [r"H:\docs\05_docs_MD_system\ENTITES_GLOBAL_INDEX\ENTITES_GLOBAL_INDEX.md"], "dossier", True),
 "GLOBAL_INDEX_IA": (os.path.join(D, "00_IA", "GLOBAL_INDEX_IA.md"),
                       [r"H:\docs\00_IA\GLOBAL_INDEX_IA.md"], "dossier", False),
}
# Entites sans fiche dans le registre : fournies par le coeur HA (sun) - usage reel verifie dans card_duree_du_jour.yaml
ENTITES_SYSTEME = {"sun.sun"}
# Noms cites dans les notes de journal du GLOBAL_INDEX_REPO comme inexistants ou retires : ne sont pas des entrees
ENTITES_NOTES = {"climate.clim_du_bureau", "sensor.direction_du_vent_vence", "sensor.vitesse_du_vent_vence"}
# Types de declencheur ecrits comme une entite (automations.yaml : trigger: timer.finished) : pas des entites
TYPES_NON_ENTITES = {"timer.finished"}
RX_LINK = re.compile(r'\]\(([^)\s]+)(?:\s+"[^"]*")?\)|href="([^"]+)"')
RX_ENT = re.compile(r"\b(?:sensor|binary_sensor|automation|script|switch|light|climate|input_[a-z]+|utility_meter|cover|select|number|device_tracker|person|group|scene|timer|counter|weather|media_player|button|fan|lock|event|update|image|text|sun)\.[a-z0-9_]+\b")


def lire(p):
    with open(p, "rb") as fh:
        return fh.read().decode("utf-8", errors="replace")


def md5(p):
    with open(p, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def entites_prod():
    S = set()
    for nom, chemin in (("registry", r"H:\.storage\core.entity_registry"), ("restore", r"H:\.storage\core.restore_state")):
        try:
            j = json.loads(lire(chemin))
            d = j.get("data", {})
            if nom == "registry":
                S.update(e.get("entity_id") for e in d.get("entities", []))
            else:
                S.update(e.get("state", {}).get("entity_id") for e in d)
        except Exception:
            pass
    S.discard(None)
    return S

def groupes_yaml():
    """Groupes definis en YAML (configuration.yaml : group: !include_dir_merge_named groups/) -> group.<cle>."""
    S = set()
    dossier = r"H:\groups"
    try:
        for fn in os.listdir(dossier):
            if fn.lower().endswith((".yaml", ".yml")):
                for m in re.finditer(r"^([a-z0-9_]+):\s*$", lire(os.path.join(dossier, fn)), re.M):
                    S.add("group." + m.group(1))
    except Exception:
        pass
    return S


def liens_de(t, local, mode, h_ok):
    n, cas = 0, []
    for m in RX_LINK.finditer(t):
        u = m.group(1) or m.group(2)
        if u.startswith(("http://", "https://", "#", "mailto:", "data:")):
            continue
        n += 1
        rel = unquote(u).split("#")[0]
        if not rel:
            continue
        bases = [os.path.dirname(local)] if mode == "dossier" else [BASE] + ([PH] if h_ok else [])
        if not any(os.path.exists(os.path.normpath(os.path.join(b, rel))) for b in bases):
            cas.append(rel)
    return n, cas


def etat_prod(local, prods, h_ok):
    if not h_ok:
        return "H: inaccessible (non controle)", False
    ml = md5(local)
    etats, ko = [], False
    for p in prods:
        if not os.path.exists(p):
            etats.append("absent %s" % p)
            ko = True
        elif md5(p) != ml:
            etats.append("DIFFERENT %s" % p)
            ko = True
    return ("OK" if not ko else "; ".join(etats)), ko


def main():
    h_ok = os.path.isdir(PH) and os.path.exists(r"H:\.storage")
    ent = (entites_prod() | groupes_yaml() | ENTITES_SYSTEME | ENTITES_NOTES | TYPES_NON_ENTITES) if h_ok else set()
    tot_liens = tot_cas = tot_ecarts = 0
    print("controle des index globaux (lecture seule)%s" % ("" if h_ok else " - H: INACCESSIBLE : prod et entites non controles"))
    for nom, (local, prods, mode, veut_ent) in INDEX.items():
        if not os.path.exists(local):
            print("%s: ABSENT (ecart) - %s" % (nom, local))
            tot_ecarts += 1
            continue
        t = lire(local)
        n, cas = liens_de(t, local, mode, h_ok)
        tot_liens += n
        tot_cas += len(cas)
        ecarts = []
        ep, ko = etat_prod(local, prods, h_ok)
        if ko:
            ecarts.append("prod")
        extra = ""
        if nom == "GLOBAL_INDEX_REPO":
            d1, d2 = len(re.findall(r"<details", t)), len(re.findall(r"</details>", t))
            b1, b2 = len(re.findall(r"<blockquote", t)), len(re.findall(r"</blockquote>", t))
            extra = " details=%d/%d blockquote=%d/%d" % (d1, d2, b1, b2)
            if d1 != d2 or b1 != b2:
                ecarts.append("balises")
        absentes = []
        if veut_ent and ent:
            vus = {m.group(0) for m in RX_ENT.finditer(t)}
            absentes = sorted(e for e in vus if e not in ent and not e.endswith("_") and "xxx" not in e)
            if absentes:
                ecarts.append("entites")
            extra += " entites_absentes=%d" % len(absentes)
        tot_ecarts += len(ecarts)
        print("%s: liens=%d casses=%d prod=%s%s" % (nom, n, len(cas), ep, extra))
        for c in cas[:10]:
            print("    LIEN CASSE : %s" % c)
        if len(cas) > 10:
            print("    ... et %d autres liens casses" % (len(cas) - 10))
        for e in absentes[:8]:
            print("    ENTITE ABSENTE : %s" % e)
        if len(absentes) > 8:
            print("    ... et %d autres entites absentes" % (len(absentes) - 8))
        if ecarts:
            print("    ECART : %s" % ", ".join(ecarts))
    print("controle global_index: index=%d liens=%d casses=%d ecarts=%d" % (len(INDEX), tot_liens, tot_cas, tot_ecarts))
    return 0 if (tot_cas == 0 and tot_ecarts == 0) else 1


if __name__ == "__main__":
    sys.exit(main())