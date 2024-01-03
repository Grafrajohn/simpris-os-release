import logging, time

from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from ...models.db_views import VwSelectProblemIndexSidebar, VwSelectProblemDetailSidebar, \
                    VProblems, VActualProblemLinks, VProblemEdit, VMyProblemStatuses, \
                    VMyProblemPriorities, VMyProblemScope, VSuggestProblemLinks, VSuggestProjectLinks, \
                    VProblemAssignees, VMyOrganisations, VLookupsByType
from ...models.models import Document, Queue, Comment, AuthUser, ProblemLog
from ...library.user_context import UserContextFull


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
def problemlist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('problem index : {0}' .format(user_context.id)))

    problem_activity = VwSelectProblemIndexSidebar.objects.all().filter(Q(userid=user_context.id) | Q(userid=''))
    problem_queues = Queue.objects.all().filter(Q(clientid=user_context.clientID))
    context_dict = {'usercontext': user_context, 'queues': problem_queues}
    return render(request, "simpris/problem/problemlist.html", context_dict)


@login_required
def activity(request):
    user_context = UserContextFull(request)
    logger.info(str.format('problem activity : {0}' .format(user_context.id)))

    problem_activity = VwSelectProblemIndexSidebar.objects.all().filter(Q(userid=user_context.id) | Q(userid=''))
    context_dict = {'sidebar': problem_activity, 'usercontext': user_context}
    return render(request, "simpris/problem/activity.html", context_dict)


@login_required
def create(request):
    user_context = UserContextFull(request)
    logger.info(str.format('problem create : {0}' .format(user_context.id)))

    organisations = VMyOrganisations.objects.all().filter(Q(userid=user_context.id) & Q(deleteddate__isnull=True)).order_by('organisationname').distinct()
    problem_statuses = VMyProblemStatuses.objects.all().filter(Q(clientid=0)).order_by('lookupvaluechar')
    problem_priorities = VMyProblemPriorities.objects.all().filter(Q(clientid=0)).order_by('lookupvaluechar')
    problem_scopes = VMyProblemScope.objects.all().filter(Q(clientid=0)).order_by('lookupvaluechar')
    problem_types = VLookupsByType.objects.all().filter(Q(clientid=0,lookuptypeid=8)).order_by('lookupvaluechar')
    problem_subtypes = VLookupsByType.objects.all().filter(Q(clientid=0,lookuptypeid=9)).order_by('lookupvaluechar')
    queues = Queue.objects.all().filter(Q(deleteddate__isnull=True))

    context_dict = {'organisations': organisations, 'problem_statuses': problem_statuses, 'problem_priorities': problem_priorities,
                    'problem_scopes': problem_scopes, 'problem_types': problem_types, 'problem_subtypes': problem_subtypes,
                    'queues': queues, 'usercontext': user_context}

    return render(request, "simpris/problem/create.html", context_dict)


@login_required
def detail(request, prob_id):
    user_context = UserContextFull(request)
    logger.info(str.format('problem create : {0}' .format(user_context.id)))

    problem_data = VProblems.objects.all().filter(Q(problemid=prob_id) &
                                                  Q(clientid=user_context.clientID))
    link_data = VActualProblemLinks.objects.all().filter(Q(problemid=prob_id))
    documents = Document.objects.all().filter(Q(documentparentid=prob_id))

    context_dict = {'id': prob_id, 'problems': problem_data, 'links': link_data, 'documents': documents,
                    'item_label': 'problem', 'item_type': 'prb', 'usercontext': user_context}

    return render(request, "simpris/problem/detail.html", context_dict)


