from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from apps.tareas.forms import TareaForm
from apps.tareas.models import Tareas

# Create your views here.

class TareasCreate(CreateView):
    model = Tareas
    form_class = TareaForm
    template_name = 'tareas/tarea_form.html'
    success_url = reverse_lazy('/')