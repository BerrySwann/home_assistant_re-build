# -*- coding: utf-8 -*-
r"""check_sous_context_ia.py - controle LECTURE SEULE des 9 fichiers IA_* de docs\00_IA\SOUS_CONTEXT_IA.
Lance par /histo (etape 2, point 11). N'ecrit rien, ne corrige rien : rapporte les ecarts.
Usage : $env:PYTHONIOENCODING='utf-8'; python -I check_sous_context_ia.py
Controles par fichier :
  1 structure : dossier = nom du fichier, fichier present, baks bien nommes, plafonds (10 le jour meme, 3 par jour passe)
  2 prod : H:\docs\00_IA\SOUS_CONTEXT_IA\<nom>\<nom>.md present et MD5 identique
  3 date declaree dans l'en-tete contre la date de modification du fichier
  4 chemins docs/... cites : existent en local
  5 nombres de type "N automations" / "N vignettes" contre la prod / les dossiers
  6 entites citees : presentes dans core.entity_registry ou core.restore_state (prod, lecture seule)
"""
import os, re, sys, json, hashlib, datetime
import yaml

BASE = r"C:\Users\Berry Swann\Documents\ReBuild"
DIR = os.path.join(BASE, "docs", "00_IA", "SOUS_CONTEXT_IA")
PROD = r"H:\docs\00_IA\SOUS_CONTEXT_IA"
if not os.path.isdir(PROD) and os.path.isdir(r"H:\docs\00_IA\sous_context_ia"):
    PROD = r"H:\docs\00_IA\sous_context_ia"  # ancien nom, tant que la prod n'a pas ete renommee
SEUIL_JOURS = 60
NON_POUSSES = {"IA_SKILLS_INVENTAIRE"}  # decision : pas en prod tant qu'Eric ne le demande pas
TODAY = datetime.date.today()
# Fichiers FIGES (decision d'Eric) : plus de controle de contenu (date, chemins, nombres, entites).
# Restent controles : structure, baks, MD5 prod, et "fige mais modifie depuis" (mtime apres la date de gel).
# Format : "IA_NOM": "AAAA-MM-JJ" (date du gel). Gel decide le 2026-10-13 apres relecture des 9 fichiers (seul IA_P4_PRESENCE : logique verifiee contre le template prod).
FIGES = {"IA_P4_PRESENCE": "2026-10-13"}

def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest().upper()

def lire(p):
    with open(p, "rb") as f:
        t = f.read().decode("utf-8", "replace")
    return t.lstrip("\ufeff")

def faits_prod():
    """Nombre d'automations prod, codes vignettes locaux, entites connues (lecture seule)."""
    F = {"auto": None, "vign": None, "entites": set(), "src": []}
    try:
        with open(r"H:\automations.yaml", "rb") as fh:
            data = yaml.safe_load(fh.read().decode("utf-8"))
        F["auto"] = len(data)
    except Exception as e:
        F["src"].append("automations.yaml illisible : %s" % e)
    for nom, chemin in (("registry", r"H:\.storage\core.entity_registry"), ("restore", r"H:\.storage\core.restore_state")):
        try:
            with open(chemin, "rb") as fh:
                j = json.loads(fh.read().decode("utf-8"))
            d = j.get("data", {})
            if nom == "registry":
                for e in d.get("entities", []):
                    F["entites"].add(e.get("entity_id"))
            else:
                for e in d:
                    st = e.get("state", {})
                    if st.get("entity_id"):
                        F["entites"].add(st["entity_id"])
        except Exception as e:
            F["src"].append("%s illisible : %s" % (nom, e))
    dd = os.path.join(BASE, "docs", "02_docs_dashboard", "dashboard_docs_MD")
    if os.path.isdir(dd):
        F["vign"] = len({m.group(0) for n in os.listdir(dd) for m in [re.match(r"L[1-9]\d*C[1-9]\d*", n)] if m})
    return F

