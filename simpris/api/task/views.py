from rest_framework.response import Response
from rest_framework import serializers
from simpris.api.task.serializers import VTasksSerializer, VTaskDependencySerializer, TaskSimpleSerializer
from simpris.models.db_views import VMyTasks, VProjectTasks, VTaskDetail, VTaskDependency
from simpris.models.models import Task, Tasklist
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view
from django.db.models import Q
import time

import logging

logger = logging.getLogger(__name__)


class APITaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task   


def validate_task(self, attrs, instance=None):
    taskid = serializers.IntegerField(label='TaskID', read_only=True)
    name = serializers.CharField(max_length=50)
    task_description_in = serializers.CharField(max_length=100)
    task_typeid_in = serializers.CharField(max_length=20)
    task_priorityid_in = serializers.IntegerField()
    assignedto_in = serializers.IntegerField()
    task_start_date_in = serializers.DateField(label='Task start date')
    task_time_estimate_in = serializers.IntegerField()
    task_percent_complete_in = serializers.IntegerField()
    completion_date = serializers.DateField()
    phaseid = serializers.IntegerField()


@api_view(['GET'])
def tasks(request):
    
    user_context = UserContextFull(request)
    logger.info(str.format('task list : {0}' .format(user_context.id)))
    
    queryset = VMyTasks.objects.all().filter(Q(assignedto=user_context.id) & Q(deleteddate__isnull=True) &
                                             Q(clientid=user_context.clientID) &
                                             Q(taskstatusid__in=[1, 2, 3, 4, 5, 6, 19])).order_by('taskpriorityid', 'projectname', 'taskname')
    serializer_class = VTasksSerializer(queryset, many=True)

    return Response(serializer_class.data) 


@api_view(['POST']) 
def insert(request): 
    
    user_context = UserContextFull(request)
    logger.info(str.format('task insert : {0}' .format(user_context.id)))

    task_name = request.POST.get('frmTaskName')
    # task_description_in = request.POST.get('frmTaskDescription')
    task_description_in = request.POST.get('ckedited')
    task_statusid_in = request.POST.get('frmTaskStatus')
    # taskID = request.POST.get('hidTaskID')
    tasklist_id = request.POST.get('hidTaskList')
    task_start_date_in = request.POST.get('frmDatePicker-' + tasklist_id)
    if task_start_date_in == '':
        task_start_date_in = None
    else:
        task_start_date_in = request.POST.get('frmDatePicker-' + tasklist_id) + ' ' + '12:00:00'
    # varfrmdatepicker = request.POST.get('frmDatePicker-' + tasklist_id) + ' ' + '12:00:00'
    task_typeid_in = request.POST.get('frmTaskType')
    task_priorityid_in = request.POST.get('frmTaskPriority')
    assignedto_in = request.POST.get('frmTaskAssignee')
    # task_start_date_in = varfrmdatepicker
    task_time_estimate_in = request.POST.get('frmEstimatedTime')
    task_percent_complete_in = request.POST.get('frmPercentageComplete')
    completion_date_in = request.POST.get('frmDatePicker2-' + tasklist_id)
    if completion_date_in == '':
        task_completion_date = None
    else:
        task_completion_date = request.POST.get('frmDatePicker2-' + tasklist_id) + ' ' + '12:00:00'
    phase_id = request.POST.get('selPhaseID')
    if phase_id == '':
        phase_id = None
    task_preceding_in = request.POST.get('frmTaskDependency') or None
    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    task_serializer = APITaskSerializer(data={'taskid': 0, 'clientid': user_context.clientID, 'tasklistid': tasklist_id,
                                                'taskname': task_name, 'taskdescription': task_description_in,
                                                'tasktypeid': task_typeid_in,
                                                'taskpriorityid': task_priorityid_in, 'assignedto': assignedto_in,
                                                'taskstartdate': task_start_date_in,
                                                'tasktimeestimate': task_time_estimate_in,
                                                'taskpercentcomplete': task_percent_complete_in,
                                                'completiondate': task_completion_date, 'phaseid': phase_id,
                                                'createdby': created_by,
                                                'createddate': created_date, 'tasklinkid': 0})

    if task_serializer.is_valid():
        tkl = Tasklist.objects.get(tasklistid=tasklist_id)

        tk = Task(tasklistid=tkl, clientid=user_context.clientID, tasktypeid=task_typeid_in,
                  taskname=task_name,
                  taskdescription=task_description_in, taskstatusid=task_statusid_in, taskpriorityid=task_priorityid_in,
                  assignedto=assignedto_in, taskstartdate=task_start_date_in, tasktimeestimate=task_time_estimate_in,
                  taskpercentcomplete=task_percent_complete_in, completiondate=task_completion_date,
                  phaseid=phase_id,
                  createddate=created_date, createdby=created_by)
        tk.save()

        new_task = VProjectTasks.objects.filter(clientid=user_context.clientID, tasklistid=tasklist_id,
                                               taskcreatedby=created_by).latest('taskid')

        response = {'taskid': new_task.taskid, 'taskpriority': new_task.taskpriority,
                    'taskstatus': new_task.taskstatus}

    else:
        errors = task_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        logger.error("Task insert - there had been an error")
        raise serializers.ValidationError(task_serializer.errors)
        response = {"status": "There has been an error"}
    
    return Response(response)    


