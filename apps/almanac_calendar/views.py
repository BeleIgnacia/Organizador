from django.shortcuts import render, redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .forms import EventForm
from .models import Event
from apps.tareas.models import Tarea, AsignarTarea
from apps.hogar.models import Usuario
import json


def add_event(request):
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return render(request, 'almanac_calendar/index.html', context={'form': form})
    return render(request, 'almanac_calendar/index.html', context={'form': EventForm()})


def MostrarCalendario(request):
    all_events = Event.objects.all()
    all_events.delete()
    tareas_asignadas = Tarea.objects.filter(asignada=True)
    lista_tareas = []
    for asignadas in tareas_asignadas:
        lista_tareas.append(asignadas)
    for object in lista_tareas:
        new_event = Event.objects.create(title=object.nombre)
        print(new_event)
    all_events = Event.objects.all()
    events = eval(serializers.serialize("json", all_events))
    events = list(map(lambda x: x['fields'], events))
    tareas = ListarTareasUsuario(request)
    context = {'events': events,
               'tareas': tareas}
    return render(request, 'almanac_calendar/calendar.html', context)


def ListarTareasUsuario(request):
    pk_usuario = request.session.get('pk_usuario', '')
    usuario = Usuario.objects.get(pk=pk_usuario)
    asignadas = AsignarTarea.objects.filter(usuario=pk_usuario)
    tareas = []
    for asignadas in asignadas.values('tarea_id'):
        tareas.append(Tarea.objects.get(pk=asignadas['tarea_id']))
    return tareas


def events_list(request):
    print('in events lists')
    events = Event.objects.all()
    return JsonResponse(list(map(lambda x: model_to_dict(x), events)), safe=False)
