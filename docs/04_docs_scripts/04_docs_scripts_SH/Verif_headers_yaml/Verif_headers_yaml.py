#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verification des en-tetes des YAML de configuration Home Assistant (LECTURE SEULE).

Cree le 2026-10-20 sur demande d'Eric. Normes : Claude md SAVE\\CLAUDE.md, sections 4 (bordures ASCII),
5 (headers obligatoires), 7 (slug tertiaire), 8 (name et unique_id).

Usage :
    python verif_headers_yaml.py [dossier ou fichier] [--erreurs] [--prefixe]

Defaut : docs/01_docs_config_system/01_config_system_SH_PY_YAML (chemin calcule depuis l emplacement du script).
--erreurs : n'affiche que les ERREUR (pas les AVIS).
--prefixe : controle aussi le prefixe de pole dans name (desactive par defaut : regle tres peu suivie).

Deux niveaux :
  ERREUR (structure, a corriger) : BOITE_DECALEE (haut/titre/bas de largeur differente), BOITE_TROP_ETROITE
      (le titre depasse la boite), ENTETE_COLLE, BOITE_PRINCIPALE_ABSENTE, HEADER_ABSENT, HEADER_ORDRE,
      SLUG_ABSENT, SLUG_DIFFERENT, ID_DOUBLON, ID_FORMAT.
  AVIS (convention, a juger) : BOITE_COINS (arrondis pour le principal, carres pour le secondaire),
      BOITE_LARGEUR (principal < 78, secondaire < 37, ou boite plus large que necessaire),
      BOITE_MINUSCULES, NUMEROTATION (secondaire : 1 a 9 dans l'ordre), SLUG_ORPHELIN, NOM_ID_DIFFERENT,
      NOM_INITIALE, TABLEAU_DEPENDANCES_ABSENT, PREFIXE_POLE (avec --prefixe).

Largeur des boites : 78 (principal) et 37 (secondaire) sont le cadre standard. Une boite peut etre plus
longue quand le titre ne tient pas : largeur mini = longueur du texte + 5 (+ 6 pour garder un espace avant la barre). Le haut, le titre et le bas
doivent avoir la meme largeur (indentation exclue).

Fichiers ignores : sauvegardes (.bak_), noms contenant une date AAAA-MM-JJ / AAAA_MM_JJ, dossiers
.scripts, scripts, notifs, themes, blueprints, ARCHIVE.
Code de retour : 0 sans ERREUR, 1 avec ERREUR, 2 si le chemin est introuvable.
"""
import os
import re
import sys
import unicodedata

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

TL_R, TR_R, BL_R, BR_R = "\u256d", "\u256e", "\u2570", "\u256f"   # coins arrondis
TL_C, TR_C, BL_C, BR_C = "\u250c", "\u2510", "\u2514", "\u2518"   # coins carres
BARRE, HZ = "\u2502", "\u2500"
DEFAUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "01_docs_config_system",
                      "01_config_system_SH_PY_YAML")
DATE_NOM = re.compile(r"\d{4}[-_]\d{2}[-_]\d{2}")
DOSSIERS_IGNORES = {".scripts", "scripts", "notifs", "themes", "blueprints", "archive", "_archive"}
HEADERS = [("DESCRIPTION", "DESCRIPTION"), ("CALCUL", "CALCUL & SOURCES"), ("CHAINE", "CHAINE DE DEPENDANCES"),
           ("IMPORTANT", "IMPORTANT (PIEGES)"), ("TABLEAU DE BORD", "TABLEAU DE BORD (VIGNETTES PRINCIPALES)")]
RE_TOP = re.compile(r"^(\s*)# ([%s%s])%s+([%s%s])\s*$" % (TL_R, TL_C, HZ, TR_R, TR_C))
RE_BOT = re.compile(r"^(\s*)# ([%s%s])%s+([%s%s])\s*$" % (BL_R, BL_C, HZ, BR_R, BR_C))
RE_TITRE = re.compile(r"^(\s*)# %s (.*?) *%s\s*$" % (BARRE, BARRE))
RE_COLLE = re.compile(r"^\s*#[|+\u2500-\u257f]")
RE_SLUG = re.compile(r"^\s*# --- (\S+) ---\s*$")
RE_UID = re.compile(r"^\s*-?\s*unique_id:\s*[\"']?([^\"'\s#]+)[\"']?\s*(#.*)?$")
RE_NAME = re.compile(r"^\s*-?\s*name:\s*[\"']?(.*?)[\"']?\s*(#.*)?$")
RE_CLE = re.compile(r"^([A-Za-z0-9_]+):\s*(#.*)?$")
CLES_DOMAINE = {"sensor", "binary_sensor", "template", "utility_meter", "command_line", "group", "input_boolean",
                "input_number", "input_text", "input_select", "input_datetime", "input_button", "timer",
                "shell_command", "light", "switch", "counter", "homeassistant", "automation", "script"}


def norm(txt):
    t = unicodedata.normalize("NFKD", txt)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]", "_", t)).strip("_")


def sans_accents_maj(x):
    t = unicodedata.normalize("NFKD", x)
    return "".join(c for c in t if not unicodedata.combining(c)).upper()


def fichiers(chemin):
    if os.path.isfile(chemin):
        yield os.path.dirname(chemin) or ".", os.path.basename(chemin)
        return
    for base, dirs, noms in os.walk(chemin):
        dirs[:] = [d for d in dirs if d.lower() not in DOSSIERS_IGNORES]
        for n in sorted(noms):
            if n.endswith(".yaml") and ".bak_" not in n and not DATE_NOM.search(n):
                yield base, n

def analyser_boites(l, rel, S):
    secondaire_n = 0
    i = 0
    while i < len(l):
        if RE_COLLE.match(l[i]):
            S.append(("ERREUR", "ENTETE_COLLE", rel, i + 1, l[i].strip()[:50]))
        mh = RE_TOP.match(l[i])
        if mh and i + 2 < len(l):
            mt, mb = RE_TITRE.match(l[i + 1]), RE_BOT.match(l[i + 2])
            if mt and mb:
                haut, titre, bas = l[i].strip(), l[i + 1].strip(), l[i + 2].strip()
                principal = mh.group(2) == TL_R
                texte = mt.group(2).strip()
                if not (len(haut) == len(titre) == len(bas)):
                    S.append(("ERREUR", "BOITE_DECALEE", rel, i + 1, "%d / %d / %d" % (len(haut), len(titre), len(bas))))
                else:
                    largeur, mini, std = len(haut), len(texte) + 6, (78 if principal else 37)
                    if largeur < mini - 1:
                        S.append(("ERREUR", "BOITE_TROP_ETROITE", rel, i + 1, "largeur %d, le titre demande au moins %d" % (largeur, mini - 1)))
                    elif largeur < std:
                        S.append(("AVIS", "BOITE_LARGEUR", rel, i + 1, "largeur %d < standard %d" % (largeur, std)))
                    elif largeur > max(std, mini):
                        S.append(("AVIS", "BOITE_LARGEUR", rel, i + 1, "largeur %d, %d suffisait" % (largeur, max(std, mini))))
                rond = (mh.group(2), mh.group(3), mb.group(2), mb.group(3)) == (TL_R, TR_R, BL_R, BR_R)
                carre = (mh.group(2), mh.group(3), mb.group(2), mb.group(3)) == (TL_C, TR_C, BL_C, BR_C)
                if not ((rond and principal) or (carre and not principal)):
                    S.append(("AVIS", "BOITE_COINS", rel, i + 1, "principal = arrondis, secondaire = carres"))
                if texte != texte.upper():
                    S.append(("AVIS", "BOITE_MINUSCULES", rel, i + 1, texte[:50]))
                if not principal:
                    m = re.match(r"^(\d+)\.\s", texte)
                    num = int(m.group(1)) if m else 0
                    if not m or num > 9 or num <= secondaire_n:
                        S.append(("AVIS", "NUMEROTATION", rel, i + 1, "numero 1 a 9 croissant attendu : %s" % texte[:40]))
                    secondaire_n = max(secondaire_n, num)
                i += 3
                continue
        i += 1


def analyser_entete(l, rel, S):
    haut = None
    for k in range(min(len(l), 6)):
        mh = RE_TOP.match(l[k])
        if mh and mh.group(2) == TL_R and not mh.group(1):
            haut = k
            break
    if haut is None:
        S.append(("ERREUR", "BOITE_PRINCIPALE_ABSENTE", rel, 1, "pas de boite a coins arrondis en tete de fichier"))
        return
    bloc = []
    for k in range(haut + 3, len(l)):
        if l[k].strip() and not l[k].lstrip().startswith("#"):
            break
        bloc.append((k + 1, l[k]))
    pos = []
    for cle, libelle in HEADERS:
        n = None
        for num, x in bloc:
            if x.startswith("# ##") and cle in sans_accents_maj(x):
                n = num
                break
        if n is None:
            S.append(("ERREUR", "HEADER_ABSENT", rel, haut + 1, libelle))
        pos.append(n)
    vus = [p for p in pos if p]
    if vus != sorted(vus):
        S.append(("ERREUR", "HEADER_ORDRE", rel, haut + 1, "les 5 headers ne suivent pas l'ordre du CLAUDE.md"))
    if pos[2] and not any("MAT" in sans_accents_maj(x) and "AVAL" in x for _, x in bloc):
        S.append(("AVIS", "TABLEAU_DEPENDANCES_ABSENT", rel, pos[2], "tableau MATERIEL ... AVAL non trouve"))

def trouver_nom(l, i, ids_lignes):
    for d in range(0, 9):
        for idx in ((i,) if d == 0 else (i - d, i + d)):
            if 0 <= idx < len(l):
                if idx != i and (idx in ids_lignes or RE_SLUG.match(l[idx])):
                    continue
                mn = RE_NAME.match(l[idx])
                if mn:
                    return idx, mn.group(1)
    return None


def analyser_ids(l, rel, S, prefixe):
    ids = []
    for i, x in enumerate(l):
        m = RE_UID.match(x)
        if m and "{{" not in m.group(1):
            ids.append((i, m.group(1), "uid"))
    if not ids:
        for i, x in enumerate(l):
            m = RE_CLE.match(x)
            if m and m.group(1) not in CLES_DOMAINE:
                ids.append((i, m.group(1), "cle"))
    ids_lignes = set(i for i, _, _ in ids)
    slugs = [(i, RE_SLUG.match(x).group(1)) for i, x in enumerate(l) if RE_SLUG.match(x)]
    vus, utilises = {}, set()
    for k, (i, uid, genre) in enumerate(ids):
        if uid in vus:
            S.append(("ERREUR", "ID_DOUBLON", rel, i + 1, "%s (deja ligne %d)" % (uid, vus[uid] + 1)))
        vus[uid] = i
        if not re.match(r"^[a-z0-9_]+$", uid):
            S.append(("ERREUR", "ID_FORMAT", rel, i + 1, "%s (minuscules, chiffres, underscores)" % uid))
        prec = ids[k - 1][0] if k else -1
        cand = [s for s in slugs if prec < s[0] < i]
        if not cand:
            S.append(("ERREUR", "SLUG_ABSENT", rel, i + 1, "# --- %s --- manquant" % uid))
        else:
            j, sl = cand[-1]
            utilises.add(j)
            if sl != uid:
                S.append(("ERREUR", "SLUG_DIFFERENT", rel, j + 1, "slug %s, id %s" % (sl, uid)))
        if genre == "uid":
            nom = trouver_nom(l, i, ids_lignes)
            if nom:
                if nom[1][:1].isalpha() and not nom[1][:1].isupper():
                    S.append(("AVIS", "NOM_INITIALE", rel, nom[0] + 1, nom[1][:50]))
                if norm(nom[1]) != uid:
                    S.append(("AVIS", "NOM_ID_DIFFERENT", rel, nom[0] + 1, "%s / %s" % (nom[1][:40], uid)))
                if prefixe:
                    pole = re.match(r"^([A-Z]{1,3}\d?)_", os.path.basename(rel))
                    if pole and not nom[1].upper().startswith(pole.group(1)):
                        S.append(("AVIS", "PREFIXE_POLE", rel, nom[0] + 1, "name sans %s" % pole.group(1)))
    for j, sl in slugs:
        if j not in utilises:
            S.append(("AVIS", "SLUG_ORPHELIN", rel, j + 1, sl))


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    seulement_erreurs = "--erreurs" in sys.argv
    prefixe = "--prefixe" in sys.argv
    chemin = args[0] if args else DEFAUT
    if not os.path.exists(chemin):
        print("chemin introuvable : %s" % chemin)
        return 2
    S, n = [], 0
    for base, nom in fichiers(chemin):
        plein = os.path.join(base, nom)
        rel = os.path.relpath(plein, chemin if os.path.isdir(chemin) else base).replace("\\", "/")
        try:
            l = [unicodedata.normalize("NFC", x) for x in open(plein, encoding="utf-8-sig").read().splitlines()]
        except Exception as e:
            S.append(("ERREUR", "ILLISIBLE", rel, 0, str(e)))
            continue
        n += 1
        analyser_boites(l, rel, S)
        analyser_entete(l, rel, S)
        analyser_ids(l, rel, S, prefixe)
    er = [x for x in S if x[0] == "ERREUR"]
    av = [x for x in S if x[0] == "AVIS"]
    for niv, typ, rel, ligne, det in (er if seulement_erreurs else er + av):
        print("  [%s][%s] %s:%s  %s" % (niv, typ, rel, ligne, det))
    print("")
    comptes = {}
    for x in S:
        comptes[(x[0], x[1])] = comptes.get((x[0], x[1]), 0) + 1
    for (niv, typ), c in sorted(comptes.items()):
        print("  %s %s : %d" % (niv, typ, c))
    print("controle verif_headers: fichiers=%d erreurs=%d avis=%d" % (n, len(er), len(av)))
    return 1 if er else 0


if __name__ == "__main__":
    sys.exit(main())