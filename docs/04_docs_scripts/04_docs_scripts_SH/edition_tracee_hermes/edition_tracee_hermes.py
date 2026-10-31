"""Modele d'edition tracee : .bak, MD5 avant/apres, ligne de journal MODIFS.

A COPIER puis adapter (chemin du journal du jour + liste EDITS), pas a importer.

Pourquoi ce fichier existe : construit dans un heredoc bash, un chemin Windows
litteral perd ses antislashs ("historique\\03_RAPPORTS" arrive en Python comme
l'octet 0x03, "\\n" comme un saut de ligne). Le resultat ecrit dans les fichiers
et dans le journal est corrompu et ne se voit qu'a la relecture. Donc : ecrire le
script avec write_file, mettre les chemins en chaine brute (r"...") ou en
chr(92), puis relire le fichier ecrit.

Usage : python edition_tracee.py
"""
import datetime
import hashlib
import io
import os
import shutil
import subprocess

BS = chr(92)

# --- adapter : journal du jour
J = r"C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\01_MODIFS_IA\MODIFS_2026-10-24_hermes.md"
RAISON = ""  # raison par defaut, courte, sans secret


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()[:8]


def stamp():
    """Heure REELLE : un .bak horodate dans le futur se voit a l'audit."""
    return datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")


def rec(action, path, av, ap, raison, bak="-"):
    if not os.path.exists(J):
        io.open(J, "w", encoding="utf-8", newline="").write("# MODIFS %s - hermes\r\n" % datetime.date.today())
    line = "%s | hermes | %s | %s | avant=%s apres=%s | %s ; bak : %s\r\n" % (
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), action, path, av, ap, raison, bak)
    io.open(J, "a", encoding="utf-8", newline="").write(line)


def edit(path, pairs, raison=RAISON):
    """Remplace chaque motif EXACTEMENT une fois. Sinon n'ecrit rien."""
    t = io.open(path, encoding="utf-8").read()
    for old, new in pairs:
        n = t.count(old)
        if n != 1:
            print("REFUS %s : motif present %d fois -> %s" % (path, n, old[:70]))
            return None
    av = md5(path)
    bak = path + ".bak_" + stamp()
    shutil.copy2(path, bak)
    for old, new in pairs:
        t = t.replace(old, new)
    io.open(path, "w", encoding="utf-8", newline="").write(t)
    ap = md5(path)
    if av == ap:  # aucun changement reel : pas de ligne MODIFIE
        print("AUCUN CHANGEMENT sur %s (MD5 identique) : pas de ligne de journal" % path)
        return None
    rec("MODIFIE", path, av, ap, raison, os.path.basename(bak))
    print("%s : %s -> %s | %s" % (path, av, ap, os.path.basename(bak)))
    return av, ap


def corbeille(path, dossier=False):
    """Suppression par la corbeille Windows, jamais seche. Recontrole apres."""
    fn = "DeleteDirectory" if dossier else "DeleteFile"
    ps = ("Add-Type -AssemblyName Microsoft.VisualBasic; "
          "[Microsoft.VisualBasic.FileIO.FileSystem]::%s('%s','OnlyErrorDialogs','SendToRecycleBin')" % (fn, path))
    subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True)
    ok = not os.path.exists(path)
    print("corbeille %s : parti=%s" % (path, ok))
    return ok


if __name__ == "__main__":
    # --- adapter : un appel par fichier
    EDITS = [
        # (r"D:\hermes\skills\<categorie>\<skill>\SKILL.md", [("ancien texte", "nouveau texte")], "raison courte"),
    ]
    for path, pairs, raison in EDITS:
        edit(path, pairs, raison)
