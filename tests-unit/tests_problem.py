from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.problem.views import problemlist, history, detail, create, edit


class ProblemTests(TestCase):
    fixtures = ['User.json','vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        #self.user = User.objects.create_superuser(username='user-name', email='user-name@gmail.com', password='password')
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test problem list page
    def test_list(self):
        request = self.client.get('/client/list')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = problemlist(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbProblemIndex')

    # test Problem detail page
    def test_detail(self):
        request = self.factory.get('/Problem/detail')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = detail(request, prob_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Problem Overview</a>')
        self.assertContains(response, 'Edit Problem')
        self.assertContains(response, 'Problem History')

    # test Problem history page
    def test_history(self):
        request = self.factory.get('/Problem/log')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = history(request, prob_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h4>Problem History</h4>')

    # test Problem create page
    def test_create(self):
        request = self.factory.get('/Problem/create')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmProblemAdd')

    # test Problem edit page
    def test_edit(self):
        request = self.factory.get('/Problem/edit')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = edit(request, prob_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmProblemEdit')
