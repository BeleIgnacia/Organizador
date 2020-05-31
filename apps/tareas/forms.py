from django import forms
from apps.tareas.models import Tarea

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
