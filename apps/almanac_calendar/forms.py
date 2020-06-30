from django.forms import ModelForm, DateInput, DateTimeInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event

        fields = [
            'start',
        ]

        widgets = {
            'start': DateTimeInput(attrs={'class':'form-control'}),
        }
