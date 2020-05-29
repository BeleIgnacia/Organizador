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
            'duracion' : 'Duracion',
            'encargado': 'Encargado',
        }

        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'Nombre Tarea'}),
            'complejidad': forms.TextInput(attrs={'placeholder':'Complejidad Tarea'}),
            'duracion' : forms.TextInput(attrs={'placeholder':'Duracion Aproximada Tarea'}),
            'encargado': forms.Select(attrs={'class':'form-control'})
        }