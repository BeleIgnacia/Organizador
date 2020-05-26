from django.db import models
from apps.hogar.models import Usuario
# Create your models here.

class Tareas (models.Model):
    nombre = models.CharField(max_length=50)
    complejidad = models.IntegerField(default=0)
    duracion = models.IntegerField(default=0)
    lugar = models.CharField(max_length=50)
    encargado = models.ForeignKey(Usuario,null=True,blank=True,on_delete=models.CASCADE)
