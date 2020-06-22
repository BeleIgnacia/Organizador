from django import forms

# Modelos
from apps.tareas.models import Tarea, AsignarTarea
from apps.hogar.models import Usuario


class AsignarTareaForm(forms.ModelForm):
    class Meta:
        model = AsignarTarea

        fields = [
            'tarea',
            'usuario',
        ]

        labels = {
            'tarea': 'Tarea',
            'usuario': 'Usuario',
        }

        widgets = {
            'tarea': forms.Select(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea

        fields = [
            'nombre',
            'complejidad',
            'duracion',
            'dependencia',
            'comentarios'
        ]

        labels = {
            'nombre': 'Nombre',
            'complejidad': 'Complejidad',
            'duracion': 'Duración en hh:mm',
            'dependencia': 'Dependencia',
            'comentarios': 'Comentarios',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'complejidad': forms.NumberInput(attrs={'class': 'custom-range', 'type': 'range', 'max': 5, 'min': 1, 'step': 1, 'list': 'tickmarks'}),
            'duracion': forms.TimeInput(attrs={'class': 'form-control','type': 'time','value': '0'}),
            'dependencia': forms.Select(attrs={'class': 'form-control'}),
            'comentarios': forms.TextInput(attrs={'class': 'form-control'}),
        }
