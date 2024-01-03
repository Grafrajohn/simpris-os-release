import logging

from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from django.core import serializers
from django.conf import settings

from ...models.db_views import VwSelectProjectIndexSidebar, VProjectDetail, VProjectTasks, VProjectOpinionDetail
from ...models.db_views import VProjectDocuments, VTaskStatuses, VMyPriorities, VMyTasktypes, VTasklistUsersDistinct
from ...models.db_views import VwSelectProjectDetailSidebar, VImportances, VProjectGantt
from ...models.db_views import VOrganisationProjectManagers, VMyOrganisations
from ...models.models import Phase, Comment
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
def index(request):
    user_context = UserContextFull(request)
    logger.info(str.format('home index : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/project/home.html", context_dict)


@login_required
def activity(request):
    user_context = UserContextFull(request)
    logger.info(str.format('project activity : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context, 'BASE_URL_DJ': settings.BASE_URL_DJ}
    return render(request, "simpris/project/activity.html", context_dict)


@login_required
def projectlist(request):

    user_context = UserContextFull(request)
    logger.info(str.format('project list : {0}' .format(user_context.id)))

    project_activity = VwSelectProjectIndexSidebar.objects.all().filter(Q(userid=user_context.id) | Q(userid='')).order_by('column4', 'projectname')
    context_dict = {'sidebar': project_activity, 'usercontext': user_context}
    return render(request, "simpris/project/projectlist.html", context_dict)


@login_required
@permission_required('simpris.add_project','/project/home/')
def create(request):
    logger.info('project create')

    user_context = UserContextFull(request)

    # organisation_users = VOrganisationProjectUsers.objects.all().filter(Q(organisationid=user_context.organisationID))
    project_managers = VOrganisationProjectManagers.objects.values('userid','first_name','last_name').filter(Q(organisationid=user_context.organisationID))\
        .order_by('first_name').distinct()
    importances = VImportances.objects.all().filter(Q())
    organisations = VMyOrganisations.objects.all().filter(Q(userid=user_context.id) & Q(deleteddate__isnull=True))

    context_dict = {'importances': importances, 'organisations': organisations, 'organisationusers': project_managers,
                    'superuser': 0, 'staff': 0,
                    'usercontext': user_context}

    return render(request, "simpris/project/create.html", context_dict)


@login_required          
def detail(request, proj_id):
    user_context = UserContextFull(request)
    logger.info(str.format('project detail : {0}' .format(user_context.id)))

    project = VProjectDetail.objects.all().filter(Q(userid=user_context.id) & Q(projectid=proj_id) &
                                                  Q(clientid=user_context.clientID))
    tasks = VProjectTasks.objects.all().filter(Q(projectid=proj_id,clientid=user_context.clientID,taskdeletedby__isnull=True,tasklistdeletedby__isnull=True)).order_by('projectid', 'tasklistid', 'taskpriorityid')
    documents = VProjectDocuments.objects.all().filter(Q(documentparentid=proj_id))
    opinions = VProjectOpinionDetail.objects.all().filter(Q(projectid=proj_id))
    tasktypes = VMyTasktypes.objects.all().filter(Q(clientid=0))
    taskstatuses = VTaskStatuses.objects.all().filter(Q(clientid=0))
    taskpriorities = VMyPriorities.objects.all().filter(Q(clientid=0))
    tasklistusers = VTasklistUsersDistinct.objects.all().order_by('last_name')\
        .distinct().filter(Q(clientid=user_context.clientID) & Q(projectid=proj_id))
    phases = Phase.objects.all().filter(Q(clientid=user_context.clientID))

    context_dict = {'projects': project, 'tasks': tasks, 'id': proj_id, 'user_context': user_context,
                    'documents': documents, 'opinion': opinions, 'tklusers': tasklistusers,
                    'tasktypes': tasktypes, 'taskstatuses': taskstatuses, 'taskpriorities': taskpriorities,
                    'item_type': 'prj', 'item_label': 'project', 'phases': phases, 'usercontext': user_context}
    
    return render(request, "simpris/project/detail.html", context_dict)


@login_required
@permission_required('simpris.change_project','/project/home/')
def edit(request, proj_id):
    user_context = UserContextFull(request)
    logger.info(str.format('project edit : {0}' .format(user_context.id)))

    project = VProjectDetail.objects.all().filter(Q(userid=user_context.id) & Q(projectid=proj_id) &
                                                  Q(clientid=user_context.clientID))
    documents = VProjectDocuments.objects.all().filter(Q(documentparentid=proj_id))
    opinions = VProjectOpinionDetail.objects.all().filter(Q(projectid=proj_id) & Q(userid=user_context.id))
    organisation_users = VOrganisationProjectManagers.objects.values('userid','first_name','last_name').filter(Q(organisationid=user_context.organisationID))\
        .order_by('first_name').distinct()
    importances = VImportances.objects.all().filter(Q())

    project_users = __project_users(proj_id)
    project_potential_users = __project_potential_users(proj_id)

    context_dict = {'projects': project, 'users': project_users, 'id': proj_id, 'organisationusers': organisation_users,
                    'potentials': project_potential_users, 'usercontext': user_context, 'importances': importances,
                    'documents': documents, 'opinion': opinions, 'superuser': 0, 'staff': 0,
                    'upload_label': 'Upload a new supporting document for your project:', 'item_type': 'prj', 'item_id': proj_id,
                    'item_label': 'project'}

    return render(request, "simpris/project/edit.html", context_dict)


@login_required
def gantt(request, proj_id):
    logger.info('gantt index')

    user_context = UserContextFull(request)

    project_data = VProjectGantt.objects.all().filter(Q(projectid=proj_id) & Q(deleteddate__isnull=True) & Q(taskdeleteddate__isnull=True))

    json_objects = serializers.serialize('json',project_data)

    project = VProjectDetail.objects.all().filter(Q(userid=user_context.id) & Q(projectid=proj_id) &
                                                  Q(clientid=user_context.clientID))

    context_dict = {'id': proj_id, 'projects': project, 'json_raw': json_objects, 'usercontext': user_context}
    return render(request, "simpris/project/gantt.html", context_dict)


@login_required
def history(request, proj_id):
    logger.info('project history')

    user_context = UserContextFull(request)
    logger.info(user_context.id)

    project_history = VwSelectProjectDetailSidebar.objects.all().filter(Q(projectid=proj_id))
    context_dict = {'id': proj_id, 'history': project_history, 'usercontext': user_context}
    return render(request, "simpris/project/history.html", context_dict)


@login_required
def ideas(request, proj_id):
    user_context = UserContextFull(request)
    logger.info(str.format('ideas : {0}' .format(user_context.id)))

    context_dict = {'id': proj_id}
    return render(request, "simpris/project/ideas.html", context_dict)


@login_required
def log(request, proj_id):
    user_context = UserContextFull(request)
    logger.info(str.format('log : {0}' .format(user_context.id)))

    project_history = VwSelectProjectDetailSidebar.objects.all().filter(Q(projectid=proj_id))
    project_log = Comment.objects.all().filter(Q(parentid=proj_id) & Q(parenttypeid=2)).order_by('createddate').reverse()
    context_dict = {'id': proj_id, 'history': project_history, 'log': project_log, 'entity': 'project', 'parent_type': 2,
        'usercontext': user_context}
    return render(request, "simpris/project/log.html", context_dict)


@login_required
def users(request, proj_id):
    logger.info('project users')

    user_context = UserContextFull(request)
    logger.info(str.format('users : {0}' .format(user_context.id)))

    # project = VProjectDetail.objects.all().filter(Q(userid=user_context.id) & Q(projectid=proj_id) &
    #                                               Q(clientid=user_context.clientID))
    project_users = __project_users(proj_id)
    project_potential_users = __project_potential_users(proj_id)

    context_dict = {'id': proj_id, 'users': project_users, 'potentials': project_potential_users, 'usercontext': user_context}
    return render(request, "simpris/project/users.html", context_dict)


def __project_users(proj_id):

    cur = connection.cursor()
    try:
        cur.callproc('simpricity.sr_get_project_users', [proj_id])
        project_users = cur.fetchall()

    finally:
        cur.close()

    return project_users


def __project_potential_users(proj_id):

    cur = connection.cursor()
    try:
        cur.callproc('simpricity.sr_get_project_potential_users', [proj_id])
        project_potential_users = cur.fetchall()

    finally:
        cur.close()

    potentials = project_potential_users

    return potentials
