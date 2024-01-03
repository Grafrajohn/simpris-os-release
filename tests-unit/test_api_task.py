from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User
from simpris.models.models import Task
from simpris.models.db_views import VUserContextFull

from simpris.api.task.views import delete, delete_post, dependencies, detail, insert, move, search_json, update, update_quick


class TaskAPITests(TestCase):
    fixtures = ['account.json',
                'client.json',
                'organisation.json',
                'project.json',
                'task.json',
                'tasklist.json',
                'User.json',
                'vmytasks.json',
                'vprojecttasks.json',
                'vtaskdetail.json',
                'vusercontextfull.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api task delete
    def test_delete(self):
        url = ('/api/task/delete/1/')
        #data = {'org_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api task delete
    def test_delete_post(self):
        url = ('/api/task/delete_post/')
        data = {'task_id': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api task list
    def test_dependencies(self):
        url = ('/api/task/dependencies/')
        #data = {'hidtaskID': '1', 'frmtaskName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api task list
    def test_detail(self):
        url = ('/api/task/detail/')
        data = {'taskid': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)

    # test api task insert
    def test_insert(self):
        url = ('/api/task/insert/')
        data = {'frmTaskName': 'task name',
        'ckedited': 'edited',
        'frmTaskStatus': 1,
        'hidTaskList': 1,
        'frmDatePicker-1': '2016-12-10',
        'frmTaskType': 1,
        'frmTaskPriority': 1,
        'frmTaskAssignee': 1,
        'frmEstimatedTime': 10,
        'frmPercentageComplete': 10,
        'frmDatePicker2-1': '2016-12-12',
        'selPhaseID': 1,
        'frmTaskDependency': 2}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api task list
    def test_list(self):
        url = ('/api/task/tasks/')
        #data = {'hidtaskID': '1', 'frmtaskName': 'Test Company Ltd'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api task move
    def test_move(self):
        url = ('/api/task/move/')
        data = {'hidTaskID': 1, 'frmTaskList': 1}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api task list
    def test_search_json(self):
        url = ('/api/task/searchj/')
        data = {'term': 'software'}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url, data)

        self.assertEqual(response.status_code, 200)

    # test api task update
    def test_update(self):
        url = ('/api/task/update/')
        data = {'frmTaskName': 'name',
            'ckedited': 'edited',
            'frmTaskStatus': 1,
            'hidTaskID': 1,
            'hidTaskList': 1,
            'frmDatePicker-1': '2016-12-10',
            'frmDatePicker': '2016-12-10',
            'frmTaskType': 1,
            'frmTaskPriority': 1,
            'frmTaskAssignee': 1,
            'frmEstimatedTime': 10,
            'frmPercentageComplete': 10,
            'frmTaskDependency': 1,
            'frmDatePicker2-1': '2016-12-14',
            'frmDatePicker2': '2016-12-14',
            'selPhaseID': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api task update quick
    def test_update_quick(self):
        url = ('/api/task/update/')
        data = {'frmTaskName': 'name',
            'ckedited': 'edited',
            'frmTaskStatus': 1,
            'hidTaskID': 1,
            'hidTaskList': 1,
            'frmDatePicker-1': '2016-12-10',
            'frmTaskType': 1,
            'frmTaskPriority': 1,
            'frmTaskAssignee': 1,
            'frmEstimatedTime': 10,
            'frmPercentageComplete': 10,
            'frmTaskDependency': 1,
            'frmDatePicker2-1': '2016-12-14',
            'selPhaseID': 1}

        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
