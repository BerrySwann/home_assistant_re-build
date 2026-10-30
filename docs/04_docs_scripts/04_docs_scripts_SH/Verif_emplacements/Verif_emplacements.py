# -*- coding: utf-8 -*-
r"""
Verif_emplacements.py - controle EN LECTURE SEULE des fichiers presents a plusieurs emplacements.
Carte des emplacements : docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS/IA_CARTE_EMPLACEMENTS.md
Cree le 2026-10-18 a la demande d'Eric.

Pour chaque fichier de la carte, empreinte git blob SHA-1 (8 caracteres) a 5 emplacements :
  L  = local ReBuild (source de verite)
  PR = prod racine /config (H:\)
  PM = prod miroir docs (H:\docs\...)
  GR = GitHub racine du depot
  GD = GitHub sous docs/
Ecrit : historique/03_RAPPORTS/06_MD5/03_VERIF_EMPLACEMENTS/verif_emplacements_AAAA-MM-JJ.txt
(le rapport du jour existant est d'abord renomme en .bak_AAAA_MM_JJ_HHhMMmSSs.txt)
Codes retour : 0 rapport ecrit ; 2 prod H: inaccessible (rien ecrit).
GitHub injoignable : rapport ecrit avec GR/GD = '?' (aucun verdict GitHub).
"""
import os, sys, hashlib, json, urllib.request, datetime

REBUILD = r'C:\Users\Berry Swann\Documents\ReBuild'
PROD = 'H:\\'
REPO = 'BerrySwann/home_assistant_re-build'
CFG = 'docs/01_docs_config_system/01_config_system_SH_PY_YAML'
MD = 'docs/01_docs_config_system/01_config_system_MD'
RAPPORT_DIR = os.path.join(REBUILD, 'historique', '03_RAPPORTS', '06_MD5', '03_VERIF_EMPLACEMENTS')

# fichiers de config_system_MD qui ont aussi une copie a la racine de la prod (local -> racine)
RACINE_MD = {MD + '/GLOBAL_INDEX_REPO/GLOBAL_INDEX_REPO.md': 'GLOBAL_INDEX_REPO.md',
             MD + '/README/README.md': 'README.md'}
# laisses en prod seule (decisions d'Eric du 2026-10-18) : jamais un ecart
PROD_SEULE_DOSSIERS = {'notifs', 'themes', 'blueprints'}
EXCLUS_NOMS = {'secrets.yaml', 'scenes.yaml', 'ip_bans.yaml'}
SOUS_DOSSIERS_SCRIPTS = ('01_scripts.sh', '02_scripts.py')


def ignore(name):
    n = name.lower()
    return '.bak' in n or n in EXCLUS_NOMS


def verrou(name):
    # fichier verrou d'editeur (ex. #MP_01_monitor_temp.sh.#) : en prod seule, jamais sur GitHub (.gitignore)
    return len(name) > 2 and name.startswith('#') and name.endswith('#')


def blob_file(path):
    with open(path, 'rb') as f:
        d = f.read()
    return hashlib.sha1(b'blob %d\0' % len(d) + d).hexdigest()


def exact(root, rel):
    """chemin du fichier si rel existe avec la casse exacte, sinon None"""
    cur = root
    for seg in rel.split('/'):
        try:
            names = os.listdir(cur)
        except OSError:
            return None
        if seg not in names:
            return None
        cur = os.path.join(cur, seg)
    return cur if os.path.isfile(cur) else None


def dossier_du_fichier(nom):
    """dossier propre a un fichier en local : <nom sans extension>_<extension> (ex. ha_git_backup_sh)"""
    stem, ext = os.path.splitext(nom)
    return stem + '_' + ext.lstrip('.')


def aplatir(rel_cfg):
    """(chemin a plat comme en prod, remarque) ; remarque = None si la structure suit la regle.
    Regle (Eric, 2026-10-29) : en local, chaque script de .scripts et chaque YAML de command_line a son
    dossier <nom>_<ext> ; en prod (HA) tout est a plat : /config/.scripts/<fichier> et
    /config/command_line/<categorie>/<fichier>. Un dossier qui ne suit pas la regle n'est pas devine."""
    p = rel_cfg.split('/')
    if p[0] == '.scripts':
        if len(p) >= 3 and p[1] in SOUS_DOSSIERS_SCRIPTS:
            p = [p[0]] + p[2:]
        cible = 2
    elif p[0] == 'command_line':
        cible = 3
    else:
        return rel_cfg, None
    if len(p) == cible:
        return '/'.join(p), None
    if len(p) == cible + 1 and p[-2] == dossier_du_fichier(p[-1]):
        return '/'.join(p[:-2] + p[-1:]), None
    return rel_cfg, 'dossier ne suivant pas la regle <nom>_<ext> (en prod tout est a plat)'


