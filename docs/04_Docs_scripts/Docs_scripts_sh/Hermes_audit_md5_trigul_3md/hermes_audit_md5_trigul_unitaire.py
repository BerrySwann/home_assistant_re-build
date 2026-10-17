# -*- coding: utf-8 -*-
"""
hermes_audit_md5_trigul_unitaire.py - extraction et comparaison A L'UNITE de H:\\automations.yaml et H:\\scripts.yaml
contre les YAML locaux de ReBuild. Etape "profonde" du /trigul (voir CLAUDE.md).

Ce que fait le script (dans cet ordre) :
 1. copie H:\\automations.yaml dans docs\\03_docs_automations\\docs_automations_YAML\\AUTOMATIONS.YALM ORIGINAL\\automations.bak_AAAA_MM_JJ_HHhMMmSSs.yaml
    et H:\\scripts.yaml dans docs\\04_docs_scripts\\DOCS_SCRIPT_ORIGINAL\\scripts.bak_AAAA_MM_JJ_HHhMMmSSs.yaml (MD5 verifie)
 2. extrait chaque automation et chaque script dans ReBuild\\_tmp_trigul_profond\\ (un fichier par unite)
 3. compare chaque unite au YAML local (MD5 logique : YAML parse, cles triees, category/labels ignores,
    espaces de debut/fin ignores, commentaires et mise en forme ignores)
 4. ecrit le rapport historique\\MD5\\trigul_profond_AAAA-MM-JJ.txt (sauvegarde .bak_date_heure si le rapport du jour existe)
 5. efface le dossier temporaire _tmp_trigul_profond

Lecture seule sur H: et sur les YAML locaux. Ordre du trigul : local, prod, GitHub (GitHub : on n'aura qu'a push).
Lancer : python -I hermes_audit_md5_trigul_unitaire.py   (PYTHONIOENCODING=utf-8)
"""
import os, re, sys, json, hashlib, datetime, shutil
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE                                                          # ReBuild/ : on remonte jusqu'au dossier qui contient docs et historique
while not (os.path.isdir(os.path.join(ROOT, 'docs')) and os.path.isdir(os.path.join(ROOT, 'historique'))):
    if os.path.dirname(ROOT) == ROOT:
        raise SystemExit('racine ReBuild introuvable depuis ' + HERE)
    ROOT = os.path.dirname(ROOT)
PROD_AUTO = r'H:\automations.yaml'
PROD_SCR = r'H:\scripts.yaml'
Y_AUTO = os.path.join(ROOT, 'docs', '03_docs_automations', 'docs_automations_YAML')
Y_SCR = os.path.join(ROOT, 'docs', '04_docs_scripts', 'docs_scripts_YAML')
ORIG_AUTO = os.path.join(Y_AUTO, 'AUTOMATIONS.YALM ORIGINAL')
ORIG_SCR = os.path.join(ROOT, 'docs', '04_docs_scripts', 'DOCS_SCRIPT_ORIGINAL')
TMP = os.path.join(ROOT, '_tmp_trigul_profond')
OUTDIR = os.path.join(ROOT, 'historique', 'MD5')

NOW = datetime.datetime.now()
STAMP = NOW.strftime('%Y_%m_%d_%Hh%Mm%Ss')
DAY = NOW.strftime('%Y-%m-%d')


class Loader(yaml.SafeLoader):
    pass


Loader.add_multi_constructor('!', lambda l, s, n: None)


def load(path):
    with open(path, encoding='utf-8-sig') as f:
        return yaml.load(f, Loader)


def norm(o):
    if isinstance(o, dict):
        return {k: norm(v) for k, v in o.items() if k not in ('category', 'labels')}
    if isinstance(o, list):
        return [norm(x) for x in o]
    if isinstance(o, str):
        return o.strip()
    return o


def hl(o):
    return hashlib.md5(json.dumps(norm(o), sort_keys=True, ensure_ascii=False).encode('utf-8')).hexdigest()[:8].upper()