@api_view(['GET'])
def delete(request, task_id):

    user_context = UserContextFull(request)
    logger.info(str.format('task delete : {0}' .format(user_context.id)))

    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    tk = Task.objects.get(taskid=task_id, clientid=user_context.clientID)
    tk.deletedby = deleted_by
    tk.deleteddate = deleted_date
    tk.save()

    response = {'taskid': task_id}

    return Response(response)


@api_view(['POST'])
def delete_post(request):

    user_context = UserContextFull(request)
    task_id = request.POST.get('task_id')
    logger.info(str.format('task delete post : {0}' .format(user_context.id)))

    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    tk = Task.objects.get(taskid=task_id, clientid=user_context.clientID)
    tk.deletedby = deleted_by
    tk.deleteddate = deleted_date
    tk.save()

    response = {'taskid': task_id}

    return Response(response)


@api_view(['POST'])
def update(request):
    
    user_context = UserContextFull(request)
    logger.info(str.format('task update : {0}' .format(user_context.id)))

    varfrmdatepicker = None
    varfrmdatepicker2 = None
    task_name = request.POST.get('frmTaskName')
    taskdescriptionin = request.POST.get('ckedited')
    #taskdescriptionin = request.POST.get('frmTaskDescription')
    taskstatusidin = request.POST.get('frmTaskStatus')
    task_id = request.POST.get('hidTaskID')
    task_list_id = request.POST.get('hidTaskList')
    if request.POST.get('frmDatePicker-' + task_id):
        varfrmdatepicker = request.POST.get('frmDatePicker-' + task_id) + ' ' + '12:00:00'
    if request.POST.get('frmDatePicker'):
        varfrmdatepicker = request.POST.get('frmDatePicker') + ' ' + '12:00:00'
        varfrmdatepicker = varfrmdatepicker.replace("/", "-")
    tasktypeidin = request.POST.get('frmTaskType')
    taskpriorityidin = request.POST.get('frmTaskPriority')
    assignedtoin = request.POST.get('frmTaskAssignee')
    taskstartdatein = varfrmdatepicker
    tasktimeestimatein = request.POST.get('frmEstimatedTime')
    taskpercentcompletein = request.POST.get('frmPercentageComplete')
    taskprecedingin = request.POST.get('frmTaskDependency') or None
    if request.POST.get('frmDatePicker2-' + task_id):
        varfrmdatepicker2 = request.POST.get('frmDatePicker2-' + task_id) + ' ' + '12:00:00'
    if request.POST.get('frmDatePicker2'):
        varfrmdatepicker2 = request.POST.get('frmDatePicker2') + ' ' + '12:00:00'
        varfrmdatepicker2 = varfrmdatepicker2.replace("/", "-")
    if varfrmdatepicker2 == None:
        task_completion_date = None
    else:
        task_completion_date = varfrmdatepicker2
    if task_completion_date == None:
        task_validate_date = time.strftime('%Y-%m-%d %H:%M:%S')
    else:
        task_validate_date = task_completion_date
    phase_id = request.POST.get('selPhaseID')
    if phase_id == '':
        task_validate_phase = 0
        phase_id = None
    else:
        task_validate_phase = phase_id
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id
    
    task_serializer = APITaskSerializer(data={'taskid': 0, 'clientid': user_context.clientID, 'tasklistid': task_list_id,
                                                'taskname': task_name, 'taskdescription': taskdescriptionin,
                                                'tasktypeid': tasktypeidin, 'taskpriorityid': taskpriorityidin,
                                                'assignedto': assignedtoin, 'taskstartdate': taskstartdatein,
                                                'tasktimeestimate': tasktimeestimatein,
                                                'taskpercentcomplete': taskpercentcompletein,
                                                'completiondate': task_validate_date, 'phaseid': task_validate_phase,
                                                'createdby': updated_by,
                                                'createddate': updated_date, 'tasklinkid': taskprecedingin})
    
    if task_serializer.is_valid():

        tk = Task.objects.get(taskid=task_id)
        tk.taskname = task_name
        tk.taskdescription = taskdescriptionin
        tk.tasktimeestimate = tasktimeestimatein
        tk.taskstatusid = taskstatusidin
        tk.taskstartdate = taskstartdatein
        tk.tasktypeid = tasktypeidin
        tk.taskpriorityid = taskpriorityidin
        tk.assignedto = assignedtoin
        tk.taskpercentcomplete = taskpercentcompletein
        tk.tasklinkid = taskprecedingin
        tk.completiondate = task_completion_date
        tk.phaseid = phase_id
        tk.updatedby = updated_by
        tk.updateddate = updated_date
        tk.save(update_fields=['taskname', 'taskdescription', 'tasktimeestimate', 'taskstatusid', 'taskstartdate',
                               'tasktypeid',
                               'taskpriorityid', 'assignedto', 'taskpercentcomplete', 'tasklinkid', 'completiondate',
                               'phaseid',
                               'updatedby', 'updateddate'])
        
        response = {'taskid': task_id}
        
    else:
        errors = task_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(task_serializer.errors)
        response = {'responseText': task_serializer.errors}

    return Response(response)


