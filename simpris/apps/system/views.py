from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from ...library.user_context import UserContextFull
from ...models.models import Account
import logging, time

logger = logging.getLogger(__name__)

# Create your views here.


@login_required
@permission_required('simpris.change_authuser','/error/permissions/')
def dashboard(request):
    user_context = UserContextFull(request)
    logger.info(str.format('system admin index : {0}' .format(user_context.id)))

    if user_context.id == 4:
        current_date = time.strftime('%Y-%m-%d %H:%M:%S')

        new_account_activity =  Account.objects.all().order_by('-createddate')[:50]
        context_dict = {'usercontext': user_context, 'accounts': new_account_activity}
        return render(request, "simpris/system/dashboard.html", context_dict)

    else:
        return render (request, "simpris/system/dashboard.html")


@login_required
@permission_required('simpris.change_authuser','/error/permissions/')
def index(request):
    user_context = UserContextFull(request)
    logger.info(str.format('system admin index : {0}' .format(user_context.id)))

    if user_context.id == 4 or user_context.id == 6:
        current_date = time.strftime('%Y-%m-%d %H:%M:%S')

        new_account_activity =  Account.objects.all().order_by('-createddate')[:50]
        context_dict = {'usercontext': user_context, 'accounts': new_account_activity}
        return render(request, "simpris/system/index.html", context_dict)

    else:
        return render (request, "simpris/system/index.html")

