# Create your tests here.
from django.http import HttpResponsePermanentRedirect
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.account.views import upgrade


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
    def test_upgrade(self):
        request = self.factory.get('/account/upgrade')
        request.user = self.user

        response = upgrade(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Upgrade your Simpris account!')
