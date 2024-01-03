# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyTasks, VTaskDependency
from simpris.models.models import Task
        
class VTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyTasks
        fields = ('taskid', 'clientid', 'projectname', 'tasklistname', 'taskdescription', 'taskname', 'assignedto', 'tasklistid')


class VTaskDependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = VTaskDependency
        fields = ('taskid', 'tasklistid', 'clientid', 'tasktypeid', 'taskname', 'taskdescription', 'taskstatusid',
                  'taskpriorityid', 'assignedto', 'taskstartdate', 'tasktimeestimate', 'taskpercentcomplete')


class TaskSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyTasks
        fields = ('taskname', 'taskid', 'taskdescription')
