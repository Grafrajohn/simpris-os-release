# Create your tests here.
from django.http import HttpResponsePermanentRedirect
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.system.views import index


class AccountTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test auth logon page
    def test_index(self):
        request = self.factory.get('/system/index')
        request.user = self.user

        response = index(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Recent signups')
