import logging
import time

from django.contrib.auth.models import User, Group
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from rest_framework.response import Response
from rest_framework import viewsets, serializers
from rest_framework.decorators import api_view

from simpris.api.project.serializers import UserSerializer, GroupSerializer, VMyCriticalWorkSerializer, \
    VClientsSerializer, VProjectsSerializer, UserProjectSerializer, VProjectTasklistsSerializer, \
    VProjectTasklistsSearchSerializer, VProjectSimpleSerializer, APIProjectSerializer, APIUserProjectSerializer
from simpris.models.db_views import VMyCriticalWork, VMyOrganisations, VMyProjects, VProjectTasklists
from simpris.models.models import Project, Userproject, Organisation
from simpris.library.user_context import UserContextFull, UserContextFull
from simpris.library import emailer


logger = logging.getLogger(__name__)


@api_view(['GET'])
def home(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home : {0}'.format(user_context.id)))

    queryset = VMyCriticalWork.objects.all().filter(clientid=user_context.clientID, assignedto=user_context.id)
    serializer_class = VMyCriticalWorkSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['POST'])
def programme(request):
    user_context = UserContextFull(request)
    logger.info(str.format('programme list : {0}'.format(user_context.id)))

    project_id = request.POST.get('hidProjectID')
    programme_id = request.POST.get('hidProgrammeID')

    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    project_serializer = APIProjectSerializer(data={'projectid': project_id,
                                                    'clientid': user_context.clientID,
                                                    'programmeid': programme_id,
                                                    'organisationid': 1,
                                                    'projectname': "DUMMY",
                                                    'projectdescription': "DUMMY",
                                                    'stakeholderid': 0,
                                                    'projectmanagerid': 0,
                                                    'deliverables': "DUMMY",
                                                    'budget': 0,
                                                    'importance': 0,
                                                    'createdby': updated_by,
                                                    'createddate': updated_date})

    if project_serializer.is_valid():

        prj = Project.objects.get(projectid=project_id)
        prj.programmeid = programme_id
        prj.updatedby = updated_by
        prj.updateddate = updated_date
        prj.save(
            update_fields=['programmeid', 'updateddate', 'updatedby'])

        subject = "Simpris: Project " + prj.projectname + " has been added to a programme"
        url = settings.BASE_URL_DJ + '/project/detail/' + project_id
        message = "You can view the changes by clicking on this link: " + url
        email_from = settings.EMAIL_FROM
        emailer_simpris = emailer
        try:
            if prj.stakeholderid != None:
                emailer_simpris.send_smtp_email("pr","u",email_from,prj.stakeholderid,subject,message)
            if prj.projectmanagerid != None:
                emailer_simpris.send_smtp_email("pr","u",email_from,prj.projectmanagerid,subject,message)
        except Exception as e:
            logger.error(e)
            pass

        response = project_id

    else:
        errors = project_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(project_serializer.errors)

    return Response(response)


@api_view(['POST'])
def programme_project_delete(request):
    user_context = UserContextFull(request)
    logger.info(str.format('programme project delete : {0}'.format(user_context.id)))

    project_id = request.POST.get('project_id')
    programme_id = request.POST.get('programme_id')

    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    project_serializer = APIProjectSerializer(data={'projectid': project_id,
                                                    'clientid': user_context.clientID,
                                                    'programmeid': programme_id,
                                                    'organisationid': 1,
                                                    'projectname': "DUMMY",
                                                    'projectdescription': "DUMMY",
                                                    'stakeholderid': 0,
                                                    'projectmanagerid': 0,
                                                    'deliverables': "DUMMY",
                                                    'budget': 0,
                                                    'importance': 0,
                                                    'createdby': updated_by,
                                                    'createddate': updated_date})

    if project_serializer.is_valid():

        prj = Project.objects.get(projectid=project_id)
        prj.programmeid = None
        prj.updatedby = updated_by
        prj.updateddate = updated_date
        prj.save(
            update_fields=['programmeid', 'updateddate', 'updatedby'])

        subject = "Simpris: Project " + prj.projectname + " has been added to a programme"
        url = settings.BASE_URL_DJ + '/project/detail/' + project_id
        message = "You can view the changes by clicking on this link: " + url
        email_from = settings.EMAIL_FROM
        emailer_simpris = emailer
        try:
            if prj.stakeholderid != None:
                emailer_simpris.send_smtp_email("pr","u",email_from,prj.stakeholderid,subject,message)
            if prj.projectmanagerid != None:
                emailer_simpris.send_smtp_email("pr","u",email_from,prj.projectmanagerid,subject,message)
        except Exception as e:
            logger.error(e)
            pass

        response = project_id

    else:
        errors = project_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(project_serializer.errors)

    return Response(response)


