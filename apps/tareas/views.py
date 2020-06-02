from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages

# Formularios
from apps.tareas.forms import TareaForm,AsignarTareaForm

# Modelos
from apps.hogar.models import Usuario,Domicilio
from apps.tareas.models import Tarea,AsignarTarea


class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/crear_tarea.html'
    success_url = reverse_lazy('tareas:crear_tarea')

    def post(self, request, *arg, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        if form.is_valid():
            # Almacena una instancia del formulario
            instance = form.save(commit=False)
            # Reemplaza la recibida por el formulario
            instance.domicilio = self.usuario.domicilio
            # Guarda el formulario
            instance.save()
            # Redirige al usuario a la pantalla de login
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class AsignarTarea(CreateView):
    model = AsignarTarea
    form_class = AsignarTareaForm
    template_name = 'tareas/asignar_tarea.html'
    success_url = reverse_lazy('tareas:asignar_tarea')

    def get_context_data(self,**kwargs):
        context = super(AsignarTarea, self).get_context_data(**kwargs)
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        # Filtra las posibles asignaciones que pueda realizar el admin según su domicilio
        context['form'].fields['tarea'].queryset = Tarea.objects.filter(domicilio=self.usuario.domicilio,asignada=False)
        context['form'].fields['usuario'].queryset = Usuario.objects.filter(domicilio=self.usuario.domicilio)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Busca la tarea a asignarse
        tarea = Tarea.objects.get(pk=instance.tarea.pk)
        # Indica que la terea ahora se encuentra asignada
        tarea.asignada = True
        # Guarda la tarea y la asignación a usuario
        tarea.save()
        instance.save()
        return HttpResponseRedirect(reverse_lazy('tareas:asignar_tarea'))

class ListarTarea(ListView):
    model = Tarea
    template_name = 'tareas/listar_tareas.html'

    def get_queryset(self):
        # Toma la id de usuario almacenada
        pk_usuario = self.request.session.get('pk_usuario','')
        # Intancia el objeto usuario
        usuario = Usuario.objects.get(pk=pk_usuario)
        if usuario:
            # Retorna las tareas filtradas según domicilio
            return Tarea.objects.filter(domicilio=usuario.domicilio)

    def form_valid(self, form):
        instance = form.save(commit=False)
        print(instance)
        instance.save()
        return HttpResponseRedirect(self.get_success_url())
