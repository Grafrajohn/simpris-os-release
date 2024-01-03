# python imports
import logging, time, datetime

# django imports
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q

# simpris imports
from ...models.db_views import VTeamMembers
from ...models.models import Team, Users
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)

# Create your views here.


@login_required
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('team list : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}

    return render(request, "simpris/team/teamlist.html", context_dict)


@login_required
@permission_required('simpris.add_team', '/project/home/')
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('team create : {0}' .format(user_context.id)))

    context_dict = {'mode': "create", 'usercontext': user_context, 'team': ''}

    return render(request, "simpris/team/create.html", context_dict)


@login_required
def detail(request, team_id):
    user_context = UserContextFull(request)
    logger.info(str.format('team create : {0}' .format(user_context.id)))

    team_data = Team.objects.all().filter(Q(clientid=user_context.clientID) & Q(teamid=team_id) & Q(deleteddate__isnull=True))

    context_dict = {'team': team_data, 'id': team_id, 'usercontext': user_context}

    return render(request, "simpris/team/detail.html", context_dict)


@login_required
@permission_required('simpris.change_team', '/project/home/')
def edit(request, team_id):
    user_context = UserContextFull(request)
    logger.info(str.format('team create : {0}' .format(user_context.id)))

    team_data = Team.objects.all().filter(Q(clientid=user_context.clientID) & Q(teamid=team_id) & Q(deleteddate__isnull=True))

    context_dict = {'mode': "edit", 'team': team_data, 'id': team_id, 'usercontext': user_context}

    return render(request, "simpris/team/edit.html", context_dict)


@login_required
def members(request, team_id):
    user_context = UserContextFull(request)
    logger.info(str.format('team create : {0}' .format(user_context.id)))

    member_data = VTeamMembers.objects.all().filter(Q(clientid=user_context.clientID) & Q(teamid=team_id) & Q(deleteddate__isnull=True))
    potential_members = Users.objects.all().filter(Q(clientid=user_context.clientID))

    context_dict = {'mode': "edit", 'members': member_data, 'id': team_id, 'usercontext': user_context, 'potentials': potential_members}

    return render(request, "simpris/team/members.html", context_dict)
