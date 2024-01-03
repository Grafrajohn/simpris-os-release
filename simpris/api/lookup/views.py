import time
from django.db.models import Q
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view
from simpris.api.lookup.serializers import LookupSerializer
from simpris.models.models import Lookup, LookupType
from simpris.library.user_context import UserContextFull


import logging

logger = logging.getLogger(__name__)


class APILookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lookup
        fields = '__all__'


class APILookupTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LookupType
        fields = '__all__'


@api_view(['GET'])
def lookups(request, lookup_type_id):
    user_context = UserContextFull(request)
    logger.info(str.format('lookup list by type : {0}'.format(user_context.id)))

    queryset = Lookup.objects.all().filter(Q(lookuptypeid=lookup_type_id) & Q(deleteddate__isnull=True) &
                                             Q(clientid=0)).order_by('lookuporder').distinct()
    serializer_class = LookupSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def list(request):
    user_context = UserContextFull(request)
    logger.info(str.format('lookup list all : {0}'.format(user_context.id)))

    queryset = Lookup.objects.all().filter(Q(deleteddate__isnull=True) &
                                           (Q(clientid=0) | Q(clientid=user_context.clientID))).order_by('lookuporder')
    serializer_class = APILookupSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def lookuptypes(request):
    user_context = UserContextFull(request)
    logger.info(str.format('lookuptype list all : {0}'.format(user_context.id)))

    queryset = LookupType.objects.all().filter(Q(deleteddate__isnull=True)).order_by('lookuptype')
    serializer_class = APILookupTypeSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):
    user_context = UserContextFull(request)
    logger.info(str.format('lookup insert : {0}'.format(user_context.id)))

    disabled = request.POST.get('disabled')
    lookuptypeid = request.POST.get('lookupTypeID')
    #lookupsubtypeid = request.POST.get('lookupSubTypeID')
    lookuporder = request.POST.get('lookupOrder')
    #lookupvaluenum = request.POST.get('lookupValueNum')
    lookupvaluechar = request.POST.get('lookupValueChar')
    lookupdescription = request.POST.get('lookupDescription')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    try:
        lookup_subtype = Lookup.objects.filter(clientid=user_context.clientID, lookuptypeid=lookuptypeid).latest('id')
        lookupsubtypeid = lookup_subtype.lookupsubtypeid
        lookupvaluenum = lookup_subtype.lookupvaluenum
    except:
        lookupsubtypeid = 0
        lookupvaluenum = 0

    lookupsubtypeid = lookupsubtypeid + 1
    lookupvaluenum = lookupvaluenum + 1

    lookup_serializer = APILookupSerializer(data={'id': 0, 'clientid': client_id,
                                    'lookuptypeid': lookuptypeid, 'lookupsubtypeid': lookupsubtypeid,
                                    'lookuporder': lookuporder, 'lookupvaluenum': lookupvaluenum,
                                    'lookupvaluechar': lookupvaluechar,
                                    'lookupdescription': lookupdescription,
                                    'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if lookup_serializer.is_valid():

        lookup_new = Lookup(clientid=client_id, lookuptypeid=lookuptypeid, lookupsubtypeid=lookupsubtypeid,
                    lookuporder=lookuporder, lookupvaluenum=lookupvaluenum, lookupdescription=lookupdescription,
                    lookupvaluechar=lookupvaluechar, createddate=created_date, createdby=created_by)
        lookup_new.save()

        lookup_object = Lookup.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('id')

        response = {'lookup_id': lookup_object.id}

    else:

        logger.warning('Lookup serializer invalid on insert')
        raise serializers.ValidationError(lookup_serializer.errors)

    return Response(response)


@api_view(['POST'])
def update(request):
    user_context = UserContextFull(request)
    logger.info(str.format('lookup update : {0}'.format(user_context.id)))

    disabled = request.POST.get('disabled')
    lookuptypeid = request.POST.get('lookupTypeID')
    lookupsubtypeid = request.POST.get('lookupSubTypeID')
    lookuporder = request.POST.get('lookupOrder')
    lookupvaluenum = request.POST.get('lookupValueNum')
    lookupvaluechar = request.POST.get('lookupValueChar')
    lookupdescription = request.POST.get('lookupDescription')
    id = request.POST.get('id')
    client_id = user_context.clientID
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    lookup_serializer = APILookupSerializer(data={'id': id, 'clientid': client_id,
                                    'lookuptypeid': lookuptypeid, 'lookupsubtypeid': lookupsubtypeid,
                                    'lookuporder': lookuporder, 'lookupvaluenum': lookupvaluenum,
                                    'lookupvaluechar': lookupvaluechar,
                                    'lookupdescription': lookupdescription,
                                    'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if lookup_serializer.is_valid():

        lookup_update = Lookup.objects.get(id=id)
        lookup_update.lookupvaluenum = lookupvaluenum
        lookup_update.lookupvaluechar = lookupvaluechar
        lookup_update.save(update_fields=['lookupvaluechar', 'lookupvaluenum'])

        response = {'lookup_id': lookup_update.id}

    else:

        logger.warning('Lookup invalid on update')
        raise serializers.ValidationError(lookup_serializer.errors)

    return Response(response)
