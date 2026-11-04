# Copie_reference.py - copie de copie_reference.py d Hermes (AppData\Local\hermes\scripts\histo), rangee dans docs sur ordre d Eric le 2026-11-04.
# Fiche : docs\04_docs_scripts\04_docs_scripts_SH_MD\Copie_reference\Copie_reference.md . Interpreteur : python -I -X utf8
# annotations_log:
# [2026-11-04] copie du script d Hermes ; seule difference : alerte() n envoie plus rien elle-meme (pas de jeton HA lu dans le .env
#   d Hermes), elle ecrit une ligne ALERTE A ENVOYER PAR CLAUDE et le code de retour reste 1 en cas d echec.
"""Copie de reference automations, scripts et configuration.yaml (etape du /histo).

Pour chacun des trois fichiers maitres de la prod (H:\\automations.yaml, H:\\scripts.yaml,
H:\\configuration.yaml) :
  1. tout fichier NON date du dossier de destination local est renomme en date, avec sa vraie
     date de modification (on ne lui invente pas la date du jour, son contenu est ancien) ;
  2. une copie de la prod est deposee dans le dossier local - datee pour automations/scripts,
     sous son nom stable pour configuration.yaml qui est le fichier de travail ;
  3. MD5 verifie apres la copie. Si le MD5 ne colle pas, la copie est retiree, le script s'arrete
     la (aucune ligne suivante, aucun redemarrage) et Eric recoit une alerte sur son telephone
     (notify.mobile_app_eric) ET dans les notifications de Home Assistant
     (persistent_notification.create) ;
  4. le plafond du menage des .bak s'applique ensuite normalement a ces copies (10 le jour meme,
     1 par jour passe, 3 au plus).

Aucune ecriture sur H: : la copie se fait de la prod vers le local, le push vers H:\\docs
reste l'affaire du push 5C, sur ordre d'Eric.
"""
import os, re, sys, shutil, hashlib, datetime

CFG = r"C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_SH_PY_YAML"

CIBLES = [
    # (fichier maitre en prod, dossier local, base de nom, nom stable ou None)
    (os.path.join("H:" + os.sep, "automations.yaml"),
     r"C:\Users\Berry Swann\Documents\ReBuild\docs\03_docs_automations\03_docs_automations_YAML\Automations_yaml_original",
     "automations", None),
    (os.path.join("H:" + os.sep, "scripts.yaml"),
     r"C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_script_ORIGINAL",
     "scripts", None),
    # configuration.yaml : le local est un fichier de TRAVAIL stable, pas une copie datee
    (os.path.join("H:" + os.sep, "configuration.yaml"), CFG, "configuration", "configuration.yaml"),
]

DATE_H_T = r"^%s\.bak_(\d{4})_(\d{2})_(\d{2})_(\d{2})h(\d{2})m(\d{2})s\.yaml$"
DATE_J_T = r"^%s\.bak_(\d{4})_(\d{2})_(\d{2})\.yaml$"


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def copies_dates(dossier, base):
    """copies datees presentes, triees de la plus ancienne a la plus recente"""
    rx_h = re.compile(DATE_H_T % re.escape(base), re.I)
    rx_j = re.compile(DATE_J_T % re.escape(base), re.I)
    out = []
    for f in os.listdir(dossier):
        m = rx_h.match(f)
        if m:
            out.append((f, "".join(m.groups())))
            continue
        m = rx_j.match(f)
        if m:
            out.append((f, "".join(m.groups()) + "000000"))
    return sorted(out, key=lambda x: x[1])


def alerte(message, titre="Copie de reference en echec"):
    """Version Claude : aucun jeton lu ici (le script d Hermes lisait son .env). La ligne ALERTE est lue par
    Claude, qui envoie lui-meme notify.mobile_app_eric et persistent_notification.create avec ses outils HA."""
    print("   ALERTE A ENVOYER PAR CLAUDE | %s | %s" % (titre, message))


def traite(prod, dossier, base, stable):
    print("== %s" % base)
    if not os.path.isfile(prod):
        print("   prod introuvable :", prod)
        alerte("%s introuvable en prod (%s). Aucune copie faite, aucun redemarrage." % (base, prod))
        return False
    if not os.path.isdir(dossier):
        print("   dossier local introuvable :", dossier)
        alerte("Dossier local introuvable pour %s (%s). Aucun redemarrage." % (base, dossier))
        return False

    m_prod = md5(prod)

    # --- fichier stable (configuration.yaml) : sauvegarde datee, puis rafraichissement ---
    if stable:
        cible = os.path.join(dossier, stable)
        if os.path.isfile(cible) and md5(cible) == m_prod:
            print("   copie deja a jour :", stable)
            return True
        if os.path.isfile(cible):
            st = os.stat(cible)
            date = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y_%m_%d_%Hh%Mm%Ss")
            bak = os.path.join(dossier, "%s.bak_%s.yaml" % (base, date))
            if not os.path.exists(bak):
                shutil.copy2(cible, bak)
                print("   sauvegarde  ->", os.path.basename(bak))
        shutil.copy2(prod, cible)
        ok = md5(cible) == m_prod
        print("   copie       -> %s  %s" % (stable, "MD5 OK" if ok else "MD5 KO"))
        if not ok:
            alerte("configuration.yaml : MD5 different apres copie (prod %s, local %s). Aucun redemarrage, a verifier a la main." %
                   (m_prod[:8], md5(cible)[:8]))
            return False
        return True

    # --- copie datee (automations, scripts) ---
    rx_h = re.compile(DATE_H_T % re.escape(base), re.I)
    rx_j = re.compile(DATE_J_T % re.escape(base), re.I)
    for f in sorted(os.listdir(dossier)):
        p = os.path.join(dossier, f)
        if not os.path.isfile(p) or not f.lower().endswith(".yaml"):
            continue
        if rx_h.match(f) or rx_j.match(f) or "bak" in f.lower():
            continue
        st = os.stat(p)
        date = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y_%m_%d_%Hh%Mm%Ss")
        cible = os.path.join(dossier, "%s.bak_%s.yaml" % (base, date))
        if os.path.exists(cible):
            print("   COLLISION, non renomme : %s" % f)
            continue
        os.rename(p, cible)
        print("   renomme  %s -> %s" % (f, os.path.basename(cible)))

    deja = copies_dates(dossier, base)
    if deja:
        dernier = os.path.join(dossier, deja[-1][0])
        if md5(dernier) == m_prod:
            print("   copie deja a jour :", deja[-1][0])
            return True
    horo = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")
    cible = os.path.join(dossier, "%s.bak_%s.yaml" % (base, horo))
    shutil.copy2(prod, cible)
    ok = md5(cible) == m_prod
    print("   copie    -> %s  %s" % (os.path.basename(cible), "MD5 OK" if ok else "MD5 KO"))
    if not ok:
        os.remove(cible)
        alerte("%s : MD5 different apres copie, copie annulee. Aucun redemarrage." % base)
        return False
    return True


def main():
    tout_ok = True
    for prod, dossier, base, stable in CIBLES:
        if not traite(prod, dossier, base, stable):
            tout_ok = False
            break          # on s'arrete a la premiere erreur : pas de ligne suivante
    print("RESULTAT :", "OK" if tout_ok else "ECHEC - arret, alerte envoyee, aucun redemarrage")
    return 0 if tout_ok else 1


if __name__ == "__main__":
    sys.exit(main())
