import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

from ...models.models import Interaction
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
def index(request):
    logger.info('interaction index')

    user_context = UserContextFull(request)

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/interaction/index.html", context_dict)

