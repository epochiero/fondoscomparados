from django.shortcuts import render_to_response
from django.template import RequestContext
from models import *


def index(request, template="index.html"):
    data= {}
    data['ba'] = ProvinciaPorAnio.objects.filter(provincia__nombre="Buenos Aires")
    data['sf'] = ProvinciaPorAnio.objects.filter(provincia__nombre="Santa Fe")
    data['er'] = ProvinciaPorAnio.objects.filter(provincia__nombre="Entre Rios")
    return render_to_response(template, data, context_instance=RequestContext(request))
