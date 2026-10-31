# -*- coding: utf-8 -*-
r"""gen_global_index_ia.py - genere docs/00_IA/ : tous les fichiers de docs/00_IA
(00_IA_CONTEXT_BASE/ et 00_IA_SOUS_CONTEXT_IA/*/), qui s'en sert, a quoi ils servent, avec les liens.

Lecture seule sur la prod (H:\docs\00_IA) et sur CLAUDE.md. Ecrit uniquement IA_GLOBAL_INDEX_memoire.md
(sauvegarde .bak_AAAA_MM_JJ_HHhMMmSSs.md avant ecrasement si le contenu change).
Les descriptions (qui / but / quand) sont dans DESC ci-dessous : un fichier sans description est signale.
Usage : $env:PYTHONIOENCODING='utf-8'; python -I gen_global_index_ia.py [--dry]
"""
import os, re, sys, hashlib, shutil, datetime
from urllib.parse import quote, unquote

ROOT = r"C:\Users\Berry Swann\Documents\ReBuild"
IA = os.path.join(ROOT, "docs", "00_IA")
OUTDIR = os.path.join(IA, "00_IA_GLOBAL_INDEX_memoire")
OUT = os.path.join(OUTDIR, "IA_GLOBAL_INDEX_memoire.md")
OUT_REL = "00_IA_GLOBAL_INDEX_memoire/IA_GLOBAL_INDEX_memoire.md"
PROD = r"H:\docs\00_IA"
CLAUDE_MD = os.path.join(ROOT, "Claude md SAVE", "CLAUDE.md")
CHECK_PY = os.path.join(ROOT, "docs", "04_docs_scripts", "04_docs_scripts_SH", "check_sous_context_ia", "check_sous_context_ia.py")
NON_POUSSES = {"DEPENDANCES_GLOBALES_CLAUDE_memoire.bak_2026_09_28", "DEPENDANCES_GLOBALES_CLAUDE_memoire.bak_2026_10_07", "DEPENDANCES_GLOBALES_CLAUDE_memoire.bak_2026_10_07(1)"}
DRY = "--dry" in sys.argv

