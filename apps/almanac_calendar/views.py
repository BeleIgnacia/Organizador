from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from .forms import EventForm
from .models import Event
from apps.tareas.models import Tarea, AsignarTarea
from apps.hogar.models import Usuario

import json

# Create your views here.


def add_event(request):
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=201)
        return render(request, 'almanac_calendar/index.html', context={'form': form})
    return render(request, 'almanac_calendar/index.html', context={'form': EventForm()})


def MostrarCalendario(request):
    tareas_asignadas = Tarea.objects.filter(asignada=True)
    lista_tareas = []
    for tareas in tareas_asignadas:
        lista_tareas.append(tareas)
    event = Event.objects.all()
    event.delete()
    for tareas in lista_tareas:
        event = Event.objects.create(title=tareas.nombre)
    event = Event.objects.all()
    events = eval(serializers.serialize("json", event))
    events = list(map(lambda x: x['fields'], events))
    return render(request, 'almanac_calendar/calendar.html', context={'events': events})


def events_list(request):
    print('in events lists')
    events = Event.objects.all()
    return JsonResponse(list(map(lambda x: model_to_dict(x), events)), safe=False)
