import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

from ...models.models import Error
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
@permission_required('simpris.change_authuser','/error/permissions/')
def list(request):
    logger.info('error list')

    user_context = UserContextFull(request)

    queryset = Error.objects.all().order_by('createddate').reverse()[:100]

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ, 'errors': queryset}
    return render(request, "simpris/error/list.html", context_dict)


@login_required
def permissions(request):
    logger.info('error permissions index')

    user_context = UserContextFull(request)

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/error/permissions.html", context_dict)
