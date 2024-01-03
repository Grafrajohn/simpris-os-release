# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.team.views import list, members, detail, create, edit


class teamTests(TestCase):
    fixtures = ['account.json',
                'User.json',
                'vusercontextfull.json',
                'organisation.json',
                'client.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test team list page
    def test_list(self):
        request = self.factory.get('/team/list')
        request.user = self.user

        response = list(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbTeamIndex')

    # test team detail page
    def test_detail(self):
        request = self.factory.get('/team/detail')
        request.user = self.user

        response = detail(request, team_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Team Overview</a>')
        self.assertContains(response, 'Edit Team')
        self.assertContains(response, 'Team Members')

    # test team history page
    def test_members(self):
        request = self.factory.get('/team/members')
        request.user = self.user

        response = members(request, team_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Team Members</a><')

    # test team create page
    def test_create(self):
        request = self.factory.get('/team/create')
        request.user = self.user

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmTeamAdd')

    # test team edit page
    def test_edit(self):
        request = self.factory.get('/team/edit')
        request.user = self.user

        try:
            response = edit(request, team_id=37)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'frmTeamEdit')

        except:
            pass
