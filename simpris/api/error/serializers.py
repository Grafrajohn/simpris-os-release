from rest_framework import serializers
from simpris.models.models import Error
from ...models.db_views import VErrors


class ErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Error
        fields = ('errorid', 'clientid', 'userid', 'organisationid', 'description',
                  'module', 'submodule', 'action', 'subaction', 'createddate')


class ErrorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VErrors
        fields = ('errorid', 'clientid', 'userid', 'organisationid', 'description', 'module',
                  'submodule', 'action', 'subaction', 'createddate')

