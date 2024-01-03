from django.shortcuts import render
from django.shortcuts import redirect
from ...models.db_views import VwSelectTaskIndexSidebar
from ...library.user_context import UserContextFull
from django.db.models import Q
from django.contrib.auth.decorators import login_required
import logging


logger = logging.getLogger(__name__)


# Create your views here.
@login_required
def move(request):
    logger.info('task index')

    logger.info('task problemlist auth OK')
    userContext = UserContextFull(request)
    logger.info(userContext)
    task_activity = VwSelectTaskIndexSidebar.objects.all().filter(Q(userid=userContext.id) | Q(userid=''))
    context_dict = {'sidebar': task_activity,'usercontext': userContext}
    return render(request, "simpris/task/tasklist.html", context_dict)