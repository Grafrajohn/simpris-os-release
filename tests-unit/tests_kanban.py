# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.schedule.views import kanban


class kanbanTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test kanban detail page
    def test_kanban(self):
        request = self.factory.get('/schedule/kanban')
        request.user = self.user

        response = kanban(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h3>Work board</h3>')
