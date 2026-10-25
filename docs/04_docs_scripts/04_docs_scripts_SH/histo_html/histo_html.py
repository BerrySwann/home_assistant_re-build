#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pages HTML sombres des journaux de bord histo (cree le 2026-10-21 a la demande d'Eric).

But : une page HTML par jour (toutes les sessions du jour dedans), a partir des journaux
histo_AAAA-MM-JJ[_sN].md et .txt. Les originaux .md et .txt ne sont JAMAIS modifies ni deplaces.

Dossiers : sources lues dans historique/ (racine) et dans le dossier historique/02_* (premier dossier dont
le nom commence par 02_) ; pages ecrites dans ce dossier 02_*. Variable HISTO_HTML_DIR : remplace historique/
(essais seulement).

Usage :
  python -I histo_html.py                 page du jour (date du PC)
  python -I histo_html.py AAAA-MM-JJ      page d'un jour
  python -I histo_html.py tout            toutes les pages (jours et journaux fusionnes)
  python -I histo_html.py fusionne        toutes les pages des journaux fusionnes (sous-dossier Fusion* du dossier 02_*)
Sans argument : page du jour + page du journal fusionne le plus recent.
Journaux fusionnes : JOURNAL_FUSIONNE_*.md et JOURNAL_COMPLET_*.md (sans .bak) donnent une page du meme nom en .html,
a cote, avec sommaire ; memes regles de sauvegarde et de collision que les pages de jours.
Dans tous les cas index.html est refait (liste des pages presentes, un par dossier).

Regles (decidees par Eric le 2026-10-21) :
- une page par jour : histo_AAAA-MM-JJ.html, gardee sans limite de jours ;
- si la page existe avec un contenu different, elle est d'abord copiee en
  histo_AAAA-MM-JJ.bak_AAAA_MM_JJ_HHhMMmSSs.html (10 au plus le meme jour, menage fait par /histo) ;
  page identique : rien n'est ecrit ;
- une page existante qui n'a pas ete generee par ce script (pas de balise generator) n'est jamais
  ecrasee : elle est signalee (COLLISION) et ignoree ;
