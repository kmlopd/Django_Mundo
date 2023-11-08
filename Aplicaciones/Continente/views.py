from typing import Any
from django.shortcuts import render
from django.db.models.query import QuerySet
from .models import Continente
from django.views.generic import (
    ListView,
)

# Create your views here.
class ListarContinentes(ListView):
    template_name = 'Continente/ListarContinentes.html'
    model = Continente
    context_object_name = 'Continentes'