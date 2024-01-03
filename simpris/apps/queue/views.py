# python imports
import logging, time, datetime

# django imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# simpris imports
# from ...models.db_views import VQueueMembers
from ...models.models import Queue, QueueUser, Users, Team, AuthUser
from ...models.db_views import VQueueUsers, VQueueTeams
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('queue list : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/queue/queuelist.html", context_dict)


@login_required
@permission_required('simpris.add_queue', '/project/home/')
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('queue create : {0}' .format(user_context.id)))

    context_dict = {'mode': "create", 'usercontext': user_context, 'queue': ''}

    return render(request, "simpris/queue/create.html", context_dict)


@login_required
def detail(request, queue_id):
    user_context = UserContextFull(request)
    logger.info(str.format('queue detail : {0}' .format(user_context.id)))

    queue_data = Queue.objects.all().filter(Q(clientid=user_context.clientID) & Q(queueid=queue_id) & Q(deleteddate__isnull=True))

    context_dict = {'queue': queue_data, 'id': queue_id, 'usercontext': user_context}

    return render(request, "simpris/queue/detail.html", context_dict)


@login_required
@permission_required('simpris.change_queue', '/project/home/')
def edit(request, queue_id):
    user_context = UserContextFull(request)
    logger.info(str.format('queue edit : {0}' .format(user_context.id)))

    queue_data = Queue.objects.all().filter(Q(clientid=user_context.clientID) & Q(queueid=queue_id) & Q(deleteddate__isnull=True))

    context_dict = {'mode': "edit", 'queue': queue_data, 'id': queue_id, 'usercontext': user_context}

    return render(request, "simpris/queue/edit.html", context_dict)


@login_required
def members(request, queue_id):
    user_context = UserContextFull(request)
    logger.info(str.format('queue members : {0}' .format(user_context.id)))

    member_data = VQueueUsers.objects.filter(Q(queueid=queue_id) & Q(deleteddate__isnull=True))
    team_data = VQueueTeams.objects.filter(Q(queueid=queue_id) & Q(deleteddate__isnull=True))
    potential_members = Users.objects.all().filter(Q(clientid=user_context.clientID))
    potential_teams = Team.objects.all().filter(Q(clientid=user_context.clientID))

    context_dict = {'mode': "edit", 'members': member_data, 'teams': team_data, 'id': queue_id, 'usercontext': user_context, 'potentials': potential_members, 'potential_teams': potential_teams}

    return render(request, "simpris/queue/members.html", context_dict)
