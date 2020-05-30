from django.db import models
from apps.hogar.models import Usuario
# Create your models here.

class Tareas (models.Model):
    nombre = models.CharField(max_length=50)
    complejidad = models.PositiveIntegerField(default=0)
    duracion = models.IntegerField(default=0)
    lugar = models.CharField(max_length=50)
    encargado = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
    fecha_creacion= models.DateField(auto_now_add=True)
    comentarios = models.CharField(max_length=200, blank=True)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
