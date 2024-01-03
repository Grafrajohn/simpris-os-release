import logging
import time

from django.contrib.auth.models import User, Group
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db.models import Q

from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view

from simpris.api.link.serializers import LinkSerializer
from simpris.models.models import Link, Project
from simpris.library.user_context import UserContextFull
from simpris.library import emailer


logger = logging.getLogger(__name__)


@api_view(['GET'])
def list(request, entity_id, entity_type):
    user_context = UserContextFull(request)
    logger.info(str.format('link list : {0}'.format(user_context.id)))

    try:
        int(entity_id)
    except:
        raise Exception("Invalid entity id in call to get links")

    try:
        int(entity_type)
    except:
        raise Exception("Invalid entity type in call to get links")

    queryset = Link.objects.all().filter(Q(clientid=user_context.clientID, entityid=entity_id, entitytype=entity_type) & Q(deleteddate__isnull=True))
    serializer_class = LinkSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['DELETE'])
def delete(request, link_id):
    user_context = UserContextFull(request)
    logger.info(str.format('link delete : {0}' .format(user_context.id)))

    link_id = link_id
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    link_serializer = LinkSerializer(data={'id': 0,
                                        'clientid': user_context.clientID,
                                        'entityid': 0,
                                        'entitytype': 0,
                                        'link_name': 'NAME',
                                        'link_url': 'DESC',
                                        'link_target': 'TG',
                                        'createdby': deleted_by,
                                        'createddate': deleted_date,
                                        'deletedby': deleted_by,
                                        'deleteddate': deleted_date})

    user = User.objects.get(id=request.user.id)
    if link_serializer.is_valid() and (user.has_perm('simpris.delete_link')):

        lnk = Link.objects.get(id=link_id, clientid=user_context.clientID)
        lnk.deletedby = deleted_by
        lnk.deleteddate = deleted_date
        lnk.save(
            update_fields=['deleteddate', 'deletedby'])

        messages.success(request._request, 'Link deleted')

        response = link_id

    else:
        errors = link_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(link_serializer.errors)

    return Response(response)


@api_view(['POST'])
def insert(request):
    user_context = UserContextFull(request)
    logger.info(str.format('link insert : {0}' .format(user_context.id)))

    link_id = 0
    entity_id = request.POST.get('hidItemID')
    entity_type = request.POST.get('hidItemType')
    link_name = request.POST.get('txtLinkName')
    link_url = request.POST.get('txtLinkURL')
    link_target = '_new'
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    link_url_processed = ""
    if link_url.find('http') != -1:
        link_url_processed = link_url
    elif link_url.find('https') != -1:
        link_url_processed = link_url
    else:
        link_url_processed = 'http://' + link_url

    link_serializer = LinkSerializer(data={'id': link_id,
                                                    'clientid': user_context.clientID,
                                                    'entityid': entity_id,
                                                    'entitytype': 2,
                                                    'link_name': link_name,
                                                    'link_url': link_url_processed,
                                                    'link_target': link_target,
                                                    'createdby': created_by,
                                                    'createddate': created_date})

    if link_serializer.is_valid():

        link_new = Link(clientid=user_context.clientID,
                        entityid=entity_id, entitytype=2,
                        link_name=link_name, link_url=link_url_processed,
                        link_target=link_target,
                        createdby=created_by, createddate=created_date)
        link_new.save(force_insert=True)

        link_object = Link.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('id')

        messages.success(request._request, 'Link successfully created')

        response = {'link_id': link_object.id}

    else:
        errors = link_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        response = {'responseText': link_serializer.errors}

    return Response(response)


@api_view(['PUT'])
def update(request, link_id):
    user_context = UserContextFull(request)
    logger.info(str.format('link update : {0}' .format(user_context.id)))

    link_id = request.POST.get('hidLinkID')
    link_name = request.POST.get('frmLinkName')
    link_url = request.POST.get('frmLinkURL')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    link_serializer = LinkSerializer(data={'id': link_id,
                                                    'clientid': user_context.clientID,
                                                    'linkname': link_name,
                                                    'linkurl': link_url,
                                                    'createdby': updated_by,
                                                    'createddate': updated_date})

    if link_serializer.is_valid():

        lnk = Link.objects.get(id=link_id)
        lnk.linkname = link_name
        lnk.linkurl = link_url
        lnk.updatedby = updated_by
        lnk.updateddate = updated_date
        lnk.save(
            update_fields=['linkname', 'linkurl', 'updateddate', 'updatedby'])

        messages.success(request._request, 'Link successfully updated.')

        response = link_id

    else:
        errors = link_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(link_serializer.errors)

    return Response(response)
