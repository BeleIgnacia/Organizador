from django.db import models

from django.contrib.auth.models import User

class Domicilio(models.Model):
	calle = models.CharField(max_length=50)
	numero = models.IntegerField(default=0)
	comuna = models.CharField(max_length=50)
	ciudad = models.CharField(max_length=50)

	def __str__(self):
		return '{} {}, {}, {}'.format(self.calle, self.numero, self.comuna, self.ciudad)

class Usuario(User):
	user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
	# Por defecto se registra como administrador
	es_administrador = models.BooleanField(default=True)
	domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
	#domicilio = models.CharField(max_length=50)
	telefono = models.CharField(max_length=50)