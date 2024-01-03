from rest_framework import serializers
from simpris.models.models import Queue


class QueueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Queue
        fields = ('queueid', 'clientid', 'queuename', 'queuedescription', 'deleteddate')

