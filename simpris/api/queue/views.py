# python imports
import logging
import time

from django.contrib.auth.models import User
# django imports
from django.db.models import Q
from rest_framework import serializers
from rest_framework.decorators import api_view
# rest imports
from rest_framework.response import Response

# simpris imports
from simpris.api.queue.serializers import QueueSerializer
from simpris.library.user_context import UserContextFull
from simpris.models.models import Queue, QueueUser, TeamQueue, Team, AuthUser

logger = logging.getLogger(__name__)


# serializer for queues
class APIQueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ('queueid', 'clientid', 'queuename', 'queuedescription', 'updateddate', 'updatedby')


# serializer for queue members
class APIQueueUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueUser
        fields = ('queueid', 'queueuserid', 'clientid')


# serializer for queue members
class APIQueueTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamQueue
        fields = ('queueid', 'queueteamid', 'clientid')


@api_view(['GET'])
def queuelist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('queue list : {0}' .format(user_context.id)))

    queryset = Queue.objects.all().filter(Q(clientid=user_context.clientID) & Q(deleteddate__isnull=True))\
        .order_by('queueid')
    serializer_class = QueueSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('queue create : {0}' .format(user_context.id)))

    queue_name = request.POST.get('frmQueueName')
    queue_description = request.POST.get('frmQueueDescription')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    queue_serializer = APIQueueSerializer(data={'queueid': 0, 'queuename': queue_name, 'queuedescription': queue_description,
                                    'clientid': client_id, 'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if queue_serializer.is_valid():

        queue_new = Queue(clientid=client_id, queuename=queue_name, queuedescription=queue_description,
                    createddate=created_date, createdby=created_by)
        queue_new.save()

        queue_object = Queue.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('queueid')

        response = {'queue_id': queue_object.queueid}

    else:

        raise serializers.ValidationError(queue_serializer.errors)

    return Response(response)


@api_view(['GET'])
def delete(request, queue_id):

    user_context = UserContextFull(request)
    logger.info(str.format('queue delete : {0}' .format(user_context.id)))

    # queue_id = queue_id
    # queue_name = request.POST.get('frmqueueName')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_queue'):

        queue_update = Queue.objects.get(queueid=queue_id, clientid=user_context.clientID)
        queue_update.deleteddate = deleted_date
        queue_update.deletedby = deleted_by
        queue_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'queue_id': queue_id}

    else:

        raise serializers.ValidationError('You are not authorised to delete queues')

    return Response(response)


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('queue update : {0}' .format(user_context.id)))

    queue_id = request.POST.get('hidQueueID')
    queue_name = request.POST.get('frmQueueName')
    queue_description = request.POST.get('frmQueueDescription')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    queue_serializer = APIQueueSerializer(data={'queueid': 0, 'clientid': user_context.clientID, 'queuename': queue_name,
                                                'queuedescription': queue_description,
                                                'updateddate': updated_date, 'updatedby': updated_by})

    if queue_serializer.is_valid():

        queue_update = Queue.objects.get(clientid=user_context.clientID, queueid=queue_id)
        queue_update.queuename = queue_name
        queue_update.queuedescription = queue_description
        queue_update.updateddate = updated_date
        queue_update.updatedby = updated_by
        queue_update.save(update_fields=['queuename', 'queuedescription', 'updateddate', 'updatedby'])

        response = {'queue_id': queue_id}

    else:

        raise serializers.ValidationError(queue_serializer.errors)

    return Response(response)


@api_view(['POST'])
def member_create(request):

    user_context = UserContextFull(request)
    logger.info(str.format('queue member create : {0}' .format(user_context.id)))

    queue_id = request.POST.get('hidQueueID')
    queue_member = request.POST.get('selQueueMember')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    queue_row = Queue.objects.get(queueid=queue_id, clientid=user_context.clientID)
    # research-code: join on two tables
    user_row = AuthUser.objects.get(id=queue_member)
    queue_member_serializer = APIQueueUserSerializer(data={'queueid': queue_row.queueid, 'queueuserid': queue_member, 'clientid': user_context.clientID})
    member_changed_id = None
    if queue_member_serializer.is_valid():

        member_new = QueueUser(queueid=queue_row, queueuserid=queue_member, clientid=user_context.clientID, createddate=created_date, createdby=created_by)
        # check if the user already exists bit has been deleted before
        try:
            # if member exists set deleted date to null to resinstate
            member_exists = QueueUser.objects.get(queueuserid=queue_member)
            member_exists.deleteddate = None
            member_exists.deletedby = None
            member_exists.save()
            member_changed_id = member_exists.id
        except:
            # member does nto exists so add to queueuser table
            member_new.save()
            member_changed_id = member_new.id

        response = member_changed_id

    else:

        raise serializers.ValidationError(queue_member_serializer.errors)

    return Response(response)


@api_view(['POST'])
def member_delete(request):

    user_context = UserContextFull(request)
    logger.info(str.format('queue member delete : {0}' .format(user_context.id)))

    id = request.POST.get('id')
    queue_id = request.POST.get('queue_id')
    queue_member_id = request.POST.get('queue_member_id')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_queue'):

        queue_member_update = QueueUser.objects.get(queueid=queue_id, clientid=user_context.clientID, queueuserid=queue_member_id, deletedby__isnull=True)
        queue_member_update.deleteddate = deleted_date
        queue_member_update.deletedby = deleted_by
        queue_member_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'queue_id': queue_id}

    else:

        raise serializers.ValidationError('You are not authorised to delete queue members')

    return Response(response)


@api_view(['POST'])
def team_create(request):

    user_context = UserContextFull(request)
    logger.info(str.format('queue member create : {0}' .format(user_context.id)))

    queue_id = request.POST.get('hidQueueID')
    queue_team = request.POST.get('selQueueTeam')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    queue = Queue.objects.get(queueid=queue_id, clientid=user_context.clientID)
    team = Team.objects.get(teamid=queue_team, clientid=user_context.clientID)
    queue_team_serializer = APIQueueTeamSerializer(data={'queueid': queue.queueid, 'queueteamid': queue_team, 'clientid': user_context.clientID})
    if queue_team_serializer.is_valid():

        member_new = TeamQueue(queueid=queue, queueteamid=team, clientid=user_context.clientID, createddate=created_date, createdby=created_by)
        member_new.save()

        response = member_new.id

    else:

        raise serializers.ValidationError(queue_team_serializer.errors)

    return Response(response)


@api_view(['POST'])
def team_delete(request):

    user_context = UserContextFull(request)
    logger.info(str.format('queue member delete : {0}' .format(user_context.id)))

    id = request.POST.get('id')
    queue_id = request.POST.get('queue_id')
    queue_team_id = request.POST.get('queue_team_id')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_queue'):

        queue_team_update = TeamQueue.objects.get(queueteamid=queue_team_id, queueid=queue_id, clientid=user_context.clientID, deletedby__isnull=True)
        queue_team_update.deleteddate = deleted_date
        queue_team_update.deletedby = deleted_by
        queue_team_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'team_id': id}

    else:

        raise serializers.ValidationError('You are not authorised to delete queue members')

    return Response(response)
