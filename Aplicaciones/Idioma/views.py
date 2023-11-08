from django.shortcuts import render
from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.db.models.query import QuerySet
from .models import Idioma
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)


# Create your views here.
class ListarIdiomas(ListView):
    template_name = 'Idioma/ListarIdiomas.html'
    model = Idioma
    context_object_name = 'Idiomas'

class ListPagIdioma (ListView):
    template_name = 'Idioma/ListPagIdioma.html'
    model = Idioma
    context_object_name = 'Idiomas'
    paginate_by = 3
    ordering = '-id'

class AgregarIdioma(CreateView):
    template_name = 'Idioma/AgregarIdioma.html'
    model = Idioma
    fields = '__all__'
    iden = ['id']
    success_url = '/DatalleIdiomas/'+str(iden)
    
    # def form_valid(self, form):
    #     Idioma = form.save
    #     Idioma.Nombre = Idioma.Nombre.upper()
    #     Idioma.save()
    #     return super(AgregarIdioma, self).form_valid(form)

class Detail_Idioma(DetailView):
    template_name = 'Idioma/Detail_Idioma.html'
    model= Idioma
    context_object_name = 'Idiomas'

