#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT HUISSIER - Proces-verbal d'audit du projet HA ReBuild (LECTURE SEULE).

Executes 5 passes d'audit d'un bloc et produit un PV horodate :
  PASSE 1 - TREE      : arborescences LOCAL / PROD / GITHUB + ecarts de structure
  PASSE 2 - MD5 TRIGUL: triangulation LOCAL <-> PROD <-> GITHUB (md5 brut + LF)
  PASSE 3 - DEPENDANCES: DEPENDANCES_GLOBALES.md + chaines de dependances des YAML
  PASSE 4 - ENTITIES  : entites YAML vs matrice (non referencees / fantomes)
  PASSE 5 - FORMAT    : conformite des YAML aux regles du CLAUDE.md

Constats uniquement - le script NE MODIFIE AUCUN fichier du projet.
Rapports ecrits dans %LOCALAPPDATA%/Temp/audit_huissier/ :
  - PV_audit_YYYY-MM-DD_HHMM.md   (proces-verbal complet)
  - audit_details.json            (details exploitables)

Usage : env -u PYTHONPATH python audit_huissier.py
"""
import os, re, sys, json, hashlib, subprocess, collections, datetime

try:
    import yaml  # noqa: F401  (verifie : passes 6-7 en ont besoin)
except ImportError:
    raise SystemExit("ERREUR: PyYAML absent de cet interpreteur. "
                     "Lancer avec le venv hermes-agent (Python 3.11) :\n"
                     '  env -u PYTHONPATH "C:/Users/Berry Swann/AppData/Local/hermes/'
                     'hermes-agent/venv/Scripts/python.exe" audit_huissier.py')

# ─── CONFIG ───────────────────────────────────────────────────────────────
LOCAL = r"C:/Users/Berry Swann/Documents/ReBuild"
PROD = "H:/"
CONFIG_YAML = LOCAL + "/docs/01_docs_config_system/01_config_system_SH_PY_YAML"
MATRICE = LOCAL + "/docs/00_IA/00_IA_DEPENDANCES_GLOBALES_CLAUDE_memoire/DEPENDANCES_GLOBALES_CLAUDE_memoire.md"
DASHBOARD_YAML = LOCAL + "/docs/02_docs_dashboard/02_dashboard_docs_YAML"
OUT_DIR = os.path.join(os.environ.get("LOCALAPPDATA", "."), "Temp", "audit_huissier")

EXCLUDE_DIRS = ("__pycache__", ".git", "_old", "backup", "historique", "CLAUDE_backup",
                "_old_avant_staging")
EXTS = (".md", ".yaml", ".yml", ".sh", ".py", ".txt", ".json")

# caracteres typographiques interdits (hors bordures ASCII U+2500/U+2502/U+256D..)
INTERDITS = {"\u2014": "em dash —", "\u2026": "ellipse ...", "\u00ab": "guillemet «",
             "\u00bb": "guillemet »", "\u00b7": "point median ·"}

RE_VIGNETTE = re.compile(r"\bL\dC\d\b")
RE_FILE_YAML = re.compile(r"\b([A-Za-z0-9_\-]+\.ya?ml)\b")
RE_SLUG = re.compile(r"^\s*#\s*---\s*([A-Za-z0-9_]+)\s*---\s*$")
RE_UID = re.compile(r"^\s*unique_id:\s*[\"']?([A-Za-z0-9_]+)")
RE_NAME = re.compile(r"^\s*-?\s*name:\s*[\"']?([^\"'\n]+)")

# nommage conforme (regex souples) + whitelist legacy connue
PREFIX_OK = re.compile(r"^(P[0-4]|M_|A_|S_|MP_|GRP_)", re.I)
LEGACY_OK = {"P0_total_pour_les_7_postes.yaml", "P2_current_all_standby.yaml"}


def sha_md5(path):
    with open(path, "rb") as f:
        data = f.read()
    return (hashlib.md5(data).hexdigest(),
            hashlib.md5(data.replace(b"\r\n", b"\n")).hexdigest())


def walk(root, sub=None, exts=EXTS):
    out = {}
    base = os.path.join(root, sub) if sub else root
    if not os.path.isdir(base):
        return out
    for dp, dns, fns in os.walk(base):
        dns[:] = [d for d in dns if d not in EXCLUDE_DIRS]
        for fn in fns:
            if fn.endswith(exts):
                p = os.path.join(dp, fn)
                rel = os.path.relpath(p, root).replace(os.sep, "/")
                out[rel] = p
    return out


def git(args):
    try:
        return subprocess.check_output(["git", "-C", "H:/", "--no-optional-locks"] + args,
                                       text=True, errors="replace", timeout=180).strip()
    except Exception as e:
        return f"<git error: {e}>"


def read_lines(path):
    try:
        with open(path, encoding="utf-8-sig", errors="replace") as f:
            return f.read().split("\n")
    except Exception:
        return []


# ═══ PASSE 1 : TREE ══════════════════════════════════════════════════════
def passe1_tree():
    r = {"pass": "TREE", "sections": {}}
    local_docs = walk(LOCAL, "docs")
    prod_docs = walk(PROD, "docs")
    # github : fichiers suivis par git (repo sur H:)
    gh_list = git(["ls-files"]).split("\n")
    gh_docs = {f: "" for f in gh_list if f.startswith("docs/")}

    def tree_resume(files):
        c = collections.Counter()
        for rel in files:
            parts = rel.split("/")
            key = "/".join(parts[:3]) if len(parts) > 3 else "/".join(parts[:-1])
            c[key] += 1
        return dict(sorted(c.items()))

    r["sections"]["local_docs_count"] = len(local_docs)
    r["sections"]["prod_docs_count"] = len(prod_docs)
    r["sections"]["github_docs_count"] = len(gh_docs)
    r["sections"]["local_tree"] = tree_resume(local_docs)
    r["sections"]["prod_tree"] = tree_resume(prod_docs)

    only_local = sorted(set(local_docs) - set(prod_docs))
    only_prod = sorted(set(prod_docs) - set(local_docs))
    only_gh = sorted(set(gh_docs) - set(prod_docs))
    r["sections"]["only_local"] = only_local[:80]
    r["sections"]["only_prod"] = only_prod[:80]
    r["sections"]["only_github"] = only_gh[:80]
    r["sections"]["n_only_local"] = len(only_local)
    r["sections"]["n_only_prod"] = len(only_prod)
    r["sections"]["n_only_github"] = len(only_gh)
    return r


# ═══ PASSE 2 : MD5 TRIGUL (via les 2 scripts separes) ════════════════════
def passe2_md5():
    """Passe 2 = execution des 2 sous-audits MD5 separes (memes scripts que
    l'utilisateur peut lancer seuls) :
      - md5_docs.py : docs  -> LOCAL <-> PROD <-> GITHUB (LOCAL = verite)
      - md5_prod.py : hors-docs -> PROD == GITHUB (doivent etre IDENTIQUES)
    """
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import md5_docs, md5_prod
    d = md5_docs.run(verbose=False)
    p = md5_prod.run(verbose=False)
    return {
        "pass": "MD5 TRIGUL",
        # volet docs
        "stats": d["stats"], "total": d["total"], "diffs": d["diffs"],
        "crlf": d["crlf"], "details": d["details"],
        # volet hors-docs
        "git": {"HEAD": p["head"], "origin_main": p["origin_main"],
                "identiques": p["identiques"], "modifs": p["modifs"],
                "n_modifs": len(p["modifs"]),
                "modifs_hors_docs": p["modifs_hors_docs"],
                "modifs_docs": p["modifs_docs"],
                "prod_egal_github": p["conforme"]},
    }


# ═══ PASSE 3 : DEPENDANCES ═══════════════════════════════════════════════
def passe3_deps():
    r = {"pass": "DEPENDANCES", "refs_cassees": [], "vignettes_absentes": []}
    # matrice presente ?
    r["matrice_presente"] = os.path.exists(MATRICE)
    if r["matrice_presente"]:
        head = read_lines(MATRICE)[:15]
        r["matrice_entete"] = [l for l in head if l.strip()][:4]
    # date declaree en tete vs mtime
    # noms de fichiers presents dans le repo LOCAL (large : racine + docs complets)
    noms = set()
    for dp, dns, fns in os.walk(LOCAL):
        dns[:] = [d for d in dns if d not in EXCLUDE_DIRS]
        for fn in fns:
            noms.add(fn.lower())
    # fichiers HA racine legitimes (cites mais hors 01_config_system_SH_PY_YAML)
    noms |= {"automations.yaml", "scripts.yaml", "configuration.yaml", "scenes.yaml",
             "sql.yaml", "input_button.yaml", "input_datetime.yaml", "input_select.yaml",
             "input_number.yaml", "ip_bans.yaml"}
    vignettes = set()
    if os.path.isdir(DASHBOARD_YAML):
        for d in os.listdir(DASHBOARD_YAML):
            vignettes.add(d)
    # scan des headers CHAINE DE DEPENDANCES dans les YAML de config
    n_fichiers = 0; n_avec_header = 0
    for dp, dns, fns in os.walk(CONFIG_YAML):
        dns[:] = [d for d in dns if d not in EXCLUDE_DIRS]
        for fn in fns:
            if not fn.endswith((".yaml", ".yml")):
                continue
            if ".bak_" in fn:
                continue          # sauvegardes .bak_AAAA_MM_JJ : hors perimetre
            p = os.path.join(dp, fn)
            txt = "\n".join(read_lines(p))
            if "CHA" in txt and "DE D" in txt and "PENDANCES" in txt.upper().replace("É", "E"):
                n_avec_header += 1
            n_fichiers += 1
            # refs fichiers + vignettes des lignes de tableau
            for m in re.finditer(r"^#\s*\|(.+)$", txt, re.M):
                ligne = m.group(1)
                for fm in RE_FILE_YAML.finditer(ligne):
                    ref = fm.group(1)
                    if ref not in noms and ref.lower() not in {x.lower() for x in noms}:
                        r["refs_cassees"].append((os.path.relpath(p, CONFIG_YAML), ref))
                for vm in RE_VIGNETTE.finditer(ligne):
                    v = vm.group(0)
                    if v not in vignettes and not any(v in d for d in vignettes):
                        r["vignettes_absentes"].append((os.path.relpath(p, CONFIG_YAML), v))
    r["n_yaml_config"] = n_fichiers
    r["n_avec_header_chaines"] = n_avec_header
    # dedupe
    r["refs_cassees"] = sorted(set(r["refs_cassees"]))[:100]
    r["vignettes_absentes"] = sorted(set(r["vignettes_absentes"]))[:50]
    return r


# ═══ PASSE 4 : ENTITIES ══════════════════════════════════════════════════
DOMAINES = ("sensor|binary_sensor|switch|light|climate|number|select|button|automation|script|"
            "input_boolean|input_number|input_select|input_datetime|input_button|input_text|"
            "media_player|cover|fan|lock|alarm_control_panel|person|device_tracker|zone|scene|"
            "group|timer|counter|update|event|siren|vacuum|water_heater|weather|valve|template|"
            "notify|rest_command|shell_command|command_line|utility_meter|proximity|sun|calendar|"
            "todo|persistent_notification")
RE_ENTITE = re.compile(r"\b(?:%s)\.([a-zA-Z0-9_]+)" % DOMAINES)
VERBES = set("""turn_on turn_off toggle set set_value set_temperature set_hvac_mode set_fan_mode
set_preset_mode set_swing_mode set_position open_cover close_cover stop_cover set_cover_position
open close stop press send_command select_option select_first select_last select_next
select_previous start pause play media_play media_pause media_stop media_next_track
media_previous_track volume_set volume_up volume_down mute unmute reload update install backup
create delete add remove enable disable lock unlock arm_away arm_home arm_night disarm trigger
call_service restart shutdown announce speak join unjoin set_volume set_level set_color set_rgb
set_white set_effect set_speed set_humidity set_hvac_action set_hold_mode set_aux_heat
set_swing_horizontal set_vertical_swing set_airflow_direction set_gradient set_custom_curve
set_profile set_boost set_eco set_comfort set_sleep set_manual set_auto set_heat set_cool set_dry
set_fan_only heat_cool set_operation_mode set_device_class enable_entity disable_entity
reload_all refresh set_title set_message clear clear_playlist remove_all_items shuffle repeat
set_repeat seek thumbnail_url get_image get_source list_sources set_source open_path close_path
read_directory open_directory get_cameras record play_media send_magic_packet get_position
set_volume_level select_source volume_control set_channel set_channel_up set_channel_down
set_input set_target_temperature set_target_humidity set_hvac set_precision
set_unit_of_measurement set_icon set_name set_native_value set_state set_availability
update_entity create_helper delete_helper""".split())


def extraire_entites(texte):
    res = set()
    for m in RE_ENTITE.finditer(texte):
        if m.group(1) in VERBES:
            continue
        res.add(m.group(0))
    return res


def est_archive(path):
    return any(x in path for x in ("Dashboard_COMPLET", "_old_avant_staging", "_old",
                                   "backup", "CLAUDE_backup", "historique"))


def passe4_entity():
    r = {"pass": "ENTITY INDEX"}
    brut = {}
    for root, dirs, files in os.walk(LOCAL + "/docs"):
        if est_archive(root):
            continue
        for fn in files:
            if fn.endswith((".yaml", ".yml")) and ".bak_" not in fn:
                p = os.path.join(root, fn)
                brut[p] = extraire_entites("\n".join(read_lines(p)))
    finaux = {}
    for p, es in brut.items():
        base = os.path.basename(p)
        cle = (os.path.dirname(p), re.sub(r"_20\d\d-\d\d-\d\d", "", base))
        m = re.search(r"_(\d{4}-\d{2}-\d{2})", base)
        date = m.group(1) if m else ""
        if cle not in finaux or date > finaux[cle][0]:
            finaux[cle] = (date, p, es)
    toutes = set()
    for _, _, es in finaux.values():
        toutes |= es
    if os.path.exists(MATRICE):
        ent_mat = extraire_entites("\n".join(read_lines(MATRICE)))
    else:
        ent_mat = set()
    non_ref = sorted(toutes - ent_mat)
    fantomes = sorted(ent_mat - toutes)
    r["n_fichiers"] = len(finaux)
    r["n_entites_yaml"] = len(toutes)
    r["n_matrice"] = len(ent_mat)
    r["non_referencees"] = non_ref[:150]
    r["n_non_ref"] = len(non_ref)
    r["fantomes"] = fantomes[:80]
    r["n_fantomes"] = len(fantomes)
    r["non_ref_par_domaine"] = dict(collections.Counter(e.split(".")[0] for e in non_ref).most_common())
    return r


# ═══ PASSE 5 : FORMAT - source de verite PROD H: ═════════════════════════
MODULAIRES = ("sensors", "templates", "utility_meter", "command_line", "groups",
              "input_booleans", "shell_command", "input_number")


def passe5_format():
    """Passe 5 = 2 sous-audits SEPARES (chacun lancable seul) sur la PROD H: :
    - check_box_ascii.py : les 2 types de boites ASCII
    - check_slug_name_uid.py : slug tertiaire / name / unique_id
    + controles residuels (headers, caracteres interdits, nommage, tabs)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import check_box_ascii, check_slug_name_uid
    return {"pass": "FORMAT",
            "box": check_box_ascii.run(verbose=False),
            "ids": check_slug_name_uid.run(verbose=False),
            "residuel": passe5_residuel()}


def passe5_residuel():
    """Controles residuels de format sur la PROD H: : headers obligatoires, caracteres
    typographiques interdits, nommage de fichier, tabulations."""
    r = {"pass": "FORMAT residuel", "fichiers": [], "resume": collections.Counter(),
         "hors_perimetre": 0}
    for dp, dns, fns in os.walk(PROD):
        if os.path.normpath(dp) == os.path.normpath(PROD):
            dns[:] = [d for d in dns if d in MODULAIRES]
            continue          # les fichiers de la racine H: (configuration.yaml,
                              # automations.yaml, scripts.yaml...) restent hors perimetre
        else:
            dns[:] = [d for d in dns if d not in EXCLUDE_DIRS]
        for fn in sorted(fns):
            if not fn.endswith((".yaml", ".yml")):
                continue
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, PROD).replace(os.sep, "/")
            lines = read_lines(p)
            txt = "\n".join(lines)
            ecarts = []

            if not txt.strip():
                ecarts.append(("VIDE", "fichier vide"))
                r["fichiers"].append((rel, ecarts)); continue

            # a. bordure principale : deleguee a check_box_ascii.py

            # b. headers obligatoires
            headers = {"DESCRIPTION": "# ## 📝", "CALCUL": "# ## 🧮", "CHAINE": "# ## 🔗",
                       "IMPORTANT": "# ## ⚠️", "DASHBOARD": "# ## 🖥️"}
            for nom, h in headers.items():
                if h not in txt:
                    # variante sans emoji acceptee en signalement
                    alt = h[:5] + " " + nom.split()[0]
                    if re.search(r"#\s*##\s*" + nom, txt):
                        ecarts.append(("HEADER-VARIANTE", f"header {nom} sans emoji"))
                    else:
                        ecarts.append(("HEADER-ABSENT", f"header {nom}"))

            # c/d. slug + name + unique_id : delegues a check_slug_name_uid.py

            # e. caracteres interdits
            for ch, label in INTERDITS.items():
                n = txt.count(ch)
                if n:
                    ecarts.append(("CARACTERE", f"{n}x {label}"))

            # f. nommage fichier
            if not PREFIX_OK.match(fn) and fn not in LEGACY_OK:
                ecarts.append(("NOMMAGE", f"prefixe fichier non conforme: {fn}"))
            if fn not in LEGACY_OK and "_" in fn:
                # heuristique : pas de minuscules dans les types attendus
                if re.search(r"^(P[0-4])_[a-z]", fn):
                    ecarts.append(("NOMMAGE", "TYPE en minuscules"))

            # g. tabulations
            if "\t" in txt:
                ecarts.append(("TAB", "tabulations detectees"))

            if ecarts:
                r["fichiers"].append((rel, ecarts))
                for cat, _ in ecarts:
                    r["resume"][cat] += 1
            else:
                r["resume"]["CONFORME"] += 1
    r["resume"] = dict(r["resume"])
    r["n_fichiers_total"] = sum(1 for _, e in r["fichiers"]) + r["resume"].get("CONFORME", 0)
    return r


