from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    #path('', add_event),
    #path('view', calendar),
    path('eventslist', events_list),
    path('mostrar', MostrarCalendario, name='mostrar_calendario'),
]
