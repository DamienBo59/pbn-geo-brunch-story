# -*- coding: utf-8 -*-
"""Recupere une image libre de droit sur Wikimedia Commons.
Repli sur l'API Openverse, injoignable depuis cette machine (timeout sur
api.openverse.org, 403 sur openverse.org, verifie le 2026-09-12).
Ne garde que les licences autorisant l'usage commercial et la modification.
"""
import json, sys, re, subprocess, urllib.parse, urllib.request, os, html

UA = "brunch-story-bot/1.0 (https://www.brunch-story.fr/; contact via site)"
OK_LIC = ('cc0', 'public domain', 'pd-', 'cc-by-sa-4.0', 'cc-by-sa-3.0',
          'cc-by-4.0', 'cc-by-3.0', 'cc-by-2.0', 'cc-by-sa-2.0', 'attribution')
BAD = ('-nc', 'noncommercial', '-nd', 'noderiv', 'fair use', 'nonfree')
# Le moteur de Commons classe par pertinence textuelle et remonte volontiers des
# planches contact ou des plateaux de cantine. On exige donc un mot de la requete
# dans le titre du fichier, et on ecarte le bruit documentaire.
TITRE_BAD = ('contact sheet', 'photo contact', 'school tray', 'logo', 'diagram',
             'map of', 'chart', 'poster', 'coat of arms', 'stamp', 'banknote',
             'plaque', 'signage', 'nutrition facts', 'label', 'packaging',
             'museum', 'archive', 'library', 'portrait of', 'president')

def api(params):
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    return json.load(urllib.request.urlopen(req, timeout=30))

def clean(s):
    if not s: return ""
    s = re.sub(r'<[^>]+>', '', s)
    return html.unescape(s).strip()

def fetch(query, slug, outdir):
    r = api({'action':'query','format':'json','generator':'search',
             'gsrsearch':'filetype:bitmap ' + query, 'gsrnamespace':6, 'gsrlimit':30,
             'prop':'imageinfo','iiprop':'url|extmetadata|size','iiurlwidth':1600})
    pages = list(r.get('query', {}).get('pages', {}).values()) if 'query' in r else []
    for p in pages:
        ii = (p.get('imageinfo') or [{}])[0]
        if not ii: continue
        if ii.get('width', 0) < 900: continue
        meta = ii.get('extmetadata', {})
        lic = (meta.get('LicenseShortName', {}).get('value', '') + ' ' +
               meta.get('License', {}).get('value', '')).lower()
        if any(b in lic for b in BAD): continue
        if not any(k in lic for k in OK_LIC): continue
        src = ii.get('thumburl') or ii.get('url')
        if not src: continue
        artist = clean(meta.get('Artist', {}).get('value', '')) or 'auteur non precise'
        artist = re.sub(r'\s+', ' ', artist)[:70]
        licname = clean(meta.get('LicenseShortName', {}).get('value', '')) or 'licence libre'
        title = clean(meta.get('ObjectName', {}).get('value', '')) or p.get('title','').replace('File:','')
        title = os.path.splitext(title)[0][:110]
        tl = title.lower()
        if any(b in tl for b in TITRE_BAD): continue
        mots = [m for m in query.lower().split() if len(m) > 3]
        if mots and not any(m in tl for m in mots): continue
        # telechargement
        tmp = '/tmp/_img_dl'
        try:
            req = urllib.request.Request(src, headers={'User-Agent': UA})
            data = urllib.request.urlopen(req, timeout=60).read()
        except Exception as e:
            print("  (echec telechargement %s: %s)" % (p.get('title'), e), file=sys.stderr); continue
        if len(data) < 15000: continue
        open(tmp, 'wb').write(data)
        os.makedirs(outdir, exist_ok=True)
        dest = os.path.join(outdir, slug + '.webp')
        cmd = ['magick', tmp, '-resize', '1600x1600>', '-quality', '82', dest]
        if subprocess.call(cmd) != 0: continue
        return {'path': '/images/blog/%s.webp' % slug, 'alt': title,
                'credit': 'Photo par %s via Wikimedia Commons (%s)' % (artist, licname),
                'source': p.get('title')}
    return None

if __name__ == '__main__':
    q, slug, outdir = sys.argv[1], sys.argv[2], sys.argv[3]
    res = fetch(q, slug, outdir)
    if not res:
        print("ECHEC: aucune image conforme pour '%s'" % q, file=sys.stderr); sys.exit(3)
    print(json.dumps(res, ensure_ascii=False))
