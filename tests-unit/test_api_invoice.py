from django.urls import reverse
from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
from django.contrib.auth.models import User

from simpris.api.invoice.views import insert, delete, invoices


class invoiceAPITests(TestCase):
    fixtures = ['account.json',
                'User.json',
                'vusercontextfull.json',
                'invoice.json',
                'client.json']

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.get_by_natural_key('user-name')

    # test api invoice delete
    def test_delete(self):
        url = ('/api/invoice/delete/4/')
        #data = {'inv_id': 4}
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    # test api invoice insert
    def test_insert(self):
        url = ('/api/invoice/insert/')
        data = {
            'frmDatePicker': '2016/12/01',
            'frmDatePicker2': '2016/12/31',
            'frmDescription': 'test description',
            'frmComments': 'comments'}
        self.client.force_authenticate(user=self.user)

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    # test api invoice list
    def test_list(self):
        url = ('/api/invoice/invoices/')
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.client.logout()
