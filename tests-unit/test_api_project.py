from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Project
from simpris.models.db_views import VUserContextFull, VMyProjects

from simpris.api.project.views import delete, deleteuser, programme, programme_project_delete, project_search, project_search_json, insert, update, home



class projectAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'organisation.json',
                'project.json',
                'User.json',
                'userproject.json',
                'users.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api project delete
    def test_delete(self):
        url = ('/api/project/delete/4/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api project delete
    def test_deleteuser(self):
        url = ('/api/project/deleteuser/')
        data = {'hidUserProjectID': 1,
                'user_project_id': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api project insert
    def test_insert(self):
        url = ('/api/project/insert/')
        data = {'frmProjectOrganisation': 1,
            'frmProjectName': 'name',
            'ckeditedDescription': 'desc',
            'frmProjectStakeholder': 1,
            'frmProjectManager': 1,
            'ckeditedDeliverables': 'delivs',
            'frmProjectBudget': 100,
            'frmProjectImportance': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api project insert user
    def test_insert_user(self):
        url = ('/api/project/insertuser/')
        data = {'hidprojectID': '1', 'selUserProject': 1, 'sepProjectUser': 4, 'hidUserID': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api project home
    def test_home(self):
        url = ('/api/project/home/')
        #data = {'hidprojectID': '1', 'frmprojectName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api programme home
    def test_programme(self):
        url = ('/api/project/programme/')
        data = {'hidProjectID': 1, 'hidProgrammeID': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api programme home
    def test_programme_project_delete(self):
        url = ('/api/project/programme_project_delete/')
        data = {'project_id': 1, 'programme_id': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api programme home
    def test_project_search(self):
        url = ('/api/project/search/')
        #data = {'hidprojectID': '1', 'frmprojectName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api programme home
    def test_project_search_json(self):
        url = ('/api/project/searchj/')
        #data = {'hidprojectID': '1', 'frmprojectName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api project list
    def test_list(self):
        url = ('/api/project/projects/')
        #data = {'hidprojectID': '1', 'frmprojectName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api project update
    def test_update(self):
        url = ('/api/project/update/')
        data = {'hidProjectID': 1,
            'hidOrganisationID': 1,
            'frmProjectName': 'name',
            'ckeditedDescription': 'desc',
            'frmProjectStakeholder': 1,
            'frmProjectManager': 1,
            'ckeditedDeliverables': 'delivs',
            'frmProjectBudget': 100,
            'frmProjectImportance': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
