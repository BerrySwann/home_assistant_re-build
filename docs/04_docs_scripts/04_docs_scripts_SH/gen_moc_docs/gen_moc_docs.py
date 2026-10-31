# -*- coding: utf-8 -*-
"""gen_moc_docs.py - genere MOC_AUTOMATIONS.md (docs/03), MOC_SCRIPTS.md (docs/04) et MOC_SKILLS.md (docs/05).
Lecture seule sur les sources : n'ecrit que les 3 fichiers MOC (sauvegarde .bak_AAAA_MM_JJ_HHhMMmSSs.md si le contenu change).
Regle d'Eric (2026-10-28) : 1 source = 1 fiche .md. Rapprochement : nom normalise identique, sinon fiche qui cite le nom du fichier,
sinon table FORCE. Les fiches proches par le nom mais non rattachees sont proposees comme candidates (a valider, jamais comptees OK).
Ignores : .bak, XX_*, *_ORIGINAL, *_archive*, __pycache__, .pyc. Option --dry : n'ecrit rien."""
import os, re, sys, datetime, difflib, urllib.parse, html

D = r"C:\Users\Berry Swann\Documents\ReBuild\docs"
SKIP = re.compile(r"(^|[\\/])(XX_[^\\/]*|99_docs_MD_system|[^\\/]*_ORIGINAL|[^\\/]*_archive[^\\/]*|__pycache__)([\\/]|$)", re.I)
FORCE = {}  # nom de fichier source en minuscules -> chemin complet de la fiche (rattachements valides par Eric)
_CLIM = r"C:\Users\Berry Swann\Documents\ReBuild\docs\04_docs_scripts\04_docs_scripts_YAML_MD\Climatisation\Scripts_clim_on_off\Scripts_clim_on_off.md"
for _n in ("j_1_1_salon_clim_on_off_intelligent.yaml", "j_1_2_bureau_clim_on_off_intelligent.yaml", "j_1_3_chambre_clim_on_off_intelligent.yaml"):
    FORCE[_n] = _CLIM  # 1 fiche pour les 3 routeurs clim (rattachement manuel, ordre d'Eric 2026-10-28)
_CFG = r"C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_MD"
FORCE["audit_md5_yaml.sh"] = _CFG + r"\.scripts\01_scripts.sh_md\Audit_md5_yaml\Audit_md5_yaml.md"  # copie identique a la prod, fiche existante (ordre d'Eric 2026-10-28, a valider)
FORCE["correct_linky.py"] = _CFG + r"\.scripts\02_scripts.py_md\Correct_linky\Correct_linky.md"  # idem
FORCE["mf_vigilance_images.sh"] = _CFG + r"\scripts\Mf_vigilance_images.md"  # idem

def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())

def walk(root, exts):
    res = []
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if ".bak" in f.lower() or f.startswith("#") or os.path.splitext(f)[1].lower() not in exts:
                continue
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, root)
            if SKIP.search(rel):
                continue
            res.append((full, rel))
    return sorted(res, key=lambda t: t[1].lower())

def link(base, label, full):
    rel = os.path.relpath(full, base).replace("\\", "/")
    return "[%s](%s)" % (label, urllib.parse.quote(rel, safe="/"))

