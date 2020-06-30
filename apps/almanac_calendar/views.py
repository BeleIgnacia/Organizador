from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.views.generic import CreateView
from .forms import EventForm
from .models import Event
from apps.tareas.models import Tarea, AsignarTarea
from apps.hogar.models import Usuario
import json
from django.urls import reverse_lazy


class MostrarCalendario(CreateView):
    model = Event
    template_name = 'almanac_calendar/calendar.html'
    form_class = EventForm
    success_url = reverse_lazy()

    def get_context_data(self, **kwargs):
        context = super(MostrarCalendario, self).get_context_data(**kwargs)
        all_events = Event.objects.all()
        events = eval(serializers.serialize("json", all_events))
        events = list(map(lambda x: x['fields'], events))
        tareas = ListarTareasUsuario(self.request)
        context['events'] = events
        context['tareas'] = tareas
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        print(instance)
        pass


"""
def add_event(request):
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return render(request, 'almanac_calendar/index.html', context={'form': form})
    return render(request, 'almanac_calendar/index.html', context={'form': EventForm()})
"""

'''
def MostrarCalendario(request):
    #se resetea el calendario
    all_events = Event.objects.all()
    all_events.delete()
    #############################
    #se piden todas las tareas asignadas a todos los usuarios
    #y luego se parsean para entregarlas en el formato válido de tipo Event al calendario
    tareas_asignadas = Tarea.objects.filter(asignada=True)
    lista_tareas = []
    for asignadas in tareas_asignadas:
        lista_tareas.append(asignadas)
    for object in lista_tareas:
        new_event = Event.objects.create(title=object.nombre)
    all_events = Event.objects.all()
    events = eval(serializers.serialize("json", all_events))
    events = list(map(lambda x: x['fields'], events))
    ##############################
    #se obtienen las tareas asignadas al usuario que esta viendo el calendario
    tareas = ListarTareasUsuario(request)
    #se entrega el contexto a la platilla
    context = {'events': events,
               'tareas': tareas}

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'almanac_calendar/calendar.html', context)
'''


def ListarTareasUsuario(request):
    pk_usuario = request.session.get('pk_usuario', '')
    usuario = Usuario.objects.get(pk=pk_usuario)
    asignadas = AsignarTarea.objects.filter(usuario=pk_usuario)
    tareas = []
    for asignadas in asignadas.values('tarea_id'):
        tareas.append(Tarea.objects.get(pk=asignadas['tarea_id']))
    return tareas


"""
def events_list(request):
    print('in events lists')
    events = Event.objects.all()
    return JsonResponse(list(map(lambda x: model_to_dict(x), events)), safe=False)
"""
