from django import forms

# Modelos
from apps.tareas.models import Tarea,AsignarTarea

class AsignarTareaForm(forms.ModelForm):
    class Meta:
        model = AsignarTarea

        fields = [
            'tarea',
            'usuario',
        ]
        
        labels = {
            'tarea' : 'Tarea',
            'usuario' : 'Usuario',
        }

        widgets = {
            'tarea' : forms.Select(attrs={'class':'form-control'}),
            'usuario' : forms.Select(attrs={'class':'form-control'}),
        }

class TareaForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(TareaForm,self).__init__(*args,**kwargs)
        # Cambia el valor incial del widget a 1
        '''
            Esto unicamente es para que la forma sea valida, el valor que
            se le asigne en el widget será reemplazado en la view.
        '''
        self.fields['domicilio'].initial = '1'

    class Meta:
        model = Tarea

        fields =[
            'nombre',
            'domicilio',
            'complejidad',
            'duracion',
            'lugar',
            'comentarios'
    #        'encargado',
        ]
        labels =  {
            'nombre' : 'Nombre',
            'domicilio' : 'Domicilio',
            'complejidad' : 'Complejidad',
            'duracion' : 'Duración en horas',
            'lugar' : 'Dependencia',
            'comentarios' : 'Comentarios',
    #        'encargado': 'Encargado',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'complejidad':forms.NumberInput(attrs={'class':'custom-range','type':'range','max':5,'min':1,'step':1,'list':'tickmarks'}),
            'duracion':forms.TextInput(attrs={'class':'form-control'}),
            'lugar':forms.TextInput(attrs={'class':'form-control'}),
            'comentarios':forms.TextInput(attrs={'class':'form-control'}),
            'domicilio':forms.Select(attrs={'hidden':True,'value':1})
        #    'encargado':forms.Select(attrs={'class':'form-control'}),
        }
