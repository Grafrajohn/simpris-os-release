# from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from simpris.api.invoice.serializers import VInvoicesSerializer
from simpris.models.db_views import VMyInvoices
from simpris.models.models import Invoice
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view
from django.db.models import Q
import time
import logging

logger = logging.getLogger(__name__)


class APIInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


@api_view(['GET'])
def invoices(request):
    
    userContext = UserContextFull(request)
    logger.info(str.format('invoices list : {0}' .format(userContext.id)))
    
    queryset = VMyInvoices.objects.all().filter(Q(clientid=userContext.clientID, userid=userContext.id) & Q(deleteddate__isnull=True)).order_by('createddate')
    serializer_class = VInvoicesSerializer(queryset,many=True)   

    return Response(serializer_class.data)


@api_view(['GET'])
def delete(request, inv_id):

    userContext = UserContextFull(request)
    logger.info(userContext)

    deletedDate = time.strftime('%Y-%m-%d %H:%M:%S')
    deletedBy = userContext.id

    inv = Invoice.objects.get(invoiceid=inv_id, clientid=userContext.clientID)
    inv.deletedby = deletedBy
    inv.deleteddate = deletedDate
    inv.save()

    response = {'invoiceid': inv_id}

    return Response(response)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('invoice create : {0}' .format(user_context.id)))

    start_date = request.POST.get('frmDatePicker')
    end_date = request.POST.get('frmDatePicker2')
    description = request.POST.get('frmDescription')
    comments = request.POST.get('frmComments')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    # client = Client.objects.get(clientid=client_id)

    invoice_serializer = APIInvoiceSerializer(data={'clientid': client_id, 'userid': user_context.id, 'statusid': 1,
                            'description': description, 'comments': comments, 'createddate': created_date,'createdby': created_by,
                            'updateddate': created_date, 'updatedby': created_by})

    if invoice_serializer.is_valid():

        invoice_new = Invoice(clientid=client_id,userid=user_context.id, statusid=1, description=description,
                                        comments=comments, createddate=created_date,createdby=created_by)
        invoice_new.save()

        invoice_object = Invoice.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('invoiceid')

        response = {'invoice_id': invoice_object.invoiceid}

    else:

        raise serializers.ValidationError(invoice_serializer.errors)

    return Response(response)
