from django.views.generic import TemplateView
from django.shortcuts import render
from random import randrange

class Home(TemplateView):
	template_name = 'interfaz/home.html'

class Nosotros(TemplateView):
	template_name = 'interfaz/nosotros.html'

class Ayuda(TemplateView):
	template_name = 'interfaz/ayuda.html'

class Contacto(TemplateView):
	template_name = 'interfaz/contacto.html'

