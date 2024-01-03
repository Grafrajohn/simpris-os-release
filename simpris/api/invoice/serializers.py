from django.contrib.auth.models import User, Group
from rest_framework import serializers
from simpris.models.db_views import VMyInvoices
        
class VInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VMyInvoices
        fields = ('invoiceid','statusid','nohours','grosstotal','nettotal','userid','deleteddate','lookupvaluechar','createddate', 'createddatef')