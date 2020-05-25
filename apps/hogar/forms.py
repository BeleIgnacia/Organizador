from django.contrib.auth.models import User

from apps.hogar.models import Usuario,Domicilio

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
			'telefono',
		]
		labels = {
			'username': 'Nombre de usuario',
			'email': 'Dirección de correo',
			'password1': 'Contraseña',
			'password2': 'Repetir contraseña',
			'telefono': 'Teléfono',
		}
		widgets = {
			'username': forms.TextInput(attrs={'placeholder':'Nombre de usuario'}),
			'email': forms.TextInput(attrs={'placeholder':'Dirección de correo'}),
			'password1': forms.TextInput(attrs={'placeholder':'Contraseña'}),
			'password2': forms.TextInput(attrs={'placeholder':'Contraseña'}),
			'telefono': forms.TextInput(attrs={'placeholder':'Teléfono'}),
		}

class RegisterDirectionForm(forms.ModelForm):

	class Meta:
		model = Domicilio
		fields = [
			'calle',
			'numero',
			'comuna',
			'ciudad',
		]
		labels = {
			'calle': 'Calle',
			'numero': 'Número',
			'comuna': 'Comuna',
			'ciudad': 'Ciudad',
		}
		widgets = {
			'calle': forms.TextInput(attrs={'placeholder':'Calle'}),
			'numero': forms.NumberInput(attrs={'placeholder':'Número'}),
			'comuna': forms.TextInput(attrs={'placeholder':'Comuna'}),
			'ciudad': forms.TextInput(attrs={'placeholder':'Ciudad'}),
		}