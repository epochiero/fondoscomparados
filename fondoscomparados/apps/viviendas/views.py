from django.shortcuts import render
from .models import *


def index(request, template="index.html"):
    try:
        year = int(request.GET.get('year', 2006))
    except ValueError:
        year = 2006
    data = {}
    data['cba'] = ProvinciaPorAnio.objects.filter(provincia__nombre="Cordoba", anio=year)
    data['sf'] = ProvinciaPorAnio.objects.filter(provincia__nombre="Santa Fe", anio=year)
    data['er'] = ProvinciaPorAnio.objects.filter(provincia__nombre="Entre Rios", anio=year)
    data['year'] = year
    return render(request, template, data)
