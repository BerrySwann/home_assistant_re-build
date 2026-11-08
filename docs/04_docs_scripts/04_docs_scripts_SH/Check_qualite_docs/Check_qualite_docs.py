# -*- coding: utf-8 -*-
"""Check_qualite_docs.py - controle de VALIDITE avant le push 5C de /histo.

Un fichier qui echoue est EXCLU du push et signale : il ne bloque PAS la session
(regle des garde-fous du 2026-11-03). Les autres fichiers partent.

Deux tests, dans cet ordre :
  1. octets de controle : tout octet < 0x20 sauf tabulation, CR et LF ;
  2. parse YAML reel     : yaml.safe_load sur chaque .yaml du perimetre.

POURQUOI CE CONTROLE EXISTE (2026-11-08) : MD5 compare deux etats, il ne dit rien
de leur QUALITE. Une corruption identique en local, en prod et sur GitHub donne
trois empreintes concordantes, donc trigul SYNC et Check_prod_fonctionnelle en
colonnes vertes. C'est arrive : six fichiers portaient des sequences d'echappement
interpretees (backslash-0 -> NUL, backslash-a -> BEL, backslash-b -> BS,
backslash-10 -> BS), dont un YAML que yaml.safe_load refusait d'ouvrir, present
aux trois niveaux depuis des semaines et signale par aucun controle.

PORTEE : le LOCAL, jamais la prod. Le local fait foi et la prod recoit ; controler
la prod apres coup revele les degats au lieu de les empecher.

PLACEMENT : en tete du 5C, apres toutes les ecritures et avant le push. Meme
schema que Check_XX_presents.py.

Codes de sortie : 0 OK, 1 ALERTE (ne rien pousser), 2 outil mal arme.
Lecture seule. Ne corrige jamais : il signale.
"""
import os
import sys

try:
    import yaml
except ImportError:
    print("ERREUR : PyYAML absent, controle impossible (code 2)")
    sys.exit(2)

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))))
DOCS = os.path.join(RACINE, "docs")

# hors perimetre : dossiers XX_, 99_, caches, exports historiques jamais touches
EXCLUS_DIRS = {"__pycache__", "node_modules", ".git", "Dashboard_COMPLET"}
EXCLUS_PREFIX = ("XX_", "99_")
EXCLUS_FIN = (".bak", ".pyc", ".log")
EXTENSIONS = (".md", ".yaml", ".yml", ".py", ".sh", ".txt", ".json")
# tabulation (9), LF (10), CR (13) sont legitimes
AUTORISES = {9, 10, 13}


class HAYamlLoader(yaml.SafeLoader):
    """SafeLoader qui accepte les tags Home Assistant sans les interpreter."""


def _tag_ha(loader, tag_suffix, node):
    """!include, !secret, !env_var et compagnie : on rend la valeur brute."""
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node, deep=True)
    return loader.construct_mapping(node, deep=True)


HAYamlLoader.add_multi_constructor("!", _tag_ha)

def perimetre():
    for root, dirs, files in os.walk(DOCS):
        dirs[:] = [d for d in dirs if d not in EXCLUS_DIRS and not d.startswith(EXCLUS_PREFIX)]
        for f in sorted(files):
            if ".bak" in f or f.endswith(EXCLUS_FIN):
                continue
            if not f.endswith(EXTENSIONS):
                continue
            yield os.path.join(root, f)

def test_octets(p):
    """Rend la liste des positions fautives."""
    fautifs = []
    with open(p, "rb") as f:
        b = f.read()
    for i, x in enumerate(b):
        if x < 0x20 and x not in AUTORISES:
            fautifs.append((i, x))
    return fautifs


BOM = b"\xef\xbb\xbf"
# Une BOM est TOLEREE par PyYAML et par Python 3, mais elle casse le JSON et
# certains shells. Sur les autres formats c'est une incoherence, pas une erreur.
EXT_BOM_FATALE = (".json", ".sh")


