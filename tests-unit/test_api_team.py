from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.models.models import Team
from simpris.models.db_views import VUserContextFull


class TeamAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'team.json',
                'teamuser.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api team delete
    def test_delete(self):
        url = ('/api/team/delete/1/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api team insert
    def test_insert(self):
        url = ('/api/team/insert/')
        data = {'frmTeamName': 'name',
            'frmTeamDescription': 'desc'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api team list
    def test_list(self):
        url = ('/api/team/list/')
        #data = {'hidteamID': '1', 'frmteamName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api team member insert
    def test_member_create(self):
        url = ('/api/team/member_create/')
        data = {'hidTeamID': 1,
            'selTeamMember': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api team member delete
    def test_member_delete(self):
        url = ('/api/team/member_delete/')
        data = {'id': 1,
            'team_id': 1,
            'team_member_id': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api team update
    def test_update(self):
        url = ('/api/team/update/')
        data = {'hidTeamID': 1,
            'frmTeamName': 1,
            'frmTeamDescription': 'desc'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
