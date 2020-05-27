from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from apps.hogar.forms import *
from apps.hogar.models import *

# Vista para registrar usuario común
class RegisterUser(CreateView):
    model = Usuario
    template_name = 'hogar/register.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    # Despliega formulario por pantalla
    def get_context_data(self,**kwargs):
        context = super(RegisterUser,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    # Recive formulario de respuesta
    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        # Identifica el id del domicilio por la url
        self.domicilio_id = self.kwargs['domicilio_id']
        # Si el formulario es valido
        if form.is_valid():
            # Almacena una instancia del formulario
            instance = form.save(commit=False)
            # Determina la instancia de Domicilio base a la id
            self.domicilio = Domicilio.objects.get(pk=self.domicilio_id)
            # Reemplaza la recivida por el formulario
            instance.domicilio = self.domicilio
            # Guarda el formulario
            instance.save()
            # Redirige al usuario a la pantalla de login
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

# Vista doble form para registrar domicilio y usuario administrador
class Register(CreateView):
    model = Domicilio
    template_name = 'hogar/register.html'
    form_class = UsuarioAdminForm
    second_form_class = DomicilioForm
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
	form = UsuarioAdminForm()
	if request.method == 'POST':
		form = UsuarioAdminForm(request.POST)
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
            # redirect()
            return redirect('hogar:dashboard')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}
    return render(request, 'hogar/login.html', context)


def dashboard(request):
    return render(request, 'hogar/dashboard.html')


def index(request):
    return render(request, 'hogar/index.html')


def blog(request):
    return render(request, 'hogar/blog.html')


def services(request):
    return render(request, 'hogar/services.html')


def about(request):
    return render(request, 'hogar/about.html')