def match_all(sources, fiches):
    mtext = {}
    for f, _ in fiches:
        try:
            mtext[f] = open(f, encoding="utf-8", errors="replace").read().lower()
        except OSError:
            mtext[f] = ""
    used = set()
    rows = []
    for sf, srel in sources:
        base = os.path.basename(sf)
        stem = norm(os.path.splitext(base)[0])
        hit, how = None, ""
        if base.lower() in FORCE and os.path.exists(FORCE[base.lower()]):
            hit, how = FORCE[base.lower()], "rattachement manuel"
        if not hit:
            for mf, mrel in fiches:
                if norm(os.path.splitext(os.path.basename(mf))[0]) == stem:
                    hit, how = mf, "nom"
                    break
        if not hit:
            for mf, mrel in fiches:
                if base.lower() in mtext[mf]:
                    hit, how = mf, "chemin cite"
                    break
        if hit:
            used.add(hit)
        rows.append({"sf": sf, "srel": srel, "md": hit, "how": how, "cand": None})
    free = [(f, r) for f, r in fiches if f not in used]
    pairs = []
    for i, r in enumerate(rows):
        if r["md"]:
            continue
        a = norm(os.path.splitext(os.path.basename(r["sf"]))[0])
        for f, rel in free:
            b = norm(os.path.splitext(os.path.basename(f))[0])
            ratio = difflib.SequenceMatcher(None, a, b).ratio()
            if a and b and (a in b or b in a):
                ratio = max(ratio, 0.75)
            pairs.append((ratio, i, f))
    taken_f, taken_i = set(), set()
    for ratio, i, f in sorted(pairs, key=lambda t: -t[0]):
        if ratio < 0.5 or i in taken_i or f in taken_f:
            continue
        rows[i]["cand"] = (f, ratio)
        taken_i.add(i)
        taken_f.add(f)
    orphans = [(f, r) for f, r in fiches if f not in used]
    return rows, orphans, taken_f

def src_table(base, rows, group_label="Categorie"):
    L = ["| %s | Source | Fiche |" % group_label, "|:-----|:-------|:------|"]
    groups = {}
    for r in rows:
        parts = r["srel"].split(os.sep)
        g = parts[0] if len(parts) > 1 else "(racine)"
        groups.setdefault(g, []).append(r)
    first_group = True
    for g in sorted(groups, key=lambda x: x.lower()):
        if not first_group:
            L.append("| <br> |  |  |")
        first_group = False
        first = True
        for r in groups[g]:
            if r["md"]:
                extra = {"nom": "", "chemin cite": " (par chemin cite)", "rattachement manuel": " (rattachement manuel)"}[r["how"]]
                fm = "Fiche OK " + link(base, "fiche", r["md"]) + extra
            elif r["cand"]:
                fm = "Fiche MANQUANTE - candidate (a valider, nom different) : " + link(base, os.path.basename(r["cand"][0]), r["cand"][0])
            else:
                fm = "Fiche MANQUANTE"
            L.append("| %s | %s | %s |" % (g if first else "", link(base, os.path.basename(r["sf"]), r["sf"]), fm))
            first = False
    return L

def counts(rows):
    ok = sum(1 for r in rows if r["md"])
    cand = sum(1 for r in rows if not r["md"] and r["cand"])
    return ok, len(rows) - ok, cand

def orphan_lines(base, orphans, taken):
    if not orphans:
        return ["- aucune"]
    L = []
    for f, rel in orphans:
        tag = " (candidate d'une source sans fiche, voir ci-dessus)" if f in taken else ""
        L.append("- %s%s" % (link(base, rel.replace("\\", "/"), f), tag))
    return L