def hf(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()[:8].upper()


def is_save(name):
    return '.bak_' in name or re.search(r'_\d{4}-\d{2}-\d{2}(_\d+h\d+)?\.ya?ml$', name) is not None


def safe(name):
    return re.sub(r'[^A-Za-z0-9_.-]', '_', str(name))


def snapshot(src, dst_dir, base):
    os.makedirs(dst_dir, exist_ok=True)
    dst = os.path.join(dst_dir, '%s.bak_%s.yaml' % (base, STAMP))
    if os.path.exists(dst):
        return dst, 'COLLISION (copie non faite)'
    shutil.copy2(src, dst)
    return dst, 'identique' if hf(src) == hf(dst) else 'DIFFERENT'


def local_files(root, skip_dirs):
    out = []
    for r, ds, fs in os.walk(root):
        ds[:] = [d for d in ds if d not in skip_dirs]
        for f in fs:
            if f.lower().endswith(('.yaml', '.yml')) and not is_save(f):
                out.append(os.path.join(r, f))
    return out


def main():
    t0 = datetime.datetime.now()
    for p in (PROD_AUTO, PROD_SCR):
        if not os.path.exists(p):
            print('H: introuvable ou fichier absent :', p)
            sys.exit(2)

    # 1. copies datees
    ca, sa = snapshot(PROD_AUTO, ORIG_AUTO, 'automations')
    cs, ss = snapshot(PROD_SCR, ORIG_SCR, 'scripts')

    # 2. extraction dans le temporaire
    if os.path.isdir(TMP):
        shutil.rmtree(TMP)
    os.makedirs(os.path.join(TMP, 'automations'))
    os.makedirs(os.path.join(TMP, 'scripts'))
    prod_a = load(PROD_AUTO)
    prod_s = load(PROD_SCR)
    for a in prod_a:
        with open(os.path.join(TMP, 'automations', safe(a.get('id')) + '.yaml'), 'w', encoding='utf-8') as f:
            yaml.safe_dump(a, f, allow_unicode=True, sort_keys=False)
    for k, v in prod_s.items():
        with open(os.path.join(TMP, 'scripts', safe(k) + '.yaml'), 'w', encoding='utf-8') as f:
            yaml.safe_dump({k: v}, f, allow_unicode=True, sort_keys=False)
    n_ext = len(os.listdir(os.path.join(TMP, 'automations'))) + len(os.listdir(os.path.join(TMP, 'scripts')))

    # 3a. automations : par id, sinon par alias sans lettre de tete
    loc = []
    for p in local_files(Y_AUTO, {'AUTOMATIONS.YALM ORIGINAL', 'RASPI'}):
        d = load(p)
        d = d[0] if isinstance(d, list) and d else d
        if isinstance(d, dict) and 'alias' in d:
            loc.append((p, d))
    byid = {str(d.get('id')): (p, d) for p, d in loc if d.get('id')}
    strip = lambda s: re.sub(r'^[A-Za-z]\s+-\s+', '', str(s)).strip().lower()
    bynoid = {strip(d['alias']): (p, d) for p, d in loc if not d.get('id')}
    res_a = []
    used = set()
    ok_a = 0
    for a in prod_a:
        i = str(a.get('id'))
        m = byid.get(i)
        how = 'id'
        if not m:
            m = bynoid.get(strip(a.get('alias')))
            how = 'alias'
        if not m:
            res_a.append(('ABSENT_LOCAL', i, str(a.get('alias')), '', hl(a), ''))
            continue
        p, d = m
        used.add(p)
        if how == 'alias':
            b = dict(a)
            b.pop('id', None)
            b['alias'] = d['alias']
            st = 'IDENTIQUE_HORS_ID_ALIAS' if hl(b) == hl(d) else 'DIFFERENT'
        else:
            st = 'IDENTIQUE' if hl(a) == hl(d) else 'DIFFERENT'
        if st == 'IDENTIQUE':
            ok_a += 1
        res_a.append((st, i, str(a.get('alias')), os.path.relpath(p, Y_AUTO), hl(a), hl(d)))
    extra_a = [os.path.relpath(p, Y_AUTO) for p, d in loc if p not in used]

    # 3b. scripts : le YAML local est un dict {nom: corps} ou le corps seul (nom du fichier = nom du script)
    locs = {}
    for p in local_files(Y_SCR, {'DOCS_SCRIPT_ORIGINAL'}):
        try:
            d = load(p)
        except Exception as e:
            locs[os.path.splitext(os.path.basename(p))[0]] = (p, None)
            continue
        if isinstance(d, dict) and len(d) == 1 and isinstance(list(d.values())[0], dict) and 'sequence' in list(d.values())[0]:
            locs[list(d.keys())[0]] = (p, list(d.values())[0])
        elif isinstance(d, dict) and 'sequence' in d:
            locs[os.path.splitext(os.path.basename(p))[0]] = (p, d)
    res_s = []
    ok_s = 0
    used_s = set()
    for k, v in prod_s.items():
        m = locs.get(k)
        if not m or m[1] is None:
            res_s.append(('ABSENT_LOCAL', k, '', hl(v), ''))
            continue
        used_s.add(k)
        same = hl(v) == hl(m[1])
        if same:
            ok_s += 1
        res_s.append(('IDENTIQUE' if same else 'DIFFERENT', k, os.path.relpath(m[0], Y_SCR), hl(v), hl(m[1])))
    extra_s = [os.path.relpath(m[0], Y_SCR) for k, m in locs.items() if k not in used_s]

    # 4. rapport
    dur = (datetime.datetime.now() - t0).total_seconds()
    head = [
        'TRIGUL PROFOND - %s' % NOW.strftime('%Y-%m-%d %H:%M:%S'),
        'Copie automations.yaml : %s (%s)' % (os.path.relpath(ca, ROOT), sa),
        'Copie scripts.yaml : %s (%s)' % (os.path.relpath(cs, ROOT), ss),
        'Prod : automations.yaml MD5 fichier %s, %d automations ; scripts.yaml MD5 fichier %s, %d scripts ; %d unites extraites' % (hf(PROD_AUTO), len(prod_a), hf(PROD_SCR), len(prod_s), n_ext),
        'MD5 logique = empreinte du YAML parse (cles triees, category/labels ignores, espaces de debut/fin ignores, commentaires et mise en forme ignores).',
        'AUTOMATIONS : %d identiques sur %d. Exports locaux sans automation prod : %s' % (ok_a, len(prod_a), ', '.join(extra_a) or 'aucun'),
        'SCRIPTS : %d identiques sur %d. YAML locaux sans script prod : %s' % (ok_s, len(prod_s), ', '.join(extra_s) or 'aucun'),
        'Duree du traitement : %.1f s' % dur,
        ''
    ]
    body = ['[AUTOMATIONS] statut | id | prod | local | fichier local | alias']
    for st, i, al, rel, hp, hlc in sorted(res_a, key=lambda x: (x[0], x[1])):
        body.append('%-24s | %-14s | prod=%s local=%s | %s | %s' % (st, i, hp, hlc or '-', rel or '-', al[:60]))
    body.append('')
    body.append('[SCRIPTS] statut | nom | prod | local | fichier local')
    for st, k, rel, hp, hlc in sorted(res_s, key=lambda x: (x[0], x[1])):
        body.append('%-24s | %-34s | prod=%s local=%s | %s' % (st, k, hp, hlc or '-', rel or '-'))
    os.makedirs(OUTDIR, exist_ok=True)
    out = os.path.join(OUTDIR, 'trigul_profond_%s.txt' % DAY)
    if os.path.exists(out):
        shutil.copy2(out, os.path.join(OUTDIR, 'trigul_profond_%s.bak_%s.txt' % (DAY, STAMP)))
    with open(out, 'w', encoding='utf-8', newline='\r\n') as f:
        f.write('\n'.join(head + body) + '\n')

    # 5. effacer le temporaire (garde-fou : uniquement le dossier attendu)
    if os.path.basename(TMP) == '_tmp_trigul_profond' and os.path.dirname(TMP) == ROOT:
        shutil.rmtree(TMP)

    print('\n'.join(head))
    for l in body:
        if not l.startswith('IDENTIQUE '):
            print(l)
    print('rapport :', out, hf(out))


if __name__ == '__main__':
    main()