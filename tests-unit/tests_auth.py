# Create your tests here.
from django.http import HttpResponsePermanentRedirect
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.auth.views import logon, logoff


class authTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test auth logon page
    def test_logon(self):
        request = self.factory.get('/auth/login')
        request.user = self.user

        response = logon(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div>Please login with your email/username and password below.</div>')

    # test auth logoff page
    def test_logoff(self):
        request = self.client.get('/auth/logoff', follow=True)
        request.user = self.user

        request.session = self.client.session

        response = logoff(request)

        self.assertFalse(isinstance(response, HttpResponsePermanentRedirect))
        #self.assertContains(response.get('location'), '/auth/logon')
        self.assertEqual(response.status_code, 302)
        #self.assertContains(response.url, '/auth/logon')

