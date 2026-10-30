# -*- coding: utf-8 -*-
r"""Check_badges_fiches.py - controle des 8 badges de chaque fiche .md de docs/ (cree le 2026-10-28, regle CLAUDE.md "BADGES DES FICHES").

Par defaut LECTURE SEULE : liste les fiches sans banniere, les badges manquants, les valeurs hors liste, les gabarits non remplis.
Avec --fix : cree les badges manquants (jamais de modification d'un badge existant), apres un .bak_AAAA_MM_JJ_HHhMMmSSs.md a cote.
  Valeurs automatiques : Statut = Actif (defaut du 2026-10-30), HA = H:\.HA_VERSION lu en live, MaJ = date du jour, IA Partner = Claude_Sonnet_5.5, Source = Interne,
  Modifs = Autorisees, Expert = HAOS_Proxmox, Type par dossier (01 System, 02 Dashboard, 03 Automation, 04 Scripts). Type ailleurs : jamais devine,
  listes comme A DECIDER.
Options : --fix ; --limite N (corrige au plus N fiches) ; --chemin SOUS_DOSSIER (restreint a un sous-dossier de docs).
Exemptes : .bak, XX_*, *_ORIGINAL, *_archive*, MOC_*, GLOBAL_INDEX_*, docs/00_IA, copies de skills (docs/05_docs_skills).
Derniere ligne : controle badges: fiches=N conformes=N a_corriger=N a_decider=N corrigees=N
"""
import os, re, sys, shutil, datetime
from urllib.parse import unquote

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild\docs"
ORDRE = ["Statut", "MaJ", "HA", "IA_Partner", "Source", "Modifs", "Expert", "Type"]
STATUTS = {"Actif", "En cours", "A terminer", "VERROUILLE", "bak", "Trash", "Archive", "Original"}  # bak/Trash/Archive ajoutes le 2026-10-30 (ordre d'Eric)
TYPES = {"Vignette", "Page", "Carte", "Page droite", "Page gauche", "Dashboard Doc", "Vignette Doc", "Page Doc", "Config Racine", "Index_Pages", "Scripts", "Script", "Script_Executant", "System", "Dashboard", "Automation", "README", "TUTO", "Hacking"}  # System/Dashboard/Automation ajoutes le 2026-10-30 (ordre d Eric)
SKIP = re.compile(r"(^|[\\/])(XX_[^\\/]*|[^\\/]*_ORIGINAL|[^\\/]*_archive[^\\/]*|00_IA|05_docs_skills|__pycache__)([\\/]|$)", re.I)
BADGE = re.compile(r"\[!\[[^\]]*\]\(https://img\.shields\.io/badge/([^)\s]+)\)\]\([^)]*\)")
FIX = "--fix" in sys.argv

def arg(nom, defaut=None):
    if nom in sys.argv:
        i = sys.argv.index(nom)
        if i + 1 < len(sys.argv):
            return sys.argv[i + 1]
    return defaut

def cle(url):
    p = unquote(url.split("?")[0])
    k = p.split("-")[0]
    k = k.replace("\u00e0", "a").replace("\u00c0", "A")
    k = {"AI_Partner": "IA_Partner", "MAJ": "MaJ", "MaJ": "MaJ"}.get(k, k)
    return k

def valeur(url):
    p = unquote(url.split("?")[0]).split("-")
    return "-".join(p[1:-1]) if len(p) >= 3 else (p[1] if len(p) > 1 else "")

def fiches():
    base = ROOT
    sous = arg("--chemin")
    if sous:
        base = os.path.join(ROOT, sous)
    for dp, dn, fn in os.walk(base):
        for f in sorted(fn):
            if not f.lower().endswith(".md") or ".bak" in f or f.startswith(("MOC_", "GLOBAL_INDEX_")):
                continue
            p = os.path.join(dp, f)
            if SKIP.search(os.path.relpath(p, ROOT)):
                continue
            yield p

def ha_version():
    try:
        return open(r"H:\.HA_VERSION", encoding="utf-8").read().strip()
    except Exception:
        return None

def ligne_badge(k, v, ha):
    m = "[![%s](https://img.shields.io/badge/%s?style=flat-square%s)](.)"
    if k == "HA":
        return m % ("HA", "HA-%s-03a9f4" % v, "&logo=home-assistant&logoColor=white")
    if k == "IA_Partner":
        return "[![IA Partner](https://img.shields.io/badge/IA_Partner-%s-blueviolet?style=flat-square)](.)" % v
    coul = {"Statut": "0f9d58", "MaJ": "44739e", "Source": "2196f3", "Modifs": "0f9d58", "Type": "ff9800"}
    if k == "Expert":
        return "[![Expert](https://img.shields.io/badge/Expert-%s-success?style=flat-square)](.)" % v
    nom = {"MaJ": "M\u00e0J"}.get(k, k)
    return m % (nom, "%s-%s-%s" % (nom if k == "MaJ" else k, v.replace("-", "--"), coul[k]), "")

def auto(k, chemin, ha):
    if k == "HA":
        return ha
    if k == "MaJ":
        return datetime.date.today().strftime("%Y-%m-%d")
    if k == "IA_Partner":
        return "Claude_Sonnet_5.5"
    if k == "Source":
        return "Interne"
    if k == "Modifs":
        return "Autorisees"
    if k == "Expert":
        return "HAOS_Proxmox"
    if k == "Statut":
        low = chemin.lower()
        if "_original" in low or "yaml_original" in low:
            return "Original"  # fichier original (ordre d'Eric 2026-10-30)
        if "archive" in low:
            return "Archive"  # sauf Modifs=INTERDITES (cas particulier)
        return "Actif"  # defaut decide par Eric le 2026-10-30
    if k == "Type":  # Type par categorie de dossier (ordre d Eric le 2026-10-30)
        for dossier, t in (("01_docs_config_system", "System"), ("02_docs_dashboard", "Dashboard"), ("03_docs_automations", "Automation"), ("04_docs_scripts", "Scripts")):
            if chemin.replace("/", "\\").startswith(dossier + "\\"):
                return t
    return None

