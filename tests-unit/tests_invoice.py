# Create your tests here.
from django.test import TestCase

# Create your tests here.
from django.test import RequestFactory
from django.contrib.auth.models import User
from django.test.client import Client

from simpris.apps.invoice.views import invoicelist, detail, create, prepare, format, insertitems, printout


class InvoiceTests(TestCase):
    fixtures = ['User.json','vusercontextfull.json']

    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

        # User.objects
        #self.user = User.objects.create_superuser(username='user-name', email='user-name@gmail.com', password='password')
        self.user = User.objects.get_by_natural_key('user-name')
        self.client.login(username='user-name', password='password')


    # test invoice list page
    def test_invoice_list(self):
        request = self.client.get('/invoice/invoicelist')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = invoicelist(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'tbInvoiceIndex')


    # test invoice detail page
    def test_detail(self):
        request = self.client.get('/invoice/detail')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = detail(request, inv_id=37)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="#">Invoice Overview</a>')


    # test invoice create page
    def test_create(self):
        request = self.client.get('/invoice/create')
        request.user = self.user
        request.META = {"CSRF_COOKIE":'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = create(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'frmInvoiceAdd')


    # test invoice edit page
    def test_format(self):
        request = self.client.get('/invoice/invoicelist/')
        response = self.client.post('/invoice/format/', {'frmDescription': 'Description', 'frmComments': 'Comments'}, user=self.user, request=request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invoice Overview')


    # test invoice insert times page
    def test_insertitems(self):
        response = self.client.post('/invoice/insertitems/', data={'hidInvoiceID': 1})

        self.assertEqual(response.status_code, 302)


    # test invoice prepare page
    def test_prepare(self):
        response = self.client.post('/invoice/prepare/', {'frmDescription': 'Description', 'frmComments': 'Comments'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Prepare Invoice')


    # test invoice printout page
    def test_printout(self):
        request = self.factory.get('/invoice/printout')
        request.user = self.user
        request.META = {"CSRF_COOKIE": 'whRYMA0fHg77asp8V1tGsJTFjvPY7uLRxDZLlVDT6BQIAPuK8jcXWsX9fDtOwRZf'}

        response = printout(request, inv_id=37)

        self.assertEqual(response.status_code, 200)
        #self.assertContains(response, 'Details')
