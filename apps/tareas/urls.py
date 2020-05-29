from django.urls import path
from apps.tareas.views import TareasCreate

urlpatterns = [
    path('tarea_form/', TareasCreate.as_view(), name='tarea_form')
]
