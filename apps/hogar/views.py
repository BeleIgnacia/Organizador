from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,ListView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from apps.hogar.forms import *
from apps.hogar.models import *

# Vista para registrar usuario común
class RegisterUser(CreateView):
    model = Usuario
    template_name = 'hogar/añadir_usuario.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('hogar:añadir')

    # Despliega formulario por pantalla
    def get_context_data(self,**kwargs):
        context = super(RegisterUser,self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    # Recibe formulario de respuesta
    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)

        if form.is_valid():
            # Almacena una instancia del formulario
            instance = form.save(commit=False)
            # Instancia de usuario administrador
            self.usuario = Usuario.objects.get(pk=request.session.get('pk_usuario',''))
            # Reemplaza el domicilio en la instancia
            instance.domicilio = self.usuario.domicilio
            # Lo incializa como usuario común
            instance.es_administrador = 0
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
            # Instancia de objeto usuario
            usuario = Usuario.objects.get(username=username)
            # Almacena la pk de usuario para utilizar a futuro
            request.session['pk_usuario'] = usuario.pk
            # Redirige
            return redirect('hogar:dashboard')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}
    return render(request, 'hogar/login.html', context)


def dashboard(request):
    pk_usuario = request.session.get('pk_usuario','')
    usuario = Usuario.objects.get(pk=pk_usuario)
    request.session['es_administrador'] = usuario.es_administrador
    return render(request, 'hogar/dashboard.html')


def index(request):
    return render(request, 'hogar/index.html')


def blog(request):
    return render(request, 'hogar/blog.html')


def services(request):
    return render(request, 'hogar/services.html')


def about(request):
    return render(request, 'hogar/about.html')


class Usuariolist(ListView):
    model = Usuario
    template_name = 'hogar/list_usuarios.html'

    def get_queryset(self):
        # Toma la id de usuario almacenada
        pk_usuario = self.request.session.get('pk_usuario','')
        # Intancia el objeto usuario
        usuario = Usuario.objects.get(pk=pk_usuario)
        if usuario:
            # Retorna los usuarios filtrados según domicilio
            return Usuario.objects.filter(domicilio=usuario.domicilio)