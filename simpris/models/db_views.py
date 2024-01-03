# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from simpris.models import base


class VAccountDetail(models.Model):
    accountid = models.IntegerField(primary_key=True)
    accountname = models.CharField(db_column='accountname', max_length=100)  # Field name made lowercase.
    authenticationid = models.CharField(db_column='authenticationid', max_length=45, blank=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    id = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_account_detail'


class VActualProblemLinks(models.Model):
    problemid = models.IntegerField(db_column='problemid')  # Field name made lowercase.
    problemlinkid = models.IntegerField(db_column='problemlinkid')  # Field name made lowercase.
    problemlinktype = models.IntegerField(db_column='problemlinktype')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    problemlinkname = models.CharField(db_column='problemlinkname', max_length=50)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_actual_problem_links'


class VBoard(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')
    itemid = models.IntegerField(db_column='itemid')  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='itemtype')  # Field name made lowercase.
    columnno = models.IntegerField(db_column='columnno')  # Field name made lowercase.
    itemorder = models.IntegerField(db_column='itemorder')  # Field name made lowercase.
    description = models.IntegerField(db_column='description')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_board'


class VBoardQueue(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    description = models.CharField(max_length=10000)
    assignedto = models.IntegerField(db_column='assignedto')  # Field name made lowercase.
    type = models.IntegerField(db_column='type')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_board_queue'


class VChartProjectBehindTasks(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True)
    counttasks = models.BigIntegerField(db_column='countTasks')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    taskstartdate = models.DateTimeField(db_column='taskstartdate', blank=True, null=True)  # Field name made lowercase.
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_chart_project_behind_tasks'


class VChartTasksByStatus(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    status = models.CharField(max_length=50, blank=True)
    counttasks = models.BigIntegerField(db_column='countTasks')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_chart_tasks_by_status'


class VClientAdminGroup(models.Model):
    groupid = models.IntegerField(db_column='groupid')  # Field name made lowercase.
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_client_admin_group'


class VClientUsers(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_client_users'


class VCommentsParent(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    commentid = models.IntegerField(db_column='commentid')  # Field name made lowercase.
    parentid = models.IntegerField(db_column='parentid')  # Field name made lowercase.
    parenttypeid = models.IntegerField(db_column='parenttypeid')  # Field name made lowercase.
    commenttypeid = models.IntegerField(db_column='commenttypeid')  # Field name made lowercase.
    commenttext = models.CharField(db_column='commenttext', max_length=5000)  # Field name made lowercase.
    createddate = models.CharField(db_column='createddate', max_length=116, blank=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    documentfilename = models.CharField(db_column='documentfilename', max_length=100, blank=True)  # Field name made lowercase.
    documentname = models.CharField(db_column='documentname', max_length=100, blank=True)  # Field name made lowercase.
    documenttitle = models.CharField(db_column='documenttitle', max_length=100, blank=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_comments_parent'


# class VEmailQueue(models.Model):
#     to_email = models.CharField(max_length=128)
#     subject = models.CharField(max_length=255)
#     message = models.TextField()
#     date_published = models.DateTimeField(blank=True, null=True)
#     date_sent = models.DateTimeField(blank=True, null=True)
#     success = models.IntegerField()
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'v_email_queue'


class VErrors(models.Model):
    id = models.IntegerField(db_column='errorid',primary_key=True)
    clientid = models.IntegerField(db_column='clientid')
    organisationid = models.IntegerField(db_column='organisationid')
    userid = models.IntegerField(db_column='userid')
    description = models.CharField(db_column='description', max_length=100)
    module = models.CharField(db_column='module', max_length=10)
    submodule = models.CharField(db_column='submodule', max_length=10)
    action = models.CharField(db_column='action', max_length=10)
    subaction = models.CharField(db_column='subaction', max_length=10)
    createddate = models.DateTimeField(db_column='createddate')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'error'


class VImportances(models.Model):
    importanceid = models.IntegerField(db_column='importanceid', blank=True, null=True)  # Field name made lowercase.
    importancename = models.CharField(db_column='importancename', max_length=50, blank=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_importances'


class VInteractions(base.Common_Client_Striped):
    interactionid = models.IntegerField(db_column='interactionid', blank=True, null=True)  # Field name made lowercase.
    details = models.CharField(db_column='details', max_length=4000, blank=True)  # Field name made lowercase.
    interactiontype = models.CharField(db_column='interactiontype', blank=True, max_length=50)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_interactions'


class VInvoiceDetail(models.Model):
    invoiceid = models.IntegerField(db_column='invoiceid', primary_key=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    statusid = models.IntegerField(db_column='statusid')  # Field name made lowercase.
    supersededby = models.IntegerField(db_column='supersededby', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    description = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lineno = models.IntegerField(db_column='lineno')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    itemdescription = models.CharField(db_column='itemdescription', max_length=150)  # Field name made lowercase.
    tax1rate = models.DecimalField(db_column='tax1rate', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tax2rate = models.DecimalField(db_column='tax2rate', max_digits=10, decimal_places=2)  # Field name made lowercase.
    tax3rate = models.DecimalField(db_column='tax3rate', max_digits=10, decimal_places=2)  # Field name made lowercase.
    hourlyrate = models.DecimalField(db_column='hourlyrate', max_digits=10, decimal_places=2)  # Field name made lowercase.
    nohours = models.DecimalField(db_column='nohours', max_digits=10, decimal_places=1)  # Field name made lowercase.
    agreedrate = models.DecimalField(db_column='agreedrate', max_digits=10, decimal_places=1)  # Field name made lowercase.
    tax1 = models.DecimalField(max_digits=10, decimal_places=2)
    tax2 = models.DecimalField(max_digits=10, decimal_places=2)
    tax3 = models.DecimalField(max_digits=10, decimal_places=2)
    grosstotal = models.DecimalField(db_column='grosstotal', max_digits=10, decimal_places=2)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='nettotal', max_digits=10, decimal_places=2)  # Field name made lowercase.
    id = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_invoice_detail'


class VLookupsByType(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')  # Field name made lowercase.
    lookupsubtypeid = models.IntegerField(db_column='lookupsubtypeid')  # Field name made lowercase.
    lookuporder = models.IntegerField(db_column='lookuporder')  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_lookups_by_type'


class VMyAssignedprojects(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_assignedprojects'


class VMyAttentionRequired(models.Model):
    type = models.CharField(max_length=7)
    ordercol = models.BigIntegerField()
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    taskdescription = models.TextField(db_column='taskdescription', blank=True)  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemid')  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_attention_required'


class VMyClient(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    user_id = models.IntegerField()
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_client'


class VMyCriticalWork(models.Model):
    type = models.CharField(max_length=7)
    ordercol = models.BigIntegerField()
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    taskdescription = models.TextField(db_column='taskdescription')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemid')  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_critical_work'


class VMyImportantWork(models.Model):
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    taskdescription = models.TextField(db_column='taskdescription')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_important_work'


class VMyInvoiceTimes(models.Model):
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    timeday = models.CharField(db_column='timeday', max_length=40, blank=True)  # Field name made lowercase.
    hours = models.FloatField()
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    timeid = models.IntegerField(db_column='timeid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_invoice_times'


class VMyInvoices(models.Model):
    invoiceid = models.IntegerField(db_column='invoiceid')  # Field name made lowercase.
    statusid = models.IntegerField(db_column='statusid')  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    nohours = models.DecimalField(db_column='nohours', max_digits=32, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    grosstotal = models.DecimalField(db_column='grosstotal', max_digits=32, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nettotal = models.DecimalField(db_column='nettotal', max_digits=32, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    createddatef = models.CharField(db_column='createddatef', max_length=20)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_invoices'


class VMyItems(models.Model):
    projectid = models.IntegerField(db_column='projectid', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_items'


class VMyOrgTasks(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    taskname = models.TextField(db_column='taskname')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_org_tasks'


class VMyOrganisationEvents(models.Model):
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    type = models.BigIntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_organisation_events'


class VMyOrganisations(models.Model):
    clientid = models.IntegerField(db_column='clientid', primary_key=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_organisations'


class VMyPriorities(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    lookuporder = models.IntegerField(db_column='lookuporder')  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_priorities'


class VMyProblemPriorities(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')  # Field name made lowercase.
    lookupsubtypeid = models.IntegerField(db_column='lookupsubtypeid')  # Field name made lowercase.
    lookuporder = models.IntegerField(db_column='lookuporder')  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_problem_priorities'


class VMyProblemScope(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')  # Field name made lowercase.
    lookupsubtypeid = models.IntegerField(db_column='lookupsubtypeid')  # Field name made lowercase.
    lookuporder = models.IntegerField(db_column='lookuporder')  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_problem_scope'


class VMyProblemStatuses(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')  # Field name made lowercase.
    lookupsubtypeid = models.IntegerField(db_column='lookupsubtypeid')  # Field name made lowercase.
    lookuporder = models.IntegerField(db_column='lookuporder')  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_problem_statuses'


class VMyProblems(models.Model):
    problemid = models.IntegerField(db_column='problemid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    problemtype = models.CharField(db_column='problemtype', max_length=200, blank=True)  # Field name made lowercase.
    problemheader = models.CharField(db_column='problemheader', max_length=50)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    problemscope = models.CharField(db_column='problemscope', max_length=200, blank=True)  # Field name made lowercase.
    problemstatus = models.CharField(db_column='problemstatus', max_length=200, blank=True)  # Field name made lowercase.
    problempriority = models.CharField(db_column='problempriority', max_length=200, blank=True)  # Field name made lowercase.
    problemscopeid = models.IntegerField(db_column='problemscopeid', blank=True, null=True)  # Field name made lowercase.
    queueid = models.IntegerField(db_column='queueid', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(db_column='first_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='last_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_problems'


class VMyProgrammes(models.Model):
    problemid = models.IntegerField(db_column='problemid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    problemtype = models.CharField(db_column='problemtype', max_length=200, blank=True)  # Field name made lowercase.
    problemheader = models.CharField(db_column='problemheader', max_length=50)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    problemscope = models.CharField(db_column='problemscope', max_length=200, blank=True)  # Field name made lowercase.
    problemstatus = models.CharField(db_column='problemstatus', max_length=200, blank=True)  # Field name made lowercase.
    problempriority = models.CharField(db_column='problempriority', max_length=200, blank=True)  # Field name made lowercase.
    problemscopeid = models.IntegerField(db_column='problemscopeid', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(db_column='first_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='last_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_problems'


class VMyProjects(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_projects'


class VMyReports(models.Model):
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_reports'


class VMyStatuses(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_statuses'


class VMyTasks(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50)
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    taskstatusid = models.IntegerField(db_column='taskstatusid')
    taskpriorityid = models.IntegerField(db_column='taskpriorityid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_tasks'


class VMyTasktypes(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_tasktypes'


class VMyTime(models.Model):
    timeid = models.IntegerField(db_column='timeid')  # Field name made lowercase.
    timeday = models.CharField(db_column='timeday', max_length=40, blank=True)  # Field name made lowercase.
    timedayraw = models.DateTimeField(db_column='timedayraw')  # Field name made lowercase.
    hours = models.FloatField()
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    timetypeid = models.IntegerField(db_column='timetypeid')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(max_length=50, blank=True)
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_time'


class VMyTimesheet(models.Model):
    timeid = models.IntegerField(db_column='timeid')  # Field name made lowercase.
    timeday = models.DateTimeField()
    timedayf = models.CharField(db_column='timedayf', max_length=40, blank=True)  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50)
    taskdescription = models.TextField(db_column='taskdescription', blank=True)  # Field name made lowercase.
    hours = models.FloatField(blank=True, null=True)
    userid = models.IntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.
    timetypeid = models.IntegerField(db_column='timetypeid')  # Field name made lowercase.
    lookuptypeid = models.IntegerField(db_column='lookuptypeid')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_timesheet'


class VMyUsers(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')
    active = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=101, blank=True)
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    activedesc = models.CharField(db_column='activedesc', max_length=3)  # Field name made lowercase.
    id = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_my_users'


class VNewUserEmails(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_new_user_emails'


class VOrganisationActivity(models.Model):
    activityid = models.IntegerField(db_column='activityid')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    activitydata = models.CharField(db_column='activitydata', max_length=100, blank=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_organisation_activity'


class VOrganisationPotentialUsers(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    company = models.IntegerField(db_column='company')
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_organisation_potential_users'


class VOrganisationProjectManagers(models.Model):
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_organisation_project_managers'


class VOrganisationProjectUsers(models.Model):
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_organisation_project_users'


class VOrganisationUsers(models.Model):
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_organisation_users'


class VOrganisations(models.Model):
    organisationid = models.IntegerField(db_column='organisationid', primary_key=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.
    #id = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_organisations'


class VProblemActivity(models.Model):
    itemid = models.IntegerField(db_column='itemid')  # Field name made lowercase.
    activity = models.CharField(max_length=6)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_problem_activity'


class VProblemAssignees(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    userid = models.IntegerField()
    problemid = models.IntegerField(db_column='problemid')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_problem_assignees'


class VProblemEdit(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    problemid = models.IntegerField(db_column='problemid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    problemdescription = models.CharField(db_column='problemdescription', max_length=2000)  # Field name made lowercase.
    noofpeopleaffected = models.IntegerField(db_column='noofpeopleaffected')  # Field name made lowercase.
    problemscopeid = models.IntegerField(db_column='problemscopeid')  # Field name made lowercase.
    problemsubtypeid = models.IntegerField(db_column='problemsubtypeid', blank=True, null=True)  # Field name made lowercase.
    problemtypeid = models.IntegerField(db_column='problemtypeid')  # Field name made lowercase.
    problemstatusid = models.IntegerField(db_column='problemstatusid', blank=True, null=True)  # Field name made lowercase.
    problempriorityid = models.IntegerField(db_column='problempriorityid', blank=True, null=True)  # Field name made lowercase.
    problemheader = models.CharField(db_column='problemheader', max_length=50)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    queueid = models.IntegerField(db_column='queueid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_problem_edit'


class VProblemJson(models.Model):
    name_exp_1 = models.CharField(db_column='name_exp_1', max_length=343, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_problem_json'


class VProblems(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    problemid = models.IntegerField(db_column='problemid', primary_key=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    problemtype = models.CharField(db_column='problemtype', max_length=200, blank=True)  # Field name made lowercase.
    problemdescription = models.CharField(db_column='problemdescription', max_length=2000)  # Field name made lowercase.
    noofpeopleaffected = models.IntegerField(db_column='noofpeopleaffected')  # Field name made lowercase.
    scope = models.IntegerField()
    problemheader = models.CharField(db_column='problemheader', max_length=50)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200, blank=True)  # Field name made lowercase.
    problemscope = models.CharField(db_column='problemscope', max_length=200, blank=True)  # Field name made lowercase.
    problemstatus = models.CharField(db_column='problemstatus', max_length=200, blank=True)  # Field name made lowercase.
    problempriority = models.CharField(db_column='problempriority', max_length=200, blank=True)  # Field name made lowercase.
    problemscopeid = models.IntegerField(db_column='problemscopeid', blank=True, null=True)  # Field name made lowercase.
    problempriorityid = models.IntegerField(db_column='problempriorityid', blank=True, null=True)  # Field name made lowercase.
    problemstatusid = models.IntegerField(db_column='problemstatusid', blank=True, null=True)  # Field name made lowercase.
    queuename = models.IntegerField(db_column='queuename', blank=True, null=True)
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    createddate = models.CharField(db_column='createddate', max_length=40)
    first_name = models.CharField(db_column='first_name', max_length=50)
    last_name = models.CharField(db_column='last_name', max_length=50)
    id = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_problems'


class VProjectActivity(models.Model):
    activityid = models.IntegerField(db_column='activityid')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    activitytypeid = models.IntegerField(db_column='activitytypeid')  # Field name made lowercase.
    activitydata = models.CharField(db_column='activitydata', max_length=100, blank=True)  # Field name made lowercase.
    activityprojectid = models.IntegerField(db_column='activityProjectid', blank=True, null=True)  # Field name made lowercase.
    activitytasklistid = models.IntegerField(db_column='activityTasklistid', blank=True, null=True)  # Field name made lowercase.
    activitytaskid = models.IntegerField(db_column='activityTaskid', blank=True, null=True)  # Field name made lowercase.
    activitydate = models.DateTimeField(db_column='activityDate')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid', blank=True, null=True)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid', blank=True, null=True)  # Field name made lowercase.
    tasktypeid = models.IntegerField(db_column='tasktypeid', blank=True, null=True)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000, blank=True)  # Field name made lowercase.
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)  # Field name made lowercase.
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby', blank=True, null=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_activity'


class VProjectAssignees(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    userid = models.IntegerField()
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_assignees'


class VProjectDetail(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    programmeid = models.IntegerField(db_column='programmeid', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    stakeholderid = models.IntegerField(db_column='stakeholderid', blank=True, null=True)  # Field name made lowercase.
    projectmanagerid = models.IntegerField(db_column='projectmanagerid', blank=True, null=True)  # Field name made lowercase.
    deliverables = models.CharField(max_length=1500, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    importance = models.IntegerField(blank=True, null=True)
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100, blank=True)  # Field name made lowercase.
    shfirstname = models.CharField(db_column='shFirstname', max_length=50, blank=True)  # Field name made lowercase.
    shlastname = models.CharField(db_column='shLastname', max_length=50, blank=True)  # Field name made lowercase.
    importancedescription = models.CharField(db_column='importancedescription', max_length=50, blank=True)  # Field name made lowercase.
    pmfirstname = models.CharField(db_column='pmFirstname', max_length=50, blank=True)  # Field name made lowercase.
    pmlastname = models.CharField(db_column='pmLastname', max_length=50, blank=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_detail'


class VProjectDocuments(models.Model):
    documentid = models.IntegerField(db_column='documentid')  # Field name made lowercase.
    documenttypeid = models.IntegerField(db_column='documenttypeid')  # Field name made lowercase.
    documentparentid = models.IntegerField(db_column='documentparentid')  # Field name made lowercase.
    documentname = models.CharField(db_column='documentname', max_length=100)  # Field name made lowercase.
    documentfilename = models.CharField(db_column='documentfilename', max_length=100)  # Field name made lowercase.
    documenttitle = models.CharField(db_column='documenttitle', max_length=100, blank=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_documents'


class VProjectGantt(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid', blank=True, null=True)  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50, blank=True)  # Field name made lowercase.
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid', blank=True, null=True)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000, blank=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    taskstartdate = models.DateTimeField(db_column='taskstartdate', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    taskenddate = models.DateTimeField(db_column='taskEnddate', blank=True, null=True)  # Field name made lowercase.
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    taskdeleteddate = models.DateTimeField(db_column='taskDeleteddate', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_gantt'


class VProjectOpinion(models.Model):
    opinionid = models.IntegerField(db_column='opinionid')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemid')  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='itemtype')  # Field name made lowercase.
    opiniontype = models.IntegerField(db_column='opiniontype', blank=True, null=True)  # Field name made lowercase.
    opinion = models.CharField(max_length=250, blank=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_opinion'


class VProjectOpinionDetail(models.Model):
    opinionid = models.IntegerField(db_column='opinionid')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemid')  # Field name made lowercase.
    itemtype = models.IntegerField(db_column='itemtype')  # Field name made lowercase.
    opiniontype = models.IntegerField(db_column='opiniontype', blank=True, null=True)  # Field name made lowercase.
    opiniondescription = models.CharField(db_column='opiniondescription', max_length=50, blank=True)  # Field name made lowercase.
    username = models.CharField(db_column='username', max_length=101, blank=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_opinion_detail'


class VProjectPie(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50, blank=True)  # Field name made lowercase.
    counttasks = models.BigIntegerField(db_column='countTasks')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_pie'


class VProjectTasklists(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_tasklists'


class VProjectTasks(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid', blank=True, null=True)  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50, blank=True)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000, blank=True)  # Field name made lowercase.
    taskdescriptionshort = models.CharField(db_column='taskdescriptionShort', max_length=83, blank=True)  # Field name made lowercase.
    tasktypeid = models.IntegerField(db_column='tasktypeid', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)  # Field name made lowercase.
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    taskstatus = models.CharField(db_column='taskstatus', max_length=50, blank=True)  # Field name made lowercase.
    taskpriority = models.CharField(db_column='taskpriority', max_length=50, blank=True)  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    taskcreatedby = models.IntegerField(db_column='taskCreatedby', blank=True, null=True)  # Field name made lowercase.
    taskdeletedby = models.IntegerField(db_column='task_deleted_by', blank=True, null=True)  # Field name made lowercase.
    tasklistdeletedby = models.IntegerField(db_column='tasklist_deleted_by', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_tasks'


class VProjectUserEmails(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_user_emails'


class VProjectUsers(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    userid = models.IntegerField()
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_project_users'


class VProjectganttJq(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    updateddate = models.DateTimeField(db_column='updateddate', blank=True, null=True)  # Field name made lowercase.
    updatedby = models.IntegerField(db_column='updatedby', blank=True, null=True)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    taskorderid = models.BigIntegerField(db_column='taskorderid')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    taskstartdate = models.BigIntegerField(db_column='taskstartdate', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    taskenddate = models.BigIntegerField(db_column='taskEnddate', blank=True, null=True)  # Field name made lowercase.
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    taskstartdate_unformatted = models.DateTimeField(db_column='taskstartdate_unformatted', blank=True, null=True)  # Field name made lowercase.
    time_estimate = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_projectgantt_jq'


class VQueueUsers(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    userid = models.IntegerField(db_column='userid')
    queueid = models.IntegerField(db_column='queueid')
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    deleteddate = models.DateTimeField(db_column='deleteddate')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_queue_users'


class VQueueTeams(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)
    teamid = models.IntegerField(db_column='teamid')
    queueid = models.IntegerField(db_column='queueid')
    teamname = models.CharField(max_length=50, blank=True)
    deleteddate = models.DateTimeField(db_column='deleteddate')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_queue_teams'


class VRegisteredUser(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    company = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_registered_user'


class VSchedule(models.Model):
    phaseid = models.IntegerField(db_column='phaseid')  # Field name made lowercase.
    phasename = models.CharField(db_column='phasename', max_length=50)
    phasedescription = models.CharField(db_column='phasedescription', max_length=500, blank=True)
    startdate = models.DateTimeField(db_column='startdate', blank=True, null=True)
    taskname = models.CharField(db_column='taskname', max_length=50)
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_schedule'


class VSearch(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    projectdescription = models.CharField(db_column='projectdescription', max_length=500, blank=True)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid', blank=True, null=True)  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50, blank=True)  # Field name made lowercase.
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid', blank=True, null=True)  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50, blank=True)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000, blank=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField()

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_search'


class VSubscribersRecent(models.Model):
    accountname = models.CharField(db_column='accountname', max_length=100)  # Field name made lowercase.
    authenticationid = models.CharField(db_column='authenticationid', max_length=45, blank=True)  # Field name made lowercase.
    authenticationid2 = models.CharField(db_column='authenticationid2', max_length=45, blank=True)  # Field name made lowercase.
    authenticationid3 = models.CharField(db_column='authenticationid3', max_length=45, blank=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='clientname', max_length=100, blank=True)  # Field name made lowercase.
    city = models.CharField(max_length=45, blank=True)
    country = models.CharField(max_length=50, blank=True)
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_subscribers_recent'


class VSubscription(models.Model):
    authenticationid = models.CharField(db_column='authenticationid', max_length=45, blank=True)  # Field name made lowercase.
    authenticationid2 = models.CharField(db_column='authenticationid2', max_length=45, blank=True)  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=75, blank=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_subscription'


class VSuggestProblemLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=50)
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_suggest_problem_links'


class VSuggestProjectLinks(models.Model):
    id = models.IntegerField(primary_key=True)
    value = models.CharField(max_length=50)
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_suggest_project_links'


class VTaskDependency(models.Model):
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')
    tasktypeid = models.IntegerField(db_column='tasktypeid')  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50)  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)  # Field name made lowercase.
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    taskstartdate = models.DateTimeField(db_column='taskstartdate', blank=True, null=True)  # Field name made lowercase.
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    taskpercentcomplete = models.IntegerField(db_column='taskpercentcomplete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_dependency'


class VTaskDetail(models.Model):
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50, blank=True)
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    tasktypeid = models.IntegerField(db_column='tasktypeid')  # Field name made lowercase.
    taskpriority = models.CharField(db_column='taskpriority', max_length=50, blank=True)  # Field name made lowercase.
    taskstatus = models.CharField(db_column='taskstatus', max_length=50, blank=True)  # Field name made lowercase.
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    assignedtoname = models.CharField(db_column='assignedtoname', max_length=101, blank=True)  # Field name made lowercase.
    taskstartdate = models.CharField(db_column='taskstartdate', max_length=10, blank=True)  # Field name made lowercase.
    tasktimeestimate = models.DecimalField(db_column='tasktimeestimate', max_digits=10, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    taskpercentcomplete = models.IntegerField(db_column='taskpercentcomplete', blank=True, null=True)  # Field name made lowercase.
    completiondate = models.CharField(db_column='completiondate', max_length=10, blank=True)
    phaseid = models.IntegerField(db_column='phaseid', blank=True, null=True)
    phasename = models.CharField(db_column='phasename', max_length=50)
    tasklinkid = models.IntegerField(db_column='tasklinkid', blank=True, null=True)  # Field name made lowercase.
    linkedtaskid = models.IntegerField(db_column='linkedTaskid', blank=True, null=True)  # Field name made lowercase.
    linkedtaskname = models.CharField(db_column='linkedTaskname', max_length=50, blank=True)
    linkedtaskdescription = models.CharField(db_column='linkedTaskdescription', max_length=10000, blank=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_detail'


class VTaskDocuments(models.Model):
    documentid = models.IntegerField(db_column='documentid')  # Field name made lowercase.
    documenttypeid = models.IntegerField(db_column='documenttypeid')  # Field name made lowercase.
    documentparentid = models.IntegerField(db_column='documentparentid')  # Field name made lowercase.
    documentname = models.CharField(db_column='documentname', max_length=100)  # Field name made lowercase.
    documentfilename = models.CharField(db_column='documentfilename', max_length=100)  # Field name made lowercase.
    documenttitle = models.CharField(db_column='documenttitle', max_length=100, blank=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='createddate')  # Field name made lowercase.
    createdby = models.IntegerField(db_column='createdby')  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.IntegerField(db_column='deletedby', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_documents'


class VTaskLinks(models.Model):
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    taskidin = models.IntegerField(db_column='taskidIn')  # Field name made lowercase.
    tasklistidin = models.IntegerField(db_column='tasklistidIn')  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=23)  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=50)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_links'


class VTaskStatuses(models.Model):
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    lookupdescription = models.CharField(db_column='lookupdescription', max_length=200)  # Field name made lowercase.
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    lookuporder = models.IntegerField(db_column='lookuporder')  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_statuses'


class VTaskUserEmails(models.Model):
    email = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_user_emails'


class VTaskUsers(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    userid = models.IntegerField()
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_task_users'


# class VTasklistActivity(models.Model):
#     tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
#     date = models.DateTimeField(blank=True, null=True)
#     userid = models.BigIntegerField(db_column='userid', blank=True, null=True)  # Field name made lowercase.
#     name = models.CharField(max_length=101, blank=True)
#     activity = models.CharField(max_length=12)
#
#     class Meta:
#         managed = False
#         app_label = 'simpris'
#         db_table = 'v_tasklist_activity'


class VTasklistProject(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_tasklist_project'


class VTasklistTask(models.Model):
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    tasklistdescription = models.CharField(db_column='tasklistdescription', max_length=500, blank=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=83)  # Field name made lowercase.
    taskpriorityid = models.IntegerField(db_column='taskpriorityid', blank=True, null=True)  # Field name made lowercase.
    taskstatusid = models.IntegerField(db_column='taskstatusid', blank=True, null=True)  # Field name made lowercase.
    taskstatus = models.CharField(db_column='taskstatus', max_length=50, blank=True)  # Field name made lowercase.
    taskpriority = models.CharField(db_column='taskpriority', max_length=50, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_tasklist_task'


class VTasklistUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_tasklist_users'


class VTasklistUsersDistinct(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_tasklist_users_distinct'


class VTeamMembers(models.Model):
    id = models.IntegerField(primary_key=True)
    teamid = models.IntegerField(db_column='teamid')
    teamname = models.CharField(db_column='teamname', max_length=50)
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_team_members'


class VTimeCalendar(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=10000)
    start = models.CharField(max_length=10, blank=True)
    url = models.IntegerField()
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_time_calendar'


class VTimeDetail(models.Model):
    timeid = models.IntegerField(db_column='timeid')  # Field name made lowercase.
    timeday = models.CharField(db_column='timeday', max_length=40, blank=True)  # Field name made lowercase.
    hours = models.FloatField()
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    timetypeid = models.IntegerField(db_column='timetypeid')  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    taskname = models.CharField(db_column='taskname', max_length=10000)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    comments = models.CharField(max_length=50, blank=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_time_detail'


class VTimeGrid(models.Model):
    project = models.CharField(max_length=50)
    projectid = models.IntegerField()
    tasklist = models.CharField(max_length=50)
    tasklistid = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    task = models.CharField(max_length=10000)
    taskid = models.IntegerField()
    timeday = models.DateTimeField(db_column='timeday')  # Field name made lowercase.
    timedaydate = models.DateField(db_column='timedayDate', blank=True, null=True)  # Field name made lowercase.
    starthour = models.CharField(max_length=7, blank=True)
    startmin = models.CharField(max_length=2, blank=True)
    hours = models.FloatField()
    mins = models.FloatField()
    minsformat = models.FloatField()
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_time_grid'


class VTimeTask(models.Model):
    project = models.CharField(max_length=50)
    projectid = models.IntegerField()
    tasklist = models.CharField(max_length=50)
    tasklistid = models.IntegerField()
    task = models.CharField(max_length=50)
    taskid = models.IntegerField()
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_time_task'


class VTimeType(models.Model):
    lookupvaluenum = models.IntegerField(db_column='lookupvaluenum', blank=True, null=True)  # Field name made lowercase.
    lookupvaluechar = models.CharField(db_column='lookupvaluechar', max_length=50, blank=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_time_type'


class VUserAssigned(models.Model):
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    tasklistid = models.IntegerField(db_column='tasklistid')  # Field name made lowercase.
    tasklistname = models.CharField(db_column='tasklistname', max_length=50)  # Field name made lowercase.
    taskid = models.IntegerField(db_column='taskid')  # Field name made lowercase.
    taskdescription = models.CharField(db_column='taskdescription', max_length=10000)  # Field name made lowercase.
    assignedto = models.IntegerField(db_column='assignedto', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='deleteddate', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_assigned'


class VUserAttributes(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    vip = models.CharField(max_length=1)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_attributes'


class VUserContextFull(models.Model):
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    issuperuser = models.IntegerField(db_column='issuperuser')  # Field name made lowercase.
    isstaff = models.IntegerField(db_column='isstaff') 
    clientname = models.CharField(db_column='clientname', max_length=100)
    teamname = models.CharField(db_column='teamname', max_length=100) # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_context_full'


class VUserContextMinimal(models.Model):
    id = models.IntegerField(primary_key=True)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    username = models.CharField(max_length=30)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_context_minimal'


class VUserCurrentProjects(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_current_projects'


class VUserDetail(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    active = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    vip = models.CharField(max_length=1, blank=True)
    pay_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    clientid = models.IntegerField(db_column='clientid')  # Field name made lowercase.
    is_staff = models.IntegerField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_detail'


class VUserGroup(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    group_id = models.IntegerField()
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_group'


class VUserGroupDetail(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    group_id = models.IntegerField()
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_group_detail'


class VUserLogin(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    active = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=40)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_login'


class VUserPotentialProjects(models.Model):
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_potential_projects'


class VUserProjects(models.Model):
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.
    organisationid = models.IntegerField(db_column='organisationid')  # Field name made lowercase.
    projectid = models.IntegerField(db_column='projectid')  # Field name made lowercase.
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_user_projects'


class VUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    active = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'v_users'


class VwSelectOrganisationDetailSidebar(models.Model):
    description = models.CharField(max_length=50)
    column2 = models.CharField(max_length=49, blank=True)
    id = models.CharField(max_length=11)
    column4 = models.BigIntegerField()
    organisationid = models.CharField(db_column='organisationid', max_length=11, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_organisation_detail_sidebar'


class VwSelectOrganisationIndexSidebar(models.Model):
    organisationname = models.CharField(db_column='organisationname', max_length=100)  # Field name made lowercase.
    column2 = models.CharField(max_length=100, blank=True)
    id = models.CharField(max_length=11)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8, primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_organisation_index_sidebar'


class VwSelectProblemDetailSidebar(models.Model):
    description = models.CharField(max_length=13)
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(primary_key=True, max_length=11)
    column4 = models.BigIntegerField()
    problemid = models.IntegerField(db_column='problemid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_problem_detail_sidebar'


class VwSelectProblemIndexSidebar(models.Model):
    problemname = models.CharField(db_column='problemname', max_length=50)  # Field name made lowercase.
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_problem_index_sidebar'


class VwSelectProgrammeHistory(models.Model):
    description = models.CharField(db_column='description', max_length=50)  # Field name made lowercase.
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    programmeid = models.CharField(db_column='programmeid', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_programme_history'


class VwSelectProgrammeIndexSidebar(models.Model):
    problemname = models.CharField(db_column='problemname', max_length=50)  # Field name made lowercase.
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_problem_index_sidebar'


class VwSelectProjectDetailSidebar(models.Model):
    description = models.CharField(max_length=50)
    column2 = models.CharField(max_length=49, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    projectid = models.BigIntegerField(db_column='projectid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_project_detail_sidebar'


class VwSelectProjectIndexSidebar(models.Model):
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    column2 = models.CharField(max_length=100, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8)  # Field name made lowercase.
    dateorder = models.CharField(max_length=23, blank=True)

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_project_index_sidebar'


class VwSelectTaskDetailSidebar(models.Model):
    description = models.CharField(max_length=32)
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    taskid = models.CharField(db_column='taskid', max_length=11)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_task_detail_sidebar'


class VwSelectTaskIndexSidebar(models.Model):
    taskname = models.TextField(db_column='taskname')  # Field name made lowercase.
    column2 = models.CharField(max_length=101, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_task_index_sidebar'


class VwSelectTimeDetailSidebar(models.Model):
    description = models.CharField(max_length=11)
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(primary_key=True, max_length=1)
    column4 = models.BigIntegerField()
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_time_detail_sidebar'


class VwSelectTimeIndexSidebar(models.Model):
    projectname = models.CharField(db_column='projectname', max_length=50)  # Field name made lowercase.
    column2 = models.CharField(max_length=53, blank=True)
    id = models.CharField(max_length=11, primary_key=True)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_time_index_sidebar'


class VwSelectUserDetailSidebar(models.Model):
    description = models.CharField(max_length=11)
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(primary_key=True, max_length=1)
    column4 = models.BigIntegerField()
    userid = models.IntegerField(db_column='userid')  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_user_detail_sidebar'


class VwSelectUserIndexSidebar(models.Model):
    username = models.CharField(db_column='username', max_length=100)  # Field name made lowercase.
    column2 = models.CharField(max_length=40, blank=True)
    id = models.CharField(max_length=8, primary_key=True)
    column4 = models.BigIntegerField()
    userid = models.CharField(db_column='userid', max_length=8)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'simpris'
        db_table = 'vw_select_user_index_sidebar'
