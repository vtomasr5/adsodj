#!/usr/bin/env python
# coding: utf-8

from urllib2 import urlopen, URLError, HTTPError
import re, sys, os
import django

directory = "/home/vjuan/uib/ADSO/adsodj"
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
sys.path.append(os.path.abspath(directory))

from web.models import Pagina, Noticia

sites = ('http://www.genbetadev.com', 'http://www.xatakaciencia.com', 'http://www.vidaextra.com', 'http://www.blogdecine.com')

# Guardamos en la BD las paginas
for i in range(len(sites)):
    reg = Pagina()
    reg.urlbase = sites[i]
    try:
        reg.save()
    except django.db.utils.IntegrityError:
        pass

# Obtenemos las URL del html de las paginas
def getUrls(url):
    urls = []
    titols = []
    try:
        doc = urlopen(url)
        html = doc.read()
    except (URLError, HTTPError), e:
        print "error conectando a ", url
        return urls

    g = re.findall(r'<div class="post post-single">.*? <h2><a .*?>.*?</h2>', html, re.I | re.S)
    if g:
        for m in g:
            p = re.search('<h2><a .*href="(.+)".*?title="(.+?)"', m, re.I)
            if p:
                l = p.groups()[0].strip()
                urls.append(url+l)
                t = p.groups()[1].strip()
                titols.append(t)
                #~ print "LINK:" + url + l
                #~ print "TITLE:" + t + "\n"

    return urls, titols

# Guardamos las noticias de las paginas en la BD
def toDB(u, t, pag, pag_id):
    for i in range(len(u)):
        reg = Noticia()
        reg.url = u[i]
        reg.titol = t[i]
        reg.pagina_id = pag_id
        try:
            reg.save()
        except django.db.utils.IntegrityError:
            pass

pags = Pagina.objects.all()
pag_id = 0
for pag in pags:
    url, titols = getUrls(pag.urlbase)
    toDB(url, titols, pag, pag.id)
    pag_id += 1
