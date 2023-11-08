from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('Pais/', views.ListarPais.as_view()),
    path('Paises-Continente/' , views.ListPaisByCont.as_view()),
]