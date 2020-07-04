from django import forms
from .models import Event
from apps.almanac_calendar.models import Horario_Ocupado


class EventForm(forms.ModelForm):
    class Meta:
        model = Event

        fields = [
            'asignar_tarea',
            'start',
        ]

        widgets = {
            'asignar_tarea': forms.Select(attrs={'class': 'form-control'}),
            'start': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }

class Horario_OcupadoForm(forms.ModelForm):
    class Meta:
        model = Horario_Ocupado

        fields = [
            'start',
            'end',
            'titulo',
            'repetir',
        ]

        labels = {
            'start': 'Hora de inicio',
            'end': 'Hora de termino',
            'titulo': '¿Qué haces a esta hora?',
            'repetir': '¿Repetir todas las semanas?',
        }

        widgets = {
            'start': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'end': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(),
            'repetir': forms.CheckboxInput(),
        }
