from rest_framework import serializers
from simpris.models.models import Phase


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = ('phaseid', 'clientid', 'phasename', 'phasedescription', 'startdate', 'enddate', 'deleteddate', 'start_date', 'end_date')

