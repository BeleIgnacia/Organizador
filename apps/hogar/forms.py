from django.contrib.auth.models import User

from apps.hogar.models import Usuario,Domicilio

from django.contrib.auth.forms import UserCreationForm
from django import forms

# Fomulario de registro usuario normal
class UsuarioForm(UserCreationForm):

	def __init__(self,*args,**kwargs):
		super(UsuarioForm,self).__init__(*args,**kwargs)
		# Si es un usuario normal desabilita el registro de administrador
		self.fields['es_administrador'].initial = False
		# Cambia el valor incial del widget a 1
		'''
			Esto unicamente es para que la forma sea valida, el valor que
			se le asigne en el widget será reemplazado en la view.
		'''
		self.fields['domicilio'].initial = '1'

	class Meta:

		model = Usuario
		fields = [
			'username',
			'email',
			'password1',
			'password2',
			'telefono',
			'es_administrador',
			'domicilio',
		]
		labels = {
			'username': 'Nombre de usuario',
			'email': 'Dirección de correo',
			'password1': 'Contraseña',
			'password2': 'Repetir contraseña',
			'telefono': 'Teléfono',
			'es_administrador': 'es_administrador',
			'domicilio': 'domicilio',
		}
		widgets = {
			'username': forms.TextInput(attrs={'placeholder':'Nombre de usuario'}),
			'email': forms.TextInput(attrs={'placeholder':'Dirección de correo'}),
			'password1': forms.TextInput(attrs={'placeholder':'Contraseña'}),
			'password2': forms.TextInput(attrs={'placeholder':'Contraseña'}),
			'telefono': forms.TextInput(attrs={'placeholder':'Teléfono'}),
			'es_administrador': forms.CheckboxInput(attrs={'hidden': True}),
			'domicilio': forms.Select(attrs={'hidden':True,'value':1})
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
			'calle': forms.TextInput(attrs={'placeholder':'Calle'}),
			'numero': forms.NumberInput(attrs={'placeholder':'Número'}),
			'comuna': forms.TextInput(attrs={'placeholder':'Comuna'}),
			'ciudad': forms.TextInput(attrs={'placeholder':'Ciudad'}),
		}