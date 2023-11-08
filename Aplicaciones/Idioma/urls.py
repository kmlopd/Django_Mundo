from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('Idiomas/', views.ListarIdiomas.as_view()),
    path('PaginacionIdiomas/' , views.ListPagIdioma.as_view()),
    path('DatalleIdiomas/<pk>' , views.Detail_Idioma.as_view()),
    path('AddIdiomas/' , views.AgregarIdioma.as_view()),
]