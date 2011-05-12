# Create your views here.

from django.shortcuts import render_to_response
from models import *

from django.http import HttpResponse

def index(request):
    html = '<html><body>Hola</body></html>'
    return HttpResponse(html)
