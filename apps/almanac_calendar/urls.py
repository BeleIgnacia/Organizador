from django.contrib import admin
from django.urls import include, path
from . import views
from .views import *

urlpatterns = [
    #path('', add_event),
    #path('view', calendar),
    #path('eventslist', events_list),
    path('mostrar', MostrarCalendario.as_view(), name='mostrar_calendario'),
    path('mostrar/<str:valida>', MostrarCalendario.as_view(), name='mostrar_calendario_valida'),
    path('listar_tareas', ListarTareasUsuario, name='listar_tareas'),
    path('agregar_horario_ocupado', views.Horario_Ocupado_View, name='agregar_horario_ocupado'),
]
