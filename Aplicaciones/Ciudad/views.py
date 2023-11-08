from django.shortcuts import render
from typing import Any
from django.db.models.query import QuerySet
from .models import Ciudad
from django.views.generic import (
    ListView,
)


# Create your views here.
class ListarCiudades(ListView):
    template_name = 'Ciudad/ListarCiudades.html'
    model = Ciudad
    context_object_name = 'Ciudades'

