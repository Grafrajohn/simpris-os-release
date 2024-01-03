import logging, time, pytz

from django.utils import timezone

from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.decorators import api_view

from simpris.models.models import Task
from simpris.library.user_context import UserContextFull

logger = logging.getLogger(__name__)


class APITaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('taskid', 'clientid', 'phaseid', 'tasktypeid', 'tasklistid', 'taskname', 'taskname', 'taskdescription', 'createddate', 'createdby', 'updateddate', 'updatedby')
        model = Task


@api_view(['POST'])
def move(request):

    user_context = UserContextFull(request)
    logger.info(str.format('schedule move : {0}' .format(user_context.id)))

    task_id = request.POST.get('task_id')
    phase_id = request.POST.get('phase_id')

    updatedDate = timezone.localtime() #time.strftime('%Y-%m-%d %H:%M:%S')
    updatedBy = user_context.id

    taskSerializer = APITaskSerializer(data={'clientid': user_context.clientID, 'tasktypeid': 0,
        'tasklistid': 1, 'taskname': 'Dummy', 'taskdescription': 'Dummy',
         'createddate': updatedDate, 'createdby': updatedBy,
        'taskid': task_id, 'phaseid': phase_id, 'updateddate': updatedDate, 'updatedby': updatedBy})

    if taskSerializer.is_valid():

        tk = Task.objects.get(clientid=user_context.clientID, taskid=task_id)
        tk.phaseid = phase_id
        tk.updatedby = updatedBy
        tk.updateddate = updatedDate

        tk.save(update_fields=['phaseid', 'updatedby', 'updateddate'])

        response = {'task_id': task_id}

    else:
        #for serialError in taskSerializer.errors():
            #logger.error(str.format('schedule move : {0}', serialError))
        logger.error('schedule move error')
        response = {'responseText': taskSerializer.errors}

    return Response(response)