@api_view(['GET'])
def project_search(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project search : {0}'.format(user_context.id)))

    queryset = VProjectTasklists.objects.values('projectname', 'tasklistid', 'tasklistname').filter(userid=user_context.id, clientid=user_context.clientID, deleteddate__isnull=True).order_by('projectname', 'tasklistname').distinct()
    serializer_class = VProjectTasklistsSearchSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def project_search_json(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project search json : {0}'.format(user_context.id)))

    term = str(request.GET.get('term'))

    queryset = VProjectTasklists.objects.values('projectid', 'projectname').filter(userid=user_context.id, clientid=user_context.clientID,
                                           deleteddate__isnull=True, projectname__icontains=term).order_by('projectname').distinct()
    serializer_class = VProjectSimpleSerializer(queryset, many=True)

    return Response(serializer_class.data)


@api_view(['GET'])
def projects(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project list : {0}'.format(user_context.id)))

    queryset = VMyProjects.objects.all().filter(clientid=user_context.clientID, userid=user_context.id, deleteddate__isnull=True).order_by('projectname').distinct()
    serializer_class = VProjectsSerializer(queryset, many=True)

    return Response(serializer_class.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


@api_view(['GET','POST'])
def delete(request, proj_id):
    user_context = UserContextFull(request)
    logger.info(str.format('project delete : {0}' .format(user_context.id)))

    project_id = proj_id
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    project_serializer = APIProjectSerializer(data={'projectid': 0,
                                                    'clientid': 0,
                                                    'organisationid': 1,
                                                    'projectname': 'NAME',
                                                    'projectdescription': 'DESC',
                                                    'stakeholderid': 0,
                                                    'projectmanagerid': 0,
                                                    'deliverables': 'DELIV',
                                                    'budget': 1, 'importance': 1,
                                                    'createdby': deleted_by,
                                                    'createddate': deleted_date,
                                                    'deletedby': deleted_by,
                                                    'deleteddate': deleted_date})

    user = User.objects.get(id=request.user.id)
    if project_serializer.is_valid() and (user.has_perm('simpris.delete_project')):

        prj = Project.objects.get(projectid=project_id, clientid=user_context.clientID)
        prj.deletedby = deleted_by
        prj.deleteddate = deleted_date
        prj.save(
            update_fields=['deleteddate', 'deletedby'])

        response = project_id

    else:
        errors = project_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(project_serializer.errors)

    return Response(response)


@api_view(['POST'])
def deleteuser(request):
    user_context = UserContextFull(request)
    logger.info(str.format('projectuser delete : {0}' .format(user_context.id)))

    project_id = request.POST.get('hidUserProjectID')
    user_id = request.POST.get('user_project_id')
    deleted_date = time.strftime('%Y-%m-%d %H:%M:%S')
    deleted_by = user_context.id

    project_user_serializer = UserProjectSerializer(data={'userid': user_id, 'projectid': project_id,
                                                          'deletedby': deleted_by, 'deleteddate': deleted_date})

    if project_user_serializer.is_valid():

        up = Userproject.objects.get(userid=user_id, projectid=project_id, deleteddate__isnull=True)
        up.deletedby = deleted_by
        up.deleteddate = deleted_date
        up.save()

        response = {'userid': user_id}

    else:
        errors = project_user_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        response = {'responseText': project_user_serializer.errors}

    return Response(response)


@api_view(['POST'])
def insert(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project insert : {0}' .format(user_context.id)))

    project_id = 0
    organisation_id = request.POST.get('frmProjectOrganisation')
    project_name = request.POST.get('frmProjectName')
    project_description = request.POST.get('ckeditedDescription')
    stakeholder_id = request.POST.get('frmProjectStakeholder')
    project_manager_id = request.POST.get('frmProjectManager')
    deliverables = request.POST.get('ckeditedDeliverables')
    budget = request.POST.get('frmProjectBudget') or 0
    importance = request.POST.get('frmProjectImportance')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    organisation = Organisation.objects.get(organisationid=organisation_id)

    project_serializer = APIProjectSerializer(data={'projectid': project_id,
                                                    'clientid': user_context.clientID,
                                                    'organisationid': organisation_id,
                                                    'projectname': project_name,
                                                    'projectdescription': project_description,
                                                    'stakeholderid': 0,
                                                    'projectmanagerid': 0,
                                                    'deliverables': deliverables,
                                                    'budget': budget, 'importance': importance, 'createdby': updated_by,
                                                    'createddate': updated_date})

    if project_serializer.is_valid():

        project_new = Project(clientid=user_context.clientID, organisationid=organisation,
                      projectname=project_name, projectdescription=project_description,
                      # stakeholderid=stakeholder_id, projectmanagerid=project_manager_id,
                      deliverables=deliverables, budget=budget, importance=importance,
                      createdby=updated_by, createddate=updated_date)
        project_new.save(force_insert=True)

        project_object = Project.objects.filter(clientid=user_context.clientID, createdby=updated_by).latest('projectid')

        prjusr = Userproject(userid=user_context.id, projectid=project_object, createddate=updated_date, createdby=updated_by)
        prjusr.save()

        subject = 'Simpris: Project "' + project_name + '" has been created'
        url = settings.BASE_URL_DJ + '/project/detail/' + str(project_object.projectid)
        message = "You can view the project by clicking on this link: " + url
        email_from = settings.EMAIL_FROM
        emailer_simpris = emailer
        try:
            emailer_simpris.send_smtp_email("pr", "u", email_from, updated_by, subject, message)
        except:
            logger.error("Email send error project insert: " + project_name)
        response = {'project_id': project_object.projectid}

    else:
        errors = project_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        response = {'responseText': project_serializer.errors}

    return Response(response)


@api_view(['POST'])
def update(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project update : {0}' .format(user_context.id)))

    project_id = request.POST.get('hidProjectID')
    organisation_id = request.POST.get('hidOrganisationID')
    project_name = request.POST.get('frmProjectName')
    project_description = request.POST.get('ckeditedDescription')
    stakeholder_id = request.POST.get('frmProjectStakeholder')
    project_manager_id = request.POST.get('frmProjectManager')
    deliverables = request.POST.get('ckeditedDeliverables')
    budget = request.POST.get('frmProjectBudget')
    importance = request.POST.get('frmProjectImportance')
    updated_date = time.strftime('%Y-%m-%d %H:%M:%S')
    updated_by = user_context.id

    project_serializer = APIProjectSerializer(data={'projectid': 0,
                                                    'clientid': user_context.clientID,
                                                    'organisationid': organisation_id,
                                                    'projectname': project_name,
                                                    'projectdescription': project_description,
                                                    'stakeholderid': stakeholder_id,
                                                    'projectmanagerid': project_manager_id,
                                                    'deliverables': deliverables,
                                                    'budget': budget,
                                                    'importance': importance,
                                                    'createdby': updated_by,
                                                    'createddate': updated_date})

    if project_serializer.is_valid():

        prj = Project.objects.get(projectid=project_id)
        prj.projectname = project_name
        prj.projectdescription = project_description
        prj.stakeholderid = stakeholder_id
        prj.projectmanagerid = project_manager_id
        prj.deliverables = deliverables
        prj.budget = budget
        prj.importance = importance
        prj.updatedby = updated_by
        prj.updateddate = updated_date
        prj.save(
            update_fields=['projectname', 'projectdescription', 'stakeholderid', 'projectmanagerid', 'deliverables',
                           'budget', 'importance', 'updateddate', 'updatedby'])

        if stakeholder_id != None:
            try:
                user_project_stakeholder = Userproject.objects.get(userid=stakeholder_id,
                                                                   projectid=project_id)
            except ObjectDoesNotExist:
                user_project = Userproject(userid=stakeholder_id, projectid=prj,
                                           createddate=updated_date, createdby=updated_by)
                user_project.save()
            except MultipleObjectsReturned:
                pass

        if project_manager_id != None:
            try:
                user_project_stakeholder = Userproject.objects.get(userid=project_manager_id,
                                                                   projectid=project_id)
            except ObjectDoesNotExist:
                user_project = Userproject(userid=project_manager_id, projectid=prj,
                                           createddate=updated_date, createdby=updated_by)
                user_project.save()
            except MultipleObjectsReturned:
                pass

        if stakeholder_id != None or project_manager_id != None:
            subject = "Simpris: Project " + project_name + " has been edited"
            url = settings.BASE_URL_DJ + '/project/detail/' + project_id
            message = "You can view the changes by clicking on this link: " + url
            email_from = settings.EMAIL_FROM
            emailer_simpris = emailer
            if stakeholder_id != None:
                emailer_simpris.send_smtp_email("pr","u",email_from,stakeholder_id,subject,message)
            if project_manager_id != None:
                emailer_simpris.send_smtp_email("pr","u",email_from,project_manager_id,subject,message)

        messages.success(request._request, 'Project successfully updated.')

        response = project_id

    else:
        errors = project_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(project_serializer.errors)

    return Response(response)


@api_view(['POST'])
def insertuser(request):
    user_context = UserContextFull(request)
    logger.info(str.format('insert user : {0}'.format(user_context.id)))

    if request.POST.get('hidUserProjectID'):
        project_id = request.POST.get('hidUserProjectID')
    else:
        project_id = request.POST.get('selUserProject')
    if request.POST.get('selProjectUser'):
        user_id = request.POST.get('selProjectUser')
    else:
        user_id = request.POST.get('hidUserID')

    created_date = time.strftime('%Y-%m-%d %H:%M:%S')
    created_by = user_context.id

    projectid = Project.objects.get(projectid=project_id)

    project_user_serializer = APIUserProjectSerializer(data={'id': 0, 'projectid': project_id, 'userid': user_id,
                                                             'createdby': created_by, 'createddate': created_date})

    if project_user_serializer.is_valid():

        upr = Userproject(projectid=projectid, userid=user_id, createddate=created_date, createdby=created_by)
        upr.save()

        response = project_id

    else:
        errors = project_user_serializer.errors.items()
        for error in errors:
            logger.error("Key: " + str(error[0]) + "Value: " + str(error[1]))
        raise serializers.ValidationError(project_user_serializer.errors)

    return Response(response)
