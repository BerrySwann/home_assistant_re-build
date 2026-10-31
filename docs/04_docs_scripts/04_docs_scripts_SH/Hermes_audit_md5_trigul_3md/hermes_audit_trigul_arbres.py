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
Le script ne modifie, ne pousse et ne supprime rien. Il n'ecrit que son rapport dans historique/03_RAPPORTS/06_MD5/00_VERIF_FINAL_TRIGUL_ARBRES (repertoire numerote, decide par Eric le 2026-10-18).
"""
import os, sys, json, hashlib, collections, datetime, shutil, time, urllib.request
import html as _html

LOCAL = r'C:\Users\Berry Swann\Documents\ReBuild\docs'
PROD = r'H:\docs'
LOCAL_README = r'C:\Users\Berry Swann\Documents\ReBuild\docs\01_docs_config_system\01_config_system_MD\README\README.md'
PROD_README = r'H:\README.md'
REPO = 'BerrySwann/home_assistant_re-build'
OUT_DIR = r'C:\Users\Berry Swann\Documents\ReBuild\historique\03_RAPPORTS\06_MD5\00_VERIF_FINAL_TRIGUL_ARBRES'
ROOT = '(racine)/README.md'

# Ecarts ATTENDUS (a part, avec la raison). Tout le reste est signale comme anomalie.
GITIGNORE_EXT = {'.txt', '.png', '.jpg', '.jpeg', '.gif', '.webp', '.ico', '.pyc'}
EXCEPTIONS_TXT = [

    "fichiers .txt .png .jpg .jpeg .gif .webp .ico .pyc presents en local + prod mais absents de GitHub : ignores par le .gitignore du depot (sauf les .txt de notifs/, versionnes depuis le 2026-10-18)",
    "fichiers verrou d editeur #...# presents en prod seule : ignores par le .gitignore, jamais sur GitHub (decide par Eric le 2026-10-18)",
    "dossiers XX_ (local seul voulu par Eric, decide le 2026-10-25) : jamais en prod, jamais sur GitHub ; comptes a part dans la ligne LOCAL SEUL VOULU, jamais en anomalie",
    "dossier modifs/ (journaux des agents) : ignore aux 3 niveaux, comme l audit MD5 docs cote HA",
]

EXCLUS_TXT = [
    "caches Python : fichiers .pyc et dossiers __pycache__ (regenerables)",
    "exports Dashboard_COMPLET plus anciens que le plus recent (Dashboard_AAAA_MM_JJ.yaml) : seul le plus recent est controle",
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
    if origin == 'L' and any(c.startswith('xx_') or c == '99_docs_md_system' for c in low.split('/')):
        return 'LOCAL SEUL VOULU (dossier XX_)'
    if origin == 'L' and '_archive_' in name:
        return 'archive locale'
    if (origin == 'L' and '/dashboard_complet/' in '/' + low and name.startswith('dashboard_')
            and name.endswith('.yaml') and name != DASH_LATEST):
        return 'ancien export Dashboard (seul le plus recent est controle)'
    if origin == 'LP' and '/notifs/' in '/' + low and name.endswith('.txt'):
        return None
    if origin == 'LP' and os.path.splitext(name)[1] in GITIGNORE_EXT:
        return 'type ignore par le .gitignore du depot'
    if origin == 'P' and len(name) > 2 and name.startswith('#') and name.endswith('#'):
        return 'fichier verrou d editeur (prod seule, ignore par le .gitignore)'
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
    n = {'md': 0, 'yaml': 0, 'sh': 0, 'py': 0, 'svg': 0, 'autres': 0}
    for k in keys:
        e = os.path.splitext(k)[1].lower()
        if e == '.md':
            n['md'] += 1
        elif e in ('.yaml', '.yml'):
            n['yaml'] += 1
        elif e == '.sh':
            n['sh'] += 1
        elif e == '.py':
            n['py'] += 1
        elif e == '.svg':
            n['svg'] += 1
        else:
            n['autres'] += 1
    return n


def ligne_res(nom, keys):
    n = par_ext(keys)
    return 'RESULTAT %-7s : %d fichiers (%d .md, %d .yaml, %d .sh, %d .py, %d .svg, %d autres)' % (nom, len(keys), n['md'], n['yaml'], n['sh'], n['py'], n['svg'], n['autres'])


def ligne_audit(aud):
    a = [(p, c) for p, c in aud if os.path.splitext(p)[1].lower() in ('.md', '.yaml', '.yml', '.sh', '.py', '.svg')]
    n = par_ext([p for p, c in a])
    k = collections.Counter(c for p, c in a)
    txt = ('RESULTAT AUDIT : %d fichiers (%d .md - %d .yaml - %d .sh - %d .py - %d .svg) - SYNC %d - fin de ligne seule %d - DIFF %d - CASSE %d'
           ' - ABSENT GITHUB %d - ABSENT PROD %d - ABSENT LOCAL %d - ABSENT 2 NIVEAUX %d') % (
        len(a), n['md'], n['yaml'], n['sh'], n['py'], n['svg'], k['SYNC'], k['EOL'], k['DIFF'], k['CASSE'],
        k['ABS_R'], k['ABS_P'], k['ABS_L'], k['ABS2'])
    ok = sum(k.values()) == len(a)
    return txt, ok


def ecrire_html(dst, ctx):
    e = _html.escape
    cls = {'OK': 'ok', 'DIFF': 'diff', 'EOL': 'eol', 'ABS': 'abs', '-': 'na'}
    sym = {'OK': '&#9989;', 'DIFF': '&#10060;', 'EOL': '&#9888;&#65039;', 'ABS': '&#128683;', '-': '-'}
    names = {'L': 'local', 'P': 'prod', 'R': 'GitHub'}

    def badge(st):
        return '<td class="b %s">%s</td>' % (cls[st], sym[st])

    def detail(r):
        v, pres = r['v'], r['pres']
        if r['kind'] == 'ATTENDU':
            return 'ecart attendu : ' + r['why'] + ((' ; ' + r['det']) if r.get('det') else '')
        if v is None:
            return ''
        if v == 'SYNC':
            return ''
        if v == V_LOCAL:
            return 'retard : prod et GitHub (local en avance, a pousser)'
        if v == V_GITHUB:
            return 'retard : GitHub (attend le backup HA)'
        if v == V_PROD:
            return 'prod seule differente (suspect)'
        if v == V_TROIS:
            return '3 contenus differents (a voir a la main)'
        if v == V_EOL:
            return 'fin de ligne seule (CRLF/LF), sans action'
        if v == V_CASSE:
            return 'casse differente entre niveaux'
        ab = [names[lv] for lv in 'LPR' if lv not in pres]
        t = 'absent : ' + ' + '.join(ab)
        t += {'PR': ' (ancien nom ?)', 'LP': ' (attend le backup HA)', 'L': ' (jamais pousse en prod)'}.get(pres, '')
        if r.get('det'):
            t += ' ; ' + r['det']
        return t

    def shown(r):
        if r['v'] == V_CASSE:
            return r['rel']
        return 'README.md' if r['rel'] == ROOT else 'docs/' + r['rel']

    def ligne(r):
        a, b, c = r['st']
        cl = {'SYNC': 'r-ok', 'ATTENDU': 'r-att'}.get(r['kind'], 'r-an')
        return '<tr class="%s">%s%s%s<td>%s</td><td class="f">%s</td></tr>' % (cl, badge(a), badge(b), badge(c), e(detail(r)), e(shown(r)))

    thead = '<thead><tr><th>L&harr;P</th><th>P&harr;R</th><th>L&harr;R</th><th>D&Eacute;TAIL</th><th>FICHIER</th></tr></thead>'
    trait = [r for r in ctx['hrows'] if r['kind'] == 'TRAITER']
    allr = sorted(ctx['hrows'], key=lambda r: shown(r).lower())
    css = (':root{--bg:#fff;--fg:#1c2330;--mut:#5b6575;--card:#f4f6f9;--line:#d9dee6;--ok:#1e7a3c;--okb:#dff3e5;'
           '--diff:#b3261e;--diffb:#fbe0de;--eol:#8a5a00;--eolb:#fdf0d0;--abs:#a33a00;--absb:#ffe6d6;--na:#6b7280;--nab:#eceff3}'
           '@media (prefers-color-scheme:dark){:root{--bg:#14181f;--fg:#e6eaf0;--mut:#9aa5b5;--card:#1d232d;--line:#2d3644;'
           '--ok:#7fd69a;--okb:#17331f;--diff:#ff9d95;--diffb:#3d1a18;--eol:#f0c36a;--eolb:#3a2e0e;--abs:#ffb184;--absb:#3d2414;--na:#9aa5b5;--nab:#242b36}}'
           'body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,Segoe UI,Arial,sans-serif}'
           'main{max-width:1250px;margin:0 auto;padding:20px 16px 48px}'
           'h1{font-size:22px;margin:0 0 4px}h2{font-size:17px;margin:28px 0 8px}'
           '.mut{color:var(--mut);font-size:13px}'
           '.ban{padding:12px 16px;border-radius:8px;font-weight:600;margin:14px 0}'
           '.ban.ok{background:var(--okb);color:var(--ok)}.ban.warn{background:var(--eolb);color:var(--eol)}.ban.ko{background:var(--diffb);color:var(--diff)}'
           '.cards{display:flex;flex-wrap:wrap;gap:10px;margin:10px 0}'
           '.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px 14px;min-width:120px}'
           '.card b{display:block;font-size:24px}.card span{font-size:12px;color:var(--mut)}'
           'table{border-collapse:collapse;width:100%;font-size:13px}'
           'th,td{border-bottom:1px solid var(--line);padding:4px 8px;text-align:left;vertical-align:top}'
           'th{position:sticky;top:0;background:var(--card);z-index:1}'
           'td.b{text-align:center;width:58px}'
           'tr.r-an td.b.ok,tr.r-att td.b.ok{background:var(--okb)}'
           'tr.r-an td.b.diff{background:var(--diffb)}tr.r-an td.b.eol{background:var(--eolb)}tr.r-an td.b.abs{background:var(--absb)}'
           'tr.r-att td.b.abs{background:var(--nab)}tr.r-att td.b.diff{background:var(--nab)}'
           'tr.r-an td.f{font-weight:700}tr.r-att{color:var(--mut)}'
           'td{white-space:nowrap}td.f{font-family:ui-monospace,Consolas,monospace}'
           '.sc{overflow:auto;max-height:78vh;border:1px solid var(--line);border-radius:8px}'
           'tr.grp td{background:var(--card);font-weight:700;padding-top:10px}'
           'pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:10px;overflow:auto;font-size:12px}'
           '#flt{width:100%;box-sizing:border-box;padding:8px 10px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg);margin:8px 0}'
           'label{font-size:13px}'
           '.leg span{display:inline-block;margin:2px 14px 2px 0}')
    d = ['<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>Trigul arbres ' + ctx['date'] + '</title><style>' + css + '</style></head><body><main>']
    d.append('<h1>Trigul - superposition des 3 arbres</h1>')
    d.append('<div class="mut">%s - lecture seule, rien n est modifie, pousse ni supprime</div>' % e(ctx['ts']))
    d.append('<div class="mut">GitHub : %s, commit %s du %s - %s</div>' % (e(REPO), e(ctx['csha']), e(ctx['cdate']), e(ctx['cmsg'])))
    d.append('<div class="mut">Exclus du trigul (ni compares ni comptes) : %d chemins - %s</div>' % (ctx['n_excl'], e(' ; '.join(ctx['excl_txt']))))
    n = len(trait)
    if ctx['n_err']:
        d.append('<div class="ban ko">ERREURS DU SCRIPT : %d (voir le rapport .txt)</div>' % ctx['n_err'])
    elif n == 0:
        d.append('<div class="ban ok">Tout est synchronise : aucune anomalie</div>')
    else:
        d.append('<div class="ban warn">%d fichier(s) a traiter, %d diff au total</div>' % (n, ctx['tot']))
    d.append('<div class="cards">')
    for lab, val in (('chemins (union)', ctx['n_union']), ('SYNC', ctx['n_sync']), ('a traiter', n),
                     ('ecarts attendus', ctx['n_att']), ('erreurs du script', ctx['n_err'])):
        d.append('<div class="card"><b>%d</b><span>%s</span></div>' % (val, e(lab)))
    d.append('</div>')
    d.append('<pre>%s</pre>' % e(ctx['ltxt']))
    d.append('<pre>%s</pre>' % e('\n'.join(ctx['niveaux'])))
    d.append('<h2>A traiter</h2>')
    if trait:
        d.append('<div class="sc"><table>' + thead + '<tbody>')
        for v in ORDRE:
            grp = sorted([r for r in trait if r['v'] == v], key=lambda r: r['rel'].lower())
            if not grp:
                continue
            d.append('<tr class="grp"><td colspan="5">%s (%d)</td></tr>' % (e(v), len(grp)))
            for r in grp:
                d.append(ligne(r))
        d.append('</tbody></table></div>')
    else:
        d.append('<p>Rien a traiter.</p>')
    d.append('<h2>&#9472;&#9472; COMPARAISON PAR PAIRES (1er coup d&rsquo;&oelig;il) &#9472;&#9472; %d fichiers</h2>' % len(allr))
    d.append('<label><input type="checkbox" id="onlyan"> anomalies et &eacute;carts attendus seulement</label>')
    d.append('<input id="flt" type="search" placeholder="Filtrer (nom de fichier, d&eacute;tail...)">')
    d.append('<div class="sc"><table id="full">' + thead + '<tbody>')
    for r in allr:
        d.append(ligne(r))
    d.append('</tbody></table></div>')
    d.append('<h2>Legende</h2><div class="leg">'
             '<span>L = local (ReBuild, source de verite)</span><span>P = prod (H:)</span><span>R = GitHub</span><br>'
             '<span>' + sym['OK'] + ' meme contenu</span>'
             '<span>' + sym['DIFF'] + ' contenu different</span>'
             '<span>' + sym['EOL'] + ' meme contenu, fins de ligne differentes (CRLF/LF), sans action</span>'
             '<span>' + sym['ABS'] + ' absent d un des deux niveaux</span>'
             '<span>- absent des deux niveaux</span></div>')
    d.append('<script>function ap(){var q=document.getElementById("flt").value.toLowerCase();var oa=document.getElementById("onlyan").checked;'
             'document.querySelectorAll("#full tbody tr").forEach(function(tr){var nm=tr.textContent.toLowerCase().indexOf(q)<0;'
             'var h=oa&&tr.classList.contains("r-ok");tr.style.display=(nm||h)?"none":""})}'
             'document.getElementById("flt").addEventListener("input",ap);document.getElementById("onlyan").addEventListener("change",ap)</script>')
    d.append('</main></body></html>')
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(d) + '\n')

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
    L = {k: v for k, v in L.items() if not k.lower().startswith('modifs/') and '_archive_' not in k.lower().rsplit('/', 1)[-1]}
    P = {k: v for k, v in P.items() if not k.lower().startswith('modifs/') and '_archive_' not in k.lower().rsplit('/', 1)[-1]}
    R = {k: v for k, v in R.items() if not k.lower().startswith('modifs/') and '_archive_' not in k.lower().rsplit('/', 1)[-1]}
    cands = sorted(k.lower().rsplit('/', 1)[-1] for k in L
                   if '/dashboard_complet/' in '/' + k.lower()
                   and k.lower().rsplit('/', 1)[-1].startswith('dashboard_')
                   and k.lower().endswith('.yaml'))
    globals()['DASH_LATEST'] = cands[-1] if cands else ''
    def exclu(k):
        low = k.lower()
        name = low.rsplit('/', 1)[-1]
        if name.endswith('.pyc') or '/__pycache__/' in '/' + low:
            return True
        return ('/dashboard_complet/' in '/' + low and name.startswith('dashboard_')
                and name.endswith('.yaml') and name != DASH_LATEST)
    n_excl = len({k.lower() for d in (L, P, R) for k in d if exclu(k)})
    L = {k: v for k, v in L.items() if not exclu(k)}
    P = {k: v for k, v in P.items() if not exclu(k)}
    R = {k: v for k, v in R.items() if not exclu(k)}
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

    def ps3(kv):
        nm = {lv: sorted(kv[lv])[0] for lv in 'LPR' if kv[lv]}

        def ps(a, b):
            if a in nm and b in nm:
                return pair(hs(a, nm[a]), hs(b, nm[b]))
            if a in nm or b in nm:
                return 'ABS'
            return '-'
        return (ps('L', 'P'), ps('P', 'R'), ps('L', 'R'))

    rows = []
    hrows = []
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
                hrows.append(dict(kind='TRAITER', v=V_CASSE, pres='LPR', st=ps3(kv), rel=nom))
                aud.append((sorted(kv['L'])[0], 'CASSE'))
                continue
            rel = next(iter(names))
            hL, hP, hR = hs('L', rel), hs('P', rel), hs('R', rel)
            v = verdict_trois(pair(hL, hP), pair(hP, hR), pair(hL, hR))
            hrows.append(dict(kind=('SYNC' if v == 'SYNC' else 'TRAITER'), v=v, pres='LPR', st=ps3(kv), rel=rel))
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
                hrows.append(dict(kind='ATTENDU', v=None, pres=present, st=ps3(kv), rel=rel, why=why, det='; '.join(detail)))
        else:
            ce = cells(kv)
            fich = rel + (('   [' + '; '.join(detail) + ']') if detail else '')
            rows.append((V_PRES[present], ce['R'], ce['L'], ce['P'], fich))
            hrows.append(dict(kind='TRAITER', v=V_PRES[present], pres=present, st=ps3(kv), rel=rel, det='; '.join(detail)))
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
    A('EXCLUS DU TRIGUL (ni compares ni comptes) : %d chemins' % n_excl)
    for x in EXCLUS_TXT:
        A('  - ' + x)
    A('')
    ltxt, lok = ligne_audit(aud)
    A('== AUDIT (perimetre de l audit MD5 docs cote HA : .md .yaml .sh, plus .py et .svg ajoutes le 2026-10-18 a la demande d Eric ; sur les 3 niveaux, hors modifs/) ==')
    A(ltxt)
    A('')
    A('== COMPTES PAR NIVEAU (perimetre docs/ + README racine, hors .bak, archives et modifs/) ==')
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
    n_xx = sum(1 for a_ in attendus if a_[1].startswith('LOCAL SEUL VOULU'))
    A('LOCAL SEUL VOULU (XX_)           : %d fichiers (dossiers XX_, jamais en prod ni sur GitHub, inclus dans les ecarts attendus)' % n_xx)
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
    dsth = os.path.join(OUT_DIR, 'trigul_arbres_%s.html' % today)
    if os.path.exists(dsth):
        ts2 = datetime.datetime.now().strftime('%Y_%m_%d_%Hh%Mm%Ss')
        shutil.copy2(dsth, dsth[:-5] + '.bak_' + ts2 + '.html')
    ecrire_html(dsth, dict(date=today, ts=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), csha=csha[:7], cdate=cdate, cmsg=cmsg,
                           hrows=hrows, attendus=attendus, n_union=n_union, n_sync=len(sync), n_att=n_att, n_err=len(coq), tot=tot,
                           ltxt=ltxt, n_excl=n_excl, excl_txt=EXCLUS_TXT, niveaux=[ligne_res('GitHub', list(R.keys())), ligne_res('local', list(L.keys())), ligne_res('prod', list(P.keys())), ligne_res('union', list(keys))]))
    print('rapport html : ' + dsth)
    return 0


if __name__ == '__main__':
    sys.exit(main())