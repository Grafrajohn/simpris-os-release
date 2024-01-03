from django.db import models

# Abstract models
class Base(models.Model):
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        abstract = True

class Common_Client_Striped(Base):
    clientid = models.IntegerField(db_column='clientid', blank=False, null=False)

    class Meta:
        abstract = True