from django.db import models

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
