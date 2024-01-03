import time
import logging
import pytz

from django.db.models import Q
from django.utils import timezone

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view

from simpris.api.lookup.serializers import LookupSerializer
from simpris.models.models import Useractivity
from simpris.library.user_context import UserContextFull

logger = logging.getLogger(__name__)


class APIUserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Useractivity
        fields = '__all__'


@api_view(['GET'])
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('activity list : {0}'.format(user_context.id)))

    queryset = Useractivity.objects.all().order_by('activityid')
    serializer_class = APIUserActivitySerializer(queryset, many=True)

    return Response(serializer_class.data)

