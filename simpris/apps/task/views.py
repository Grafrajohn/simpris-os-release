from django.shortcuts import render
from ...models.db_views import VwSelectTaskIndexSidebar, VTaskDetail, VCommentsParent, VTaskDocuments, \
        VwSelectTaskDetailSidebar, VTaskStatuses, VMyPriorities, VMyTasktypes, VTaskLinks, VProjectAssignees, \
        VProjectTasklists
from ...models.models import Phase
from ...library.user_context import UserContextFull
from django.db.models import Q
from django.contrib.auth.decorators import login_required

import logging

logger = logging.getLogger(__name__)


# Create your views here.
@login_required
def tasklist(request):
    user_context = UserContextFull(request)
    logger.info(str.format('tasklist list : {0}' .format(user_context.id)))

    context_dict = {'usercontext': user_context}
    return render(request, "simpris/task/tasklist.html", context_dict)


@login_required
def activity(request):
    user_context = UserContextFull(request)
    logger.info(str.format('task activity : {0}' .format(user_context.id)))

    task_activity = VwSelectTaskIndexSidebar.objects.all().filter(Q(userid=user_context.id) | Q(userid=''))
    context_dict = {'sidebar': task_activity, 'usercontext': user_context}
    return render(request, "simpris/task/activity.html", context_dict)


@login_required
def detail(request, task_id):
    user_context = UserContextFull(request)
    logger.info(str.format('task detail : {0}' .format(user_context.id)))

    task_data = VTaskDetail.objects.all().filter(Q(taskid=task_id, clientid=user_context.clientID))[:1]
    comment_data = VCommentsParent.objects.all().filter(Q(parentid=task_id, parenttypeid=3))
    document_data = VTaskDocuments.objects.all().filter(Q(documentparentid=task_id))
    upload_label = 'Upload a document for this task:'

    context_dict = {'id': task_id, 'tasks': task_data, 'comments': comment_data, 'documents': document_data,
                    'upload_label': upload_label, 'item_id': task_id, 'item_type': 'tsk',
                    'parent_type': 3, 'item_label': 'task'}

    return render(request, "simpris/task/detail.html", context_dict)


@login_required
def edit(request, task_id):
    user_context = UserContextFull(request)
    logger.info(str.format('task edit : {0}' .format(user_context.id)))

    task_status_data = VTaskStatuses.objects.all().filter(Q(clientid=0))
    task_priority_data = VMyPriorities.objects.all().filter(Q(clientid=0))
    task_assignee_data = VProjectAssignees.objects.all().filter(Q(taskid=task_id))
    task_documents_data = VTaskDocuments.objects.all().filter(Q(documentparentid=task_id, documenttypeid=3))
    task_data = VTaskDetail.objects.all().filter(Q(taskid=task_id, userid=user_context.id))
    task_type_data = VMyTasktypes.objects.all().filter(Q(clientid=0))
    task_dependency_data = VTaskLinks.objects.all().filter(Q(taskidin=task_id))
    task_phase_data = Phase.objects.all().filter(Q(clientid=user_context.clientID))

    context_dict = {'id': task_id, 'tasks': task_data, 'task_types': task_type_data, 'task_statuses': task_status_data,
                    'task_priorities': task_priority_data, 'task_assignees': task_assignee_data,
                    'documents': task_documents_data, 'dependencies': task_dependency_data,
                    'upload_label': 'Upload a new supporting document for your task:',
                    'item_type': 'tsk', 'item_id': task_id, 'phases': task_phase_data,  'usercontext': user_context}

    return render(request, "simpris/task/edit.html", context_dict)


@login_required
def history(request, task_id):
    user_context = UserContextFull(request)
    logger.info(str.format('task history : {0}' .format(user_context.id)))

    history_data = VwSelectTaskDetailSidebar.objects.all().filter(Q(taskid=task_id))[:1]

    context_dict = {'id': task_id, 'history': history_data}

    return render(request, "simpris/task/history.html", context_dict)


@login_required
def move(request, task_id):
    user_context = UserContextFull(request)
    logger.info(str.format('task move : {0}' .format(user_context.id)))

    project_task_lists = VProjectTasklists.objects.all().filter(Q(clientid=user_context.clientID,
                                                                  userid=user_context.id)).distinct()
    task_data = VTaskDetail.objects.all().filter(Q(taskid=task_id, userid=user_context.id)).distinct()

    context_dict = {'id': task_id, 'tasklists': project_task_lists, 'tasks': task_data}

    return render(request, "simpris/task/move.html", context_dict)
