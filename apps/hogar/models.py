from django.db import models

from django.contrib.auth.models import User


class Domicilio(models.Model):
    calle = models.CharField(max_length=50)
    numero = models.IntegerField(default=0)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return '{} {}, {}, {}'.format(self.calle, self.numero, self.comuna, self.ciudad)

# Usuario crea sus dependencias
# Todas las que quiera
# Luego ve si las asigna
class Dependencia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)

# Son un tanto redundantes estos modelos
# Pero su estructura es necesaria para los formularios
# Para consultar por las dependencias de un domicilio es
# pd = PerteneceDependencia.objects.filter(domicilio=self.usuario.domicilio,asignada=True)
# pd es un queryset
class PerteneceDependencia(models.Model):
    dependencia = models.ForeignKey(Dependencia, on_delete=models.CASCADE)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    asignada = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.dependencia)

class Usuario(User):
    user = models.OneToOneField(User, parent_link=True, on_delete=models.CASCADE)
    # Por defecto se registra como administrador
    es_administrador = models.BooleanField(default=True)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.user)
