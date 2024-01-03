from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Tasklist
from simpris.models.db_views import VUserContextFull


class TasklistAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'organisation.json',
                'project.json',
                'tasklist.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api tasklist delete
    def test_delete(self):
        url = ('/api/tasklist/delete/')
        data = {'tasklist_id': 1, 'project_id': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api tasklist insert
    def test_insert(self):
        url = ('/api/tasklist/insert/')
        data = {'frmTaskListName': 'name',
            'frmTaskListDescription': 'desc',
            'hidProjectID': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api tasklist update
    def test_update(self):
        url = ('/api/tasklist/update/')
        data = {'hidTasklistID': 1,
            'hidProjectID': 1,
            'frmTaskListName': 'name',
            'frmTaskListDescription': 'desc'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
