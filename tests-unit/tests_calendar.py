# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.calendartab.views import calendartab


class calendarTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test calendar list page
    def test_calendartab(self):
        request = self.factory.get('/time/calendar')
        request.user = self.user

        response = calendartab(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div id="calendar"></div>')




