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
from simpris.api.error.serializers import ErrorSerializer, ErrorsSerializer
from simpris.library.user_context import UserContextFull
from simpris.models.models import Error
from ...models.db_views import VErrors

logger = logging.getLogger(__name__)


# serializer for Errors
class APIErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ('Errorid', 'clientid', 'userid', 'organisationid', 'Errortypeid', 'details', 'createddate')


@api_view(['GET'])
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('Error list : {0}' .format(user_context.id)))

    queryset = VErrors.objects.all().filter(Q(clientid=user_context.clientID) & Q(deleteddate__isnull=True))\
        .order_by('createddate').reverse()
    serializer_class = ErrorsSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def detail(request):
    user_context = UserContextFull(request)
    logger.info(str.format('Error detail : {0}' .format(user_context.id)))

    Error_id = request.query_params.get('int_id')

    queryset = Error.objects.all().filter(Q(clientid=user_context.clientID) & Q(Errorid=Error_id)).order_by('createddate')
    serializer_class = ErrorSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('Error create : {0}' .format(user_context.id)))

    description = request.POST.get('description')
    module = request.POST.get('module')
    submodule = request.POST.get('submodule')
    action = request.POST.get('action')
    subaction = request.POST.get('subaction')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')

    Error_serializer = APIErrorSerializer(data={'Errorid': 0, 'clientid': client_id, 'userid': user_context.id,
                                    'description': description, 'organisationid': user_context.organisationID,
                                    'module': module, 'submodule': submodule, 'action': action,
                                    'subaction': subaction, 'createddate': created_date})

    if Error_serializer.is_valid():

        Error_new = Error(clientid=client_id, organisationid=user_context.organisationID, description=description,
                    userid=user_context.id, module=module, submodule=submodule, action=action,
                    subaction=subaction, createddate=created_date)
        Error_new.save()

        Error_object = Error.objects.filter(clientid=user_context.clientID, userid=user_context.id).latest('Errorid')

        response = {'Error_id': Error_object.id}

    else:

        raise serializers.ValidationError(Error_serializer.errors)

    return Response(response)

