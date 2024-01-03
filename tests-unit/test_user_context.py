# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.library.user_context import UserContextFull
from simpris.apps.user.views import userlist, history, password, profile, detail, create, edit
from simpris.models.db_views import VUserContextFull


class ContextTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test user context with user
    def test_context_good(self):

        request = self.factory.get('/')
        request.user = self.user
        context = UserContextFull(request)

        self.assertEqual(context.username, 'user-name')
        self.assertEqual(context.clientID, 3)
        self.assertEqual(context.firstName, 'Graham')
        self.assertEqual(context.lastName, 'Johnson')
        self.assertEqual(context.fullname, 'Graham Johnson')
        self.assertEqual(context.id, 4)
        self.assertEqual(context.organisationID, 3)
        self.assertEqual(context.organisationName, 'GoodlyCode Ltd')
        self.assertEqual(context.isClientAdmin, 1)
        self.assertEqual(context.isSuperUser, 1)

    # test user context with NO user
    def test_context_bad(self):

        request = self.factory.get('/')
        request.user = None
        context = UserContextFull(request)

        self.assertEqual(context.username, None)
        self.assertEqual(context.clientID, None)
        self.assertEqual(context.firstName, None)
        self.assertEqual(context.lastName, None)
        self.assertEqual(context.fullname, None)
        self.assertEqual(context.id, None)
        self.assertEqual(context.organisationID, None)
        self.assertEqual(context.organisationName, None)
        self.assertEqual(context.isClientAdmin, None)
        self.assertEqual(context.isSuperUser, None)
