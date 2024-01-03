# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.models import Tasklist
        
class TaskListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasklist
        fields = ('taskid','projectname','tasklistname','taskdescription','assignedto','tasklistid')                                            