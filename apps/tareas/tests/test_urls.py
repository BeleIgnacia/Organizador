from django.test import SimpleTestCase
from django.urls import reverse, resolve
from apps.tareas.views import *

class TestUrls_tareas(SimpleTestCase):
    #url generales
    def test_listar_tarea_url_is_resolved(self):
        url = reverse('tareas:listar_tareas')
        self.assertEquals(resolve(url).func.view_class, ListarTarea)

    def test_listar_tarea_asignada_url_is_resolved(self):
        url = reverse('tareas:listar_tareas_asignadas')
        self.assertEquals(resolve(url).func.view_class, ListarTareaAsignada)
        
    #url administrador
    def test_crear_tarea_url_is_resolved(self):
        url = reverse('tareas:crear_tarea')
        self.assertEquals(resolve(url).func.view_class, CrearTarea)
         
    def test_asignar_tarea_url_is_resolved(self):    
        url = reverse('tareas:asignar_tarea')
        self.assertEquals(resolve(url).func.view_class, AsignarTarea)

    def test_moficar_tarea_url_is_resolved(self):
        url = reverse('tareas:editar_tarea',kwargs={"pk": 1}) #cambiar pk a generico
        self.assertEquals(resolve(url).func.view_class, ModificarTarea)

    def test_eliminar_tarea_url_is_resolved(self):
        url = reverse('tareas:elimnar_tarea',kwargs={"pk": 1}) #cambiar pk a generico
        self.assertEquals(resolve(url).func.view_class, EliminarTarea)