from rest_framework import serializers
from simpris.models.models import Idea


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ('id', 'clientid', 'parentid', 'parenttypeid', 'name', 'description', 'deleteddate')

