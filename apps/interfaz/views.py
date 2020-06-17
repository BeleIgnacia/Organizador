from django.views.generic import TemplateView
from django.shortcuts import render
from random import randrange

class Home(TemplateView):
	template_name = 'interfaz/home.html'