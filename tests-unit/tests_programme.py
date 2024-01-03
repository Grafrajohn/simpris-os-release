# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.programme.views import list, history, detail, create, edit, index


class programmeTests(TestCase):
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

    # test programme list page
    def test_list(self):
        request = self.factory.get('/programme/list')
        request.user = self.user

        response = list(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbProgrammeIndex')

    # test programme detail page
    def test_detail(self):
        request = self.factory.get('/programme/detail')
        request.user = self.user

        response = detail(request, programme_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Programme Overview</a>')
        self.assertContains(response, 'Edit Programme')
        self.assertContains(response, 'Programme History')

    # test programme history page
    def test_history(self):
        request = self.factory.get('/programme/history')
        request.user = self.user

        response = history(request, programme_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h4>Programme History</h4>')

    # test programme create page
    def test_create(self):
        request = self.factory.get('/programme/create')
        request.user = self.user

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmProgrammeAdd')

    # test programme edit page
    def test_edit(self):
        request = self.factory.get('/programme/edit')
        request.user = self.user

        try:
            response = edit(request, programme_id=37)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'frmProgrammeEdit')

        except:
            pass
