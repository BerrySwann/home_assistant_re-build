#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Check_XX_presents.py - controle des dossiers XX_ de ReBuild/docs. OUTIL UNIQUE (copie maitre dans ReBuild depuis le 2026-10-25 ; ancienne copie D:\hermes\scripts\check_xx.py a ne plus utiliser).
# Fusion de deux versions ecrites le 2026-10-25 :
#   - decouverte recursive des dossiers XX_ et manifeste fichier par fichier : idee de Claude
#     (docs/04_docs_scripts/04_docs_scripts_SH/Check_XX_presents/Check_XX_presents.py) ;
#   - controle "aucun XX_ en prod" et controle APRES le push : idee de Hermes.
# UN SEUL manifeste : celui de Claude, dans son dossier, qui reste sa propriete. Ce script le
# lit ; il ne l'ecrit que sur --maj, lui-meme sur ordre d'Eric.
# LECTURE SEULE par defaut : n'ecrit rien, ne cree rien, ne restaure rien.
#
# Usage :
#   python -I -X utf8 Check_XX_presents.py            # controle complet, bavard
#   python -I -X utf8 Check_XX_presents.py --quiet    # une ligne, pour le hook avant/apres push
#   python -I -X utf8 Check_XX_presents.py --json     # sortie machine
#   python -I -X utf8 Check_XX_presents.py --maj      # reecrit le manifeste (ORDRE D'ERIC UNIQUEMENT)
# Codes : 0 = OK, 1 = ALERTE (ne rien pousser), 2 = outil mal arme (manifeste absent).
import os, sys, json

BASE = os.path.join("C:" + chr(92), "Users", "Berry Swann", "Documents", "ReBuild")
DOCS = os.path.join(BASE, "docs")
PROD = "H:" + chr(92) + "docs"
MANIFEST = os.path.join(DOCS, "04_docs_scripts", "04_docs_scripts_SH", "Check_XX_presents",
                        "XX_manifest.json")
SKIP = {"TEMPO", "__pycache__"}
PREF = ("XX_", "99_docs_MD_system")
PROD_AUTORISE = {"99_docs_MD_system/ENTITES_GLOBAL_INDEX/ENTITES_GLOBAL_INDEX.md"}  # seul fichier de 99_ autorise en prod (Eric, 2026-10-31 17h33)  # 99_ ajoute le 2026-10-31 (ordre d Eric) : local seul, comme XX_


def rel(p):
    return os.path.relpath(p, DOCS).replace(chr(92), "/")


def est_bak(nom):
    return ".bak" in nom


def releve(docs):
    """Decouverte RECURSIVE : tout dossier XX_, a n'importe quelle profondeur, y compris un XX_
    imbrique dans un autre XX_ : il compte alors separement, et ses fichiers ne sont pas
    comptes deux fois dans le manifeste du parent."""
    res = {}
    for dp, dn, fn in os.walk(docs):
        dn[:] = [x for x in dn if x not in SKIP]
        for d in sorted(dn):
            if not d.startswith(PREF):
                continue
            top = os.path.join(dp, d)
            fichiers = []
            for p2, d2, f2 in os.walk(top):
                d2[:] = [x for x in d2 if x not in SKIP and not x.startswith(PREF)]
                for f in f2:
                    if est_bak(f):
                        continue
                    fichiers.append(rel(os.path.join(p2, f)))
            res[os.path.relpath(top, docs).replace(chr(92), "/")] = sorted(fichiers)
    return res


def en_prod(docs_prod):
    """Tout dossier XX_ present en prod est une faute : XX_ est local seul."""
    if not os.path.isdir(docs_prod):
        return None  # prod inaccessible : on ne conclut pas
    trouves = []
    for dp, dn, _fn in os.walk(docs_prod):
        dn[:] = [x for x in dn if x not in SKIP]
        for d in dn:
            if d == "99_docs_MD_system":
                # exception d Eric (2026-10-31 17h33) : seul ENTITES_GLOBAL_INDEX.md de 99_ va en prod (sauvegarde GitHub), jamais les .bak
                for p3, _d3, f3 in os.walk(os.path.join(dp, d)):
                    for f in f3:
                        r3 = os.path.relpath(os.path.join(p3, f), docs_prod).replace(chr(92), "/")
                        if r3 not in PROD_AUTORISE:
                            trouves.append(r3)
            elif d.startswith(PREF):
                trouves.append(os.path.relpath(os.path.join(dp, d), docs_prod))
    return sorted(trouves)


def main():
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv
    now = releve(DOCS)

    if "--maj" in sys.argv:
        os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
        json.dump(now, open(MANIFEST, "w", encoding="utf-8"), indent=1, sort_keys=True)
        n = sum(len(v) for v in now.values())
        print("manifeste mis a jour : %d dossiers XX_, %d fichiers" % (len(now), n))
        print("ATTENTION : --maj ne se lance que sur ordre d'Eric ; le manifeste appartient a Claude.")
        return 0

    if not os.path.exists(MANIFEST):
        print("ALERTE : manifeste absent (%s) - ne pas pousser ; --maj sur ordre d'Eric" % MANIFEST)
        return 2
    ref = json.load(open(MANIFEST, encoding="utf-8"))

    alertes, infos = [], []
    for d, fichiers in sorted(ref.items()):
        if d not in now:
            alertes.append("DOSSIER MANQUANT : docs/" + d + " (%d fichiers au manifeste)" % len(fichiers))
            continue
        for f in fichiers:
            if f not in now[d]:
                alertes.append("FICHIER MANQUANT : docs/" + f)
        for f in now[d]:
            if f not in fichiers:
                infos.append("nouveau fichier dans docs/" + d + " : " + f)
    for d in now:
        if d not in ref:
            infos.append("nouveau dossier XX_ non liste au manifeste : docs/" + d)

    prod = en_prod(PROD)
    if prod:
        for p in prod:
            alertes.append("XX_ PRESENT EN PROD (interdit) : " + p)
    elif prod is None and not quiet:
        infos.append("prod H: inaccessible : controle prod non fait")

    ok = not alertes
    if as_json:
        print(json.dumps({"ok": ok, "dossiers": len(now),
                          "fichiers": sum(len(v) for v in now.values()),
                          "alertes": alertes, "infos": infos,
                          "prod_controlee": prod is not None}, ensure_ascii=False, indent=1))
    elif quiet:
        if ok:
            print("XX_ : OK, %d dossiers, %d fichiers, aucun en prod"
                  % (len(now), sum(len(v) for v in now.values())))
        else:
            print("XX_ : ALERTE (%d) - ne pas pousser, detail sans --quiet" % len(alertes))
    else:
        for a in alertes:
            print(a)
        for i in infos:
            print("INFO " + i)
        print("controle XX_ : %d dossiers, %d fichiers au manifeste ; manquants %d ; infos %d ; prod %s"
              % (len(ref), sum(len(v) for v in ref.values()), len(alertes), len(infos),
                 "controlee" if prod is not None else "inaccessible"))
        print("RESULTAT : " + ("ALERTE - ne pas pousser avant d'avoir prevenu Eric" if alertes else "OK"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
