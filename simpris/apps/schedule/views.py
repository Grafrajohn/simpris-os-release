from django.shortcuts import render
import logging
from ...models.db_views import VBoard, VBoardQueue, VSchedule
from ...library.user_context import UserContextFull
from django.db.models import Q
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@login_required
def kanban(request):
    user_context = UserContextFull(request)
    logger.info(str.format('kanban : {0}' .format(user_context.id)))

    tasks = VBoardQueue.objects.all().filter(Q(assignedto=user_context.id)).order_by('id')
    board = VBoard.objects.all().filter(Q(userid=user_context.id))

    context_dict = {'tasks': tasks, 'board': board, 'usercontext': user_context}
    return render(request, "simpris/schedule/kanban.html", context_dict)


@login_required
def schedule(request):
    user_context = UserContextFull(request)
    logger.info(str.format('schedule : {0}' .format(user_context.id)))

    tasks = VBoardQueue.objects.all().filter(Q(assignedto=user_context.id)).order_by('id')
    schedule = VSchedule.objects.all().filter(Q(clientid=user_context.clientID) & (Q(assignedto=user_context.id) | Q(taskid__isnull=True))).order_by('startdate','phaseid')

    context_dict = {'tasks': tasks, 'schedule': schedule, 'usercontext': user_context}
    return render(request, "simpris/schedule/schedule.html", context_dict)
