from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    #URLs para administrar usuarios del hogar
    path('usuarios/listar', views.Usuariolist.as_view(), name='list_usuarios'),
    path('usuarios/agregar', views.RegisterUser.as_view(), name='añadir'),
]
