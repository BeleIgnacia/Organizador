from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from apps.tareas.forms import TareaForm
from apps.tareas.models import Tareas, Usuario
from django.contrib import messages

# Create your views here.


class crear_tarea(CreateView):
    model = Tareas
    form_class = TareaForm
    template_name = 'tareas/crear_tarea.html'
    success_url = reverse_lazy('tareas:crear_tarea')


class asignar_tarea(CreateView):
    model = Tareas
    form_class = TareaForm
    template_name = 'tareas/asignar_tarea.html'
    success_url = reverse_lazy('')


class listar_tareas(ListView):
    model = Tareas
    template_name = 'tareas/listar_tareas.html'
