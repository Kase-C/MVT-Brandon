from lzma import _FilterChain
from django.http import HttpResponse
from django.template import Context, Template, loader
from models import Familiar

def mostrarPrimerFamiliar(request):
    primer_familiar = Familiar(nombre = "Alejandra", edad = 40, fecha_de_nacimiento = 24/3/1982)

    primer_familiar.save()

    diccionario = {"Nombre": primer_familiar.nombre, "Edad": primer_familiar.edad, "Fecha_de_nacimiento": primer_familiar.fecha_de_nacimiento}

    plantilla = loader.get_template('MostrarFamiliar.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


