from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView,ListView,TemplateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from apps.hogar.forms import *
from apps.hogar.models import *

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from apps.almanac_calendar.forms import EventForm
from apps.almanac_calendar.models import Event
from apps.tareas.models import Tarea, AsignarTarea
from apps.hogar.models import Usuario

import json

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

    # Guarda nuevo usuario añadido a hogar
    def form_valid(self, form):
        instance = form.save(commit=False)
        self.usuario = Usuario.objects.get(pk=self.request.session.get('pk_usuario',''))
        instance.domicilio = self.usuario.domicilio
        instance.es_administrador = 0
        instance.save()
        return HttpResponseRedirect(self.get_success_url())

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
            request.session['es_administrador'] = usuario.es_administrador
            # Redirige
            return redirect('hogar:dashboard')
        else:
            messages.info(request, 'Usuario o contraseña incorrectos')

    context = {}
    return render(request, 'hogar/login.html', context)


class Dashboard(TemplateView):
    template_name = 'hogar/dashboard.html'

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

# View para modificar domicilio
class DomicilioModificar(CreateView):
    model = Domicilio
    form_class = DomicilioForm
    template_name = 'hogar/domicilio_modificar.html'
    success_url = reverse_lazy('hogar:domicilio_modificar')

    def get_context_data(self,**kwargs):
        context = super(DomicilioModificar, self).get_context_data(**kwargs)
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        context['domicilio_actual'] = self.usuario.domicilio
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        self.usuario.domicilio.calle = instance.calle
        self.usuario.domicilio.numero = instance.numero
        self.usuario.domicilio.comuna = instance.comuna
        self.usuario.domicilio.ciudad = instance.ciudad
        self.usuario.domicilio.save()
        return HttpResponseRedirect(self.success_url)

# View para crear y asignar dependencias, las dos en una
class DomicilioDependencias(CreateView):
    model = Dependencia
    template_name = 'hogar/domicilio_dependencias.html'
    form_class = CrearDependenciaForm
    second_form_class = AsignarDependenciaForm
    success_url = reverse_lazy('hogar:domicilio_dependencias')

    def get_context_data(self, **kwargs):
        context = super(DomicilioDependencias, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)

        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        context['dependencias_disponibles'] = PerteneceDependencia.objects.filter(domicilio=self.usuario.domicilio,asignada=False)
        context['dependencias_asignadas'] = PerteneceDependencia.objects.filter(domicilio=self.usuario.domicilio,asignada=True)
        context['form2'].fields['dependencia'].queryset = PerteneceDependencia.objects.filter(domicilio=self.usuario.domicilio,asignada=False)
        return context

    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
            pertence_instance = PerteneceDependencia(domicilio=self.usuario.domicilio,dependencia=instance,asignada=False)
            instance.save()
            pertence_instance.save()
            return HttpResponseRedirect(self.get_success_url())
        elif form2.is_valid():
            instance = form2.save(commit=False)
            self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
            self.pertenece_instance = PerteneceDependencia.objects.get(dependencia_id=instance.dependencia.pk)
            self.pertenece_instance.asignada = True
            self.pertenece_instance.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))

def MostrarCalendario(request):
    tareas_asignadas=Tarea.objects.filter(asignada=True)
    print(tareas_asignadas)
    lista_tareas = []
    for tareas in tareas_asignadas:
        lista_tareas.append(tareas)
    print(lista_tareas)
    event=Event.objects.all()
    event.delete()
    for tareas in lista_tareas:
        event = Event.objects.create(title=tareas.nombre)
    event=Event.objects.all()
    events = eval(serializers.serialize("json", event))
    events = list(map(lambda x: x['fields'], events))
    print(events)
    return render(request, 'almanac_calendar/calendar.html', context={'events': events})
