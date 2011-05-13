# Create your views here.

from django.utils.translation import gettext as _
from django.shortcuts import render_to_response, redirect
from models import *

from django.http import HttpResponse

def index(request):
    return render_to_response('index.html', locals())

def base(request):
    data = {'h1': 'Base', 'title': 'titol base', 'content': 'contingut base'}
    return render_to_response('base.html', data)
