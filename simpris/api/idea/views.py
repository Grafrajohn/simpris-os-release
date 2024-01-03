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
from simpris.api.idea.serializers import IdeaSerializer
from simpris.library.user_context import UserContextFull
from simpris.models.models import Idea

logger = logging.getLogger(__name__)


# serializer for ideas
class APIIdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'clientid', 'parentid', 'parenttypeid', 'name', 'description', 'updateddate', 'updatedby')


@api_view(['GET'])
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('idea list : {0}' .format(user_context.id)))

    proj_id = request.query_params.get('proj_id')

    queryset = Idea.objects.all().filter(Q(clientid=user_context.clientID) & Q(parentid=proj_id) & Q(deleteddate__isnull=True))\
        .order_by('id')
    serializer_class = IdeaSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('idea create : {0}' .format(user_context.id)))

    idea_name = request.POST.get('id')
    idea_description = request.POST.get('frmideaDescription')
    parentid = request.POST.get('parent_id')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    idea_serializer = APIIdeaSerializer(data={'id': 0, 'name': idea_name, 'description': idea_description,
                                    'parentid': parentid, 'parenttypeid': 1,
                                    'clientid': client_id, 'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if idea_serializer.is_valid():

        idea_new = Idea(clientid=client_id, name=idea_name, description=idea_description,
                    parentid=parentid, parenttypeid=1,
                    createddate=created_date, createdby=created_by)
        idea_new.save()

        idea_object = Idea.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('id')

        response = {'idea_id': idea_object.id}

    else:

        raise serializers.ValidationError(idea_serializer.errors)

    return Response(response)


@api_view(['POST'])
def delete(request):

    user_context = UserContextFull(request)
    logger.info(str.format('idea delete : {0}' .format(user_context.id)))

    idea_name = request.POST.get('id')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    try:
        idea_update = Idea.objects.get(name=idea_name, clientid=user_context.clientID)
        idea_update.deleteddate = deleted_date
        idea_update.deletedby = deleted_by
        idea_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'idea_id': idea_name}

        return Response(response)
    except:
        raise


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('idea update : {0}' .format(user_context.id)))

    # = request.POST.get('ideaid')
    idea_name = request.POST.get('name')
    idea_description = request.POST.get('content')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    idea_serializer = APIIdeaSerializer(data={'id': 0, 'clientid': user_context.clientID, 'name': idea_name,
                                                'description': idea_description, 'parentid': 1,
                                                'parenttypeid': 1,
                                                'updateddate': updated_date, 'updatedby': updated_by})

    if idea_serializer.is_valid():

        idea_update = Idea.objects.get(clientid=user_context.clientID, name=idea_name)
        idea_update.name = idea_name
        idea_update.description = idea_description
        idea_update.updateddate = updated_date
        idea_update.updatedby = updated_by
        idea_update.save(update_fields=['name', 'description', 'updateddate', 'updatedby'])

        response = {'idea_id': idea_name}

    else:

        raise serializers.ValidationError(idea_serializer.errors)

    return Response(response)
