from apps.tareas.views import CrearTarea,ListarTarea,AsignarTarea,ListarTareaAsignada
from django.urls import path


urlpatterns = [
    path('tarea_form/', CrearTarea.as_view(), name='crear_tarea'),
    path('listar_tareas/', ListarTarea.as_view(), name='listar_tareas'),
    path('listar_tareas_asignadas/', ListarTareaAsignada.as_view(), name='listar_tareas_asignadas'),
    path('asignar_tarea/', AsignarTarea.as_view(), name='asignar_tarea'),
]
