#!/usr/bin/env python
# Controle des repertoires XX_ et 99_ de ReBuild/docs (LOCAL SEUL, jamais en prod, jamais sur GitHub).
# Decision d'Eric du 2026-10-25 : ils ne doivent jamais disparaitre. Ce controle se lance
# AVANT et APRES chaque push, et a chaque tour de travail qui touche docs/.
# LECTURE SEULE : n'ecrit rien. Sortie 0 = tout est la ; sortie 1 = un dossier manque ou a maigri.
#
# Usage :
#   python -I check_xx_repertoires.py            # controle complet
#   python -I check_xx_repertoires.py --quiet    # une seule ligne si tout va bien
#   python -I check_xx_repertoires.py --json
import os, sys, json

DOCS = os.path.join("C:" + chr(92), "Users", "Berry Swann", "Documents", "ReBuild", "docs")
PROD = "H:" + chr(92) + "docs"

# (chemin relatif a docs, nombre minimal de fichiers hors .bak constate le 2026-10-25)
LOCAL_SEUL = {"99_docs_MD_system"}  # 99_ ne va JAMAIS en prod : controle d existence locale seulement (renommage du 2026-10-31)
ATTENDUS = [
    ("99_docs_MD_system", 2),
    (os.path.join("02_docs_dashboard", "02_dashboard_docs_MD", "L4C1_MINI_PC",
                  "XX_L4C1_MINI_PC_03_Page_RASPI"), 1),
    (os.path.join("02_docs_dashboard", "02_dashboard_docs_YAML", "L6C3_VIGIEAU",
                  "XX_L6C3_VIGIEAU_03_Correctif_upstream"), 1),
    (os.path.join("02_docs_dashboard", "02_dashboard_docs_YAML", "XX_RASPI"), 2),
    (os.path.join("03_docs_automations", "03_docs_automations_YAML", "XX_RASPI"), 2),
    (os.path.join("04_docs_scripts", "04_docs_scripts_SH",
                  "XX_MP_01_monitor_temp_sh_save_pour_RASPI"), 1),
    (os.path.join("04_docs_scripts", "04_docs_scripts_SH",
                  "XX_MPC_01_monitor_temp_sh_save_pour_RASPI"), 1),
]


def compte(d):
    n = 0
    for base, _dirs, files in os.walk(d):
        for f in files:
            if ".bak" not in f:
                n += 1
    return n


def main():
    quiet = "--quiet" in sys.argv
    as_json = "--json" in sys.argv
    res = []
    pb = 0
    for rel, mini in ATTENDUS:
        p = os.path.join(DOCS, rel)
        existe = os.path.isdir(p)
        n = compte(p) if existe else 0
        etat = "OK"
        if not existe:
            etat = "MANQUANT"
            pb += 1
        elif n < mini:
            etat = "MAIGRI (%d < %d)" % (n, mini)
            pb += 1
        en_prod = False if rel in LOCAL_SEUL else os.path.isdir(os.path.join(PROD, rel))
        if en_prod:
            etat = "PRESENT EN PROD, interdit"
            pb += 1
        res.append({"dossier": rel, "existe": existe, "fichiers": n, "minimum": mini,
                    "en_prod": en_prod, "etat": etat})

    if as_json:
        print(json.dumps({"ok": pb == 0, "problemes": pb, "dossiers": res}, ensure_ascii=False, indent=1))
    elif quiet and pb == 0:
        print("XX_ : %d dossiers presents, aucun en prod" % len(res))
    else:
        for r in res:
            print("%-9s %2d/%2d  %s%s" % (r["etat"][:9], r["fichiers"], r["minimum"], r["dossier"],
                                         "  [EN PROD]" if r["en_prod"] else ""))
        print("bilan : %d problemes sur %d dossiers XX_ attendus" % (pb, len(res)))
    return 0 if pb == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
