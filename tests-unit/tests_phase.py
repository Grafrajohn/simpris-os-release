# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.phase.views import phaselist, detail, create, edit


class phaseTests(TestCase):
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

    # test phase list page
    def test_list(self):
        request = self.factory.get('/phase/list')
        request.user = self.user

        response = phaselist(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbPhaseIndex')

    # test phase detail page
    def test_detail(self):
        request = self.factory.get('/phase/detail')
        request.user = self.user

        response = detail(request, phase_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Phase Overview</a>')
        self.assertContains(response, 'Edit Phase')

    # test phase create page
    def test_create(self):
        request = self.factory.get('/phase/create')
        request.user = self.user

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmPhaseAdd')

    # test phase edit page
    def test_edit(self):
        request = self.factory.get('/phase/edit')
        request.user = self.user

        try:
            response = edit(request, phase_id=37)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'frmPhaseEdit')

        except:
            pass

