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
from simpris.api.phase.serializers import PhaseSerializer
from simpris.models.models import Phase
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view


logger = logging.getLogger(__name__)


# serializer for phases
class APIPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = ('phaseid', 'clientid', 'phasename', 'phasedescription', 'startdate', 'enddate', 'updateddate', 'updatedby')


@api_view(['GET'])
def phaselist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('phase list : {0}' .format(user_context.id)))

    queryset = Phase.objects.all().filter(Q(clientid=user_context.clientID) & Q(deleteddate__isnull=True))\
        .order_by('startdate')
    serializer_class = PhaseSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('phase create : {0}' .format(user_context.id)))

    phase_name = request.POST.get('frmPhaseName')
    phase_description = request.POST.get('frmPhaseDescription')
    client_id = user_context.clientID
    phase_startdate = request.POST.get('frmDatePicker') + "T00:00"
    phase_enddate = request.POST.get('frmDatePicker2') + "T00:00"
    phase_startdate = phase_startdate.replace('/', '-')
    phase_enddate = phase_enddate.replace('/', '-')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    phase_serializer = APIPhaseSerializer(data={'phasename': phase_name, 'phasedescription': phase_description,
                                    'startdate': phase_startdate, 'enddate': phase_enddate,
                                    'clientid': client_id, 'createddate': created_date, 'createdby': created_by,
                                    'updateddate': created_date, 'updatedby': created_by})

    if phase_serializer.is_valid():

        phase_new = Phase(clientid=client_id, phasename=phase_name, phasedescription=phase_description,
                    startdate=phase_startdate, enddate=phase_enddate,
                    createddate=created_date, createdby=created_by)
        phase_new.save()

        phase_object = Phase.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('phaseid')

        response = {'phase_id': phase_object.phaseid}

    else:

        raise serializers.ValidationError(phase_serializer.errors)

    return Response(response)


@api_view(['GET'])
def delete(request, phase_id):

    user_context = UserContextFull(request)
    logger.info(str.format('phase delete : {0}' .format(user_context.id)))

    # phase_name = request.POST.get('frmphaseName')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    user = User.objects.get(id=request.user.id)
    if user.has_perm('simpris.delete_phase'):

        phase_update = Phase.objects.get(phaseid=phase_id, clientid=user_context.clientID)
        # phase_update.phasename = phase_name
        phase_update.deleteddate = deleted_date
        phase_update.deletedby = deleted_by
        phase_update.save(update_fields=['deleteddate', 'deletedby'])

        response = {'phase_id': phase_id}

    else:

        raise serializers.ValidationError('You are not authorised to delete client phases')

    return Response(response)


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('phase update : {0}' .format(user_context.id)))

    phase_id = request.POST.get('hidPhaseID')
    phase_name = request.POST.get('frmPhaseName')
    phase_description = request.POST.get('frmPhaseDescription')
    phase_startdate = request.POST.get('frmDatePicker') + "T00:00"
    phase_enddate = request.POST.get('frmDatePicker2') + "T00:00"
    phase_startdate = phase_startdate.replace('/', '-')
    phase_enddate = phase_enddate.replace('/', '-')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    phase_serializer = APIPhaseSerializer(data={'clientid': user_context.clientID, 'phasename': phase_name,
                                                'phasedescription': phase_description, 'startdate': phase_startdate,
                                                'enddate': phase_enddate,
                                                'updateddate': updated_date, 'updatedby': updated_by})

    if phase_serializer.is_valid():

        phase_update = Phase.objects.get(clientid=user_context.clientID, phaseid=phase_id)
        phase_update.phasename = phase_name
        phase_update.phasedescription = phase_description
        phase_update.startdate = phase_startdate
        phase_update.enddate = phase_enddate
        phase_update.updateddate = updated_date
        phase_update.updatedby = updated_by
        phase_update.save(update_fields=['phasename', 'phasedescription', 'startdate', 'enddate', 'updateddate', 'updatedby'])

        response = {'phase_id': phase_id}

    else:

        raise serializers.ValidationError(phase_serializer.errors)

    return Response(response)
