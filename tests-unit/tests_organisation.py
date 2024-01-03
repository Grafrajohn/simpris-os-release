from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client
from django.urls import reverse

from simpris.apps.organisation.views import list, history, detail, create, edit


class OrganisationTests(TestCase):
    fixtures = ['User.json','vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()

        self.client = Client()

        # User.objects
        #self.user = User.objects.create_superuser(username='user-name', email='user-name@gmail.com', password='password')
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test client list page
    def test_client_list(self):

        request = self.client.get('/client/list/')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = list(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbOrganisationIndex')

    # test organisation detail page
    def test_detail(self):
        request = self.client.get('/organisation/detail')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = detail(request, org_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Organisation Overview</a>')
        self.assertContains(response, 'Edit Organisation')
        self.assertContains(response, 'Organisation Users')
        self.assertContains(response, 'Organisation History')

    # test organisation history page
    def test_history(self):
        request = self.client.get('/organisation/history')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = history(request, org_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h4>Organisation History</h4>')

    # test organisation create page
    def test_create(self):
        request = self.client.get('/organisation/create/')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmOrganisationAdd')

    # test organisation edit page
    def test_edit(self):
        request = self.client.get('/organisation/edit')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = edit(request, org_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmOrganisationEdit')
