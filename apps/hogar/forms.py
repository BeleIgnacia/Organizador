from django.contrib.auth.models import User

from apps.hogar.models import Usuario,Domicilio,Dependencia,PerteneceDependencia

from django.contrib.auth.forms import UserCreationForm
from django import forms

# Fomulario de registro usuario normal
class UsuarioForm(UserCreationForm):

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

# Formulario de registro usuario administrador
class UsuarioAdminForm(UserCreationForm):
	
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

# Formulario de registro de domicilio
class DomicilioForm(forms.ModelForm):

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
			'calle': forms.TextInput(attrs={'placeholder':'Calle','class':'form-control'}),
			'numero': forms.NumberInput(attrs={'placeholder':'Número','class':'form-control'}),
			'comuna': forms.TextInput(attrs={'placeholder':'Comuna','class':'form-control'}),
			'ciudad': forms.TextInput(attrs={'placeholder':'Ciudad','class':'form-control'}),
		}

class CrearDependenciaForm(forms.ModelForm):

	class Meta:

		model = Dependencia
		fields = [
			'nombre',
		]
		labels = {
			'nombre': 'Nombre',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'placeholder':'Nombre','class':'form-control'}),
		}

class AsignarDependenciaForm(forms.ModelForm):

	class Meta:

		model = PerteneceDependencia
		fields = [
			'dependencia',
		]
		labels = {
			'dependencia': 'Dependencias',
		}
		widgets = {
			'dependencia': forms.Select(attrs={'placeholder':'Dependencias','class':'form-control'}),
		}