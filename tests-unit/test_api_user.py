from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.models.models import Users
from simpris.models.db_views import VUserContextFull


class UserAPITests(TestCase):
    fixtures = ['account.json',
                'auth_user.json',
                'auth_group',
                'client.json',
                'organisation.json',
                'User.json',
                'users.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api user delete
    def test_delete(self):
        url = ('/api/user/delete/1/')
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api user delete yourself
    def test_delete_yourself(self):
        url = ('/api/user/delete/4/')
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 400)

    # test api user insert
    def test_insert(self):
        url = ('/api/user/insert/')
        data = {'frmUsername': 'name',
            'frmOrganisation': 1,
            'frmFirstName': 'name',
            'frmLastName': 'last',
            'frmEmail': 'me@simpris12345.com',
            'frmPhone': '16273839300',
            'frmPassword': 'password',
            'frmPasswordConfirm': 'password'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api user list
    def test_detail(self):
        url = ('/api/user/detail/')
        data = {'hiduserID': '1', 'frmuserName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api user list
    def test_list(self):
        url = ('/api/user/users/')
        #data = {'hiduserID': '1', 'frmuserName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api user profile
    def test_profile(self):
        url = ('/api/user/profile/')
        data = {'frmEmail': 'user-name@gmail.com', 'frmPhone': '12345569660'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api user update
    def test_update(self):
        url = ('/api/user/update/')
        data = {'hidUserID': 4,
            'frmUsername': 'user-name',
            'frmOrganisation': 1,
            'frmFirstName': 'first',
            'frmLastName': 'last',
            'frmEmail': 'user-name@gmail.com',
            'frmPhone': '1516172829',
            'frmProjectMngr': 1,
            'frmVIP': 'y',
            'frmPayRate': 1,
            'frmTaxRate': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api user password update
    def test_password(self):
        url = ('/api/user/password/')
        data = {'hidUserID': 1,
            'frmUsername': 'username',
            'frmOrganisation': 1,
            'frmFirstName': 'first',
            'frmLastName': 'last',
            'frmEmail': 'email12345@simpris.com',
            'frmPhone': '1516172829',
            'frmProjectMngr': 1,
            'frmVIP': 'y',
            'frmPayRate': 1,
            'frmTaxRate': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
