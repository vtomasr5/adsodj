#!/usr/bin/env python
# coding: utf-8

from urllib2 import urlopen, URLError, HTTPError
import re, sys

sites = ('http://www.genbetadev.com/', 'http://www.xatakaciencia.com/', 'http://www.vidaextra.com/', 'http://www.blogdecine.com/')

def get_urls(url):
    urls = set()
    domains = set()
    try:
        doc = urlopen(url)
        html = doc.read()
    except (URLError, HTTPError), e:
        print "Error conectando con ", url
        sys.exit(-1)

    res = re.findall(r'<(?:a|img|link|script) .*?(?:href|src)=["\'](.+?)["\'].*?>', html, re.I | re.S) # Mal
    if res:
        for i in res:
            r = re.search(r'<h2>\s*<a href="(.+)"\s+title="(.+)">', res, re.I)
            if p:
                t = r.groups()[0].strip()
                u = r.groups()[1].strip()
                print "LINKS:", t
                print "URL:", u
            else:
                print "Res2"
    else:
        "Res1"
    return titol, url

    # r'\.(.+?)\.' # quedar-se amb el basename de sa url

#~ def check_url(url):
    #~ try:
        #~ d = urlopen(url)
        #~ s = d.read(4096)
        #~ return True
    #~ except (URLError, HTTPError), e:
        #~ return False

# Inici
for url in sites:
    titol, url = get_urls(url)

#~ for u in urls:
    #~ print u
    #~ if check_url(u):
        #~ print "OK:", u
    #~ else:
        #~ print "BAD:", u
