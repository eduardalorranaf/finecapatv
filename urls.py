from django.contrib import admin
from django.urls import path
from reservas.views import index, reserva_criar, reserva_deletar, reserva_editar, reserva_listar


urlpatterns = [
    path('', index, name='index'),
    path('reserva/criar', reserva_criar, name='reserva_criar'),
    path('reserva/listar', reserva_listar, name='reserva_listar'),
    path('reserva/editar/<int:id>/', reserva_editar, name='reserva_editar'),
    path('reserva/deletar/<int:id>/' , reserva_deletar, name='reserva_deletar'),
    path('admin/', admin.site.urls)
]
