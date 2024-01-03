# from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework import serializers
from simpris.api.tasklist.serializers import TaskListsSerializer
from simpris.models.models import Tasklist, Project
from simpris.library.user_context import UserContextFull
from rest_framework.decorators import api_view
# from django.db.models import Q
from django import forms
import time

import logging

logger = logging.getLogger(__name__)


class APITasklistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = '__all__'


class TasklistForm(forms.Form):
    frmTaskListName = forms.CharField(required=True, label='frmTaskListName', max_length=50)
    frmTaskListDescription = forms.CharField(required=True, label='frmTaskListDescription', max_length=500)
    hidProjectID = forms.CharField(required=True, max_length=50, widget=forms.HiddenInput())


@api_view(['POST'])
def insert(request):
    user_context = UserContextFull(request)
    logger.info(str.format('tasklist insert : {0}' .format(user_context.id)))

    tasklistnamein = request.POST.get('frmTaskListName')
    tasklistdescriptionin = request.POST.get('frmTaskListDescription')
    project_id = request.POST.get('hidProjectID')
    project = Project.objects.get(projectid=project_id)
    createddate = time.strftime('%Y-%m-%d %H:%M:%S')
    createdby = user_context.id

    tasklist_serializer = APITasklistSerializer(data={'tasklistid': 0,
                                                      'projectid': project_id,
                                                      'clientid': user_context.clientID,
                                                      'tasklistname': tasklistnamein,
                                                      'tasklistdescription': tasklistdescriptionin,
                                                      'createdby': createdby,
                                                      'createddate': createddate})

    if tasklist_serializer.is_valid():
        tkl = Tasklist(projectid=project, clientid=user_context.clientID, tasklistname=tasklistnamein,
                       tasklistdescription=tasklistdescriptionin, createddate=createddate, createdby=createdby)
        tkl.save()

        newTaskList = Tasklist.objects.filter(clientid=user_context.clientID, projectid=project_id, createdby=createdby).latest('tasklistid')
        response = newTaskList.tasklistid
    else:
        raise serializers.ValidationError(tasklist_serializer.errors)
        # response = tasklist_serializer.errors

    return Response(response)


@api_view(['POST'])
def update(request):
    user_context = UserContextFull(request)
    logger.info(str.format('tasklist update : {0}' .format(user_context.id)))

    tasklistid = request.POST.get('hidTasklistID')
    project_id = request.POST.get('hidProjectID')
    tasklistnamein = request.POST.get('frmTaskListName')
    tasklistdescriptionin = request.POST.get('frmTaskListDescription')
    updateddate = time.strftime('%Y-%m-%d %H:%M:%S')
    updatedby = user_context.id

    tasklist_serializer = APITasklistSerializer(data={'tasklistid': 0,
                                                      'projectid': project_id,
                                                      'clientid': user_context.clientID,
                                                      'tasklistname': tasklistnamein,
                                                      'tasklistdescription': tasklistdescriptionin,
                                                      'createdby': updatedby,
                                                      'createddate': updateddate,
                                                      'updatedby': updatedby,
                                                      'updateddate': updateddate})

    if tasklist_serializer.is_valid():

        tkl = Tasklist.objects.get(tasklistid=tasklistid)
        tkl.tasklistname = tasklistnamein
        tkl.tasklistdescription = tasklistdescriptionin
        tkl.updateddate = updateddate
        tkl.updatedby = updatedby
        tkl.save(update_fields=['tasklistname', 'tasklistdescription', 'updateddate', 'updatedby'])

        response = {'tasklistid': tkl.pk, 'tasklistname': tasklistnamein, 'tasklistdescription': tasklistdescriptionin}

    else:

        raise serializers.ValidationError(tasklist_serializer.errors)
        # response = tasklist_serializer.errors

    return Response(response)


@api_view(['POST'])
def delete(request):
    user_context = UserContextFull(request)
    logger.info(str.format('tasklist delete : {0}' .format(user_context.id)))

    tasklistid = request.data["tasklist_id"]
    project_id = request.data["project_id"]
    updateddate = time.strftime('%Y-%m-%d %H:%M:%S')
    updatedby = user_context.id

    tasklist_serializer = APITasklistSerializer(data={'tasklistid': tasklistid,
                                                      'projectid': project_id,
                                                      'clientid': user_context.clientID,
                                                      'tasklistname': 'dummy',
                                                      'tasklistdescription': 'dummy',
                                                      'createdby': updatedby,
                                                      'createddate': updateddate,
                                                      'updatedby': updatedby,
                                                      'updateddate': updateddate})

    if tasklist_serializer.is_valid():

        tkl = Tasklist.objects.get(tasklistid=tasklistid)
        tkl.deleteddate = updateddate
        tkl.deletedby = updatedby
        tkl.save(update_fields=['deleteddate', 'deletedby'])

        response = {'tasklistid': tasklistid}

    else:

        raise serializers.ValidationError(tasklist_serializer.errors)

    return Response(response)