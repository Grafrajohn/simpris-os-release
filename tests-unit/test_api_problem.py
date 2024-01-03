from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Problem
from simpris.models.db_views import VUserContextFull


class problemAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'organisation.json',
                'problem.json',
                'User.json',
                #'vmyproblems.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api problem delete
    def test_delete(self):
        url = ('/api/problem/delete/1/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api problem insert
    def test_insert(self):
        url = ('/api/problem/insert/')
        data = {'frmOrganisation': 1,
        'frmProblemHeader': 'header',
        'frmProblemDescription': 'desc',
        'frmProblemType': 1,
        'frmProblemSubType': 1,
        'frmNoofPeopleAffected': 1,
        'frmProblemScope': 1,
        'frmProblemStatus': 1,
        'frmProblemPriority': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api problem list
    def test_list(self):
        url = ('/api/problem/problems/')
        #data = {'hidproblemID': '1', 'frmproblemName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api problem update
    def test_update(self):
        url = ('/api/problem/update/')
        data = {'hidProblemID': 1,
            'hidOrganisationID': 1,
            'frmProblemHeader': 'head',
            'frmProblemDescription': 'desc',
            'frmProblemType': 1,
            'frmProblemSubType': 1,
            'frmNoofPeopleAffected': 1,
            'frmProblemScope': 1,
            'frmProblemStatus': 1,
            'frmProblemPriority': 1,
            'frmProblemAssignee': 1,
            'frmProblemLink': 1,
            'frmProjectLink': 1,
            'hidProblemLink': 1,
            'hidProjectLink': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api problem update
    #def test_insert_problem_link(self):
        # url = ('/api/problem/insert_problem_link/')
        # data = {'hidproblemID': '1', 'frmproblemName': 'Test Company Ltd'}
        # self.client.force_authenticate(user=self.user)
        #
        # response = self.client.post(url, data)
        #
        # self.assertEqual(response.status_code, 200)

    # test api problem update
    # def test_update_problem_link(self):
    #     url = ('/api/problem/update_problem_link/')
    #     data = {'hidproblemID': '1', 'frmproblemName': 'Test Company Ltd'}
    #     self.client.force_authenticate(user=self.user)
    #
    #     response = self.client.post(url, data)
    #
    #     self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
