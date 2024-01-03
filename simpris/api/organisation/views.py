from django.contrib.auth import hashers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import viewsets, serializers, permissions
from simpris.api.organisation.serializers import OrganisationSerializer, VClientsSerializer
from simpris.models.models import Organisation, Client, Userorganisation
from simpris.models.db_views import VMyOrganisations
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view
from django.db.models import Q
import time, datetime, math

import logging

logger = logging.getLogger(__name__)


# serializer for organisations
class APIOrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('organisationname','updateddate','updatedby')


class APIUserOrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userorganisation
        fields = ('userid','organisationid')


@api_view(['GET'])
def organisations(request):
    user_context = UserContextFull(request)
    logger.info(str.format('organisation list : {0}' .format(user_context.id)))

    queryset = VMyOrganisations.objects.all().filter(clientid=user_context.clientID, userid=user_context.id,
                                                     deleteddate__isnull=True).order_by('organisationname')
    serializer_class = VClientsSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('organisation create : {0}' .format(user_context.id)))

    organisation_name = request.POST.get('frmOrganisationName')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    client = Client.objects.get(clientid=client_id)

    organisation_serializer = APIOrganisationSerializer(data={'organisationname': organisation_name,
                          'clientid': client_id, 'createddate': created_date,'createdby': created_by,
                          'updateddate': created_date, 'updatedby': created_by})

    if organisation_serializer.is_valid():

        organisation_new = Organisation(clientid=client,organisationname=organisation_name,
                                        createddate=created_date,createdby=created_by)
        organisation_new.save()

        organisation_object = Organisation.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('organisationid')
        userorganisation_new = Userorganisation(userid=created_by,organisationid=organisation_object,
                                                                  createdby=created_by,createddate=created_date,
                                                updatedby=created_by,updateddate=created_date)
        userorganisation_new.save()

        response = {'organisation_id': organisation_object.organisationid}

    else:

        raise serializers.ValidationError(organisation_serializer.errors)

    return Response(response)


@api_view(['GET'])
def delete(request, org_id):

    user_context = UserContextFull(request)
    logger.info(str.format('organisation delete : {0}' .format(user_context.id)))

    organisation_id = org_id
    # organisation_name = request.POST.get('frmOrganisationName')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_organisation'):
        if user_context.organisationID != int(org_id):
            organisation_update = Organisation.objects.get(organisationid=organisation_id, clientid=user_context.clientID)
            # organisation_update.organisationname = organisation_name
            organisation_update.deleteddate = deleted_date
            organisation_update.deletedby = deleted_by
            organisation_update.save(update_fields=['deleteddate','deletedby'])

            response = {'organisation_id': organisation_id}
        else:

            raise serializers.ValidationError('You are not authorised to delete this organisation')

    else:

        raise serializers.ValidationError('You are not authorised to delete client organisations')

    return Response(response)


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('organisation update : {0}' .format(user_context.id)))

    organisation_id = request.POST.get('hidOrganisationID')
    organisation_name = request.POST.get('frmOrganisationName')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    # organisation = Organisation.objects.get(organisationid=organisation_id)

    organisation_serializer = APIOrganisationSerializer(data={'organisationname': organisation_name, 'updateddate': updated_date, 'updatedby': updated_by})

    if organisation_serializer.is_valid():

        organisation_update = Organisation.objects.get(organisationid=organisation_id)
        organisation_update.organisationname = organisation_name
        organisation_update.updateddate = updated_date
        organisation_update.updatedby = updated_by
        organisation_update.save(update_fields=['organisationname','updateddate','updatedby'])

        response = {'organisation_id': organisation_id}

    else:

        raise serializers.ValidationError(organisation_serializer.errors)

    return Response(response)


@api_view(['POST'])
def deleteuser(request):

    user_context = UserContextFull(request)
    logger.info(str.format('organisation user delete : {0}' .format(user_context.id)))

    organisation_id = request.POST.get('hidUserOrganisationID')
    user_id = request.POST.get('organisation_user_id')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    organisation_user = Userorganisation.objects.get(organisationid=organisation_id, userid=user_id, deletedby__isnull = True)

    #organisation_user_serializer = APIUserOrganisationSerializer(data={'organisationid': organisation_id, 'userid': user_id, 'updateddate': updated_date, 'updatedby': updated_by})

    if organisation_user != None:
        organisation_user.deleteddate = updated_date
        organisation_user.deletedby = user_context.id
        organisation_user.save()
    else:
        raise Exception("User not found")

    return Response(0)


@api_view(['POST'])
def adduser(request):

    user_context = UserContextFull(request)
    logger.info(str.format('organisation user add : {0}' .format(user_context.id)))

    organisation_id = request.POST.get('hidUserOrganisationID')
    user_id = request.POST.get('selOrganisationUser')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    if Userorganisation.objects.filter(organisationid=organisation_id, userid=user_id, deletedby__isnull=True).exists():
    # if organisation_user:
        raise Exception('User already set for this organisation')

    organisation = Organisation.objects.get(organisationid=organisation_id)

    organisation_user_serializer = APIUserOrganisationSerializer(data={'organisationid': organisation_id, 'userid': user_id, 'updateddate': updated_date, 'updatedby': updated_by})

    if organisation_user_serializer.is_valid():
        userorganisation_new = Userorganisation(userid=user_id,organisationid=organisation,
                                                createdby=updated_by,createddate=updated_date)
        userorganisation_new.save()
    else:
        raise serializers.ValidationError(organisation_user_serializer.errors)

    return Response(0)
