from django.shortcuts import render
from django.template import Context, Template
from .models import Familiar

def mostrarFamiliares(request):
    primer_familiar = Familiar(nombre = "Alejandra", edad = 40, fecha_de_nacimiento = 24/3/1982)

    primer_familiar.save()

    segundo_familiar = Familiar(nombre = "Francisco", edad = 40, fecha_de_nacimiento = 20/10/1982)

    segundo_familiar.save()

    tercer_familiar = Familiar(nombre = "Roque", edad = 60, fecha_de_nacimiento = 14/3/1962)

    tercer_familiar.save()

    familiares = [primer_familiar, segundo_familiar, tercer_familiar]

    return render(request, 'MostrarFamiliares.html', {'Familiares': familiares})
