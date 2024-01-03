from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Account
from simpris.models.db_views import VUserContextFull


class UtilityAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api utility list
    # def test_logerror(self):
    #     url = ('/api/utility/logerror/')
    #     #data = {'hidutilityID': '1', 'frmutilityName': 'Test Company Ltd'}
    #     self.client.force_authenticate(user=self.user)
    #
    #     response = self.client.post(url)
    #
    #     self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
