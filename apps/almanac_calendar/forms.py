from django import forms
from .models import Event


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
