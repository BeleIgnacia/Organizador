from django.views.generic import TemplateView
from django.shortcuts import render
from random import randrange

class Home(TemplateView):
	template_name = 'interfaz/home.html'

	def get_context_data(self,**kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['content'] = "home_content"
		return context

class Nosotros(TemplateView):
	template_name = 'interfaz/home.html'

	def get_context_data(self,**kwargs):
		context = super(Nosotros, self).get_context_data(**kwargs)
		context['content'] = "nosotros_content"
		return context

class Ayuda(TemplateView):
	template_name = 'interfaz/home.html'

	def get_context_data(self,**kwargs):
		context = super(Ayuda, self).get_context_data(**kwargs)
		context['content'] = "ayuda_content"
		return context

class Contacto(TemplateView):
	template_name = 'interfaz/home.html'

	def get_context_data(self,**kwargs):
		context = super(Contacto, self).get_context_data(**kwargs)
		context['content'] = "contacto_content"
		return context

