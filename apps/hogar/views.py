from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages

from apps.hogar.forms import RegisterUserForm

def registerUser(request):
	form = RegisterUserForm()
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {'form':form}
	return render(request, 'hogar/register.html', context)


def loginUser(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			#redirect()
			return redirect('hogar:dashboard')
		else:
			messages.info(request, 'Usuario o contraseña incorrectos')

	context = {}
	return render(request, 'hogar/login.html', context)

def dashboard(request):
	return render(request, 'hogar/dashboard.html')

'''
class RegistroUsuario(CreateView):
	model = User
	form_class = RegistroForm
	success_url = reverse_lazy('interfaz:inicio')
'''