def check_structure(stem, ecarts):
    sub = os.path.join(DIR, stem)
    res = []
    if not os.path.isfile(os.path.join(sub, stem + ".md")):
        ecarts.append("fichier %s.md absent de son dossier" % stem)
    par_jour = {}
    for n in sorted(os.listdir(sub)):
        if n == stem + ".md":
            continue
        m = re.match(r"^%s\.bak_(\d{4})_(\d{2})_(\d{2})(_\d{2}h\d{2}m\d{2}s)?\.md$" % re.escape(stem), n)
        if not m:
            ecarts.append("nom hors format : %s" % n)
            continue
        par_jour.setdefault("%s_%s_%s" % m.group(1, 2, 3), []).append(n)
    j0 = TODAY.strftime("%Y_%m_%d")
    for j, noms in par_jour.items():
        cap = 10 if j == j0 else 3
        if len(noms) > cap:
            ecarts.append("%d baks le %s (plafond %d)" % (len(noms), j, cap))
    return sum(len(v) for v in par_jour.values())

def check_prod(stem):
    loc = os.path.join(DIR, stem, stem + ".md")
    pro = os.path.join(PROD, stem, stem + ".md")
    if not os.path.isfile(pro):
        return "absent (attendu)" if stem in NON_POUSSES else "ABSENT"
    return "OK" if md5(loc) == md5(pro) else "DIFF"

def date_declaree(t):
    for l in t.splitlines()[:12]:
        if re.search(r"(derni[eè]re mise [àa] jour|mis [àa] jour le|refait le|^date\s*:)", l, re.I):
            m = re.search(r"(\d{4})-(\d{2})-(\d{2})", l)
            if m:
                return datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    return None

RX_CHEMIN = re.compile(r"docs[/\\]\d{2}_[A-Za-z0-9_.\-/\\]*[A-Za-z0-9_.\-/\\]")
RX_ENT = re.compile(r"\b(?:sensor|binary_sensor|automation|script|switch|light|climate|input_[a-z]+|utility_meter|cover|select|number|device_tracker|person|group|scene|timer|counter|weather|media_player|button|fan|lock|event|update|image|text|sun)\.[a-z0-9_]+\b")
SANS_ENTITES = {"IA_ARBO_DETAIL", "IA_SKILLS_INVENTAIRE"}

def check_chemins(t):
    morts, vus = [], 0
    for m in RX_CHEMIN.finditer(t):
        brut = m.group(0).rstrip(". ")
        suite = t[m.end():m.end() + 1]
        if suite in ("*", "{", "<", "["):
            continue
        if re.search(r"[*{}<>]|xxx|AAAA|YYYY|JJ|\.\.\.", brut):
            continue
        avant = t[max(0, m.start() - 3):m.start()]
        if avant.upper() == "D:\\":
            continue
        racine = "H:\\" if avant.upper() == "H:\\" else BASE
        cible = os.path.join(racine, brut.replace("/", os.sep).replace("\\", os.sep))
        ligne = t[t.rfind("\n", 0, m.start()) + 1:(t.find("\n", m.end()) if t.find("\n", m.end()) >= 0 else len(t))]
        if re.search(r"supprim|corbeille|n.existe plus|retir|disparu", ligne, re.I):
            continue
        vus += 1
        if not os.path.exists(cible) and brut not in morts:
            morts.append(brut)
    return vus, morts

def check_nombres(t, F):
    ecarts = []
    for i, l in enumerate(t.splitlines(), 1):
        for m in re.finditer(r"(\d+)\s+automations?\b", l):
            n = int(m.group(1))
            if 30 <= n <= 150 and F["auto"] is not None and n != F["auto"]:
                ecarts.append("L%d : %d automations cite, prod = %d" % (i, n, F["auto"]))
        for m in re.finditer(r"(\d+)\s+vignettes?\b", l):
            n = int(m.group(1))
            if n >= 10 and F["vign"] is not None and n != F["vign"]:
                ecarts.append("L%d : %d vignettes cite, dossiers = %d" % (i, n, F["vign"]))
    return ecarts

def check_entites(t, F):
    if not F["entites"]:
        return None
    vus = sorted({m.group(0) for m in RX_ENT.finditer(t)})
    vus = [e for e in vus if not e.endswith("_") and "xxx" not in e]
    return [e for e in vus if e not in F["entites"]]

CLAUDE_MD = os.path.join(BASE, "Claude md SAVE", "CLAUDE.md")
RX_CLAUDE = re.compile(r"docs/00_IA/[A-Za-z0-9_./-]*[A-Za-z0-9_]\.md")

