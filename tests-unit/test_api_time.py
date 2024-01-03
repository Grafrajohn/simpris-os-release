from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.models.models import Time, Users
from simpris.models.db_views import VUserContextFull


class TimeAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'organisation.json',
                'project.json',
                'task.json',
                'tasklist.json',
                'time.json',
                'User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api time clendar
    def test_calendar(self):
        url = ('/api/time/calendar/')
        #data = {'hidtimeID': '1', 'frmtimeName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api time delete
    def test_delete(self):
        url = ('/api/time/delete/1/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api time delete
    def test_delete_time(self):
        url = ('/api/time/deletetime/')
        data = {'timeid': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api time insert
    def test_insert(self):
        url = ('/api/time/insert/')
        data = {'frmTaskID': 1,
            'frmDatePicker': '2016-12-02',
            'frmHours': 1,
            'frmMins': 20,
            'frmTimeType': 1,
            'frmComments': 'comments'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api time insert
    def test_insert_time(self):
        url = ('/api/time/inserttime/')

        data = {'frmdate': '2016-12-02', 'starthour': 9, 'startmin': 25, 'hours': 5, 'mins': 20, 'taskid': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api time list
    def test_list(self):
        url = ('/api/time/times/')
        #data = {'hidtimeID': '1', 'frmtimeName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api time update
    # def test_save_timegrid(self):
    #     url = ('/api/time/timegrid/')
    #     data = {'hidtimeID': '1', 'frmtimeName': 'Test Company Ltd'}
    #     self.client.force_authenticate(user=self.user)
    #
    #     response = self.client.post(url, data)
    #
    #     self.assertEqual(response.status_code, 200)

    # test api time team clendar
    #def test_team_calendar(self):
        #url = ('/api/time/teamcalendar/')
        #data = {'hidtimeID': '1', 'frmtimeName': 'Test Company Ltd'}
        #self.client.force_authenticate(user=self.user)

        #response = self.client.get(url)

        #self.assertEqual(response.status_code, 200)

    # test api time timegrid
    def test_timegrid(self):
        url = ('/api/time/timegrid/')
        data = {'indate': '2016-12-02'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)

    # test api time timegrid
    def test_timetask(self):
        url = ('/api/time/timetask/')
        #data = {'hidtimeID': '1', 'frmtimeName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api time update
    def test_update(self):
        url = ('/api/time/update/')
        data = {'hidTimeID': 1,
            'hidTaskID': 1,
            'hidUserID': 4,
            'frmHours': 2,
            'frmTimeType': 1,
            'frmComment': 'comment'}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api time update
    def test_update_time(self):
        url = ('/api/time/updatetime/')
        data = {'frmdate': '2016-12-02',
            'starthour': 4,
            'startmin': 25,
            'hours': 5,
            'mins': 25,
            'timeid': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
