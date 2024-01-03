from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User


class ReportAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'phase.json',
                'User.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    def tearDown(self):
        self.client.logout()
