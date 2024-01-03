from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyProblems
        
class VProblemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyProblems
        fields = ('problemid', 'organisationid', 'problemtype', 'problemheader', 'assignedto', 'problemscope', 'problemstatus',
                  'problempriority', 'createdby', 'first_name', 'last_name')