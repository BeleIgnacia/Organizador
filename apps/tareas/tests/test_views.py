from django.test import TestCase, Client
from django.urls import reverse

from apps.tareas.models import *

import json

class TestViews_tareas(TestCase):

    def setUp(self):
        self.client = Client()
        #
        self.crear_tarea_url = reverse('tareas:crear_tarea')
        self.asignar_tarea_url = reverse('tareas:asignar_tarea')
        #
        self.listar_tarea_url = reverse('tareas:listar_tareas')
        self.listar_asignada_tarea_url = reverse('tareas:listar_tareas_asignadas')
        
        # 
        ## https://stackoverflow.com/questions/48814830/how-to-test-djangos-updateview
        # self.modificar_tarea_url = reverse('tareas:editar_tarea')
        # self.eliminar_tarea_url = reverse('tareas:elimnar_tarea')

    def test_crear_tarea(self):
        pass
    
    def test_asignar_tarea(self):
        pass
    
    def test_listar_tarea(self):
        # response = self.client.get(self.listar_tarea_url)

        # self.assertEquals(response.status_code, 200)
        # self.assertTemplateUsed(response, 'tareas/listar_tareas.html')
        pass
    
    
    def test_listar_asignada_tarea(self):
        pass
    
    def test_modificar_tarea(self):
        pass
    
    def test_eliminar_tarea(self):
        pass