# chemin relatif a docs/00_IA (avec /) -> (qui, but, quand)
DESC = {
 "00_IA_SOUS_CONTEXT_IA/IA_NOM_DES_REPERTOIRES_ET_FICHIERS/IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md": (
  "Claude et Hermes (qui s'aligne dessus) pour nommer les dossiers et fichiers de docs ; Eric pour valider les regles",
  "Regles de nommage des repertoires et des fichiers du dossier docs (poles, abreviations, accents, niveaux, releve des ecarts a renommer). Copie du maitre historique/IA_NOM_DES_REPERTOIRES_ET_FICHIERS.md ; statut brouillon a valider par Eric.",
  "Avant de creer, renommer ou deplacer un fichier ou un dossier de docs ; pour savoir quels noms sont encore en ecart."),
 "00_IA_CONTEXT_BASE/IA_CONTEXT_BASE.md": (
  "Claude (c'est son CLAUDE.md local), Hermes et toute IA du projet ; Eric pour relire les regles. Tenu identique en 3 emplacements (voir son en-tete)",
  "Directives IA completes : regles de codage YAML, nomenclature, hierarchie visuelle, arborescences, protocoles, regle de sauvegarde. Meme contenu que le CLAUDE.md local.",
  "Quand une IA doit travailler dans le projet : c'est le contexte de base, les sous-contextes ci-dessous le completent."),
 "00_IA_SOUS_CONTEXT_IA/IA_ARBO_DETAIL/IA_ARBO_DETAIL.md": (
  "Claude, via /update-arbo et /histo (etape 6)",
  "Arborescences completes local, prod et GitHub avec les comptages de fichiers, URLs raw GitHub.",
  "Audit de fichiers, synchro GitHub, recherche d'un fichier en prod, verification de l'arborescence locale."),
 "00_IA_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS/IA_CARTE_EMPLACEMENTS.md": (
  "Claude et les skills qui copient ou comparent des fichiers (histo, ha-push-yaml, ha-push-docs, ha-trigul...)",
  "Carte unique des fichiers presents a plusieurs emplacements (local, prod racine, prod miroir docs, GitHub racine et docs/) et regles de correspondance ; script de controle Verif_emplacements.py.",
  "Avant un push de config, de GLOBAL_INDEX_REPO ou de README, ou un controle local / prod / GitHub."),
 "00_IA_SOUS_CONTEXT_IA/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE/IA_AUDIT_ENERGETIQUE_ET_THERMIQUE.md": (
  "Claude, en mode expert audit energetique",
  "Prompt expert : caracteristiques du logement, equipements, methodes d'analyse, missions et format du rapport d'audit conso et thermique.",
  "Audit de consommation, analyse DUT par piece, efficacite isolation/volets/rideaux, ecart entre la theorie des YAML et les logs reels."),
 "00_IA_SOUS_CONTEXT_IA/IA_AUTOMATIONS_NOTIFS/IA_AUTOMATIONS_NOTIFS.md": (
  "Claude, pour ecrire ou modifier des automations et des notifications",
  "Regles de codage des automations et referentiel des notifications de la prod (canaux, titres, messages, fichiers log).",
  "Creation ou modification d'une automation, ecriture d'un message notify, script HA."),
 "00_IA_SOUS_CONTEXT_IA/IA_CMD_TERMINAL_HA/IA_CMD_TERMINAL_HA.md": (
  "Claude et Eric, pour les commandes a lancer sur HA",
  "Commandes terminal HA : commande tree prod, audits MD5, sauvegarde git vers GitHub, logs, chemins /homeassistant/.",
  "Lancer un audit ou un backup, lire un log, retrouver un chemin /homeassistant/."),
 "00_IA_SOUS_CONTEXT_IA/IA_INDEX_AUTOMATIONS/IA_INDEX_AUTOMATIONS.md": (
  "Claude, pour tenir l'index des automations",
  "Comment les automations sont indexees (index genere et resume de GLOBAL_INDEX_REPO), arborescence locale, comptage par categorie, procedure de mise a jour.",
  "Ajout, suppression ou renommage d'une automation, regeneration de l'index."),
 "00_IA_SOUS_CONTEXT_IA/IA_INDEX_NAVIGATION/IA_INDEX_NAVIGATION.md": (
  "Claude, pour tenir l'index du dashboard",
  "Comment la navigation du dashboard est indexee (index genere et section 02 de GLOBAL_INDEX_REPO), arborescence, chemins GitHub, limites connues.",
  "Ajout d'une vignette ou d'une page, mapping des entites vers leurs fichiers sources."),
 "00_IA_SOUS_CONTEXT_IA/IA_INTEGRATIONS_CARTES/IA_INTEGRATIONS_CARTES.md": (
  "Claude, pour valider un YAML de dashboard",
  "Referentiel des integrations HA (HACS, core, add-ons), des cartes du dashboard et de la palette de couleurs.",
  "YAML dashboard a valider, type custom:* inconnu, integration manquante, nouvelle carte a ajouter."),
 "00_IA_SOUS_CONTEXT_IA/IA_P4_PRESENCE/IA_P4_PRESENCE.md": (
  "Claude, pour les automations et messages qui dependent de la presence",
  "Referentiel de la presence : logique de sensor.groupe (automatisation, reseau cible) et de sensor.presence (format dans les notifications).",
  "Automation clim, message notify avec presence, logique groupe WiFi."),
  "00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.bak_2026_09_28.md": (
   "Personne en usage courant ; Eric pour retrouver un ancien etat",
   "Archive de la chaine de dependances au 2026-09-28, date de fin de la tenue manuelle annoncee dans son en-tete (la carte vivante etait alors DEPENDANCES_GLOBALES_HERMES_V1.md). Conservee pour son journal et ses constats.",
   "Seulement pour retrouver un ancien constat ou le journal d une date. Pas une reference technique."),
  "00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.bak_2026_10_07.md": (
   "Personne en usage courant ; Eric pour retrouver un ancien etat",
   "Archive de la chaine de dependances, etat du 2026-10-07 18h13 (derniere mise a jour citee en tete : 2026-10-04 S3).",
   "Seulement pour retrouver un ancien constat ou le journal d une date. Pas une reference technique."),
  "00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.bak_2026_10_07(1).md": (
   "Personne en usage courant ; Eric pour retrouver un ancien etat",
   "Archive de la chaine de dependances, etat du 2026-10-07 19h20 (derniere mise a jour citee en tete : 2026-10-07, automation D watchdog SdB).",
   "Seulement pour retrouver un ancien constat ou le journal d une date. Pas une reference technique."),
  "00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md": (
   "Claude (il la tient a jour via /sync_index et /histo) ; Hermes a sa propre version dans docs/XX_docs_MD_system/DEPENDANCES_GLOBALES_HERMES",
   "Chaine de dependances du dashboard : matrice des 18 vignettes, entites, fichiers et automations par domaine, scripts, fichiers config racine. Citee par IA_CONTEXT_BASE, IA_ARBO_DETAIL, IA_INDEX_NAVIGATION et IA_NOM_DES_REPERTOIRES_ET_FICHIERS.",
   "Apres validation d un YAML, d une automation ou d une vignette ; pour savoir quelles entites et quels fichiers dependent d une vignette."),
 "00_IA_SOUS_CONTEXT_IA/IA_SKILLS_INVENTAIRE/IA_SKILLS_INVENTAIRE.md": (
  "Eric, et Claude ou Hermes pour aligner les skills",
  "Inventaire des skills Hermes regroupees par sujet, avec les skills communes a Claude en face a face.",
  "Savoir quelle skill existe, aligner les skills de Claude et d'Hermes. Pas dans la table de lecture de CLAUDE.md, pas pousse en prod."),
}

