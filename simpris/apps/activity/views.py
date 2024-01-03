import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
@permission_required('simpris.change_authuser','/error/permissions/')
def index(request):
    logger.info('user activity index')

    user_context = UserContextFull(request)

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/activity/index.html", context_dict)

