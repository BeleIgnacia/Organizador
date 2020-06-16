from apps.tareas.views import CrearTarea,ListarTarea,AsignarTarea,ListarTareaAsignada
from django.urls import path


urlpatterns = [
    path('crear/', CrearTarea.as_view(), name='crear_tarea'),
    path('listar/', ListarTarea.as_view(), name='listar_tareas'),
    path('listar/asignadas/', ListarTareaAsignada.as_view(), name='listar_tareas_asignadas'),
    path('asignar/', AsignarTarea.as_view(), name='asignar_tarea'),
]
