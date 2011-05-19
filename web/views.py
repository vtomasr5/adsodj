# coding: utf-8

from models import *
from django.shortcuts import render_to_response
from django.core.paginator import Paginator

def select(request, pag_id):
    page = request.GET.get('page')

    if not page:
        page = 1

    if not pag_id:
        pag_id = 0

    pag_id = int(pag_id)
    if pag_id > 0:
        noticies = Noticia.objects.filter(pagina=pag_id).order_by('-id')
    else:
        noticies = Noticia.objects.all().order_by('-id')

    pags = Pagina.objects.all().order_by('id')

    p = Paginator(noticies, 5)
    pages = p.page(page)
    entrades = pages.object_list

    data = {"entrades": entrades,
            "pagines": pags,
            "noticies": pages,
           }
    return render_to_response("index.html", data)
