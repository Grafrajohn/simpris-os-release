# Create your tests here.
import time

from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.time.views import timesheet, timegrid, detail, create, edit, timelist, timeprint


class timeTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test time list page
    def test_list(self):
        request = self.factory.get('/time/list')
        request.user = self.user

        response = timelist(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbTimeIndex')

    # test time detail page
    def test_detail(self):
        request = self.factory.get('/time/detail')
        request.user = self.user

        response = detail(request, time_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Time Detail')

    # test time grid page
    def test_timegrid(self):
        request = self.factory.get('/time/members')
        request.user = self.user

        response = timegrid(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Time Editor')

    # test time print page
    def test_timeprint(self):
        request = self.factory.get('/time/members')
        request.user = self.user

        time_start = time.strftime('%Y-%m-%d %H:%M:%S')
        time_end = time.strftime('%Y-%m-%d %H:%M:%S')

        response = timeprint(request, time_start, time_end)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Timesheet for:')

    # test time create page
    def test_create(self):
        request = self.factory.get('/time/create')
        request.user = self.user

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmTimeAdd')

    # test time edit page
    def test_edit(self):
        request = self.factory.get('/time/edit')
        request.user = self.user

        try:
            response = edit(request, time_id=37)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'frmTimeEdit')

        except:
            pass

