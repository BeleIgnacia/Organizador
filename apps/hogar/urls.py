from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    #URLs para administrar usuarios del hogar
    path('usuarios/listar', views.Usuariolist.as_view(), name='list_usuarios'),
    path('usuarios/agregar', views.RegisterUser.as_view(), name='añadir'),
    path('usuarios/editar/<int:pk>', views.UsuarioModificar.as_view(), name='editar'),
    #URLs para administrar domicilio
    path('domicilio/modificar', views.DomicilioModificar.as_view(), name='domicilio_modificar'),
    path('domicilio/dependencias', views.DomicilioDependencias.as_view(), name='domicilio_dependencias'),
]
