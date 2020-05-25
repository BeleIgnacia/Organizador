from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from apps.hogar.forms import RegisterUserForm,RegisterDirectionForm
from apps.hogar.models import Domicilio,Usuario

class Register(CreateView):
	model = Domicilio
	template_name = 'hogar/register.html'
	form_class = RegisterUserForm
	second_form_class = RegisterDirectionForm
	success_url = reverse_lazy('login')

	def get_context_data(self, **kwargs):
		context = super(Register, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *arg, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			sol = form.save(commit=False)
			sol.domicilio = form2.save()
			sol.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

'''
def registerUser(request):
	form = RegisterUserForm()
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	context = {'form':form}
	return render(request, 'hogar/register.html', context)
'''

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