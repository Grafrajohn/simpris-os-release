import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

from ...models.models import Lookup
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
@permission_required('simpris.add_project','/error/permissions/')
def index(request):
    logger.info('lookup index')

    user_context = UserContextFull(request)

    queryset = Lookup.objects.all().filter(clientid=user_context.clientID).order_by('lookuptypeid')

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/lookup/index.html", context_dict)

