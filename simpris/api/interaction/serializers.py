from rest_framework import serializers
from simpris.models.models import Interaction
from ...models.db_views import VInteractions


class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = ('interactionid', 'clientid', 'userid', 'organisationid', 'interactiontypeid', 'details', 'createddate', 'createdby',
                  'updateddate', 'updatedby', 'deleteddate', 'deletedby')


class InteractionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VInteractions
        fields = ('interactionid', 'clientid', 'interactiontype', 'details', 'createddate', 'createdby',
                  'updateddate', 'updatedby', 'deleteddate', 'deletedby')

