import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

from ...models.db_views import VwSelectProjectIndexSidebar, VProjectDetail, VProjectTasks, VProjectOpinionDetail
from ...models.db_views import VProjectDocuments, VTaskStatuses, VMyPriorities, VMyTasktypes, VTasklistUsersDistinct
from ...models.db_views import VwSelectProjectDetailSidebar, VImportances, VProjectGantt
from ...models.db_views import VOrganisationProjectManagers, VMyOrganisations
from ...models.models import Phase, Comment
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


@login_required
def index(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/index.html", context_dict)


@login_required
def detail(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home detail : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/detail.html", context_dict)


@login_required
def index1(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index1 : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/index1.html", context_dict)


@login_required
def index2(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index2 : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/index2.html", context_dict)


@login_required
def index3(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index3 : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/index3.html", context_dict)


@login_required
def index4(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index4 : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/index4.html", context_dict)


@login_required
def index5(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index5 : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/ideas/index5.html", context_dict)

