import time
from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Phase
from simpris.models.db_views import VUserContextFull

from simpris.api.phase.views import phaselist, insert, delete, update


class PhaseAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'phase.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api phase delete
    def test_delete(self):
        url = ('/api/phase/delete/4/')
        self.client.login(username='user-name', password='password')
        #self.client.force_authenticate(user=self.user)

        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, 200)

    # test api phase insert
    def test_insert(self):
        self.client.login(username='user-name', password='password')
        url = ('/api/phase/insert/')
        data = {'frmPhaseName': 'phase name',
        'frmPhaseDescription': 'phase desc',
        'frmDatePicker': '2015-08-06',
        'frmDatePicker2': '2015-09-06'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api phase list
    def test_list(self):
        url = ('/api/phase/list/')
        #data = {'hidphaseID': '1', 'frmphaseName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api phase update
    def test_update(self):
        url = ('/api/phase/update/')
        data = {'hidPhaseID': '1',
            'frmPhaseName': 'phase name',
            'frmPhaseDescription': 'phase desc',
            'frmDatePicker': '2016-12-02',
            'frmDatePicker2': '2016-12-30'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
