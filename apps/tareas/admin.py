from django.contrib import admin
from apps.tareas.models import Tarea, AsignarTarea

# Register your models here.
admin.site.register(Tarea)
admin.site.register(AsignarTarea)
