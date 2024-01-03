from rest_framework import serializers
from simpris.models.models import IdeaMap


class IdeaMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaMap
        fields = ('id', 'clientid', 'name', 'description', 'deleteddate')

