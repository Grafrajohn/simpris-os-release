from rest_framework.response import Response
from simpris.api.time.serializers import VCalendarSerializer, VTimegridSerializer, VTimetaskSerializer, \
    VTimelistSerializer
from simpris.models.db_views import VTimeCalendar, VTimeGrid, VTimeTask, VMyTime
from simpris.models.models import Time, Task
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view
from rest_framework import viewsets, serializers
# from django.template.context_processors import csrf
from datetime import datetime
from django.db.models import Q
import time, datetime
import logging

logger = logging.getLogger(__name__)


# serializer for time
class APITimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('timeday', 'hours', 'taskid', 'timetypeid', 'userid', 'comments')


@api_view(['GET'])
def calendar(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext)     
    
    queryset = VTimeCalendar.objects.all().filter((Q(userid=userContext.id) | Q(assignedto=userContext.id)), clientid=userContext.clientID,
                                                  start__isnull=False)
    serializer_class = VCalendarSerializer(queryset, many=True)

    return Response(serializer_class.data)


def teamcalendar(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext)     
    
    queryset = VTimeCalendar.objects.all().filter(userid=userContext.id)
    serializer_class = VCalendarSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def timegrid(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext)
     
    rawDate = request.GET["indate"]
    indate = rawDate.replace('/', '-')
    
    queryset = VTimeGrid.objects.all().filter(clientid=userContext.clientID, assignedto=userContext.id,
                                              timedaydate=indate)
    serializer_class = VTimegridSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def timetask(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext)     
    
    queryset = VTimeTask.objects.all().filter(clientid=userContext.clientID, assignedto=userContext.id)
    serializer_class = VTimetaskSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def save_timegrid(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext) 
    
    c = {}
    c.update(csrf(request))    
    
    queryset = VTimeTask.objects.all().filter(assignedto=userContext.id)
    serializer_class = VTimetaskSerializer(queryset, many=True)

    return Response(serializer_class.data, c)   


@api_view(['GET'])
def delete(request, time_id):

    userContext = UserContextFull(request)
    logger.info(userContext)

    dateDeleted = time.strftime('%Y-%m-%d %H:%M:%S')

    queryset = Time.objects.get(timeid=time_id, clientid=userContext.clientID)
    queryset.deletedby=userContext.id
    queryset.deleteddate=dateDeleted
    queryset.save()

    return Response("OK")


@api_view(['POST'])
def delete_time(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext) 
    
    dateDeleted = time.strftime('%Y-%m-%d %H:%M:%S')
    
    queryset = Time.objects.get(timeid=request.data["timeid"], clientid=userContext.clientID)
    queryset.deletedby=userContext.id
    queryset.deleteddate=dateDeleted
    queryset.save()
    
    return Response("OK")    


@api_view(['POST'])
def update_time(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext) 
    
    queryTime = request.data["frmdate"].replace('/', '-')
    timeday = queryTime + ' ' + str(request.data["starthour"]) + ':' + str(request.data["startmin"])
    dateUpdated = time.strftime('%Y-%m-%d %H:%M:%S')
    hoursin = float(request.data["hours"]) + float(request.data["mins"])    
       
    queryset = Time.objects.get(timeid=request.data["timeid"])
    queryset.hours=str(hoursin)
    queryset.timeday=timeday
    queryset.updatedby=userContext.id
    queryset.updateddate=dateUpdated
    queryset.save()
    
    return Response("OK")    


@api_view(['POST'])
def insert_time(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext) 
    
    queryTime = request.data["frmdate"].replace('/', '-')
    timeday = queryTime + ' ' + request.data["starthour"] + ':' + request.data["startmin"]
    dateCreated = time.strftime('%Y-%m-%d %H:%M:%S')
    hoursin = float(request.data["hours"]) + float(request.data["mins"])
       
    queryTask = Task(taskid=request.data["taskid"])
    queryset = Time(taskid=queryTask, timeday=timeday, hours=hoursin, createdby=userContext.id,
                    clientid=userContext.clientID, timetypeid=8, userid=userContext.id,
                    createddate=dateCreated)
    queryset.save()
    
    return Response("OK")


@api_view(['GET'])
def times(request):
    
    userContext = UserContextFull(request)
    logger.info(userContext)     
    
    queryset = VMyTime.objects.all().filter(Q(userid=userContext.id) &
                                            Q(clientid = userContext.clientID) &
                                            Q(deleteddate__isnull=True)).order_by('timeday')
    serializer_class = VTimelistSerializer(queryset,many=True)   

    return Response(serializer_class.data)


@api_view(['POST'])
def insert(request):

    user_context = UserContextFull(request)
    logger.info(str.format('time create : {0}' .format(user_context.id)))

    #time_id = request.POST.get('hidTimeID')
    task_id = request.POST.get('frmTaskID')
    time_user = user_context.id
    time_day_in = request.POST.get('frmDatePicker')
    time_day = time_day_in.replace('/', '-') + ' 00:00:00'
    # time_day = datetime.datetime.strptime(request.POST.get('frmDatePicker'),'%Y/%m/%d').date()
    time_hours = request.POST.get('frmHours')
    time_mins = request.POST.get('frmMins')
    time_type = request.POST.get('frmTimeType')
    time_comment = request.POST.get('frmComments')
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    hours = time_hours + time_mins

    # organisation = Organisation.objects.get(organisationid=organisation_id)

    time_serializer = APITimeSerializer(data={'timeday': time_day, 'hours': float(hours),
                            'taskid': task_id, 'timetypeid': time_type, 'comments': time_comment,
                                              'userid': time_user})

    if time_serializer.is_valid():

        task = Task.objects.get(taskid=task_id)

        time_new = Time(clientid=user_context.clientID, timeday=time_day, hours=hours, taskid=task,
                    timetypeid=time_type, userid=user_context.id, comments=time_comment, createddate=created_date,
                    createdby=created_by)
        time_new.save()

        time_object = Time.objects.filter(clientid=user_context.clientID, createdby=created_by).latest('timeid')

        response = {'time_id': time_object.timeid}

    else:
        raise serializers.ValidationError(time_serializer.errors)

    return Response(response)


@api_view(['POST'])
def update(request):

    user_context = UserContextFull(request)
    logger.info(str.format('time update : {0}' .format(user_context.id)))

    time_id = request.POST.get('hidTimeID')
    task_id = request.POST.get('hidTaskID')
    time_user = request.POST.get('hidUserID')
    time_hours = request.POST.get('frmHours')
    time_type = request.POST.get('frmTimeType')
    time_comment = request.POST.get('frmComment')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    # organisation = Organisation.objects.get(organisationid=organisation_id)

    time_serializer = APITimeSerializer(data={'timeday': updated_date, 'hours': time_hours,
                            'taskid': task_id, 'timetypeid': time_type, 'comments': time_comment,
                                              'userid': time_user})

    if time_serializer.is_valid():

        time_update = Time.objects.get(timeid=time_id)
        time_update.timetypeid = time_type
        time_update.comments = time_comment
        time_update.updated_by = updated_by
        time_update.updated_date = updated_date
        time_update.save(update_fields=['timetypeid', 'comments', 'updateddate', 'updatedby'])

        response = {'time_id': time_id}

    else:
        raise serializers.ValidationError(time_serializer.errors)

    return Response(response)
