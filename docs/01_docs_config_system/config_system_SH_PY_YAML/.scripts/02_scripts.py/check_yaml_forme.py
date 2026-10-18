#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Controle de forme des YAML de configuration Home Assistant.

Recupere le 2026-09-29 depuis l'etape 3 du WORKFLOW_REBUILD.md supprime,
et remis en etat : le dossier est desormais un argument (le workflow pointait
sur un chemin bidon "/path/to/TREE_CORRIGE" qui n'existait plus).

Usage :
    python check_yaml_forme.py [dossier]

Defaut : docs/01_docs_config_system/config_system_SH_PY_YAML du dossier ReBuild,
ou le dossier /config si on l'execute sur la machine HA.

Trois controles, issus des regles YAML du CLAUDE.md :
  1. en-tete secondaire colle : "#|", "#+" ou "#" suivi d un trait de boite (cadre) au lieu de "# |".
     Un "#" suivi d une lettre (code commente, commentaire simple) n est pas une anomalie.
  2. boites ASCII dont le haut, le titre et le bas n'ont pas la meme largeur
  3. reference obsolete P3_01_somme_par_piece (renommee P3_POWER_2_TOTAL_MULTI_ZONE)

Fichiers ignores : les sauvegardes (.bak_...) et tout nom contenant une date AAAA-MM-JJ ou AAAA_MM_JJ.
Largeur des boites : le cadre standard est 78 (principal) et 37 (secondaire), mais une boite peut etre
plus large quand le titre ne tient pas dans 78. Seul l alignement haut/titre/bas est controle.

Sortie : une ligne par anomalie, puis un compte. Code de retour 1 si anomalie.
"""
import os
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

DEFAUT_LOCAL = os.path.join("docs", "01_docs_config_system", "config_system_SH_PY_YAML")
OBSOLETE = "P3_01_somme_par_piece"
DATE_NOM = re.compile(r"\d{4}[-_]\d{2}[-_]\d{2}")  # sauvegardes et copies datees : ignorees


def analyser(dossier):
    soucis = []
    for base, _, fichiers in os.walk(dossier):
        for nom in sorted(fichiers):
            if not nom.endswith(".yaml") or ".bak_" in nom or DATE_NOM.search(nom):
                continue
            plein = os.path.join(base, nom)
            rel = os.path.relpath(plein, dossier).replace("\\", "/")
            try:
                lignes = open(plein, encoding="utf-8").read().splitlines()
            except Exception as e:
                soucis.append(("ILLISIBLE", rel, 0, str(e)))
                continue

            # 1. en-tete secondaire sans espace apres le diese
            for i, l in enumerate(lignes, 1):
                if re.match(r"^#[|+\u2500-\u257f]", l):
                    soucis.append(("ENTETE_COLLE", rel, i, l[:60]))

            # 2. alignement des boites ASCII
            for i in range(len(lignes) - 2):
                haut, titre, bas = (lignes[i].rstrip(), lignes[i + 1].rstrip(), lignes[i + 2].rstrip())
                if haut.startswith("#") and bas.startswith("#") and haut.endswith(tuple("\u256e╮┐")) \
                        and bas.endswith(tuple("\u256f╯┘")):
                    if len(haut) != len(titre) or len(bas) != len(titre):
                        soucis.append(("BOITE_DECALEE", rel, i + 1,
                                       "%d / %d / %d" % (len(haut), len(titre), len(bas))))

            # 3. reference obsolete, hors journal d annotations
            dans_annot = False
            for i, l in enumerate(lignes, 1):
                if "# annotations_log:" in l:
                    dans_annot = True
                if not dans_annot and OBSOLETE in l:
                    soucis.append(("REF_OBSOLETE", rel, i, l.strip()[:60]))
    return soucis


def main():
    dossier = sys.argv[1] if len(sys.argv) > 1 else DEFAUT_LOCAL
    if not os.path.isdir(dossier):
        print("dossier introuvable : %s" % dossier)
        return 2
    soucis = analyser(dossier)
    for type_, rel, ligne, detail in soucis:
        print("  [%s] %s:%s  %s" % (type_, rel, ligne, detail))
    print("")
    if not soucis:
        print("RESULTAT : %s - aucune anomalie" % dossier)
        return 0
    print("RESULTAT : %s - %d anomalie(s)" % (dossier, len(soucis)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
