from django.urls import path

from apps.inicio.views import index_inicio

urlpatterns = [
    path('', index_inicio,name='inicio'),
]