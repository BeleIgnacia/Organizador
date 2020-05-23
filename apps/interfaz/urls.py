from django.urls import path

from apps.interfaz.views import home

urlpatterns = [
    path('', home, name='inicio'),
]