def analyser(texte):
    tete = texte.splitlines()[:30]
    bloc = "\n".join(tete)
    trouves = {}
    for m in BADGE.finditer(bloc):
        trouves[cle(m.group(1))] = (m.group(0), valeur(m.group(1)))
    return trouves, bloc

def valeurs_hors_liste(tr):
    pb = []
    if "Statut" in tr and tr["Statut"][1] not in STATUTS: pb.append("Statut=%s" % tr["Statut"][1])
    if "Type" in tr and tr["Type"][1] not in TYPES: pb.append("Type=%s" % tr["Type"][1])
    if "Modifs" in tr and tr["Modifs"][1] not in ("Autorisees", "INTERDITES"): pb.append("Modifs=%s" % tr["Modifs"][1])
    if "HA" in tr and not re.match(r"^\d{4}\.\d+(\.\d+)?$", tr["HA"][1]): pb.append("HA=%s" % tr["HA"][1])
    if "MaJ" in tr and not re.match(r"^\d{4}--\d{2}--\d{2}$", tr["MaJ"][1].replace("-", "--") if "--" not in tr["MaJ"][1] else tr["MaJ"][1]): pb.append("MaJ=%s" % tr["MaJ"][1])
    return pb

def reconstruire(texte, tr, manquants, chemin, ha):
    eol = "\r\n" if "\r\n" in texte else "\n"
    lignes = texte.split(eol)
    iv = next((i for i, l in enumerate(lignes[:30]) if l.strip().startswith('<div align="center">')), None)
    jv = next((i for i in range(iv or 0, min(len(lignes), 40)) if lignes[i].strip() == "</div>"), None) if iv is not None else None
    nouv = {}
    for k in manquants:
        v = auto(k, chemin, ha)
        if v:
            nouv[k] = ligne_badge(k, v, ha)
    if not nouv:
        return None
    if iv is not None and jv is not None:
        exist = {cle(BADGE.search(l).group(1)): l.strip() for l in lignes[iv:jv] if BADGE.search(l)}
        if len(exist) != sum(1 for l in lignes[iv:jv] if BADGE.search(l)):
            return None
        exist.update(nouv)
        ordre = [k for k in ORDRE if k in exist] + [k for k in exist if k not in ORDRE]
        corps = []
        for n, k in enumerate(ordre):
            l = exist[k].rstrip()
            l = re.sub(r"(&nbsp;)+$", "", l)
            corps.append(l + ("&nbsp;" if n < len(ordre) - 1 else ""))
        return eol.join(lignes[:iv + 1] + [""] + corps + [""] + lignes[jv:])
    if tr:
        return None  # badges hors <div> : forme a revoir a la main
    ordre = [k for k in ORDRE if k in nouv]
    corps = [re.sub(r"(&nbsp;)+$", "", nouv[k]) + ("&nbsp;" if n < len(ordre) - 1 else "") for n, k in enumerate(ordre)]
    banniere = ['<div align="center">', ""] + corps + ["", "</div>", ""]
    ih = next((i for i, l in enumerate(lignes[:15]) if l.startswith("# ")), None)
    pos = (ih + 1) if ih is not None else 0
    if ih is not None and pos < len(lignes) and lignes[pos].strip() == "":
        pos += 1
    return eol.join(lignes[:pos] + banniere + lignes[pos:])

def main():
    ha = ha_version()
    lim = int(arg("--limite", "100000"))
    n = ok = corr = dec = faits = 0
    for p in fiches():
        n += 1
        rel = os.path.relpath(p, ROOT)
        try:
            texte = open(p, encoding="utf-8", newline="").read()
        except Exception as e:
            print("ILLISIBLE  %s (%s)" % (rel, e)); continue
        tr, bloc = analyser(texte)
        manq = [k for k in ORDRE if k not in tr]
        pb = valeurs_hors_liste(tr)
        gab = "{TYPE_DOC}" in texte or bool(re.search(r"\{[A-Z_]{3,}\}", bloc))
        if not manq and not pb and not gab:
            ok += 1; continue
        corr += 1
        indecis = [k for k in manq if auto(k, rel, ha) is None]
        if indecis: dec += 1
        print("%s | manque=%s | hors_liste=%s | gabarit=%s | a_decider=%s" % (rel, ",".join(manq) or "-", ",".join(pb) or "-", "oui" if gab else "non", ",".join(indecis) or "-"))
        if FIX and manq and faits < lim:
            if "HA" in manq and not ha:
                print("   FIX ignore : H:\\.HA_VERSION illisible"); continue
            nt = reconstruire(texte, tr, manq, rel, ha)
            if nt is None:
                print("   FIX ignore : forme a revoir a la main"); continue
            bak = p[:-3] + ".bak_" + datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss") + ".md"
            shutil.copy2(p, bak)
            with open(p, "w", encoding="utf-8", newline="") as f:
                f.write(nt)
            faits += 1
            print("   FIX ok (bak %s)" % os.path.basename(bak))
    print("controle badges: fiches=%d conformes=%d a_corriger=%d a_decider=%d corrigees=%d" % (n, ok, corr, dec, faits))
    return 0 if corr == 0 else 1

if __name__ == "__main__":
    sys.exit(main())