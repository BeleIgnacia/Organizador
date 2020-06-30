from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.hogar.models import *
import json


# Status codes
# https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        # urls
        self.register_url = reverse('register')
        self.login_url = reverse('login')

    def test_Register(self):
        # Verifica template
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogar/register.html')

        # Verifica el post
        response = self.client.post(self.register_url, {
            'username': 'UsuarioTest',
            'email': 'usuario@test.com',
            'password1': 'PassTest',
            'password2': 'PassTest',
            'telefono': 111111111,
            'calle': 'CalleTest',
            'numero': 112,
            'comuna': 'ComunaTest',
            'ciudad': 'CiudadTest'
        })
        # 302 para HttpResponseRedirect
        self.assertEquals(response.status_code, 302)

    def test_loginUser(self):
        # Verifica template
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'hogar/login.html')

        # Verifica el post
        Usuario.objects.create(
            user=User.objects.create(
                username='UsuarioTest',
                email='usuario@test.com',
                password='PassTest',
            ),
            telefono=111111111,
            domicilio=Domicilio.objects.create(
                calle='CalleTest',
                numero=112,
                comuna='ComunaTest',
                ciudad='CiudadTest',
            ),
        )

        response = self.client.post(self.login_url, {
            'username': 'UsuarioTest',
            'password': 'PassTest'
        })

        #Aqui debo comparar estos
        #self.assertEquals(Usuario.objects.get(username='UsuarioTest').username,'PassTest')
        #Este aún no funciona bien 200 302
        #Debe enviar un 302 pero recibe un 200
        self.assertEquals(response.status_code, 302)