@api_view(['POST'])
def update_quick(request):

    userContext = UserContextFull(request)
    logger.info(str.format('task update quick : {0}' .format(userContext.id)))

    varfrmdatepicker = None
    varfrmdatepicker2 = None
    task_status_id_in = request.POST.get('frmTaskStatus')
    task_id = request.POST.get('hidTaskID')
    if request.POST.get('frmDatePicker'):
        varfrmdatepicker = request.POST.get('frmDatePicker') + ' ' + '12:00:00'
        varfrmdatepicker = varfrmdatepicker.replace("/","-")
    if request.POST.get('frmDatePicker2'):
        varfrmdatepicker2 = request.POST.get('frmDatePicker2') + ' ' + '12:00:00'
        varfrmdatepicker2 = varfrmdatepicker2.replace("/","-")
    assigned_to_in = request.POST.get('frmTaskAssignee')
    task_start_date_in = varfrmdatepicker
    task_time_estimate_in = request.POST.get('frmEstimatedTime')
    task_percent_complete_in = request.POST.get('frmPercentComplete')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = userContext.id

    tk = Task.objects.get(taskid=task_id)

    taskSerializer = APITaskSerializer(data={'taskid': task_id, 'clientid': userContext.clientID, 'tasklistid': tk.tasklistid.tasklistid,
                                             'taskname': "Test",
                                             'taskdescription': "Dummy", 'tasktypeid': 1,
                                             'taskpriorityid': 1, 'assignedto': assigned_to_in,
                                             'completionDate': varfrmdatepicker2,
                                             'taskstartdate': task_start_date_in, 'tasktimeestimate': 0,
                                             'taskpercentcomplete': task_percent_complete_in, 'createdby': updated_by,
                                             'createddate': updated_date, 'tasklinkid': 0})

    if taskSerializer.is_valid():

        #tk = Task.objects.get(taskid=task_id)
        #tk.tasktimeestimate = task_time_estimate_in
        tk.taskstatusid = task_status_id_in
        tk.taskstartdate = task_start_date_in
        tk.assignedto = assigned_to_in
        tk.completiondate = varfrmdatepicker2
        tk.taskpercentcomplete = task_percent_complete_in
        tk.updatedby = updated_by
        tk.updateddate = updated_date
        tk.save()

        response = {'taskid': task_id}

    else:


        errors = taskSerializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(taskSerializer.errors)
        response = {'responseText': taskSerializer.errors}

    return Response(response)


