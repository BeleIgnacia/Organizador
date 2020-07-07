from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

# Modelos
from apps.hogar.models import Usuario, PerteneceDependencia, Dependencia
# Formularios
from apps.tareas.forms import TareaForm, AsignarTareaForm
from apps.tareas.models import AsignarTarea as AsignarTarea_model
from apps.tareas.models import Tarea


class CrearTarea(CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:crear_tarea')

    def get_context_data(self, **kwargs):
        context = super(CrearTarea, self).get_context_data(**kwargs)
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        self.pertenece_dependencia = PerteneceDependencia.objects.filter(domicilio=self.usuario.domicilio,
                                                                         asignada=True)
        self.dependencia = Dependencia.objects.filter(pk__in=self.pertenece_dependencia)
        context['form'].fields['dependencia'].queryset = self.dependencia
        context['name'] = "Añadir Nueva Tarea"
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        instance.domicilio = self.usuario.domicilio
        # Pasa los minutos a horas
        instance.duracion = instance.duracion * 60
        instance.save()
        return HttpResponseRedirect(reverse_lazy('tareas:crear_tarea'))


class AsignarTarea(CreateView):
    model = AsignarTarea_model
    form_class = AsignarTareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('tareas:asignar_tarea')

    def get_context_data(self, **kwargs):
        context = super(AsignarTarea, self).get_context_data(**kwargs)
        context['name'] = "Asignar Tarea"
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        # Filtra las posibles asignaciones que pueda realizar el admin según su domicilio
        context['form'].fields['tarea'].queryset = Tarea.objects.filter(domicilio=self.usuario.domicilio,
                                                                        asignada=False)
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

        # Notifica mediante mail al usuario
        datos = Usuario.objects.get(pk=instance.usuario.pk)
        mensaje = "Hola " + datos.username + ", se te ha asignado la siguiente tarea: " + tarea.nombre + ", en " + str(tarea.dependencia) + ".\nComentarios: " + tarea.comentarios + ".\nPorfavor revisa la app.\n\nOrganizador =D"
        send_mail('Nueva asignación de tarea', mensaje, 'organizador.is2020@gmail.com', [datos.email], fail_silently=False)

        return HttpResponseRedirect(reverse_lazy('tareas:asignar_tarea'))


# vista para modificar las propiedades de una tarea, no modifica la asignacion de esta tarea.
class ModificarTarea(UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'tareas/modificar_tarea.html'
    success_url = reverse_lazy('tareas:listar_tareas_asignadas')

    def get_context_data(self, **kwargs):
        context = super(ModificarTarea, self).get_context_data(**kwargs)
        context['name'] = "Modificar Tarea"
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Tarea, id=id_)


class EliminarTarea(DeleteView):
    model = Tarea
    template_name = 'tareas/modificar_tarea.html'
    success_url = reverse_lazy('tareas:listar_tareas_asignadas')

    def get_context_data(self, **kwargs):
        context = super(EliminarTarea, self).get_context_data(**kwargs)
        context['name'] = "Eliminar Tarea"
        return context

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Tarea, id=id_)


class ListarTarea(ListView):
    model = Tarea
    template_name = 'tareas/listar_tareas.html'

    def get_queryset(self):
        # Toma la id de usuario almacenada
        pk_usuario = self.request.session.get('pk_usuario', '')
        # Intancia el objeto usuario
        usuario = Usuario.objects.get(pk=pk_usuario)
        usuarios = Usuario.objects.filter(domicilio=usuario.domicilio)
        # Retorna las tareas filtradas según domicilio, indicando las correspondiente al usuario en session
        return AsignarTarea_model.objects.filter(usuario__in=usuarios, usuario=usuario)


class ListarTareaAsignada(ListView):
    model = Tarea
    template_name = 'tareas/listar_tareas_asignadas.html'

    def get_queryset(self):
        # Toma la id de usuario almacenada
        pk_usuario = self.request.session.get('pk_usuario', '')
        # Intancia el objeto usuario
        usuario = Usuario.objects.get(pk=pk_usuario)
        usuarios = Usuario.objects.filter(domicilio=usuario.domicilio)
        # Retorna las tareas asignadas filtradas según domicilio
        return AsignarTarea_model.objects.filter(usuario__in=usuarios)
