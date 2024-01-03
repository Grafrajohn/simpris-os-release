from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.report.views import project, metric, datatable, chart, gantt, gantt_jq, generic


class ReportTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test project report page
    def test_project(self):
        request = self.factory.get('/report/project')
        request.user = self.user

        response = project(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<title>Project Metrics</title>')

    # test project report page
    def test_metric(self):
        request = self.factory.get('/report/metric')
        request.user = self.user

        response = metric(request, report_id=1)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div id="visualization"></div>')

    # test datatable report page
    def test_datatable(self):
        request = self.factory.get('/report/datatable')
        request.user = self.user

        response = datatable(request, report_id=1)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<table id="tbReportIndex" class="dtable"></table>')

    # test chart report page
    def test_chart(self):
        request = self.factory.get('/report/chart')
        # request.data = {
        #     'chart_id': 1,
        #     'item_id': 1
        # }
        request.user = self.user

        response = chart(request, chart_id=1, item_id = 1)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h3>Open Tasks for Project by status: </h3>')

    # test gantt report page
    def test_gantt(self):
        request = self.factory.get('/report/gantt')
        request.user = self.user

        response = gantt(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div gantt data="data">')

    # test gantt_jq report page
    def test_gantt_jq(self):
        request = self.factory.get('/report/gantt_jq')
        request.user = self.user

        response = gantt_jq(request, proj_id = 1)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<div style="margin-top :0;" class="gantt"></div>')


    # test generic report page
    def test_generic(self):
        request = self.factory.get('/report/generic')
        request.user = self.user

        response = generic(request, report_id=1)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<canvas id="chart-01"></canvas>')
