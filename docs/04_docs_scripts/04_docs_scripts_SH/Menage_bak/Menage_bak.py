# -*- coding: utf-8 -*-
"""Menage_bak.py - menage des .bak du perimetre docs et Claude md SAVE.

Remplace le menage refait a la main a chaque /histo (R77.1, decision d'Eric).
Les regles sont celles de CLAUDE.md (REGLE DE SAUVEGARDE) et de
histo_ref_menage.md, recopiees ici pour que le script soit la reference unique :
  - un .bak horodate du jour par fichier : 10 au maximum, le 11e envoie le plus
    ancien a la corbeille ;
  - un .bak date par jour passe : 3 au maximum, au-dela le plus ancien part ;
  - JAMAIS de suppression definitive : tout part a la CORBEILLE WINDOWS,
    l utilisateur peut restaurer. Le script ne vide jamais la corbeille.

PERIMETRE : docs/00_* a 05_* (recursif) et "Claude md SAVE".
HORS PERIMETRE : TODO, Github, historique, Infra_Proxmox, _old_avant_staging,
99_docs_MD_system, TEMPO.

USAGE :
  python -I -X utf8 Menage_bak.py            -> dry-run, n ecrit rien
  python -I -X utf8 Menage_bak.py --go       -> envoie a la corbeille

Codes de sortie : 0 rien a faire ou tout fait, 1 erreur.
"""
import os
import re
import sys
import glob
import collections

PLAFOND_JOUR = 10
PLAFOND_JOURS_PASSES = 3
VERBE = "--go" in sys.argv

BASE = r"C:\Users\Berry Swann\Documents\ReBuild"
SAVE = os.path.join(BASE, "Claude md SAVE")
AJOURDHUI = "2026_11_08"  # fige en debut d execution par date_du_jour()

# nom valide : stem + .bak_AAAA_MM_JJ[_HHhMMmSSs][.ext]
PAT = re.compile(
    r"^(?P<stem>.+)\.bak_"
    r"(?P<annee>\d{4})_(?P<mois>\d{2})_(?P<jour>\d{2})"
    r"(?P<heure>_\d{2}h\d{2}m\d{2}s)?"
    r"(?:\.(?P<ext2>[A-Za-z0-9]+))?$"
)

EXCLUS_DIRS = {"__pycache__", "TEMPO", ".git", "99_docs_MD_system",
               "_old_avant_staging", "Infra_Proxmox"}


def date_du_jour():
    import datetime
    return datetime.date.today().strftime("%Y_%m_%d")


def corbeille(chemin):
    """Envoie UN fichier a la corbeille Windows. Rend True si parti."""
    import ctypes
    from ctypes import wintypes

    class SHFILEOPSTRUCTW(ctypes.Structure):
        _fields_ = [
            ("hwnd", wintypes.HWND), ("wFunc", wintypes.UINT),
            ("pFrom", wintypes.LPCWSTR), ("pTo", wintypes.LPCWSTR),
            ("fFlags", ctypes.c_uint16), ("fAnyOperationsAborted", wintypes.BOOL),
            ("hNameMappings", ctypes.c_void_p), ("lpszProgressTitle", wintypes.LPCWSTR),
        ]

    FO_DELETE = 3
    FOF_ALLOWUNDO = 0x0040
    FOF_NOCONFIRMATION = 0x0010
    FOF_NOERRORUI = 0x0400
    FOF_SILENT = 0x0004

    op = SHFILEOPSTRUCTW(
        hwnd=None, wFunc=FO_DELETE, pFrom=os.path.abspath(chemin) + "\0",
        pTo=None,
        fFlags=FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_NOERRORUI | FOF_SILENT,
        fAnyOperationsAborted=False, hNameMappings=None, lpszProgressTitle=None,
    )
    res = ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op))
    return res == 0 and not op.fAnyOperationsAborted


def racines():
    for n in range(6):
        for d in glob.glob(os.path.join(BASE, "docs", "%02d_*" % n)):
            if os.path.isdir(d) and os.path.basename(d) not in EXCLUS_DIRS:
                yield d
    if os.path.isdir(SAVE):
        yield SAVE