# autres index globaux du projet : (libelle, chemin relatif a docs/00_IA, qui le tient, controle)
AUTRES = [
 ("GLOBAL_INDEX_REPO.md", "../01_docs_config_system/01_config_system_MD/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md", "Index du depot GitHub, liens depuis la racine du depot. Tenu a la main par /histo (sync_index) ; a pousser aux 2 endroits de la prod (racine et miroir docs).", "check_global_index.py"),
 ("GLOBAL_INDEX_AUTOMATIONS.md", "../03_docs_automations/GLOBAL_INDEX_AUTOMATIONS.md", "Genere par gen_global_index_automations.py.", "etape 8 de /histo + check_global_index.py"),
 ("GLOBAL_INDEX_VIGNETTES_PAGES.md", "../02_docs_dashboard/GLOBAL_INDEX_VIGNETTES_PAGES.md", "Genere par gen_global_index_vignettes_pages.py.", "etape 9 de /histo + check_global_index.py"),
 ("GLOBAL_INDEX_SCRIPTS_SH.md", "../04_docs_scripts/GLOBAL_INDEX_SCRIPTS_SH.md", "Genere par gen_global_index_scripts.py (scripts bash et python).", "etape 10 de /histo + check_global_index.py"),
 ("GLOBAL_INDEX_SCRIPTS_YAML.md", "../04_docs_scripts/GLOBAL_INDEX_SCRIPTS_YAML.md", "Genere par gen_global_index_scripts.py (scripts Home Assistant).", "etape 10 de /histo + check_global_index.py"),
 ("ENTITES_GLOBAL_INDEX.md", "../XX_docs_MD_system/ENTITES_GLOBAL_INDEX/ENTITES_GLOBAL_INDEX.md", "Index des entites, sans generateur : tenu a la main.", "check_global_index.py"),
 ("IA_GLOBAL_INDEX_memoire.md", "00_IA_GLOBAL_INDEX_memoire/IA_GLOBAL_INDEX_memoire.md", "Ce fichier, genere par gen_global_index_ia.py.", "etape 11 de /histo + check_global_index.py"),
]
RX_BAK = re.compile(r"\.bak_\d{4}_\d{2}_\d{2}")
RX_GEN = re.compile(r"^.*(Fichier GENERE le|img.shields.io/badge/M.J-).*$", re.M)
RX_LINK = re.compile(r"\]\(([^)]+)\)")


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def link(label, rel):
    rel = rel.replace("\\", "/")
    r2 = os.path.relpath(os.path.normpath(os.path.join(IA, rel)), OUTDIR).replace("\\", "/")
    if rel.endswith("/"):
        r2 = r2.rstrip("/") + "/"
    return "[%s](%s)" % (label, quote(r2, safe="/.:_-()"))


