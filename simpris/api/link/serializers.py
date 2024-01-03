from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.models import Link


class LinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ('id', 'entityid', 'entitytype', 'link_name', 'link_url', 'link_target', 'updateddate')
