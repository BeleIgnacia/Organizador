from django.db import models

# Modelos
from apps.hogar.models import Domicilio, Usuario, Dependencia


class Tarea(models.Model):
    nombre = models.CharField(max_length=50)
    # Toda tarea esta ligada al domicilio en que se crea
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    complejidad = models.PositiveIntegerField(default=0)
    duracion = models.DurationField(default=0)
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    comentarios = models.TextField(max_length=200, blank=True)
    # Tareas por defecto no son asignadas ni completadas
    asignada = models.BooleanField(default=False)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.nombre)


class AsignarTarea(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calendarizar = models.BooleanField(default=False)
    # Usuario notifica su tarea asignada como completada
    notifica_completada = models.BooleanField(default=False)

    def __str__(self):
        return 'tarea {} a usuario {}'.format(self.tarea, self.usuario)
