from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyUsers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VMyUsers
        fields = ('user_id','name', 'first_name', 'last_name', 'organisationname', 'activedesc', 'clientid')