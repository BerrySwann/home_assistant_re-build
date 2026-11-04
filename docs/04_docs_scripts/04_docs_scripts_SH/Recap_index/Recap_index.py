# Recap_index.py - copie de recap_index.py d Hermes (AppData\Local\hermes\scripts\histo), rangee dans docs sur ordre d Eric le 2026-11-04.
# Fiche : docs\04_docs_scripts\04_docs_scripts_SH_MD\Recap_index\Recap_index.md . Interpreteur : python -I -X utf8
# annotations_log:
# [2026-11-04] ajout Claude : .bak avant ecriture et aucune ecriture si le bloc est identique (regle de sauvegarde du projet).
# [2026-11-04] copie a l identique du script d Hermes (md5 source 15fdf133), seul cet en-tete est ajoute.
"""Recapitulatif des entites, pose en fin de chaque index global.

Le bloc est encadre par deux marqueurs HTML, remplaces a chaque passage :
    <!-- RECAP-ENTITES:DEBUT -->
    ... tableau ...
    <!-- RECAP-ENTITES:FIN -->

Classification, telle que validee le 2026-11-03 :
  - NAT <plateforme>  : l entree de registre a un config_entry (vient d une integration) ;
  - CREE <famille>    : pas de config_entry, ou nom declare dans un YAML local ; la famille vient du
                        dossier qui declare l objet (template, utility_meter, groups, sensors...) ;
  - mention RASPI-PI4-4GO pour les trois entites du Pi 4 4 Go ;
  - les noms cites dans une note 'obsolete / inexistant / retire' ne sont pas comptes comme vivants.

Usage : python recap_index.py [--dry]
"""
import os, re, sys, json, collections, datetime

R = r"C:\Users\Berry Swann\Documents\ReBuild"
IDX_REPO = os.path.join(R, r"docs\01_docs_config_system\01_config_system_MD\GLOBAL_INDEX_REPO\GLOBAL_INDEX_REPO.md")
CFG = os.path.join(R, r"docs\01_docs_config_system\01_config_system_SH_PY_YAML")
REG = r"H:\.storage\core.entity_registry"
TITRES = {}   # domaine installe -> titres des entrees Appareils et services
CUSTOM_DIR = r"H:\custom_components"   # tout ce qui est la vient de HACS ou d un depot, pas du coeur HA

INDEX = [
 IDX_REPO,
 os.path.join(R, r"docs\99_docs_MD_system\ENTITES_GLOBAL_INDEX\ENTITES_GLOBAL_INDEX.md"),
 os.path.join(R, r"docs\03_docs_automations\GLOBAL_INDEX_AUTOMATIONS.md"),
 os.path.join(R, r"docs\02_docs_dashboard\GLOBAL_INDEX_VIGNETTES_PAGES.md"),
 os.path.join(R, r"docs\04_docs_scripts\GLOBAL_INDEX_SCRIPTS_SH.md"),
 os.path.join(R, r"docs\04_docs_scripts\GLOBAL_INDEX_SCRIPTS_YAML.md"),
 os.path.join(R, r"docs\00_IA\00_IA_GLOBAL_INDEX_memoire\IA_GLOBAL_INDEX_memoire.md"),
]

DEBUT, FIN = "<!-- RECAP-ENTITES:DEBUT -->", "<!-- RECAP-ENTITES:FIN -->"
RASPI = {"fan.rpi_cooling_fan", "binary_sensor.rpi_power_status", "sensor.system_monitor_temperature_du_processeur"}
SUPPR = {"climate.clim_du_bureau", "sensor.vitesse_du_vent_vence", "sensor.direction_du_vent_vence"}
ARTEF = {"timer.finished", "this.entity_id"}
DOM = {"sensor", "binary_sensor", "light", "switch", "climate", "weather", "camera", "media_player",
       "input_boolean", "input_number", "input_select", "input_datetime", "input_button", "input_text",
       "script", "automation", "group", "person", "device_tracker", "timer", "counter", "number",
       "select", "button", "update", "fan", "cover", "vacuum", "remote", "sun", "zone",
       "alarm_control_panel", "scene", "todo", "text", "date", "time", "event"}
RX = re.compile(r"(?:<code>|`)([a-z_][a-z0-9_]*\.[a-z0-9_]+)(?:</code>|`)")
EXT = ("yaml", "yml", "json", "md", "txt", "py", "sh", "cfg", "conf", "ini", "csv", "png", "jpg", "svg")


