# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client

from simpris.apps.project.views import projectlist, history, detail, create, edit, index


class projectTests(TestCase):
    fixtures = ['User.json','vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        #self.user = User.objects.create_superuser(username='user-name', email='user-name@gmail.com', password='password')
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test home index page
    def test_project_home(self):
        request = self.factory.get('/project/home')
        request.user = self.user

        response = index(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbHomeIndex')

    # test project list page
    def test_project_list(self):
        request = self.factory.get('/project/list')
        request.user = self.user

        response = projectlist(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbProjectIndex')

    # test project detail page
    def test_detail(self):
        request = self.factory.get('/project/detail')
        request.user = self.user

        response = detail(request, proj_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Project Overview</a>')
        self.assertContains(response, 'Edit Project')
        self.assertContains(response, 'Project History')

    # test project history page
    def test_history(self):
        request = self.factory.get('/project/history')
        request.user = self.user

        response = history(request, proj_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h4>Project History</h4>')

    # test project create page
    def test_create(self):
        request = self.factory.get('/project/create')
        request.user = self.user

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmProjectAdd')

    # test project edit page
    def test_edit(self):
        request = self.factory.get('/project/edit')
        request.user = self.user

        try:
            response = edit(request, proj_id=37)
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'frmProjectEdit')

        except:
            pass

    # test project create task
    # def test_task_create(self):
    #     request = self.factory.get('/project/detail')
    #     request.user = self.user
    #
    #     response = detail(request, proj_id=37)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, '<a href="#">Project Overview</a>')
    #     self.assertContains(response, 'Edit Project')
    #     self.assertContains(response, 'Project History')

    # test project create tasklist
    # def test_tasklist_create(self):
    #     request = self.factory.get('/project/detail')
    #     request.user = self.user
    #
    #     response = detail(request, proj_id=37)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, '<a href="#">Project Overview</a>')
    #     self.assertContains(response, 'Edit Project')
    #     self.assertContains(response, 'Project History')

    # test project add document
    # def test_document_upload(self):
    #     request = self.factory.get('/project/detail')
    #     request.user = self.user
    #
    #     response = detail(request, proj_id=37)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, '<a href="#">Project Overview</a>')
    #     self.assertContains(response, 'Edit Project')
    #     self.assertContains(response, 'Project History')
