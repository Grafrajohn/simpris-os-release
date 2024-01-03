# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.models import Lookup
from simpris.models.models import Task
        
class LookupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lookup
        fields = ('id', 'clientid', 'lookuptypeid', 'lookupsubtypeid', 'lookuporder', 'lookupvaluenum', 'lookupvaluechar', 'lookupdescription')

