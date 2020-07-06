from datetime import timedelta

from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib import messages

from apps.almanac_calendar.forms import Horario_OcupadoForm
from apps.hogar.models import Usuario, Dependencia
from apps.tareas.models import Tarea, AsignarTarea
from .forms import EventForm
from .models import Event


class MostrarCalendario(CreateView):
    model = Event
    template_name = 'almanac_calendar/calendar.html'
    form_class = EventForm
    success_url = reverse_lazy('calendario:mostrar_calendario')

    def get_context_data(self, **kwargs):
        context = super(MostrarCalendario, self).get_context_data(**kwargs)

        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        # Determina usuarios de domicilio
        self.usuarios = Usuario.objects.filter(domicilio=self.usuario.domicilio)
        # Filtra las tareas asignadas al domicilio con candelarizar
        self.tareas = AsignarTarea.objects.filter(usuario__in=self.usuarios, calendarizar=True)
        self.events = Event.objects.filter(asignar_tarea__in=self.tareas)
        self.events = eval(serializers.serialize("json", self.events))
        self.events = list(map(lambda x: x['fields'], self.events))
        # Filtra las tareas asignadas al domicilio sin candelarizar
        self.tareas = AsignarTarea.objects.filter(usuario__in=self.usuarios, calendarizar=False)

        context['form'].fields['asignar_tarea'].queryset = self.tareas
        context['events'] = self.events
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        # Asigna titulo, termino y descripción al evento
        instance.title = instance.asignar_tarea.tarea.nombre
        instance.end = instance.start + instance.asignar_tarea.tarea.duracion
        instance.description = instance.asignar_tarea.tarea.comentarios
        instance.asignar_tarea.calendarizar = True

        # Verifica si dependencia no esta ocupada
        self.usuario = Usuario.objects.get(pk=self.request.session['pk_usuario'])
        self.usuarios = Usuario.objects.filter(domicilio=self.usuario.domicilio)
        self.tareas = AsignarTarea.objects.filter(usuario__in=self.usuarios, calendarizar=True)
        self.events = Event.objects.filter(asignar_tarea__in=self.tareas)
        # Si hay un evento que se solape con instance
        # caso 1: event comienza antes y acaba antes de instance
        # caso 2: event comienza luego y acaba luego de instance
        # caso 3: event comienza luego y acaba antes de instance
        dependencia_disponible = True
        for event in self.events:
            if event.asignar_tarea.tarea.dependencia == instance.asignar_tarea.tarea.dependencia:
                if event.start < instance.start < event.end < instance.end:
                    dependencia_disponible = False
                    # print("caso 1")
                if instance.start < event.start < event.end < instance.end:
                    dependencia_disponible = False
                    # print("caso 2")
                if instance.start < event.start < instance.end < event.end:
                    dependencia_disponible = False
                    # print("caso 3")
        if not dependencia_disponible:
            # return HttpResponseRedirect(reverse_lazy('calendario:mostrar_calendario', kwargs={}))
            # return HttpResponseRedirect(reverse('calendario:mostrar_calendario', kwargs={}))
            print("Ya hay otra tarea en esa dependencia")
            return HttpResponseRedirect(reverse_lazy('calendario:mostrar_calendario'))

        instance.asignar_tarea.save()
        instance.save()
        return HttpResponseRedirect(reverse_lazy('calendario:mostrar_calendario'))


def ListarTareasUsuario(request):
    pk_usuario = request.session.get('pk_usuario', '')
    usuario = Usuario.objects.get(pk=pk_usuario)
    asignadas = AsignarTarea.objects.filter(usuario=pk_usuario)
    tareas = []
    for asignadas in asignadas.values('tarea_id'):
        tareas.append(Tarea.objects.get(pk=asignadas['tarea_id']))
    return tareas


def Horario_Ocupado_View(request):
    if request.method == 'POST':
        form = Horario_OcupadoForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['start'] > form.cleaned_data['end']:
                messages.error(request, 'La hora de termino debe ser despues que la hora de inicio!!!')
                return render(request, 'hogar/../../templates/almanac_calendar/horario_ocupado.html', {'form': form})
            pk_usuario = request.session.get('pk_usuario', '')
            usuario = Usuario.objects.get(pk=pk_usuario)
            dur = timedelta()

            dependencia = Dependencia.objects.create(
                nombre="nulo"
            )

            tarea = Tarea.objects.create(
                nombre=form.cleaned_data['titulo'],
                domicilio=usuario.domicilio,
                dependencia=dependencia,
                duracion=dur,
                asignada=True
            )

            asignar_tarea = AsignarTarea.objects.create(
                tarea=tarea,
                usuario=usuario,
                calendarizar=True
            )
            if form.cleaned_data['repetir'] == True:
                for i in range(10):
                    Event.objects.create(
                        title=form.cleaned_data['titulo'],
                        asignar_tarea=asignar_tarea,
                        start=form.cleaned_data['start'] + timedelta(weeks=i),
                        end=form.cleaned_data['end'] + timedelta(weeks=i)
                    )
            else:
                Event.objects.create(
                    title=form.cleaned_data['titulo'],
                    asignar_tarea=asignar_tarea,
                    start=form.cleaned_data['start'],
                    end=form.cleaned_data['end']
                )
            return HttpResponseRedirect(reverse_lazy('calendario:agregar_horario_ocupado'))
    else:
        form = Horario_OcupadoForm()
    return render(request, 'hogar/../../templates/almanac_calendar/horario_ocupado.html', {'form': form})
