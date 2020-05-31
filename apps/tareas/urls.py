from apps.tareas.views import crear_tarea,  listar_tareas, asignar_tarea
from django.urls import path


urlpatterns = [
    path('tarea_form/', crear_tarea.as_view(), name='tarea_form'),
    path('listar_tareas/', listar_tareas.as_view(), name='listar_tareas'),
    path('asignar_tarea/', asignar_tarea.as_view(), name='asignar_tarea'),
]
