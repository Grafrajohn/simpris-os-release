from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.db_views import VUserContextFull

from simpris.api.organisation.views import insert, update, delete, organisations, adduser, deleteuser


class OrganisationAPITests(TestCase):
    fixtures = ['account.json',
                'User.json',
                'vusercontextfull.json',
                'organisation.json',
                'userorganisation.json',
                'client.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api organisation delete
    def test_delete(self):
        url = ('/api/organisation/delete/4/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'tbOrganisationIndex')

    # test api organisation insert
    def test_insert(self):
        url = ('/api/organisation/insert/')
        data = {'hidOrganisationID': '1', 'frmOrganisationName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'tbOrganisationIndex')

    # test api organisation list
    def test_list(self):
        url = ('/api/organisation/organisations/')
        #data = {'hidOrganisationID': '1', 'frmOrganisationName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'tbOrganisationIndex')

    # test api organisation update
    def test_update(self):
        url = ('/api/organisation/update/')
        data = {'hidOrganisationID': '1', 'frmOrganisationName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'tbOrganisationIndex')

    # test api organisation add user
    def test_add_user(self):
        url = ('/api/organisation/adduser/')
        data = {'hidUserOrganisationID': 1, 'selOrganisationUser': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'tbOrganisationIndex')

    # test api organisation delete user
    def test_delete_user(self):
        url = ('/api/organisation/deleteuser/')
        data = {'hidUserOrganisationID': 1, 'organisation_user_id': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'tbOrganisationIndex')

    def tearDown(self):
        self.client.logout()
