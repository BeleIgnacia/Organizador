from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    #path('', add_event),
    #path('view', calendar),
    #path('eventslist', events_list),
    path('mostrar', MostrarCalendario.as_view(), name='mostrar_calendario'),
    path('listar_tareas', ListarTareasUsuario, name='listar_tareas'),
]
