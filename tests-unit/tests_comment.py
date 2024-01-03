# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.comment.views import insert


class CommentTests(TestCase):
    fixtures = ['auth_user.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test comment insert page
    def test_insert(self):
        request = self.factory.post('/comment/insert/154/')
        request.user = self.user

        response = self.client.post('/comment/insert/154/',
                                     {'frmTextComment': 'test comment', 'hidUploadSource': 'task_comment',
                                     'hidParentID': '154', 'hidParentType': '3'})

        self.assertRedirects(response, '/task/detail/154', status_code=302, target_status_code=301)
        self.assertEqual(response.status_code, 302)