# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

# Simpris imports
from simpris.apps.search.views import index, SearchForm


class SearchTests(TestCase):
    fixtures = ['auth_user.json',
                'User.json',
                'vsearch.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test search page GET
    def test_index(self):
        request = self.client.get('/search/index/')
        request.user = self.user
        request.method = 'GET'
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = index(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h3>Search results</h3>')

    # test search page POST
    def test_search(self):
        search_phrase = 'design'
        request = self.client.post('/search/index/', {'frmSearchText': search_phrase})
        request.user = self.user
        request.method = 'POST'
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = self.client.post('/search/index/', request)
        #response.client = Client()

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Search results')
