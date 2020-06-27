from apps.tareas.views import CrearTarea,ListarTarea,AsignarTarea,ListarTareaAsignada,ModificarTarea,EliminarTarea
from django.urls import path


urlpatterns = [
    path('crear/', CrearTarea.as_view(), name='crear_tarea'),
    path('listar/', ListarTarea.as_view(), name='listar_tareas'),
    path('listar/asignadas/', ListarTareaAsignada.as_view(), name='listar_tareas_asignadas'),
    path('editar/<int:pk>',  ModificarTarea.as_view(), name='editar_tarea'),
    path('eliminar/<int:pk>',  EliminarTarea.as_view(), name='elimnar_tarea'),
    path('asignar/', AsignarTarea.as_view(), name='asignar_tarea'),
]
