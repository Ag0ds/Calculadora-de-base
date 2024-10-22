from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("CalcularBase", views.calcular, name="calcular"),
    path("Operaçoes", views.operacoes, name="operacoes")
]