def write(path, text, dry):
    text = avec_badges(text, path)
    stamp = lambda t: sans_maj("\n".join(l for l in t.split("\n") if not l.startswith("Genere le ")))
    old = open(path, encoding="utf-8").read().replace("\r\n", "\n") if os.path.exists(path) else None
    if old is not None and stamp(old) == stamp(text):
        print("inchange : " + path)
        return
    if dry:
        print("--dry : rien d'ecrit (%s)" % path)
        return
    if old is not None:
        st = datetime.datetime.now().strftime("%Y_%m_%d_%Hh%Mm%Ss")
        bak = re.sub(r"\.md$", ".bak_%s.md" % st, path)
        with open(bak, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(old)
        print("sauvegarde : " + bak)
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("ecrit : " + path)

def header(title, name, regle):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    return ["# %s" % title, "", "Genere le %s par docs/04_docs_scripts/04_docs_scripts_SH/gen_moc_docs/gen_moc_docs.py (%s). Ne pas modifier a la main : le script ecrase les modifications." % (now, name), "", regle, ""]
def moc_automations(dry):
    root = os.path.join(D, "03_docs_automations")
    src = walk(os.path.join(root, "03_docs_automations_YAML"), {".yaml", ".yml"})
    fic = walk(os.path.join(root, "03_docs_automations_MD"), {".md"})
    rows, orph, taken = match_all(src, fic)
    annex = [(f, r) for f, r in orph if re.search(r"(^|_)XX_", os.path.basename(f))]
    orph = [x for x in orph if x not in annex]
    ok, ko, cand = counts(rows)
    L = header("MOC_AUTOMATIONS.md - 1 YAML = 1 fiche .md (automations)", "MOC_AUTOMATIONS", "Regle d'Eric (2026-10-28) : chaque YAML de docs/03_docs_automations a sa fiche .md. Le rapprochement se fait par le nom du fichier, sinon par une fiche qui cite le nom du YAML. Une fiche proche par le nom mais non rattachee est seulement proposee comme candidate (a valider par Eric, jamais comptee OK). Sont ignores : .bak, XX_*, *_ORIGINAL, *_archive*. Voir aussi GLOBAL_INDEX_AUTOMATIONS.md (lien avec les automations de la prod). Les liens sont relatifs a ce fichier.")
    L += ["## Controle", "", "- YAML suivis : %d" % len(rows), "- YAML avec fiche : %d" % ok, "- YAML sans fiche (MANQUANT) : %d dont %d avec une fiche candidate a valider" % (ko, cand), "- Fiches .md sans YAML correspondant : %d" % len(orph), "- Documents annexes (prefixe P1_XX_, fiche sans YAML voulue) : %d" % len(annex), "", "## Automations par categorie", ""]
    L += src_table(root, rows)
    NOTE = {"p1_xx_sdb_soufflant_specification_2026": "specification de reference du soufflant de la salle de bain (2026-09-28, mise a jour 2026-09-29)",
            "p1_xx_timers_sdb_soufflant_et_seche_serviettes": "timers du soufflant (60 min) et du seche-serviettes (2 h) avec rattrapage au demarrage de HA, du 2026-10-07, non testes en conditions reelles",
            "p1_xx_d_watchdog_radiateur_sdb": "ancienne version du watchdog (alias D ... RADIATEUR), doublon probable de la fiche C_watchdog_soufflant_SDB, a decider (TODO R86.3)"}
    L += ["", "## Documents annexes (fiches sans YAML, voulues)", "", "Fiches de reference rangees avec leur famille d'automations mais qui ne decrivent aucun YAML : le prefixe P1_XX_ le dit. Elles ne sont pas des anomalies.", ""]
    if annex:
        for f, rel in annex:
            st = os.path.splitext(os.path.basename(f))[0].lower()
            L.append("- %s : %s" % (link(root, rel.replace("\\", "/"), f), NOTE.get(st, "document annexe")))
    else:
        L.append("- aucun")
    L += ["", "## Fiches sans YAML correspondant", ""] + orphan_lines(root, orph, taken) + [""]
    write(os.path.join(root, "MOC_AUTOMATIONS.md"), "\n".join(L), dry)
    print("03 : sources=%d avec_fiche=%d sans_fiche=%d (candidates=%d) fiches_sans_source=%d annexes=%d" % (len(rows), ok, ko, cand, len(orph), len(annex)))

AUDIT = re.compile(r"^(audit|check|verif|hermes_audit|trigul_run)", re.I)
_PROD = {}

def prod_usage(name):
    """Cherche le nom du fichier dans les YAML de la prod (H:), lecture seule."""
    base = "H:" + chr(92)
    if not os.path.isdir(base):
        return "H: inaccessible"
    if not _PROD:
        files = [os.path.join(base, n) for n in ("shell_command.yaml", "scripts.yaml", "automations.yaml", "configuration.yaml")]
        for d in ("shell_command", "shell_commands", "scripts", "timers"):
            dd = os.path.join(base, d)
            if os.path.isdir(dd):
                for dp, dn, fn in os.walk(dd):
                    files += [os.path.join(dp, f) for f in fn if f.lower().endswith((".yaml", ".yml"))]
        for f in files:
            try:
                _PROD[f] = open(f, encoding="utf-8", errors="replace").read().lower()
            except OSError:
                pass
    hits = sorted(set(os.path.basename(f) for f, t in _PROD.items() if name.lower() in t))
    return ("oui (" + ", ".join(hits) + ")") if hits else "non trouve dans les YAML de la prod"

def hlink(base, label, full):
    rel = os.path.relpath(full, base).replace("\\", "/")
    return '<a href="%s">%s</a>' % (urllib.parse.quote(rel, safe="/"), html.escape(label))

COLS = (18, 26, 24, 32)  # largeurs en % : identiques dans tous les tableaux (.sh, .py, .yaml, audit)

def header_sections(path):
    """Nombre de sections '# ## TITRE' dans les 80 premieres lignes (convention d'en-tete du projet)."""
    n = 0
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for i, line in enumerate(fh):
                if i >= 80:
                    break
                if re.match(r"^\s*#\s*##\s+\S", line):
                    n += 1
    except OSError:
        return 0
    return n
def src_table_x(base, rows, group_label="Dossier"):
    L = ['<table style="table-layout:fixed;width:100%;overflow-wrap:anywhere">',
         "<colgroup>" + "".join('<col width="%d%%">' % w for w in COLS) + "</colgroup>",
         "<thead><tr><th>%s</th><th>Source</th><th>Fiche</th><th>Appele par Home Assistant</th></tr></thead>" % group_label,
         "<tbody>"]
    groups = {}
    for r in rows:
        parts = r["srel"].split(os.sep)
        g = parts[-2] if len(parts) > 1 else "(racine)"
        groups.setdefault(g, []).append(r)
    first_group = True
    for g in sorted(groups, key=lambda x: x.lower()):
        if not first_group:
            L.append('<tr><td colspan="4">&nbsp;</td></tr>')
        first_group = False
        first = True
        for r in groups[g]:
            if r["md"]:
                extra = {"nom": "", "chemin cite": " (par chemin cite)", "rattachement manuel": " (rattachement manuel)"}[r["how"]]
                fm = "Fiche OK " + hlink(base, "fiche", r["md"]) + extra
            elif r["cand"]:
                fm = "Fiche MANQUANTE - candidate (a valider, nom different) : " + hlink(base, os.path.basename(r["cand"][0]), r["cand"][0])
            else:
                hs = header_sections(r["sf"])
                fm = ("Documente dans l'en-tete du fichier (%d sections), pas de fiche .md" % hs) if hs >= 3 else "Fiche MANQUANTE"
            sf = r["sf"]
            key = os.path.splitext(os.path.basename(sf))[0] if os.path.splitext(sf)[1].lower() in (".yaml", ".yml") else os.path.basename(sf)
            L.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (html.escape(g) if first else "", hlink(base, os.path.basename(sf), sf), fm, html.escape(prod_usage(key))))
            first = False
    L.append("</tbody></table>")
    return L