@api_view(['GET'])
def dependencies(request):

    user_context = UserContextFull(request)
    logger.info(str.format('task dependencies : {0}' .format(user_context.id)))

    project_id = request.GET.get('projectid')

    queryset = VTaskDependency.objects.all().filter(Q(projectid=project_id))
    serializer_class = VTaskDependencySerializer(queryset, many=True)

    response = {'taskDependencies': serializer_class.data}

    return Response(response)


@api_view(['GET'])
def detail(request):

    user_context = UserContextFull(request)
    logger.info(str.format('task detail : {0}' .format(user_context.id)))

    task_id = request.GET.get('taskid')

    tk = VTaskDetail.objects.all().filter(Q(clientid=user_context.clientID, taskid=task_id)).first()

    response = {'taskName': tk.taskname, 'taskDescription': tk.taskdescription, 'taskType': tk.tasktypeid,
                'taskPriority': tk.taskpriorityid, 'taskStartDate': tk.taskstartdate,
                'taskStatus': tk.taskstatusid, 'taskAssignee': tk.assignedto, 'taskDatePicker': tk.taskstartdate,
                'taskEstimatedTime': tk.tasktimeestimate, 'completionDate': tk.completiondate, 'phaseID': tk.phaseid,
                'taskDependency': tk.tasklinkid, 'taskPercentageComplete': tk.taskpercentcomplete}

    return Response(response)


@api_view(['POST'])
def move(request):

    user_context = UserContextFull(request)
    logger.info('task move: ' + str(user_context.id))

    task_list_to = request.POST.get('frmTaskList')
    task_id = request.POST.get('hidTaskID')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    task_serializer = APITaskSerializer(data={'taskid': 0, 'clientid': user_context.clientID,
                                              'tasklistid': task_list_to, 'taskname': 'VALIDATION',
                                              'taskdescription': 'VALIDATION', 'tasktypeid': 0, 'createdby': updated_by,
                                              'createddate': updated_date})

    if task_serializer.is_valid():

        tk = Task.objects.get(taskid=task_id)
        tkl = Tasklist.objects.get(tasklistid=task_list_to)
        tk.tasklistid = tkl
        tk.updatedby = updated_by
        tk.updateddate = updated_date
        tk.save()

        response = {'taskid': task_id}

    else:
        errors = task_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(task_serializer.errors)
        response = {'responseText': task_serializer.errors}

    return Response(response)


@api_view(['GET'])
def search_json(request):

    user_context = UserContextFull(request)
    logger.info(str.format('task search : {0}' .format(user_context.id)))

    term = request.GET.get('term')

    queryset = VMyTasks.objects.values('taskid', 'taskname', 'taskdescription').filter(clientid=user_context.clientID, taskname__icontains=term)\
        .order_by('taskname').distinct()

    serializer_class = TaskSimpleSerializer(queryset, many=True)

    return Response(serializer_class.data)
