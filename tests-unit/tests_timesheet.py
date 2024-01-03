# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.time.views import timesheet


class timesheetTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test timesheet list page
    def test_timesheet(self):
        request = self.factory.get('/time/timesheet')
        request.user = self.user

        response = timesheet(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Timesheet for:')