def racine_de(rel_cfg):
    """chemin a la racine de la prod d'un fichier de 01_config_system_SH_PY_YAML"""
    return aplatir(rel_cfg)[0]


def lister(root):
    out = []
    for dp, dns, fns in os.walk(root):
        for fn in fns:
            out.append(os.path.relpath(os.path.join(dp, fn), root).replace('\\', '/'))
    return out


def api(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'verif-emplacements'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode('utf-8'))


def github():
    c = api('https://api.github.com/repos/%s/commits?per_page=1' % REPO)[0]
    t = api('https://api.github.com/repos/%s/git/trees/%s?recursive=1' % (REPO, c['sha']))
    if t.get('truncated'):
        raise RuntimeError('arbre GitHub tronque')
    blobs = {e['path']: e['sha'] for e in t['tree'] if e['type'] == 'blob'}
    return c['sha'][:8], c['commit']['author']['date'], c['commit']['message'].splitlines()[0], blobs


def main():
    if not os.path.isdir(os.path.join(PROD, 'docs')):
        print('prod H: inaccessible : rien ecrit')
        return 2
    now = datetime.datetime.now()
    try:
        gsha, gdate, gmsg, gh = github()
        gtxt = 'commit %s du %s (%s)' % (gsha, gdate, gmsg)
    except Exception as e:
        gh = None
        gtxt = 'GitHub injoignable (%s) : colonnes GR et GD = ?' % e

    # 1. liste des fichiers suivis : (libelle, L, PR, PM, GR, GD)
    items = []
    nonconf = []
    cfg_root = os.path.join(REBUILD, CFG.replace('/', os.sep))
    for rel in sorted(lister(cfg_root)):
        top = rel.split('/')[0]
        if top in PROD_SEULE_DOSSIERS or ignore(os.path.basename(rel)) or '#' in rel:
            continue
        r, remarque = aplatir(rel)
        if remarque:
            nonconf.append((rel, remarque))
        items.append((rel, CFG + '/' + rel, r, CFG + '/' + rel, r, CFG + '/' + rel))
    for lrel, r in RACINE_MD.items():
        items.append((lrel, lrel, r, lrel, r, lrel))

    lignes, comptes = [], {}
    suivis_racine, suivis_miroir = set(), set()
    for lib, l, pr, pm, gr, gd in items:
        suivis_racine.add(pr)
        suivis_miroir.add(pm)
        v = {}
        p = exact(REBUILD, l)
        v['L'] = blob_file(p) if p else None
        p = exact(PROD, pr)
        v['PR'] = blob_file(p) if p else None
        p = exact(PROD, pm)
        v['PM'] = blob_file(p) if p else None
        if gh is None:
            v['GR'] = v['GD'] = '?'
        else:
            v['GR'] = gh.get(gr)
            v['GD'] = gh.get(gd)
        manque = [k for k in ('L', 'PR', 'PM', 'GR', 'GD') if v[k] is None]
        loc = v['L']
        prod_diff = [k for k in ('PR', 'PM') if v[k] is not None and v[k] != loc]
        gh_diff = [k for k in ('GR', 'GD') if v[k] not in (None, '?') and v[k] != loc]
        if manque and set(manque) <= {'GR', 'GD'} and not prod_diff and v['PR'] == loc and v['PM'] == loc:
            verdict = 'GITHUB EN ATTENTE DU BACKUP absent ' + '+'.join(manque)
            if gh_diff:
                verdict += ' / different ' + '+'.join(gh_diff)
        elif manque:
            verdict = 'ABSENT ' + '+'.join(manque)
            if prod_diff or gh_diff:
                verdict += ' / DIFFERENT ' + '+'.join(prod_diff + gh_diff)
        elif prod_diff:
            verdict = 'PROD DIFFERENTE DU LOCAL ' + '+'.join(prod_diff)
            if gh_diff:
                verdict += ' (GitHub different aussi)'
        elif gh_diff:
            verdict = 'GITHUB EN ATTENTE DU BACKUP ' + '+'.join(gh_diff)
        else:
            verdict = 'SYNC'
        comptes[verdict.split(' ')[0]] = comptes.get(verdict.split(' ')[0], 0) + 1
        def c(k):
            return '-' if v[k] is None else ('?' if v[k] == '?' else v[k][:8])
        lignes.append((verdict, '%-8s %-8s %-8s %-8s %-8s' % (c('L'), c('PR'), c('PM'), c('GR'), c('GD')), lib))

    # 2. fichiers presents ailleurs mais pas en local (dans le perimetre suivi)
    seuls = []
    attendus = []
    tops = sorted({x[0].split('/')[0] for x in items if not x[0].startswith('docs/')})
    for top in tops:
        base = os.path.join(PROD, top)
        if not os.path.isdir(base):
            continue
        for rel in lister(base):
            rr = top + '/' + rel
            if not ignore(os.path.basename(rr)) and rr not in suivis_racine:
                if verrou(os.path.basename(rr)):
                    attendus.append(('VERROU EDITEUR PROD RACINE (attendu)', rr))
                else:
                    seuls.append(('PROD RACINE SEULE', rr))
    mir = os.path.join(PROD, CFG.replace('/', os.sep))
    if os.path.isdir(mir):
        for rel in lister(mir):
            rr = CFG + '/' + rel
            if rel.split('/')[0] in PROD_SEULE_DOSSIERS or ignore(os.path.basename(rel)):
                continue
            if rr not in suivis_miroir:
                if verrou(os.path.basename(rel)):
                    attendus.append(('VERROU EDITEUR PROD MIROIR (attendu)', rr))
                else:
                    seuls.append(('PROD MIROIR SEUL', rr))
    if gh is not None:
        for path in gh:
            top = path.split('/')[0]
            if path.startswith(CFG + '/'):
                if path.split('/')[3] not in PROD_SEULE_DOSSIERS and not ignore(os.path.basename(path)) and path not in suivis_miroir:
                    seuls.append(('GITHUB DOCS SEUL', path))
            elif top in tops and not ignore(os.path.basename(path)) and path not in suivis_racine:
                seuls.append(('GITHUB RACINE SEUL', path))

    # 3. rapport
    os.makedirs(RAPPORT_DIR, exist_ok=True)
    out = os.path.join(RAPPORT_DIR, 'verif_emplacements_%s.txt' % now.strftime('%Y-%m-%d'))
    if os.path.exists(out):
        os.rename(out, out[:-4] + '.bak_%s.txt' % now.strftime('%Y_%m_%d_%Hh%Mm%Ss'))
    nb_anom = sum(n for k, n in comptes.items() if k != 'SYNC') + len(seuls) + len(nonconf)
    txt = ['VERIF EMPLACEMENTS - %s (lecture seule)' % now.strftime('%Y-%m-%d %H:%M:%S'),
           'Carte : docs/00_IA/00_IA_SOUS_CONTEXT_IA/IA_CARTE_EMPLACEMENTS/IA_CARTE_EMPLACEMENTS.md',
           'GitHub : ' + gtxt,
           'Colonnes : L local | PR prod racine /config | PM prod miroir docs | GR GitHub racine | GD GitHub docs/ (empreinte git blob, - = absent)',
           '', '== 1. FICHIERS SUIVIS (%d) ==' % len(lignes)]
    for verdict, cols, lib in sorted(lignes, key=lambda x: (x[0] == 'SYNC', x[0], x[2])):
        txt.append('%-45s | %s | %s' % (verdict, cols, lib))
    txt += ['', '== 2. PRESENTS AILLEURS QU EN LOCAL (%d) ==' % len(seuls)]
    for k, p in sorted(seuls):
        txt.append('%-20s | %s' % (k, p))
    txt += ['', '== 3. ECARTS ATTENDUS (%d) : fichiers verrou d editeur #...# en prod seule, ignores par le .gitignore, pas une anomalie ==' % len(attendus)]
    for k, p in sorted(attendus):
        txt.append('%-40s | %s' % (k, p))
    txt += ['', '== 4. STRUCTURE NON CONFORME (%d) : le dossier d un fichier de .scripts ou command_line ne suit pas la regle <nom>_<ext>, chemin a plat non devine ==' % len(nonconf)]
    for rel, rq in sorted(nonconf):
        txt.append('%s | %s' % (rel, rq))
    res = 'RESULTAT : %d fichiers suivis - %s - presents ailleurs qu en local %d - structure non conforme %d' % (
        len(lignes), ' - '.join('%s %d' % (k, n) for k, n in sorted(comptes.items())), len(seuls), len(nonconf))
    txt += ['', 'ANOMALIES : ' + ('aucune' if nb_anom == 0 else 'x %d' % nb_anom), res]
    with open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(txt) + '\n')
    print('rapport : ' + out)
    print('GitHub : ' + gtxt)
    print('ANOMALIES : ' + ('aucune' if nb_anom == 0 else 'x %d' % nb_anom))
    print(res)
    return 0


if __name__ == '__main__':
    sys.exit(main())