def moc_scripts(dry):
    root = os.path.join(D, "04_docs_scripts")
    L = header("MOC_SCRIPTS.md - 1 script = 1 fiche .md", "MOC_SCRIPTS", "Regle d'Eric (2026-10-28) : chaque script de docs/04_docs_scripts a sa fiche .md. Rapprochement par le nom du fichier, sinon par une fiche qui cite le nom du fichier ; fiche proche mais non rattachee = candidate (a valider, jamais comptee OK). Classement (Eric, 2026-10-28) : deux groupes. Home Assistant : les .sh, puis les .py, puis les scripts YAML (les scripts de Home Assistant). Audit interne : les .sh, puis les .py ; ces scripts ne font pas tourner Home Assistant. Un script est range en verification ou audit quand son nom commence par Audit, Check, Verif, Hermes_audit ou trigul_run. La colonne Appele par Home Assistant dit si le nom du fichier apparait dans les YAML de la prod (H:), lecture seule. Voir GLOBAL_INDEX_SCRIPTS_SH.md et GLOBAL_INDEX_SCRIPTS_YAML.md. Les liens sont relatifs a ce fichier.")
    fam, allrows = [], []
    for title, ydir, exts, mdir in (("Scripts SH (bash et python)", "04_docs_scripts_SH", {".sh", ".py"}, "04_docs_scripts_SH_MD"), ("Scripts YAML (Home Assistant)", "04_docs_scripts_YAML", {".yaml", ".yml", ".py"}, "04_docs_scripts_YAML_MD")):
        src = walk(os.path.join(root, ydir), exts)
        fic = walk(os.path.join(root, mdir), {".md"})
        rows, orph, taken = match_all(src, fic)
        ok, ko, cand = counts(rows)
        fam.append((title, len(rows), ok, ko, cand, len(orph), orph, taken))
        allrows += rows
    ext = lambda r: os.path.splitext(r["sf"])[1].lower()
    aud = lambda r: bool(AUDIT.match(os.path.basename(r["sf"])))
    sh = [r for r in allrows if ext(r) == ".sh" and not aud(r)]
    py = [r for r in allrows if ext(r) == ".py" and not aud(r)]
    yml = [r for r in allrows if ext(r) in (".yaml", ".yml")]
    a_sh = [r for r in allrows if ext(r) == ".sh" and aud(r)]
    a_py = [r for r in allrows if ext(r) == ".py" and aud(r)]
    key = lambda rs: sorted(rs, key=lambda r: os.path.basename(r["sf"]).lower())
    L += ["## Controle", ""]
    for t, n, ok, ko, cand, no, o, tk in fam:
        L.append("- %s : %d sources, %d avec fiche, %d sans fiche (dont %d avec candidate a valider), %d fiches sans source" % (t, n, ok, ko, cand, no))
    L += ["- Repartition : %d scripts bash, %d scripts python, %d scripts YAML Home Assistant, %d verification ou audit en bash, %d verification ou audit en python" % (len(sh), len(py), len(yml), len(a_sh), len(a_py)), ""]
    hd = [r for r in allrows if not r["md"] and not r["cand"] and header_sections(r["sf"]) >= 3]
    L += ["- Sans fiche .md mais documentes dans leur en-tete (3 sections ou plus) : %d (%s)" % (len(hd), ", ".join(os.path.basename(r["sf"]) for r in hd)), ""]
    L += ["## Home Assistant", "", "### .sh", ""] + src_table_x(root, key(sh)) + ["", "---", "", "### .py", ""] + src_table_x(root, key(py)) + ["", "---", "", "### .yaml (scripts Home Assistant, ils tournent dans Home Assistant)", ""] + src_table_x(root, key(yml)) + [""]
    L += ["## Audit interne (ils ne font pas tourner Home Assistant)", "", "Outils de controle, pour Eric, Claude et Hermes. Certains sont lances depuis un bouton ou une automation de Home Assistant (voir la colonne Appele par Home Assistant), mais ils ne servent qu'a controler : la maison fonctionnerait sans eux.", "", "### .sh", ""] + src_table_x(root, key(a_sh)) + ["", "---", "", "### .py", ""] + src_table_x(root, key(a_py)) + [""]
    for t, n, ok, ko, cand, no, o, tk in fam:
        L += ["## Fiches sans source correspondante (" + t + ")", ""] + orphan_lines(root, o, tk) + [""]
    write(os.path.join(root, "MOC_SCRIPTS.md"), "\n".join(L), dry)
    for t, n, ok, ko, cand, no, o, tk in fam:
        print("04 %s : sources=%d avec_fiche=%d sans_fiche=%d (candidates=%d) fiches_sans_source=%d" % (t, n, ok, ko, cand, no))
    print("04 repartition : bash=%d python=%d yaml=%d audit_bash=%d audit_python=%d" % (len(sh), len(py), len(yml), len(a_sh), len(a_py)))
