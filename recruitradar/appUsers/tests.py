# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import ExperienciaLaboral, Educacion, Skills, Idiomas, DataUsuario
from django.contrib.auth.models import User
from .models import Idiomas

from django.contrib.auth.models import User

class TestLoginRequestView(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()

    def test_login_request_exitoso(self):

        response = self.client.post(reverse('Login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.client.session['_auth_user_id'])



    def test_login_request_fallido(self):

        response = self.client.post(reverse('Login'), {'username': 'testuser', 'password': 'incorrectpass'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.client.session.get('_auth_user_id'))


    def test_login_request_primera_vez(self):

        response = self.client.get(reverse('Login'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('miFormulario', response.context)

class TestPerfilView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.experiencia = ExperienciaLaboral.objects.create(user=self.user, 
                                                             empresa="Empresa de Prueba", 
                                                             cargo="Puesto de Prueba",
                                                             periodo_inicio=2020,
                                                             periodo_fin=2023,
                                                             description="ss",
                                                             pais="venezuela")
        self.educacion = Educacion.objects.create(user=self.user, 
                                                  institucion="Institución de Prueba", 
                                                  titulo="Título de Prueba", 
                                                  periodo_inicio=2020,
                                                             periodo_fin=2023,
                                                             description="ss",pais="venezuela")

    def test_perfil_vista(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('Perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Empresa de Prueba")
        self.assertContains(response, "Puesto de Prueba")
        self.assertContains(response, "Institución de Prueba")
        self.assertContains(response, "Título de Prueba")
        self.assertIsNotNone(response.context['experiencias'])
        self.assertIsNotNone(response.context['estudios'])
        self.assertIsNotNone(response.context['idiomas'])
        self.assertIsNotNone(response.context['perfil'])
        self.assertIsNotNone(response.context['skills'])
        self.assertEqual(response.context['avatar'], 'none')


    