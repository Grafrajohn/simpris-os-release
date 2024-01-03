from rest_framework import serializers
from simpris.models.db_views import VTimeCalendar, VTimeGrid, VTimeTask, VMyTime
from simpris.models.models import Time
        
class VCalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = VTimeCalendar
        fields = ('id', 'title', 'start')
        
class VTimegridSerializer(serializers.ModelSerializer):
    class Meta:
        model = VTimeGrid
        fields = ('id', 'clientid', 'starthour', 'startmin', 'project', 'tasklist', 'task', 'taskid', 'timeday', 'hours',
                  'mins', 'minsformat', 'assignedto')
        
class VTimetaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = VTimeTask
        fields = ('taskid', 'project', 'tasklist', 'task')
        
class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = ('taskid', 'timeday', 'hours')
        
class VTimelistSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyTime
        fields = ('timeid', 'timeday', 'taskdescription', 'hours', 'lookupvaluechar')