def test_bom(p, ext):
    """Rend (alerte, info).

    alerte : la BOM casse reellement le format, le fichier est a exclure.
    info   : la BOM est presente mais inoffensive, c'est une incoherence a
             signaler sans bloquer (7 fichiers YAML du depot sont dans ce cas
             au 2026-11-08, et ils se parsent tres bien).

    Detecte aussi les octets NUL en FIN de fichier, qui sont toujours anormaux :
    trois NUL correspondent exactement a la taille d une BOM UTF-8, ce qui
    suggere un outil ayant dimensionne le fichier en comptant la BOM puis ecrit
    le contenu sans elle. Piste non confirmee, mais le remplissage est a retirer.
    """
    with open(p, "rb") as f:
        b = f.read()
    if not b:
        return None, None
    # NUL en fin de fichier : anormal quel que soit le format
    fin = len(b) - len(b.rstrip(b"\x00"))
    if fin:
        return ("NUL en fin de fichier : %d octet(s) de remplissage" % fin), None
    if b.startswith(BOM):
        if ext in EXT_BOM_FATALE:
            return ("BOM UTF-8 sur un %s, ce format ne l accepte pas" % ext), None
        return None, "BOM UTF-8 (inoffensive sur %s)" % ext
    return None, None

def test_yaml(p):
    """Rend un message d'erreur, ou None si le YAML se parse.

    Deux pieges du corpus, qui produisaient trois fausses alertes au premier
    passage (2026-11-08) :
      - les tags Home Assistant !include, !secret, !env_var ne sont pas du YAML
        standard : safe_load leve ConstructorError. On les ACCEPTE, ils sont
        normaux dans ce depot ;
      - certains fichiers contiennent plusieurs documents separes par --- :
        safe_load leve ComposerError. On utilise load_all.
    Un YAML HA qui echoue ICI est donc vraiment casse, pas simplement exotique.
    """
    try:
        with open(p, encoding="utf-8") as f:
            for _ in yaml.load_all(f, Loader=HAYamlLoader):
                pass
        return None
    except Exception as e:
        return f"{type(e).__name__}: {str(e).splitlines()[0][:90]}"

def main():
    if not os.path.isdir(DOCS):
        print(f"ERREUR : dossier docs introuvable : {DOCS} (code 2)")
        return 2

    alertes_octets = []
    alertes_yaml = []
    alertes_bom = []
    infos_bom = []
    n = 0

    for p in perimetre():
        n += 1
        rel = os.path.relpath(p, RACINE).replace("\\", "/")
        fautifs = test_octets(p)
        if fautifs:
            detail = ", ".join(f"{hex(x)}@{i}" for i, x in fautifs[:6])
            alertes_octets.append((rel, len(fautifs), detail))
            continue  # un fichier avec octets de controle ne se parse pas utilement
        bom_alerte, bom_info = test_bom(p, os.path.splitext(p)[1].lower())
        if bom_alerte:
            alertes_bom.append((rel, bom_alerte))
            continue
        if bom_info:
            infos_bom.append((rel, bom_info))
        if p.endswith((".yaml", ".yml")):
            err = test_yaml(p)
            if err:
                alertes_yaml.append((rel, err))

    print(f"Check_qualite_docs - {n} fichiers du perimetre docs")

    if alertes_octets:
        print(f"\n1. OCTETS DE CONTROLE : {len(alertes_octets)} fichier(s)")
        for rel, nb, detail in alertes_octets:
            print(f"   {rel} | {nb} octet(s) | {detail}")

    if alertes_yaml:
        print(f"\n2. YAML INVALIDE : {len(alertes_yaml)} fichier(s)")
        for rel, err in alertes_yaml:
            print(f"   {rel} | {err}")

    if alertes_bom:
        print(f"\n3. BOM FATALE OU REMPLISSAGE : {len(alertes_bom)} fichier(s)")
        for rel, msg in alertes_bom:
            print(f"   {rel} | {msg}")

    if infos_bom:
        print(f"\nINFO - BOM inoffensive : {len(infos_bom)} fichier(s), non bloquant")
        for rel, msg in infos_bom[:10]:
            print(f"   {rel} | {msg}")
        if len(infos_bom) > 10:
            print(f"   ... et {len(infos_bom) - 10} autres")

    if alertes_octets or alertes_yaml or alertes_bom:
        fautifs = sorted({rel for rel, *_ in alertes_octets}
                         | {rel for rel, *_ in alertes_yaml}
                         | {rel for rel, *_ in alertes_bom})
        print("\nA EXCLURE DU PUSH : %d fichier(s)" % len(fautifs))
        for rel in fautifs:
            print("   ", rel)
        print("\nLes autres fichiers partent normalement. Signaler ces fichiers a Eric (code 1).")
        return 1

    print("\noctets de controle : aucun")
    print("BOM fatale ou remplissage : aucun")
    print("YAML invalide : aucun")
    print("RESULTAT : OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