def front(path):
    try:
        t = open(path, encoding="utf-8", errors="replace").read().replace("\r\n", "\n")
    except OSError:
        return "", ""
    m = re.match(r"---\n(.*?)\n---", t, re.S)
    if not m:
        return "", ""
    fm = m.group(1).split("\n")
    name, desc = "", ""
    for i, l in enumerate(fm):
        if l.startswith("name:"):
            name = l[5:].strip().strip("\"'")
        if l.startswith("description:"):
            v = l[12:].strip()
            if v in (">", "|", ">-", "|-"):
                buf = []
                for l2 in fm[i + 1:]:
                    if l2.startswith((" ", "\t")):
                        buf.append(l2.strip())
                    else:
                        break
                desc = " ".join(buf)
            else:
                desc = v.strip("\"'")
    return name, desc

def moc_skills(dry):
    root = os.path.join(D, "05_docs_skills")
    rootp = os.path.join(root, "05_docs_skills_PURE")  # skills en anglais (2026-10-31)
    rootm = os.path.join(root, "05_docs_skills_MD")  # fiches FR, un dossier skill_<nom> par skill
    if not os.path.isdir(rootp): rootp = root
    L = header("MOC_SKILLS.md - skills du projet et leur explication", "MOC_SKILLS", "Regle d'Eric (2026-10-28) : la liste des skills avec leur explication (champ description du SKILL.md, repris de la copie en docs/05_docs_skills). Une copie par skill : dossier `skill_NOM/NOM.md` (anglais, dans 05_docs_skills_PURE) et fiche francaise dans 05_docs_skills_MD. Les liens sont relatifs a ce fichier.")
    dirs = sorted([d for d in os.listdir(rootp) if os.path.isdir(os.path.join(rootp, d)) and d.startswith("skill_")], key=str.lower)
    rows, vides = [], []
    for d in dirs:
        fs = [f for f in os.listdir(os.path.join(rootp, d)) if f.lower().endswith(".md") and ".bak" not in f.lower()]
        fs = [f for f in fs if f.lower() == d[6:].lower() + ".md"] or fs  # le fichier du skill porte le nom du dossier (histo_ref_*.md = fichiers de reference, 2026-10-31)
        if not fs:
            vides.append(d)
            continue
        full = os.path.join(rootp, d, fs[0])
        name, desc = front(full)
        desc = re.sub(r"\s+", " ", desc).replace("|", "/")
        desc = re.split(r"\s*(?:Declencher|Usage typique)", desc)[0].strip(" .-") + "."
        if len(desc) > 110:
            desc = desc[:107].rstrip() + "..."
        mt = datetime.datetime.fromtimestamp(os.path.getmtime(full)).strftime("%Y-%m-%d")
        rows.append((name or d[6:], d, full, desc, mt))
    pdir = r"C:\Users\Berry Swann\Documents\ReBuild\.claude\skills"
    proj = sorted(os.listdir(pdir), key=str.lower) if os.path.isdir(pdir) else []
    have = set(norm(r[0]) for r in rows)
    manque = [p for p in proj if norm(p) not in have]
    L += ["## Controle", "", "- Skills avec copie en docs : %d" % len(rows), "- Skills du projet (.claude/skills) : %d" % len(proj), "- Skills du projet sans copie en docs : %s" % (", ".join(manque) if manque else "aucun"), "- Dossiers skill_ sans copie (seulement des .bak) : %s" % (", ".join(vides) if vides else "aucun"), "", "## Skills", "", "| Skill | Anglais | FR | Explication | Date |", "|:------|:------|:------|:------------|:---------------|"]
    for name, d, full, desc, mt in rows:
        fr = os.path.join(rootm, d, os.path.basename(full))
        frl = link(root, os.path.basename(fr), fr) if os.path.isfile(fr) else "a creer"
        if os.path.isfile(fr):  # explication en francais prise dans la fiche FR (section "A quoi ca sert"), 2026-10-31
            m = re.search(r"## A quoi ca sert\s*\n+(.+?)\n\s*\n", open(fr, encoding="utf-8").read() + "\n\n", re.S)
            if m: desc = re.sub(r"\s+", " ", m.group(1)).replace("|", "/").strip()
            if len(desc) > 110: desc = desc[:107].rstrip() + "..."
        L.append("| %s | %s | %s | %s | %s |" % (name, link(root, os.path.basename(full), full), frl, desc or "(pas de description dans la copie)", mt))
    L.append("")
    write(os.path.join(root, "MOC_SKILLS.md"), "\n".join(L), dry)
    print("05 : skills=%d projet=%d sans_copie=%d dossiers_vides=%d" % (len(rows), len(proj), len(manque), len(vides)))

def avec_badges(texte, path):
    """Banniere des 8 badges via Check_badges_fiches.reconstruire (regle unique, ordre d'Eric le 2026-10-31 : badges partout sauf .bak). 00_IA et 05_docs_skills restent exemptes."""
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
    dry = "--dry" in sys.argv
    moc_automations(dry)
    moc_scripts(dry)
    moc_skills(dry)

if __name__ == "__main__":
    main()