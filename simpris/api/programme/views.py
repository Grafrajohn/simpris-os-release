# from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets, serializers
from simpris.api.programme.serializers import VProgrammesSerializer
from simpris.models.db_views import VMyProgrammes
from simpris.models.models import Organisation, Programme
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.models import User
import time
import logging

logger = logging.getLogger(__name__)


class APIProgrammeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = '__all__'


class APIProgrammeSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ('programmeid', 'clientid', 'programmename', 'programmedescription', 'createdby')


@api_view(['GET'])
def programmes(request):
    
    user_context = UserContextFull(request)
    logger.info(str.format('Programme list : {0}' .format(user_context.id)))
    
    queryset = Programme.objects.all().filter(Q(clientid=user_context.clientID), Q(deletedby__isnull=True)).order_by('programmename')
    serializer_class = VProgrammesSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):
    user_context = UserContextFull(request)
    logger.info(str.format('Programme insert : {0}' .format(user_context.id)))

    programme_id = 0
    programme_name = request.POST.get('frmProgrammeName')
    programme_description = request.POST.get('frmProgrammeDescription')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    #organisation = Organisation.objects.get(organisationid=organisation_id)

    programme_serializer = APIProgrammeSerializer(data={'programmeid': programme_id,
                                                    'clientid': user_context.clientID,
                                                    'programmename': programme_name,
                                                    'programmedescription': programme_description,
                                                    'assignedto': 0, 'createdby': created_by,
                                                    'createddate': created_date})

    if programme_serializer.is_valid():

        programme_new = Programme(clientid=user_context.clientID, programmedescription=programme_description,
                      programmename=programme_name,
                      createdby=created_by, createddate=created_date)
        programme_new.save(force_insert=True)

        programme_object = Programme.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('programmeid')

        messages.success(request._request, 'Programme successfully created')

        response = {'programme_id': programme_object.programmeid}

    else:

        raise serializers.ValidationError(programme_serializer.errors)
        # response = {'responseText': programme_serializer.errors}

    return Response(response)


@api_view(['GET','POST'])
def delete(request,programme_id):
    user_context = UserContextFull(request)
    logger.info(str.format('Programme delete : {0}' .format(user_context.id)))

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_programme'):

        deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
        deleted_by = user_context.id

        prog = Programme.objects.get(programmeid=programme_id, clientid=user_context.clientID)
        prog.deletedby = deleted_by
        prog.deleteddate = deleted_date
        prog.save()

        #messages.success(request._request, 'Programme successfully deleted')

        response = {'programme_id': prog.programmeid}

    else:
        raise serializers.ValidationError("User is not authorised to delete Programme")

    return Response(response)


@api_view(['POST'])
def update(request):
    user_context = UserContextFull(request)
    logger.info(str.format('Programme update : {0}' .format(user_context.id)))

    programme_id = request.POST.get('hidProgrammeID')
    # organisation_id = request.POST.get('hidOrganisationID')
    programme_name = request.POST.get('frmProgrammeName')
    programme_description = request.POST.get('frmProgrammeDescription')

    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    programme_serializer = APIProgrammeSerializer2(data={# 'Programmeid': programme_id,
                                                    'clientid': user_context.clientID,
                                                    'programmename': programme_name,
                                                    'programmedescription': programme_description,
                                                    'updateddate': updated_date,
                                                    'updatedby': updated_by,
                                                    'createddate': updated_date,
                                                    'createdby': updated_by})

    if programme_serializer.is_valid():

        prog = Programme.objects.get(programmeid=programme_id)
        prog.programmename = programme_name
        prog.programmedescription = programme_description

        prog.updatedby = updated_by
        prog.updateddate = updated_date
        prog.save()

        messages.success(request._request, 'Programme successfully updated')

        response = {'programme_id': prog.programmeid}

    else:

        raise serializers.ValidationError(programme_serializer.errors)

    return Response(response)
