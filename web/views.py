# coding: utf-8

from models import *
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

# Filtra els resultats per pagina
def select(request, pag_id):
    page = request.GET.get('page')

    if not page:
        page = 1

    if not pag_id:
        pag_id = 0

    pag_id = int(pag_id)
    if pag_id > 0:
        noticies = Noticia.objects.filter(pagina=pag_id).order_by('id')
    else:
        noticies = Noticia.objects.all().order_by('id')

    pags = Pagina.objects.all().order_by('id')

    n = 5 # numero per pagina
    p = Paginator(noticies, n)
    total = p.count / n
    pages = p.page(page)
    entrades = pages.object_list

    data = {"entrades": entrades,
            "pagines": pags,
            "noticies": pages,
            "total": total,
           }
    return render_to_response("index.html", data)
