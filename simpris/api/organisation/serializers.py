from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyOrganisations

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VMyOrganisations
        fields = ('organisationid','organisationname')


class VClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyOrganisations
        fields = ('clientid', 'organisationid', 'organisationname', 'userid')
