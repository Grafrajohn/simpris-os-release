from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.api.account.views import auto


class AccountAPITests(TestCase):
    fixtures = ['account.json',
                'User.json',
                #'vusercontextfull.json',
                'organisation.json',
                'userorganisation.json',
                'client.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api account auto
    def test_auto_fail_no_security_data(self):
        url = ('/api/account/auto/')
        data = {}

        try:
            self.client.post(url, data)
            self.fail('Should not have got this far with bad post data')
        except ValueError:
            pass

    # test api account auto
    def test_auto(self):
        url = ('/api/account/auto/')
        data = {'security_data': 4,
                'security_hash': 1,
                'SubscriptionReferrer': '1-123456788',
                'subscription.customer.firstName': 'Fred',
                'subscription.customer.lastName': 'Bloggs'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