def collecte():
    """Rend (groupes, mal_nommes). Un groupe = un fichier d origine."""
    groupes = collections.defaultdict(lambda: {"jour": [], "passe": []})
    mal_nommes = []
    for r in racines():
        for root, dirs, files in os.walk(r):
            dirs[:] = [d for d in dirs if d not in EXCLUS_DIRS]
            for f in files:
                if ".bak_" not in f:
                    continue
                chemin = os.path.join(root, f)
                m = PAT.match(f)
                if not m:
                    mal_nommes.append(chemin)
                    continue
                date = "%s_%s_%s" % (m.group("annee"), m.group("mois"), m.group("jour"))
                cle = os.path.join(root, m.group("stem"))
                if date == AJOURDHUI:
                    groupes[cle]["jour"].append((m.group("heure") or "", chemin))
                else:
                    groupes[cle]["passe"].append((date, chemin))
    return groupes, mal_nommes


def plan(groupes):
    """Rend la liste des (chemin, raison) a envoyer a la corbeille."""
    a_retirer = []
    for cle, v in sorted(groupes.items()):
        # regle du jour : 10 au maximum, on retire les plus anciens horodatages
        jour = sorted(v["jour"])
        if len(jour) > PLAFOND_JOUR:
            for _, chemin in jour[: len(jour) - PLAFOND_JOUR]:
                a_retirer.append((chemin, "plafond jour (%d > %d)" % (len(jour), PLAFOND_JOUR)))
        # regle des jours passes : 3 jours differents au maximum
        par_jour = collections.defaultdict(list)
        for date, chemin in v["passe"]:
            par_jour[date].append(chemin)
        jours = sorted(par_jour)
        if len(jours) > PLAFOND_JOURS_PASSES:
            for date in jours[: len(jours) - PLAFOND_JOURS_PASSES]:
                for chemin in sorted(par_jour[date]):
                    a_retirer.append((chemin, "plafond jours passes (jour %s)" % date))
    return a_retirer


def main():
    global AJOURDHUI
    AJOURDHUI = date_du_jour()

    groupes, mal_nommes = collecte()
    total = sum(len(v["jour"]) + len(v["passe"]) for v in groupes.values())
    a_retirer = plan(groupes)

    print("Menage_bak - %s" % AJOURDHUI)
    print("perimetre : docs/00_* a 05_*, Claude md SAVE")
    print("fichiers porteurs de .bak : %d | .bak au total : %d" % (len(groupes), total))
    print("plafonds : %d horodates du jour, %d jours passes par fichier"
          % (PLAFOND_JOUR, PLAFOND_JOURS_PASSES))

    if mal_nommes:
        print("\nNOMS HORS FORMAT : %d (non traites, a renommer a la main)" % len(mal_nommes))
        for c in sorted(mal_nommes)[:10]:
            print("   ", os.path.relpath(c, BASE))
        if len(mal_nommes) > 10:
            print("    ... et %d autres" % (len(mal_nommes) - 10))

    if not a_retirer:
        print("\nRESULTAT : rien a envoyer a la corbeille, les plafonds sont respectes")
        return 0

    print("\nA ENVOYER A LA CORBEILLE : %d" % len(a_retirer))
    for chemin, raison in a_retirer:
        print("   %s | %s" % (os.path.relpath(chemin, BASE), raison))

    if not VERBE:
        print("\nDRY-RUN : rien n a ete touche. Relancer avec --go pour envoyer.")
        return 0

    print("\nenvoi a la corbeille Windows...")
    ok, ko = 0, []
    for chemin, _ in a_retirer:
        if corbeille(chemin):
            ok += 1
        else:
            ko.append(chemin)
    print("   partis : %d | echecs : %d" % (ok, len(ko)))
    for c in ko:
        print("   ECHEC :", os.path.relpath(c, BASE))
    # controle : plus aucun depassement
    restants = plan(collecte()[0])
    print("   depassements restants : %d" % len(restants))
    return 0 if not ko and not restants else 1


if __name__ == "__main__":
    sys.exit(main())
