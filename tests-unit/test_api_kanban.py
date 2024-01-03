from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.api.kanban.views import insert, move


class KanbanAPITests(TestCase):
    fixtures = ['account.json',
                'board.json',
                'User.json',
                'vusercontextfull.json',
                'organisation.json',
                'userorganisation.json',
                'client.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api kanban insert
    def test_insert(self):
        url = ('/api/kanban/insert/')
        data = {'column_id': '1',
            'item_type': 1,
            'item_id':'1',
            'source_column': '1'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api kanban move
    def test_move(self):
        url = ('/api/kanban/move/')
        data = {'column_id': '1',
            'item_type': '1',
            'item_id': '1',
            'source_column': '1'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
