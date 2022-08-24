from django.urls import path
from .views import *


urlpatterns = [
    path('familiar1/', mostrarPrimerFamiliar),
]