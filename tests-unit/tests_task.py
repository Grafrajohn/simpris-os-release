# Django imports
from django.test import TestCase, RequestFactory, Client
from django.contrib.auth.models import User
from django.test.client import Client

# Simpris imports
from .unit_configuration import TestConfig
from simpris.apps.task.views import tasklist, history, detail, edit


class TaskTests(TestCase):

    def setUp(self):
        test_config = TestConfig()
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.create_superuser(username='user-name', email='user-name@gmail.com', password='password')
        self.client.login(username='user-name', password='password')

    # test task index page
    def test_index(self):
        response = self.client.get('/task/list/', follow=True)
        #request.user = self.user
        #request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbTaskIndex')

    # test task index page
    def test_detail(self):
        response = self.client.get('/task/detail/1/', follow=True)
        #request.user = self.user
        #request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task Overview')

