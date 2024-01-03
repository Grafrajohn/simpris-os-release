# python imports
import logging, time, pytz

from django.contrib.auth.models import User
# django imports
from django.db.models import Q
from rest_framework import serializers
from rest_framework.decorators import api_view
# rest imports
from rest_framework.response import Response

# simpris imports
from simpris.api.interaction.serializers import InteractionSerializer, InteractionsSerializer
from simpris.library.user_context import UserContextFull
from simpris.models.models import Interaction
from ...models.db_views import VInteractions

logger = logging.getLogger(__name__)


# serializer for interactions
class APIInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ('interactionid', 'clientid', 'userid', 'organisationid', 'interactiontypeid', 'details', 'createddate')

@api_view(['GET'])
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('interaction list : {0}' .format(user_context.id)))

    queryset = VInteractions.objects.all().filter(Q(clientid=user_context.clientID) & Q(deleteddate__isnull=True))\
        .order_by('createddate').reverse()
    serializer_class = InteractionsSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def detail(request):
    user_context = UserContextFull(request)
    logger.info(str.format('interaction detail : {0}' .format(user_context.id)))

    interaction_id = request.query_params.get('int_id')

    queryset = Interaction.objects.all().filter(Q(clientid=user_context.clientID) & Q(interactionid=interaction_id)).order_by('createddate')
    serializer_class = InteractionSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('interaction create : {0}' .format(user_context.id)))

    details = request.POST.get('details')
    interactiontypeid = request.POST.get('type')
    client_id = user_context.clientID
    created_date = timezone.localtime() #time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    interaction_serializer = APIInteractionSerializer(data={'interactionid': 0, 'clientid': client_id, 'userid': user_context.id,
                                    'interactiontypeid': interactiontypeid, 'organisationid': user_context.organisationID,
                                    'details': details, 'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if interaction_serializer.is_valid():

        interaction_new = Interaction(clientid=client_id, organisationid=user_context.organisationID, details=details,
                    userid=user_context.id, interactiontypeid=interactiontypeid, createddate=created_date, createdby=created_by)
        interaction_new.save()

        interaction_object = Interaction.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('interactionid')

        response = {'interaction_id': interaction_object.id}

    else:

        raise serializers.ValidationError(interaction_serializer.errors)

    return Response(response)

