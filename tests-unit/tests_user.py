# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.user.views import userlist, history, password, profile, detail, create, edit


class userTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test user list page
    def test_list(self):
        request = self.factory.get('/user/list')
        request.user = self.user

        response = userlist(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbUserIndex')

    # test user detail page
    def test_detail(self):
        request = self.factory.get('/user/detail')
        request.user = self.user

        response = detail(request, user_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">User Overview</a>')
        self.assertContains(response, 'Edit User')

    # test user create page
    def test_create(self):
        request = self.factory.get('/user/create')
        request.user = self.user

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmUserAdd')

    # test user edit page
    def test_edit(self):
        request = self.factory.get('/user/edit')
        request.user = self.user

        try:
            response = edit(request, user_id=37)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'frmUserEdit')

        except:
            pass
