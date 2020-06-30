from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.hogar.views import *


class TestUrls(SimpleTestCase):
    #urls de organizador
    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, Register)

    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, loginUser)

    #urls de hogar
    def test_dashboard_url_is_resolved(self):
        url = reverse('hogar:dashboard')
        self.assertEquals(resolve(url).func.view_class, Dashboard)

    def test_list_usuarios_url_is_resolved(self):
        url = reverse('hogar:list_usuarios')
        self.assertEquals(resolve(url).func.view_class, Usuariolist)

    def test_añadir_url_is_resolved(self):
        url = reverse('hogar:añadir')
        self.assertEquals(resolve(url).func.view_class, RegisterUser)

    def test_domicilio_modificar_url_is_resolved(self):
        url = reverse('hogar:domicilio_modificar')
        self.assertEquals(resolve(url).func.view_class, DomicilioModificar)

    def test_domicilio_dependencias_url_is_resolved(self):
        url = reverse('hogar:domicilio_dependencias')
        self.assertEquals(resolve(url).func.view_class, DomicilioDependencias)
