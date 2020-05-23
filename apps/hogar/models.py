from django.db import models

from django.contrib.auth.models import User

class Usuario(User):
	user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
	# Por defecto se registra como administrador
	es_administrador = models.BooleanField(default=True)
	domicilio = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)