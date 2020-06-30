from django.db import models
from django.utils import timezone

from apps.tareas.models import AsignarTarea


# Create your models here.
class Event(models.Model):
    asignar_tarea = models.ForeignKey(AsignarTarea, on_delete=models.CASCADE)

    title = models.CharField(max_length=100, default='Title')
    type = models.CharField(blank=True, null=True, max_length=10, default='EV')
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    # all_day = models.BooleanField(default=False)

    def __str__(self):
        return self.title