# ═══ PASSE 6 : AUTOMATIONS ═══════════════════════════════════════════════
def passe6_automations():
    """Compare chaque automation du automations.yaml PROD (reference de contenu)
    aux fichiers individuels LOCAUX (docs/03) - remonte les DIFFS.
    Regle : source de verite fichiers = LOCAL ; mise a jour ensuite, generalement
    DEPUIS le automations.yaml prod (action separee, avec GO)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import check_automations
    return check_automations.run(verbose=False)


# ═══ PASSE 7 : SCRIPTS ═══════════════════════════════════════════════════
def passe7_scripts():
    """Scripts YAML (H:/scripts.yaml vs 04_docs_scripts_YAML locaux) + scripts SH
    (04_docs_scripts_SH : chaque .sh compare LOCAL vs PROD docs)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import check_scripts
    return check_scripts.run(verbose=False)


# ═══ PV ══════════════════════════════════════════════════════════════════
def rendu_md(p1, p2, p3, p4, p5, p6, p7, now):
    L = []
    A = L.append
    A(f"# PROCES-VERBAL D'AUDIT - PROJET HA ReBuild")
    A(f"")
    A(f"- **Date** : {now.strftime('%Y-%m-%d %H:%M:%S')}")
    A(f"- **Perimetre** : LOCAL `{LOCAL}` / PROD `{PROD}` / GITHUB (repo git H:)")
    A(f"- **Nature** : constat en lecture seule - aucun fichier du projet modifie.")
    A(f"- **Script** : audit_huissier.py (7 passes)")
    A("")
    # P1
    s = p1["sections"]
    A("## PASSE 1 - ARBORESCENCES (TREE)")
    A(f"- LOCAL docs/ : **{s['local_docs_count']} fichiers** | PROD docs/ : **{s['prod_docs_count']}** | GITHUB docs/ : **{s['github_docs_count']}**")
    A(f"- Fichiers seulement LOCAL : {s['n_only_local']} | seulement PROD : {s['n_only_prod']} | seulement GITHUB : {s['n_only_github']}")
    if s["only_local"]:
        A(""); A("<details><summary>Details only LOCAL (max 80)</summary>"); A("")
        for f in s["only_local"]:
            A(f"- {f}")
        A(""); A("</details>")
    if s["only_prod"]:
        A(""); A("<details><summary>Details only PROD (max 80)</summary>"); A("")
        for f in s["only_prod"]:
            A(f"- {f}")
        A(""); A("</details>")
    A("")
    # P2
    st = p2.get("stats", {})
    g = p2.get("git", {})
    A("## PASSE 2 - MD5 TRIANGULATION")
    A("")
    A("### Volet A - HORS DOCS (YAML config HA) - regle : PROD et GITHUB IDENTIQUES")
    prod_gh = g.get("prod_egal_github")
    A(f"- Verdict : **{'CONFORME' if prod_gh else 'ECART'}** (PROD == GITHUB)")
    A(f"- HEAD {g.get('HEAD','?')} vs origin/main {g.get('origin_main','?')} : {'identiques' if g.get('identiques') else 'DIFFERENTS'}")
    A(f"- Fichiers hors-docs modifies non commites sur H: : {len(g.get('modifs_hors_docs', []))}")
    for l in g.get("modifs_hors_docs", [])[:25]:
        A(f"  - {l}")
    A("")
    A("### Volet B - DOCS - regle : LOCAL = source de verite (local -> H:\\Docs -> GitHub)")
    A(f"- Fichiers compares (docs) : {p2.get('total', 0)}")
    A(f"- SYNC : {st.get('SYNC', 0)} | CRLF seul : {st.get('CRLF', 0)} | DIFF : {st.get('DIFF', 0)} | absent PROD : {st.get('ABSENT_PROD', 0)} | absent LOCAL : {st.get('ABSENT_LOCAL', 0)}")
    A(f"- Fichiers docs modifies non commites sur H: : {len(g.get('modifs_docs', []))}")
    for l in g.get("modifs_docs", [])[:25]:
        A(f"  - {l}")
    det = p2.get("details", {})
    if det:
        A("")
        A("Preuves MD5 des fichiers divergents (brut puis normalise LF) - GITHUB lu via git HEAD :")
        A("")
        A("| Fichier | L brut | P brut | G brut | L norm | P norm | G norm |")
        A("|---|---|---|---|---|---|---|")
        for rel, d in sorted(det.items()):
            A(f"| {rel} | {d['L']} | {d['P']} | {d['G']} | {d['L_norm']} | {d['P_norm']} | {d['G_norm']} |")
    if p2["diffs"]:
        A(""); A(f"<details><summary>Ecarts ({len(p2['diffs'])})</summary>"); A("")
        for why, rel in p2["diffs"][:120]:
            A(f"- {why} : {rel}")
        A(""); A("</details>")
    A("")
    # P3
    A("## PASSE 3 - DEPENDANCES")
    A(f"- DEPENDANCES_GLOBALES.md present : **{p3['matrice_presente']}**"
      + ("" if p3["matrice_presente"] else f"  (chemin cherche : `{MATRICE}`)")
      + f" | matrice : **{p4.get('n_matrice','?')} entites**")
    for l in p3.get("matrice_entete", []):
        A(f"  - `{l.strip()[:110]}`")
    A(f"- YAML config analyses : {p3['n_yaml_config']} | avec header CHAINE DE DEPENDANCES : {p3['n_avec_header_chaines']}")
    A(f"- References de fichiers cassees : **{len(p3['refs_cassees'])}** | vignettes introuvables : **{len(p3['vignettes_absentes'])}**")
    if p3["refs_cassees"]:
        A(""); A("<details><summary>References cassees</summary>"); A("")
        for f, ref in p3["refs_cassees"][:80]:
            A(f"- `{ref}` cite dans {f}")
        A(""); A("</details>")
    A("")
    # P4
    A("## PASSE 4 - ENTITY INDEX")
    A(f"- Fichiers YAML actifs : {p4['n_fichiers']} | entites YAML uniques : {p4['n_entites_yaml']} | entites dans la matrice : {p4['n_matrice']}")
    A(f"- Entites NON referencees dans la matrice : **{p4['n_non_ref']}**")
    for d, c in list(p4["non_ref_par_domaine"].items())[:10]:
        A(f"  - {d} : {c}")
    A(f"- Entites fantomes (matrice sans YAML) : **{p4['n_fantomes']}**")
    if p4["fantomes"]:
        A(""); A("<details><summary>Fantomes (max 80)</summary>"); A("")
        for e in p4["fantomes"]:
            A(f"- {e}")
        A(""); A("</details>")
    A("")
    # P5
    A("## PASSE 5 - FORMAT (box ASCII + identifiants) - source de verite PROD H:")
    box = p5.get("box", {})
    ids = p5.get("ids", {})
    res = p5.get("residuel", {})
    A("")
    A("### 5a - BOX ASCII (2 types : principale ╭/╰ et secondaire ┌/┐)")
    A(f"- Fichiers analyses : {box.get('n_fichiers', '?')} | conformes : {box.get('n_conformes', '?')} | avec ecarts : {len(box.get('fichiers', []))}")
    for c, n in sorted(box.get("stats", {}).items(), key=lambda x: -x[1]):
        A(f"  - {c} : {n}")
    if box.get("fichiers"):
        A(""); A("<details><summary>Details box (max 150)</summary>"); A("")
        for r in box["fichiers"][:150]:
            A(f"- **{r['fichier']}**")
            for c, msg in r["ecarts"][:10]:
                A(f"  - {c} : {msg}")
            if len(r["ecarts"]) > 10:
                A(f"  - ... et {len(r['ecarts'])-10} autres")
        A(""); A("</details>")
    A("")
    A("### 5b - SLUG / NAME / UNIQUE_ID")
    A(f"- Fichiers : {ids.get('n_fichiers', '?')} | unique_id : {ids.get('n_uid', '?')}")
    A(f"- Sans slug tertiaire : {ids.get('n_sans_slug', 0)} | slug incoherent avec le unique_id : {ids.get('n_slugs_faux', 0)} | sans name : {ids.get('n_sans_name', 0)}")
    if ids.get("fichiers"):
        A(""); A("<details><summary>Details identifiants</summary>"); A("")
        for r in ids["fichiers"]:
            A(f"- **{r['fichier']}** ({r['n_uid']} uid)")
            for uid, l in r["sans_slug"]:
                A(f"  - SLUG-ABSENT l.{l} : {uid}")
            for uid, l, s in r["slugs_faux"]:
                A(f"  - SLUG-INCOHERENT l.{l} : uid={uid} / slug={s}")
            for uid, l in r["sans_name"]:
                A(f"  - NAME-ABSENT l.{l} : {uid}")
        A(""); A("</details>")
    A("")
    if res:
        A(f"### 5c - Residuel (headers, caracteres interdits, nommage, tabs) - {res.get('n_fichiers_total', '?')} fichiers")
        for cat, n in sorted(res.get("resume", {}).items(), key=lambda x: -x[1]):
            if cat != "CONFORME":
                A(f"  - {cat} : {n}")
        if res.get("fichiers"):
            A(""); A("<details><summary>Details residuel (max 150)</summary>"); A("")
            for rel, ecarts in res["fichiers"][:150]:
                A(f"- **{rel}**")
                for cat, msg in ecarts[:10]:
                    A(f"  - {cat} : {msg}")
            A(""); A("</details>")
    A("")
    # P6
    A("## PASSE 6 - AUTOMATIONS (automations.yaml PROD vs fichiers LOCAUX)")
    st6 = p6.get("stats", {})
    A(f"- automations.yaml : {p6.get('total_prod', '?')} automations | fichiers locaux : {p6.get('total_fichiers', '?')}")
    A(f"- OK : {st6.get('OK', 0)} | DIFF : {st6.get('DIFF', 0)} | sans fichier local : {st6.get('ABSENT_LOCAL', 0)} | orphelins : {len(p6.get('orphelins', []))}")
    if p6.get("resultats"):
        A("")
        A("<details><summary>Details des ecarts</summary>")
        A("")
        for r in p6["resultats"]:
            if r["statut"] == "OK":
                continue
            A(f"- **[{r['statut']}] {r['alias']}**" + (f" ({r['fichier']})" if r.get("fichier") else ""))
            for chemin, vprod, vloc, _ in r["diffs"][:10]:
                A(f"  - `{chemin}` : PROD `{vprod}` vs LOCAL `{vloc}`")
            if len(r["diffs"]) > 10:
                A(f"  - ... et {len(r['diffs'])-10} autres differences")
        if p6.get("archives"):
            A("")
            A(f"Archives locales (dossier old/, versions anterieures - non comparees) : {len(p6['archives'])}")
            for rel in p6["archives"][:40]:
                A(f"  - {rel}")
        if p6.get("orphelins"):
            A("")
            A(f"Orphelins (fichier local sans automation dans le prod) : {len(p6['orphelins'])}")
            for rel in p6["orphelins"][:40]:
                A(f"  - {rel}")
        A("")
        A("</details>")
    A("")
    # P7
    A("## PASSE 7 - SCRIPTS (scripts.yaml + .sh)")
    y7 = p7.get("yaml", {})
    ya = p7.get("yaml_stats", {})
    sh = p7.get("sh", {})
    sb = p7.get("sh_stats", {})
    A(f"- Scripts YAML : {y7.get('total_prod', '?')} scripts prod | OK {ya.get('OK', 0)} | DIFF {ya.get('DIFF', 0)} | sans fichier local {ya.get('ABSENT_LOCAL', 0)}")
    for r in y7.get("resultats", []):
        if r["statut"] == "OK":
            continue
        A(f"  - **[{r['statut']}] {r['nom']}**" + (f" ({r['fichier']})" if r.get("fichier") else ""))
        for c, vp, vl, _ in r["diffs"][:10]:
            A(f"    - `{c}` : PROD `{vp}` vs LOCAL `{vl}`")
        if len(r["diffs"]) > 10:
            A(f"    - ... et {len(r['diffs'])-10} autres")
        if r.get("autres_versions"):
            A(f"    - versions anterieures non retenues : {', '.join(r['autres_versions'])}")
    if y7.get("orphelins"):
        A(f"  - Orphelins locaux (cle sans script prod) : {', '.join(y7['orphelins'])}")
    A(f"- Scripts SH : OK {sb.get('OK', 0)} | DIFF {sb.get('DIFF', 0)} | absents local {sb.get('ABSENT_LOCAL', 0)} | absents prod {sb.get('ABSENT_PROD', 0)}")
    for r in sh.get("resultats", []):
        if r["statut"] == "OK":
            continue
        A("")
        A(f"  - **[{r['statut']}] {r['fichier']}** (L={r['md5_local']} P={r['md5_prod']})")
        A("```diff")
        for l in r.get("diff", [])[:20]:
            A(l)
        A("```")
    A("")
    A("---")
    A("*Fin du proces-verbal. Constats uniquement : aucune correction appliquee. Mise a jour des automations : generalement depuis automations.yaml prod vers le fichier local, apres analyse et GO utilisateur.*")
    return "\n".join(L)


