from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from .models import Pais
from django.views.generic import (
    ListView,
)


# Create your views here.
class ListarPais(ListView):
    template_name = 'Pais/ListarPais.html'
    model = Pais
    context_object_name = 'Paises'


class ListPaisByCont(ListView):
    template_name = 'Pais/ListPaisByCont.html'
    model = Pais
    context_object_name = 'Paises'

    # def get_queryset(self):
    #     x = self.request.GET.get('Continente','')
    #     PaisContinete = Pais.objects.get(Continente=x)
    #     Paise = PaisContinete.Continente.all()
    #     return Paise

