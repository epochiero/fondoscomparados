from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *


def index(request, template="index.html"):
    data= {}
    data['ppa'] = ProvinciaPorAnio.objects.all()
    return render_to_response(template, data, context_instance=RequestContext(request))
