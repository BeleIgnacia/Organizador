from django.contrib.auth.models import User

from apps.hogar.models import Usuario

from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterUserForm(UserCreationForm):
	class Meta:
		model = Usuario
		fields = [
			'username',
			'email',
			'password1',
			'password2',
			'domicilio',
			'telefono',
		]
		labels = {
			'username': 'Nombre de usuario',
			'email': 'Dirección de correo',
			'password1': 'Contraseña',
			'password2': 'Repetir contraseña',
			'domicilio': 'Domicilio',
			'telefono': 'Teléfono',
		}
		widgets = {
			'username': forms.TextInput(attrs={'placeholder':'Nombre de usuario'}),
			'email': forms.TextInput(attrs={'placeholder':'Dirección de correo'}),
			'password1': forms.TextInput(attrs={'placeholder':'Contraseña'}),
			'password2': forms.TextInput(attrs={'placeholder':'Contraseña'}),
			'domicilio': forms.TextInput(attrs={'placeholder':'Domicilio'}),
			'telefono': forms.TextInput(attrs={'placeholder':'Teléfono'}),
		}