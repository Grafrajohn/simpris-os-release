# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.administration.views import home


class adminTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test admin home page
    def test_home(self):
        request = self.factory.get('/admin/home')
        request.user = self.user

        response = home(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h3>Information for Administrators</h3>')