@login_required
def edit(request, prob_id):
    user_context = UserContextFull(request)
    logger.info(str.format('problem edit : {0}' .format(user_context.id)))

    problem_data = VProblemEdit.objects.all().filter(Q(problemid=prob_id) &
                                                  Q(clientid=user_context.clientID))
    problem_statuses = VMyProblemStatuses.objects.all().filter(Q(clientid=0))
    problem_priorities = VMyProblemPriorities.objects.all().filter(Q(clientid=0))
    problem_scopes = VMyProblemScope.objects.all().filter(Q(clientid=0))
    problem_suggested_links = VSuggestProblemLinks.objects.all().filter(Q(userid=user_context.id))
    project_suggested_links = VSuggestProjectLinks.objects.all().filter(Q(userid=user_context.id))
    problem_actual_links = VActualProblemLinks.objects.all().filter(Q(problemid=prob_id))
    problem_assignees = VProblemAssignees.objects.all().filter(Q(problemid=prob_id))
    documents = Document.objects.all().filter(Q(documentparentid=prob_id))
    problem_types = VLookupsByType.objects.all().filter(Q(clientid=0,lookuptypeid=8)).order_by('lookupvaluechar')
    problem_subtypes = VLookupsByType.objects.all().filter(Q(clientid=0,lookuptypeid=9)).order_by('lookupvaluechar')
    queues = Queue.objects.all().filter(Q(deleteddate__isnull=True) & Q(clientid=user_context.clientID))

    problem_actual_link_type = 0
    problem_actual_link_id = 0
    project_actual_link_id = 0
    project_actual_link_type = 0
    for link in problem_actual_links:
        if link.problemlinktype == 1:
            project_actual_link_id = link.problemlinkid or 0
            project_actual_link_type = link.problemlinktype or 0
        if link.problemlinktype == 2:
            problem_actual_link_id = link.problemlinkid or 0
            problem_actual_link_type = link.problemlinktype or 0

    context_dict = {'id': prob_id, 'problem': problem_data, 'problem_statuses': problem_statuses,
                    'problem_priorities': problem_priorities, 'problem_scopes': problem_scopes,
                    'problem_suggested_links': problem_suggested_links,
                    'project_suggested_links': project_suggested_links,
                    'problem_actual_links': problem_actual_links, 'problem_assignees': problem_assignees,
                    'problem_types': problem_types, 'problem_subtypes': problem_subtypes,
                    'problem_actual_link_id': problem_actual_link_id,
                    'problem_actual_link_type': problem_actual_link_type,
                    'project_actual_link_id': project_actual_link_id,
                    'project_actual_link_type': project_actual_link_type,
                    'documents': documents,
                    'queues': queues,
                    'upload_label': 'Upload a new supporting document for your problem:',
                    'item_type': 'prb',
                    'item_id': prob_id,
                    'item_label': 'problem',
                    'usercontext': user_context}

    return render(request, "simpris/problem/edit.html", context_dict)


@login_required
def history(request, prob_id):
    user_context = UserContextFull(request)
    logger.info(str.format('problem log : {0}' .format(user_context.id)))

    problem_history = VwSelectProblemDetailSidebar.objects.all().filter(Q(problemid=prob_id))
    # problem_log = ProblemLog.objects.values('comment__commenttext').filter(Q(parentid=prob_id) & Q(parenttypeid=4)).order_by('createddate').reverse()
    problem_log = Comment.objects.all().filter(Q(parentid=prob_id) & Q(parenttypeid=4)).order_by('createddate').reverse()


    context_dict = {'id': prob_id, 'history': problem_history, 'log': problem_log, 'entity': 'problem', 'parent_type': 4,
        'usercontext': user_context}

    return render(request, "simpris/problem/log.html", context_dict)


@login_required
def log(request, prob_id):
    user_context = UserContextFull(request)
    logger.info(str.format('problem log : {0}' .format(user_context.id)))

    problem_history = VwSelectProblemDetailSidebar.objects.all().filter(Q(problemid=prob_id))
    # problem_log = ProblemLog.objects.values('comment__commenttext').filter(Q(parentid=prob_id) & Q(parenttypeid=4)).order_by('createddate').reverse()
    problem_log = Comment.objects.all().filter(Q(parentid=prob_id) & Q(parenttypeid=4)).order_by('createddate').reverse()


    context_dict = {'id': prob_id, 'history': problem_history, 'log': problem_log, 'entity': 'problem', 'parent_type': 4,
        'usercontext': user_context}

    return render(request, "simpris/problem/log.html", context_dict)
