# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.register.views import new, thankyou, welcome, RegisterForm


class projectTests(TestCase):
    fixtures = ['auth_group.json',
                'auth_user.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()
        User.objects
        self.user = User(username='user-name')
        self.client.login(username='user-name', password='password')

    # test register new page
    def test_new(self):
        data = {
            'g-recaptcha-response': 'jfkflfdflvdfvkmdfvd',
            'username': 'test_user',
            'company': 'test co',
            'first_name': 'Jim',
            'last_name': 'Jones',
            'email': 'jim.jones@testco.com',
            'phone': '92736446474',
            'password': 'pwdhere01',
            'password_confirm': 'pwdhere01',
            'tcs': True
        }

        request = self.factory.post('/register/new',
            data)
        request.user = self.user
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

        response = new(request)
        response.client = Client()

        self.assertRedirects(response, 'http://127.0.0.1:8000/register/welcome', status_code=302, target_status_code=302)

    # test register thankyou list page
    def test_thankyou(self):
        request = self.factory.get('/register/thankyou')
        request.user = self.user

        response = thankyou(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Subscription and Upgrade complete!')

    # test register welcome page
    def test_welcome(self):
        request = self.factory.get('/register/welcome')
        request.user = self.user

        response = welcome(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to Simpris')
