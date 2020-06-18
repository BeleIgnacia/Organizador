from django.urls import path
from apps.interfaz.views import Home, Nosotros, Ayuda, Contacto

urlpatterns = [
    path('', Home.as_view()),
	path('nosotros/', Nosotros.as_view()),
	path('ayuda/', Ayuda.as_view()),
	path('contacto/', Contacto.as_view()),
]