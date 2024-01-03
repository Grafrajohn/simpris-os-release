from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Programme
from simpris.models.db_views import VUserContextFull


class programmeAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'programme.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api programme delete
    def test_delete(self):
        url = ('/api/programme/delete/1/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api programme insert
    def test_insert(self):
        url = ('/api/programme/insert/')
        data = {'frmProgrammeName': 'name',
            'frmProgrammeDescription': 'desc'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api programme list
    def test_list(self):
        url = ('/api/programme/programmes/')
        #data = {'hidprogrammeID': '1', 'frmprogrammeName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api programme update
    def test_update(self):
        url = ('/api/programme/update/')
        data = {'hidProgrammeID': '1',
                'frmProgrammeName': 'Test Company Ltd',
                'frmProgrammeDescription': 'Desc'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
