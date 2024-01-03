from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.models.models import Account
from simpris.models.db_views import VSchedule


class ScheduleAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'vschedule.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api schedule move
    def test_move(self):
        url = ('/api/schedule/move/')
        data = {'task_id': 1, 'phase_id': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
