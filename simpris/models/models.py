# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
import datetime
import time

from django.db import models
from django.contrib.contenttypes.models import ContentType
from simpris.models import base


class Account(models.Model):
    accountid = models.AutoField(db_column='accountid', primary_key=True)
    accountname = models.CharField(db_column='accountname', max_length=100)
    authenticationid = models.CharField(db_column='authenticationid', max_length=45, blank=True, null=True)
    authenticationid2 = models.CharField(db_column='authenticationid2', max_length=45, blank=True, null=True)
    authenticationid3 = models.CharField(db_column='authenticationid3', max_length=45, blank=True, null=True)
    membershiptypeid = models.IntegerField(db_column='membershiptypeid')
    membershiprenewaldate = models.DateTimeField(db_column='membershiprenewaldate', blank=True, null=True)
    firstname = models.CharField(max_length=50, blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=75, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updatedate = models.DateTimeField(db_column='updatedate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'account'
        unique_together = (('accountname', 'email'),)


class Answer(models.Model):
    answerid = models.AutoField(db_column='answerid', primary_key=True)
    questionid = models.IntegerField(db_column='questionid')
    answer = models.CharField(max_length=5000)
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'answer'

#
# class AuthGroup(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'auth_group'
#
#
# class AuthGroupPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     group = models.ForeignKey(AuthGroup, on_delete=models.DO_NOTHING,)
#     permission = models.ForeignKey('AuthPermission', on_delete=models.DO_NOTHING,)
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'auth_group_permissions'
#         unique_together = (('group_id', 'permission_id'),)
#
#
# class AuthPermission(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     name = models.CharField(max_length=50)
#     content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING,)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'auth_permission'
#         unique_together = (('content_type_id', 'codename'),)
#

class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'auth_user'

#
# class AuthUserGroups(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     user = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING,)
#     group = models.ForeignKey(AuthGroup, on_delete=models.DO_NOTHING,)
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'auth_user_groups'
#         unique_together = (('user_id', 'group_id'),)
#
#
# class AuthUserUserPermissions(models.Model):
#     id = models.IntegerField(primary_key=True)  # AutoField?
#     user = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING,)
#     permission = models.ForeignKey(AuthPermission, on_delete=models.DO_NOTHING,)
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user_id', 'permission_id'),)


class Board(models.Model):
    userid = models.IntegerField(db_column='userid')
    itemid = models.IntegerField(db_column='itemid')
    itemtype = models.IntegerField(db_column='itemtype')
    columnno = models.IntegerField(db_column='columnno')
    itemorder = models.IntegerField(db_column='itemorder')

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'board'


class Client(models.Model):
    clientid = models.AutoField(db_column='clientid', primary_key=True)
    accountid = models.ForeignKey(Account, db_column='accountid', on_delete=models.CASCADE,)
    userid = models.IntegerField(db_column='userid')
    clientname = models.CharField(db_column='clientname', max_length=100)
    address1 = models.CharField(max_length=45)
    address2 = models.CharField(max_length=45)
    address3 = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    region = models.CharField(max_length=45)
    country = models.CharField(max_length=50)
    postcode = models.CharField(max_length=45)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updatedate = models.DateTimeField(db_column='updatedate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'client'


class Comment(models.Model):
    commentid = models.AutoField(db_column='commentid', primary_key=True)
    parentid = models.IntegerField(db_column='parentid')
    parenttypeid = models.IntegerField(db_column='parenttypeid')
    commenttypeid = models.IntegerField(db_column='commenttypeid')
    commenttext = models.CharField(db_column='commenttext', max_length=5000)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'comment'


class Country(models.Model):
    countryid = models.IntegerField(db_column='countryid', primary_key=True)
    countryname = models.CharField(db_column='countryname', unique=True, max_length=100)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'country'


class Document(models.Model):
    documentid = models.AutoField(db_column='documentid', primary_key=True)
    documenttypeid = models.IntegerField(db_column='documenttypeid')
    documentparentid = models.IntegerField(db_column='documentparentid')
    documentname = models.CharField(db_column='documentname', max_length=100)
    documentfilename = models.CharField(db_column='documentfilename', max_length=100)
    documenttitle = models.CharField(db_column='documenttitle', max_length=100, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'document'


class Error(models.Model):
    id = models.IntegerField(db_column='errorid',primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    organisationid = models.IntegerField(db_column='organisationid')
    userid = models.IntegerField(db_column='userid')
    description = models.CharField(db_column='description', max_length=500)
    module = models.CharField(db_column='module', max_length=10)
    submodule = models.CharField(db_column='submodule', max_length=10)
    action = models.CharField(db_column='action', max_length=10)
    subaction = models.CharField(db_column='subaction', max_length=10)
    createddate = models.DateTimeField(db_column='createddate')

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'error'


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'groups'


class Idea(base.Common_Client_Striped):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parentid = models.IntegerField(db_column='parentid')
    parenttypeid = models.IntegerField(db_column='parenttypeid')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'idea'


class IdeaMap(base.Common_Client_Striped):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'ideamap'


class Interaction(base.Common_Client_Striped):
    interactionid = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userid')
    organisationid = models.IntegerField(db_column='organisationid')
    interactiontypeid = models.IntegerField(db_column='interactiontypeid')
    details = models.CharField(db_column='details', max_length=4000, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'interaction'


class Invoice(models.Model):
    invoiceid = models.AutoField(db_column='invoiceid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    userid = models.IntegerField(db_column='userid')
    statusid = models.IntegerField(db_column='statusid')
    supersededby = models.IntegerField(db_column='supersededby', blank=True, null=True)
    description = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    invoicecol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'invoice'


class Invoiceline(models.Model):
    invoiceid = models.IntegerField(db_column='invoiceid')
    lineno = models.IntegerField(db_column='lineno')
    taskid = models.IntegerField(db_column='taskid')
    timeid = models.IntegerField(db_column='timeid')
    itemdescription = models.CharField(db_column='itemdescription', max_length=150)
    tax1rate = models.DecimalField(db_column='tax1rate', max_digits=10, decimal_places=2)
    tax2rate = models.DecimalField(db_column='tax2rate', max_digits=10, decimal_places=2)
    tax3rate = models.DecimalField(db_column='tax3rate', max_digits=10, decimal_places=2)
    hourlyrate = models.DecimalField(db_column='hourlyrate', max_digits=10, decimal_places=2)
    nohours = models.DecimalField(db_column='nohours', max_digits=10, decimal_places=1)
    agreedrate = models.DecimalField(db_column='agreedrate', max_digits=10, decimal_places=1)
    tax1 = models.DecimalField(max_digits=10, decimal_places=2)
    tax2 = models.DecimalField(max_digits=10, decimal_places=2)
    tax3 = models.DecimalField(max_digits=10, decimal_places=2)
    grosstotal = models.DecimalField(db_column='grosstotal', max_digits=10, decimal_places=2)
    nettotal = models.DecimalField(db_column='nettotal', max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'invoiceline'
        unique_together = (('invoiceid', 'lineno'),)


class Link(base.Common_Client_Striped):
    id = models.IntegerField(primary_key=True)  # AutoField?
    entityid = models.IntegerField(db_column='entityid')
    entitytype = models.CharField(db_column='entitytype', max_length=4)
    link_name = models.CharField(db_column='link_name', max_length=100)
    link_url = models.CharField(db_column='link_url', max_length=100)
    link_target = models.CharField(db_column='link_target', max_length=20)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'link'


class LoginAttempts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ip_address = models.CharField(max_length=16)
    login = models.CharField(max_length=100)
    time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'login_attempts'


class Lookup(models.Model):
    clientid = models.IntegerField(db_column='clientid')
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')
    lookupsubtypeid = models.IntegerField(db_column='lookupsubtypeid')
    lookuporder = models.IntegerField(db_column='lookuporder')
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True, null=True)
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    id = models.IntegerField(db_column='id', primary_key=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'lookup'


class LookupType(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    lookuptype = models.CharField(db_column='lookuptype', max_length=100)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'lookup_type'


class Meta(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    mainorganisationid = models.IntegerField(db_column='mainorganisationid', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'meta'


class Opinion(models.Model):
    opinionid = models.AutoField(db_column='opinionid', primary_key=True)
    userid = models.IntegerField(db_column='userid')
    itemtype = models.IntegerField(db_column='itemtype')
    itemid = models.IntegerField(db_column='itemid')
    opiniontype = models.IntegerField(db_column='opiniontype', blank=True, null=True)
    opinion = models.CharField(max_length=250, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'opinion'
        unique_together = (('userid', 'itemtype', 'itemid'),)


class Organisation(models.Model):
    organisationid = models.AutoField(db_column='organisationid', primary_key=True)
    clientid = models.ForeignKey(Client, db_column='clientid', on_delete=models.DO_NOTHING,)
    organisationname = models.CharField(db_column='organisationname', max_length=100)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'organisation'


class OrganisationArchive(models.Model):
    organisationid = models.IntegerField(db_column='organisationid')
    clientid = models.IntegerField(db_column='clientid')
    organisationname = models.CharField(db_column='organisationname', max_length=100)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'organisation_archive'


class Payrate(models.Model):
    payrateid = models.AutoField(db_column='payrateid', primary_key=True)
    payratedescription = models.CharField(db_column='payratedescription', max_length=20)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    rateper = models.IntegerField()
    tasktype = models.IntegerField(db_column='tasktype', blank=True, null=True)
    effectivedate = models.DateTimeField(db_column='effectiveDate')  
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updatedate = models.DateTimeField(db_column='updatedate', blank=True, null=True)
    updateby = models.IntegerField(db_column='updateby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'payrate'


class Phase(models.Model):
    phaseid = models.AutoField(db_column='phaseid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    phasename = models.CharField(db_column='phasename', max_length=50)
    phasedescription = models.CharField(db_column='phasedescription', max_length=500, blank=True, null=True)
    startdate = models.DateTimeField(db_column='startdate', blank=True, null=True)
    enddate = models.DateTimeField(db_column='enddate', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    @property
    def start_date(self):
        return '%s' % self.startdate.strftime('%Y/%m/%d')

    @property
    def end_date(self):
        return '%s' % self.enddate.strftime('%Y/%m/%d')

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'phase'


class Problem(models.Model):
    problemid = models.AutoField(db_column='problemid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    organisationid = models.ForeignKey(Organisation, db_column='organisationid', on_delete=models.DO_NOTHING,)
    problemtypeid = models.IntegerField(db_column='problemtypeid')
    problemsubtypeid = models.IntegerField(db_column='problemsubtypeid', blank=True, null=True)
    problemheader = models.CharField(db_column='problemheader', max_length=50)
    problemdescription = models.CharField(db_column='problemdescription', max_length=2000)
    noofpeopleaffected = models.IntegerField(db_column='noofpeopleaffected')
    scope = models.IntegerField()
    problemstatusid = models.IntegerField(db_column='problemstatusid', blank=True, null=True)
    problempriorityid = models.IntegerField(db_column='problempriorityid', blank=True, null=True)
    queueid = models.IntegerField(db_column='queueid', blank=True, null=True)
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)
    completeddate = models.DateTimeField(db_column='completeddate', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'problem'
        #unique_together = (('organisationid', 'problemheader'),)


class ProblemArchive(models.Model):
    problemid = models.IntegerField(db_column='problemid')
    clientid = models.IntegerField(db_column='clientid')
    organisationid = models.IntegerField(db_column='organisationid')
    problemtypeid = models.IntegerField(db_column='problemtypeid')
    problemsubtypeid = models.IntegerField(db_column='problemsubtypeid', blank=True, null=True)
    problemheader = models.CharField(db_column='problemheader', max_length=50)
    problemdescription = models.CharField(db_column='problemdescription', max_length=2000)
    noofpeopleaffected = models.IntegerField(db_column='noofpeopleaffected')
    scope = models.IntegerField()
    problemstatusid = models.IntegerField(db_column='problemstatusid', blank=True, null=True)
    problempriorityid = models.IntegerField(db_column='problempriorityid', blank=True, null=True)
    queueid = models.IntegerField(db_column='queueid', blank=True, null=True)
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)
    completeddate = models.DateTimeField(db_column='completeddate', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'problem_archive'


class Problemlink(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    problemid = models.IntegerField(db_column='problemid')
    problemlinkid = models.IntegerField(db_column='problemlinkid')
    problemlinktype = models.IntegerField(db_column='problemlinktype')
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'problemlink'


class ProblemLog(Comment):
    authuser = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING,)

    class Meta:
        managed = True
        app_label = 'simpris'


class Programme(models.Model):
    programmeid = models.AutoField(db_column='programmeid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    programmename = models.CharField(db_column='programmename', max_length=50)
    programmedescription = models.CharField(db_column='programmedescription', max_length=500, blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby')
    createddate = models.DateTimeField(db_column='createddate')
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'programme'
        app_label = 'simpris'


class Project(base.Common_Client_Striped):
    projectid = models.AutoField(db_column='projectid', primary_key=True)
    organisationid = models.ForeignKey(Organisation, db_column='organisationid', on_delete=models.DO_NOTHING,)
    programmeid = models.IntegerField(db_column='programmeid', blank=True, null=True)
    projectname = models.CharField(db_column='projectname', max_length=50)
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True, null=True)
    stakeholderid = models.IntegerField(db_column='stakeholderid', blank=True, null=True)
    projectmanagerid = models.IntegerField(db_column='projectmanagerid', blank=True, null=True)
    deliverables = models.CharField(max_length=1500, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'project'


class ProjectArchive(base.Common_Client_Striped):
    projectid = models.IntegerField(db_column='projectid')
    organisationid = models.IntegerField(db_column='organisationid')
    programmeid = models.IntegerField(db_column='programmeid', blank=True, null=True)
    projectname = models.CharField(db_column='projectname', max_length=50)
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True, null=True)
    stakeholderid = models.IntegerField(db_column='stakeholderid', blank=True, null=True)
    projectmanagerid = models.IntegerField(db_column='projectmanagerid', blank=True, null=True)
    deliverables = models.CharField(max_length=1500, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'project_archive'


class Queue(base.Common_Client_Striped):
    queueid = models.AutoField(db_column='queueid', primary_key=True)
    queuename = models.CharField(db_column='queuename', max_length=45)
    queuedescription = models.CharField(db_column='queuedescription', max_length=450, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'queue'


class QueueUser(models.Model):
    queueid = models.ForeignKey(Queue, db_column='queueid', on_delete=models.DO_NOTHING,)
    clientid = models.IntegerField(db_column='clientid')
    queueuserid = models.IntegerField(db_column='queueuserid')
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'queue_user'


class Question(models.Model):
    questionid = models.AutoField(db_column='questionid', primary_key=True)
    questionname = models.CharField(db_column='questionname', max_length=45, blank=True, null=True)
    questiontext = models.CharField(db_column='questiontext', max_length=5000, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'question'


class Questionnaire(models.Model):
    questionnaireid = models.AutoField(db_column='questionnaireid', primary_key=True)
    questionnairename = models.CharField(db_column='questionnairename', max_length=45)
    contactuserid = models.IntegerField(db_column='contactuserid')
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'questionnaire'


class QuestionnaireQuestion(models.Model):
    questionnaireid = models.IntegerField(db_column='questionnaireid')
    questionid = models.IntegerField(db_column='questionid')
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'questionnaire_question'
        unique_together = (('questionnaireid', 'questionid'),)


class Status(models.Model):
    statusid = models.IntegerField(db_column='statusid', primary_key=True)
    userid = models.IntegerField(db_column='userid', blank=True, null=True)
    itemid = models.IntegerField(db_column='itemid', blank=True, null=True)
    itemtype = models.IntegerField(db_column='itemtype', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    statuscol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'status'
        unique_together = (('userid', 'itemid', 'itemtype'),)


class Tasklist(models.Model):
    tasklistid = models.AutoField(db_column='tasklistid', primary_key=True)
    projectid = models.ForeignKey(Project, db_column='projectid', on_delete=models.DO_NOTHING,)
    clientid = models.IntegerField(db_column='clientid')
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'tasklist'
        unique_together = (('projectid', 'tasklistname'), ('tasklistname', 'projectid'),)


class Task(models.Model):
    taskid = models.AutoField(db_column='taskid', primary_key=True)
    tasklistid = models.ForeignKey(Tasklist, db_column='tasklistid', on_delete=models.DO_NOTHING,)
    clientid = models.IntegerField(db_column='clientid')
    tasktypeid = models.IntegerField(db_column='tasktypeid')
    taskname = models.CharField(db_column='taskname', max_length=50)
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)
    taskstartdate = models.DateTimeField(db_column='taskstartdate', blank=True, null=True)
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)
    taskpercentcomplete = models.IntegerField(db_column='taskpercentcomplete', blank=True, null=True)
    completiondate = models.DateTimeField(db_column='completiondate', blank=True, null=True)
    phaseid = models.IntegerField(db_column='phaseid', blank=True, null=True)
    tasklinkid = models.IntegerField(db_column='tasklinkid', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'task'


class TaskArchive(models.Model):
    taskid = models.IntegerField(db_column='taskid')
    tasklistid = models.IntegerField(db_column='tasklistid')
    clientid = models.IntegerField(db_column='clientid')
    tasktypeid = models.IntegerField(db_column='tasktypeid')
    taskname = models.CharField(db_column='taskname', max_length=50, blank=True, null=True)
    taskdescription = models.CharField(db_column='taskdescription', max_length=500)
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)
    taskstartdate = models.DateTimeField(db_column='taskstartdate', blank=True, null=True)
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)
    taskpercentcomplete = models.IntegerField(db_column='taskpercentcomplete', blank=True, null=True)
    completiondate = models.DateTimeField(db_column='completiondate', blank=True, null=True)
    phaseid = models.IntegerField(db_column='phaseid', blank=True, null=True)
    tasklinkid = models.IntegerField(db_column='tasklinkid', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'task_archive'


class TaskTemplate(models.Model):
    tasktemplateid = models.AutoField(db_column='tasktemplateid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid', blank=True, null=True)
    tasktemplatename = models.CharField(db_column='tasktemplatename', max_length=100, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'task_template'
        unique_together = (('tasktemplatename', 'clientid'),)


class TasklistArchive(models.Model):
    tasklistid = models.IntegerField(db_column='tasklistid')
    projectid = models.IntegerField(db_column='projectid')
    clientid = models.IntegerField(db_column='clientid', blank=True, null=True)
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedid = models.IntegerField(db_column='updatedid', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'tasklist_archive'


class Taskstep(models.Model):
    taskstepid = models.AutoField(db_column='taskstepid', primary_key=True)
    taskid = models.IntegerField(db_column='taskid', blank=True, null=True)
    steporder = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'taskstep'
        unique_together = (('taskid', 'steporder'),)


class Taxrate(models.Model):
    taxrateid = models.AutoField(db_column='taxrateid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    taxratedescription = models.CharField(db_column='taxratedescription', max_length=100)
    taxrate = models.DecimalField(max_digits=10, decimal_places=2)
    effectivedate = models.DateTimeField(db_column='effectiveDate')  
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'taxrate'


class Team(models.Model):
    teamid = models.AutoField(db_column='teamid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    teamname = models.CharField(db_column='teamname', max_length=100)
    teamdescription = models.CharField(db_column='teamdescription', max_length=1000, blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby')
    createddate = models.DateTimeField(db_column='createddate')
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'team'


class TeamQueue(models.Model):
    queueid = models.ForeignKey(Queue, db_column='queueid', on_delete=models.DO_NOTHING,)
    clientid = models.IntegerField(db_column='clientid')
    queueteamid = models.ForeignKey(Team, db_column='queueteamid', on_delete=models.DO_NOTHING,)
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'queue_team'


class TeamUser(models.Model):
    teamid = models.IntegerField(db_column='teamid')
    userid = models.IntegerField(db_column='userid')
    clientid = models.IntegerField(db_column='clientid')
    createdby = models.IntegerField(db_column='createdby')
    createddate = models.DateTimeField(db_column='createddate')
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'team_user'


class TestTable(models.Model):
    testint = models.IntegerField()

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'test_table'


class Time(models.Model):
    timeid = models.AutoField(db_column='timeid', primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    timeday = models.DateTimeField(db_column='timeday')
    hours = models.FloatField()
    taskid = models.ForeignKey(Task, db_column='taskid', on_delete=models.DO_NOTHING,)
    timetypeid = models.IntegerField(db_column='timetypeid')
    userid = models.IntegerField(db_column='userid')
    comments = models.CharField(max_length=50, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'time'


class UserAttributes(models.Model):
    userid = models.IntegerField(db_column='userid', primary_key=True)
    vip = models.CharField(max_length=1)
    countryid = models.IntegerField(db_column='countryid', blank=True, null=True)
    mobilephoneno = models.CharField(db_column='mobilephoneno', max_length=20, blank=True, null=True)
    faxno = models.CharField(db_column='faxno', max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'user_attributes'


class UserConfiguration(models.Model):
    userid = models.IntegerField(db_column='userid')
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')
    configurationdata = models.CharField(db_column='configurationdata', max_length=50)
    configurationdatanum = models.FloatField(db_column='configurationdataNum')
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate')
    updatedby = models.IntegerField(db_column='updatedby')
    deleteddate = models.DateTimeField(db_column='deleteddate')
    deletedby = models.IntegerField(db_column='deletedby')

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'user_configuration'
        unique_together = (('userid', 'lookuptypeid'),)


class UserCookie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.BigIntegerField(db_column='userid')
    uuid = models.CharField(db_column='uuid', max_length=128)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    created_on = models.DateTimeField()

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'user_cookie'


class UserPayrate(models.Model):
    userid = models.IntegerField(db_column='userid', primary_key=True)
    payrateid = models.IntegerField(db_column='payrateid')
    effectivedate = models.DateTimeField(db_column='effectiveDate')  
    defaultrate = models.DecimalField(db_column='defaultrate', max_digits=10, decimal_places=2, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'user_payrate'


class UserStatus(models.Model):
    statusid = models.IntegerField(db_column='statusid', primary_key=True)
    userid = models.IntegerField(db_column='userid', blank=True, null=True)
    itemid = models.IntegerField(db_column='itemid', blank=True, null=True)
    itemtype = models.IntegerField(db_column='itemtype', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    statuscol = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'user_status'
        unique_together = (('userid', 'itemid', 'itemtype'),)


class UserTaxrate(models.Model):
    userid = models.IntegerField(db_column='userid', primary_key=True)
    taxrateid = models.DecimalField(db_column='taxrateid', max_digits=10, decimal_places=2)
    effectivedate = models.DateTimeField(db_column='effectiveDate', blank=True, null=True)  
    defaultrate = models.DecimalField(db_column='defaultrate', max_digits=10, decimal_places=2, blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'user_taxrate'


class Useractivity(models.Model):
    activityid = models.AutoField(db_column='activityid', primary_key=True)
    userid = models.IntegerField(db_column='userid')
    activitytype = models.CharField(db_column='activitytype', max_length=10)
    activitydata = models.CharField(db_column='activitydata', max_length=100, blank=True, null=True)
    activity_module = models.CharField(db_column='activity_module', max_length=10, blank=True, null=True)
    activity_submodule = models.CharField(db_column='activity_submodule', max_length=10)
    client_id = models.IntegerField(db_column='client_id', blank=True, null=True)
    activitydate = models.DateTimeField(db_column='activityDate')  

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'useractivity'


class Userorganisation(models.Model):
    userid = models.IntegerField(db_column='userid')
    organisationid = models.ForeignKey(Organisation, db_column='organisationid', on_delete=models.DO_NOTHING,)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'userorganisation'
        unique_together = (('userid', 'organisationid'),)


class Userproject(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    userid = models.IntegerField(db_column='userid')
    projectid = models.ForeignKey(Project, db_column='projectid', on_delete=models.DO_NOTHING,)
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'userproject'


class Userreport(models.Model):
    userid = models.IntegerField(db_column='userid')
    reportid = models.IntegerField(db_column='reportid')
    createddate = models.DateTimeField(db_column='createddate')
    createdby = models.IntegerField(db_column='createdby')
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'userreport'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    clientid = models.IntegerField(db_column='clientid')
    ip_address = models.CharField(max_length=16)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    activation_code = models.CharField(max_length=40, blank=True, null=True)
    forgotten_password_code = models.CharField(max_length=40, blank=True, null=True)
    forgotten_password_time = models.IntegerField(blank=True, null=True)
    remember_code = models.CharField(max_length=40, blank=True, null=True)
    created_on = models.IntegerField()
    last_login = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'users'


class UsersArchive(models.Model):
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    ip_address = models.CharField(max_length=16)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=40)
    salt = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=100)
    activation_code = models.CharField(max_length=40, blank=True, null=True)
    forgotten_password_code = models.CharField(max_length=40, blank=True, null=True)
    forgotten_password_time = models.IntegerField(blank=True, null=True)
    remember_code = models.CharField(max_length=40, blank=True, null=True)
    created_on = models.IntegerField()
    last_login = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'users_archive'


class UsersGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'users_groups'


class Usertask(models.Model):
    userid = models.IntegerField(db_column='userid')
    taskid = models.ForeignKey(Task, db_column='taskid', on_delete=models.DO_NOTHING,)

    class Meta:
        managed = True
        app_label = 'simpris'
        db_table = 'usertask'
        unique_together = (('userid', 'taskid'),)

