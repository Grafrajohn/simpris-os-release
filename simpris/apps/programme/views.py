import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

# from ...models.db_views import VwSelectProgrammeIndexSidebar, VProgrammeDetail
# from ...models.db_views import VProgrammeDocuments, VTaskStatuses, VMyPriorities, VMyTasktypes, VTasklistUsersDistinct
# from ...models.db_views import VwSelectProgrammeDetailSidebar, Phase, VImportances
from ...models.models import Programme, Project
from ...models.db_views import VwSelectProgrammeHistory
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
def index(request):
    logger.info('programme index')

    user_context = UserContextFull(request)

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/programme/home.html", context_dict)


@login_required
def activity(request):
    logger.info('programme activity index')

    user_context = UserContextFull(request)

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/programme/activity.html", context_dict)


@login_required
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('programme list : {0}' .format(user_context.id)))

    programme_activity = None # VwSelectProgrammeIndexSidebar.objects.all().filter(Q(userid=user_context.id) | Q(userid='')).order_by('column4', 'programmename')
    context_dict = {'sidebar': programme_activity, 'usercontext': user_context}
    return render(request, "simpris/programme/list.html", context_dict)


@login_required
@permission_required('simpris.add_programme','/project/home/')
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('programme create : {0}' .format(user_context.id)))

    context_dict = {'superuser': 0, 'staff': 0, 'usercontext': user_context}

    return render(request, "simpris/programme/create.html", context_dict)


@login_required          
def detail(request, programme_id):
    user_context = UserContextFull(request)
    logger.info(str.format('programme detail : {0}' .format(user_context.id)))

    programme = Programme.objects.all().filter(Q(programmeid=programme_id) & Q(clientid=user_context.clientID))
    projects = Project.objects.all().filter(programmeid=programme_id)

    context_dict = {'programmes': programme, 'id': programme_id, 'usercontext': user_context, 'projects': projects}
    
    return render(request, "simpris/programme/detail.html", context_dict)


@login_required
@permission_required('simpris.change_programme','/project/home/')
def edit(request, programme_id):
    user_context = UserContextFull(request)
    logger.info(str.format('programme edit : {0}' .format(user_context.id)))

    programme = Programme.objects.all().filter(Q(programmeid=programme_id) &
                                                  Q(clientid=user_context.clientID))

    context_dict = {'programme': programme, 'id': programme_id, 'usercontext': user_context}

    return render(request, "simpris/programme/edit.html", context_dict)


@login_required
def history(request, programme_id):
    user_context = UserContextFull(request)
    logger.info(str.format('programme history : {0}' .format(user_context.id)))

    programme_history = VwSelectProgrammeHistory.objects.all().filter(Q(programmeid=programme_id))
    context_dict = {'id': programme_id, 'history': programme_history, 'usercontext': user_context}
    return render(request, "simpris/programme/history.html", context_dict)