def main():
    now = datetime.datetime.now()
    os.makedirs(OUT_DIR, exist_ok=True)
    print(f"AUDIT HUISSIER - {now.strftime('%Y-%m-%d %H:%M')} - lecture seule")
    steps = [("PASSE 1 - TREE", passe1_tree), ("PASSE 2 - MD5", passe2_md5),
             ("PASSE 3 - DEPENDANCES", passe3_deps), ("PASSE 4 - ENTITIES", passe4_entity),
             ("PASSE 5 - FORMAT", passe5_format), ("PASSE 6 - AUTOMATIONS", passe6_automations),
             ("PASSE 7 - SCRIPTS", passe7_scripts)]
    results = {}
    for label, fn in steps:
        try:
            results[label] = fn()
            print(f"  [OK] {label}")
        except Exception as e:
            results[label] = {"pass": label, "error": str(e)}
            print(f"  [ERREUR] {label} : {e}")

    p1 = results["PASSE 1 - TREE"]
    p2 = results["PASSE 2 - MD5"]
    p3 = results["PASSE 3 - DEPENDANCES"]
    p4 = results["PASSE 4 - ENTITIES"]
    p5 = results["PASSE 5 - FORMAT"]
    p6 = results["PASSE 6 - AUTOMATIONS"]
    p7 = results["PASSE 7 - SCRIPTS"]

    md = rendu_md(p1, p2, p3, p4, p5, p6, p7, now)
    pv = os.path.join(OUT_DIR, f"PV_audit_{now.strftime('%Y-%m-%d_%H%M')}.md")
    with open(pv, "w", encoding="utf-8") as f:
        f.write(md)
    det = os.path.join(OUT_DIR, "audit_details.json")
    with open(det, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=1, default=str)

    print()
    print(f"  PV  : {pv}")
    print(f"  JSON: {det}")
    # resume console
    st = p2.get("stats", {})
    print(f"  TREE    : {p1['sections']['local_docs_count']} local / {p1['sections']['prod_docs_count']} prod / {p1['sections']['github_docs_count']} github")
    print(f"  MD5     : {st.get('SYNC',0)} SYNC / {st.get('CRLF',0)} CRLF / {st.get('DIFF',0)} DIFF / {st.get('ABSENT_PROD',0)} absents PROD")
    print(f"  DEPS    : {len(p3.get('refs_cassees',[]))} refs cassees / {len(p3.get('vignettes_absentes',[]))} vignettes introuvables")
    print(f"  ENTITY  : {p4.get('n_non_ref','?')} non referencees / {p4.get('n_fantomes','?')} fantomes")
    b5, i5, r5 = p5.get("box", {}), p5.get("ids", {}), p5.get("residuel", {})
    print(f"  BOX     : {b5.get('n_conformes','?')} conformes / {len(b5.get('fichiers',[]))} avec ecarts (PROD)")
    print(f"  IDENT   : {i5.get('n_uid','?')} uid / {i5.get('n_sans_slug',0)} sans slug / {i5.get('n_slugs_faux',0)} slugs incoherents / {i5.get('n_sans_name',0)} sans name")
    print(f"  RESIDU  : {len(r5.get('fichiers',[]))} fichiers avec ecarts (headers/caracteres/nommage)")
    st6 = p6.get("stats", {})
    print(f"  AUTOM   : {st6.get('OK',0)} OK / {st6.get('DIFF',0)} DIFF / {st6.get('ABSENT_LOCAL',0)} sans fichier local / {len(p6.get('orphelins',[]))} orphelins / {len(p6.get('archives',[]))} archives")
    y7, sh7 = p7.get("yaml_stats", {}), p7.get("sh_stats", {})
    print(f"  SCRIPTS : YAML {y7.get('OK',0)} OK / {y7.get('DIFF',0)} DIFF / {y7.get('ABSENT_LOCAL',0)} sans fichier local | SH {sh7.get('OK',0)} OK / {sh7.get('DIFF',0)} DIFF")


if __name__ == "__main__":
    main()
