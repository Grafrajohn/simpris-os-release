# python imports
import time
import logging

# django imports
from django.db.models import Q
from django.contrib.auth.models import User

# rest imports
from rest_framework.response import Response
from rest_framework import serializers

# simpris imports
from simpris.api.team.serializers import TeamSerializer
from simpris.models.models import Team, TeamUser
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view


logger = logging.getLogger(__name__)


# serializer for teams
class APITeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('teamid', 'clientid', 'teamname', 'teamdescription', 'updateddate', 'updatedby')


# serializer for team members
class APITeamUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamUser
        fields = ('teamid', 'userid', 'clientid')

@api_view(['GET'])
def teamlist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('team list : {0}' .format(user_context.id)))

    queryset = Team.objects.all().filter(Q(clientid=user_context.clientID) & Q(deleteddate__isnull=True))\
        .order_by('teamid')
    serializer_class = TeamSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('team create : {0}' .format(user_context.id)))

    team_name = request.POST.get('frmTeamName')
    team_description = request.POST.get('frmTeamDescription')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    team_serializer = APITeamSerializer(data={'teamid': 0, 'teamname': team_name, 'teamdescription': team_description,
                                    'clientid': client_id, 'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if team_serializer.is_valid():

        team_new = Team(clientid=client_id, teamname=team_name, teamdescription=team_description,
                    createddate=created_date, createdby=created_by)
        team_new.save()

        team_object = Team.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('teamid')

        response = {'team_id': team_object.teamid}

    else:

        raise serializers.ValidationError(team_serializer.errors)

    return Response(response)


@api_view(['GET'])
def delete(request, team_id):

    user_context = UserContextFull(request)
    logger.info(str.format('team delete : {0}' .format(user_context.id)))

    # team_id = team_id
    # team_name = request.POST.get('frmteamName')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_team'):

        team_update = Team.objects.get(teamid=team_id, clientid=user_context.clientID)
        team_update.deleteddate = deleted_date
        team_update.deletedby = deleted_by
        team_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'team_id': team_id}

    else:

        raise serializers.ValidationError('You are not authorised to delete teams')

    return Response(response)


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('team update : {0}' .format(user_context.id)))

    team_id = request.POST.get('hidTeamID')
    team_name = request.POST.get('frmTeamName')
    team_description = request.POST.get('frmTeamDescription')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    team_serializer = APITeamSerializer(data={'teamid': 0, 'clientid': user_context.clientID, 'teamname': team_name,
                                                'teamdescription': team_description,
                                                'updateddate': updated_date, 'updatedby': updated_by})

    if team_serializer.is_valid():

        team_update = Team.objects.get(clientid=user_context.clientID, teamid=team_id)
        team_update.teamname = team_name
        team_update.teamdescription = team_description
        team_update.updateddate = updated_date
        team_update.updatedby = updated_by
        team_update.save(update_fields=['teamname', 'teamdescription', 'updateddate', 'updatedby'])

        response = {'team_id': team_id}

    else:

        raise serializers.ValidationError(team_serializer.errors)

    return Response(response)


@api_view(['POST'])
def member_create(request):

    user_context = UserContextFull(request)
    logger.info(str.format('team member create : {0}' .format(user_context.id)))

    team_id = request.POST.get('hidTeamID')
    team_member = request.POST.get('selTeamMember')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    team = Team.objects.get(teamid=team_id, clientid=user_context.clientID)
    team_member_serializer = APITeamUserSerializer(data={'teamid': team.teamid, 'userid': team_member, 'clientid': user_context.clientID})
    if team_member_serializer.is_valid():

        member_new = TeamUser(teamid=team_id, userid=team_member, clientid=user_context.clientID, createddate=created_date, createdby=created_by)
        member_new.save()

        response = member_new.id

    else:

        raise serializers.ValidationError(team_member_serializer.errors)

    return Response(response)

@api_view(['POST'])
def member_delete(request):

    user_context = UserContextFull(request)
    logger.info(str.format('team member delete : {0}' .format(user_context.id)))

    id = request.POST.get('id')
    team_id = request.POST.get('team_id')
    team_member_id = request.POST.get('team_member_id')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_team'):

        team_member_update = TeamUser.objects.get(id=id, teamid=team_id, clientid=user_context.clientID, userid=team_member_id, deletedby__isnull=True)
        team_member_update.deleteddate = deleted_date
        team_member_update.deletedby = deleted_by
        team_member_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'team_id': team_id}

    else:

        raise serializers.ValidationError('You are not authorised to delete team members')

    return Response(response)
