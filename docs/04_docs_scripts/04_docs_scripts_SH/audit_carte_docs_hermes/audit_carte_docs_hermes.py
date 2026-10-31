"""Audit LECTURE SEULE de la carte des docs (arborescence + index).

1. Recompte l'arborescence en local ET en prod, en separant les sauvegardes .bak.
2. Extrait les liens et chemins cites par les fichiers d'index et teste leur existence,
   en deux passes (un nom de fichier cite sans son dossier n'est pas un lien mort).

Usage : python audit_carte_docs.py
Regler LOCAL / PROD / ZONES / INDEX avant de lancer. Ne modifie AUCUN fichier.

Pieges Python sur Windows (vecus, coutent une iteration chacun) :
  * os.path.join("C:", "Users", ...) rend "C:Users\\..." SANS separateur : os.walk ne trouve
    rien, sans lever d'erreur, et le projet parait vide. Ecrire "C:/Users/..." ou "C:" + os.sep.
  * r"H:\\" est une SyntaxError : une chaine brute ne peut pas finir par un antislash.
"""

import hashlib
import os
import re

LOCAL = "C:/Users/Berry Swann/Documents/ReBuild"
PROD = "H:" + os.sep

# (etiquette, chemin relatif a LOCAL, chemin relatif a PROD ou None si local seulement)
ZONES = [
    ("docs/", "docs", "docs"),
    ("docs/00_IA/", "docs/00_IA", "docs/00_IA"),
    ("  sous_context_ia/", "docs/00_IA/sous_context_ia", "docs/00_IA/sous_context_ia"),
    ("docs/01_docs_config_system/", "docs/01_docs_config_system", "docs/01_docs_config_system"),
    ("docs/02_docs_dashboard/", "docs/02_docs_dashboard", "docs/02_docs_dashboard"),
    ("docs/03_docs_automations/", "docs/03_docs_automations", "docs/03_docs_automations"),
    ("docs/04_docs_scripts/", "docs/04_docs_scripts", "docs/04_docs_scripts"),
    ("docs/99_docs_MD_system/", "docs/99_docs_MD_system", None),
    ("historique/", "historique", None),
    ("scripts/", "scripts", None),
]

INDEX = [
    "docs/01_docs_config_system/01_config_system_MD/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md",
    "docs/99_docs_MD_system/ENTITES_GLOBAL_INDEX/ENTITES_GLOBAL_INDEX.md",
    "docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_INDEX_NAVIGATION/IA_INDEX_NAVIGATION.md",
    "docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_INDEX_AUTOMATIONS/IA_INDEX_AUTOMATIONS.md",
]

MOTIFS = [
    re.compile(r"\[[^\]]*\]\(([^)\s]+)\)"),          # lien markdown
    re.compile(r'href="([^"]+)"'),                      # lien HTML
    re.compile(r"`([A-Za-z0-9_./\-]+\."                # chemin en backticks
               r"(?:md|yaml|yml|sh|py|txt|json|html|png|csv))`"),
]

EXCLUS = (".git", "node_modules", "__pycache__")


def compte(racine):
    """(total, dont sauvegardes) ou None si le dossier n'existe pas."""
    if not os.path.isdir(racine):
        return None
    tot = bak = 0
    for _, dossiers, fichiers in os.walk(racine):
        dossiers[:] = [d for d in dossiers if d not in EXCLUS]
        for f in fichiers:
            tot += 1
            bak += ".bak" in f
    return tot, bak


def carte_noms():
    """nom de fichier -> emplacements, pour la 2e passe de resolution des liens."""
    noms = {}
    for base in (LOCAL, PROD):
        for racine, dossiers, fichiers in os.walk(base):
            dossiers[:] = [d for d in dossiers if d not in EXCLUS]
            if racine.count(os.sep) - base.count(os.sep) > 6:
                dossiers[:] = []
            for f in fichiers:
                noms.setdefault(f, []).append(os.path.join(racine, f))
    return noms


def existe(chemin):
    """teste le chemin en local puis en prod (les docs vivent des deux cotes)."""
    c = chemin.lstrip("/").replace("\\", "/")
    if c.startswith("homeassistant/"):
        c = c[len("homeassistant/"):]
    return any(os.path.exists(os.path.join(base, c)) for base in (LOCAL, PROD))


print("=== 1. ARBORESCENCE (recomptage) ===")
print(f"{'zone':34s} {'local':>16s} {'prod':>16s}")
for etiquette, rel_local, rel_prod in ZONES:
    cl = compte(os.path.join(LOCAL, rel_local))
    cp = compte(os.path.join(PROD, rel_prod)) if rel_prod else None
    tl = f"{cl[0]} (dont {cl[1]} .bak)" if cl else "ABSENT"
    tp = f"{cp[0]} (dont {cp[1]} .bak)" if cp else "-"
    print(f"{etiquette:34s} {tl:>16s} {tp:>16s}")
print("\nRappel : les .bak sont compris dans les totaux ; publier les deux chiffres.")

print("\n=== 2. INDEX : miroir local / prod puis liens ===")
noms = carte_noms()
for rel in INDEX:
    p = os.path.join(LOCAL, rel)
    pp = os.path.join(PROD, rel.replace("Github/", ""))
    if not os.path.exists(p):
        print(f"### {rel} : ABSENT en local")
        continue
    empreinte = hashlib.md5(open(p, "rb").read()).hexdigest()[:8]
    etat = ""
    if os.path.exists(pp):
        autre = hashlib.md5(open(pp, "rb").read()).hexdigest()[:8]
        etat = "miroir local/prod identique" if autre == empreinte else f"ECART avec prod ({autre})"
    texte = open(p, encoding="utf-8", errors="replace").read()
    liens = set()
    for motif in MOTIFS:
        liens.update(motif.findall(texte))

    morts, faux = [], []
    for lien in sorted(liens):
        if lien.startswith(("http://", "https://", "mailto:", "#")):
            continue
        if existe(lien):
            continue
        nom = os.path.basename(lien.replace("\\", "/"))
        if nom in noms:
            faux.append((lien, sorted({os.path.relpath(e, LOCAL) if e.startswith(LOCAL)
                                       else "PROD:" + os.path.relpath(e, PROD)
                                       for e in noms[nom]})[:2]))
        else:
            morts.append(lien)

    print(f"### {rel}   ({empreinte}{', ' + etat if etat else ''})")
    print(f"    {len(liens)} references   {len(morts)} DISPARUS   {len(faux)} cites sans leur dossier")
    for lien in morts[:12]:
        print(f"       disparu : {lien}")
    for lien, ou in faux[:6]:
        print(f"       a reecrire : {lien}  ->  {ou[0]}")
    print()
