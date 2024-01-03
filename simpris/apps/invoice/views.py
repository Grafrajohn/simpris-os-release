from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect
import logging, time
from ...models.models import Invoice, Invoiceline
from ...models.db_views import VInvoiceDetail, VMyInvoiceTimes
from ...library.user_context import UserContextFull
from django.db.models import Q
from django.db import connection, transaction

logger = logging.getLogger(__name__)


@login_required
def invoicelist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice list : {0}' .format(user_context.id)))

    userContext = UserContextFull(request)

    invoice_activity = ""
    context_dict = {'usercontext': userContext}
    return render(request, "simpris/invoice/invoicelist.html",context_dict)


@login_required
def activity(request):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice activity : {0}' .format(user_context.id)))

    userContext = UserContextFull(request)

    invoice_activity = ""
    context_dict = {'sidebar': invoice_activity,'usercontext': userContext}
    return render(request, "simpris/invoice/activity.html",context_dict)


@login_required
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice create : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/invoice/create.html",context_dict)


@login_required
def detail(request, inv_id):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice detail : {0}' .format(user_context.id)))

    invoice_data = VInvoiceDetail.objects.all().filter(Q(userid=user_context.id) & Q(invoiceid=inv_id) & Q(clientid=user_context.clientID)).distinct()

    context_dict = {'id': inv_id, 'invoices': invoice_data}

    return render(request, "simpris/invoice/detail.html",context_dict)


@login_required
def format(request):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice format : {0}' .format(user_context.id)))

    description = request.POST.get('frmDescription')
    comments = request.POST.get('frmComments')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    invoice_new = Invoice(clientid=user_context.clientID,userid=user_context.id, statusid=1, description=description,
                                    comments=comments, createddate=created_date,createdby=created_by)
    invoice_new.save()

    context_dict = {'id': invoice_new.pk}
    return render(request, "simpris/invoice/detail.html", context_dict)


@login_required
def insertitems(request):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice insert items : {0}' .format(user_context.id)))

    invoice_id = request.POST.get('hidInvoiceID')

    line_no = 1
    # loop through post fields
    for key in request.POST.getlist('timeID[]'):
        __insert_invoicelines(invoice_id, key, line_no, user_context.id)
        line_no += 1

    return redirect('/invoice/detail/' + invoice_id)


@login_required
def prepare(request):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice prepare : {0}' .format(user_context.id)))

    start_date = request.POST.get('frmDatePicker')
    end_date = request.POST.get('frmDatePicker2')
    description = request.POST.get('frmDescription')
    comments = request.POST.get('frmComments')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    invoice_new = Invoice(clientid=user_context.clientID,userid=user_context.id, statusid=1, description=description,
                                    comments=comments, createddate=created_date,createdby=created_by)
    invoice_new.save()

    invoice_object = Invoice.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('invoiceid')

    invoice_times_data = VMyInvoiceTimes.objects.all().filter(Q(userid=user_context.id) & Q(deleteddate__isnull=True)).order_by('timeday')

    context_dict = {'id': invoice_object.invoiceid, 'description': description, 'comments': comments, 'start_date': start_date,
                    'end_date': end_date, 'times': invoice_times_data}
    return render(request, "simpris/invoice/format.html",context_dict)


@login_required
def printout(request, inv_id):
    user_context = UserContextFull(request)
    logger.info(str.format('invoice printout : {0}' .format(user_context.id)))

    invoice_data = VInvoiceDetail.objects.all().filter(Q(userid=user_context.id) & Q(invoiceid=inv_id) & Q(clientid=user_context.clientID)).distinct()

    context_dict = {'id': inv_id, 'invoices': invoice_data}

    return render(request, "simpris/print/invoice.html",context_dict)


@transaction.atomic
def __insert_invoicelines(inv_id,time_id,line_no,user_id):

    cur = connection.cursor()
    try:
        cur.callproc('simpricity.sr_insert_invoice_line', [inv_id,time_id,line_no,user_id])
        # transaction.commit_unless_managed()

    finally:
        cur.close()

    return
