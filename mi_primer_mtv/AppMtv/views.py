from django.shortcuts import render
from django.template import Context, Template
from .models import Familiar

def mostrarFamiliares(request):
    primer_familiar = Familiar(nombre = "Alejandra", edad = 40, fecha_de_nacimiento = "1982-03-24")

    primer_familiar.save()

    segundo_familiar = Familiar(nombre = "Francisco", edad = 40, fecha_de_nacimiento = "1982-10-20")

    segundo_familiar.save()

    tercer_familiar = Familiar(nombre = "Roque", edad = 60, fecha_de_nacimiento = "1963-03-14")

    tercer_familiar.save()

    familiares = [primer_familiar, segundo_familiar, tercer_familiar]

    return render(request, 'MostrarFamiliares.html', {'Familiares': familiares})
