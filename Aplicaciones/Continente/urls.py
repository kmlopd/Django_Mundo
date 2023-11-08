from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('Continentes/', views.ListarContinentes.as_view()),
]