"""Verifie une ecriture : MD5, taille, lignes physiques, octets de controle, non-ASCII.

Usage : python verif_ecriture.py FICHIER [FICHIER ...]
Code retour 1 si un fichier contient un octet de controle (ecriture corrompue),
2 si un fichier est illisible, 0 sinon.

Un fichier de journal ou de message doit sortir avec lignes=2 (entete + 1 ligne)
et controle=aucun. Tout 0x01, 0x03 ou saut de ligne supplementaire signale un
antislash mange par une sequence d'echappement : restaurer le .bak et reecrire.
"""
import hashlib
import io
import sys


def rapport(path):
    raw = open(path, 'rb').read()
    texte = io.open(path, encoding='utf-8', errors='replace').read()
    ctrl = sorted(set(hex(ord(c)) for c in texte if ord(c) < 9 or 13 < ord(c) < 32))
    non_ascii = sorted(set(c for c in texte if ord(c) > 126))
    ligne = "%-64s md5=%s taille=%d lignes=%d controle=%s nonascii=%d" % (
        path,
        hashlib.md5(raw).hexdigest()[:8],
        len(raw),
        len(texte.splitlines()),
        ctrl if ctrl else "aucun",
        len(non_ascii),
    )
    return ligne, bool(ctrl)


def main(args):
    if not args:
        print(__doc__)
        return 2
    code = 0
    for path in args:
        try:
            ligne, a_ctrl = rapport(path)
        except Exception as exc:
            print("%-64s ERREUR %s" % (path, exc))
            code = 2
            continue
        print(ligne)
        if a_ctrl and code == 0:
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
