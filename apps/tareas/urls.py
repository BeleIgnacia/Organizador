from django.urls import path
from apps.tareas.views import TareasCreate, listar_tareas

urlpatterns = [
    path('tarea_form/', TareasCreate.as_view(), name='tarea_form'),
    path('listar_tareas/', listar_tareas, name='listar_tareas')
]
