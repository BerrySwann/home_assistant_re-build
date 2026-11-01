#!/usr/bin/env python
# Controle des repertoires XX_ et 99_ de ReBuild/docs (LOCAL SEUL, jamais en prod, jamais sur GitHub).
# Decision d'Eric du 2026-10-25 : ils ne doivent jamais disparaitre. Ce controle se lance
# AVANT et APRES chaque push, et a chaque tour de travail qui touche docs/.
# LECTURE SEULE : n'ecrit rien. Sortie 0 = tout est la ; sortie 1 = un probleme.
#
# Depuis le 2026-11-01 (idee 8, h20261101-30) : la liste des dossiers et leurs fichiers attendus
# ne sont PLUS codes en dur. La source est le manifeste de Claude, lu en lecture seule :
#   docs/04_docs_scripts/04_docs_scripts_JSON/Check_XX_presents/XX_manifest.json
# Deux renommages en deux jours (99_ le 31/10, suffixes " (a ne pas jeter)" le 01/11) ont casse
# une liste en dur : un seul proprietaire de la liste, c'est le manifeste. Ce script ne l'ecrit
# jamais et ne le modifie jamais (--maj appartient a Check_XX_presents.py, sur ordre d'Eric).
#
# Usage :
#   python -I check_xx_repertoires.py            # controle complet
#   python -I check_xx_repertoires.py --quiet    # une seule ligne si tout va bien
#   python -I check_xx_repertoires.py --json
import json
import os
import sys

DOCS = os.path.join("C:" + chr(92), "Users", "Berry Swann", "Documents", "ReBuild", "docs")
PROD = "H:" + chr(92) + "docs"
MANIFESTE = os.path.join(DOCS, "04_docs_scripts", "04_docs_scripts_JSON",
                         "Check_XX_presents", "XX_manifest.json")

# 99_ ne va jamais en prod (decision d'Eric du 2026-10-31, exception ENTITES_GLOBAL_INDEX.md non
# verifiee ici) : pour cette entree, seule l'existence locale est exigee.
LOCAL_SEUL = {"99_docs_MD_system"}


def compte(d):
    """Nombre de fichiers hors .bak sous d."""
    n = 0
    for base, _dirs, files in os.walk(d):
        for f in files:
            if ".bak" not in f:
                n += 1
    return n


def manifeste():
    with open(MANIFESTE, encoding="utf-8") as fh:
        return json.load(fh)


def dossiers_xx_disque():
    """Chemins relatifs (slashes) de tous les dossiers dont le nom commence par XX_."""
    trouves = []
    for base, dirs, _files in os.walk(DOCS):
        for nom in dirs:
            if nom.startswith("XX_"):
                trouves.append(os.path.relpath(os.path.join(base, nom), DOCS).replace(os.sep, "/"))
    return trouves


def main():
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv
    if not os.path.exists(MANIFESTE):
        print("MANIFESTE ABSENT : %s" % MANIFESTE)
        return 1
    man = manifeste()
    res = []
    pb = 0
    for rel, fichiers in sorted(man.items()):
        p = os.path.join(DOCS, rel.replace("/", os.sep))
        existe = os.path.isdir(p)
        n = compte(p) if existe else 0
        mini = len(fichiers)
        etat = "OK"
        if not existe:
            etat = "MANQUANT"
        elif n < mini:
            etat = "MAIGRI (%d < %d)" % (n, mini)
        absents = [f for f in fichiers
                   if not os.path.exists(os.path.join(DOCS, f.replace("/", os.sep)))]
        if existe and absents:
            etat = "FICHIER ABSENT (%s)" % absents[0][:40]
        en_prod = False
        if rel not in LOCAL_SEUL and not rel.startswith("99_"):
            en_prod = os.path.isdir(os.path.join(PROD, rel.replace("/", os.sep)))
            if en_prod:
                etat = "PRESENT EN PROD, interdit"
        if etat != "OK":
            pb += 1
        res.append({"dossier": rel, "existe": existe, "fichiers": n, "minimum": mini,
                    "en_prod": en_prod, "etat": etat})

    declares = set(man.keys())
    non_declares = [dl for dl in dossiers_xx_disque()
                    if dl not in declares
                    and not any(dl.startswith(d2 + "/") for d2 in declares)]
    if non_declares:
        pb += len(non_declares)

    if as_json:
        print(json.dumps({"ok": pb == 0, "problemes": pb, "manifeste": MANIFESTE,
                          "dossiers": res, "non_declares": non_declares},
                         ensure_ascii=False, indent=1))
    elif quiet and pb == 0:
        print("XX_ : %d dossiers presents, aucun en prod" % len(res))
    else:
        for r in res:
            print("%-9s %2d/%2d  %s%s" % (r["etat"][:9], r["fichiers"], r["minimum"], r["dossier"],
                                         "  [EN PROD]" if r["en_prod"] else ""))
        for dl in non_declares:
            print("NON DECLARE dans le manifeste : %s" % dl)
        print("bilan : %d problemes sur %d dossiers du manifeste" % (pb, len(res)))
    return 0 if pb == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