- un .md et un .txt de meme jour et meme session : le .md est pris, le .txt est signale ;
- les fichiers .bak, .html et les journaux fusionnes ne sont pas lus.
Contenu deterministe (pas d'heure de generation) pour que 'identique' soit fiable. Aucun secret lu ou ecrit.
"""
import datetime
import html as _html
import os
import re
import shutil
import sys

ROOT = r'C:\Users\Berry Swann\Documents\ReBuild'
HIST = os.environ.get('HISTO_HTML_DIR') or os.path.join(ROOT, 'historique')
GEN = '<meta name="generator" content="histo_html.py">'
NOM = re.compile(r'^histo_(\d{4}-\d{2}-\d{2})(?:_[sS](\d+))?\.(md|txt)$')

CSS = """body{font-family:system-ui,Arial,sans-serif;margin:0 auto;padding:20px 16px;max-width:1000px;background:#12181b;color:#e4eaed;font-size:15px;line-height:1.55}
h1{margin:0 0 4px}h2{margin:34px 0 6px;border-bottom:1px solid #2c383d;padding-bottom:4px}h3{margin:18px 0 4px}h4{margin:16px 0 4px;color:#4fb8c9}
p{margin:6px 0}.mut,.src{color:#93a3ab;font-size:.85rem}a{color:#4fb8c9}hr{border:0;border-top:1px solid #2c383d;margin:14px 0}
pre{background:#1a2226;border:1px solid #2c383d;border-radius:4px;padding:10px 12px;white-space:pre-wrap;word-break:break-word;font:13px/1.5 ui-monospace,Consolas,monospace;margin:6px 0}
code{background:#1a2226;border:1px solid #2c383d;border-radius:3px;padding:0 4px;font:13px ui-monospace,Consolas,monospace}
ul{margin:4px 0 4px 20px;padding:0}li{margin:2px 0}nav{margin:10px 0}nav a{margin-right:12px}
table{border-collapse:collapse;width:100%;background:#1a2226;border:1px solid #2c383d}th,td{padding:6px 8px;border-bottom:1px solid #2c383d;text-align:left}th{color:#93a3ab;font-weight:500;font-size:.8rem}"""


def esc(t):
    return _html.escape(t, quote=False)


def tete(titre):
    return ('<!doctype html><html lang="fr"><head><meta charset="utf-8">' + GEN +
            '<meta name="viewport" content="width=device-width,initial-scale=1"><title>%s</title><style>%s</style></head><body>\n'
            % (_html.escape(titre), CSS))


def inline(t):
    t = esc(t)
    t = re.sub(r'`([^`]+)`', r'<code>\1</code>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'(?<![\*\w])\*([^*\s][^*]*?)\*(?![\*\w])', r'<em>\1</em>', t)
    return t


def rend_txt(lignes):
    out, pre = [], []

    def vide():
        if pre:
            out.append('<pre>' + esc('\n'.join(pre)) + '</pre>')
            del pre[:]

    for l in lignes:
        m = re.match(r'^=== (.+?) ===\s*$', l)
        if m:
            vide()
            out.append('<h3>%s</h3>' % esc(m.group(1)))
            continue
        m = re.match(r'^-- (.+?) --\s*$', l)
        if m:
            vide()
            out.append('<h4>%s</h4>' % esc(m.group(1)))
            continue
        pre.append(l)
    vide()
    return '\n'.join(out)


def rend_table(rows):
    cells = []
    for r in rows:
        c = [x.strip() for x in r.strip().strip('|').split('|')]
        if all(re.match(r'^:?-{2,}:?$', x) for x in c if x):
            continue
        cells.append(c)
    if not cells:
        return ''
    h = '<table><tr>' + ''.join('<th>%s</th>' % inline(x) for x in cells[0]) + '</tr>'
    for c in cells[1:]:
        h += '<tr>' + ''.join('<td>%s</td>' % inline(x) for x in c) + '</tr>'
    return h + '</table>'


def rend_md(texte, toc=None):
    lignes = texte.splitlines()
    # ancien format : tout le journal est dans un bloc ```text
    if toc is None and lignes and lignes[0].strip().startswith('```'):
        fin = len(lignes)
        while fin > 1 and not lignes[fin - 1].strip():
            fin -= 1
        if lignes[fin - 1].strip() == '```':
            fin -= 1
        return rend_txt(lignes[1:fin])
    out, liste, code, buf, para, tab = [], False, False, [], [], []

    def f_para():
        if para:
            out.append('<p>' + inline(' '.join(para)) + '</p>')
            del para[:]

    def f_liste():
        nonlocal liste
        if liste:
            out.append('</ul>')
            liste = False

    for l in lignes:
        if l.strip().startswith('```'):
            if code:
                out.append('<pre>' + esc('\n'.join(buf)) + '</pre>')
                buf, code = [], False
            else:
                f_para()
                f_liste()
                code = True
            continue
        if code:
            buf.append(l)
            continue
        if re.match(r'^\s*\|.*\|\s*$', l):
            f_para()
            f_liste()
            tab.append(l)
            continue
        if tab:
            out.append(rend_table(tab))
            tab = []
        m = re.match(r'^(#{1,6})\s+(.*)$', l)
        if m:
            f_para()
            f_liste()
            n = min(len(m.group(1)) + 2, 6)
            ident = ''
            if toc is not None and len(m.group(1)) <= 3:
                ident = ' id="h%d"' % len(toc)
                toc.append((len(m.group(1)), re.sub(r'[*`]', '', m.group(2)), 'h%d' % len(toc)))
            out.append('<h%d%s>%s</h%d>' % (n, ident, inline(m.group(2)), n))
            continue
        if re.match(r'^\s*-{3,}\s*$', l):
            f_para()
            f_liste()
            out.append('<hr>')
            continue
        m = re.match(r'^\s*[-*]\s+(.*)$', l)
        if m:
            f_para()
            if not liste:
                out.append('<ul>')
                liste = True
            out.append('<li>' + inline(m.group(1)) + '</li>')
            continue
        if not l.strip():
            f_para()
            f_liste()
            continue
        f_liste()
        para.append(l.strip())
    if code:
        out.append('<pre>' + esc('\n'.join(buf)) + '</pre>')
    if tab:
        out.append(rend_table(tab))
    f_para()
    f_liste()
    return '\n'.join(out)


def rendre_fusionne(nom, chemin):
    toc = []
    corps = rend_md(lire(chemin), toc)
    sommaire = ''.join('<li%s><a href="#%s">%s</a></li>' % (' style="margin-left:18px"' if n > 2 else '', i, esc(t))
                       for n, t, i in toc)
    return (tete('Journal fusionne ' + nom) + '<h1>%s</h1><p class="src">Source : %s.md</p>\n'
            '<nav><a href="index.html">Liste</a></nav>\n<h2>Sommaire</h2><ul>%s</ul>\n%s\n</body></html>\n'
            % (esc(nom), esc(nom), sommaire, corps))


FUS = re.compile(r'^(JOURNAL_(?:FUSIONNE|COMPLET)_[0-9_-]+)\.md$')


def dossier_fusionne(sorties):
    for n in sorted(os.listdir(sorties)):
        if n.upper().startswith('FUSION') and os.path.isdir(os.path.join(sorties, n)):
            return os.path.join(sorties, n)
    return None


def index_dossier(d, motif):
    lignes = ''
    for n in sorted(os.listdir(d), reverse=True):
        m = motif.match(n)
        if not m:
            continue
        with open(os.path.join(d, n), 'rb') as f:
            t = f.read().decode('utf-8', 'replace')
        if GEN in t:
            info = '%d session(s)' % t.count('<section') if '<section' in t else 'journal fusionne'
        else:
            info = 'page d origine, non generee'
        lignes += '<tr><td><a href="%s">%s</a></td><td>%s</td></tr>\n' % (n, n[:-5], info)
    return (tete('Index') + '<h1>Index</h1>\n<table><tr><th>Page</th><th>Contenu</th></tr>\n' + lignes +
            '</table></body></html>\n')


def dossier_pages():
    """Dossier de sortie : premier dossier 02_* de historique/ (cree par Eric le 2026-10-21)."""
    for n in sorted(os.listdir(HIST)):
        if n.startswith('02_') and os.path.isdir(os.path.join(HIST, n)):
            return os.path.join(HIST, n)
    return None


def collecter(sorties):
    """{jour: {session(int, 0 = sans numero): (chemin, ext)}} + liste des .txt ecartes (doublon d'un .md)."""
    jours, ecartes = {}, []
    for d in sorted({HIST, sorties}):
        for n in sorted(os.listdir(d)):
            m = NOM.match(n)
            if not m or not os.path.isfile(os.path.join(d, n)):
                continue
            jour, s, ext = m.group(1), int(m.group(2) or 0), m.group(3)
            cur = jours.setdefault(jour, {}).get(s)
            p = os.path.join(d, n)
            if cur is None:
                jours[jour][s] = (p, ext)
            elif cur[1] == 'txt' and ext == 'md':
                ecartes.append(cur[0])
                jours[jour][s] = (p, ext)
            else:
                ecartes.append(p)
    return jours, ecartes


def lire(p):
    with open(p, 'rb') as f:
        return f.read().decode('utf-8-sig', 'replace').replace('\r\n', '\n')


def rendre_jour(jour, sessions):
    nav, corps = '', ''
    for s in sorted(sessions):
        p, ext = sessions[s]
        titre = 'Session S%d' % s if s else 'Journal'
        ancre = 's%d' % s
        nav += '<a href="#%s">%s</a>' % (ancre, titre)
        t = lire(p)
        bloc = rend_md(t) if ext == 'md' else rend_txt(t.splitlines())
        corps += '<section id="%s"><h2>%s</h2><p class="src">Source : %s</p>\n%s\n</section>\n' % (
            ancre, titre, esc(os.path.basename(p)), bloc)
    page = (tete('Journal de bord ' + jour) + '<h1>Journal de bord du %s</h1><p class="mut">%d session(s)</p>\n'
            '<nav><a href="index.html">Liste des jours</a> %s</nav>\n%s</body></html>\n' % (jour, len(sessions), nav, corps))
    return page


def ecrire_page(chemin, page, avec_bak=True):
    donnees = page.encode('utf-8')
    etat = 'cree'
    if os.path.isfile(chemin):
        with open(chemin, 'rb') as f:
            ancien = f.read()
        if GEN.encode() not in ancien:
            return 'COLLISION : page existante non generee par ce script, ignoree'
        if ancien == donnees:
            return 'inchange'
        etat = 'mis a jour'
        if avec_bak:
            bak = '%s.bak_%s.html' % (os.path.splitext(chemin)[0], datetime.datetime.now().strftime('%Y_%m_%d_%Hh%Mm%Ss'))
            shutil.copy2(chemin, bak)
            etat += ' (bak ' + os.path.basename(bak) + ')'
    with open(chemin, 'wb') as f:
        f.write(donnees)
    return etat


def main(a):
    sorties = dossier_pages()
    if not sorties:
        print('DOSSIER 02_* ABSENT dans ' + HIST)
        return 2
    jours, ecartes = collecter(sorties)
    fus = dossier_fusionne(sorties)
    fusionnes = sorted(FUS.match(n).group(1) for n in os.listdir(fus) if FUS.match(n)) if fus else []
    if not a:
        cibles = [datetime.date.today().strftime('%Y-%m-%d')]
        cf = fusionnes[-1:]
    elif a[0] == 'tout':
        cibles = sorted(jours)
        cf = fusionnes
    elif a[0] == 'fusionne':
        cibles = []
        cf = fusionnes
    else:
        cibles = [a[0]]
        cf = []
    code = 0
    for nom in cf:
        etat = ecrire_page(os.path.join(fus, nom + '.html'), rendre_fusionne(nom, os.path.join(fus, nom + '.md')))
        print('%s.html : %s' % (nom, etat))
    if fus:
        print('Fusionne\\index.html : ' + ecrire_page(os.path.join(fus, 'index.html'),
              index_dossier(fus, re.compile(r'^(JOURNAL_.+)\.html$')), avec_bak=False))
    for j in cibles:
        if j not in jours:
            print('%s : AUCUN JOURNAL histo_%s*.md ou .txt' % (j, j))
            code = 1
            continue
        etat = ecrire_page(os.path.join(sorties, 'histo_%s.html' % j), rendre_jour(j, jours[j]))
        print('histo_%s.html : %s' % (j, etat))
    for p in ecartes:
        print('ECARTE (doublon d un .md ou d un .txt) : ' + p)
    lignes = ''
    for n in sorted(os.listdir(sorties), reverse=True):
        m = re.match(r'^histo_(\d{4}-\d{2}-\d{2})\.html$', n)
        if not m:
            continue
        with open(os.path.join(sorties, n), 'rb') as f:
            t = f.read().decode('utf-8', 'replace')
        if GEN in t:
            info = '%d session(s)' % t.count('<section')
        else:
            info = 'page d origine, non generee'
        lignes += '<tr><td><a href="%s">%s</a></td><td>%s</td></tr>\n' % (n, m.group(1), info)
    idx = (tete('Journaux de bord') + '<h1>Journaux de bord</h1>\n<table><tr><th>Jour</th><th>Contenu</th></tr>\n' +
           lignes + '</table></body></html>\n')
    print('index.html : ' + ecrire_page(os.path.join(sorties, 'index.html'), idx, avec_bak=False))
    return code


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