def existe_casse(rel):
    """Vrai si le chemin existe sous BASE avec la casse exacte (Windows ignore la casse, la prod et GitHub non)."""
    cur = BASE
    for part in rel.split("/"):
        try:
            if part not in os.listdir(cur):
                return False
        except OSError:
            return False
        cur = os.path.join(cur, part)
    return True

def check_claude_md():
    """Chemins docs/00_IA/...md cites dans CLAUDE.md : doivent exister en local, casse comprise. Lecture seule."""
    if not os.path.isfile(CLAUDE_MD):
        return 0, None
    t = lire(CLAUDE_MD)
    vus, morts = set(), []
    for m in RX_CLAUDE.finditer(t):
        ch = m.group(0)
        vus.add(ch)
        if not existe_casse(ch) and ch not in morts:
            morts.append(ch)
    return len(vus), morts

def main():
    F = faits_prod()
    print("prod : automations=%s vignettes_locales=%s entites_connues=%d" % (F["auto"], F["vign"], len(F["entites"])))
    for s in F["src"]:
        print("  attention : " + s)
    total_ecarts = total_casses = nb_baks = nb = 0
    for n in sorted(os.listdir(DIR)):
        p = os.path.join(DIR, n)
        if not os.path.isdir(p):
            print("ECART fichier hors dossier a la racine : " + n)
            total_ecarts += 1
            continue
        nb += 1
        ec = []
        nb_baks += check_structure(n, ec)
        pr = check_prod(n)
        if pr in ("DIFF", "ABSENT"):
            ec.append("prod %s" % pr)
        principal = os.path.join(p, n + ".md")
        if n in FIGES:
            gel = datetime.date.fromisoformat(FIGES[n])
            mt0 = datetime.date.fromtimestamp(os.path.getmtime(principal)) if os.path.isfile(principal) else None
            if mt0 and mt0 > gel:
                ec.append("fige le %s mais modifie le %s : a re-geler ou a controler" % (gel, mt0))
            print("%s : prod=%s ; FIGE depuis %s (controle de contenu ignore)" % (n, pr, gel))
            for e in ec:
                print("   ECART " + e)
            total_ecarts += len(ec)
            continue
        t = lire(principal) if os.path.isfile(principal) else ""
        dd = date_declaree(t)
        mt = datetime.date.fromtimestamp(os.path.getmtime(principal)) if t else None
        age = (TODAY - dd).days if dd else None
        info = "date declaree %s%s" % (dd or "aucune", " (%d j)" % age if age is not None else "")
        if age is not None and age > SEUIL_JOURS:
            ec.append("date declaree ancienne : %d jours (seuil %d), a relire" % (age, SEUIL_JOURS))
        if dd and mt and mt > dd + datetime.timedelta(days=SEUIL_JOURS // 2):
            info += " ; fichier modifie le %s (date declaree non rafraichie)" % mt
        vus, morts = check_chemins(t)
        total_casses += len(morts)
        for x in morts:
            ec.append("chemin mort : " + x)
        ec += check_nombres(t, F)
        ent = [] if n in SANS_ENTITES else check_entites(t, F)
        print("%s : prod=%s ; %s ; chemins=%d casses=%d ; entites_introuvables=%s" % (n, pr, info, vus, len(morts), "n/a" if ent is None else len(ent)))
        for e in ec:
            print("   ECART " + e)
        if ent:
            print("   A VERIFIER entites absentes du registre et des etats : " + ", ".join(ent[:12]) + (" ..." if len(ent) > 12 else ""))
        total_ecarts += len(ec)
    cites, morts = check_claude_md()
    if morts is None:
        print("CLAUDE.md introuvable : " + CLAUDE_MD)
        total_ecarts += 1
    else:
        print("CLAUDE.md : chemins docs/00_IA cites=%d morts=%d" % (cites, len(morts)))
        for x in morts:
            print("   ECART chemin mort dans CLAUDE.md : " + x)
        total_ecarts += len(morts)
        total_casses += len(morts)
    print("controle sous_context_ia: dossiers=%d baks=%d ecarts=%d casses=%d" % (nb, nb_baks, total_ecarts, total_casses))

if __name__ == "__main__":
    main()