def read(p):
    with open(p, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def md5(p):
    h = hashlib.md5()
    with open(p, "rb") as fh:
        h.update(fh.read())
    return h.hexdigest()


def scan():
    """Retourne (contenus, baks) : contenus = liste de chemins relatifs a IA (avec /), baks = dict dossier -> nb."""
    contenus, baks = [], {}
    for dp, dn, fn in os.walk(IA):
        dn.sort()
        for n in sorted(fn):
            full = os.path.join(dp, n)
            rel = os.path.relpath(full, IA).replace("\\", "/")
            dossier = os.path.dirname(rel) or "."
            if RX_BAK.search(n):
                baks[dossier] = baks.get(dossier, 0) + 1
            elif rel != OUT_REL:
                contenus.append(rel)
    return contenus, baks


def prod_etat(rel, prod_ok):
    stem = os.path.splitext(os.path.basename(rel))[0]
    if stem in NON_POUSSES:
        return "non pousse (voulu)"
    if not prod_ok:
        return "H: inaccessible"
    p = os.path.join(PROD, rel.replace("/", os.sep))
    if not os.path.exists(p):
        return "absent en prod"
    return "OK (MD5 identique)" if md5(p) == md5(os.path.join(IA, rel.replace("/", os.sep))) else "DIFFERENT de la prod"


def ligne(rel, prod_ok, claude_txt, manques):
    nom = os.path.basename(rel)
    stem = os.path.splitext(nom)[0]
    d = DESC.get(rel)
    if d is None:
        manques.append(rel)
        d = ("A DECRIRE", "A DECRIRE", "A DECRIRE")
    dans = "oui" if stem in claude_txt else "non"
    return "| %s | %s | %s | %s | %s | %s |" % (
        link(nom, rel), esc(d[0]), esc(d[1]), esc(d[2]), dans, prod_etat(rel, prod_ok))


ENTETE_T = "| Fichier | Qui s'en sert | Son but | Quand le lire | Cite dans CLAUDE.md | Prod |\n|---|---|---|---|---|---|"

def build(now):
    contenus, baks = scan()
    prod_ok = os.path.isdir(PROD)
    claude_txt = read(CLAUDE_MD) if os.path.exists(CLAUDE_MD) else ""
    manques = []
    base = [r for r in contenus if r.startswith("00_IA_CONTEXT_BASE/")]
    sous = [r for r in contenus if r.startswith("00_IA_SOUS_CONTEXT_IA/")]
    autres_fichiers = [r for r in contenus if r not in base and r not in sous]
    nb_baks = sum(baks.values())
    L = []
    L.append("# IA_GLOBAL_INDEX_memoire - index des fichiers de docs/00_IA")
    L.append("")
    L.append('<div align="center">')
    L.append("")
    _day = datetime.datetime.now().strftime("%Y--%m--%d")
    _bd = [("Statut", "Actif", "0f9d58"), ("M\u00e0J", _day, "44739e"),
           ("HA", "2026.10.4", "03a9f4&logo=home-assistant&logoColor=white"),
           ("IA_Partner", "Claude_Sonnet_5.5", "blueviolet"), ("Source", "Interne", "2196f3"),
           ("Modifs", "Script_seul", "ff9800"), ("Expert", "HAOS_Proxmox", "success"),
           ("Type", "Index_genere", "ff9800")]
    for _i, (_a, _b, _c) in enumerate(_bd):
        _sep = "?style=flat-square" if "&" not in _c else "&style=flat-square"
        _c2 = _c.replace("&logo", "?logo", 1) if "&" in _c else _c
        _sep = "&style=flat-square" if "?" in _c2 else "?style=flat-square"
        L.append("[![%s](https://img.shields.io/badge/%s-%s-%s%s)](.)%s" % (_a, _a, _b, _c2, _sep, "&nbsp;" if _i < len(_bd) - 1 else ""))
    L.append("")
    L.append("</div>")
    L.append("")
    L.append("> Fichier GENERE le %s par gen_global_index_ia.py - ne pas editer a la main (relancer le script ou /histo)." % now)
    L.append("> %d fichiers de contenu, %d sauvegardes (.bak), %d sans description." % (len(contenus), nb_baks, 0))
    _s = "\U0001F6A8"
    L.append("")
    L.append("> %s%s%s **GYROPHARE ROUGE - DANS HOME ASSISTANT TOUT EST A PLAT** %s%s%s" % ((_s,) * 6))
    L.append(">")
    L.append("> - Un script est en `/config/.scripts/<fichier>` (aucun sous-dossier) ; un YAML command_line est en `/config/command_line/<categorie>/<fichier>` (un seul niveau).")
    L.append("> - Le rangement par dossier (`<nom>_<extension>`) existe UNIQUEMENT en local (ReBuild) et dans le miroir docs de la prod. NE JAMAIS pousser ces dossiers tels quels vers `/config` : les `shell_command` appellent des chemins absolus plats, et un YAML pousse en double serait charge deux fois.")
    L.append("> - Avant tout push vers la prod racine : aplatir le chemin. Explication complete (arbre local trie, liste a plat, cascades bouton -> script -> fonction) : section SCRIPTS ET COMMAND_LINE de %s." % link("DEPENDANCES_GLOBALES_CLAUDE_memoire.md", "00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md"))
    L.append("")
    L.append("## A quoi sert ce fichier")
    L.append("")
    L.append("Liste de tous les fichiers de docs/00_IA (le dossier des directives pour les IA), avec pour chacun : qui s'en sert, son but, quand le lire, et un lien. "
             "Il sert a Claude et Hermes pour savoir quel sous-contexte charger, et a Eric pour retrouver ou est quoi. "
             "Les descriptions viennent de la table de lecture de CLAUDE.md et de l'en-tete de chaque fichier ; les sauvegardes (.bak) ne sont pas listees une par une.")
    L.append("")
    L.append("## Contexte de base (00_IA_CONTEXT_BASE)")
    L.append("")
    L.append(ENTETE_T)
    for r in base:
        L.append(ligne(r, prod_ok, claude_txt, manques))
    L.append("")
    L.append("## Sous-contextes (00_IA_SOUS_CONTEXT_IA)")
    L.append("")
    L.append("Un dossier par fichier. Chargés a la demande : Claude ne les lit que si la tache le demande (colonne Quand le lire).")
    L.append("")
    L.append(ENTETE_T)
    for r in sous:
        L.append(ligne(r, prod_ok, claude_txt, manques))
    L.append("")
    L.append("## Memoires de Claude (00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire)")
    L.append("")
    L.append(ENTETE_T)
    for r in autres_fichiers:
        L.append(ligne(r, prod_ok, claude_txt, manques))
    L.append("")
    L.append("## Sauvegardes (.bak)")
    L.append("")
    L.append("Copies datees a cote de chaque fichier (regle de sauvegarde de CLAUDE.md : 10 max le jour meme, 3 les jours precedents, menage par /histo). Jamais poussees en prod.")
    L.append("")
    L.append("| Dossier | Nombre de sauvegardes |")
    L.append("|---|---|")
    for d in sorted(baks):
        lien = link("00_IA (racine)" if d == "." else d, "./" if d == "." else d + "/")
        L.append("| %s | %d |" % (lien, baks[d]))
    L.append("")
    L.append("## Les autres index globaux du projet")
    L.append("")
    L.append("Tous sont verifies par /histo (liens casses, existence, prod).")
    L.append("")
    L.append("| Index | Role | Verification |")
    L.append("|---|---|---|")
    for lib, rel, role, ctrl in AUTRES:
        L.append("| %s | %s | %s |" % (link(lib, rel), esc(role), esc(ctrl)))
    L.append("")
    txt = "\n".join(L) + "\n"
    txt = txt.replace("%d sans description." % 0, "%d sans description%s." % (len(manques), " (voir A DECRIRE)" if manques else ""))
    return txt, manques


def casses_de(txt):
    n = 0
    cas = []
    for m in RX_LINK.finditer(txt):
        t = m.group(1)
        if t.startswith(("http://", "https://", "#", "mailto:")):
            continue
        n += 1
        if unquote(t) != "IA_GLOBAL_INDEX_memoire.md" and not os.path.exists(os.path.normpath(os.path.join(OUTDIR, unquote(t)))):
            cas.append(t)
    return n, cas


def avec_badges(texte, path):
    """Banniere des 8 badges via Check_badges_fiches.reconstruire (regle unique, ordre d'Eric le 2026-10-31 : badges partout sauf .bak anciens)."""
    sys.path.insert(0, r"C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_SH\Check_badges_fiches")
    import Check_badges_fiches as cb
    rel = os.path.relpath(path, r"C:\Users\Berry Swann\Documents\ReBuild\docs")
    if cb.SKIP.search(rel):
        return texte
    ha = cb.ha_version()
    if not ha:
        print("ATTENTION : H:\\.HA_VERSION illisible, badge HA absent pour " + rel)
    nt = cb.reconstruire(texte, {}, cb.ORDRE, rel, ha)
    if nt is None:
        print("ATTENTION : badges non ajoutes pour " + rel)
        return texte
    return nt


def sans_maj(s):
    return re.sub(r"M.J-\d{4}--\d{2}--\d{2}", "MaJ-X", s)

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    txt, manques = build(now)
    liens, cas = casses_de(txt)
    txt = avec_badges(txt, OUT)  # apres le controle des liens
    ancien = read(OUT) if os.path.exists(OUT) else None
    change = ancien is None or sans_maj(RX_GEN.sub("", ancien)) != sans_maj(RX_GEN.sub("", txt))
    if DRY:
        print("[DRY] ecriture %s" % ("necessaire" if change else "inutile (contenu identique)"))
    elif change:
        if ancien is not None:
            ts = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")
            shutil.copy2(OUT, os.path.join(OUTDIR, "IA_GLOBAL_INDEX_memoire.bak_%s.md" % ts))
        with open(OUT, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(txt)
        print("ecrit : %s" % OUT)
    else:
        print("inchange : %s" % OUT)
    for m in manques:
        print("SANS DESCRIPTION : %s" % m)
    for c in cas:
        print("LIEN CASSE : %s" % c)
    print("liens=%d casses=%d sans_description=%d" % (liens, len(cas), len(manques)))
    return 1 if (cas or manques) else 0


if __name__ == "__main__":
    sys.exit(main())