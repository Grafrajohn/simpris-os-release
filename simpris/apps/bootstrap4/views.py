import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

from simpris.models.db_views import VwSelectProjectIndexSidebar, VProjectDetail, VProjectTasks, VProjectOpinionDetail
from simpris.models.db_views import VProjectDocuments, VTaskStatuses, VMyPriorities, VMyTasktypes, VTasklistUsersDistinct
from simpris.models.db_views import VwSelectProjectDetailSidebar, VImportances, VProjectGantt
from simpris.models.db_views import VOrganisationProjectManagers, VMyOrganisations
from simpris.models.models import Phase, Comment
from simpris.library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.

@login_required
def dashboard(request):
    user_context = UserContextFull(request)
    logger.info(str.format('bootstrap 4 dashboard : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/bootstrap4_dev/dashboard_simple.html", context_dict)


@login_required
def index_4(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index 4 : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/project/home_4.html", context_dict)