def entites_citees(t):
    """les entites citees, en ignorant celles qui n apparaissent que dans une note d obsolescence"""
    vus = set()
    for m in RX.finditer(t):
        e = m.group(1)
        if e.split(".", 1)[0] not in DOM or e.rsplit(".", 1)[-1].lower() in EXT:
            continue
        # contexte : on regarde la ligne ou le bloc
        deb = max(0, m.start() - 400)
        contexte = t[deb:m.end() + 200].lower()
        if any(k in contexte for k in ("obsolete", "obsolète", "inexistant", "retiré", "retire", "n'existe pas", "n existe pas")):
            continue
        vus.add(e)
    return vus


def familles_yaml():
    """objet -> famille, d apres le dossier du YAML qui le declare"""
    fam = {}
    for base, dirs, files in os.walk(CFG):
        for f in files:
            if ".bak" in f or not f.lower().endswith((".yaml", ".yml")):
                continue
            p = os.path.join(base, f)
            rel = os.path.relpath(p, CFG)
            top = rel.split(os.sep)[0].lower().replace(".", "")
            if os.sep not in rel:            # fichier a la racine : la famille est son domaine
                top = os.path.splitext(f)[0].lower()
            try:
                txt = open(p, encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for m in re.finditer(r"(?m)^\s*([a-z0-9_]{3,})\s*:", txt):
                fam.setdefault(m.group(1), top)
    return fam


def classifie(entites, reg, fam):
    out = collections.Counter()
    for e in entites:
        if e in RASPI:
            out["RASPI-PI4-4GO"] += 1
        elif e in SUPPR:
            out["SUPPRIMEE"] += 1
        elif e in ARTEF:
            out["ARTEFACT-TEMPLATE"] += 1
        elif e in reg and reg[e][1]:
            # une entree de registre avec config_entry = entite fournie par une integration.
            # On distingue le COEUR de Home Assistant de ce qui a ete installe (HACS ou depot) :
            # un domaine present dans H:\custom_components n est pas natif.
            dom = reg[e][0] or "integration"
            prefixe = "HACS " if dom in CUSTOM else "NAT "
            out[prefixe + dom] += 1
        else:
            obj = e.split(".", 1)[1]
            f = fam.get(obj) or (reg[e][0] if e in reg else None)
            out["CREE " + f if f else "NAT-SANS-REGISTRE"] += 1
    return out


def explique(k):
    """explication lisible de l origine, telle qu Eric la veut : le type, puis le nom de
    l integration dans Appareils et services."""
    if k == "NAT mqtt":
        return ("chaine a trois maillons, verifiee le 2026-11-03 : Zigbee2MQTT (conteneur 200, "
                "Proxmox 10.32.154.244) publie vers le broker `core-mosquitto` (add-on Mosquitto, port 1883), "
                "que consomme l integration `mqtt` d Appareils et services. Si un des trois manque, les entites tombent")
    if k.startswith("NAT "):
        return ("integration `%s` du coeur de Home Assistant, installee et visible dans "
                "Appareils et services" % k[4:])
    if k.startswith("HACS "):
        dom = k[5:]
        noms = TITRES.get(dom) or []
        if not noms:
            if dom in CUSTOM:
                return ("installee via HACS (qui va etre renomme marketplace) ; son entree dans Appareils et "
                        "services n a pas de nom affiche")
            return ("installee via HACS (qui va etre renomme marketplace), pas encore ajoutee dans "
                    "Appareils et services : ses entites viennent du YAML")
        if len(noms) == 1:
            return ("deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans "
                    "Appareils et services sous le nom `%s`" % noms[0])
        return ("deux temps : installee via HACS (qui va etre renomme marketplace), puis ajoutee dans "
                "Appareils et services en %d entrees (premiere : `%s`)" % (len(noms), noms[0]))
    if k.startswith("CREE "):
        return ("creee par un YAML du depot, dossier `%s`, sans aucune integration dans Appareils et services"
                % k[5:])
    if k == "RASPI-PI4-4GO":
        return ("entites du Raspberry Pi 4 4 Go : elles existent, le materiel est hors tension "
                "(pour Raspberry Pi4 4Go)")
    if k == "ARTEFACT-TEMPLATE":
        return "mot-cle de template, pas une entite"
    if k == "NAT-SANS-REGISTRE":
        return "fournie par Home Assistant sans entree au registre (zone.home)"
    return ""


def bloc(c):
    total = sum(c.values())
    lignes = [DEBUT,
              "",
              "## Recapitulatif des entites citees par cet index",
              "",
              "Total : **%d entites**. Origine de chacune : type, puis le nom de l integration telle qu elle "
              "apparait dans Appareils et services." % total,
              "",
              "| origine | nombre | explication |",
              "|:---|---:|:---|"]
    for k, n in sorted(c.items(), key=lambda x: (-x[1], x[0])):
        lignes.append("| %s | %d | %s |" % (k, n, explique(k)))
    lignes += ["",
               "> **Chaine la plus fragile** : les `NAT mqtt` ne dependent pas que de Home Assistant. Mesure du 2026-11-03 : l integration `mqtt` "
               "pointe le broker add-on `core-mosquitto` (1883), et les mesures viennent de Zigbee2MQTT, conteneur 200 sur 10.32.154.244. "
               "Conteneur arrete, broker en vrac ou integration retiree : les entites tombent, sans que rien ne le signale dans l interface. "
               "A la meme date, 114 des 128 entites citees avaient remonte dans les 2 heures.",
               "",
               "*Bloc ecrit par `recap_index.py`, encadre par deux marqueurs : il est remplace a chaque passage, "
               "jamais edite a la main. Classification : NAT <integration> si l entree de registre a un config entry ; "
               "NAT <integration> pour le coeur de Home Assistant, HACS <integration> pour ce qui vient de HACS ou d un depot (dossier custom_components) ; CREE <famille> sinon, famille = dossier du YAML qui declare l objet ; RASPI-PI4-4GO pour les trois entites "
               "du Pi 4 4 Go (materiel hors tension, entites existantes) ; SUPPRIMEE pour les noms remplaces ; "
               "ARTEFACT-TEMPLATE pour les mots-cles qui ne sont pas des entites.*",
               "", FIN]
    return "\n".join(lignes)


def main():
    dry = "--dry" in sys.argv
    brut = json.load(open(REG, encoding="utf-8"))["data"]["entities"]
    reg = {e["entity_id"]: (e.get("platform"), bool(e.get("config_entry_id")))
           for e in brut if e.get("entity_id")}
    global CUSTOM
    CUSTOM = {d.lower() for d in os.listdir(CUSTOM_DIR) if os.path.isdir(os.path.join(CUSTOM_DIR, d))} if os.path.isdir(CUSTOM_DIR) else set()
    print("integrations installees hors coeur :", len(CUSTOM))
    global TITRES
    ce = json.load(open(r"H:\.storage\core.config_entries", encoding="utf-8"))["data"]["entries"]
    for e in ce:
        d = (e.get("domain") or "").lower()
        if d in CUSTOM:
            titre = e.get("title") or ""
            if titre:
                TITRES.setdefault(d, [])
                if titre not in TITRES[d]:
                    TITRES[d].append(titre)
    print("integrations installees, titres Appareils et services :", {k: len(v) for k, v in TITRES.items()})
    fam = familles_yaml()
    entites = entites_citees(open(IDX_REPO, encoding="utf-8", errors="replace").read())
    c = classifie(entites, reg, fam)
    print("entites retenues :", len(entites), "|", dict(sorted(c.items(), key=lambda x: -x[1])))
    b = bloc(c)
    for p in INDEX:
        if not os.path.exists(p):
            print("   absent :", p); continue
        t = open(p, encoding="utf-8", errors="replace").read()
        if DEBUT in t and FIN in t:
            i, j = t.index(DEBUT), t.index(FIN) + len(FIN)
            t2 = t[:i] + b + t[j:]
        else:
            t2 = t.rstrip("\n") + "\n\n" + b + "\n"
        if dry:
            print("   [dry] bloc a poser dans", os.path.basename(p)); continue
        if t2 == t:
            print("   inchange :", os.path.basename(p)); continue
        bak = os.path.splitext(p)[0] + ".bak_" + datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss") + ".md"
        open(bak, "w", encoding="utf-8", newline="").write(t)
        open(p, "w", encoding="utf-8", newline="").write(t2)
        print("   bloc ecrit :", os.path.basename(p), "| sauvegarde", os.path.basename(bak))


if __name__ == "__main__":
    main()
