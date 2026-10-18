#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hermes_audit_trigul_arbres.py - superposition des 3 arbres GITHUB / LOCAL / PROD (docs/). LECTURE SEULE.

Principe (demande d'Eric, 2026-10-17) :
  Une ligne par fichier, trois colonnes dans cet ordre : R (GitHub), L (local), P (prod).
  Chaque case contient l'empreinte courte du fichier, ou - s'il n'existe pas a ce niveau.
  Phase 1 : superposition des chemins. Ce qui n'existe pas aux 3 niveaux (en trop / manquant) est mis
            de cote avec son origine. Une casse differente entre niveaux est signalee a part.
  Phase 2 : sur les chemins communs (meme casse), comparaison des empreintes (git blob SHA-1 des octets ;
            GitHub la fournit dans sa liste, rien a telecharger).
  VERDICT : nomme le niveau en retard ou different (le local est la source de verite : "different"
            ne veut pas dire "faux").
Option --tout : liste aussi les fichiers SYNC (par defaut seulement leur total).
Le script ne modifie, ne pousse et ne supprime rien. Il n'ecrit que son rapport dans historique/MD5.
"""
import os, sys, json, hashlib, collections, datetime, shutil, time, urllib.request

LOCAL = r'C:\Users\Berry Swann\Documents\ReBuild\docs'
PROD = r'H:\docs'
LOCAL_README = r'C:\Users\Berry Swann\Documents\ReBuild\Github\README.md'
PROD_README = r'H:\README.md'
REPO = 'BerrySwann/home_assistant_re-build'
OUT_DIR = r'C:\Users\Berry Swann\Documents\ReBuild\historique\MD5'
ROOT = '(racine)/README.md'

# Ecarts ATTENDUS (a part, avec la raison). Tout le reste est signale comme anomalie.
GITIGNORE_EXT = {'.txt', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico', '.pyc'}
EXCEPTIONS_TXT = [

    "archives locales (nom contenant _archive_) presentes en local seulement : restent en local",
    "exports Dashboard_COMPLET plus anciens que le plus recent (Dashboard_AAAA_MM_JJ.yaml), en local seulement : seul le plus recent est controle",
    "fichiers .txt .png .jpg .jpeg .gif .webp .ico .pyc presents en local + prod mais absents de GitHub : ignores par le .gitignore du depot",
    "dossier modifs/ (journaux des agents) : ignore aux 3 niveaux, comme l audit MD5 docs cote HA",
]

DASH_LATEST = ''
V_PROD = 'PROD seule differente (suspect)'
V_TROIS = '3 contenus differents (a voir a la main)'
V_LOCAL = 'LOCAL en avance (prod et GitHub en retard)'
V_GITHUB = 'GITHUB en retard (attend le backup HA)'
V_EOL = 'fin de ligne seule (sans action)'
V_CASSE = 'CASSE differente entre niveaux'
V_PRES = {
    'PR': 'ABSENT du LOCAL (ancien nom ?)',
    'LR': 'ABSENT de la PROD',
    'LP': 'ABSENT de GITHUB (attend le backup HA)',
    'L': 'LOCAL seul (jamais pousse en prod)',
    'P': 'PROD seule',
    'R': 'GITHUB seul',
}
ORDRE = [V_PROD, V_TROIS, V_LOCAL, V_GITHUB, V_EOL, V_CASSE,
         V_PRES['PR'], V_PRES['LR'], V_PRES['LP'], V_PRES['L'], V_PRES['P'], V_PRES['R']]


def gsha(b):
    return hashlib.sha1(b'blob %d\x00' % len(b) + b).hexdigest()


_cache = {}


def fh(path):
    if path not in _cache:
        with open(path, 'rb') as f:
            data = f.read()
        _cache[path] = (gsha(data), gsha(data.replace(b'\r\n', b'\n')))
    return _cache[path]


def scan(root, skip_bak=False):
    out = {}
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if skip_bak and '.bak' in f.lower():
                continue
            full = os.path.join(dp, f)
            out[os.path.relpath(full, root).replace('\\', '/')] = full
    return out


def api(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'trigul-arbres'})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def attendu(rel, origin):
    low = rel.lower()
    name = low.rsplit('/', 1)[-1]
    if origin == 'L' and '.bak' in name:
        return 'sauvegarde locale'
    if origin == 'L' and '_archive_' in name:
        return 'archive locale'
    if (origin == 'L' and '/dashboard_complet/' in '/' + low and name.startswith('dashboard_')
            and name.endswith('.yaml') and name != DASH_LATEST):
        return 'ancien export Dashboard (seul le plus recent est controle)'
    if origin == 'LP' and os.path.splitext(name)[1] in GITIGNORE_EXT:
        return 'type ignore par le .gitignore du depot'
    if origin == 'PR' and low.startswith('modifs/'):
        return 'journal des agents (copie H: seulement)'
    return None


def verdict_trois(lp, pr, lr):
    if lp == pr == lr == 'OK':
        return 'SYNC'
    if 'DIFF' not in (lp, pr, lr):
        return V_EOL
    eq_lp, eq_pr, eq_lr = lp != 'DIFF', pr != 'DIFF', lr != 'DIFF'
    if eq_pr and not eq_lp:
        return V_LOCAL
    if eq_lp and not eq_pr:
        return V_GITHUB
    if eq_lr and not eq_lp:
        return V_PROD
    return V_TROIS

def par_ext(keys):
    n = {'md': 0, 'yaml': 0, 'sh': 0, 'autres': 0}
    for k in keys:
        e = os.path.splitext(k)[1].lower()
        if e == '.md':
            n['md'] += 1
        elif e in ('.yaml', '.yml'):
            n['yaml'] += 1
        elif e == '.sh':
            n['sh'] += 1
        else:
            n['autres'] += 1
    return n


def ligne_res(nom, keys):
    n = par_ext(keys)
    return 'RESULTAT %-7s : %d fichiers (%d .md, %d .yaml, %d .sh, %d autres)' % (nom, len(keys), n['md'], n['yaml'], n['sh'], n['autres'])


def ligne_audit(aud):
    a = [(p, c) for p, c in aud if os.path.splitext(p)[1].lower() in ('.md', '.yaml', '.yml', '.sh')]
    n = par_ext([p for p, c in a])
    k = collections.Counter(c for p, c in a)
    txt = ('RESULTAT AUDIT : %d fichiers (%d .md - %d .yaml - %d .sh) - SYNC %d - fin de ligne seule %d - DIFF %d - CASSE %d'
           ' - ABSENT GITHUB %d - ABSENT PROD %d - ABSENT LOCAL %d - ABSENT 2 NIVEAUX %d') % (
        len(a), n['md'], n['yaml'], n['sh'], k['SYNC'], k['EOL'], k['DIFF'], k['CASSE'],
        k['ABS_R'], k['ABS_P'], k['ABS_L'], k['ABS2'])
    ok = sum(k.values()) == len(a)
    return txt, ok


def main():
    t0 = time.time()
    tout = '--tout' in sys.argv
    today = datetime.date.today().isoformat()
    L = scan(LOCAL, True)
    P = scan(PROD)
    if os.path.isfile(LOCAL_README):
        L[ROOT] = LOCAL_README
    if os.path.isfile(PROD_README):
        P[ROOT] = PROD_README
    c = api('https://api.github.com/repos/%s/commits?per_page=1' % REPO)
    csha = c[0]['sha']
    cdate = c[0]['commit']['committer']['date']
    cmsg = c[0]['commit']['message'].split('\n')[0]
    t = api('https://api.github.com/repos/%s/git/trees/%s?recursive=1' % (REPO, csha))
    if t.get('truncated'):
        print('ERREUR : liste GitHub tronquee, audit impossible')
        return 2
    R = {}
    for e in t['tree']:
        if e['type'] != 'blob':
            continue
        if e['path'].startswith('docs/'):
            R[e['path'][5:]] = e['sha']
        elif e['path'] == 'README.md':
            R[ROOT] = e['sha']
    L = {k: v for k, v in L.items() if not k.lower().startswith('modifs/')}
    P = {k: v for k, v in P.items() if not k.lower().startswith('modifs/')}
    R = {k: v for k, v in R.items() if not k.lower().startswith('modifs/')}
    cands = sorted(k.lower().rsplit('/', 1)[-1] for k in L
                   if '/dashboard_complet/' in '/' + k.lower()
                   and k.lower().rsplit('/', 1)[-1].startswith('dashboard_')
                   and k.lower().endswith('.yaml'))
    globals()['DASH_LATEST'] = cands[-1] if cands else ''
    LV = {'L': L, 'P': P, 'R': R}

    keys = collections.defaultdict(lambda: {'L': set(), 'P': set(), 'R': set()})
    for lv, d in LV.items():
        for rel in d:
            keys[rel.lower()][lv].add(rel)

    def hs(lv, rel):
        if lv == 'R':
            return (R[rel], R[rel])
        return fh(LV[lv][rel])

    def pair(a, b):
        if a[0] == b[0]:
            return 'OK'
        if a[1] == b[1] or a[1] == b[0] or a[0] == b[1]:
            return 'EOL'
        return 'DIFF'

    def cells(kv):
        out = {}
        for lv in 'RLP':
            out[lv] = hs(lv, sorted(kv[lv])[0])[0][:8] if kv[lv] else '-'
        return out

    rows = []
    aud = []
    attendus = []
    sync = []
    n_bak = 0
    for k in sorted(keys):
        kv = keys[k]
        present = ''.join(lv for lv in 'LPR' if kv[lv])
        names = set().union(*[kv[lv] for lv in 'LPR'])
        if present == 'LPR':
            if len(names) > 1:
                ce = cells(kv)
                nom = ' / '.join('%s=%s' % (lv, sorted(kv[lv])[0]) for lv in 'RLP')
                rows.append((V_CASSE, ce['R'], ce['L'], ce['P'], nom))
                aud.append((sorted(kv['L'])[0], 'CASSE'))
                continue
            rel = next(iter(names))
            hL, hP, hR = hs('L', rel), hs('P', rel), hs('R', rel)
            v = verdict_trois(pair(hL, hP), pair(hP, hR), pair(hL, hR))
            if v == 'SYNC':
                sync.append((hR[0][:8], rel))
                aud.append((rel, 'SYNC'))
            else:
                rows.append((v, hR[0][:8], hL[0][:8], hP[0][:8], rel))
                aud.append((rel, 'EOL' if v == V_EOL else 'DIFF'))
            continue
        rel = sorted(names)[0]
        detail = []
        if len(names) > 1:
            detail.append('casse differente : ' + ' / '.join(
                '%s=%s' % (lv, sorted(kv[lv])[0]) for lv in 'RLP' if kv[lv]))
        if len(present) == 2:
            a, b = present[0], present[1]
            ra, rb = sorted(kv[a])[0], sorted(kv[b])[0]
            detail.append('meme contenu' if pair(hs(a, ra), hs(b, rb)) != 'DIFF' else 'contenu different')
        why = attendu(rel, present) if len(names) == 1 else None
        if why:
            if why == 'sauvegarde locale':
                n_bak += 1
            else:
                attendus.append((present, why, '; '.join(detail), rel))
        else:
            ce = cells(kv)
            fich = rel + (('   [' + '; '.join(detail) + ']') if detail else '')
            rows.append((V_PRES[present], ce['R'], ce['L'], ce['P'], fich))
            aud.append((rel, {'LP': 'ABS_R', 'LR': 'ABS_P', 'PR': 'ABS_L'}.get(present, 'ABS2')))

    cnt = collections.Counter(r[0] for r in rows)

    def ndiff(v, hr, hl, hp):
        hh = [h for h in (hr, hl, hp) if h != '-']
        n = 3 - len(hh)
        if v != V_EOL:
            n += len(set(hh)) - 1
        if v == V_CASSE:
            n = max(n, 1)
        return n
    n_union = len(keys)
    n_att = len(attendus) + n_bak

    out = []
    A = out.append
    A('TRIGUL ARBRES - superposition GITHUB / LOCAL / PROD (docs/) - ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    A('Lecture seule. Rien n est modifie, pousse ni supprime.')
    A('GitHub  : %s commit %s du %s (%d fichiers) - %s' % (REPO, csha[:7], cdate, len(R), cmsg))
    A('Local   : %s (%d fichiers)' % (LOCAL, len(L)))
    A('Prod    : %s (%d fichiers)' % (PROD, len(P)))
    A('README racine : compare sous le nom %s' % ROOT)
    A('Colonnes : R = GitHub, L = local, P = prod ; chaque case = empreinte courte (git blob SHA-1) ou - si absent.')
    A('Le local est la source de verite : "LOCAL en avance" veut dire a pousser, pas "faux".')
    A('')
    A('ECARTS ATTENDUS (a part, avec la raison) :')
    for x in EXCEPTIONS_TXT:
        A('  - ' + x)
    A('')
    ltxt, lok = ligne_audit(aud)
    A('== AUDIT (meme perimetre que l audit MD5 docs cote HA : .md .yaml .sh, sur les 3 niveaux, hors modifs/) ==')
    A(ltxt)
    A('')
    A('== COMPTES PAR NIVEAU (perimetre docs/ + README racine, hors .bak et modifs/) ==')
    A(ligne_res('GitHub', list(R.keys())))
    A(ligne_res('local', list(L.keys())))
    A(ligne_res('prod', list(P.keys())))
    A(ligne_res('union', list(keys)))
    A('')
    A('== VUE D ENSEMBLE ==')
    A('chemins (union des 3 niveaux)   : %d' % n_union)
    A('SYNC (3 niveaux identiques)     : %d' % len(sync))
    A('a traiter                       : %d' % len(rows))
    for v in ORDRE:
        if cnt.get(v):
            A('   %-48s : %d' % (v, cnt[v]))
    A('ecarts attendus (a part)        : %d' % n_att)
    A('')
    A('== 1. A TRAITER ==')
    A('%-10s | %-10s | %-10s | %-5s | %-10s | %s' % ('R (GitHub)', 'L (local)', 'P (prod)', 'R L P', 'DIFF', 'FICHIER'))
    for v in ORDRE:
        grp = sorted([r for r in rows if r[0] == v], key=lambda r: r[4].lower())
        if not grp:
            continue
        A('-- %s (%d) --' % (v, len(grp)))
        for _, hr, hl, hp, fich in grp:
            pr3 = ['0' if h == '-' else '1' for h in (hr, hl, hp)]
            A('%-10s | %-10s | %-10s | %-5s | %-10s | %s' % ('R=' + hr, 'L=' + hl, 'P=' + hp, ' '.join(pr3), 'x %d diff' % ndiff(v, hr, hl, hp), fich))
    if not rows:
        A('(rien a traiter)')
    A('')
    A('== 2. ECARTS ATTENDUS ==')
    for pres, why, det, rel in sorted(attendus, key=lambda r: (r[1], r[3].lower())):
        A('[%s] | %s | %s | %s' % (pres, why, det or '-', rel))
    if not attendus:
        A('(aucun)')
    A('')
    if tout:
        A('== 3. SYNC (%d) ==' % len(sync))
        for h, rel in sorted(sync, key=lambda r: r[1].lower()):
            A('%-10s | 1 1 1 | aucune     | %s' % ('=' + h, rel))
        A('')
    A('== CONTROLE : 3 - 1 - 1 - 1 = 0 pour un fichier present partout ==')
    in3 = (V_PROD, V_TROIS, V_LOCAL, V_GITHUB, V_EOL, V_CASSE)
    coq = []
    if not lok:
        coq.append('statuts audit : somme differente du total')
    for v, hr, hl, hp, fich in rows:
        e = 3 - sum(1 for h in (hr, hl, hp) if h != '-')
        if (e == 0) != (v in in3):
            coq.append('ecart %d incoherent avec le verdict %s : %s' % (e, v, fich))
    for k in keys:
        e = 3 - sum(1 for lv in 'LPR' if keys[k][lv])
        if (e == 0) != all(keys[k][lv] for lv in 'LPR'):
            coq.append('presence incoherente : ' + k)
    if n_union != len(sync) + len(rows) + n_att:
        coq.append('chemins perdus : union %d, classes %d' % (n_union, len(sync) + len(rows) + n_att))
    n0 = len(sync) + sum(cnt[v] for v in in3)
    A('chemins : %d = SYNC %d + a traiter %d + attendus %d' % (n_union, len(sync), len(rows), n_att))
    A('ecart 0 (presents aux 3 niveaux) : %d ; ecart > 0 (en trop ou manquant) : %d' % (n0, n_union - n0))
    if coq:
        A('ERREURS DU SCRIPT (%d) :' % len(coq))
        for q in coq[:30]:
            A('  ' + q)
    else:
        A('controle du script : OK (aucun chemin perdu, ecarts coherents)')
    tot = sum(ndiff(r[0], r[1], r[2], r[3]) for r in rows)
    A('')
    A('ANOMALIES : ' + ('aucune' if not rows else 'x %d fichiers, %d diff au total' % (len(rows), tot)))
    A(ltxt)
    A('RESULTAT : %d chemins ; SYNC %d ; a traiter %d ; ecarts attendus %d ; erreurs du script %d' % (n_union, len(sync), len(rows), n_att, len(coq)))
    A('Duree : %.1f s' % (time.time() - t0))

    os.makedirs(OUT_DIR, exist_ok=True)
    dst = os.path.join(OUT_DIR, 'trigul_arbres_%s.txt' % today)
    if os.path.exists(dst):
        ts = datetime.datetime.now().strftime('%Y_%m_%d_%Hh%Mm%Ss')
        shutil.copy2(dst, dst[:-4] + '.bak_' + ts + '.txt')
    with open(dst, 'wb') as f:
        f.write(('\r\n'.join(out) + '\r\n').encode('utf-8'))
    print(out[-2])
    print('rapport : ' + dst)
    return 0


if __name__ == '__main__':
    sys.exit(main())