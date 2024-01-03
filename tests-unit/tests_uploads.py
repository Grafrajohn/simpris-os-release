# Create your tests here.
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.test.client import Client
from django.core.files.uploadedfile import SimpleUploadedFile

from simpris.apps.uploads.views import upload, handle_uploaded_file


class UploadTests(TestCase):
    fixtures = ['User.json',
                'vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')

    # test upload file
    def test_new(self):
        request = self.factory.post('/uploads/upload')
        request.user = self.user

        testFile = SimpleUploadedFile("unit_configuration.py", b"file_content")
        request.POST['hidItemType'] = 'tsk'
        request.POST['hidItemID'] = 1
        request.POST['hidParentID'] = 1
        request.POST['frmUserFile'] = 'unit_configuration.py'

        request.FILES.update({'frmUserFile': testFile})

        #HttpRe
        #response.client = Client()
        response = upload(request)
        response.client = Client()

        redirect = '/task/detail/1/'

        self.assertRedirects(response, redirect, status_code=302, target_status_code=302)

    # test handle uploaed file
    # def test_thankyou(self):
    #     request = self.factory.get('/register/thankyou')
    #     request.user = self.user
    #
    #     response = handle_uploaded_file(request)
    #
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Subscription and Upgrade complete!')
