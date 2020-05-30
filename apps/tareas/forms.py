from django import forms
from apps.tareas.models import Tareas

class TareaForm(forms.ModelForm):
    

    class Meta:
        model = Tareas

        fields =[
            'nombre',
            'complejidad',
            'duracion',
            'encargado',
        ]
        labels =  {
            'nombre' : 'Nombre',
            'complejidad' : 'Complejidad',
            'duracion' : 'Duración en horas',
            'encargado': 'Encargado',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'complejidad':forms.NumberInput(attrs={'class':'custom-range','type':'range','max':5,'min':1,'step':1,'list':'tickmarks'}),
            'duracion':forms.TextInput(attrs={'class':'form-control'}),
            'encargado':forms.Select(attrs={'class':'form-control'}),
        }