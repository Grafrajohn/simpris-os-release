from rest_framework import serializers
from simpris.models.models import Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('teamid', 'clientid', 'teamname', 'teamdescription', 'deleteddate')

