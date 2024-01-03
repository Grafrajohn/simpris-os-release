from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyProgrammes
from simpris.models.models import Programme
        
class VProgrammesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programme
        fields = ('programmeid', 'clientid', 'programmename', 'programmedescription', 'createdby')